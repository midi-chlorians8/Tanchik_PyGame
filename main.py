import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

from bullet import *
bullet = Bullet()



from wall import *
walls = Wall2()

class Enemy:
    def __init__(self):
        self.level = 1
        self.enemy_count = 1

        self.spawn_coords_mass = [[300,200],[200,100]]
        #print(self.spawn_coords_mass[0][0])
        #self.spawn_coords_x = 300
        #self.spawn_coords_y = 200

        self.directions_mass = [{"up":False,"down":False,"right":True,"left":False},{"up":False,"down":False,"right":True,"left":False}]
        #print(self.directions_mass[0]["right"])
        # self.up = False  # directions
        # self.down = False
        # self.right = True
        # self.left = False

        self.touch_to_new_dir = False
        self.touch_counter = 0
    def logic(self, level):
        self.level = level

        #print(self.spawn_coords_mass[0][0])
        if self.level == 1:
            self.enemy_count = 2

# Обработка движения взависимости от направления:
#         for enemy in range(self.enemy_count):
#             print(enemy)

        if self.directions_mass[0]["right"] == True: #self.right == True:
            self.spawn_coords_mass[0][0] +=4

        if self.directions_mass[0]["left"] == True: #self.right == True:
            self.spawn_coords_mass[0][0] -=4

        if self.directions_mass[0]["up"] == True: #self.right == True:
            self.spawn_coords_mass[0][1] -=4

        if self.directions_mass[0]["down"] == True: #self.right == True:
            self.spawn_coords_mass[0][1] +=4

# Обработка движения взависимости от направления:


#Если выходим за пределы уровня. Обработка врага №0:
        if self.spawn_coords_mass[0][0] > width - 130:
            self.directions_mass[0]["right"] = False
            lastdir = "right"

            self.touch_to_new_dir = True
            self.spawn_coords_mass[0][0] = width - 130 # отходим назад чтоб один раз спокойно выбрать новое направление движения
        #
        elif self.spawn_coords_mass[0][0] < 0 :
            self.directions_mass[0]["left"] = False
            lastdir = "left"

            self.touch_to_new_dir = True
            self.spawn_coords_mass[0][0] = 0 # отходим назад чтоб один раз спокойно выбрать новое направление движения

        elif self.spawn_coords_mass[0][1] < 0 :
            self.directions_mass[0]["up"] = False
            lastdir = "up"

            self.touch_to_new_dir = True
            self.spawn_coords_mass[0][1] = 0 # отходим назад чтоб один раз спокойно выбрать новое направление движения

        elif self.spawn_coords_mass[0][1] > height -120:
            self.directions_mass[0]["down"] = False
            lastdir = "down"

            self.touch_to_new_dir = True
            self.spawn_coords_mass[0][1] = height -120 # отходим назад чтоб один раз спокойно выбрать новое направление движения

# Если выходим за пределы уровня. Обработка врага №0:

        if self.touch_to_new_dir == True: # коснулись чего-то и меняем направление
            self.rand(lastdir)
            new_dir = self.rand(lastdir)
            print(new_dir)
            if new_dir == 'up':
                self.directions_mass[0]["up"] = True
            elif new_dir == 'down':
                self.directions_mass[0]["down"] = True
            elif new_dir == 'right':
                self.directions_mass[0]["right"] = True
            elif new_dir == 'left':
                self.directions_mass[0]["left"] = True

            #print(self.spawn_coords_mass[0][0])

            self.touch_to_new_dir = False


    def rand(self, lastdir_income):
        #print(lastdir_income)
        dir_list = ['up', 'down', 'right','left']

        index = -1
        for element in dir_list: # Удаляем из списка всех направлений то где мы уже были
            #print(element)
            index += 1
            if element == lastdir_income:
                del dir_list[index]

        res = random.choice(dir_list)
        return res


    def draw(self):
        color = (95, 140, 130)  # Color body tank
        tannchik_body = pygame.draw.rect(screen, color, pygame.Rect(30 + self.spawn_coords_mass[0][0], 30 + self.spawn_coords_mass[0][1], 60, 60))

        # draw tank weapon depend button up down right left
        color = (255, 100, 0)  # Color weapon
        if self.directions_mass[0]["up"] == True:#self.up:
            tannchik_weapon = pygame.draw.rect(screen, color, pygame.Rect(50 + self.spawn_coords_mass[0][0], 10 + self.spawn_coords_mass[0][1], 20, 20))
        if self.directions_mass[0]["down"] == True:#self.down:
            tannchik_weapon = pygame.draw.rect(screen, color, pygame.Rect(50 + self.spawn_coords_mass[0][0], 90 + self.spawn_coords_mass[0][1], 20, 20))
        if self.directions_mass[0]["right"] == True:#self.right:
            tannchik_weapon = pygame.draw.rect(screen, color, pygame.Rect(90 + self.spawn_coords_mass[0][0], 50 + self.spawn_coords_mass[0][1], 20, 20))
        if self.directions_mass[0]["left"] == True: #self.left:
            tannchik_weapon = pygame.draw.rect(screen, color, pygame.Rect(10 + self.spawn_coords_mass[0][0], 50 + self.spawn_coords_mass[0][1], 20, 20))
        # draw tank weapon depend button up down right left
enemies = Enemy()
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


            if self.x > width-120:
                self.x = width -110

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

            if self.y > height -110:
                self.y = height -110

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

    enemies.logic(level=1)
    enemies.draw()

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)  # wait until next frame (at 60 FPS)
