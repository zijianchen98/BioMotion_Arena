
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion Stimulus - Turning Woman")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5

# --- Biomechanical Model (15 points) ---
# Relative 3D coordinates for a 'slender' and slightly 'slumped' figure.
# Coordinates are defined relative to a central vertical axis (Y-axis).
# X: lateral dimension (left/right of the central axis). Negative X is the body's right side.
# Y: vertical dimension (height from the 'ground', where y=0.0 represents the ankle level).
# Z: sagittal dimension (forward/backward of the central axis). Negative Z is forward (e.g., arms slightly in front).

# These coordinates are designed to represent a 'light weight' (slender) woman.
# The 'sad' aspect is implicitly conveyed through slower motion and subtly designed posture.
BASE_POINTS_3D = [
    (0.0, 1.7, 0.0),      # 1: Head (topmost point)
    (0.0, 1.5, 0.0),      # 2: Neck
    (-0.18, 1.35, -0.05), # 3: Right Shoulder (body's right, appears on screen left when facing forward; slightly forward)
    (0.18, 1.35, -0.05),  # 4: Left Shoulder (body's left, appears on screen right when facing forward; slightly forward)
    (-0.28, 0.95, -0.1),  # 5: Right Elbow
    (0.28, 0.95, -0.1),   # 6: Left Elbow
    (-0.35, 0.55, -0.15), # 7: Right Wrist
    (0.35, 0.55, -0.15),  # 8: Left Wrist
    (-0.12, 0.78, 0.0),   # 9: Right Hip
    (0.12, 0.78, 0.0),    # 10: Left Hip
    (0.0, 0.73, 0.0),     # 11: Pelvis Center (or lower spine base)
    (-0.12, 0.38, 0.0),   # 12: Right Knee
    (0.12, 0.38, 0.0),    # 13: Left Knee
    (-0.12, 0.0, 0.0),    # 14: Right Ankle (ground level)
    (0.12, 0.0, 0.0),     # 15: Left Ankle (ground level)
]

# Ensure exactly 15 points are defined, as per requirements.
assert len(BASE_POINTS_3D) == 15, "There must be exactly 15 points defined for the biological motion stimulus."

# Scaling and Offset for screen projection
# The total height of the figure (Y-range) is from 0.0 (ankles) to 1.7 (head).
# We scale this to occupy a significant portion of the screen height, e.g., 70%.
SCALE_FACTOR = SCREEN_HEIGHT * 0.7 / 1.7 # Maps the figure's height units to screen pixels
OFFSET_X = SCREEN_WIDTH // 2 # Center the figure horizontally on the screen
OFFSET_Y = SCREEN_HEIGHT * 0.9 # Position the 'ground' (y=0.0) near the bottom of the screen

def project_3d_to_2d(x_3d, y_3d, z_3d, angle, scale_factor, offset_x, offset_y):
    """
    Applies Y-axis rotation to a 3D point and projects it onto 2D screen coordinates.
    Rotation is around the y-axis (vertical axis), simulating a person turning.
    The y-coordinate (height) of the point remains unchanged during y-axis rotation.
    """
    
    # Perform 3D rotation around the Y-axis.
    # The new X coordinate on screen is derived from the original X and Z in 3D space.
    # X_new = X_old * cos(angle) - Z_old * sin(angle)
    # Z_new = X_old * sin(angle) + Z_old * cos(angle) (Z_new is not used for 2D projection)
    rotated_x = x_3d * math.cos(angle) - z_3d * math.sin(angle)

    # Scale the rotated X and original Y to screen pixel coordinates.
    # OFFSET_X centers the figure horizontally.
    screen_x = int(offset_x + rotated_x * scale_factor)
    # Pygame's Y-axis increases downwards, so subtract from OFFSET_Y to make higher Y-coords draw higher on screen.
    screen_y = int(offset_y - y_3d * scale_factor)
    
    return screen_x, screen_y

# Animation variables
rotation_angle = 0.0 # Start facing forward (0 degrees)
# Define a slow, deliberate rotation speed, contributing to the 'sad' and 'natural' feel.
# A full 360-degree turn (2 * pi radians) will take approx. 523 frames (2*pi / 0.012).
# At 60 frames per second, this means one full turn takes about 8.7 seconds.
rotation_speed = 0.012 # Radians per frame

# Game loop
running = True
clock = pygame.time.Clock()
FPS = 60 # Frames per second for smooth animation

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update rotation angle for the next frame
    rotation_angle += rotation_speed
    # Loop the animation indefinitely: if the angle exceeds 360 degrees, wrap it around.
    if rotation_angle > 2 * math.pi:
        rotation_angle -= 2 * math.pi

    # Drawing
    screen.fill(BLACK) # Clear screen with solid black background for each frame

    # Project each 3D point to 2D screen coordinates and draw it
    for coords_3d in BASE_POINTS_3D:
        x_3d, y_3d, z_3d = coords_3d
        screen_x, screen_y = project_3d_to_2d(x_3d, y_3d, z_3d, rotation_angle, SCALE_FACTOR, OFFSET_X, OFFSET_Y)
        pygame.draw.circle(screen, WHITE, (screen_x, screen_y), POINT_RADIUS)

    pygame.display.flip() # Update the entire screen to show the newly drawn frame

    clock.tick(FPS) # Control the frame rate to ensure smooth and consistent animation speed

# Quit Pygame
pygame.quit()
