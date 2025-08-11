
import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Bowing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Number of point-lights
NUM_LIGHTS = 15

# Joint positions relative to a central body (simplified skeleton)
# These are relative positions for a bowing motion (in a normalized space)
# Format: [x, y, z] where z is depth (for 2D projection)

# Joint names (for reference)
# Head, Neck, Spine1, Spine2, Spine3, Pelvis,
# Left Shoulder, Left Elbow, Left Wrist,
# Right Shoulder, Right Elbow, Right Wrist,
# Left Hip, Left Knee, Left Ankle

# Initial joint positions in local space (simplified)
joint_positions = np.array([
    [0, 0, 0],       # Head
    [0, -0.2, 0],    # Neck
    [0, -0.5, 0],    # Spine1
    [0, -0.8, 0],    # Spine2
    [0, -1.1, 0],    # Spine3
    [0, -1.4, 0],    # Pelvis
    [-0.3, -0.6, 0], # Left Shoulder
    [-0.3, -0.9, 0], # Left Elbow
    [-0.3, -1.2, 0], # Left Wrist
    [0.3, -0.6, 0],  # Right Shoulder
    [0.3, -0.9, 0],  # Right Elbow
    [0.3, -1.2, 0],  # Right Wrist
    [-0.2, -1.4, 0], # Left Hip
    [-0.2, -1.7, 0], # Left Knee
    [-0.2, -2.0, 0], # Left Ankle
    [0.2, -1.4, 0],  # Right Hip
    [0.2, -1.7, 0],  # Right Knee
    [0.2, -2.0, 0],  # Right Ankle
])

# Bowing animation parameters
bowing_angle = 0.0
bowing_speed = 0.02
bowing_range = math.pi / 3  # 60 degrees

# Function to apply a bowing rotation to the skeleton
def apply_bow(angle):
    rotated = joint_positions.copy()
    for i in range(len(joint_positions)):
        # Apply a rotation about the z-axis (spine rotation)
        x, y, z = joint_positions[i]
        # Rotate around the pelvis (index 5)
        dx = x - joint_positions[5][0]
        dy = y - joint_positions[5][1]
        new_x = dx * math.cos(angle) - dy * math.sin(angle)
        new_y = dx * math.sin(angle) + dy * math.cos(angle)
        rotated[i][0] = new_x + joint_positions[5][0]
        rotated[i][1] = new_y + joint_positions[5][1]
    return rotated

# Function to project 3D points to 2D screen coordinates
def project(points, screen_size=(WIDTH, HEIGHT), scale=100, center=(WIDTH//2, HEIGHT//2)):
    projected = []
    for x, y, z in points:
        # Simple orthographic projection
        px = int(center[0] + x * scale)
        py = int(center[1] - y * scale)
        projected.append((px, py))
    return projected

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Update bowing angle
    bowing_angle += bowing_speed
    if bowing_angle > bowing_range:
        bowing_speed = -abs(bowing_speed)
    elif bowing_angle < -bowing_range:
        bowing_speed = abs(bowing_speed)

    # Apply bowing motion
    animated_joints = apply_bow(bowing_angle)

    # Project to 2D
    lights = project(animated_joints, screen_size=(WIDTH, HEIGHT), scale=100, center=(WIDTH//2, HEIGHT//2))

    # Draw point-lights
    for x, y in lights:
        pygame.draw.circle(screen, WHITE, (x, y), 5)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
