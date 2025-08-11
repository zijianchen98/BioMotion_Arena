
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion Stimulus: Turning Around")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light parameters
POINT_RADIUS = 5  # Size of the white dots

# Biomechanical model (simplified 15 points)
# Points are defined relative to a central origin (e.g., mid-hip) at (0,0,0)
# Y: vertical (up/down)
# X: horizontal (left/right)
# Z: depth (forward/backward from viewer). Positive Z means closer to viewer.
# Initial pose: Facing forward (viewer).
# These are rough estimations of human joint positions in a normalized space.
# The relative positions are designed to suggest a 'woman with heavy weight' through
# a slightly wider stance and generally upright posture.
initial_points_3d = {
    "head":           (0.0,   0.40,  0.0),
    "neck":           (0.0,   0.30,  0.0),  # Base of neck / top of spine
    "l_shoulder":     (-0.16, 0.25,  0.0),  # Slightly wider shoulders
    "r_shoulder":     (0.16,  0.25,  0.0),
    "l_elbow":        (-0.26, 0.10,  0.0),
    "r_elbow":        (0.26,  0.10,  0.0),
    "l_wrist":        (-0.31, -0.05, 0.0),
    "r_wrist":        (0.31,  -0.05, 0.0),
    "torso_center":   (0.0,   0.15,  0.0),  # Mid-torso/spine
    "l_hip":          (-0.10, 0.0,   0.0),  # Wider hips for "heavy weight" suggestion
    "r_hip":          (0.10,  0.0,   0.0),
    "l_knee":         (-0.10, -0.20, 0.0),
    "r_knee":         (0.10,  -0.20, 0.0),
    "l_ankle":        (-0.10, -0.40, 0.0),
    "r_ankle":        (0.10,  -0.40, 0.0),
}

# Ensure exactly 15 points
if len(initial_points_3d) != 15:
    raise ValueError(f"Expected 15 points, but got {len(initial_points_3d)}. "
                     "Please ensure the 'initial_points_3d' dictionary contains exactly 15 entries.")

# Convert dict to a list of (name, (x,y,z)) for consistent processing order
points_list = [(name, pos) for name, pos in initial_points_3d.items()]

# Scaling factors for mapping normalized coordinates to screen pixels
# These determine the overall size of the human figure on screen.
BODY_HEIGHT_SCALE = 220  # Height from feet to head. Adjust as needed.
BODY_WIDTH_SCALE = 180   # Width of the figure. Adjust as needed.

# Center of the figure on screen
# Adjusted so the figure is centered vertically, slightly up from true center
# to account for typical standing poses
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2 + 50

# Animation parameters
rotation_angle = 0.0  # Current rotation angle in radians (initial: facing forward)
# Speed of rotation (radians per frame). Slower for 'heavy weight' suggestion.
# 0.5 degrees per frame = 0.5 * pi / 180 radians/frame.
# At 60 FPS, a full 360-degree turn will take 720 frames (12 seconds), suggesting a deliberate pace.
rotation_speed = math.radians(0.5)

# Game loop
running = True
clock = pygame.time.Clock()
FPS = 60  # Frames per second for smooth animation

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  # Clear the screen with black

    # Update global rotation angle for the entire body
    rotation_angle += rotation_speed
    # Loop the rotation continuously after a full turn (360 degrees)
    if rotation_angle > 2 * math.pi:
        rotation_angle -= 2 * math.pi

    # Calculate and draw 2D projected points
    for name, (x, y, z) in points_list:
        # Apply Y-axis rotation to the 3D point (x, y, z)
        # The formulas for 3D rotation around the Y-axis are:
        # new_x = x * cos(angle) - z * sin(angle)
        # new_z = x * sin(angle) + z * cos(angle)
        # new_y = y (Y-coordinate remains unchanged for Y-axis rotation)
        rotated_x = x * math.cos(rotation_angle) - z * math.sin(rotation_angle)
        rotated_z = x * math.sin(rotation_angle) + z * math.cos(rotation_angle)
        rotated_y = y # Y-coordinate remains unchanged by Y-axis rotation

        # Project the rotated 3D point onto the 2D screen.
        # Orthographic projection is used, meaning Z is only for rotation calculation,
        # not for scaling the visual size of the points, as per the example image.
        # Scale the coordinates to screen pixels and translate to the screen center.
        screen_x = CENTER_X + rotated_x * BODY_WIDTH_SCALE
        screen_y = CENTER_Y - rotated_y * BODY_HEIGHT_SCALE  # Y-axis inverted for screen coordinates (origin is top-left)

        # Draw the white circle point
        pygame.draw.circle(screen, WHITE, (int(screen_x), int(screen_y)), POINT_RADIUS)

    pygame.display.flip()  # Update the full display surface to show the new frame
    clock.tick(FPS)        # Control the frame rate

pygame.quit()
