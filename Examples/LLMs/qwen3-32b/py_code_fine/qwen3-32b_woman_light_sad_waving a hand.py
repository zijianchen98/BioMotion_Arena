
import pygame
import sys
import math
import numpy as np

# Setup
pygame.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Waving Hand - Point Light Display")
clock = pygame.time.Clock()

# Joint positions (relative to a center point)
def get_joint_positions(t):
    # Define the joint positions for a waving hand (simplified)
    # t is the time step in the animation (0 to 1)
    # This is a simplified model with 15 joints
    # We'll simulate a waving hand with a sad posture

    # Center of the body
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    # Joint positions relative to center (simplified skeleton)
    joints = [
        # Head
        (0, -100),
        # Neck
        (0, -60),
        # Left shoulder
        (-30, -30),
        # Right shoulder
        (30, -30),
        # Left elbow
        (-60, 0),
        # Right elbow
        (60, 0),
        # Left hand (waving)
        (-90, 0),
        # Right hand
        (90, 0),
        # Left hip
        (-20, 50),
        # Right hip
        (20, 50),
        # Left knee
        (-20, 100),
        # Right knee
        (20, 100),
        # Left foot
        (-20, 150),
        # Right foot
        (20, 150),
        # Torso center
        (0, 10),
    ]

    # Apply waving motion to the right hand
    wave_amp = 20
    wave_freq = 1.5
    wave_offset = wave_amp * math.sin(2 * math.pi * wave_freq * t)
    joints[7] = (90 + wave_offset, 0)

    # Apply slight head droop for sad expression
    head_drop = 10 * math.sin(2 * math.pi * 0.5 * t)
    joints[0] = (0, -100 + head_drop)

    # Apply positions to screen coordinates
    positions = [(center_x + x, center_y + y) for x, y in joints]
    return positions

# Main loop
frame = 0
total_frames = 120  # 2 seconds of animation at 60 FPS
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current joint positions
    t = frame / total_frames
    positions = get_joint_positions(t)

    # Draw point lights
    for x, y in positions:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()
    frame = (frame + 1) % total_frames

pygame.quit()
sys.exit()
