
import pygame
import sys
import math
import numpy as np
from pygame.locals import *

# Configuration
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_FRAMES = 120  # 2 seconds of animation at 60 FPS

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sadwoman Running - Point-Light Display")
clock = pygame.time.Clock()

# Define a basic skeleton for a sadwoman (15 joints)
# These are relative positions in a frame (in pixels)
skeleton_template = {
    "hips": (0, 0),
    "left_hip": (-40, 20),
    "right_hip": (40, 20),
    "left_knee": (-40, 80),
    "right_knee": (40, 80),
    "left_ankle": (-40, 140),
    "right_ankle": (40, 140),
    "spine": (0, -60),
    "neck": (0, -120),
    "head": (0, -160),
    "left_shoulder": (-30, -100),
    "right_shoulder": (30, -100),
    "left_elbow": (-70, -100),
    "right_elbow": (70, -100),
    "left_wrist": (-110, -100),
    "right_wrist": (110, -100),
}

# Generate a sequence of frames for the running motion
def generate_frames(num_frames):
    frames = []
    for i in range(num_frames):
        # Base motion (center of motion)
        center_x = WIDTH // 2
        center_y = HEIGHT // 2

        # Running motion: vertical bounce and horizontal movement
        bounce = 20 * math.sin(2 * math.pi * i / num_frames * 4)
        forward = 10 * i
        side = 5 * math.sin(2 * math.pi * i / num_frames * 2)

        # Modify skeleton for running motion
        skeleton = {}
        for key, (dx, dy) in skeleton_template.items():
            # Add bounce and forward motion
            x = center_x + dx + forward + side
            y = center_y + dy + bounce
            skeleton[key] = (x, y)

        # Adjust for sad posture: head down, spine curved
        if key == "head":
            skeleton[key] = (skeleton["head"][0], skeleton["head"][1] + 20)
        if key == "neck":
            skeleton[key] = (skeleton["neck"][0], skeleton["neck"][1] + 10)
        if key == "spine":
            skeleton[key] = (skeleton["spine"][0], skeleton["spine"][1] + 5)

        # Add arm swing for running
        arm_swing = 20 * math.sin(2 * math.pi * i / num_frames * 2)
        if key == "left_shoulder":
            skeleton[key] = (skeleton["left_shoulder"][0], skeleton["left_shoulder"][1] + arm_swing)
        if key == "right_shoulder":
            skeleton[key] = (skeleton["right_shoulder"][0], skeleton["right_shoulder"][1] - arm_swing)
        if key == "left_elbow":
            skeleton[key] = (skeleton["left_elbow"][0], skeleton["left_elbow"][1] + arm_swing)
        if key == "right_elbow":
            skeleton[key] = (skeleton["right_elbow"][0], skeleton["right_elbow"][1] - arm_swing)
        if key == "left_wrist":
            skeleton[key] = (skeleton["left_wrist"][0], skeleton["left_wrist"][1] + arm_swing)
        if key == "right_wrist":
            skeleton[key] = (skeleton["right_wrist"][0], skeleton["right_wrist"][1] - arm_swing)

        frames.append(skeleton)

    return frames

frames = generate_frames(NUM_FRAMES)

# Main loop
frame_index = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Black background

    # Draw current frame
    current_frame = frames[frame_index % len(frames)]
    for _, (x, y) in current_frame.items():
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(FPS)
    frame_index += 1
