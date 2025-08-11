
import pygame
import math
import sys
import numpy as np

# Set up constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_FRAMES = 120
NUM_JOINTS = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define joint indices for biological motion
# 0: head, 1: neck, 2: spine, 3: pelvis
# 4: left shoulder, 5: left elbow, 6: left hand
# 7: right shoulder, 8: right elbow, 9: right hand
# 10: left hip, 11: left knee, 12: left foot
# 13: right hip, 14: right knee, 15: right foot

# Define joint positions over time (simplified walking animation)
# This is a basic simulation of a walking motion with 15 joints
# Each joint has a list of positions over time (x, y)

def generate_walking_animation():
    # Generate positions for each joint over time
    positions = [[] for _ in range(NUM_JOINTS)]
    for t in range(NUM_FRAMES):
        # Head
        positions[0].append((WIDTH // 2, 100 + 10 * math.sin(t * 0.1)))
        # Neck
        positions[1].append((WIDTH // 2, 120 + 10 * math.sin(t * 0.1)))
        # Spine
        positions[2].append((WIDTH // 2, 140 + 10 * math.sin(t * 0.1)))
        # Pelvis
        positions[3].append((WIDTH // 2, 160 + 10 * math.sin(t * 0.1)))

        # Left shoulder
        positions[4].append((WIDTH // 2 - 50 - 20 * math.sin(t * 0.3), 130 + 10 * math.sin(t * 0.1)))
        # Left elbow
        positions[5].append((WIDTH // 2 - 100 - 20 * math.sin(t * 0.3), 140 + 10 * math.sin(t * 0.1)))
        # Left hand
        positions[6].append((WIDTH // 2 - 150 - 20 * math.sin(t * 0.3), 150 + 10 * math.sin(t * 0.1)))

        # Right shoulder
        positions[7].append((WIDTH // 2 + 50 + 20 * math.sin(t * 0.3), 130 + 10 * math.sin(t * 0.1)))
        # Right elbow
        positions[8].append((WIDTH // 2 + 100 + 20 * math.sin(t * 0.3), 140 + 10 * math.sin(t * 0.1)))
        # Right hand
        positions[9].append((WIDTH // 2 + 150 + 20 * math.sin(t * 0.3), 150 + 10 * math.sin(t * 0.1)))

        # Left hip
        positions[10].append((WIDTH // 2 - 30 - 20 * math.sin(t * 0.2), 170 + 10 * math.sin(t * 0.1)))
        # Left knee
        positions[11].append((WIDTH // 2 - 70 - 20 * math.sin(t * 0.2), 200 + 30 * math.sin(t * 0.4)))
        # Left foot
        positions[12].append((WIDTH // 2 - 110 - 20 * math.sin(t * 0.2), 230 + 30 * math.sin(t * 0.4)))

        # Right hip
        positions[13].append((WIDTH // 2 + 30 + 20 * math.sin(t * 0.2), 170 + 10 * math.sin(t * 0.1)))
        # Right knee
        positions[14].append((WIDTH // 2 + 70 + 20 * math.sin(t * 0.2), 200 + 30 * math.sin(t * 0.4)))
        # Right foot
        positions[15].append((WIDTH // 2 + 110 + 20 * math.sin(t * 0.2), 230 + 30 * math.sin(t * 0.4)))

    return positions

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happyman Walking")
clock = pygame.time.Clock()

# Generate the walking animation
positions = generate_walking_animation()

# Main animation loop
frame = 0
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Draw the point-light stimulus for the current frame
    for i in range(NUM_JOINTS):
        x, y = positions[i][frame]
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()

    # Update the frame
    frame = (frame + 1) % NUM_FRAMES

pygame.quit()
sys.exit()
