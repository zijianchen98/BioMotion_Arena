
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
LIGHT_RADIUS = 10
LIGHT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the lights
lights = []
for i in range(15):
    x = i * (WIDTH // 15)
    light = pygame.draw.circle(screen, LIGHT_COLOR, (x, HEIGHT // 2), LIGHT_RADIUS)
    lights.append(light)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the lights
    for i, light in enumerate(lights):
        x = (light.left + (WIDTH // 15) * (i % 3)) % WIDTH
        pygame.draw.circle(screen, BACKGROUND_COLOR, light.center, LIGHT_RADIUS)
        light = pygame.draw.circle(screen, LIGHT_COLOR, (x, HEIGHT // 2), LIGHT_RADIUS)
        lights[i] = light

    # Update the display
    pygame.display.flip()
