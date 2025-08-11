
import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_RADIUS = 4
NUM_LIGHTS = 15

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Jumping Up")
clock = pygame.time.Clock()

# Skeleton joints (relative to center of mass)
joint_positions = {
    "left_hip": (0, 0),
    "right_hip": (0, 0),
    "left_knee": (0, 0),
    "right_knee": (0, 0),
    "left_ankle": (0, 0),
    "right_ankle": (0, 0),
    "spine": (0, 0),
    "neck": (0, 0),
    "head": (0, 0),
    "left_shoulder": (0, 0),
    "right_shoulder": (0, 0),
    "left_elbow": (0, 0),
    "right_elbow": (0, 0),
    "left_wrist": (0, 0),
    "right_wrist": (0, 0),
}

# Define a jumping motion over time
def jumping_motion(t, amplitude=100, frequency=0.2):
    # t: time in seconds
    # returns vertical offset (up and down)
    return amplitude * (1 - math.cos(2 * math.pi * frequency * t)) / 2

# Define the skeleton's position and movement
def update_skeleton(t):
    # Center of motion
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    # Jump height
    jump_height = jumping_motion(t)

    # Update joint positions (simplified but biomechanically plausible)
    joint_positions["left_hip"] = (center_x - 60, center_y - 100 + jump_height)
    joint_positions["right_hip"] = (center_x + 60, center_y - 100 + jump_height)
    joint_positions["left_knee"] = (center_x - 100, center_y - 150 + jump_height)
    joint_positions["right_knee"] = (center_x + 100, center_y - 150 + jump_height)
    joint_positions["left_ankle"] = (center_x - 120, center_y - 200 + jump_height)
    joint_positions["right_ankle"] = (center_x + 120, center_y - 200 + jump_height)
    joint_positions["spine"] = (center_x, center_y - 100 + jump_height)
    joint_positions["neck"] = (center_x, center_y - 160 + jump_height)
    joint_positions["head"] = (center_x, center_y - 200 + jump_height)
    joint_positions["left_shoulder"] = (center_x - 40, center_y - 160 + jump_height)
    joint_positions["right_shoulder"] = (center_x + 40, center_y - 160 + jump_height)
    joint_positions["left_elbow"] = (center_x - 80, center_y - 180 + jump_height)
    joint_positions["right_elbow"] = (center_x + 80, center_y - 180 + jump_height)
    joint_positions["left_wrist"] = (center_x - 100, center_y - 190 + jump_height)
    joint_positions["right_wrist"] = (center_x + 100, center_y - 190 + jump_height)

# Main loop
time = 0
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update skeleton positions
    update_skeleton(time)

    # Draw all lights
    for joint in joint_positions.values():
        pygame.draw.circle(screen, WHITE, (int(joint[0]), int(joint[1])), LIGHT_RADIUS)

    pygame.display.flip()
    time += 1 / FPS

pygame.quit()
sys.exit()
