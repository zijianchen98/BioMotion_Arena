
"""
This program creates a point‐light animation of a sad woman (with a lightweight posture)
waving her right hand. The stimulus is rendered as exactly 15 white point‐lights
(mimicking key joints) on a solid black background. The right hand (index 6) is animated
to simulate a realistic, biomechanically plausible hand wave.
"""

import pygame
import math
import sys

# Initialize Pygame
pygame.init()
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Biological Motion - Waving Hand")
clock = pygame.time.Clock()

# Define colors and parameters
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 5

# Set up base joint positions (indices 0 to 14)
# The coordinates are chosen to roughly resemble a standing human (sadwoman)
# with a slightly drooped posture.
#
# Joints indices:
#  0: Head
#  1: Left Shoulder
#  2: Right Shoulder
#  3: Left Elbow
#  4: Right Elbow
#  5: Left Hand
#  6: Right Hand (animated)
#  7: Torso Top
#  8: Torso Bottom
#  9: Left Hip
# 10: Right Hip
# 11: Left Knee
# 12: Right Knee
# 13: Left Ankle
# 14: Right Ankle

base_joints = {
    0: (320, 150),  # Head
    7: (320, 180),  # Torso top
    8: (320, 230),  # Torso bottom
    1: (290, 180),  # Left Shoulder
    2: (350, 180),  # Right Shoulder
    3: (270, 210),  # Left Elbow
    5: (260, 240),  # Left Hand
    9: (300, 230),  # Left Hip
    10: (340, 230), # Right Hip
    11: (300, 280), # Left Knee
    12: (340, 280), # Right Knee
    13: (300, 330), # Left Ankle
    14: (340, 330), # Right Ankle
}

# For the right arm, we define the elbow and base for hand:
right_elbow = (360, 210)  # Joint index 4 (Right Elbow) fixed
# The right hand (joint index 6) will be computed relative to the elbow.

# Animation parameters for the waving hand (right hand)
L = 30                       # Length from elbow to hand (pixels)
base_angle = math.pi / 2     # At rest, the hand points downward (vertical below elbow)
angle_amplitude = math.radians(30)  # maximum deviation: 30 degrees
wave_period = 2.0            # period in seconds of a full waving cycle
omega = (2 * math.pi) / wave_period  # angular frequency

# Main loop
running = True
start_ticks = pygame.time.get_ticks()  # to control animation time
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Compute elapsed time in seconds
    t = (pygame.time.get_ticks() - start_ticks) / 1000.0

    # Compute the angle for the right hand as a function of time.
    # The hand rotates about the right elbow in a smooth sinusoidal manner.
    # When sin(omega*t) = 0 => angle = base_angle, so at rest hand points straight down.
    # The hand oscillates ±angle_amplitude around the vertical.
    angle = base_angle + angle_amplitude * math.sin(omega * t)

    # Compute the new position of the right hand (joint index 6)
    right_hand_x = right_elbow[0] + L * math.cos(angle)
    right_hand_y = right_elbow[1] + L * math.sin(angle)
    current_joints = base_joints.copy()
    current_joints[4] = right_elbow      # Right Elbow remains fixed
    current_joints[6] = (right_hand_x, right_hand_y)

    # Clear screen
    screen.fill(BLACK)

    # Draw all 15 point-lights
    # Sorting the keys to have a consistent drawing order.
    for j in range(15):
        # Only draw if the joint is in our dictionary (we set 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)
        if j in current_joints:
            pos = current_joints[j]
            # Draw circle (as white dot)
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 frames per second
    clock.tick(60)

pygame.quit()
sys.exit()