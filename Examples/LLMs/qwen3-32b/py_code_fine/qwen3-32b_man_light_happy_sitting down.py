
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
FPS = 30
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sitting Down")
clock = pygame.time.Clock()

# Joint positions (relative to body center)
# 15 joints: head, neck, torso, left and right shoulder, elbow, hand, hip, knee, foot
# We'll animate these joints to simulate "sitting down" motion

# Define a skeleton in neutral position
neutral_joints = [
    [0, -100],  # head
    [0, -50],   # neck
    [0, 0],     # torso
    [-30, 0],   # left shoulder
    [-60, 0],   # left elbow
    [-90, 0],   # left hand
    [30, 0],    # right shoulder
    [60, 0],    # right elbow
    [90, 0],    # right hand
    [-20, 50],  # left hip
    [-20, 100], # left knee
    [-20, 150], # left foot
    [20, 50],   # right hip
    [20, 100],  # right knee
    [20, 150],  # right foot
]

# Normalize joint positions for animation
neutral_joints = np.array(neutral_joints)

# Define the animation as a sequence of joint positions
# We'll simulate the transition from standing to sitting
# The animation will be 60 frames long

def animate_sitting_down(num_frames):
    animation = []
    for t in range(num_frames):
        # Normalize time from 0 to 1
        progress = t / (num_frames - 1)

        # Torso bending forward
        torso_angle = math.pi * 0.4 * progress  # 40 degrees
        torso_rot = np.array([
            [math.cos(torso_angle), -math.sin(torso_angle)],
            [math.sin(torso_angle), math.cos(torso_angle)]
        ])

        # Hip bending
        hip_angle = math.pi * 0.6 * progress  # 60 degrees
        left_hip_rot = np.array([
            [math.cos(hip_angle), -math.sin(hip_angle)],
            [math.sin(hip_angle), math.cos(hip_angle)]
        ])
        right_hip_rot = np.array([
            [math.cos(hip_angle), math.sin(hip_angle)],
            [-math.sin(hip_angle), math.cos(hip_angle)]
        ])

        # Knee bending
        knee_angle = math.pi * 0.6 * progress  # 60 degrees
        left_knee_rot = np.array([
            [math.cos(knee_angle), -math.sin(knee_angle)],
            [math.sin(knee_angle), math.cos(knee_angle)]
        ])
        right_knee_rot = np.array([
            [math.cos(knee_angle), math.sin(knee_angle)],
            [-math.sin(knee_angle), math.cos(knee_angle)]
        ])

        # Apply transformations
        frame = neutral_joints.copy()
        
        # Rotate torso and upper body
        frame[[0, 1, 2, 3, 4, 5, 6, 7, 8]] = np.dot(frame[[0, 1, 2, 3, 4, 5, 6, 7, 8]] - [0, 0], torso_rot.T) + [0, 0]
        
        # Left leg
        frame[9] = neutral_joints[9]  # left hip
        frame[10] = neutral_joints[10] + np.dot(frame[10] - frame[9], left_hip_rot.T)  # left knee
        frame[11] = neutral_joints[11] + np.dot(frame[11] - frame[10], left_knee_rot.T)  # left foot
        
        # Right leg
        frame[12] = neutral_joints[12]  # right hip
        frame[13] = neutral_joints[13] + np.dot(frame[13] - frame[12], right_hip_rot.T)  # right knee
        frame[14] = neutral_joints[14] + np.dot(frame[14] - frame[13], right_knee_rot.T)  # right foot

        animation.append(frame)
    
    return animation

# Generate the animation
animation = animate_sitting_down(60)

# Main loop
frame_index = 0
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw current frame
    current_frame = animation[frame_index]
    for x, y in current_frame:
        pygame.draw.circle(screen, POINT_COLOR, (int(WIDTH/2 + x), int(HEIGHT/2 + y)), POINT_RADIUS)

    # Update display
    pygame.display.flip()

    # Update frame index
    frame_index = (frame_index + 1) % len(animation)

# Quit Pygame
pygame.quit()
sys.exit()
