
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display window
win_width = 800
win_height = 600
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Point Light Animation")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the clock
clock = pygame.time.Clock()

# Number of points
num_points = 15

# Initial positions and velocities for each point
points = []
for _ in range(num_points):
    x = random.randint(0, win_width)
    y = random.randint(0, win_height)
    vx = random.uniform(-1, 1)
    vy = random.uniform(-1, 1)
    points.append([x, y, vx, vy])

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill(black)

    # Update and draw each point
    for point in points:
        # Apply gravity-like effect for jumping motion
        point[1] += 0.3  # Increase y-coordinate for downward motion
        point[3] -= 0.1  # Decrease vertical velocity for upward motion

        # Bounce off the bottom of the screen
        if point[1] > win_height:
            point[1] = win_height
            point[3] *= -0.7  # Reduce velocity on bounce

        # Wrap around the screen horizontally
        if point[0] > win_width:
            point[0] = 0
        elif point[0] < 0:
            point[0] = win_width

        # Update position based on velocity
        point[0] += point[2]
        point[1] += point[3]

        # Draw the point
        pygame.draw.circle(window, white, (int(point[0]), int(point[1])), 2)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
