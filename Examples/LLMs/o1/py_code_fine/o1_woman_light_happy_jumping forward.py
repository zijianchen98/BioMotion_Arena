#!/usr/bin/env python3

import pygame
import math
import sys

# ----------------------------------------------------------------------------------
# A simple Pygame script that displays 15 white point-lights on a black background,
# portraying a forward-jumping motion with a lightweight, happy female figure.
# ----------------------------------------------------------------------------------

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 30  # frames per second

def rotate(point, degrees):
    """Rotate a (dx, dy) point around (0, 0) by 'degrees' (in deg) counterclockwise."""
    rad = math.radians(degrees)
    sin_r = math.sin(rad)
    cos_r = math.cos(rad)
    x, y = point
    return (x*cos_r - y*sin_r, x*sin_r + y*cos_r)

def get_points(t):
    """
    Returns a list of 15 (x, y) positions that represent a jumping animation
    for a lightweight, happy woman. 't' goes from 0 to 1 over one jump cycle.
    """

    # Base horizontal and vertical location
    # Horizontal: moves from x=200 to x=400 across t in [0..1]
    pelvis_x = 200 + 200 * t

    # Simple parabolic jump: peak ~ middle of the cycle
    # Max jump height ~ 80 px above y_base
    y_base = 300
    pelvis_y = y_base - 320 * t * (1 - t)  # 4*h (h=80) => 320

    # Angles (in degrees) to provide some "happy" jump-like movement
    # Using sine waves for a rough approximation of limb movements.
    thigh_angle_left =  20 * math.sin(2 * math.pi * t)
    thigh_angle_right = -20 * math.sin(2 * math.pi * t)
    knee_angle_left  =  20 * math.sin(2 * math.pi * t + math.pi/2)
    knee_angle_right =  20 * math.sin(2 * math.pi * t + math.pi/2)
    # Arms
    shoulder_angle_left  =  20 * math.sin(2 * math.pi * t + math.pi/3)
    shoulder_angle_right = -20 * math.sin(2 * math.pi * t + math.pi/3)
    elbow_angle_left     =  20 * math.sin(2 * math.pi * t + math.pi/1.5)
    elbow_angle_right    = -20 * math.sin(2 * math.pi * t + math.pi/1.5)

    # Pelvis (point 1)
    pelvis = (pelvis_x, pelvis_y)

    # Chest (point 2) - keep torso vertical
    chest = (pelvis_x, pelvis_y - 70)

    # Head (point 3) - above chest
    head = (pelvis_x, pelvis_y - 100)

    # Left thigh start (point 4): pelvis + rotation(0, 50)
    left_thigh = (
        pelvis[0] + rotate((0, 50), thigh_angle_left)[0],
        pelvis[1] + rotate((0, 50), thigh_angle_left)[1],
    )
    # Left knee (point 5): from left_thigh + rotation(0, 50)
    left_knee = (
        left_thigh[0] + rotate((0, 50), knee_angle_left + thigh_angle_left)[0],
        left_thigh[1] + rotate((0, 50), knee_angle_left + thigh_angle_left)[1],
    )
    # Left ankle (point 6): from knee + rotation(0, 50)
    left_ankle = (
        left_knee[0] + rotate((0, 50), knee_angle_left + thigh_angle_left)[0],
        left_knee[1] + rotate((0, 50), knee_angle_left + thigh_angle_left)[1],
    )

    # Right thigh start (point 7): pelvis + rotation(0, 50)
    right_thigh = (
        pelvis[0] + rotate((0, 50), thigh_angle_right)[0],
        pelvis[1] + rotate((0, 50), thigh_angle_right)[1],
    )
    # Right knee (point 8)
    right_knee = (
        right_thigh[0] + rotate((0, 50), knee_angle_right + thigh_angle_right)[0],
        right_thigh[1] + rotate((0, 50), knee_angle_right + thigh_angle_right)[1],
    )
    # Right ankle (point 9)
    right_ankle = (
        right_knee[0] + rotate((0, 50), knee_angle_right + thigh_angle_right)[0],
        right_knee[1] + rotate((0, 50), knee_angle_right + thigh_angle_right)[1],
    )

    # Left shoulder (point 10): chest + small rotation around chest
    left_shoulder = (
        chest[0] + rotate((0, -20), shoulder_angle_left)[0],
        chest[1] + rotate((0, -20), shoulder_angle_left)[1],
    )
    # Left elbow (point 11)
    left_elbow = (
        left_shoulder[0] + rotate((0, -40), elbow_angle_left + shoulder_angle_left)[0],
        left_shoulder[1] + rotate((0, -40), elbow_angle_left + shoulder_angle_left)[1],
    )
    # Left wrist (point 12)
    left_wrist = (
        left_elbow[0] + rotate((0, -30), elbow_angle_left + shoulder_angle_left)[0],
        left_elbow[1] + rotate((0, -30), elbow_angle_left + shoulder_angle_left)[1],
    )

    # Right shoulder (point 13)
    right_shoulder = (
        chest[0] + rotate((0, -20), shoulder_angle_right)[0],
        chest[1] + rotate((0, -20), shoulder_angle_right)[1],
    )
    # Right elbow (point 14)
    right_elbow = (
        right_shoulder[0] + rotate((0, -40), elbow_angle_right + shoulder_angle_right)[0],
        right_shoulder[1] + rotate((0, -40), elbow_angle_right + shoulder_angle_right)[1],
    )
    # Right wrist (point 15)
    right_wrist = (
        right_elbow[0] + rotate((0, -30), elbow_angle_right + shoulder_angle_right)[0],
        right_elbow[1] + rotate((0, -30), elbow_angle_right + shoulder_angle_right)[1],
    )

    # Combine into 15 points
    return [
        pelvis, chest, head,
        left_thigh, left_knee, left_ankle,
        right_thigh, right_knee, right_ankle,
        left_shoulder, left_elbow, left_wrist,
        right_shoulder, right_elbow, right_wrist
    ]

def main():
    running = True
    t = 0.0
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update time parameter t in [0, 1]
        # One cycle is 2 seconds => each second we add 0.5 to t
        t += (1.0 / FPS) / 2.0
        t %= 1.0

        # Draw background
        screen.fill(BLACK)

        # Get the 15 points
        points = get_points(t)
        # Draw them
        for (x, y) in points:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

        # Flip display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()