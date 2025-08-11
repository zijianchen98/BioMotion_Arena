
import pygame
import math
import sys
import numpy as np
from collections import deque

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NUM_LIGHTS = 15
JOINT_RADIUS = 10

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Happy Man Waving")
clock = pygame.time.Clock()

# Joint indices for a 15-point-light human model (simplified)
# 0: head
# 1: neck
# 2: torso center
# 3: left shoulder
# 4: left elbow
# 5: left hand
# 6: right shoulder
# 7: right elbow
# 8: right hand
# 9: left hip
# 10: left knee
# 11: left foot
# 12: right hip
# 13: right knee
# 14: right foot

# Define joint positions relative to center of screen
# We'll use a simplified skeleton and animate the right arm (shoulder, elbow, hand) for waving

# Joint connections (edges to draw)
edges = [
    (0, 1), (1, 2), (2, 9), (2, 12), (3, 4), (4, 5), (6, 7), (7, 8),
    (9, 10), (10, 11), (12, 13), (13, 14)
]

# Central position
center_x = WIDTH // 2
center_y = HEIGHT // 2

# Joint offsets in resting position
joint_offsets = [
    (0, -100),       # head
    (0, -50),        # neck
    (0, 0),          # torso
    (-40, 30),       # left shoulder
    (-40, 70),       # left elbow
    (-40, 110),      # left hand
    (40, 30),        # right shoulder
    (40, 70),        # right elbow
    (40, 110),       # right hand
    (-30, 60),       # left hip
    (-30, 100),      # left knee
    (-30, 140),      # left foot
    (30, 60),        # right hip
    (30, 100),       # right knee
    (30, 140),       # right foot
]

# Animation parameters
wave_speed = 0.03
wave_offset = 0

# Function to compute joint positions based on waving motion
def get_joint_positions(t):
    positions = []
    for i, (dx, dy) in enumerate(joint_offsets):
        x = center_x + dx
        y = center_y + dy

        # Apply waving motion only to the right arm
        if i in [6, 7, 8]:  # right shoulder, elbow, hand
            wave = 15 * math.sin(t + i * 0.5)
            x += wave
            y -= 0.5 * wave  # slight up-down motion

        positions.append((x, y))
    return positions

# Main animation loop
running = True
t = 0

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    t += wave_speed
    positions = get_joint_positions(t)

    # Draw joints
    for x, y in positions:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), JOINT_RADIUS)

    # Draw edges
    for a, b in edges:
        pygame.draw.line(screen, WHITE, positions[a], positions[b], 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
