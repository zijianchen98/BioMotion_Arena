
import pygame
import math
import sys
import numpy as np
from pygame.locals import *

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Woman Jumping Forward")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Joint positions (relative to body) - 15 joints
# These are approximate joint positions for a standing human (in cm)
# Joints: head, neck, thorax, left shoulder, left elbow, left hand,
#          right shoulder, right elbow, right hand,
#          left hip, left knee, left foot,
#          right hip, right knee, right foot
JOINTS = [
    (0, -90),   # Head
    (0, -80),   # Neck
    (0, -60),   # Thorax
    (-20, -50), # Left Shoulder
    (-20, -30), # Left Elbow
    (-20, 0),   # Left Hand
    (20, -50),  # Right Shoulder
    (20, -30),  # Right Elbow
    (20, 0),    # Right Hand
    (-15, -40), # Left Hip
    (-15, -10), # Left Knee
    (-15, 20),  # Left Foot
    (15, -40),  # Right Hip
    (15, -10),  # Right Knee
    (15, 20)    # Right Foot
]

# Convert joint positions to a numpy array for easier manipulation
JOINTS = np.array(JOINTS, dtype=float)

# Animation parameters
JUMP_DURATION = 100  # frames
TOTAL_FRAMES = 300   # total animation duration
GRAVITY = 0.3        # gravity strength
JUMP_HEIGHT = 50     # jump height in animation units
WALK_SPEED = 2       # horizontal speed

# Initialize joint positions and velocities
positions = JOINTS.copy()
velocities = np.zeros_like(JOINTS)

# Define a simple jump and forward motion
def animate(frame):
    t = frame / TOTAL_FRAMES
    jump_phase = (frame % JUMP_DURATION) / JUMP_DURATION

    # Jumping motion
    jump_offset = JUMP_HEIGHT * (2 * jump_phase - 1) * (1 - abs(2 * jump_phase - 1))
    positions[:, 1] = JOINTS[:, 1] + jump_offset

    # Forward motion
    positions[:, 0] = JOINTS[:, 0] + WALK_SPEED * frame

    # Apply some walking-like leg movement
    leg_offset = 10 * math.sin(2 * math.pi * t)
    positions[10, 0] = JOINTS[10, 0] + leg_offset
    positions[12, 0] = JOINTS[12, 0] - leg_offset

    leg_offset = 5 * math.sin(2 * math.pi * t + math.pi)
    positions[11, 0] = JOINTS[11, 0] + leg_offset
    positions[13, 0] = JOINTS[13, 0] - leg_offset

    # Arm swing
    arm_offset = 5 * math.sin(2 * math.pi * t)
    positions[3, 0] = JOINTS[3, 0] + arm_offset
    positions[6, 0] = JOINTS[6, 0] - arm_offset

    return positions

# Main loop
frame = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(BLACK)

    # Update animation
    positions = animate(frame)

    # Draw the point-light stimulus
    for x, y in positions:
        pygame.draw.circle(screen, WHITE, (int(x) + WIDTH // 2, int(y) + HEIGHT // 2), 5)

    pygame.display.flip()
    clock.tick(FPS)
    frame = (frame + 1) % TOTAL_FRAMES

pygame.quit()
sys.exit()
