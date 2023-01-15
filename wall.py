import pygame
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
class Wall2:
    def __init__(self):
        self.x = 1
        self.wall_list = []
        self.lv_mass = [
            ['*', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['*', '-', '-', '*', '-', '*', '-', '*', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '*', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['*', '-', '-', '-', '*', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['*', '-', '-', '*', '*', '*', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '*', '-', '-', '-', '*', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '*', '-', '-', '-', '*', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
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