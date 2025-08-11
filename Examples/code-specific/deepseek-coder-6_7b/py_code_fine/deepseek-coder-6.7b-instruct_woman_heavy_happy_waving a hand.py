
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
LIGHT_COUNT = 15
LIGHT_RADIUS = 5

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the lights
lights = []
for i in range(LIGHT_COUNT):
    x = i * (WIDTH // LIGHT_COUNT)
    light = pygame.draw.circle(screen, (255, 255, 255), (x, HEIGHT // 2), LIGHT_RADIUS)
    lights.append(light)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the lights
    for i, light in enumerate(lights):
        x = (light.left + (WIDTH // LIGHT_COUNT) * (i + 1)) % WIDTH
        pygame.draw.circle(screen, (0, 0, 0), light.topleft, LIGHT_RADIUS)
        light = pygame.draw.circle(screen, (255, 255, 255), (x, HEIGHT // 2), LIGHT_RADIUS)
        lights[i] = light

    # Update the display
    pygame.display.flip()
