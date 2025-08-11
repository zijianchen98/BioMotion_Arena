
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sadman Jumping (Point-Light Biological Motion)")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate and animation settings
FPS = 30
clock = pygame.time.Clock()

# Number of points and their joint structure
NUM_POINTS = 15
JOINTS = [
    (0, 1), (1, 2), (2, 3),  # Left leg
    (0, 4), (4, 5), (5, 6),  # Right leg
    (0, 7), (7, 8), (8, 9), (9, 10),  # Torso and head
    (7, 11), (11, 12),  # Left arm
    (7, 13), (13, 14),  # Right arm
]

# Initial joint positions relative to center (simplified 2D stick figure)
# Coordinates are in local joint space
JOINT_RELATIVE = np.array([
    [0, 0],  # Hip
    [0, -100],  # Left knee
    [0, -200],  # Left ankle
    [0, -300],  # Left foot

    [0, -100],  # Right knee
    [0, -200],  # Right ankle
    [0, -300],  # Right foot

    [0, -100],  # Torso center
    [0, -150],  # Shoulders center
    [-40, -150],  # Left shoulder
    [-70, -200],  # Left hand
    [40, -150],  # Right shoulder
    [40, -200],  # Right hand

    [0, -100],  # Head
])

# Time-based animation parameters
JUMP_DURATION = 1.5  # seconds
TOTAL_FRAMES = int(FPS * JUMP_DURATION)
GRAVITY = 9.8
AMPLITUDE = 150  # Jump height
TIME = np.linspace(0, JUMP_DURATION, TOTAL_FRAMES)

# Function to simulate jump motion
def jump_position(t):
    # Parabolic motion for vertical jump
    y = AMPLITUDE * (2 * t / JUMP_DURATION - (t / JUMP_DURATION) ** 2)
    return y

# Function to rotate joint around a point
def rotate_point(point, angle, origin):
    x, y = point - origin
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    rx = x * cos_theta - y * sin_theta
    ry = x * sin_theta + y * cos_theta
    return np.array([rx, ry]) + origin

# Main animation loop
frame = 0
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate jump height at current frame
    t = TIME[frame]
    jump_y = jump_position(t)

    # Calculate joint positions
    joint_positions = np.zeros((NUM_POINTS, 2))
    joint_positions[0] = [WIDTH // 2, HEIGHT // 2 - jump_y]  # Hip at center, adjusted for jump

    # Left leg
    joint_positions[1] = joint_positions[0] + rotate_point(JOINT_RELATIVE[1], -0.3 * t, [0, 0])
    joint_positions[2] = joint_positions[1] + rotate_point(JOINT_RELATIVE[2], -0.6 * t, [0, 0])
    joint_positions[3] = joint_positions[2] + rotate_point(JOINT_RELATIVE[3], -0.3 * t, [0, 0])

    # Right leg
    joint_positions[4] = joint_positions[0] + rotate_point(JOINT_RELATIVE[4], 0.3 * t, [0, 0])
    joint_positions[5] = joint_positions[4] + rotate_point(JOINT_RELATIVE[5], 0.6 * t, [0, 0])
    joint_positions[6] = joint_positions[5] + rotate_point(JOINT_RELATIVE[6], 0.3 * t, [0, 0])

    # Torso and head
    joint_positions[7] = joint_positions[0] + rotate_point(JOINT_RELATIVE[7], -0.1 * t, [0, 0])
    joint_positions[8] = joint_positions[7] + rotate_point(JOINT_RELATIVE[8], -0.2 * t, [0, 0])

    # Left arm
    joint_positions[9] = joint_positions[8] + rotate_point(JOINT_RELATIVE[9], 0.4 * t, [0, 0])
    joint_positions[10] = joint_positions[9] + rotate_point(JOINT_RELATIVE[10], 0.6 * t, [0, 0])

    # Right arm
    joint_positions[11] = joint_positions[8] + rotate_point(JOINT_RELATIVE[11], -0.4 * t, [0, 0])
    joint_positions[12] = joint_positions[11] + rotate_point(JOINT_RELATIVE[12], -0.6 * t, [0, 0])

    # Head
    joint_positions[13] = joint_positions[7] + rotate_point(JOINT_RELATIVE[13], -0.1 * t, [0, 0])

    # Draw point-lights
    for i in range(NUM_POINTS):
        pygame.draw.circle(screen, WHITE, (int(joint_positions[i][0]), int(joint_positions[i][1])), 5)

    # Draw joints
    for a, b in JOINTS:
        pygame.draw.line(screen, WHITE, joint_positions[a], joint_positions[b], 2)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)
    frame = (frame + 1) % TOTAL_FRAMES

pygame.quit()
sys.exit()
