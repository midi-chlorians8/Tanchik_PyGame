import pygame

pygame.init()

# screen = pygame.display.set_mode((1280,720))
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


# class Wall:
#     def __init__(self, start_pos_x, start_pos_y, count, dir):
#         self.x = start_pos_x
#         self.y = start_pos_y
#         self.count = count
#         self.dir = dir
#
#     def draw(self):
#         # Object Wall
#         color_wall = (200, 200, 100)  # Color body tank
#         pygame.draw.rect(screen, color_wall, pygame.Rect(30 + self.x, 30 + self.y, 60, 30))
#
# wall = Wall(0,0,2,"hor")
class Wall2:
    def __init__(self):
        self.x = 1
        self.wall_list = []

    def draw(self):
        # Object Wall
        color_wall = (200, 200, 100)  # Color body
        w1 = pygame.draw.rect(screen, color_wall, pygame.Rect(0 + 200, 0 + 160, 160, 30))
        w2 = pygame.draw.rect(screen, color_wall, pygame.Rect(120, 300, 60, 30))

        self.wall_list = [w1, w2]

    def getwallslist(self):
        return self.wall_list


walls = Wall2()


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

    def input_keys(self):

        speed = 3  # speed move
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

            if self.x < 0:
                self.x = 0

            self.right = False
            self.left = True
            self.up = False
            self.down = False

            # self.reloadWallDirection = False

        elif keys[pygame.K_RIGHT]:
            if self.stopRight == False:
                self.x += speed

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

            if self.y < 0:
                self.y = 0

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
            # if self.last_dir != 'down':
            #     self.stop = False

            self.up = False
            self.down = True
            self.right = False
            self.left = False

        print(f"Tank coord x= {self.x} y= {self.y}, last_dir={self.last_dir}, "
              f"stopLeft = {self.stopLeft}, stopUp = {self.stopUp}, stopRight = {self.stopRight}",
              f"self.left = {self.left}")

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



        # ==================================== Обработка столкновений ==================================
        if (tannchik_weapon.colliderect(walls.getwallslist()[0]) or tannchik_body.colliderect(
                walls.getwallslist()[0] )) and self.up == True:  # сюда над завести стену
            self.stopUp = True
            self.y = self.y + 1  # If tank inside wall - move back

        elif (tannchik_weapon.colliderect(walls.getwallslist()[0]) or tannchik_body.colliderect(
                walls.getwallslist()[0])) and self.down == True:  # сюда над завести стену
            self.stopDown = True
            self.y = self.y - 1  # If tank inside wall - move back

        elif (tannchik_weapon.colliderect(walls.getwallslist()[0]) or tannchik_body.colliderect(
                walls.getwallslist()[0])) and self.left == True:  # сюда над завести стену
            self.stopLeft = True
            self.x = self.x + 1  # If tank inside wall - move back

        elif (tannchik_weapon.colliderect(walls.getwallslist()[0]) or tannchik_body.colliderect(
                walls.getwallslist()[0])) and self.right == True:  # сюда над завести стену
            self.stopRight = True
            self.x = self.x - 1  # If tank inside wall - move back

        # double code from second wall
        if (tannchik_weapon.colliderect(walls.getwallslist()[1]) or tannchik_body.colliderect(
                walls.getwallslist()[1] )) and self.up == True:  # сюда над завести стену
            self.stopUp = True
            self.y = self.y + 1  # If tank inside wall - move back

        elif (tannchik_weapon.colliderect(walls.getwallslist()[1]) or tannchik_body.colliderect(
                walls.getwallslist()[1])) and self.down == True:  # сюда над завести стену
            self.stopDown = True
            self.y = self.y - 1  # If tank inside wall - move back

        elif (tannchik_weapon.colliderect(walls.getwallslist()[1]) or tannchik_body.colliderect(
                walls.getwallslist()[1])) and self.left == True:  # сюда над завести стену
            self.stopLeft = True
            self.x = self.x + 1  # If tank inside wall - move back

        elif (tannchik_weapon.colliderect(walls.getwallslist()[1]) or tannchik_body.colliderect(
                walls.getwallslist()[1])) and self.right == True:  # сюда над завести стену
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


tank = MyTank(start_pos_x=100, start_pos_y=400)

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

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)  # wait until next frame (at 60 FPS)
