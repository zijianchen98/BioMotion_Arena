
import pygame
import numpy as np
import sys
import time

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of point-lights
num_lights = 15

# Initial positions and velocities of the point-lights
lights = np.random.rand(num_lights, 2) * np.array([width, height])
velocities = np.random.rand(num_lights, 2) - 0.5

# Function to update the positions of the point-lights
def update_positions():
    global lights
    lights += velocities
    for i in range(num_lights):
        if lights[i, 0] < 0 or lights[i, 0] > width:
            velocities[i, 0] *= -1
        if lights[i, 1] < 0 or lights[i, 1] > height:
            velocities[i, 1] *= -1

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update positions
    update_positions()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the point-lights
    for light in lights:
        pygame.draw.circle(screen, WHITE, light.astype(int), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
