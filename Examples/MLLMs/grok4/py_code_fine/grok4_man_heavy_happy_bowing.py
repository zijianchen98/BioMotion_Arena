
import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
NUM_POINTS = 15
FPS = 30

# Setup the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Animation: Bowing')

# Define initial positions of the point lights
# Assume an initial position representing a standing bowing pose
# This is a simplified representation for the example
points = np.array([
    [400, 100],  # Head
    [380, 160],  # Left shoulder
    [420, 160],  # Right shoulder
    [360, 220],  # Left elbow
    [440, 220],  # Right elbow
    [340, 280],  # Left hand
    [460, 280],  # Right hand
    [400, 300],  # Torso
    [370, 360],  # Left hip
    [430, 360],  # Right hip
    [360, 440],  # Left knee
    [440, 440],  # Right knee
    [340, 500],  # Left foot
    [460, 500],  # Right foot
    [400, 350],  # Center of mass (optional)
    [400, 200],  # Heavy weight position (for bowing)
])

# Animation function
def animate(points, frame):
    # Simple bow animation adjustment
    bow_angle = 0.1 * np.sin(frame / 10)  # Adjust for smooth bow motion
    points[0, 1] += 10 * bow_angle  # Head bow
    points[1, 1] += 10 * bow_angle  # Left shoulder bow
    points[2, 1] += 10 * bow_angle  # Right shoulder bow
    # You can add more points transformation based on action here for realism
    return points

# Main loop
frame = 0
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Update points for animation
    animated_points = animate(points.copy(), frame)

    # Draw the point lights
    for point in animated_points:
        pygame.draw.circle(screen, POINT_COLOR, (int(point[0]), int(point[1])), 5)

    # Update the display
    pygame.display.flip()
    frame += 1
    pygame.time.Clock().tick(FPS)
