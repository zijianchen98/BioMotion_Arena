
import pygame
import sys
import numpy as np
import math

# Configuration
WIDTH, HEIGHT = 800, 600
FPS = 30
LIGHT_RADIUS = 3
NUM_FRAMES = 120
LIGHT_COLOR = (255, 255, 255)
BG_COLOR = (0, 0, 0)

# Joint positions relative to the body (simplified model)
# Each joint is represented as a tuple of (x_offset, y_offset, z_offset)
# For a sad walk, the motion is slower, with a hunched posture and dragging steps

joint_offsets = [
    (0, 0, 0),         # Hip
    (-10, -20, 0),     # Left hip
    (10, -20, 0),      # Right hip
    (-10, -40, 0),     # Left knee
    (10, -40, 0),      # Right knee
    (-10, -60, 0),     # Left ankle
    (10, -60, 0),      # Right ankle
    (-5, -30, 0),      # Left shoulder
    (5, -30, 0),       # Right shoulder
    (-15, -50, 0),     # Left elbow
    (15, -50, 0),      # Right elbow
    (-15, -70, 0),     # Left hand
    (15, -70, 0),      # Right hand
    (0, -25, 0),       # Head
    (0, -45, 0),       # Chin (extra joint to show sad posture)
]

# Generate walking motion with a sad posture
def generate_sad_walk(num_frames):
    positions = []
    for frame in range(num_frames):
        phase = 2 * math.pi * frame / num_frames
        walk_cycle = math.sin(phase)

        # Hip position moves up and down slightly
        hip_y = 200 + 10 * math.sin(phase)
        hip_x = 400 + 20 * walk_cycle

        # Generate joint positions based on the walking phase
        joints = []
        for i, (dx, dy, dz) in enumerate(joint_offsets):
            # Add some vertical motion for the legs
            if i == 1 or i == 3 or i == 5:  # Left leg joints
                y_offset = dy + 10 * math.sin(phase + math.pi)
            elif i == 2 or i == 4 or i == 6:  # Right leg joints
                y_offset = dy + 10 * math.sin(phase)
            else:
                y_offset = dy

            # Add some forward/backward motion for shoulders and arms
            if i >= 7 and i <= 12:  # Arms and shoulders
                x_offset = dx + 10 * math.sin(phase + math.pi / 2)
            else:
                x_offset = dx

            # Apply offsets
            x = hip_x + x_offset
            y = hip_y + y_offset

            joints.append((x, y))

        positions.append(joints)
    return positions

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Walking Point-Light Stimulus")
clock = pygame.time.Clock()

# Generate the motion sequence
positions = generate_sad_walk(NUM_FRAMES)

# Main loop
frame_index = 0
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    # Draw the current frame
    for x, y in positions[frame_index]:
        pygame.draw.circle(screen, LIGHT_COLOR, (int(x), int(y)), LIGHT_RADIUS)

    pygame.display.flip()

    # Update frame index
    frame_index = (frame_index + 1) % NUM_FRAMES

pygame.quit()
sys.exit()
