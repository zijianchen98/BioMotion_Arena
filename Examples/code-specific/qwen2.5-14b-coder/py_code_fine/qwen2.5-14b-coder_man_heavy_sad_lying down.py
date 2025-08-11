
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Point light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_SPEED = 1.5

# Initial positions of the lights
lights = []
for i in range(NUM_LIGHTS):
    x = SCREEN_WIDTH // 2 + 100 * math.cos(2 * math.pi * i / NUM_LIGHTS)
    y = SCREEN_HEIGHT // 2 + 100 * math.sin(2 * math.pi * i / NUM_LIGHTS)
    lights.append([x, y])

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update light positions
    for i in range(NUM_LIGHTS):
        angle = 2 * math.pi * i / NUM_LIGHTS
        x = SCREEN_WIDTH // 2 + 100 * math.cos(angle + LIGHT_SPEED * pygame.time.get_ticks() / 1000)
        y = SCREEN_HEIGHT // 2 + 100 * math.sin(angle + LIGHT_SPEED * pygame.time.get_ticks() / 1000)
        lights[i] = [x, y]

    # Draw the background
    screen.fill(BLACK)

    # Draw the lights
    for light in lights:
        pygame.draw.circle(screen, WHITE, (int(light[0]), int(light[1])), LIGHT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
