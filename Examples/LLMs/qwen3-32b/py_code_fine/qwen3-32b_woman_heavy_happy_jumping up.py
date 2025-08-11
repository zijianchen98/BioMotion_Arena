
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Woman Jumping Up")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Frame rate
FPS = 30

# Joint positions relative to the body (in a jumping motion)
# These are simplified and stylized for a happy jump with heavy weight
# We will animate these points over time

# Number of joints
NUM_JOINTS = 15

# Initial joint positions (relative to body center)
joint_positions = [
    (0, 0),  # Center of mass (hips)
    (-20, -40),  # Left shoulder
    (20, -40),  # Right shoulder
    (-10, -70),  # Left elbow
    (10, -70),  # Right elbow
    (-30, -100),  # Left hand
    (30, -100),  # Right hand
    (-20, 20),  # Left hip
    (20, 20),  # Right hip
    (-40, 50),  # Left knee
    (40, 50),  # Right knee
    (-60, 80),  # Left foot
    (60, 80),  # Right foot
    (-20, -20),  # Head
    (20, -20),  # Head (top of head)
]

# Convert to numpy for easier manipulation
joint_positions = np.array(joint_positions, dtype=float)

# Animation parameters
jump_phase = 0.0  # 0 to 1.0 for the jump cycle
jump_speed = 0.005  # Speed of the jump cycle

# Function to animate the jump with a happy, heavy motion
def animate_jump(joint_positions, phase):
    # Body lift and drop based on phase
    lift_factor = math.sin(math.pi * phase)  # Lift up in the middle of the jump
    # Add exaggerated bounce effect
    bounce = 0.3 * math.sin(2 * math.pi * phase)
    # Apply vertical lift and bounce
    joint_positions[:, 1] = joint_positions[:, 1] * (1 + 0.1 * lift_factor) - 10 * lift_factor - 5 * bounce
    # Apply horizontal motion for a happy, bouncy jump
    joint_positions[:, 0] = joint_positions[:, 0] * (1 + 0.05 * lift_factor)

    return joint_positions

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update animation phase
    jump_phase += jump_speed
    if jump_phase >= 1.0:
        jump_phase = 0.0

    # Animate the joints
    animated_joints = animate_jump(joint_positions.copy(), jump_phase)

    # Center the body on screen
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    for x, y in animated_joints:
        px = int(center_x + x)
        py = int(center_y + y)
        pygame.draw.circle(screen, WHITE, (px, py), 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
