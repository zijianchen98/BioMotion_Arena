
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Happyman Bowing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 30
clock = pygame.time.Clock()

# Number of joints (point-lights)
NUM_JOINTS = 15

# Define joint indices for clarity
JOINTS = {
    "head": 0,
    "neck": 1,
    "spine1": 2,
    "spine2": 3,
    "left_shoulder": 4,
    "left_elbow": 5,
    "left_hand": 6,
    "right_shoulder": 7,
    "right_elbow": 8,
    "right_hand": 9,
    "pelvis": 10,
    "left_hip": 11,
    "left_knee": 12,
    "left_ankle": 13,
    "right_hip": 14,
    "right_knee": 15,
    "right_ankle": 16,
}

# Generate a simple bowing motion using sine functions for smooth movement
def generate_bowing_motion(t, joint_indices):
    positions = []

    # Center of the screen
    cx, cy = WIDTH // 2, HEIGHT // 2

    # Base positions relative to center
    base_positions = [
        (0, -100),      # head
        (0, -60),       # neck
        (0, -20),       # spine1
        (0, 10),        # spine2
        (-20, 20),      # left_shoulder
        (-20, 60),      # left_elbow
        (-20, 100),     # left_hand
        (20, 20),       # right_shoulder
        (20, 60),       # right_elbow
        (20, 100),      # right_hand
        (0, 30),        # pelvis
        (-20, 70),      # left_hip
        (-20, 120),     # left_knee
        (-20, 170),     # left_ankle
        (20, 70),       # right_hip
        (20, 120),      # right_knee
        (20, 170),      # right_ankle
    ]

    # Bowing motion: tilt the upper body forward using sine function
    bow_factor = math.sin(t / 10) * 20  # Smooth sine wave for bowing

    for i, (dx, dy) in enumerate(base_positions):
        if i in [JOINTS["head"], JOINTS["neck"], JOINTS["spine1"], JOINTS["spine2"]]:
            # Upper body joints: tilt forward
            x = cx + dx
            y = cy + dy - bow_factor
        elif i in [JOINTS["left_shoulder"], JOINTS["left_elbow"], JOINTS["left_hand"]]:
            # Left arm: slightly bend during bowing
            x = cx + dx
            y = cy + dy + bow_factor * 0.5
        elif i in [JOINTS["right_shoulder"], JOINTS["right_elbow"], JOINTS["right_hand"]]:
            # Right arm: slightly bend during bowing
            x = cx + dx
            y = cy + dy + bow_factor * 0.5
        elif i in [JOINTS["pelvis"], JOINTS["left_hip"], JOINTS["left_knee"], JOINTS["left_ankle"],
                   JOINTS["right_hip"], JOINTS["right_knee"], JOINTS["right_ankle"]]:
            # Legs: minimal movement
            x = cx + dx
            y = cy + dy
        else:
            x = cx + dx
            y = cy + dy

        positions.append((x, y))
    return positions

# Main loop
t = 0  # Time step
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate current joint positions
    joint_positions = generate_bowing_motion(t, JOINTS)

    # Draw point-lights
    for x, y in joint_positions:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(FPS)
    t += 1

pygame.quit()
sys.exit()
