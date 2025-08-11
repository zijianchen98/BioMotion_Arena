
import pygame
import sys
import math
import numpy as np

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Woman Walking with Heavy Weight")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Joint indices for a 15-point light biological motion model
JOINTS = [
    'Hip', 'Right Up Leg', 'Right Low Leg', 'Right Foot',
    'Left Up Leg', 'Left Low Leg', 'Left Foot',
    'Spine', 'Torso', 'Neck', 'Head',
    'Left Arm', 'Left Forearm', 'Right Arm', 'Right Forearm'
]

# Frame rate and animation speed
FPS = 30
ANIMATION_SPEED = 1.0

# Load motion capture data (simplified version for demonstration)
# In a real scenario, this would be loaded from a motion capture file
def generate_motion_data(num_frames):
    data = []
    for frame in range(num_frames):
        t = frame / num_frames * 2 * math.pi * 2  # Walking cycle
        # Generate simplified joint positions (x, y, z)
        joints = {
            'Hip': [WIDTH // 2, HEIGHT - 100 + 10 * math.sin(t), 0],
            'Right Up Leg': [WIDTH // 2 - 50, HEIGHT - 100 + 20 * math.sin(t + math.pi / 2), 0],
            'Right Low Leg': [WIDTH // 2 - 50 - 20 * math.cos(t), HEIGHT - 100 + 20 * math.sin(t + math.pi / 2) + 30, 0],
            'Right Foot': [WIDTH // 2 - 50 - 20 * math.cos(t) - 10, HEIGHT - 100 + 20 * math.sin(t + math.pi / 2) + 50, 0],
            'Left Up Leg': [WIDTH // 2 + 50, HEIGHT - 100 + 20 * math.sin(t - math.pi / 2), 0],
            'Left Low Leg': [WIDTH // 2 + 50 + 20 * math.cos(t), HEIGHT - 100 + 20 * math.sin(t - math.pi / 2) + 30, 0],
            'Left Foot': [WIDTH // 2 + 50 + 20 * math.cos(t) + 10, HEIGHT - 100 + 20 * math.sin(t - math.pi / 2) + 50, 0],
            'Spine': [WIDTH // 2, HEIGHT - 100 + 10 * math.sin(t) - 20, 0],
            'Torso': [WIDTH // 2, HEIGHT - 100 + 10 * math.sin(t) - 40, 0],
            'Neck': [WIDTH // 2, HEIGHT - 100 + 10 * math.sin(t) - 60, 0],
            'Head': [WIDTH // 2 + 10 * math.sin(t), HEIGHT - 100 + 10 * math.sin(t) - 80, 0],
            'Left Arm': [WIDTH // 2 - 30, HEIGHT - 100 + 10 * math.sin(t) - 40 + 20 * math.sin(t + math.pi / 2), 0],
            'Left Forearm': [WIDTH // 2 - 30 - 20 * math.cos(t), HEIGHT - 100 + 10 * math.sin(t) - 40 + 20 * math.sin(t + math.pi / 2) + 20, 0],
            'Right Arm': [WIDTH // 2 + 30, HEIGHT - 100 + 10 * math.sin(t) - 40 + 20 * math.sin(t - math.pi / 2), 0],
            'Right Forearm': [WIDTH // 2 + 30 + 20 * math.cos(t), HEIGHT - 100 + 10 * math.sin(t) - 40 + 20 * math.sin(t - math.pi / 2) + 20, 0]
        }
        data.append(joints)
    return data

# Generate motion data for 60 frames
motion_data = generate_motion_data(60)

# Main animation loop
frame_index = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Get current frame data
    frame = motion_data[int(frame_index) % len(motion_data)]

    # Draw point lights
    for joint in JOINTS:
        x = int(frame[joint][0])
        y = int(frame[joint][1])
        pygame.draw.circle(screen, WHITE, (x, y), 5)

    # Update display
    pygame.display.flip()

    # Update frame index
    frame_index += ANIMATION_SPEED

    # Cap the frame rate
    clock.tick(FPS)
