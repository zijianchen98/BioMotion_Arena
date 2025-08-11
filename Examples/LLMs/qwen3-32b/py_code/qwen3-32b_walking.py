
import pygame
import sys
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_FRAMES = 60  # Number of frames for one walking cycle
NUM_JOINTS = 15  # 15 joints (point-lights)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Walking")
clock = pygame.time.Clock()

# Load precomputed joint positions (simulating a walking gait)
# This is a simplified simulation of a human walking using 15 joints
# You can replace this with real motion capture data for higher realism
joint_positions = []

# Simulated joint positions (relative to body center)
# The positions are in 3D space and will be projected to 2D for display
# These are example positions for a walking gait (simplified)
def generate_walking_gait():
    positions = []
    for frame in range(NUM_FRAMES):
        # Simulate a walking gait using sine and cosine functions
        # 15 joints: head, neck, thorax, pelvis, left shoulder, left elbow, left hand,
        #            right shoulder, right elbow, right hand, left hip, left knee, left foot,
        #            right hip, right knee, right foot
        # Simplified 3D positions (x, y, z)
        x_offset = np.sin(2 * np.pi * frame / NUM_FRAMES)
        y_offset = np.cos(2 * np.pi * frame / NUM_FRAMES)

        joints = [
            # Head
            (0, 100, 0),
            # Neck
            (0, 80, 0),
            # Thorax
            (0, 60, 0),
            # Pelvis
            (0, 40, 0),
            # Left shoulder
            (-20, 70, 0),
            # Left elbow
            (-40, 70, 0),
            # Left hand
            (-60, 70, 0),
            # Right shoulder
            (20, 70, 0),
            # Right elbow
            (40, 70, 0),
            # Right hand
            (60, 70, 0),
            # Left hip
            (-15, 30, 0),
            # Left knee
            (-30, 10 + 20 * np.sin(2 * np.pi * (frame + 0) / NUM_FRAMES), 0),
            # Left foot
            (-45, 0 + 20 * np.sin(2 * np.pi * (frame + 0) / NUM_FRAMES), 0),
            # Right hip
            (15, 30, 0),
            # Right knee
            (30, 10 + 20 * np.sin(2 * np.pi * (frame + 30) / NUM_FRAMES), 0),
            # Right foot
            (45, 0 + 20 * np.sin(2 * np.pi * (frame + 30) / NUM_FRAMES), 0),
        ]
        # Convert to 2D (projecting z=0)
        projected = [(x + WIDTH // 2, y + HEIGHT // 2) for x, y, z in joints]
        positions.append(projected)
    return positions

joint_positions = generate_walking_gait()

# Main loop
frame_index = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Black background

    # Draw point-lights
    positions = joint_positions[frame_index]
    for x, y in positions:
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(FPS)

    # Update frame index
    frame_index = (frame_index + 1) % NUM_FRAMES
