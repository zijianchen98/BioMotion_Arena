
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Woman Turning Around with Heavy Weight")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 30

# Joint positions relative to the body (simplified human model)
# 15 joints: head, shoulders, elbows, wrists, hips, knees, ankles, and additional for weight
# Coordinates are relative to the center of the body
JOINTS = np.array([
    [0, -100],   # head
    [-40, -60],  # left shoulder
    [40, -60],   # right shoulder
    [-60, -20],  # left elbow
    [60, -20],   # right elbow
    [-30, 10],   # left wrist
    [30, 10],    # right wrist
    [-20, 40],   # left hip
    [20, 40],    # right hip
    [-50, 80],   # left knee
    [50, 80],    # right knee
    [-30, 120],  # left ankle
    [30, 120],   # right ankle
    [-10, 100],  # weight (left side)
    [10, 100],   # weight (right side)
])

# Initial body position (center of the hips)
BODY_CENTER = [WIDTH // 2, HEIGHT // 2]

# Animation parameters
rotation_angle = 0  # in degrees
rotation_speed = 1  # degrees per frame
lean_angle = 0  # for turning realism
lean_speed = 0.5

# Main animation loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update rotation and lean angles
    rotation_angle += rotation_speed
    lean_angle = math.sin(math.radians(rotation_angle / 2)) * 10  # simulate lean

    # Calculate new joint positions based on rotation and lean
    rotated_joints = []
    for x, y in JOINTS:
        # Apply rotation
        rad = math.radians(rotation_angle)
        new_x = x * math.cos(rad) - y * math.sin(rad)
        new_y = x * math.sin(rad) + y * math.cos(rad)
        # Apply lean
        new_y += lean_angle
        # Translate to screen position
        rotated_joints.append((BODY_CENTER[0] + new_x, BODY_CENTER[1] + new_y))

    # Draw the point-light stimulus
    for px, py in rotated_joints:
        pygame.draw.circle(screen, WHITE, (int(px), int(py)), 5)

    pygame.display.flip()

pygame.quit()
sys.exit()
