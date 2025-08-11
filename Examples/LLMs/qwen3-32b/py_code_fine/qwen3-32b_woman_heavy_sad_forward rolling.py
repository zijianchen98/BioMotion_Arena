
import pygame
import sys
import math
import numpy as np
from pygame.locals import *

# Set up the display
WIDTH, HEIGHT = 800, 600
FPS = 60
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman with Heavy Weight - Forward Rolling (Point-Light Display)")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
num_frames = 120
frame_rate = 10  # 120 frames over 10 fps = 12 seconds

# Define joint positions for a sad woman with heavy weight forward rolling
# Each frame is a 2D coordinate for each of the 15 joints
# These are simplified for point-light display and should be manually adjusted to simulate the motion
# The joints are:
# 1. Head, 2. Neck, 3. Spine, 4. Pelvis,
# 5. Left Shoulder, 6. Left Elbow, 7. Left Wrist,
# 8. Right Shoulder, 9. Right Elbow, 10. Right Wrist,
# 11. Left Hip, 12. Left Knee, 13. Left Ankle,
# 14. Right Hip, 15. Right Knee, 16. Right Ankle

# We'll simulate a forward rolling motion with a sad posture (rounded back, heavy movement)

# Generate the joint positions over time
num_joints = 15
joint_positions = []

# Define a rolling motion with a sad posture
for frame in range(num_frames):
    t = frame / num_frames  # time from 0 to 1
    x_offset = t * WIDTH  # forward movement
    # Add a wobbling effect to simulate weight and sadness
    wobble = math.sin(t * 4 * math.pi) * 10

    # Define joint positions
    joints = [
        # Head
        (x_offset + 100 + wobble, 100),
        # Neck
        (x_offset + 100 + wobble, 120),
        # Spine (upper)
        (x_offset + 100 + wobble, 140),
        # Spine (lower)
        (x_offset + 100 + wobble, 170),
        # Pelvis
        (x_offset + 100 + wobble, 200),
        # Left Shoulder
        (x_offset + 70 + wobble, 130),
        # Left Elbow
        (x_offset + 60 + wobble, 160),
        # Left Wrist
        (x_offset + 50 + wobble, 190),
        # Right Shoulder
        (x_offset + 130 + wobble, 130),
        # Right Elbow
        (x_offset + 140 + wobble, 160),
        # Right Wrist
        (x_offset + 150 + wobble, 190),
        # Left Hip
        (x_offset + 80 + wobble, 200),
        # Left Knee
        (x_offset + 70 + wobble, 230),
        # Left Ankle
        (x_offset + 70 + wobble, 260),
        # Right Hip
        (x_offset + 120 + wobble, 200),
        # Right Knee
        (x_offset + 130 + wobble, 230),
        # Right Ankle
        (x_offset + 130 + wobble, 260),
    ]
    joint_positions.append(joints)

# Animation loop
current_frame = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Draw point lights
    for joint in joint_positions[current_frame]:
        pygame.draw.circle(screen, WHITE, (int(joint[0]), int(joint[1])), 3)

    current_frame = (current_frame + 1) % num_frames

    pygame.display.flip()
    clock.tick(FPS)
