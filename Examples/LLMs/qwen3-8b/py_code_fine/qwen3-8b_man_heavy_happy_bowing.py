
import numpy as np
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Happy Man Bowing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define the 15 point-light positions (approximate joints)
# Based on a happy man bowing motion
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, feet, spine, etc.
# These are simplified and approximate for the animation

# Initial positions (in screen coordinates)
joint_positions = np.array([
    [400, 100],    # Head
    [300, 200],    # Left shoulder
    [250, 300],    # Left elbow
    [230, 400],    # Left wrist
    [350, 200],    # Right shoulder
    [400, 300],    # Right elbow
    [420, 400],    # Right wrist
    [300, 450],    # Left hip
    [350, 450],    # Right hip
    [280, 550],    # Left knee
    [320, 550],    # Right knee
    [260, 600],    # Left ankle
    [340, 600],    # Right ankle
    [300, 400],    # Spine
    [350, 400],    # Pelvis
])

# Animation parameters
amplitude = 50  # Movement amplitude
frequency = 0.01  # Frequency of motion
phase_offset = np.random.rand(15) * 2 * np.pi  # Random phase for each joint

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Update joint positions based on sine wave motion
    for i in range(15):
        angle = frequency * i + phase_offset[i]
        joint_positions[i, 0] += amplitude * np.sin(angle)
        joint_positions[i, 1] += amplitude * np.cos(angle)

        # Constrain positions within screen
        joint_positions[i, 0] = np.clip(joint_positions[i, 0], 0, WIDTH)
        joint_positions[i, 1] = np.clip(joint_positions[i, 1], 0, HEIGHT)

    # Draw point-lights
    for pos in joint_positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
