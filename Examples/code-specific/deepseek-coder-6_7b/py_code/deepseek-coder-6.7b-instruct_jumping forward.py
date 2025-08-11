
import pygame
import pygame.gfxdraw

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Set up the point light
point_light = pygame.Rect(0, HEIGHT // 2, 10, 10)

def draw_point_light():
    pygame.draw.rect(win, (255, 255, 255), point_light)

def move_point_light():
    point_light.x += 1
    if point_light.x > WIDTH:
        point_light.x = 0

# Game loop
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    move_point_light()
    draw_point_light()
    pygame.display.update()

pygame.quit()
