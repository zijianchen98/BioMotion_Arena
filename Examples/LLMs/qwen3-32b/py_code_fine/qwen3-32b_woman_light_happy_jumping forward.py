
import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Woman Jumping Forward")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Define the joint positions (15 joints) for a standing woman (in local coordinates)
# These are relative positions of the body joints
# Format: [ (x, y), ... ] for each joint

# Joint indices:
# 0: Head center
# 1: Neck
# 2: Left shoulder
# 3: Right shoulder
# 4: Left elbow
# 5: Right elbow
# 6: Left hand
# 7: Right hand
# 8: Torso center
# 9: Left hip
# 10: Right hip
# 11: Left knee
# 12: Right knee
# 13: Left foot
# 14: Right foot

# Define the basic body structure (in cm or arbitrary units)
body_template = np.array([
    (0, -100),  # Head
    (0, -50),   # Neck
    (-25, 0),   # Left shoulder
    (25, 0),    # Right shoulder
    (-40, 30),  # Left elbow
    (40, 30),   # Right elbow
    (-55, 70),  # Left hand
    (55, 70),   # Right hand
    (0, 0),     # Torso center
    (-20, 40),  # Left hip
    (20, 40),   # Right hip
    (-25, 80),  # Left knee
    (25, 80),   # Right knee
    (-20, 120), # Left foot
    (20, 120)   # Right foot
])

# Convert body_template to a list of tuples for easier manipulation
body_template = [tuple(joint) for joint in body_template]

# Animation parameters
jump_height = 100  # How high the woman jumps
jump_duration = 60  # Frames to complete the jump
gravity = 9.8 / FPS  # Gravity in pixels per frame squared

# Initial position of the body (centered on the screen)
center_x, center_y = WIDTH // 2, HEIGHT // 2

# Scaling factor (pixels per unit)
scale = 2

# Initial joint positions
joints = np.array(body_template)

# Translate to screen center
def translate_to_center(joints, center_x, center_y):
    return joints + np.array([center_x, center_y])

# Jumping animation
jump_phase = 0
jumping = True

# Main loop
while True:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update jump phase
    if jump_phase < jump_duration:
        # Upward motion (accelerate upwards)
        dy = -jump_height * (jump_phase / jump_duration) ** 2
    else:
        # Downward motion (decelerate)
        jump_phase = jump_duration * 2 - jump_phase
        dy = -jump_height * (jump_phase / jump_duration) ** 2
        if jump_phase >= jump_duration * 2:
            jump_phase = 0

    jump_phase += 1

    # Apply jump to the vertical position
    center_y = HEIGHT // 2 + dy

    # Translate and scale the joints
    translated_joints = translate_to_center(joints, center_x, center_y) * scale

    # Draw the point-light stimulus
    for joint in translated_joints:
        pygame.draw.circle(screen, WHITE, (int(joint[0]), int(joint[1])), 5)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)
