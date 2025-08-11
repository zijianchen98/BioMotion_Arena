
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
    y = HEIGHT // 2
    light = pygame.rect.Rect(x, y, LIGHT_RADIUS, LIGHT_RADIUS)
    lights.append(light)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the lights
    for light in lights:
        pygame.draw.rect(screen, (255, 255, 255), light)

    # Move the lights
    for i, light in enumerate(lights):
        light.x = (i * (WIDTH // LIGHT_COUNT)) % (WIDTH - LIGHT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Delay to control the animation speed
    pygame.time.delay(100)
