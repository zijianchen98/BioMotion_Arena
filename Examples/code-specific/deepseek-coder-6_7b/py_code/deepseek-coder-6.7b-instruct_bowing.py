
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Set up the point light
point_light = pygame.rect.Rect((0, 0, 10, 10))

def draw_point_light():
    pygame.draw.rect(screen, (255, 255, 255), point_light)

def move_point_light():
    point_light.move_ip(1, 0)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    move_point_light()
    draw_point_light()
    pygame.display.flip()
    clock.tick(FPS)
