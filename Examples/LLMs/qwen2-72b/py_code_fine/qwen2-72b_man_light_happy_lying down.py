
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point Light Animation")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the clock
clock = pygame.time.Clock()

# Number of points
num_points = 15

# Create a list to store the positions of the points
points = [(random.randint(0, screen_width), random.randint(0, screen_height)) for _ in range(num_points)]

# Animation loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Update the positions of the points (simple random movement)
    for i in range(num_points):
        x, y = points[i]
        dx = random.uniform(-1, 1)
        dy = random.uniform(-1, 1)
        points[i] = (x + dx, y + dy)

        # Ensure the points stay within the screen bounds
        points[i] = (min(max(points[i][0], 0), screen_width), min(max(points[i][1], 0), screen_height))

    # Draw the points
    for point in points:
        pygame.draw.circle(screen, white, point, 2)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
