
import pygame
import math
import sys
import numpy as np

# Pygame initialization
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Woman Lying Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 30

# Number of joints (point-lights)
NUM_JOINTS = 15

# Joint names for clarity
JOINT_NAMES = [
    "Head", "Neck", "Shoulder Left", "Shoulder Right",
    "Elbow Left", "Elbow Right", "Hand Left", "Hand Right",
    "Hip Center", "Hip Left", "Hip Right", "Knee Left",
    "Knee Right", "Ankle Left", "Ankle Right"
]

# Create a simple motion sequence for "lying down"
# This is a simplified 2D representation of the motion
def generate_motion_sequence(frames):
    motion = []
    for frame in range(frames):
        # Base positions (centered at the screen)
        head = (400, 100 - 20 * math.sin(frame * 0.1))
        neck = (400, 120)
        shoulder_left = (380, 140)
        shoulder_right = (420, 140)
        elbow_left = (360, 160 + 10 * math.sin(frame * 0.2))
        elbow_right = (440, 160 + 10 * math.sin(frame * 0.2))
        hand_left = (340, 180)
        hand_right = (460, 180)
        hip_center = (400, 220)
        hip_left = (380, 240)
        hip_right = (420, 240)
        knee_left = (360, 260 + 10 * math.sin(frame * 0.15))
        knee_right = (440, 260 + 10 * math.sin(frame * 0.15))
        ankle_left = (340, 280)
        ankle_right = (460, 280)

        # Store as a list of (x, y) tuples
        frame_data = [
            head, neck, shoulder_left, shoulder_right,
            elbow_left, elbow_right, hand_left, hand_right,
            hip_center, hip_left, hip_right, knee_left,
            knee_right, ankle_left, ankle_right
        ]
        motion.append(frame_data)
    return motion

# Generate motion sequence (100 frames)
motion_sequence = generate_motion_sequence(100)

# Main animation loop
frame_index = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Get current frame's joint positions
    current_frame = motion_sequence[frame_index]

    # Draw each joint as a white point-light
    for joint in current_frame:
        pygame.draw.circle(screen, WHITE, (int(joint[0]), int(joint[1])), 5)

    # Update display
    pygame.display.flip()

    # Move to next frame
    frame_index = (frame_index + 1) % len(motion_sequence)

    # Control frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
