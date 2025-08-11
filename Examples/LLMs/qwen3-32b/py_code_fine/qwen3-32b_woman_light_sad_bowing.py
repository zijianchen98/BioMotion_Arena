
import numpy as np
import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Woman Bowing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
CLOCK = pygame.time.Clock()

# Joint positions (simplified for a sad woman bowing)
# The positions are in relative coordinates (0 to 1) and will be scaled to the screen
JOINT_SEQUENCE = np.load("bowing_sequence.npy")  # Assume we have pre-recorded motion data

# If you don't have a .npy file, you can generate a simple sequence manually or use a motion capture dataset

# Scale the joint positions to fit on the screen
SCALE = 200
JOINT_SEQUENCE = JOINT_SEQUENCE * SCALE + [WIDTH / 2, HEIGHT / 2]

# Main loop
frame_idx = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill(BLACK)

    # Draw point lights
    if frame_idx < len(JOINT_SEQUENCE):
        positions = JOINT_SEQUENCE[frame_idx]
        for pos in positions:
            pygame.draw.circle(SCREEN, WHITE, (int(pos[0]), int(pos[1])), 5)

        frame_idx += 1
    else:
        frame_idx = 0  # Loop the animation

    pygame.display.flip()
    CLOCK.tick(FPS)
