
import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Woman Running with Heavy Weight")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Define the joint positions (relative to the body)
# We will model a 2D stick figure with 15 joints
# The positions will be updated dynamically to simulate running

# Initial joint positions (relative to center)
joint_names = [
    'head', 'neck', 'torso', 'left shoulder', 'left elbow', 'left hand',
    'right shoulder', 'right elbow', 'right hand', 'left hip', 'left knee',
    'left foot', 'right hip', 'right knee', 'right foot'
]

# Joint indices
HEAD = 0
NECK = 1
TORSO = 2
LEFT_SHOULDER = 3
LEFT_ELBOW = 4
LEFT_HAND = 5
RIGHT_SHOULDER = 6
RIGHT_ELBOW = 7
RIGHT_HAND = 8
LEFT_HIP = 9
LEFT_KNEE = 10
LEFT_FOOT = 11
RIGHT_HIP = 12
RIGHT_KNEE = 13
RIGHT_FOOT = 14

# Initial joint positions (relative to center)
joint_positions = np.array([
    [0, -100],  # head
    [0, -60],   # neck
    [0, 0],     # torso
    [-30, 0],   # left shoulder
    [-30, 40],  # left elbow
    [-30, 80],  # left hand
    [30, 0],    # right shoulder
    [30, 40],   # right elbow
    [30, 80],   # right hand
    [-20, 0],   # left hip
    [-20, 40],  # left knee
    [-20, 80],  # left foot
    [20, 0],    # right hip
    [20, 40],   # right knee
    [20, 80],   # right foot
], dtype=np.float32)

# Animation parameters
center = np.array([WIDTH // 2, HEIGHT // 2], dtype=np.float32)
speed = 2.0  # forward speed
animation_speed = 0.05  # controls the speed of the motion cycle

# Define the motion as a function of time
def update_joint_positions(t):
    # t is a time parameter
    # We will animate the legs and arms to simulate running
    # The motion will be slower and more labored to represent a sad woman with heavy weight

    # Leg motion: slow and with a slight limp
    leg_angle = t * 0.5  # slower leg motion
    left_leg_angle = math.sin(leg_angle)
    right_leg_angle = math.sin(leg_angle + math.pi)

    # Arm motion: arms move in sync with legs, but with reduced amplitude
    arm_angle = t * 0.5
    left_arm_angle = math.sin(arm_angle)
    right_arm_angle = math.sin(arm_angle + math.pi)

    # Head and torso bobbing
    head_bob = math.sin(t * 0.3) * 5  # small up-down motion

    # Update joint positions
    joint_positions[HEAD] = [0, -100 + head_bob]
    joint_positions[NECK] = [0, -60 + head_bob]
    joint_positions[TORSO] = [0, 0 + head_bob]

    # Left arm
    joint_positions[LEFT_SHOULDER] = [-30, 0 + left_arm_angle * 20]
    joint_positions[LEFT_ELBOW] = [-30 + left_arm_angle * 10, 40 + left_arm_angle * 20]
    joint_positions[LEFT_HAND] = [-30 + left_arm_angle * 20, 80 + left_arm_angle * 20]

    # Right arm
    joint_positions[RIGHT_SHOULDER] = [30, 0 + right_arm_angle * 20]
    joint_positions[RIGHT_ELBOW] = [30 + right_arm_angle * 10, 40 + right_arm_angle * 20]
    joint_positions[RIGHT_HAND] = [30 + right_arm_angle * 20, 80 + right_arm_angle * 20]

    # Left leg (slow and heavy)
    joint_positions[LEFT_HIP] = [-20, 0 + left_leg_angle * 10]
    joint_positions[LEFT_KNEE] = [-20 + left_leg_angle * 10, 40 + left_leg_angle * 20]
    joint_positions[LEFT_FOOT] = [-20 + left_leg_angle * 20, 80 + left_leg_angle * 20]

    # Right leg
    joint_positions[RIGHT_HIP] = [20, 0 + right_leg_angle * 10]
    joint_positions[RIGHT_KNEE] = [20 + right_leg_angle * 10, 40 + right_leg_angle * 20]
    joint_positions[RIGHT_FOOT] = [20 + right_leg_angle * 20, 80 + right_leg_angle * 20]

    # Move forward
    joint_positions[:, 0] += speed

    # Reset if off-screen
    if joint_positions[TORSO][0] > WIDTH + 100:
        joint_positions[:, 0] = [0, 0, 0, -30, -30, -30, 30, 30, 30, -20, -20, -20, 20, 20, 20]
        joint_positions[:, 1] = [-100, -60, 0, 0, 40, 80, 0, 40, 80, 0, 40, 80, 0, 40, 80]

# Main animation loop
t = 0.0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update joint positions
    update_joint_positions(t)

    # Translate to center
    joint_positions[:, 0] += center[0]
    joint_positions[:, 1] += center[1]

    # Draw point lights
    for x, y in joint_positions:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    # Update display
    pygame.display.flip()

    # Increment time
    t += animation_speed

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
