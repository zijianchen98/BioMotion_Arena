
import pygame
import sys
import numpy as np
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Woman Jumping")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Time-based animation
frame = 0
phase = 0
jump_height = 100
jump_duration = 60  # frames
gravity = 0.005

# Define joint positions (simplified stick figure: 15 points)
# Joints: [hips, left and right knees, left and right feet, spine, neck, head, left and right shoulders, left and right elbows, left and right hands]

# Rest position (relative to center)
rest_joints = np.array([
    [0, 0],  # hips
    [-30, -40],  # left knee
    [30, -40],  # right knee
    [-30, -70],  # left foot
    [30, -70],  # right foot
    [0, -30],  # spine
    [0, -60],  # neck
    [0, -90],  # head
    [-30, -60],  # left shoulder
    [30, -60],  # right shoulder
    [-45, -90],  # left elbow
    [45, -90],  # right elbow
    [-60, -120],  # left hand
    [60, -120],  # right hand
    [0, -75]  # center of motion (hips)
])

# Normalize rest positions for animation
rest_joints[:, 1] *= -1  # flip y-axis to match screen coordinates

# Motion function: jump up with a sad, light weight motion
def jump_position(frame, jump_duration, jump_height):
    t = frame / jump_duration
    if t < 1:
        # Upward motion with a gentle curve
        y = jump_height * (1 - math.cos(t * math.pi / 2))
    else:
        # Downward motion with a slight delay to look sad
        t = (frame - jump_duration) / jump_duration
        y = jump_height * math.sin(t * math.pi / 2)
    return y

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Center point
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    # Jump height over time
    motion_y = jump_position(frame % (2 * jump_duration), jump_duration, 100)

    # Apply motion to the center of motion (hips)
    rest_joints[-1, 1] = motion_y

    # Compute current joint positions (apply motion to all joints relative to hips)
    joints = rest_joints.copy()
    joints[:, 0] += center_x
    joints[:, 1] += center_y - motion_y

    # Draw point-lights
    for joint in joints:
        pygame.draw.circle(screen, WHITE, (int(joint[0]), int(joint[1])), 5)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)
    frame += 1

pygame.quit()
sys.exit()
