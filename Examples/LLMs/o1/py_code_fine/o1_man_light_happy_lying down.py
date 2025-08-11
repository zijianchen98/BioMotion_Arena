#!/usr/bin/env python3
import pygame
import math
import sys

# -----------------------------------------
# A simple point-light biological motion style animation
# depicting a "happyman" lying down.
# 15 white points on a black background.
# -----------------------------------------

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happyman Lying Down")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Define base positions (x, y) for 15 points of the "happyman" lying down
# Indices:
#   0: Head
#   1: Neck
#   2: Right Shoulder
#   3: Right Elbow
#   4: Right Hand
#   5: Left Shoulder
#   6: Left Elbow
#   7: Left Hand
#   8: Right Hip
#   9: Right Knee
#   10: Right Foot
#   11: Left Hip
#   12: Left Knee
#   13: Left Foot
#   14: Torso Center

base_positions = [
    (200, 300),  # Head
    (210, 300),  # Neck
    (220, 290),  # Right Shoulder
    (240, 290),  # Right Elbow
    (260, 290),  # Right Hand
    (220, 310),  # Left Shoulder
    (240, 310),  # Left Elbow
    (260, 310),  # Left Hand
    (300, 295),  # Right Hip
    (320, 295),  # Right Knee
    (340, 295),  # Right Foot
    (300, 305),  # Left Hip
    (320, 305),  # Left Knee
    (340, 305),  # Left Foot
    (250, 300),  # Torso Center
]

# Function to get updated point positions for frame t
def get_lying_down_positions(t):
    # t is an integer frame count, we can use trigonometric functions
    # to create small realistic offsets for arms/legs to simulate gentle motion
    positions = []
    # We'll define a small amplitude for the movement
    arm_amp = 5
    leg_amp = 5
    speed = 0.05

    for i, (bx, by) in enumerate(base_positions):
        # By default, no offset
        dx, dy = 0, 0

        # Animate arms (right elbow, right hand, left elbow, left hand)
        if i == 3:  # Right Elbow
            dx = arm_amp * math.sin(speed * t)
            dy = arm_amp * math.cos(speed * t)
        elif i == 4:  # Right Hand
            dx = arm_amp * 1.5 * math.sin(speed * t + math.pi / 2)
            dy = arm_amp * 1.5 * math.sin(speed * t + math.pi / 2)
        elif i == 6:  # Left Elbow
            dx = -arm_amp * math.sin(speed * t)
            dy = arm_amp * math.cos(speed * t)
        elif i == 7:  # Left Hand
            dx = -arm_amp * 1.5 * math.sin(speed * t + math.pi / 2)
            dy = arm_amp * 1.5 * math.sin(speed * t + math.pi / 2)

        # Animate legs (right knee, right foot, left knee, left foot)
        if i == 9:   # Right Knee
            dx += leg_amp * math.sin(speed * t + math.pi / 3)
            dy += leg_amp * math.cos(speed * t + math.pi / 3)
        elif i == 10:  # Right Foot
            dx += leg_amp * math.cos(speed * t + 0.5)
            dy += leg_amp * math.sin(speed * t + 0.5)
        elif i == 12:  # Left Knee
            dx += -leg_amp * math.sin(speed * t + math.pi / 3)
            dy += leg_amp * math.cos(speed * t + math.pi / 3)
        elif i == 13:  # Left Foot
            dx += -leg_amp * math.cos(speed * t + 0.5)
            dy += leg_amp * math.sin(speed * t + 0.5)

        # Combine base position with computed offsets
        x = bx + dx
        y = by + dy
        positions.append((x, y))

    return positions

def main():
    running = True
    frame_count = 0

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen black
        screen.fill((0, 0, 0))

        # Get the positions for current animation frame
        points = get_lying_down_positions(frame_count)

        # Draw the 15 white points
        for (x, y) in points:
            pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 4)

        pygame.display.flip()
        frame_count += 1

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()