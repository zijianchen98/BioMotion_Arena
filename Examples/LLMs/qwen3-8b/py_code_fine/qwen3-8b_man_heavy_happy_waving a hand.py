
import numpy as np
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Happy Man Waving")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define body joints (simplified skeleton)
JOINTS = [
    (0, 0),  # Spine base
    (0, -100),  # Spine mid
    (0, -200),  # Spine top
    (-50, -200),  # Left shoulder
    (50, -200),  # Right shoulder
    (-50, -250),  # Left elbow
    (50, -250),  # Right elbow
    (-50, -300),  # Left wrist
    (50, -300),  # Right wrist
    (-50, -350),  # Left hand
    (50, -350),  # Right hand
    (-100, -200),  # Left hip
    (100, -200),  # Right hip
    (-100, -250),  # Left knee
    (100, -250),  # Right knee
    (-100, -300),  # Left ankle
    (100, -300),  # Right ankle
]

# Define joint connections
CONNECTORS = [
    (0, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6),
    (5, 7), (6, 8), (7, 9), (8, 10), (3, 11), (4, 12),
    (11, 13), (12, 14), (13, 15), (14, 16)
]

# Create point lights as a list of joint indices
POINT_LIGHTS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Define a function to calculate the position of a joint based on time
def get_joint_position(joint_index, time):
    # Spine base
    if joint_index == 0:
        return (WIDTH / 2, HEIGHT / 2)
    # Spine mid
    elif joint_index == 1:
        return (WIDTH / 2, HEIGHT / 2 - 50)
    # Spine top
    elif joint_index == 2:
        return (WIDTH / 2, HEIGHT / 2 - 100)
    # Left shoulder
    elif joint_index == 3:
        return (WIDTH / 2 - 50, HEIGHT / 2 - 100)
    # Right shoulder
    elif joint_index == 4:
        return (WIDTH / 2 + 50, HEIGHT / 2 - 100)
    # Left elbow
    elif joint_index == 5:
        return (WIDTH / 2 - 75, HEIGHT / 2 - 130)
    # Right elbow
    elif joint_index == 6:
        return (WIDTH / 2 + 75, HEIGHT / 2 - 130)
    # Left wrist
    elif joint_index == 7:
        return (WIDTH / 2 - 100, HEIGHT / 2 - 160)
    # Right wrist
    elif joint_index == 8:
        return (WIDTH / 2 + 100, HEIGHT / 2 - 160)
    # Left hand
    elif joint_index == 9:
        return (WIDTH / 2 - 120, HEIGHT / 2 - 190)
    # Right hand
    elif joint_index == 10:
        return (WIDTH / 2 + 120, HEIGHT / 2 - 190)
    # Left hip
    elif joint_index == 11:
        return (WIDTH / 2 - 100, HEIGHT / 2 - 100)
    # Right hip
    elif joint_index == 12:
        return (WIDTH / 2 + 100, HEIGHT / 2 - 100)
    # Left knee
    elif joint_index == 13:
        return (WIDTH / 2 - 120, HEIGHT / 2 - 130)
    # Right knee
    elif joint_index == 14:
        return (WIDTH / 2 + 120, HEIGHT / 2 - 130)
    # Left ankle
    elif joint_index == 15:
        return (WIDTH / 2 - 140, HEIGHT / 2 - 160)
    # Right ankle
    elif joint_index == 16:
        return (WIDTH / 2 + 140, HEIGHT / 2 - 160)

# Main loop
running = True
time = 0
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Update time
    time += 0.05

    # Get positions of all joints
    joint_positions = [get_joint_position(i, time) for i in range(len(JOINTS))]

    # Draw connectors
    for a, b in CONNECTORS:
        pygame.draw.line(screen, WHITE, joint_positions[a], joint_positions[b], 2)

    # Draw point lights
    for idx in POINT_LIGHTS:
        x, y = joint_positions[idx]
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 4)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
