
import pygame
import sys
import math
import numpy as np

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Parameters for the happyman lying down
center_x, center_y = WIDTH // 2, HEIGHT // 2
radius = 100
num_lights = 15
lights = []

# Initialize lights in a circular pattern
for i in range(num_lights):
    angle = 2 * math.pi * i / num_lights
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    lights.append([x, y])

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Time variables for smooth animation
t = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update the positions of the lights to simulate lying down
    for i in range(num_lights):
        angle = 2 * math.pi * i / num_lights + t
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle) + 20 * math.sin(t * 2)  # Add a vertical oscillation
        lights[i] = [x, y]

    # Draw the lights
    for light in lights:
        pygame.draw.circle(screen, WHITE, (int(light[0]), int(light[1])), 5)

    # Update the display
    pygame.display.flip()

    # Increment time
    t += 0.02

    # Control the frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()
