import pygame

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
class Bullet:
    def __init__(self):
         #pygame.draw.rect(screen, 0,                             pygame.Rect(-10000 , -1000, 5, 2))
        self.x = 1
        self.y = 1

        self.faerrr = False
        self.dir = "down"

        self.bullet_list = []
        self.counter = 0
        self.one_plus = False # Чтоб счетчик нажатий выстрелов корректно прирастал

#чтоб несколько пуль влетали
        # bullet up vars
        self.my_x1_up = 10000
        self.my_y1_up = 0

        self.my_x2_up = 10000
        self.my_y2_up = 0

        self.my_x3_up = 10000
        self.my_y3_up = 0

        self.my_x4_up = 10000
        self.my_y4_up = 0
        # bullet up vars

        # bullet down vars
        self.my_x1_down = 10000
        self.my_y1_down = 10000

        self.my_x2_down = 10000
        self.my_y2_down = 10000

        self.my_x3_down = 10000
        self.my_y3_down = 10000

        self.my_x4_down = 10000
        self.my_y4_down = 10000
        # bullet down vars

        # bullet left vars
        self.my_x1_left = 10000
        self.my_y1_left = 10000

        self.my_x2_left = 10000
        self.my_y2_left = 10000

        self.my_x3_left = 10000
        self.my_y3_left = 10000

        self.my_x4_left = 10000
        self.my_y4_left = 10000
         # bullet left vars

         # bullet right vars
        self.my_x1_right = 10000
        self.my_y1_right = 10000

        self.my_x2_right = 10000
        self.my_y2_right = 10000

        self.my_x3_right = 10000
        self.my_y3_right = 10000

        self.my_x4_right = 10000
        self.my_y4_right = 10000
         # bullet left vars

        self.my_x = 0
        self.my_y = 0

        self.bool_up = False
        self.up_counter = 1
        self.down_counter = 1
        self.left_counter = 1
        self.right_counter = 1

        self.bullet_rect0up = None
        self.bullet_rect1up = None
        self.bullet_rect2up = None
        self.bullet_rect3up = None

        self.bullet_rect0down = None
        self.bullet_rect1down = None
        self.bullet_rect2down = None
        self.bullet_rect3down = None

        self.bullet_rect0left = None
        self.bullet_rect1left = None
        self.bullet_rect2left = None
        self.bullet_rect3left = None

        self.bullet_rect0right = None
        self.bullet_rect1right = None
        self.bullet_rect2right = None
        self.bullet_rect3right = None
    def set_zapusk(self, faer, tank_coords):
        self.faerrr = faer
        self.dir = tank_coords[2]

        if self.faerrr == False: # Если не стреляем
            self.one_plus = False
            # ============= ставим стартовые коорды пули в зависимости от направления танка
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
        else:
            self.faerrr = False # Мол мы поняли что был сигнал на выстрел
            if self.one_plus == False:
                self.counter += 1 # Урутим счет выстрелов
                self.one_plus = True
        # print(self.counter)
    def get_bullet_state(self):
        return self.faerrr


    def draw(self):
        color_wall = (200, 200, 100)  # Color bullet

        if self.counter == 1 and self.dir == "up":
            self.my_x1_up = self.x
            self.my_y1_up = self.y

            self.up_counter = self.counter

            self.counter +=1 # Сч>тчик вылетивших пуль

        if self.counter == 3 and self.dir == "up":
            self.my_x2_up = self.x
            self.my_y2_up = self.y

            self.counter +=1

        if self.counter == 5 and self.dir == "up":
            self.my_x3_up = self.x
            self.my_y3_up = self.y

            self.counter += 1

        if self.counter == 7 and self.dir == "up":
            self.my_x4_up = self.x
            self.my_y4_up = self.y

            self.counter += 1



        if self.counter == 1 and self.dir == "down":
            self.my_x1_down = self.x
            self.my_y1_down = self.y
            self.counter +=1
            self.down_counter = self.counter

        if self.counter == 3 and self.dir == "down":
            self.my_x2_down = self.x
            self.my_y2_down = self.y
            self.counter +=1

        if self.counter == 5 and self.dir == "down":
            self.my_x3_down = self.x
            self.my_y3_down = self.y
            self.counter +=1


        if self.counter == 7 and self.dir == "down":
            self.my_x4_down = self.x
            self.my_y4_down = self.y
            self.counter +=1

        if self.counter == 1 and self.dir == "left":
            self.my_x1_left = self.x
            self.my_y1_left = self.y
            self.counter +=1
            self.left_counter = self.counter

        if self.counter == 3 and self.dir == "left":
            self.my_x2_left = self.x
            self.my_y2_left = self.y
            self.counter +=1

        if self.counter == 5 and self.dir == "left":
            self.my_x3_left = self.x
            self.my_y3_left = self.y
            self.counter +=1

        if self.counter == 7 and self.dir == "left":
            self.my_x4_left = self.x
            self.my_y4_left = self.y
            self.counter +=1

    #
        if self.counter == 1 and self.dir == "right":
            self.my_x1_right = self.x
            self.my_y1_right = self.y
            self.counter +=1
            self.right_counter = self.counter

        if self.counter == 3 and self.dir == "right":
            self.my_x2_right = self.x
            self.my_y2_right = self.y
            self.counter +=1

        if self.counter == 5 and self.dir == "right":
            self.my_x3_right = self.x
            self.my_y3_right = self.y
            self.counter +=1

        if self.counter == 7 and self.dir == "right":
            self.my_x4_right = self.x
            self.my_y4_right = self.y
            self.counter +=1

        if self.counter == 8: # Сч>тчик вылетивших пуль
            self.counter = 0

        up_mass = [
            [self.my_x1_up, self.my_y1_up],
            [self.my_x2_up, self.my_y2_up],
            [self.my_x3_up, self.my_y3_up],
            [self.my_x4_up, self.my_y4_up]
        ]
        if self.up_counter > 0: #self.dir == "up":
            iter = 0
            for coord in up_mass:
                # print(iter, coord)
                if iter == 0:
                    self.bullet_rect0up = pygame.draw.rect(screen, color_wall,
                                      pygame.Rect(coord[0] , coord[1], 2, 5))
                if iter == 1:
                    self.bullet_rect1up = pygame.draw.rect(screen, color_wall,
                                      pygame.Rect(coord[0] , coord[1], 2, 5))
                if iter == 2:
                    self.bullet_rect2up = pygame.draw.rect(screen, color_wall,
                                      pygame.Rect(coord[0] , coord[1], 2, 5))
                if iter == 3:
                    self.bullet_rect3up = pygame.draw.rect(screen, color_wall,
                                      pygame.Rect(coord[0] , coord[1], 2, 5))
                iter += 1


            self.my_y1_up -= 2
            self.my_y2_up -= 2
            self.my_y3_up -= 2
            self.my_y4_up -= 2



        down_mass = [
            [self.my_x1_down, self.my_y1_down],
            [self.my_x2_down, self.my_y2_down],
            [self.my_x3_down, self.my_y3_down],
            [self.my_x4_down, self.my_y4_down]
        ]
        if self.down_counter > 0: #: == "down":
            iter = 0
            for coord in down_mass:
                if iter == 0:
                    self.bullet_rect0down = pygame.draw.rect(screen, color_wall,
                                                         pygame.Rect(coord[0], coord[1], 2, 5))
                if iter == 1:
                    self.bullet_rect1down = pygame.draw.rect(screen, color_wall,
                                                         pygame.Rect(coord[0], coord[1], 2, 5))
                if iter == 2:
                    self.bullet_rect2down = pygame.draw.rect(screen, color_wall,
                                                         pygame.Rect(coord[0], coord[1], 2, 5))
                if iter == 3:
                    self.bullet_rect3down = pygame.draw.rect(screen, color_wall,
                                                         pygame.Rect(coord[0], coord[1], 2, 5))
                iter += 1
            # pygame.draw.rect(screen, color_wall,
            #                  pygame.Rect(self.my_x1_down , self.my_y1_down, 2, 5))
            # pygame.draw.rect(screen, color_wall,
            #                  pygame.Rect(self.my_x2_down, self.my_y2_down, 2, 5))
            self.my_y1_down += 20
            self.my_y2_down += 20
            self.my_y3_down += 20
            self.my_y4_down += 20

        left_mass = [
            [self.my_x1_left, self.my_y1_left],
            [self.my_x2_left, self.my_y2_left],
            [self.my_x3_left, self.my_y3_left],
            [self.my_x4_left, self.my_y4_left]
        ]
        if self.left_counter > 0:
            iter = 0
            for coord in left_mass:
                if iter == 0:
                    self.bullet_rect0left = pygame.draw.rect(screen, color_wall,
                                                         pygame.Rect(coord[0], coord[1], 5, 2))
                if iter == 1:
                    self.bullet_rect1left = pygame.draw.rect(screen, color_wall,
                                                         pygame.Rect(coord[0], coord[1], 5, 2))
                if iter == 2:
                    self.bullet_rect2left = pygame.draw.rect(screen, color_wall,
                                                         pygame.Rect(coord[0], coord[1], 5, 2))
                if iter == 3:
                    self.bullet_rect3left = pygame.draw.rect(screen, color_wall,
                                                         pygame.Rect(coord[0], coord[1], 5, 2))
                iter += 1
            self.my_x1_left -= 20
            self.my_x2_left -= 20
            self.my_x3_left -= 20
            self.my_x4_left -= 20


        right_mass = [
            [self.my_x1_right, self.my_y1_right],
            [self.my_x2_right, self.my_y2_right],
            [self.my_x3_right, self.my_y3_right],
            [self.my_x4_right, self.my_y4_right]
        ]
        if self.right_counter > 0:
            iter = 0
            for coord in right_mass:
                if iter == 0:
                    self.bullet_rect0right = pygame.draw.rect(screen, color_wall,
                                                             pygame.Rect(coord[0], coord[1], 5, 2))
                if iter == 1:
                    self.bullet_rect1right = pygame.draw.rect(screen, color_wall,
                                                             pygame.Rect(coord[0], coord[1], 5, 2))
                if iter == 2:
                    self.bullet_rect2right = pygame.draw.rect(screen, color_wall,
                                                             pygame.Rect(coord[0], coord[1], 5, 2))
                if iter == 3:
                    self.bullet_rect3right = pygame.draw.rect(screen, color_wall,
                                                             pygame.Rect(coord[0], coord[1], 5, 2))
                iter += 1
            self.my_x1_right += 20
            self.my_x2_right += 20
            self.my_x3_right += 20
            self.my_x4_right += 20


    def detecting_collision(self,wall_mass):
        # ==================================== Обработка столкновений ==================================
        for wall in wall_mass:
            # print(wall, self.bullet_rect0, self.counter, self.up_counter)

            # up detect and move bullet
            if self.bullet_rect0up.colliderect(wall):
                print(wall, self.bullet_rect0up)
                print("STOP bullet 0 up")
                self.my_x1_up = 10000

            if self.bullet_rect1up.colliderect(wall):
                print(wall, self.bullet_rect1up)
                print("STOP bullet 1 up")
                self.my_x2_up = 10000

            if self.bullet_rect2up.colliderect(wall):
                print(wall, self.bullet_rect2up)
                print("STOP bullet 2")
                self.my_x3_up = 10000

            if self.bullet_rect3up.colliderect(wall):
                print(wall, self.bullet_rect3up)
                print("STOP bullet 3 up")
                self.my_x4_up = 10000
            # up detect and move bullet

            # down detect and move bullet
            if self.bullet_rect0down.colliderect(wall):
                print(wall, self.bullet_rect0down)
                print("STOP bullet 0 down")
                self.my_x1_down = 10000

            if self.bullet_rect1down.colliderect(wall):
                print(wall, self.bullet_rect1down)
                print("STOP bullet 1 down")
                self.my_x2_down = 10000

            if self.bullet_rect2down.colliderect(wall):
                # pass
                print(wall, self.bullet_rect2down)
                print("STOP bullet 2 down")
                self.my_x3_down = 10000

            if self.bullet_rect3down.colliderect(wall):
                print(wall, self.bullet_rect3down)
                print("STOP bullet 3 down")
                self.my_x4_down = 10000
            # down detect and move bullet

            # left detect and move bullet
            if self.bullet_rect0left.colliderect(wall):
                print(wall, self.bullet_rect0left)
                print("STOP bullet 0 left")
                self.my_x1_left = -10000

            if self.bullet_rect1left.colliderect(wall):
                print(wall, self.bullet_rect1left)
                print("STOP bullet 1 left")
                self.my_x2_left = -10000

            if self.bullet_rect2left.colliderect(wall):
                print(wall, self.bullet_rect2left)
                print("STOP bullet 2 left")
                self.my_x3_left = -10000

            if self.bullet_rect3left.colliderect(wall):
                print(wall, self.bullet_rect3left)
                print("STOP bullet 3 left")
                self.my_x4_left = -10000
            # left detect and move bullet

            # right detect and move bullet
            if self.bullet_rect0right.colliderect(wall):
                print(wall, self.bullet_rect0right)
                print("STOP bullet 0 right")
                self.my_x1_right = -10000

            if self.bullet_rect1right.colliderect(wall):
                print(wall, self.bullet_rect1right)
                print("STOP bullet 1 right")
                self.my_x2_right = -10000

            if self.bullet_rect2right.colliderect(wall):
                print(wall, self.bullet_rect2right)
                print("STOP bullet 2 right")
                self.my_x3_right = -10000

            if self.bullet_rect3right.colliderect(wall):
                print(wall, self.bullet_rect3right)
                print("STOP bullet 3 right")
                self.my_x4_right = -10000
            # left detect and move bullet