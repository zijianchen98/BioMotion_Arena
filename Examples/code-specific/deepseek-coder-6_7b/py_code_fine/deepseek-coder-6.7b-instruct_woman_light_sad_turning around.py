
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
light_color = (255, 255, 255)

def draw_point_light():
    pygame.draw.rect(screen, light_color, point_light)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Move and draw the point light
    point_light.move_ip(2, 0)
    if point_light.right > WIDTH:
        point_light.left = 0
    draw_point_light()

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
