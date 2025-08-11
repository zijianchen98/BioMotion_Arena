#!/usr/bin/env python3
"""
Point-Light Biological Motion: A 'Happy, Heavy Woman' Turning Around

This Python program uses Pygame to display a simple point-light
animation of a woman turning around. The figure is represented
as 15 white dots (joints) on a black background, moving in a
way that suggests a heavy, joyful person turning in place.

Instructions:
1) Install pygame if needed: pip install pygame
2) Run this script: python3 point_light_biological_motion.py
3) A window will appear with 15 white dots on a black background,
   rotating smoothly in unison to simulate a 3D turn-around motion.
4) Close the window or press ESC to exit.

Note:
Point-light animations typically encode minimal cues about gender
or body type, but here we represent a slightly wider hip and
general proportions to convey a heavier figure.
"""

import pygame
import math
import sys

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Heavy Woman Turning")
clock = pygame.time.Clock()

# Number of white point-lights
NUM_POINTS = 15

# Define a simple 3D skeleton with 15 joint positions (x, y, z).
# For a "heavy woman," we can slightly increase hip width and torso thickness.
#
# Joints (indices reference):
#  0: Head
#  1: Upper torso center (chest)
#  2: Left shoulder
#  3: Right shoulder
#  4: Left elbow
#  5: Right elbow
#  6: Left wrist
#  7: Right wrist
#  8: Lower torso / hip center
#  9: Left hip
# 10: Right hip
# 11: Left knee
# 12: Right knee
# 13: Left ankle
# 14: Right ankle
#
# Coordinates chosen so that the figure stands upright along the Y-axis.
# Y increases upwards, X is horizontal, Z goes into/out of screen.

skeleton_3d = [
    (0.0,  1.8, 0.0),   # Head
    (0.0,  1.4, 0.0),   # Chest
    (-0.3, 1.4, 0.0),   # Left shoulder
    ( 0.3, 1.4, 0.0),   # Right shoulder
    (-0.5, 1.0, 0.0),   # Left elbow
    ( 0.5, 1.0, 0.0),   # Right elbow
    (-0.6, 0.6, 0.0),   # Left wrist
    ( 0.6, 0.6, 0.0),   # Right wrist
    ( 0.0,  0.8, 0.0),  # Hip center
    (-0.35, 0.8, 0.0),  # Left hip
    ( 0.35, 0.8, 0.0),  # Right hip
    (-0.35, 0.2, 0.0),  # Left knee
    ( 0.35, 0.2, 0.0),  # Right knee
    (-0.35, -0.3, 0.0), # Left ankle
    ( 0.35, -0.3, 0.0), # Right ankle
]

def rotate_y(x, y, z, theta):
    """
    Rotate a point (x, y, z) around the Y-axis by angle theta.
    Returns the rotated point (xr, yr, zr).
    """
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    xr = x * cos_t + z * sin_t
    yr = y
    zr = -x * sin_t + z * cos_t
    return xr, yr, zr

def project_2d(x, y, z, screen_w, screen_h, scale=150):
    """
    Orthographic projection from 3D to 2D:
    (x, y, z) -> (X, Y) on the Pygame screen.
    Scale and center on screen for better viewing.
    """
    X = int(screen_w // 2 + x * scale)
    Y = int(screen_h // 2 - y * scale)
    return X, Y

def main():
    angle = 0.0  # This will track the rotation about the Y-axis.
    running = True

    while running:
        clock.tick(60)  # ~60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Increase angle so that the figure keeps turning
        # Full turn in about 4 seconds -> 2π in 4s => ~π/120 each frame at 60fps
        angle += math.pi / 120  
        # Keep angle in [0, 2π) for cleanliness
        angle = angle % (2.0 * math.pi)

        # Clear screen (black background)
        screen.fill((0, 0, 0))

        # For each joint, rotate around Y and project to 2D
        for (x, y, z) in skeleton_3d:
            xr, yr, zr = rotate_y(x, y, z, angle)
            X, Y = project_2d(xr, yr, zr, WIDTH, HEIGHT, scale=200)
            pygame.draw.circle(screen, (255, 255, 255), (X, Y), 5)

        # Update display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()