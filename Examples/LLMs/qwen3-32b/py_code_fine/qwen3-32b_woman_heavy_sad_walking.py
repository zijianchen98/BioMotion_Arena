
import numpy as np
import pygame
import sys
import os

# Set up display
WIDTH, HEIGHT = 800, 600
FPS = 60

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sad Woman Walking")
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define joint positions for a sad walking motion (point-light positions)
# These are simplified and approximate positions over time
# Each entry is a joint position (x, y) for each frame

# Total number of frames
NUM_FRAMES = 120

# Define joint positions over time
# This is a simplified and stylized representation of a sad walking motion
# Each joint's position is represented as a list of (x, y) positions for each frame

# For simplicity, we'll define 15 joints (point-lights)
# These positions are manually created to simulate a sad walking motion
# Each joint is represented as a list of (x, y) positions for each frame

# Define joint positions
# 0: head
# 1: neck
# 2: right shoulder
# 3: left shoulder
# 4: right elbow
# 5: left elbow
# 6: right hand
# 7: left hand
# 8: upper spine
# 9: lower spine
# 10: right hip
# 11: left hip
# 12: right knee
# 13: left knee
# 14: right foot
# 15: left foot

# Generate positions for a sad walking motion
positions = []

for frame in range(NUM_FRAMES):
    # Base positions (center of screen)
    cx, cy = WIDTH // 2, HEIGHT // 2

    # Generate joint positions for the current frame
    joint_positions = [
        (cx, cy - 150),  # head
        (cx, cy - 120),  # neck
        (cx - 30, cy - 100),  # right shoulder
        (cx + 30, cy - 100),  # left shoulder
        (cx - 60, cy - 80),  # right elbow
        (cx + 60, cy - 80),  # left elbow
        (cx - 90, cy - 60),  # right hand
        (cx + 90, cy - 60),  # left hand
        (cx, cy - 80),  # upper spine
        (cx, cy - 50),  # lower spine
        (cx - 30, cy - 20),  # right hip
        (cx + 30, cy - 20),  # left hip
        (cx - 40, cy + 20),  # right knee
        (cx + 40, cy + 20),  # left knee
        (cx - 60, cy + 60),  # right foot
        (cx + 60, cy + 60),  # left foot
    ]

    # Add some motion over time
    t = frame / NUM_FRAMES * 2 * np.pi  # normalized time
    walk_offset = 10 * np.sin(t)
    head_offset = 10 * np.sin(t * 2)
    shoulder_offset = 10 * np.sin(t * 1.5)
    elbow_offset = 15 * np.sin(t * 2)
    knee_offset = 10 * np.sin(t * 2.5)

    # Update positions based on time
    joint_positions[0] = (cx, cy - 150 + head_offset)
    joint_positions[2] = (cx - 30 + shoulder_offset, cy - 100)
    joint_positions[3] = (cx + 30 - shoulder_offset, cy - 100)
    joint_positions[4] = (cx - 60 + elbow_offset, cy - 80)
    joint_positions[5] = (cx + 60 - elbow_offset, cy - 80)
    joint_positions[12] = (cx - 40 + knee_offset, cy + 20)
    joint_positions[13] = (cx + 40 - knee_offset, cy + 20)
    joint_positions[14] = (cx - 60 + walk_offset, cy + 60)
    joint_positions[15] = (cx + 60 - walk_offset, cy + 60)

    positions.append(joint_positions)

# Animation loop
current_frame = 0
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Draw point-lights for current frame
    for x, y in positions[current_frame]:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    # Update frame
    current_frame = (current_frame + 1) % NUM_FRAMES

    pygame.display.flip()

pygame.quit()
sys.exit()
