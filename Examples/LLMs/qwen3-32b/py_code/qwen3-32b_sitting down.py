
import pygame
import sys
import numpy as np
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()

# Frame rate
FPS = 30

# Number of joints (points)
NUM_JOINTS = 15

# Joint indices (for clarity)
HEAD = 0
NECK = 1
TORSO = 2
LEFT_SHOULDER = 3
LEFT_ELBOW = 4
LEFT_HAND = 5
RIGHT_SHOULDER = 6
RIGHT_ELBOW = 7
RIGHT_HAND = 8
LEFT_HIP = 9
LEFT_KNEE = 10
LEFT_FOOT = 11
RIGHT_HIP = 12
RIGHT_KNEE = 13
RIGHT_FOOT = 14

# Predefined joint positions for sitting down motion (simplified)
# This is a basic simulation of sitting down using keyframe interpolation.
# In a real experiment, these positions would be derived from motion capture data.
positions = [
    # Frame 0
    [WIDTH // 2, 100],
    [WIDTH // 2, 130],
    [WIDTH // 2, 170],
    [WIDTH // 2 - 50, 170],
    [WIDTH // 2 - 70, 200],
    [WIDTH // 2 - 80, 230],
    [WIDTH // 2 + 50, 170],
    [WIDTH // 2 + 70, 200],
    [WIDTH // 2 + 80, 230],
    [WIDTH // 2 - 30, 170],
    [WIDTH // 2 - 50, 220],
    [WIDTH // 2 - 60, 270],
    [WIDTH // 2 + 30, 170],
    [WIDTH // 2 + 50, 220],
    [WIDTH // 2 + 60, 270],
]

# Number of frames in the animation
NUM_FRAMES = 30

# Generate a smooth animation by interpolating between keyframes
keyframes = []

# Generate keyframes for the sitting down motion
for t in np.linspace(0, 1, NUM_FRAMES):
    frame = []
    # Head and neck move slightly forward
    head_x = positions[HEAD][0]
    head_y = positions[HEAD][1] + int(30 * t)
    frame.append((head_x, head_y))

    neck_x = positions[NECK][0]
    neck_y = positions[NECK][1] + int(30 * t)
    frame.append((neck_x, neck_y))

    torso_x = positions[TORSO][0]
    torso_y = positions[TORSO][1] + int(40 * t)
    frame.append((torso_x, torso_y))

    # Left arm stays still
    frame.append(positions[LEFT_SHOULDER])
    frame.append(positions[LEFT_ELBOW])
    frame.append(positions[LEFT_HAND])

    # Right arm stays still
    frame.append(positions[RIGHT_SHOULDER])
    frame.append(positions[RIGHT_ELBOW])
    frame.append(positions[RIGHT_HAND])

    # Left leg bends
    left_hip_x = positions[LEFT_HIP][0]
    left_hip_y = positions[LEFT_HIP][1] + int(20 * t)
    frame.append((left_hip_x, left_hip_y))

    left_knee_x = positions[LEFT_KNEE][0]
    left_knee_y = positions[LEFT_KNEE][1] + int(50 * t)
    frame.append((left_knee_x, left_knee_y))

    left_foot_x = positions[LEFT_FOOT][0]
    left_foot_y = positions[LEFT_FOOT][1] + int(50 * t)
    frame.append((left_foot_x, left_foot_y))

    # Right leg bends
    right_hip_x = positions[RIGHT_HIP][0]
    right_hip_y = positions[RIGHT_HIP][1] + int(20 * t)
    frame.append((right_hip_x, right_hip_y))

    right_knee_x = positions[RIGHT_KNEE][0]
    right_knee_y = positions[RIGHT_KNEE][1] + int(50 * t)
    frame.append((right_knee_x, right_knee_y))

    right_foot_x = positions[RIGHT_FOOT][0]
    right_foot_y = positions[RIGHT_FOOT][1] + int(50 * t)
    frame.append((right_foot_x, right_foot_y))

    keyframes.append(frame)

# Animation loop
frame_index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Draw the current frame
    current_frame = keyframes[frame_index]
    for x, y in current_frame:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(FPS)

    # Update frame index
    frame_index = (frame_index + 1) % NUM_FRAMES
