
import pygame
import math
import sys
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_POINTS = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Walking - Point-Light Animation")
clock = pygame.time.Clock()

# Skeleton joint indices for a sad walking motion
JOINTS = [
    "Pelvis",      # 0
    "Left Hip",    # 1
    "Right Hip",   # 2
    "Left Knee",   # 3
    "Right Knee",  # 4
    "Left Ankle",  # 5
    "Right Ankle", # 6
    "Left Foot",   # 7
    "Right Foot",  # 8
    "Spine",       # 9
    "Chest",       # 10
    "Neck",        # 11
    "Head",        # 12
    "Left Shoulder", # 13
    "Right Shoulder" # 14
]

# Sad walking motion (simplified 2D positions over time)
# Each joint's position is a sine wave with different phase and amplitude
# to simulate a sad, slow, and heavy walking motion

# Amplitudes and phases for each joint
amplitudes = [
    0.0,       # Pelvis
    0.5,       # Left Hip
    0.5,       # Right Hip
    0.3,       # Left Knee
    0.3,       # Right Knee
    0.2,       # Left Ankle
    0.2,       # Right Ankle
    0.1,       # Left Foot
    0.1,       # Right Foot
    0.1,       # Spine
    0.1,       # Chest
    0.05,      # Neck
    0.05,      # Head
    0.3,       # Left Shoulder
    0.3        # Right Shoulder
]

phases = [
    0,         # Pelvis
    0,         # Left Hip
    math.pi,   # Right Hip (opposite phase)
    0.5,       # Left Knee
    0.5 + math.pi, # Right Knee (opposite phase)
    1.0,       # Left Ankle
    1.0 + math.pi, # Right Ankle
    1.5,       # Left Foot
    1.5 + math.pi, # Right Foot
    0.2,       # Spine
    0.4,       # Chest
    0.6,       # Neck
    0.8,       # Head
    1.0,       # Left Shoulder
    1.0 + math.pi  # Right Shoulder
]

# Base positions (center of screen)
base_x = WIDTH // 2
base_y = HEIGHT // 2

# Animation parameters
time = 0.0
speed = 0.03  # slower speed for sad walking

def get_position(joint_index, time):
    amp = amplitudes[joint_index]
    phase = phases[joint_index]
    x_offset = amp * math.sin(time + phase)
    y_offset = amp * math.cos(time + phase) * 0.5  # smaller vertical movement for sad walk
    return (base_x + x_offset * 100, base_y + y_offset * 100)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    time += speed

    # Draw points
    for i in range(NUM_POINTS):
        x, y = get_position(i, time)
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
