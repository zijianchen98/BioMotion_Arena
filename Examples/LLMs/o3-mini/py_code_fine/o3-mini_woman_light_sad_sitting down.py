
"""
This program creates a point‐light stimulus animation of a “sad woman with light weight” sitting down.
It uses exactly 15 white point-lights on a black background to represent key joints of the body.
The animation smoothly interpolates from an upright (standing) posture to a sitting posture
that reflects a slight slump (a “sad” gesture) and biomechanically plausible motion.
Run with: python3 point_light_sitting.py
"""

import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions and settings.
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion - Sitting Down")

clock = pygame.time.Clock()
FPS = 60

# Define the 15 joint positions for the standing (upright) posture.
# Each coordinate is a tuple (x, y); y increases downward.
standing_coords = [
    (320, 150),  # 0: Head
    (320, 170),  # 1: Neck
    (300, 170),  # 2: Left Shoulder
    (340, 170),  # 3: Right Shoulder
    (280, 190),  # 4: Left Elbow
    (360, 190),  # 5: Right Elbow
    (270, 210),  # 6: Left Hand
    (370, 210),  # 7: Right Hand
    (320, 180),  # 8: Chest (upper torso)
    (320, 210),  # 9: Abdomen (lower torso)
    (320, 230),  # 10: Pelvis (hip center)
    (310, 280),  # 11: Left Knee
    (330, 280),  # 12: Right Knee
    (300, 330),  # 13: Left Foot
    (340, 330)   # 14: Right Foot
]

# Define the 15 joint positions for the sitting posture.
# This posture shows a slumped, “sad” gesture. Note that the legs are bent and drawn upward.
sitting_coords = [
    (320, 165),  # 0: Head drops slightly
    (320, 185),  # 1: Neck
    (300, 185),  # 2: Left Shoulder (slumps a bit)
    (340, 185),  # 3: Right Shoulder
    (290, 205),  # 4: Left Elbow (a little forward)
    (350, 205),  # 5: Right Elbow
    (280, 225),  # 6: Left Hand
    (360, 225),  # 7: Right Hand
    (320, 190),  # 8: Chest (slightly raised compared to abdomen)
    (320, 220),  # 9: Abdomen
    (320, 250),  # 10: Pelvis moves down as if lowering into the chair
    (310, 260),  # 11: Left Knee raised (bent)
    (330, 260),  # 12: Right Knee raised
    (300, 300),  # 13: Left Foot (moved upward)
    (340, 300)   # 14: Right Foot
]

# Duration of the sitting down transition (in seconds)
transition_duration = 5.0

# Total time including a pause at the end (seconds)
total_duration = transition_duration + 1.0

# Function to interpolate between start and end coordinates.
def interpolate(pt_start, pt_end, t):
    # t is a parameter from 0 (start) to 1 (end)
    x = pt_start[0] + (pt_end[0] - pt_start[0]) * t
    y = pt_start[1] + (pt_end[1] - pt_start[1]) * t
    return (x, y)

# Main loop variables
running = True
start_ticks = pygame.time.get_ticks()  # in milliseconds

while running:
    # Handle events (like quitting)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Compute elapsed time in seconds
    elapsed = (pygame.time.get_ticks() - start_ticks) / 1000.0

    # Compute the interpolation parameter t.
    # During the transition duration, t goes from 0 to 1.
    if elapsed < transition_duration:
        t = elapsed / transition_duration
    else:
        t = 1.0  # Hold the sitting posture once the transition is complete

    # Clear the screen with black.
    screen.fill((0, 0, 0))

    # For each joint, compute the current position and draw a white circle.
    for i in range(15):
        start_pt = standing_coords[i]
        end_pt = sitting_coords[i]
        current_pt = interpolate(start_pt, end_pt, t)
        # Draw a circle at the current position.
        pygame.draw.circle(screen, (255, 255, 255), (int(current_pt[0]), int(current_pt[1])), 5)

    # Update the display.
    pygame.display.flip()

    # Cap the frame rate.
    clock.tick(FPS)

    # Optionally, stop the program after a full cycle (transition + pause)
    if elapsed > total_duration:
        running = False

pygame.quit()
sys.exit()