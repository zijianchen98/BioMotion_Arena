
import numpy as np
import pygame
import sys
import os

# Set up constants
WIDTH, HEIGHT = 800, 800
FPS = 30
LIGHT_RADIUS = 5
LIGHT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
NUM_FRAMES = 60  # Total frames of animation

# Define joint positions for a sad woman sitting down
# Positions are in normalized coordinates (0.0 to 1.0) and will be scaled to the screen size
# The skeleton is simplified for demonstration purposes

# Joint names (15 joints)
joint_names = [
    "head",
    "neck",
    "spine",
    "pelvis",
    "left_shoulder",
    "left_elbow",
    "left_hand",
    "right_shoulder",
    "right_elbow",
    "right_hand",
    "left_hip",
    "left_knee",
    "left_foot",
    "right_hip",
    "right_knee",
    "right_foot",
]

# Generate a simple animation sequence for a sad woman sitting down
# Each frame is a list of 15 (x, y) positions (normalized)
animation = []

# Initial standing position
positions = [
    (0.5, 0.1),  # head
    (0.5, 0.2),  # neck
    (0.5, 0.3),  # spine
    (0.5, 0.4),  # pelvis
    (0.4, 0.35),  # left_shoulder
    (0.4, 0.45),  # left_elbow
    (0.4, 0.55),  # left_hand
    (0.6, 0.35),  # right_shoulder
    (0.6, 0.45),  # right_elbow
    (0.6, 0.55),  # right_hand
    (0.4, 0.4),   # left_hip
    (0.4, 0.5),   # left_knee
    (0.4, 0.6),   # left_foot
    (0.6, 0.4),   # right_hip
    (0.6, 0.5),   # right_knee
    (0.6, 0.6),   # right_foot
]
animation.append(positions)

# Transition to sitting position
for i in range(1, 30):
    head_y = 0.1 + i * 0.003
    neck_y = 0.2 + i * 0.003
    spine_y = 0.3 + i * 0.004
    pelvis_y = 0.4 + i * 0.005
    left_shoulder_y = 0.35 + i * 0.002
    left_elbow_y = 0.45 + i * 0.003
    left_hand_y = 0.55 + i * 0.004
    right_shoulder_y = 0.35 + i * 0.002
    right_elbow_y = 0.45 + i * 0.003
    right_hand_y = 0.55 + i * 0.004
    left_hip_y = 0.4 + i * 0.004
    left_knee_y = 0.5 + i * 0.005
    left_foot_y = 0.6 + i * 0.006
    right_hip_y = 0.4 + i * 0.004
    right_knee_y = 0.5 + i * 0.005
    right_foot_y = 0.6 + i * 0.006

    positions = [
        (0.5, head_y),
        (0.5, neck_y),
        (0.5, spine_y),
        (0.5, pelvis_y),
        (0.4, left_shoulder_y),
        (0.4, left_elbow_y),
        (0.4, left_hand_y),
        (0.6, right_shoulder_y),
        (0.6, right_elbow_y),
        (0.6, right_hand_y),
        (0.4, left_hip_y),
        (0.4, left_knee_y),
        (0.4, left_foot_y),
        (0.6, right_hip_y),
        (0.6, right_knee_y),
        (0.6, right_foot_y),
    ]
    animation.append(positions)

# Holding the sitting position for a few frames
for i in range(30, 45):
    positions = [
        (0.5, 0.19),
        (0.5, 0.29),
        (0.5, 0.39),
        (0.5, 0.49),
        (0.4, 0.37),
        (0.4, 0.47),
        (0.4, 0.57),
        (0.6, 0.37),
        (0.6, 0.47),
        (0.6, 0.57),
        (0.4, 0.44),
        (0.4, 0.54),
        (0.4, 0.64),
        (0.6, 0.44),
        (0.6, 0.54),
        (0.6, 0.64),
    ]
    animation.append(positions)

# Transition back to standing position (optional for full cycle)
for i in range(45, 60):
    head_y = 0.19 - (i - 45) * 0.003
    neck_y = 0.29 - (i - 45) * 0.003
    spine_y = 0.39 - (i - 45) * 0.004
    pelvis_y = 0.49 - (i - 45) * 0.005
    left_shoulder_y = 0.37 - (i - 45) * 0.002
    left_elbow_y = 0.47 - (i - 45) * 0.003
    left_hand_y = 0.57 - (i - 45) * 0.004
    right_shoulder_y = 0.37 - (i - 45) * 0.002
    right_elbow_y = 0.47 - (i - 45) * 0.003
    right_hand_y = 0.57 - (i - 45) * 0.004
    left_hip_y = 0.44 - (i - 45) * 0.004
    left_knee_y = 0.54 - (i - 45) * 0.005
    left_foot_y = 0.64 - (i - 45) * 0.006
    right_hip_y = 0.44 - (i - 45) * 0.004
    right_knee_y = 0.54 - (i - 45) * 0.005
    right_foot_y = 0.64 - (i - 45) * 0.006

    positions = [
        (0.5, head_y),
        (0.5, neck_y),
        (0.5, spine_y),
        (0.5, pelvis_y),
        (0.4, left_shoulder_y),
        (0.4, left_elbow_y),
        (0.4, left_hand_y),
        (0.6, right_shoulder_y),
        (0.6, right_elbow_y),
        (0.6, right_hand_y),
        (0.4, left_hip_y),
        (0.4, left_knee_y),
        (0.4, left_foot_y),
        (0.6, right_hip_y),
        (0.6, right_knee_y),
        (0.6, right_foot_y),
    ]
    animation.append(positions)

# Convert to pixel coordinates
for frame in animation:
    for i in range(len(frame)):
        x, y = frame[i]
        frame[i] = (int(x * WIDTH), int(y * HEIGHT))

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Sitting Down (Point-Light Display)")
clock = pygame.time.Clock()

# Main loop
frame_index = 0
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    # Draw the current frame
    for x, y in animation[frame_index]:
        pygame.draw.circle(screen, LIGHT_COLOR, (x, y), LIGHT_RADIUS)

    pygame.display.flip()

    frame_index = (frame_index + 1) % NUM_FRAMES

pygame.quit()
sys.exit()
