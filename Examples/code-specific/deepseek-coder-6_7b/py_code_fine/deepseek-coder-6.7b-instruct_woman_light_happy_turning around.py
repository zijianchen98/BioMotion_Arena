
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 800
LIGHT_RADIUS = 10
LIGHT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
NUM_LIGHTS = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the lights
lights = []
for i in range(NUM_LIGHTS):
    x = WIDTH / 2 + math.cos(i * 2 * math.pi / NUM_LIGHTS) * (WIDTH / 2 - LIGHT_RADIUS)
    y = HEIGHT / 2 + math.sin(i * 2 * math.pi / NUM_LIGHTS) * (HEIGHT / 2 - LIGHT_RADIUS)
    lights.append((x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(BACKGROUND_COLOR)

    # Draw the lights
    for light in lights:
        pygame.draw.circle(screen, LIGHT_COLOR, (int(light[0]), int(light[1])), LIGHT_RADIUS)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
