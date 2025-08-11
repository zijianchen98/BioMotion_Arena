
import pygame
import numpy as np
import math

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
NUM_POINTS = 15
RADIUS = 10
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)

# Define point light positions in an initial T-pose
initial_positions = np.array([
    [0, -4],  # Head
    [-2, -2], [2, -2],  # Shoulders
    [-3, 0], [3, 0],    # Elbows
    [-3, 2], [3, 2],    # Hands
    [0, 3],             # Torso
    [-1, 4], [1, 4],    # Hips
    [-1, 6], [1, 6],    # Knees
    [-1, 8], [1, 8],    # Feet
    [0, 9]              # Top of head
]) * 20  # Scale for visibility

# Function to rotate points
def rotate(points, angle):
    rotation_matrix = np.array([
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle), math.cos(angle)]
    ])
    return np.dot(points, rotation_matrix)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation")
clock = pygame.time.Clock()

running = True
angle = 0

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Update the angle for rotation
    angle += 0.1  # Speed of rotation
    if angle >= 2 * math.pi:
        angle -= 2 * math.pi

    # Rotate and draw points
    rotated_positions = rotate(initial_positions, angle)
    for point in rotated_positions:
        x = WIDTH // 2 + point[0]
        y = HEIGHT // 2 + point[1]
        pygame.draw.circle(screen, POINT_COLOR, (int(x), int(y)), RADIUS)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
