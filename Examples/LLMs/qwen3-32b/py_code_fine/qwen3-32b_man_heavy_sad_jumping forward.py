
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sadman Jumping Forward - Biological Motion")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Point-light positions (relative to body)
# We'll define a basic skeleton of 15 joints:
# 0 - Head
# 1 - Thorax
# 2 - Upper left arm
# 3 - Lower left arm
# 4 - Upper right arm
# 5 - Lower right arm
# 6 - Pelvis
# 7 - Upper left leg
# 8 - Lower left leg
# 9 - Upper right leg
# 10 - Lower right leg
# 11 - Left foot
# 12 - Right foot
# 13 - Left hand
# 14 - Right hand

# Initial joint positions (relative to center)
relative_positions = np.array([
    [0, -100],     # Head
    [0, -50],      # Thorax
    [-30, -20],    # Upper left arm
    [-60, 10],     # Lower left arm
    [30, -20],     # Upper right arm
    [60, 10],      # Lower right arm
    [0, 20],       # Pelvis
    [-20, 50],     # Upper left leg
    [-40, 90],     # Lower left leg
    [20, 50],      # Upper right leg
    [40, 90],      # Lower right leg
    [-40, 130],    # Left foot
    [40, 130],     # Right foot
    [-60, 10],     # Left hand
    [60, 10],      # Right hand
])

# Animation parameters
center_x = WIDTH // 2
center_y = HEIGHT // 2
speed = 2  # Forward speed
jump_height = 0
jump_velocity = 0
gravity = 0.5
max_jump_height = 30
phase = 0

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    clock.tick(FPS)
    SCREEN.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update jump
    jump_velocity -= gravity
    jump_height += jump_velocity
    if jump_height <= 0:
        jump_velocity = 0
        jump_height = 0
        phase = (phase + 0.1) % (2 * math.pi)

    # Apply forward movement
    center_x += speed

    # Calculate joint positions with motion
    positions = relative_positions.copy()

    # Apply forward motion
    positions[:, 0] += center_x
    positions[:, 1] += center_y

    # Apply jump motion to upper body
    positions[[0, 1, 2, 3, 4, 5, 6], 1] += jump_height

    # Apply arm and leg motion (sad and heavy jump)
    arm_angle = math.sin(phase) * 0.5
    leg_angle = math.sin(phase + math.pi) * 0.5

    # Upper arms
    positions[2, 0] = -30 * math.cos(arm_angle) - 20
    positions[2, 1] = -20 * math.sin(arm_angle) - 50
    positions[4, 0] = 30 * math.cos(arm_angle) + 20
    positions[4, 1] = -20 * math.sin(arm_angle) - 50

    # Lower arms
    positions[3, 0] = -60 * math.cos(arm_angle) - 40
    positions[3, 1] = 10 * math.sin(arm_angle) - 40
    positions[5, 0] = 60 * math.cos(arm_angle) + 40
    positions[5, 1] = 10 * math.sin(arm_angle) - 40

    # Upper legs
    positions[7, 0] = -20 * math.cos(leg_angle) - 10
    positions[7, 1] = 50 * math.sin(leg_angle) + 70
    positions[9, 0] = 20 * math.cos(leg_angle) + 10
    positions[9, 1] = 50 * math.sin(leg_angle) + 70

    # Lower legs
    positions[8, 0] = -40 * math.cos(leg_angle) - 20
    positions[8, 1] = 90 * math.sin(leg_angle) + 100
    positions[10, 0] = 40 * math.cos(leg_angle) + 20
    positions[10, 1] = 90 * math.sin(leg_angle) + 100

    # Feet
    positions[11, 0] = -40 * math.cos(leg_angle) - 40
    positions[11, 1] = 130 * math.sin(leg_angle) + 130
    positions[12, 0] = 40 * math.cos(leg_angle) + 40
    positions[12, 1] = 130 * math.sin(leg_angle) + 130

    # Hands
    positions[13, 0] = -60 * math.cos(arm_angle) - 60
    positions[13, 1] = 10 * math.sin(arm_angle) - 30
    positions[14, 0] = 60 * math.cos(arm_angle) + 60
    positions[14, 1] = 10 * math.sin(arm_angle) - 30

    # Draw point-lights
    for x, y in positions:
        pygame.draw.circle(SCREEN, WHITE, (int(x), int(y)), 5)

    pygame.display.flip()

pygame.quit()
sys.exit()
