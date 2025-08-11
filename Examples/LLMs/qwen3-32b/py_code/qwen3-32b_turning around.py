
import pygame
import math
import sys
import numpy as np

# Define constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NUM_FRAMES = 120  # Total frames for the animation
NUM_LIGHTS = 15

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Turning Around")
clock = pygame.time.Clock()

# Center of the screen
center_x, center_y = WIDTH // 2, HEIGHT // 2

# Define joint positions relative to the center
# This is a simplified model of a person turning around using 15 points
# Each joint is represented as a (x, y) offset from the center
# We'll simulate a turning motion by rotating these points over time

# Joints: head, shoulders, elbows, wrists, hips, knees, ankles
joint_offsets = [
    (0, -100),  # head
    (-20, -60),  # left shoulder
    (-40, -20),  # left elbow
    (-40, 20),   # left wrist
    (-20, 30),   # left hip
    (-20, 60),   # left knee
    (-20, 100),  # left ankle
    (20, -60),   # right shoulder
    (40, -20),   # right elbow
    (40, 20),    # right wrist
    (20, 30),    # right hip
    (20, 60),    # right knee
    (20, 100),   # right ankle
    (-10, 0),    # spine top
    (10, 0),     # spine bottom
]

# Convert joint positions to numpy array for rotation
joint_positions = np.array([(x, y) for x, y in joint_offsets], dtype=np.float32)

# Animation loop
frame = 0
rotation_angle = 0.0
rotation_increment = 2 * math.pi / NUM_FRAMES  # Full rotation over NUM_FRAMES

running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rotate the joint positions
    rotation_angle += rotation_increment
    rotated_joints = np.zeros_like(joint_positions)
    for i, (x, y) in enumerate(joint_positions):
        rotated_x = x * math.cos(rotation_angle) - y * math.sin(rotation_angle)
        rotated_y = x * math.sin(rotation_angle) + y * math.cos(rotation_angle)
        rotated_joints[i] = (rotated_x, rotated_y)

    # Draw the point lights
    for x, y in rotated_joints:
        pygame.draw.circle(screen, WHITE, (int(center_x + x), int(center_y + y)), 5)

    pygame.display.flip()
    frame += 1

pygame.quit()
sys.exit()
