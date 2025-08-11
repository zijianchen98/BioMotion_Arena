
import pygame
import math

# --- Configuration ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2 + 100  # Shift figure slightly down for better centering

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
POINT_RADIUS_BASE = 5  # Base radius of the circle for each point
POINT_COLOR = WHITE

# Conversion factor from abstract model units to screen pixels
# This scales the human figure to a reasonable size on the screen.
# A figure height of ~1.6 units * 150 pixels/unit = 240 pixels tall.
SCALE_FACTOR = 150

# Biomechanical model (15 points)
# Initial 3D coordinates [x, y, z] relative to the body's center (pelvis).
# x: side-to-side (positive for right, negative for left)
# y: up-down (positive for up, negative for down)
# z: front-back (positive for towards viewer, negative for away from viewer)
# These Z-coordinates are crucial for creating a 3D turning effect.
initial_points_3d = {
    "head":        [0.0,   0.9,  0.05],  # Top of the head, slightly forward
    "neck":        [0.0,   0.7,  0.02],  # Base of the neck
    "r_shoulder":  [0.2,   0.6, -0.05],  # Right shoulder, slightly behind torso center
    "l_shoulder":  [-0.2,  0.6, -0.05],  # Left shoulder, slightly behind torso center
    "r_elbow":     [0.3,   0.3,  0.05],  # Right elbow, slightly in front
    "l_elbow":     [-0.3,  0.3,  0.05],  # Left elbow, slightly in front
    "r_wrist":     [0.35,  0.0,  0.08],  # Right wrist, furthest forward
    "l_wrist":     [-0.35, 0.0,  0.08],  # Left wrist, furthest forward
    "pelvis_center":[0.0,   0.0,  0.0],   # Center of the body, origin for rotation
    "r_hip":       [0.1,  -0.1,  0.01],  # Right hip
    "l_hip":       [-0.1,  -0.1,  0.01],  # Left hip
    "r_knee":      [0.15, -0.4,  0.03],  # Right knee
    "l_knee":      [-0.15, -0.4,  0.03],  # Left knee
    "r_ankle":     [0.15, -0.7,  0.05],  # Right ankle
    "l_ankle":     [-0.15, -0.7,  0.05],  # Left ankle
}

# Animation parameters for "turning around with heavy weight"
# The "heavy weight" is simulated by:
# 1. Slower rotation speed.
# 2. Subtle bobbing (vertical oscillation) and swaying (horizontal oscillation)
#    of the entire figure, suggesting effort and balance shifts.
rotation_angle = 0.0      # Current global rotation angle around Y-axis (in radians)
rotation_speed = 0.015    # Radians per frame (approx 0.86 deg/frame)
                          # A full 360-degree turn takes about 5.2 seconds at 60 FPS,
                          # which feels appropriate for "heavy weight".

bob_amplitude = 0.01      # Vertical oscillation amplitude (in model units)
bob_frequency = 0.08      # Frequency of bobbing (radians per frame)
sway_amplitude = 0.008    # Horizontal sway amplitude (in model units)
sway_frequency = 0.04     # Frequency of swaying (radians per frame)

# Perspective projection settings
CAMERA_DISTANCE = 5.0     # Distance of the virtual camera from the origin (0,0,0).
                          # Larger values reduce perspective distortion (more orthographic look).
                          # Smaller values increase distortion (more dramatic 3D effect).

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Turning with Heavy Weight")
clock = pygame.time.Clock()

# --- Animation Loop ---
running = True
frame_count = 0

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Update global rotation angle for the entire figure
    rotation_angle += rotation_speed
    # Loop the rotation angle to keep it within [0, 2*pi)
    if rotation_angle >= 2 * math.pi:
        rotation_angle -= 2 * math.pi

    # Calculate current global bobbing (vertical shift) and swaying (horizontal shift)
    # These movements are applied to the entire figure to simulate "heavy weight" exertion.
    current_bob = bob_amplitude * math.sin(frame_count * bob_frequency)
    # Phase shift sway to make it look less robotic relative to bobbing
    current_sway = sway_amplitude * math.sin(frame_count * sway_frequency + math.pi / 2)

    # List to store 2D screen coordinates and radii for drawing
    points_to_draw = []

    # Process each 3D point
    for name, coords in initial_points_3d.items():
        x, y, z = coords

        # Step 1: Apply global rotation around the Y-axis (vertical axis)
        # This transforms the 3D coordinates of each point as the body turns.
        rotated_x = x * math.cos(rotation_angle) - z * math.sin(rotation_angle)
        rotated_z = x * math.sin(rotation_angle) + z * math.cos(rotation_angle)
        rotated_y = y  # Y-coordinate is unchanged during Y-axis rotation

        # Step 2: Apply global bobbing and swaying
        # These are subtle shifts applied to the rotated coordinates.
        final_x = rotated_x + current_sway
        final_y = rotated_y + current_bob
        final_z = rotated_z  # Z-coordinate (depth) is not affected by bob/sway in this model

        # Step 3: Project 3D coordinates to 2D screen coordinates with perspective
        # The `divisor` calculates the effective distance from the camera.
        # Points further away (larger `final_z` in our coordinate system where positive Z is towards viewer)
        # will have a larger `divisor` and thus a smaller `perspective_scale`.
        # This makes closer points appear larger and further points appear smaller.
        divisor = CAMERA_DISTANCE + final_z
        
        # If a point goes behind or exactly at the camera plane, skip drawing it to avoid division by zero or inverse perspective.
        if divisor <= 0:
            continue

        perspective_scale = CAMERA_DISTANCE / divisor

        # Apply scaling and offset to center the figure on screen (Y-axis is inverted in Pygame)
        screen_x = int(CENTER_X + final_x * SCALE_FACTOR * perspective_scale)
        screen_y = int(CENTER_Y - final_y * SCALE_FACTOR * perspective_scale)

        # Scale point radius based on its perceived distance (perspective)
        point_radius_actual = int(POINT_RADIUS_BASE * perspective_scale)
        if point_radius_actual < 1:  # Ensure a minimum visible size
            point_radius_actual = 1

        points_to_draw.append((screen_x, screen_y, point_radius_actual))

    # Draw all the projected points
    for sx, sy, r in points_to_draw:
        pygame.draw.circle(screen, POINT_COLOR, (sx, sy), r)

    # Update the display
    pygame.display.flip()

    # Increment frame count and control frame rate
    frame_count += 1
    clock.tick(60)  # Limit to 60 frames per second

# Quit Pygame
pygame.quit()
