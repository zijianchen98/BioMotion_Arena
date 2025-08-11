
import numpy as np
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Happy Woman Lying Down with Heavy Weight")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Frame rate
FPS = 30

# Number of joints (point-lights)
NUM_JOINTS = 15

# Joint names for clarity
JOINT_NAMES = [
    "Head", "Neck", "Left Shoulder", "Right Shoulder", "Left Elbow",
    "Right Elbow", "Left Wrist", "Right Wrist", "Left Hip", "Right Hip",
    "Left Knee", "Right Knee", "Left Ankle", "Right Ankle", "Torso Center"
]

# Initial joint positions (relative to a central point)
# These positions are in local space and will be transformed for animation
initial_positions = np.array([
    [0, -100],       # Head
    [0, -50],        # Neck
    [-30, -40],      # Left Shoulder
    [30, -40],       # Right Shoulder
    [-40, -10],      # Left Elbow
    [40, -10],       # Right Elbow
    [-45, 10],       # Left Wrist
    [45, 10],        # Right Wrist
    [-25, 50],       # Left Hip
    [25, 50],        # Right Hip
    [-40, 90],       # Left Knee
    [40, 90],        # Right Knee
    [-50, 130],      # Left Ankle
    [50, 130],       # Right Ankle
    [0, 0]           # Torso Center
], dtype=np.float32)

# Animation parameters
center_x, center_y = WIDTH // 2, HEIGHT // 2
scale = 3  # Scale the joint positions for visibility
angle = 0  # Initial rotation angle
rotation_speed = 0.02  # Slow rotation for natural movement
gravity = 0.1  # Gravity effect for realism

# Movement simulation for lying down with heavy weight
# We simulate a slow, heavy, and happy motion of the body
def animate_joints(t):
    """Animate joints to simulate a happy woman lying down with heavy weight."""
    # Base movement (lying down)
    base_y = 100 * np.sin(t * 0.5)  # Slow up and down movement for the body
    base_x = 10 * np.sin(t * 0.3)   # Slight side-to-side movement

    # Joint positions relative to base
    positions = initial_positions.copy()

    # Apply body tilt
    tilt = 0.1 * np.sin(t * 0.4)  # Slow body tilt

    # Apply a simulated heavy weight to lower body
    weight_factor = 1.2 + 0.2 * np.sin(t * 0.3)

    # Apply transformations
    for i in range(NUM_JOINTS):
        x, y = positions[i]
        # Apply base movement
        positions[i][0] += base_x
        positions[i][1] += base_y
        # Apply tilt
        positions[i][0] += y * tilt
        # Apply weight to lower body
        if i in [8, 9, 10, 11, 12, 13]:  # Hips, knees, ankles
            positions[i][1] += y * (weight_factor - 1)
        # Apply gravity
        positions[i][1] += gravity * t

    return positions

# Main loop
running = True
t = 0  # Animation time parameter
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Animate the joints
    positions = animate_joints(t)

    # Rotate the entire body for natural motion
    rotated_positions = []
    for x, y in positions:
        # Rotate around the torso center
        x_rot = x * np.cos(angle) - y * np.sin(angle)
        y_rot = x * np.sin(angle) + y * np.cos(angle)
        rotated_positions.append([x_rot, y_rot])

    # Scale and translate to screen coordinates
    screen_positions = []
    for x, y in rotated_positions:
        sx = int(center_x + x * scale)
        sy = int(center_y + y * scale)
        screen_positions.append((sx, sy))

    # Draw point-lights (joints)
    for pos in screen_positions:
        pygame.draw.circle(screen, WHITE, pos, 5)

    # Update the display
    pygame.display.flip()

    # Increment time and angle
    t += 0.1
    angle += rotation_speed

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
