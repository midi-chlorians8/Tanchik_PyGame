import pygame

pygame.init()

#screen = pygame.display.set_mode((1280,720))
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

class Wall:
    def __init__(self, start_pos_x, start_pos_y, count, dir):
        self.x = start_pos_x
        self.y = start_pos_y
        self.count = count
        self.dir = dir

    def draw(self):
        # Object Wall
        color_wall = (200, 200, 100)  # Color body tank
        pygame.draw.rect(screen, color_wall, pygame.Rect(30 + self.x, 30 + self.y, 60, 30))

wall = Wall(0,0,2,"hor")

class MyTank:
    def __init__(self, start_pos_x, start_pos_y):
        self.x = start_pos_x
        self.y = start_pos_y

        self.up = True  # direction
        self.down = False
        self.right = False
        self.left = False

        self.stop = False
    def input_keys(self):

        speed = 3  # speed move
        # print("Hello my name is " + self.name)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= speed
            if self.x < 0:
                self.x = 0
            self.right = False
            self.left = True
            self.up = False
            self.down = False

        if keys[pygame.K_RIGHT]:
            self.x += speed

            self.right = True
            self.left = False
            self.up = False
            self.down = False

        if keys[pygame.K_UP]:
            if self.stop == False:
                self.y -= speed

            if self.y < 0:
                self.y = 0

            self.up = True
            self.down = False
            self.right = False
            self.left = False

        if keys[pygame.K_DOWN]:
            self.y += speed

            self.up = False
            self.down = True
            self.right = False
            self.left = False
        print(f"Tank coord x= {self.x} y= {self.y}")
        # return up,down,right,left



    def draw(self):
        # Object Tank
        color = (255, 0, 0)  # Color body tank
        tannchik_body = pygame.draw.rect(screen, color, pygame.Rect(30 + self.x, 30 + self.y, 60, 60))



        color = (255, 100, 0)  # Color weapon
        if self.up:
            tannchik_weapon = pygame.draw.rect(screen, color, pygame.Rect(50+self.x, 10+self.y, 20, 20))
        if self.down:
            tannchik_weapon = pygame.draw.rect(screen, color, pygame.Rect(50+self.x, 90 + self.y, 20, 20))
        if self.right:
            tannchik_weapon = pygame.draw.rect(screen, color, pygame.Rect(90 + self.x, 50 + self.y, 20, 20))
        if self.left:
            tannchik_weapon = pygame.draw.rect(screen, color, pygame.Rect(10 + self.x, 50 + self.y, 20, 20))

        color_wall = (200, 200, 100)  # Color body tank
        wal1 = pygame.draw.rect(screen, color_wall, pygame.Rect(0 + 20, 0 + 20, 60, 30))
        if tannchik_weapon.colliderect(wal1):  # сюда над завести стену
            print("tank+wall")
            self.stop = True
        else:
            self.stop = False



tank = MyTank(start_pos_x = 100, start_pos_y = 400)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("black")  # Fill the display with a solid color

#    wall.draw()

    tank.input_keys()
    tank.draw()


    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)