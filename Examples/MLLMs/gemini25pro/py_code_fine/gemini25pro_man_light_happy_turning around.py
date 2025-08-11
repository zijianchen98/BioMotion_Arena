
import pygame
import numpy as np
import sys

# --- Constants ---
# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 800
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Animation parameters
FPS = 60
POINT_RADIUS = 6
# Rotation speed in radians per frame. Negative for clockwise.
ROTATION_SPEED = -0.015
# Parameters for the "happy" bounce motion
BOUNCE_AMPLITUDE = 5  # Vertical movement in pixels
BOUNCE_FREQUENCY = 2  # Number of bounces per full 360-degree rotation

# --- 3D Point-Light Model Data ---
# A 15-point model representing the major joints of a human figure.
# This structure is standard for biological motion studies.
# Coordinates are in a 3D space (x, y, z) centered around the body's core.
# Y-axis is vertical (positive up), X-axis is horizontal, Z-axis is depth.
# The initial coordinates define a neutral standing pose designed to
# resemble the style of the provided example image.
points_3d_base = np.array([
    # [x, y, z]
    # Head and Torso (5 points)
    [0, 200, 0],      # 1. Head
    [0, 140, 0],      # 2. Sternum (between shoulders)
    [-35, 145, 0],    # 3. Left Shoulder
    [35, 145, 0],     # 4. Right Shoulder
    [0, 60, 0],       # 5. Pelvis (center of rotation)

    # Arms (4 points)
    [-60, 100, 5],    # 6. Left Elbow
    [60, 100, 5],     # 7. Right Elbow
    [-70, 45, 10],    # 8. Left Wrist
    [70, 45, 10],     # 9. Right Wrist

    # Legs (6 points)
    [-30, 60, 0],     # 10. Left Hip
    [30, 60, 0],      # 11. Right Hip
    [-25, -20, 0],    # 12. Left Knee
    [25, -20, 0],     # 13. Right Knee
    [-25, -100, 0],   # 14. Left Ankle
    [25, -100, 0],    # 15. Right Ankle
])

def main():
    """
    Main function to initialize Pygame, run the animation loop,
    and display the point-light stimulus of a person turning around.
    """
    pygame.init()

    # Set up the display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Turning Around")
    clock = pygame.time.Clock()

    # Animation state variable for the current rotation angle
    angle = 0.0
    running = True

    while running:
        # --- Event Handling ---
        # Check for quit events (closing the window or pressing ESC)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- Update Physics and Motion ---
        # Increment the rotation angle for the next frame
        angle += ROTATION_SPEED
        # Keep the angle within one full circle to prevent floating point errors
        if abs(angle) > 2 * np.pi:
            angle %= (2 * np.pi)

        # Create the 3D rotation matrix for rotation around the vertical (Y) axis
        cos_a = np.cos(angle)
        sin_a = np.sin(angle)
        rotation_matrix_y = np.array([
            [cos_a, 0, sin_a],
            [0, 1, 0],
            [-sin_a, 0, cos_a]
        ])

        # Apply the rotation to the base model points using matrix multiplication
        rotated_points_3d = points_3d_base @ rotation_matrix_y.T

        # Add a subtle vertical bounce to simulate a more natural, "happy" motion
        y_offset = BOUNCE_AMPLITUDE * np.cos(angle * BOUNCE_FREQUENCY)
        rotated_points_3d[:, 1] += y_offset

        # --- Drawing ---
        # Clear the screen with a solid black background
        screen.fill(BLACK)

        # Project the 3D points to 2D screen coordinates and draw them
        for point_3d in rotated_points_3d:
            x_3d, y_3d, z_3d = point_3d
            
            # Simple orthographic projection with screen transformation:
            # 1. Center the figure horizontally (add SCREEN_WIDTH / 2).
            # 2. Center the figure vertically (add SCREEN_HEIGHT / 2).
            # 3. Invert the y-axis because Pygame's y=0 is at the top.
            screen_x = int(x_3d + SCREEN_WIDTH / 2)
            screen_y = int(-y_3d + SCREEN_HEIGHT / 2)

            # Draw the point as a white circle
            pygame.draw.circle(screen, WHITE, (screen_x, screen_y), POINT_RADIUS)

        # Update the full display surface to the screen
        pygame.display.flip()

        # Control the animation speed by capping the frame rate
        clock.tick(FPS)

    # Clean up and exit
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
