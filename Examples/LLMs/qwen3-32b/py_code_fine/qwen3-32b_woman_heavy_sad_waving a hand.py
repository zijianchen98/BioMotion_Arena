
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Waving with Heavy Weight")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Joint positions (relative to body center)
# 15 joints: head, chest, pelvis, left shoulder, left elbow, left hand, right shoulder, right elbow, right hand,
#            left hip, left knee, left foot, right hip, right knee, right foot

# Default joint positions (relative to center)
joint_offsets = [
    (0, -100),     # head
    (0, -50),      # chest
    (0, 0),        # pelvis
    (-30, -30),    # left shoulder
    (-60, -10),    # left elbow
    (-90, 20),     # left hand
    (30, -30),     # right shoulder
    (60, -10),     # right elbow
    (90, 20),      # right hand
    (-20, 0),      # left hip
    (-20, 50),     # left knee
    (-20, 90),     # left foot
    (20, 0),       # right hip
    (20, 50),      # right knee
    (20, 90),      # right foot
]

# Joint connections
connections = [
    (0, 1),  # head -> chest
    (1, 2),  # chest -> pelvis
    (2, 3),  # pelvis -> left shoulder
    (3, 4),  # left shoulder -> left elbow
    (4, 5),  # left elbow -> left hand
    (2, 6),  # pelvis -> right shoulder
    (6, 7),  # right shoulder -> right elbow
    (7, 8),  # right elbow -> right hand
    (2, 9),  # pelvis -> left hip
    (9, 10), # left hip -> left knee
    (10, 11),# left knee -> left foot
    (2, 12), # pelvis -> right hip
    (12, 13),# right hip -> right knee
    (13, 14),# right knee -> right foot
]

# Animation parameters
center = [WIDTH // 2, HEIGHT // 2]
angle = 0
waving_arm = 5  # Index of left hand
waving_speed = 0.03
waving_amp = 15
gravity = 0.3
bounce = 0.7
foot_y = 0
foot_speed = 0
sadness = 0.7  # Factor to reduce upward motion

# Main animation loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update waving motion (left hand)
    angle += waving_speed
    dx = waving_amp * math.sin(angle)
    dy = waving_amp * math.cos(angle) * 0.5  # Downward bias for sadness

    # Update left hand position
    joint_offsets[waving_arm] = (-90 + int(dx), 20 + int(dy))

    # Update left shoulder and elbow to follow the hand
    joint_offsets[4] = (-60, -10 + int(dy * 0.5))  # left elbow
    joint_offsets[3] = (-30 + int(dx * 0.5), -30 + int(dy * 0.3))  # left shoulder

    # Simulate heavy weight by limiting hand movement speed
    joint_offsets[waving_arm] = (
        joint_offsets[waving_arm][0] * 0.9,
        joint_offsets[waving_arm][1] * 0.9
    )

    # Draw joints and connections
    points = []
    for i, (x, y) in enumerate(joint_offsets):
        px = center[0] + x
        py = center[1] + y
        points.append((px, py))
        pygame.draw.circle(screen, WHITE, (int(px), int(py)), 5)

    # Draw connections
    for a, b in connections:
        pygame.draw.line(screen, WHITE, points[a], points[b], 2)

    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
