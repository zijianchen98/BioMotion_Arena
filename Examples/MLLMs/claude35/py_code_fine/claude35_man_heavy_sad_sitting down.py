
import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Point-Light Animation of a Sad Man Sitting Down')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light attributes
num_points = 15
point_positions = []
point_radius = 5

# Create initial positions for point-lights in an upright position
for i in range(num_points):
    x = width // 2
    y = height // 4 + (i * (height // num_points))
    point_positions.append((x, y))

# Define the sitting down movement
def update_positions(frame):
    # Simulate sitting down by moving points downward and bringing them closer
    for i in range(num_points):
        y_offset = int(np.sin(frame / 10) * 20)  # Oscillate slightly for realism
        if i < num_points // 2:
            x_offset = 0
            y_position = point_positions[i][1] + y_offset
        else:
            x_offset = int(np.sin(frame / 15) * 10)  # Add some movement to the side for arms
            y_position = point_positions[i][1] + 100 + y_offset

        point_positions[i] = (point_positions[i][0] + x_offset, y_position)

# Main loop
clock = pygame.time.Clock()
frame = 0

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update positions
    update_positions(frame)

    # Draw everything
    screen.fill(BLACK)  # Clear screen
    for x, y in point_positions:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), point_radius)

    pygame.display.flip()  # Update the display
    frame += 1
    clock.tick(30)  # Frame rate
