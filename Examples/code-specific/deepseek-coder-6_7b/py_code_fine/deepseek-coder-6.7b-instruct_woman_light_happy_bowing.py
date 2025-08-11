
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
LIGHT_RADIUS = 5
LIGHT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the lights
lights = []
for i in range(15):
    x = i * (WIDTH // 15)
    lights.append(pygame.Rect(x, HEIGHT // 2, LIGHT_RADIUS, LIGHT_RADIUS))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the lights
    for light in lights:
        pygame.draw.rect(screen, LIGHT_COLOR, light)

    # Move the lights
    for i, light in enumerate(lights):
        light.x = (i * (WIDTH // 15)) % (WIDTH - LIGHT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(100)
