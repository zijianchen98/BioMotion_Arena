
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
light_x, light_y = 0, HEIGHT // 2
light_color = (255, 255, 255)
light_radius = 5

def draw_light():
    pygame.draw.circle(screen, light_color, (light_x, light_y), light_radius)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the point light
    draw_light()

    # Update the display
    pygame.display.flip()

    # Move the point light
    light_x += 1
    if light_x > WIDTH:
        light_x = 0

    # Delay to control the frame rate
    clock.tick(FPS)
