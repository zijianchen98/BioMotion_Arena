
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Woman Jumping Forward")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Number of points
NUM_POINTS = 15

# Joint positions relative to a central point (in a simplified stick figure style)
# These represent the positions of the joints in a standing posture (relative to center)
# We'll animate them to simulate a sad jump forward

# Define joint positions in a simplified stick figure (in relative coordinates)
JOINTS = {
    'head': (0, -150),
    'neck': (0, -100),
    'torso': (0, 0),
    'left_shoulder': (-30, -50),
    'right_shoulder': (30, -50),
    'left_elbow': (-60, -10),
    'right_elbow': (60, -10),
    'left_hand': (-90, 0),
    'right_hand': (90, 0),
    'left_hip': (-20, 50),
    'right_hip': (20, 50),
    'left_knee': (-20, 120),
    'right_knee': (20, 120),
    'left_ankle': (-20, 200),
    'right_ankle': (20, 200),
}

# Convert joint dictionary to a list for easier handling
joint_names = list(JOINTS.keys())
joint_positions = [JOINTS[name] for name in joint_names]

# Animation parameters
jump_height = 50
jump_duration = 60  # frames
step_duration = 30  # frames
gravity = -9.8  # m/s^2 (simplified)
time = 0
phase = 0  # 0: jump up, 1: jump down, 2: step forward

# Function to animate the jump
def animate_jump(t, duration):
    # Simple parabolic motion
    t /= duration
    if t <= 0.5:
        return jump_height * 4 * t * t
    else:
        t = t - 0.5
        return jump_height * (-4 * t * t + 4 * t + 1)

# Function to animate the sad forward jump
def get_joints(t, duration):
    # t is the current frame in the animation
    # duration is the total number of frames for one full jump cycle

    # Normalize time
    t /= duration

    # Base forward movement
    forward = 100 * t

    # Jump height
    vertical = animate_jump(t, duration)

    # Define joint offsets based on the jump and forward movement
    joints = {}
    for name in joint_names:
        x, y = JOINTS[name]
        # Apply forward and vertical movement
        new_x = x + forward
        new_y = y + vertical
        # Apply some additional joint-specific movement for realism
        if name in ['left_hand', 'right_hand']:
            # Hands move in a sad, floppy way
            new_y += 20 * math.sin(2 * math.pi * t * 2)
        elif name in ['left_knee', 'right_knee']:
            # Knees bend during jump
            bend = 30 * (1 - math.cos(2 * math.pi * t))
            if name == 'left_knee':
                new_y += bend
            else:
                new_y += bend
        elif name in ['left_ankle', 'right_ankle']:
            # Ankles move with knees
            if name == 'left_ankle':
                new_y += 20 * math.sin(2 * math.pi * t)
            else:
                new_y += 20 * math.sin(2 * math.pi * t)
        elif name in ['left_shoulder', 'right_shoulder']:
            # Shoulders slightly lower for sad posture
            new_y += 10 * math.sin(2 * math.pi * t)
        joints[name] = (new_x, new_y)

    return joints

# Main animation loop
running = True
frame = 0
duration = 120  # total frames for one full animation cycle

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Get current joint positions
    joints = get_joints(frame, duration)

    # Draw the point-lights
    for name in joint_names:
        x, y = joints[name]
        # Center the figure on the screen
        px = WIDTH // 2 + x
        py = HEIGHT // 2 + y
        pygame.draw.circle(screen, WHITE, (int(px), int(py)), 5)

    pygame.display.flip()
    clock.tick(FPS)
    frame = (frame + 1) % duration

pygame.quit()
sys.exit()
