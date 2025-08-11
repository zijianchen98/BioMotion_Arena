
import pygame
import math

# --- Pygame Initialization ---
pygame.init()

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_RADIUS = 5  # Size of the point lights
SCALE_FACTOR = 1.8  # Adjusts the overall size of the figure

# Center of the display for the figure. Y is adjusted to place the figure slightly above the true center.
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2 + 50

# Animation parameters
ROTATION_DURATION_SECONDS = 4  # Time for one full 360-degree rotation
ROTATION_SPEED_DEGREES_PER_FRAME = 360 / (FPS * ROTATION_DURATION_SECONDS)
current_rotation_angle = 0  # Current angle of the figure in degrees (0-360)

# Initial 3D coordinates of 15 body points relative to a central origin (e.g., pelvis/waist level).
# (x, y, z) where:
#   x: lateral displacement (positive right, negative left)
#   y: vertical displacement (positive up, negative down). The pelvis is set at y=-20.
#   z: depth displacement (positive forward, negative backward)
# These values are chosen to approximate a human body structure, with subtle
# adjustments for a "sadman" (slightly lower shoulders, perhaps less upright posture)
# and to ensure plausible 3D projection during turning.
POINTS_3D_INIT = {
    # Head and Neck
    'head': (0, 100, 0),
    'neck': (0, 80, 0),
    # Shoulders, Elbows, Wrists (Arms)
    # Arms are slightly forward (positive z) to show depth during rotation
    'r_shoulder': (30, 65, 10),
    'l_shoulder': (-30, 65, 10),
    'r_elbow': (45, 30, 15),
    'l_elbow': (-45, 30, 15),
    'r_wrist': (60, 0, 20),
    'l_wrist': (-60, 0, 20),
    # Hips, Knees, Ankles (Legs)
    # Knees and ankles are slightly backward (negative z) for a more relaxed/sad posture
    'r_hip': (15, -20, 0),
    'l_hip': (-15, -20, 0),
    'r_knee': (20, -65, -5),  # Slightly bent knees
    'l_knee': (-20, -65, -5),
    'r_ankle': (25, -100, -10),  # Slight foot placement behind
    'l_ankle': (-25, -100, -10),
    # Pelvis/Core point, roughly at the center of the hips
    'pelvis': (0, -20, 0)
}

# --- Pygame Setup ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Sadman Turning Around")
clock = pygame.time.Clock()

# --- Animation Loop ---
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the global rotation angle for the figure
    current_rotation_angle = (current_rotation_angle + ROTATION_SPEED_DEGREES_PER_FRAME) % 360
    angle_rad = math.radians(current_rotation_angle)

    # --- Drawing ---
    screen.fill(BLACK)  # Clear screen with black background

    # Calculate a subtle vertical bobbing motion to add realism
    # This simulates natural weight shifts or breathing during movement.
    # The bobbing frequency is set to create 2 cycles per full rotation (e.g., for two 'steps' or sway).
    bob_amplitude = 5  # Maximum vertical displacement in pixels
    bob_frequency = 2  # Cycles of bobbing per 360-degree turn
    y_bob_offset = bob_amplitude * math.sin(angle_rad * bob_frequency)

    # Iterate through each defined body point
    for point_name, (x_init, y_init, z_init) in POINTS_3D_INIT.items():
        # Apply Y-axis rotation to the 3D coordinates.
        # This transforms the initial (x, y, z) into (x_rotated, y_rotated, z_rotated)
        # as the figure turns around its vertical axis.
        # The rotation formulas are for rotating (x, z) around the origin in the X-Z plane.
        x_rotated = x_init * math.cos(angle_rad) + z_init * math.sin(angle_rad)
        y_rotated = y_init  # Y-coordinate remains unchanged for rotation around Y-axis
        z_rotated = -x_init * math.sin(angle_rad) + z_init * math.cos(angle_rad)

        # Apply the vertical bobbing offset to all points
        y_rotated += y_bob_offset

        # Project the 3D point onto 2D screen coordinates.
        # The x_rotated value directly becomes the screen x coordinate.
        # The y_rotated value becomes the screen y coordinate, but is inverted
        # because Pygame's Y-axis increases downwards, while our model's Y increases upwards.
        # SCALE_FACTOR adjusts the visual size of the human figure.
        screen_x = CENTER_X + x_rotated * SCALE_FACTOR
        screen_y = CENTER_Y - y_rotated * SCALE_FACTOR

        # Draw the white point-light on the screen
        pygame.draw.circle(screen, WHITE, (int(screen_x), int(screen_y)), POINT_RADIUS)

    # Update the entire screen to show the newly drawn frame
    pygame.display.flip()

    # Control the animation speed by limiting the frame rate
    clock.tick(FPS)

# --- Quit Pygame ---
pygame.quit()
