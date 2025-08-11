
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINTS_NUM = 15

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Animation')

# Define initial positions for point lights (based on the image)
# Example coordinates for 'happyman' with 15 points
points = [
    (400, 150),  # head
    (370, 200), (400, 200), (430, 200),  # shoulders
    (350, 250), (400, 250), (450, 250),  # arms
    (370, 325), (430, 325),  # hip joints
    (380, 400), (420, 400),  # knees
    (350, 500), (450, 500),  # feet
]

# Animation variables
angle = 0
weight_y_offset = 10  # Weight visual position offset

def update_points(angle):
    # Update the coordinates of points to simulate running motion
    new_points = []
    for i, (x, y) in enumerate(points):
        # Basic transformation for running motion
        y += int(np.sin(angle + i) * 5)  # Simulate running bounce
        if 7 <= i <= 12:  # For legs
            x += int(np.cos(angle + i) * 2)  # Left-right motion during running
        new_points.append((x, y))
    
    return new_points

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the angle for motion
    angle += 0.1
    if angle >= 2 * np.pi:
        angle = 0

    # Update the positions of the points
    current_points = update_points(angle)

    # Fill the background
    screen.fill(BLACK)

    # Draw the points
    for point in current_points:
        pygame.draw.circle(screen, WHITE, (point[0], point[1]), 5)

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

# Quit Pygame
pygame.quit()
