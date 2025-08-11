
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Woman Jumping")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
CLOCK = pygame.time.Clock()

# Joint positions (simplified skeleton with 15 points)
# This is a basic 2D point-light model of a human with 15 joints
# Coordinates are in normalized space and will be scaled to screen size
JOINTS = [
    [0.5, 0.6],   # Center of mass (hip)
    [0.4, 0.65],  # Left hip
    [0.6, 0.65],  # Right hip
    [0.4, 0.45],  # Left knee
    [0.6, 0.45],  # Right knee
    [0.4, 0.25],  # Left ankle
    [0.6, 0.25],  # Right ankle
    [0.5, 0.5],   # Spine
    [0.45, 0.4],  # Left shoulder
    [0.55, 0.4],  # Right shoulder
    [0.4, 0.3],   # Left elbow
    [0.55, 0.3],  # Right elbow
    [0.4, 0.15],  # Left hand
    [0.55, 0.15], # Right hand
    [0.5, 0.3],   # Head
]

# Animation parameters
jump_height = 0.15
jump_speed = 0.005
jump_phase = 0
jump_duration = 2 * math.pi  # One full jump cycle

# Function to scale joints to screen coordinates
def scale_joints(joints, width, height):
    scaled = []
    for x, y in joints:
        sx = x * width
        sy = y * height
        scaled.append((sx, sy))
    return scaled

# Function to animate the jump
def animate_jump(joints, phase):
    animated = joints.copy()
    # Move the hips up and down
    animated[0][1] -= jump_height * math.sin(phase)
    animated[1][1] -= jump_height * math.sin(phase) * 0.7
    animated[2][1] -= jump_height * math.sin(phase) * 0.7
    animated[4][1] -= jump_height * math.sin(phase) * 0.5
    animated[5][1] -= jump_height * math.sin(phase) * 0.3
    animated[6][1] -= jump_height * math.sin(phase) * 0.3
    animated[8][1] += jump_height * math.sin(phase) * 0.3
    animated[9][1] += jump_height * math.sin(phase) * 0.3
    animated[10][1] += jump_height * math.sin(phase) * 0.5
    animated[11][1] += jump_height * math.sin(phase) * 0.5
    animated[12][1] += jump_height * math.sin(phase) * 0.7
    animated[13][1] += jump_height * math.sin(phase) * 0.7
    animated[14][1] -= jump_height * math.sin(phase)
    return animated

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    SCREEN.fill(BLACK)

    # Animate the joints
    jump_phase += jump_speed
    if jump_phase > jump_duration:
        jump_phase = 0
    joints_animated = animate_jump(JOINTS, jump_phase)
    joints_scaled = scale_joints(joints_animated, WIDTH, HEIGHT)

    # Draw point-lights
    for x, y in joints_scaled:
        pygame.draw.circle(SCREEN, WHITE, (int(x), int(y)), 6)

    # Update display
    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
sys.exit()
