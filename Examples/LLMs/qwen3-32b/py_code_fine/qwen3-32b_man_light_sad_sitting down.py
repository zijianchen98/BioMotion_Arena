
import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sadman Sitting Down - Point-Light Biological Motion")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()

# Frame rate
FPS = 30

# Define joint positions (relative to a central body)
# We'll use 15 joints: head, shoulders, elbows, wrists, hips, knees, ankles, and spine
# All positions are in a 3D-like coordinate system (x, y, z), where z is used for depth simulation
JOINTS = {
    'head': [400, 100, 0],
    'neck': [400, 140, 0],
    'left_shoulder': [350, 160, 0],
    'left_elbow': [320, 200, 0],
    'left_wrist': [310, 240, 0],
    'right_shoulder': [450, 160, 0],
    'right_elbow': [480, 200, 0],
    'right_wrist': [490, 240, 0],
    'spine_top': [400, 180, 0],
    'spine_mid': [400, 220, 0],
    'spine_bottom': [400, 260, 0],
    'left_hip': [360, 280, 0],
    'left_knee': [340, 320, 0],
    'left_ankle': [330, 360, 0],
    'right_hip': [440, 280, 0],
    'right_knee': [460, 320, 0],
    'right_ankle': [470, 360, 0],
}

# Convert to list for animation
joint_names = list(JOINTS.keys())
joint_positions = list(JOINTS.values())
num_joints = len(joint_positions)

# Animation parameters
animation_duration = 120  # frames
frames = []

# Generate animation frames for "sitting down"
for frame in range(animation_duration):
    positions = []
    for i, name in enumerate(joint_names):
        x, y, z = joint_positions[i]

        # Adjust y-coordinate to simulate sitting down over time
        # Smooth transition using a sine curve to make it natural
        if name in ['head', 'neck', 'left_shoulder', 'right_shoulder', 'spine_top']:
            y += 20 * (1 - math.sin(math.pi * frame / (animation_duration - 1)))
        elif name in ['spine_mid', 'spine_bottom', 'left_hip', 'right_hip']:
            y += 30 * (1 - math.sin(math.pi * frame / (animation_duration - 1)))
        elif name in ['left_knee', 'right_knee']:
            y += 10 * math.sin(math.pi * frame / (animation_duration - 1))
        elif name in ['left_ankle', 'right_ankle']:
            y += 5 * (1 - math.sin(math.pi * frame / (animation_duration - 1)))

        # Adjust x-coordinate slightly to simulate natural body flex
        if name == 'left_elbow':
            x += 5 * math.sin(math.pi * frame / (animation_duration - 1))
        elif name == 'right_elbow':
            x -= 5 * math.sin(math.pi * frame / (animation_duration - 1))

        positions.append((x, y))
    frames.append(positions)

# Main loop
frame_index = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Draw current frame
    positions = frames[frame_index]
    for x, y in positions:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    frame_index = (frame_index + 1) % len(frames)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
