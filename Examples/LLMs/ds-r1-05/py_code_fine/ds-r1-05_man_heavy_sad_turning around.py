
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5
FPS = 60
NUM_POINTS = 15

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sad Man Turning Animation")
clock = pygame.time.Clock()

# Define key body points (initial positions in upright stance relative to pelvis)
points_3d_upright = np.array([
    [0.0, 25.0, 0.0],     # Head
    [0.0, 15.0, 0.0],     # Neck
    [-5.0, 15.0, 0.0],    # Left shoulder
    [5.0, 15.0, 0.0],     # Right shoulder
    [-7.0, 8.0, 0.0],     # Left elbow
    [7.0, 8.0, 0.0],      # Right elbow
    [-8.0, 2.0, 0.0],     # Left wrist
    [8.0, 2.0, 0.0],      # Right wrist
    [-3.0, 0.0, 0.0],     # Left hip
    [3.0, 0.0, 0.0],      # Right hip
    [-3.0, -12.0, 0.0],   # Left knee
    [3.0, -12.0, 0.0],    # Right knee
    [-3.0, -25.0, 0.0],   # Left ankle
    [3.0, -25.0, 0.0],    # Right ankle
    [0.0, 0.0, 0.0]       # Pelvis (root)
])

# Create a sad/heavy stance (torso lean forward by 15 degrees)
tilt_angle = np.radians(15)
rotation_x = np.array([
    [1, 0, 0],
    [0, np.cos(tilt_angle), -np.sin(tilt_angle)],
    [0, np.sin(tilt_angle), np.cos(tilt_angle)]
])
points_3d_base = np.dot(points_3d_upright, rotation_x.T)

# Adjust the whole model down to position pelvis at screen center
pelvis_base_y = points_3d_base[14, 1]
points_3d_base[:, 1] -= pelvis_base_y

# Animation variables
angle = 0.0
angular_speed = 0.01  # radians per frame (slow speed for heaviness)

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(BG_COLOR)
    
    # Compute rotation matrix for current frame
    rotation_y = np.array([
        [np.cos(angle), 0, -np.sin(angle)],
        [0, 1, 0],
        [np.sin(angle), 0, np.cos(angle)]
    ])
    
    # Rotate points
    rotated_points = np.dot(points_3d_base, rotation_y.T)
    
    # Project 3D points to 2D screen
    scale = 10
    screen_points = []
    for point in rotated_points:
        # Flip Y coordinate: Pygame's Y is down, our 3D Y is up
        # Center pelvis at screen center
        x_screen = SCREEN_WIDTH // 2 + point[0] * scale
        y_screen = SCREEN_HEIGHT // 2 - point[1] * scale
        screen_points.append((x_screen, y_screen))
    
    # Draw points
    for x, y in screen_points:
        pygame.draw.circle(screen, POINT_COLOR, (int(x), int(y)), POINT_RADIUS)
    
    # Update angle for next frame
    angle += angular_speed
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
