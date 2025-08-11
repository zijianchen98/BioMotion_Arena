
import pygame
import sys
import math
import numpy as np
from pygame.locals import *

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
LIGHT_RADIUS = 4
LIGHT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Joint positions relative to a standing person (in a waving motion)
# This is a simplified 2D skeletal model of a person waving a hand
# The joints are modeled as points in 2D space, with relative angles and distances

# Joints: head, neck, spine, left_shoulder, left_elbow, left_hand, right_shoulder, right_elbow, right_hand, left_hip, left_knee, left_ankle, right_hip, right_knee, right_ankle
JOINT_COUNT = 15
JOINT_NAMES = [
    "head", "neck", "spine", "left_shoulder", "left_elbow", "left_hand",
    "right_shoulder", "right_elbow", "right_hand", "left_hip", "left_knee",
    "left_ankle", "right_hip", "right_knee", "right_ankle"
]

# Initial joint positions (relative to center of screen)
JOINT_RELATIVE = {
    "head": (0, -100),
    "neck": (0, -70),
    "spine": (0, -30),
    "left_shoulder": (-30, -10),
    "left_elbow": (-60, 20),
    "left_hand": (-90, 60),
    "right_shoulder": (30, -10),
    "right_elbow": (60, 20),
    "right_hand": (90, 60),
    "left_hip": (-20, 30),
    "left_knee": (-30, 70),
    "left_ankle": (-30, 110),
    "right_hip": (20, 30),
    "right_knee": (30, 70),
    "right_ankle": (30, 110)
}

# Scaling factor to make the figure fit in the screen
SCALE = 3

# Center of the screen
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

# Waving motion parameters
WAVE_SPEED = 0.05
WAVE_AMPLITUDE = 20
WAVE_FREQUENCY = 1.0

def get_joint_positions(t):
    # Get the joint positions at time t (simulating a waving motion)
    positions = []
    for joint in JOINT_NAMES:
        x_rel, y_rel = JOINT_RELATIVE[joint]
        if joint == "left_hand" or joint == "right_hand":
            # Add waving motion to the hands
            if joint == "left_hand":
                x = x_rel - WAVE_AMPLITUDE * math.sin(t * WAVE_FREQUENCY)
            else:
                x = x_rel + WAVE_AMPLITUDE * math.sin(t * WAVE_FREQUENCY)
            y = y_rel
        else:
            x = x_rel
            y = y_rel
        positions.append((x * SCALE, y * SCALE))
    return positions

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Happy Woman Waving")
    clock = pygame.time.Clock()

    t = 0.0  # Time parameter for animation

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)

        t += WAVE_SPEED
        positions = get_joint_positions(t)

        # Draw the joints
        for x_rel, y_rel in positions:
            x = int(CENTER_X + x_rel)
            y = int(CENTER_Y + y_rel)
            pygame.draw.circle(screen, LIGHT_COLOR, (x, y), LIGHT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
