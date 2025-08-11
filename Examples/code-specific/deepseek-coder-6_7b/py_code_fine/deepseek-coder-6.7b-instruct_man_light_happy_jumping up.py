
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
LIGHT_RADIUS = 5
LIGHT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a list to hold the light objects
lights = []

# Create the lights
for _ in range(15):
    x = random.randint(LIGHT_RADIUS, WIDTH - LIGHT_RADIUS)
    y = random.randint(HEIGHT + LIGHT_RADIUS, HEIGHT + 2 * LIGHT_RADIUS)
    light = pygame.rect.Rect(x - LIGHT_RADIUS, y - LIGHT_RADIUS, 2 * LIGHT_RADIUS, 2 * LIGHT_RADIUS)
    lights.append(light)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Update the positions of the lights
    for light in lights:
        light.move_ip(0, -1)
        if light.top < 0:
            light.bottom = HEIGHT

    # Draw the lights
    for light in lights:
        pygame.draw.ellipse(screen, LIGHT_COLOR, light)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
