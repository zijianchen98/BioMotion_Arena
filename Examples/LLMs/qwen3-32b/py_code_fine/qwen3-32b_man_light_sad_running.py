
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Man Running")
clock = pygame.time.Clock()

# Joint positions (relative to a central body position)
# 15 joints: head, shoulders, elbows, wrists, hips, knees, ankles, spine
# Using a simplified model of a human figure in motion
JOINTS = [
    # head
    [0, -100],
    # left shoulder, left elbow, left wrist
    [-40, -60], [-60, -10], [-60, 40],
    # right shoulder, right elbow, right wrist
    [40, -60], [60, -10], [60, 40],
    # left hip, left knee, left ankle
    [-30, 50], [-40, 100], [-40, 140],
    # right hip, right knee, right ankle
    [30, 50], [40, 100], [40, 140],
    # spine
    [0, 0]
]

# Convert joint positions to numpy array for vector operations
JOINTS = np.array(JOINTS, dtype=np.float32)

# Animation parameters
TIME = 0
PHASE = 0

def update_joints(time):
    # Apply motion to joints to simulate running
    # This is a simplified model of running motion using sine waves
    # You can refine this with more accurate motion capture data for realism

    # Arm motion (left and right)
    arm_amp = 40
    arm_freq = 2
    arm_offset = time * arm_freq * 2 * math.pi

    JOINTS[1] = [-40, -60 + arm_amp * math.sin(arm_offset)]
    JOINTS[3] = [-60, 40 + arm_amp * math.sin(arm_offset + math.pi / 2)]

    JOINTS[4] = [40, -60 + arm_amp * math.sin(arm_offset + math.pi)]
    JOINTS[6] = [60, 40 + arm_amp * math.sin(arm_offset + 3 * math.pi / 2)]

    # Leg motion (left and right)
    leg_amp = 40
    leg_freq = 1.5
    leg_offset = time * leg_freq * 2 * math.pi

    JOINTS[7] = [-30, 50 + leg_amp * math.sin(leg_offset)]
    JOINTS[9] = [-40, 100 + leg_amp * math.sin(leg_offset + math.pi / 2)]
    JOINTS[11] = [-40, 140 + leg_amp * math.sin(leg_offset + math.pi)]

    JOINTS[8] = [30, 50 + leg_amp * math.sin(leg_offset + math.pi)]
    JOINTS[10] = [40, 100 + leg_amp * math.sin(leg_offset + 3 * math.pi / 2)]
    JOINTS[12] = [40, 140 + leg_amp * math.sin(leg_offset + 2 * math.pi)]

    # Head and spine motion
    head_amp = 10
    head_freq = 1
    head_offset = time * head_freq * 2 * math.pi

    JOINTS[0] = [0, -100 + head_amp * math.sin(head_offset)]
    JOINTS[14] = [0, 0 + head_amp * math.sin(head_offset + math.pi)]

    # Add a slight forward motion to simulate running
    forward_speed = 5
    for i in range(len(JOINTS)):
        JOINTS[i][0] += forward_speed

    return JOINTS

def draw_joints(joints, screen):
    # Draw each joint as a white circle
    for joint in joints:
        x = int(joint[0] + WIDTH // 2)
        y = int(joint[1] + HEIGHT // 2)
        pygame.draw.circle(screen, WHITE, (x, y), 5)

# Main animation loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update joint positions
    global TIME
    TIME += 0.02
    joints = update_joints(TIME)

    # Draw the joints
    draw_joints(joints, screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
