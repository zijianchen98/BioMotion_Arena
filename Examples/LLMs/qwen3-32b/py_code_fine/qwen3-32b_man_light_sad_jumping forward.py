
import numpy as np
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Man Jumping Forward")
clock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Joint indices for a 15-point biological motion model
JOINTS = [
    "head",        # 0
    "neck",        # 1
    "left shoulder",# 2
    "right shoulder",# 3
    "left elbow",  # 4
    "right elbow", # 5
    "left hand",   # 6
    "right hand",  # 7
    "torso",       # 8
    "left hip",    # 9
    "right hip",   # 10
    "left knee",   # 11
    "right knee",  # 12
    "left foot",   # 13
    "right foot"   # 14
]

# Initial joint positions (in local coordinates relative to the body center)
# These positions are for a standing pose
joint_positions = np.array([
    [0, -100],   # head
    [0, -60],    # neck
    [-30, -30],  # left shoulder
    [30, -30],   # right shoulder
    [-60, 0],    # left elbow
    [60, 0],     # right elbow
    [-90, -10],  # left hand
    [90, -10],   # right hand
    [0, 0],      # torso
    [-30, 40],   # left hip
    [30, 40],    # right hip
    [-30, 80],   # left knee
    [30, 80],    # right knee
    [-30, 110],  # left foot
    [30, 110]    # right foot
], dtype=np.float32)

# Define the jump parameters
jump_height = 50
jump_duration = 120  # frames
gravity = 9.81 / FPS  # convert gravity to per frame
velocity_y = math.sqrt(2 * gravity * jump_height)

# Animation timing
frame = 0
jump_phase = 0  # 0: ascent, 1: peak, 2: descent
jump_frame = 0

# Arm and leg motion for a sad jump (slower, less exaggerated)
arm_angle = 0
leg_angle = 0
arm_speed = 0.03
leg_speed = 0.02

# Main animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update jump phase
    jump_frame += 1
    if jump_frame < jump_duration // 2:
        # Ascent
        joint_positions[:, 1] -= velocity_y
        velocity_y -= gravity
    elif jump_frame < jump_duration:
        # Descent
        joint_positions[:, 1] -= velocity_y
        velocity_y -= gravity
    else:
        jump_frame = 0
        velocity_y = math.sqrt(2 * gravity * jump_height)
        joint_positions[:, 1] = np.array([
            -100, -60, -30, 30, -60, 60, -90, 90, 0, -30, 30, -30, 30, -30, 30
        ])

    # Apply sad arm motion (slower, less movement)
    arm_angle += arm_speed
    joint_positions[2, 0] = -30 + 10 * math.sin(arm_angle)  # left shoulder
    joint_positions[4, 0] = -60 + 10 * math.sin(arm_angle)  # left elbow
    joint_positions[6, 0] = -90 + 10 * math.sin(arm_angle)  # left hand
    joint_positions[3, 0] = 30 + 10 * math.sin(arm_angle + math.pi)  # right shoulder
    joint_positions[5, 0] = 60 + 10 * math.sin(arm_angle + math.pi)  # right elbow
    joint_positions[7, 0] = 90 + 10 * math.sin(arm_angle + math.pi)  # right hand

    # Apply sad leg motion (slower, less movement)
    leg_angle += leg_speed
    joint_positions[9, 0] = -30 + 10 * math.sin(leg_angle)  # left hip
    joint_positions[11, 0] = -30 + 10 * math.sin(leg_angle)  # left knee
    joint_positions[13, 0] = -30 + 10 * math.sin(leg_angle)  # left foot
    joint_positions[10, 0] = 30 + 10 * math.sin(leg_angle + math.pi)  # right hip
    joint_positions[12, 0] = 30 + 10 * math.sin(leg_angle + math.pi)  # right knee
    joint_positions[14, 0] = 30 + 10 * math.sin(leg_angle + math.pi)  # right foot

    # Draw point lights
    for pos in joint_positions:
        pygame.draw.circle(screen, WHITE, (int(WIDTH / 2 + pos[0]), int(HEIGHT / 2 + pos[1])), 5)

    pygame.display.flip()
    clock.tick(FPS)
    frame += 1

pygame.quit()
sys.exit()
