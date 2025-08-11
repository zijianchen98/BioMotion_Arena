
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
LIGHT_RADIUS = 5
LIGHT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
NUM_LIGHTS = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a list to hold the light objects
lights = []

# Create the light objects
for _ in range(NUM_LIGHTS):
    x = random.randint(LIGHT_RADIUS, WIDTH - LIGHT_RADIUS)
    y = random.randint(LIGHT_RADIUS, HEIGHT - LIGHT_RADIUS)
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    light = pygame.draw.circle(screen, LIGHT_COLOR, (x, y), LIGHT_RADIUS)
    lights.append((light, dx, dy))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Update the positions of the lights
    for light, dx, dy in lights:
        x, y = light.center
        x += dx
        y += dy
        if x - LIGHT_RADIUS < 0 or x + LIGHT_RADIUS > WIDTH:
            dx = -dx
        if y - LIGHT_RADIUS < 0 or y + LIGHT_RADIUS > HEIGHT:
            dy = -dy
        pygame.draw.circle(screen, LIGHT_COLOR, (x, y), LIGHT_RADIUS)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
