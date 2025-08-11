
"""
This program displays an animation of 15 white point‐lights on a solid black background.
They represent a simplified human figure (a “happy woman” with heavy weight) performing a
bowing action. The figure is composed of 15 points corresponding to anatomical landmarks.
The upper body (head, shoulders, elbows, hands, and upper spine) rotates around the lower spine,
simulating a biomechanically plausible bowing (forward bending) motion.
"""

import sys
import math
import pygame
from pygame.locals import QUIT

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Bowing Figure")

# Clock to manage animation speed
clock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the base skeleton positions (in a body-centered coordinate system)
# Coordinates are defined relative to a natural origin.
# We choose the lower spine as the pivot for the bowing motion.
#
# The 15 points (all positions in pixels, in the local coordinate system):
#   - "head"
#   - "left_shoulder", "right_shoulder"
#   - "left_elbow", "right_elbow"
#   - "left_hand", "right_hand"
#   - "upper_spine"
#   - "lower_spine" (pivot)
#   - "left_hip", "right_hip"
#   - "left_knee", "right_knee"
#   - "left_foot", "right_foot"
skeleton = {
    "head":         (0, -100),
    "left_shoulder":  (-20, -80),
    "right_shoulder": (20, -80),
    "left_elbow":     (-40, -60),
    "right_elbow":    (40, -60),
    "left_hand":      (-50, -40),
    "right_hand":     (50, -40),
    "upper_spine":    (0, -60),
    "lower_spine":    (0, -20),  # Pivot for bowing
    "left_hip":       (-15, 0),
    "right_hip":      (15, 0),
    "left_knee":      (-15, 40),
    "right_knee":     (15, 40),
    "left_foot":      (-15, 80),
    "right_foot":     (15, 80)
}

# For the bowing animation, the upper body (above lower_spine) rotates.
rotating_parts = {
    "head", "left_shoulder", "right_shoulder",
    "left_elbow", "right_elbow", "left_hand", "right_hand",
    "upper_spine"
}

# Parameters for the bowing motion
max_angle = math.radians(30)  # maximum bowing angle (30 degrees)
bow_frequency = 0.5           # cycles per second

# For positioning the figure on the screen, pick a center offset.
screen_offset = (WIDTH // 2, HEIGHT // 2 + 50)  # shift slightly downward

def rotate_point(point, pivot, angle):
    """
    Rotate a point around a pivot by a given angle.
    point and pivot are (x,y) tuples.
    Returns the rotated (x,y) tuple.
    """
    # Translate point relative to pivot
    dx = point[0] - pivot[0]
    dy = point[1] - pivot[1]
    # Apply rotation
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    new_dx = dx * cos_a - dy * sin_a
    new_dy = dx * sin_a + dy * cos_a
    # Translate back
    return (pivot[0] + new_dx, pivot[1] + new_dy)

def get_current_skeleton(t):
    """
    Compute the current skeleton positions given time t.
    Uses a sinusoidal function to vary the bowing angle between 0 and max_angle.
    The rotation is applied to points in 'rotating_parts' about lower_spine.
    """
    # Oscillate between 0 (upright) and max_angle (bowing forward).
    angle = max_angle * abs(math.sin(2 * math.pi * bow_frequency * t))
    
    pivot = skeleton["lower_spine"]
    current = {}
    for key, pos in skeleton.items():
        if key in rotating_parts:
            # Apply rotation around the pivot (lower_spine)
            new_pos = rotate_point(pos, pivot, angle)
            current[key] = new_pos
        else:
            # Nonrotating parts remain the same (in this simplified model)
            current[key] = pos
    return current

def draw_skeleton(skel):
    """
    Draw each of the 15 points on the screen.
    Each point is drawn as a small white circle.
    """
    for pos in skel.values():
        # Convert from local coordinates to screen coordinates
        screen_x = int(pos[0] + screen_offset[0])
        screen_y = int(pos[1] + screen_offset[1])
        pygame.draw.circle(screen, WHITE, (screen_x, screen_y), 4)

def main():
    t_start = pygame.time.get_ticks() / 1000.0  # start time in seconds

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Clear the screen
        screen.fill(BLACK)

        # Calculate elapsed time in seconds
        t = pygame.time.get_ticks() / 1000.0 - t_start

        # Get current skeleton positions for this frame
        current_skel = get_current_skeleton(t)

        # Draw the skeleton as 15 white point-lights
        draw_skeleton(current_skel)

        # Update the display
        pygame.display.flip()

        # Maintain FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()