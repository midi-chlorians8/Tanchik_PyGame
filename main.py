import pygame

pygame.init()

#screen = pygame.display.set_mode((1280,720))
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

x = 0 #hor pos
y = 0 #vert position
speed = 1 #speed move

up = True #direction
down = False
right = False
left = False

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed

        right = False
        left = True
        up = False
        down = False

    if keys[pygame.K_RIGHT]:
        x += speed

        right = True
        left = False
        up = False
        down = False

    if keys[pygame.K_UP]:
        y -= speed

        up = True
        down = False
        right = False
        left = False

    if keys[pygame.K_DOWN]:
        y += speed

        up = False
        down = True
        right = False
        left = False
    print(f"Tank coord x= {x} y= {y}")
    # Render the graphics here.
    # ...


    screen.fill("black")  # Fill the display with a solid color


    # Object Tank
    color = (255, 0, 0)  # Color body tank
    pygame.draw.rect(screen, color, pygame.Rect(30+x, 30+y, 60, 60))
    color = (255, 100, 0)  #  Color weapon

    if up:
        pygame.draw.rect(screen, color, pygame.Rect(50+x, 10+y, 20, 20))
    if down:
        pygame.draw.rect(screen, color, pygame.Rect(50+x, 90 + y, 20, 20))
    if right:
        pygame.draw.rect(screen, color, pygame.Rect(90 + x, 50 + y, 20, 20))
    if left:
        pygame.draw.rect(screen, color, pygame.Rect(10 + x, 50 + y, 20, 20))

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)