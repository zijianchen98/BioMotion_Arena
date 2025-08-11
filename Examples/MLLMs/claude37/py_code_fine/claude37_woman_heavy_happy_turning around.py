
import pygame
import numpy as np
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_POINTS = 15
RADIUS = 5

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation: Happy Woman Turning Around")
clock = pygame.time.Clock()

# Initial positions of the point-lights
# In a realistic scenario, these would represent body joints
points = []
for i in range(NUM_POINTS):
    angle = i * (2 * math.pi / NUM_POINTS)
    radius = 100  # Distance from the center
    x = WIDTH // 2 + radius * math.cos(angle)
    y = HEIGHT // 2 + radius * math.sin(angle)
    points.append([x, y])

def update_points(angle):
    for i in range(NUM_POINTS):
        # Calculate the new position based on the angle
        x = WIDTH // 2 + 100 * math.cos(angle + i * (2 * math.pi / NUM_POINTS))
        y = HEIGHT // 2 + 100 * math.sin(angle + i * (2 * math.pi / NUM_POINTS))
        points[i] = [x, y]

# Main loop
running = True
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the point locations to simulate turning
    angle += 0.05  # Control the speed of turning
    update_points(angle)

    # Clear the screen
    screen.fill(BLACK)

    # Draw the points
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), RADIUS)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
