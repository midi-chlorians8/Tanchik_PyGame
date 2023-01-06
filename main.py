import pygame

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


class Bullet:
    def __init__(self):
        self.x = 1
        self.y = 1

        self.faerrr = False
        self.dir = "down"

    def set_zapusk(self, faer, tank_coords):
        self.faerrr = faer
        self.dir = tank_coords[2]

        if self.faerrr == False:
            if self.dir == "up":
                self.y = tank_coords[1] + 5
                self.x = tank_coords[0] + 60
            elif self.dir == "down":
                self.y = tank_coords[1] + 110
                self.x = tank_coords[0] + 60
            elif self.dir == "left":
                self.y = tank_coords[1] + 60
                self.x = tank_coords[0] + 5
            elif self.dir == "right":
                self.y = tank_coords[1] + 60
                self.x = tank_coords[0] + 110

    def draw(self):
        # self.y = tank_coords[1] + 5
        # if self.faerrr == True:
        color_wall = (200, 200, 100)  # Color bullet

        if self.dir == "up":
            pygame.draw.rect(screen, color_wall,
                             pygame.Rect(self.x , self.y, 2, 5))
            self.y -= 20
            print(self.y)

        if self.dir == "down":
            pygame.draw.rect(screen, color_wall,
                             pygame.Rect(self.x , self.y, 2, 5))
            self.y += 20

        if self.dir == "left":
            pygame.draw.rect(screen, color_wall,
                             pygame.Rect(self.x , self.y, 5, 2))
            self.x -= 20

        if self.dir == "right":
            pygame.draw.rect(screen, color_wall,
                             pygame.Rect(self.x , self.y, 5, 2))
            self.x += 20

bullet = Bullet()


class Wall2:
    def __init__(self):
        self.x = 1
        self.wall_list = []
        self.lv_mass = [
            ['*', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['*', '-', '-', '*', '-', '*', '-', '-', '-'],
            ['-', '-', '-', '-', '*', '-', '-', '-', '-'],
            ['*', '-', '-', '-', '*', '-', '-', '-', '-'],
            ['-', '-', '*', '-', '-', '-', '*', '-', '-'],
            ['*', '-', '-', '*', '*', '*', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        ]

    def draw(self):
        s = 0
        box_height_res = 0
        box_height = 0

        box_width = 0
        for row in self.lv_mass:
            box_height_res += 1
            for elem in row:
                # s += elem
                box_width_res = len(row)
        box_width = width / (box_width_res)  # ширина куба стенки = ширина экрана / кол-во элментов по ширине
        box_height = height / box_height_res  # высота куба стенки

        # print(
        #     f", width ={width} "
        #     f" height= {height} "
        #
        #     f", box_height_res={box_height_res} "
        #     f", box_width_res ={box_width_res} "
        #
        #     f", box_width ={box_width} "
        #     f" box_height= {box_height}"
        #       )
        t = []  #
        counter_ver = -1
        color_wall = (200, 200, 100)  # Color wall
        for row in self.lv_mass:
            counter_hor = -1
            counter_ver += 1
            for elem in row:
                counter_hor += 1
                if elem == '*':
                    obj = pygame.draw.rect(screen, color_wall,
                                           pygame.Rect(counter_hor * box_width, counter_ver * box_height, box_width,
                                                       box_height))
                    t.append(obj)
        # Object Wall list

        self.wall_list = t  # [w1, w2]
        # print(self.wall_list)

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

        self.trigger_state = False

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

            self.up = False
            self.down = True
            self.right = False
            self.left = False

        elif keys[pygame.K_SPACE]:
            print("AAAAA")
            self.trigger_state = True

        print(f"Tank coord x= {self.x} y= {self.y}"
              # f", last_dir={self.last_dir}, "
              # f"stopLeft = {self.stopLeft}, stopUp = {self.stopUp}, stopRight = {self.stopRight}",
              # f"self.left = {self.left}"
              )

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

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)  # wait until next frame (at 60 FPS)
