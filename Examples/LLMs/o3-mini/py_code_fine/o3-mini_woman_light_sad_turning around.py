
"""
A Python program to display a point‐light stimulus animation representing a sad woman with light weight turning around.
The animation shows exactly 15 white point‐lights on a solid black background that depict a human figure
(in this case a “sadwoman” with a slightly slumped posture) rotating about its vertical axis in a biomechanically‐plausible way.
Make sure pygame is installed (pip install pygame).

Press the window close button to exit.
"""

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-light Biological Motion: Sad Woman Turning Around")

clock = pygame.time.Clock()

# Define projection parameters:
focal_length = 300   # focal length for perspective projection
scale_factor = 2     # scale factor to enlarge the figure
center_x, center_y = WIDTH // 2, HEIGHT // 2

# Define the 15 joints of the body in model 3D coordinates.
# Coordinate system:
#   - X: horizontal axis (positive to right)
#   - Y: vertical axis (positive upward)
#   - Z: depth (positive coming out of the screen). 
# The joints are arranged in a “sad” posture with the head slightly tilted downward.
# The units are arbitrary (e.g., pixels or centimeters before scaling).
joints = [
    (  0, 160, -2),   # 0: Head (tilted a bit downward to convey sadness)
    (  0, 150,  0),   # 1: Neck
    (-10, 150,  0),   # 2: Left Shoulder
    ( 10, 150,  0),   # 3: Right Shoulder
    (-15, 135,  0),   # 4: Left Elbow
    ( 15, 135,  0),   # 5: Right Elbow
    (-20, 120,  0),   # 6: Left Wrist
    ( 20, 120,  0),   # 7: Right Wrist
    (  0, 140,  0),   # 8: Spine (a reference point in the torso)
    (-10, 120,  0),   # 9: Left Hip
    ( 10, 120,  0),   # 10: Right Hip
    (-10,  90,  0),   # 11: Left Knee
    ( 10,  90,  0),   # 12: Right Knee
    (-10,  60,  0),   # 13: Left Ankle
    ( 10,  60,  0)    # 14: Right Ankle
]

def rotate_about_y(point, angle):
    """Rotate a 3D point about the vertical (Y) axis by the given angle in radians."""
    x, y, z = point
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    x_rot = x * cos_a + z * sin_a
    z_rot = -x * sin_a + z * cos_a
    return (x_rot, y, z_rot)

def project_point(point):
    """Project a 3D point using a simple perspective projection."""
    x, y, z = point
    # Avoid division by zero – assume focal_length > z_rot to always get a positive denominator.
    factor = focal_length / (focal_length - z)
    x_proj = x * factor
    y_proj = y * factor
    return (x_proj, y_proj)

def draw_figure(angle):
    """Draw the figure by rotating, projecting, and then drawing each joint as a white circle."""
    for joint in joints:
        # Rotate the joint around the Y axis to simulate turning.
        x_rot, y_rot, z_rot = rotate_about_y(joint, angle)
        # Project the rotated 3D point to 2D.
        x_proj, y_proj = project_point((x_rot, y_rot, z_rot))
        # Apply scale and translation to center on the display.
        x_screen = int(center_x + scale_factor * x_proj)
        y_screen = int(center_y - scale_factor * y_proj)
        # Draw the point-light (circle of radius 4).
        pygame.draw.circle(screen, (255, 255, 255), (x_screen, y_screen), 4)

def main():
    running = True
    angle = 0.0  # initial rotation angle in radians
    rotation_speed = math.radians(45)  # rotate 45 degrees per second

    while running:
        dt = clock.tick(60) / 1000.0  # seconds passed since last frame (frame rate capped at 60 FPS)
        # Event handling.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update rotation angle.
        angle += rotation_speed * dt
        angle %= (2 * math.pi)

        # Clear screen with black background.
        screen.fill((0, 0, 0))

        # Draw the figure.
        draw_figure(angle)

        # Refresh display.
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()