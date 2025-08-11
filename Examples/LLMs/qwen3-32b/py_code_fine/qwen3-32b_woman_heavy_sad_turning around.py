
import numpy as np
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Woman Turning Around with Heavy Weight")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 30

# Define joint positions relative to the body (simplified skeleton with 15 joints)
# We will rotate the whole body to simulate turning around

# Joint order: head, neck, spine, pelvis, left shoulder, left elbow, left hand, right shoulder, right elbow, right hand,
# left hip, left knee, left foot, right hip, right knee, right foot
# Coordinates are relative to the center of the body (pelvis)

joint_positions = [
    (0, -100),  # Head
    (0, -80),   # Neck
    (0, -60),   # Spine
    (0, 0),     # Pelvis (center)
    (-30, -40), # Left shoulder
    (-30, -10), # Left elbow
    (-30, 20),  # Left hand
    (30, -40),  # Right shoulder
    (30, -10),  # Right elbow
    (30, 20),   # Right hand
    (-20, 20),  # Left hip
    (-20, 60),  # Left knee
    (-20, 100), # Left foot
    (20, 20),   # Right hip
    (20, 60),   # Right knee
    (20, 100)   # Right foot
]

# Convert joint positions to numpy array for easier rotation
joint_positions = np.array(joint_positions, dtype=np.float32)

# Animation parameters
angle = 0  # Initial rotation angle
angle_speed = 0.02  # Radians per frame
center = (WIDTH // 2, HEIGHT // 2)

# Main loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rotate the joint positions around the center of the body (pelvis)
    # Apply rotation matrix
    rotation_matrix = np.array([
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle), math.cos(angle)]
    ])

    rotated_joints = np.dot(joint_positions, rotation_matrix.T) + np.array(center)

    # Draw point lights
    for point in rotated_joints:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)

    # Update rotation angle
    angle += angle_speed

    # Limit rotation to simulate turning around once
    if angle > 2 * math.pi:
        angle_speed *= -1  # Reverse direction after turning around
    elif angle < 0:
        angle_speed *= -1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
