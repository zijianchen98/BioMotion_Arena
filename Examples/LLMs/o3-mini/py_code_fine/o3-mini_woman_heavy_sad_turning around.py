
"""
This program displays a point‐light animation of a “sadwoman with heavy weight” turning around.
It uses 15 white “joints” plotted on a solid black background.
The 15 3D points represent key body markers. Their 3D coordinates encode a slightly “drooped”
posture (to imply sadness and heaviness) and subtle depth differences.
Over time the figure rotates smoothly about its vertical (y) axis.
A basic perspective projection is used so that the turning action generates realistic depth cues.
Press the close button on the window to quit.
"""

import sys, math, pygame

# -----------------------------
# Configuration parameters
# -----------------------------
WIDTH, HEIGHT = 800, 600          # window dimensions in pixels
FPS = 60                        # frames per second
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Perspective projection parameter (distance from camera to projection plane)
FOCAL_LENGTH = 300

# Pivot for rotation (we want the figure rotating in place)
# The model is built so that its center is at (0,0,?) in model coordinates.
# We'll translate the model along the z-axis so it lies in front of the camera.
Z_OFFSET = 5.0  # baseline depth (in world units)

# Rotation speed: one full turn every 6 seconds.
ROTATION_SPEED = 2 * math.pi / 6  # radians per second

# -----------------------------
# Define the 15 joint positions in 3D (in world units)
# The coordinates are chosen in a coordinate system where y increases upward.
# These positions represent a human figure in a slightly drooped posture.
# We build the skeleton in a "relative" configuration: the model is centered vertically.
#
# To simulate “sad” posture and heaviness, the head is slightly shifted forward (positive z)
# relative to the shoulders and the arms and legs are arranged in a natural, heavy posture.
# -----------------------------
# The model is defined in a coordinate system where the vertical midline is at y=0.
# We define joints relative to that. Then we add a constant Z offset (Z_OFFSET) to place
# the figure in front of the camera.
#
# Joint list (exactly 15 points):
#   0: Head
#   1: Neck
#   2: Left Shoulder
#   3: Right Shoulder
#   4: Left Elbow
#   5: Right Elbow
#   6: Left Hand
#   7: Right Hand
#   8: Torso (center chest)
#   9: Left Hip
#  10: Right Hip
#  11: Left Knee
#  12: Right Knee
#  13: Left Foot
#  14: Right Foot
#
# Coordinates: (x, y, z)
# (All positions are in world units; you may think of them loosely as meters.)
# We add small differences in the z coordinate to give depth, and a slight forward lean for the head.
joints = [
    ( 0.00,  0.85,  0.10),   # Head (leaning slightly forward)
    ( 0.00,  0.65,  0.05),   # Neck
    (-0.20,  0.65,  0.00),   # Left Shoulder
    ( 0.20,  0.65,  0.00),   # Right Shoulder
    (-0.30,  0.45, -0.05),   # Left Elbow
    ( 0.30,  0.45, -0.05),   # Right Elbow
    (-0.35,  0.25, -0.05),   # Left Hand
    ( 0.35,  0.25, -0.05),   # Right Hand
    ( 0.00,  0.45,  0.05),   # Torso (center chest)
    (-0.15,  0.15,  0.00),   # Left Hip
    ( 0.15,  0.15,  0.00),   # Right Hip
    (-0.15, -0.35,  0.00),   # Left Knee
    ( 0.15, -0.35,  0.00),   # Right Knee
    (-0.15, -0.85,  0.05),   # Left Foot
    ( 0.15, -0.85,  0.05)    # Right Foot
]

# After defining joints in the “model” space, translate them along z so that the figure
# is placed in front of the camera.
translated_joints = []
for (x, y, z) in joints:
    translated_joints.append((x, y, z + Z_OFFSET))

# -----------------------------
# 3D rotation function: rotate a 3D point about the vertical (y) axis,
# around a given pivot (here, pivot is (0,0,Z_OFFSET)).
# -----------------------------
def rotate_y(point, theta, pivot=(0, 0, Z_OFFSET)):
    # Subtract pivot to work in local coordinates
    x, y, z = point
    px, py, pz = pivot
    x_rel = x - px
    y_rel = y - py
    z_rel = z - pz
    # Rotation around y axis:
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    x_new = cos_t * x_rel + sin_t * z_rel
    y_new = y_rel
    z_new = -sin_t * x_rel + cos_t * z_rel
    # Add back the pivot
    return (x_new + px, y_new + py, z_new + pz)

# -----------------------------
# Perspective projection function:
# Projects a 3D point (X, Y, Z) to 2D screen coordinates.
# We assume a pinhole camera where the projection is:
#    x_proj = (FOCAL_LENGTH * X) / Z
#    y_proj = (FOCAL_LENGTH * Y) / Z
# We then translate so that the screen center is at (WIDTH/2, HEIGHT/2),
# and invert the y axis so that upward is positive.
# -----------------------------
def project_point(point):
    x, y, z = point
    # Avoid division by zero; if z is very small, clamp it.
    if z < 0.1:
        z = 0.1
    factor = FOCAL_LENGTH / z
    x_proj = x * factor
    y_proj = y * factor
    screen_x = WIDTH // 2 + int(x_proj)
    screen_y = HEIGHT // 2 - int(y_proj)
    return (screen_x, screen_y)

# -----------------------------
# Main program using Pygame
# -----------------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sadwoman Turning Animation - Point-Light Stimulus")
    clock = pygame.time.Clock()

    theta = 0.0  # current rotation angle

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # seconds elapsed since last frame
        # Increase rotation angle based on elapsed time
        theta += ROTATION_SPEED * dt

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen with a black background
        screen.fill(BLACK)

        # For each joint, apply rotation about the y-axis and project to 2D
        for pt in translated_joints:
            rotated_pt = rotate_y(pt, theta)
            proj = project_point(rotated_pt)
            # Draw a small white circle to represent the point-light
            pygame.draw.circle(screen, WHITE, proj, 4)

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()