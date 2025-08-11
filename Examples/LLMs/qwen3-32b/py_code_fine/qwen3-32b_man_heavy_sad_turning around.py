
import pygame
import math
import sys
import numpy as np

# Set up display
WIDTH, HEIGHT = 800, 800
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 4

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sadman Turning Around - Point-Light Biological Motion")
clock = pygame.time.Clock()

# Define body joints
# We'll use a simplified model of 15 joints for a human figure
# Coordinates are relative to a center point and will be updated over time

# Joint indices
JOINTS = {
    'hips': 0,
    'right_hip': 1,
    'right_knee': 2,
    'right_ankle': 3,
    'left_hip': 4,
    'left_knee': 5,
    'left_ankle': 6,
    'spine': 7,
    'neck': 8,
    'head': 9,
    'left_shoulder': 10,
    'left_elbow': 11,
    'left_wrist': 12,
    'right_shoulder': 13,
    'right_elbow': 14,
    'right_wrist': 15
}

# Define a simple walking turning motion using sine waves and rotation
# We will simulate the turning motion by rotating the whole body around the hips

def get_joint_positions(angle, time, amplitude=0.1, frequency=0.5, offset=0):
    # Base positions relative to center
    base = {
        'hips': (0, 0),
        'right_hip': (0, 50),
        'right_knee': (0, 100),
        'right_ankle': (0, 150),
        'left_hip': (0, 50),
        'left_knee': (0, 100),
        'left_ankle': (0, 150),
        'spine': (0, -50),
        'neck': (0, -100),
        'head': (0, -150),
        'left_shoulder': (-30, -80),
        'left_elbow': (-30, -130),
        'left_wrist': (-30, -180),
        'right_shoulder': (30, -80),
        'right_elbow': (30, -130),
        'right_wrist': (30, -180)
    }

    # Add dynamic motion for legs and arms using sine waves
    for joint in ['right_hip', 'right_knee', 'right_ankle', 'left_hip', 'left_knee', 'left_ankle']:
        x, y = base[joint]
        base[joint] = (x, y + amplitude * math.sin(frequency * time + offset))

    for joint in ['left_shoulder', 'left_elbow', 'left_wrist', 'right_shoulder', 'right_elbow', 'right_wrist']:
        x, y = base[joint]
        base[joint] = (x + amplitude * math.sin(frequency * time + offset), y)

    # Rotate the entire body around the hips
    rotated = {}
    cx, cy = base['hips']
    for joint, (x, y) in base.items():
        dx = x - cx
        dy = y - cy
        new_x = dx * math.cos(angle) - dy * math.sin(angle)
        new_y = dx * math.sin(angle) + dy * math.cos(angle)
        rotated[joint] = (cx + new_x, cy + new_y)

    return rotated

# Main loop
angle = 0
time = 0
center = (WIDTH // 2, HEIGHT // 2)
scale = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    # Get current joint positions
    joint_positions = get_joint_positions(angle, time)

    # Draw the joints
    for joint, (x, y) in joint_positions.items():
        px = int(center[0] + x * scale)
        py = int(center[1] + y * scale)
        pygame.draw.circle(screen, POINT_COLOR, (px, py), POINT_RADIUS)

    # Update rotation angle and time
    angle += 0.01
    time += 0.1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
