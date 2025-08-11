
import numpy as np
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Jumping Man")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define body joints and their connections (simplified skeleton)
body_joints = [
    ("hips", (400, 300)),
    ("left_hip", (380, 320)),
    ("left_knee", (350, 360)),
    ("left_ankle", (320, 400)),
    ("right_hip", (420, 320)),
    ("right_knee", (450, 360)),
    ("right_ankle", (480, 400)),
    ("torso", (400, 250)),
    ("chest", (400, 220)),
    ("neck", (400, 200)),
    ("head", (400, 170)),
    ("left_shoulder", (360, 230)),
    ("left_elbow", (330, 260)),
    ("left_wrist", (300, 290)),
    ("right_shoulder", (440, 230)),
    ("right_elbow", (470, 260)),
    ("right_wrist", (500, 290)),
]

# Create a list of joint positions
joint_positions = [pos for (_, pos) in body_joints]

# Define motion parameters for jumping
gravity = 0.5
velocity = 10
jump_height = 100
jump_duration = 150  # frames

# Initialize joint positions
joint_positions = [np.array(pos) for (_, pos) in body_joints]

# Time variables
time = 0
jumping = False
jump_phase = 0
jump_frame = 0

# Animation loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simulate jumping motion
    if not jumping:
        # Start jump
        jumping = True
        jump_phase = 0
        jump_frame = 0
    else:
        # Jumping phase
        if jump_frame < jump_duration:
            # Calculate jump position
            jump_phase = jump_frame / jump_duration
            jump_y = 300 - jump_height * (math.sin(math.pi * jump_phase))
            for i, pos in enumerate(joint_positions):
                joint_positions[i][1] = pos[1] + (jump_y - 300)
            jump_frame += 1
        else:
            # Landing phase
            jumping = False
            jump_frame = 0

    # Draw joints as point lights
    for pos in joint_positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 5)

    # Draw skeleton lines
    for i in range(len(body_joints) - 1):
        start = joint_positions[i]
        end = joint_positions[i + 1]
        pygame.draw.line(screen, WHITE, (int(start[0]), int(start[1])), (int(end[0]), int(end[1])), 2)

    pygame.display.flip()

pygame.quit()
