
import pygame
import math
import sys
import numpy as np
from pygame.locals import *

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
LIGHT_RADIUS = 3
NUM_FRAMES = 120  # 2 seconds of animation at 60 FPS

# Biological motion joints (15 points) for a human figure
JOINTS = {
    'hips': (WIDTH // 2, HEIGHT * 0.7),
    'left_hip': (WIDTH // 2 - 30, HEIGHT * 0.65),
    'right_hip': (WIDTH // 2 + 30, HEIGHT * 0.65),
    'left_knee': (WIDTH // 2 - 30, HEIGHT * 0.55),
    'right_knee': (WIDTH // 2 + 30, HEIGHT * 0.55),
    'left_ankle': (WIDTH // 2 - 30, HEIGHT * 0.45),
    'right_ankle': (WIDTH // 2 + 30, HEIGHT * 0.45),
    'left_shoulder': (WIDTH // 2 - 30, HEIGHT * 0.6),
    'right_shoulder': (WIDTH // 2 + 30, HEIGHT * 0.6),
    'left_elbow': (WIDTH // 2 - 60, HEIGHT * 0.5),
    'right_elbow': (WIDTH // 2 + 60, HEIGHT * 0.5),
    'left_hand': (WIDTH // 2 - 90, HEIGHT * 0.4),
    'right_hand': (WIDTH // 2 + 90, HEIGHT * 0.4),
    'head': (WIDTH // 2, HEIGHT * 0.5),
    'neck': (WIDTH // 2, HEIGHT * 0.55)
}

# Generate a forward rolling motion using a sine wave for movement
def forward_rolling(t, amplitude, frequency, direction):
    return amplitude * math.sin(2 * math.pi * frequency * t + direction)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Woman Forward Rolling")
clock = pygame.time.Clock()

# Generate a sequence of joint positions over time
positions = []

for frame in range(NUM_FRAMES):
    t = frame / FPS
    offset = t * 100  # Forward movement speed

    joints = JOINTS.copy()

    # Move hips forward
    joints['hips'] = (WIDTH // 2 + offset, HEIGHT * 0.7)
    # Move head slightly up and forward
    joints['head'] = (WIDTH // 2 + offset, HEIGHT * 0.5 - forward_rolling(t, 10, 1, 0))
    # Move shoulders with slight bounce
    joints['left_shoulder'] = (WIDTH // 2 - 30 + offset, HEIGHT * 0.6 + forward_rolling(t, 5, 1, 0))
    joints['right_shoulder'] = (WIDTH // 2 + 30 + offset, HEIGHT * 0.6 + forward_rolling(t, 5, 1, 0))
    # Move legs for rolling motion
    joints['left_hip'] = (WIDTH // 2 - 30 + offset, HEIGHT * 0.65 + forward_rolling(t, 5, 2, 0))
    joints['right_hip'] = (WIDTH // 2 + 30 + offset, HEIGHT * 0.65 + forward_rolling(t, 5, 2, math.pi))
    joints['left_knee'] = (WIDTH // 2 - 30 + offset, HEIGHT * 0.55 - forward_rolling(t, 5, 2, 0))
    joints['right_knee'] = (WIDTH // 2 + 30 + offset, HEIGHT * 0.55 - forward_rolling(t, 5, 2, math.pi))
    joints['left_ankle'] = (WIDTH // 2 - 30 + offset, HEIGHT * 0.45 + forward_rolling(t, 5, 2, 0))
    joints['right_ankle'] = (WIDTH // 2 + 30 + offset, HEIGHT * 0.45 + forward_rolling(t, 5, 2, math.pi))
    # Move arms for happy, rolling motion
    joints['left_elbow'] = (WIDTH // 2 - 60 + offset, HEIGHT * 0.5 - forward_rolling(t, 10, 2, 0))
    joints['right_elbow'] = (WIDTH // 2 + 60 + offset, HEIGHT * 0.5 - forward_rolling(t, 10, 2, math.pi))
    joints['left_hand'] = (WIDTH // 2 - 90 + offset, HEIGHT * 0.4 - forward_rolling(t, 15, 2, 0))
    joints['right_hand'] = (WIDTH // 2 + 90 + offset, HEIGHT * 0.4 - forward_rolling(t, 15, 2, math.pi))

    positions.append(joints)

# Main animation loop
frame_index = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background

    # Draw point lights
    current_joints = positions[frame_index]
    for joint in current_joints.values():
        pygame.draw.circle(screen, (255, 255, 255), (int(joint[0]), int(joint[1])), LIGHT_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)
    frame_index = (frame_index + 1) % NUM_FRAMES

pygame.quit()
sys.exit()
