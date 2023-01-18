import pygame



pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

from bullet import *
bullet = Bullet()



from wall import *
walls = Wall2()

class Enemy:
    def __init__(self, enemy_count):
        self.enemy_count = enemy_count

    def logic(self):
        pass

    def draw(self):
        pass

class MyTank:

    def __init__(self, start_pos_x, start_pos_y):
        self.x = start_pos_x
        self.y = start_pos_y

        self.up = True  # direction
        self.down = False
        self.right = False
        self.left = False

        self.stopUp = False
        self.stopDown = False
        self.stopLeft = False
        self.stopRight = False

        self.last_dir = 'up'

        self.trigger_state = False

    def input_keys(self):

        speed = 8  # speed move
        # print("Hello my name is " + self.name)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.stopLeft == False:
                self.x -= speed

            self.stopRight = False
            self.stopUp = False
            self.stopDown = False

            if self.last_dir != 'left':
                self.stop = False

            if self.x < -10:
                self.x = -9

            self.right = False
            self.left = True
            self.up = False
            self.down = False

            # self.reloadWallDirection = False

        elif keys[pygame.K_RIGHT]:
            if self.stopRight == False:
                self.x += speed


            if self.x > width-80:
                self.x = width -70

            self.stopLeft = False
            self.stopUp = False
            self.stopDown = False

            if self.last_dir != 'right':
                self.stop = False

            self.right = True
            self.left = False
            self.up = False
            self.down = False

        elif keys[pygame.K_UP]:
            if self.stopUp == False:
                self.y -= speed

            self.stopDown = False
            self.stopLeft = False
            self.stopRight = False

            if self.y < -10:
                self.y = -9

            self.up = True
            self.down = False
            self.right = False
            self.left = False

        elif keys[pygame.K_DOWN]:
            if self.stopDown == False:
                self.y += speed

            self.stopUp = False
            self.stopLeft = False
            self.stopRight = False

            self.up = False
            self.down = True
            self.right = False
            self.left = False

        elif keys[pygame.K_SPACE]:
            # print("AAAAA")
            self.trigger_state = True

        # print(f"Tank coord x= {self.x} y= {self.y}"
        #       # f", last_dir={self.last_dir}, "
        #       # f"stopLeft = {self.stopLeft}, stopUp = {self.stopUp}, stopRight = {self.stopRight}",
        #       # f"self.left = {self.left}"
        #       )

    def set_pull_trigger(self, state):
        self.trigger_state = state

    def get_pull_trigger(self):
        return self.trigger_state

    def draw(self):
        # Object Tank
        color = (255, 0, 0)  # Color body tank
        tannchik_body = pygame.draw.rect(screen, color, pygame.Rect(30 + self.x, 30 + self.y, 60, 60))

        # draw tank weapon depend button up down right left
        color = (255, 100, 0)  # Color weapon
        if self.up:
            tannchik_weapon = pygame.draw.rect(screen, color, pygame.Rect(50 + self.x, 10 + self.y, 20, 20))
        if self.down:
            tannchik_weapon = pygame.draw.rect(screen, color, pygame.Rect(50 + self.x, 90 + self.y, 20, 20))
        if self.right:
            tannchik_weapon = pygame.draw.rect(screen, color, pygame.Rect(90 + self.x, 50 + self.y, 20, 20))
        if self.left:
            tannchik_weapon = pygame.draw.rect(screen, color, pygame.Rect(10 + self.x, 50 + self.y, 20, 20))
        # draw tank weapon depend button up down right left

        my_tank = [tannchik_body, tannchik_weapon]

        # ==================================== Обработка столкновений ==================================
        for wall in walls.getwallslist():
            for tank_part in my_tank:
                if (tank_part.colliderect(wall)) and self.up == True:  # сюда над завести стену
                    self.stopUp = True
                    self.y = self.y + 1  # If tank inside wall - move back

                elif (tank_part.colliderect(wall)) and self.down == True:  # сюда над завести стену
                    self.stopDown = True
                    self.y = self.y - 1  # If tank inside wall - move back

                elif (tank_part.colliderect(wall)) and self.left == True:  # сюда над завести стену
                    self.stopLeft = True
                    self.x = self.x + 1  # If tank inside wall - move back

                elif (tank_part.colliderect(wall)) and self.right == True:  # сюда над завести стену
                    self.stopRight = True
                    self.x = self.x - 1  # If tank inside wall - move back

        if self.left:
            self.last_dir = 'left'
        elif self.right:
            self.last_dir = 'right'
        elif self.down:
            self.last_dir = 'down'
        elif self.up:
            self.last_dir = 'up'

    def get_coords_dir(self):
        return self.x, self.y, self.last_dir


tank = MyTank(start_pos_x=500, start_pos_y=400)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("black")  # Fill the display with a solid color

    walls.draw()

    tank.draw()
    tank.input_keys()

    bullet.set_zapusk(tank.get_pull_trigger(), tank.get_coords_dir())
    bullet.draw()
    bullet.detecting_collision(walls.getwallslist())
    #print(walls.getwallslist())

    tank.set_pull_trigger(bullet.get_bullet_state() )

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)  # wait until next frame (at 60 FPS)
