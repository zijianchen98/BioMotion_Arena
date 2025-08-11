
import pygame
import math
import sys
import numpy as np

# Set up display
WIDTH, HEIGHT = 800, 600
FPS = 60

# Define joint positions for a simplified 15-point stick figure
# We'll simulate a bowing motion using sine functions to control joint positions over time
# Initial joint positions (relative to body center)
JOINTS = [
    # Head
    (0, -100),
    # Torso top
    (0, -50),
    # Left shoulder
    (-25, 0),
    # Left elbow
    (-45, 30),
    # Left hand
    (-60, 60),
    # Right shoulder
    (25, 0),
    # Right elbow
    (45, 30),
    # Right hand
    (60, 60),
    # Pelvis
    (0, 50),
    # Left hip
    (-20, 70),
    # Left knee
    (-30, 110),
    # Left foot
    (-30, 150),
    # Right hip
    (20, 70),
    # Right knee
    (30, 110),
    # Right foot
    (30, 150),
]

# Convert joint positions to numpy array for easier manipulation
JOINTS = np.array(JOINTS, dtype=float)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Bowing - Point-Light Display")
clock = pygame.time.Clock()

def bowing_animation(t, joints):
    """Simulate a bowing motion by adjusting joint positions based on time t."""
    bow_angle = math.sin(t * 0.5) * 0.3  # Control the bow angle
    sway = math.sin(t * 1.0) * 5         # Add a subtle side-to-side sway

    # Torso bending
    joints[1][1] += bow_angle * 100  # Torso top
    joints[2][1] += bow_angle * 80   # Left shoulder
    joints[3][1] += bow_angle * 70   # Left elbow
    joints[4][1] += bow_angle * 60   # Left hand
    joints[5][1] += bow_angle * 80   # Right shoulder
    joints[6][1] += bow_angle * 70   # Right elbow
    joints[7][1] += bow_angle * 60   # Right hand

    # Head tilts down with the bow
    joints[0][1] += bow_angle * 100

    # Swaying left and right
    joints[1][0] += sway
    joints[2][0] += sway
    joints[3][0] += sway
    joints[4][0] += sway
    joints[5][0] -= sway
    joints[6][0] -= sway
    joints[7][0] -= sway

    return joints

def draw_point_lights(positions):
    """Draw white circles at each joint position."""
    for pos in positions:
        pygame.draw.circle(screen, (255, 255, 255), (int(pos[0] + WIDTH // 2), int(pos[1] + HEIGHT // 2)), 5)

# Main loop
t = 0
running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Animate the bowing motion
    animated_joints = bowing_animation(t, JOINTS.copy())

    # Draw the point-light display
    draw_point_lights(animated_joints)

    pygame.display.flip()
    t += 0.1

pygame.quit()
sys.exit()
