
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
POINT_RADIUS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# --- Animation Parameters ---
ROLL_SPEED_DPS = 270  # Degrees per second for rotation (e.g., 270 means 3/4 revolution per second)
FORWARD_SPEED_PPS = 150 # Pixels per second for horizontal movement
TUCK_AMOUNT = 0.4    # Max percentage reduction in limb length during tuck (0.0 to 1.0).
                      # A value of 0.4 means limbs can reduce to 60% (1-0.4) of original length.
VERTICAL_BOUNCE_AMPLITUDE = 60 # Pixels: how much the body's center of mass rises and falls during the roll.

# Approximate dimensions for the standing figure, used to define relative point positions.
# These values are chosen to match the proportions shown in the example image.
BODY_VISUAL_HEIGHT = 180 # Approximate pixel height of the standing figure
BODY_VISUAL_WIDTH = 100  # Approximate pixel width of the standing figure

# Initial relative positions of the 15 points for a standing figure.
# The origin (0,0) is set to be roughly the pelvis/center of rotation.
# Y-coordinates are positive downwards in Pygame.
BODY_POINTS_RELATIVE_INITIAL = {
    'head':       (0, -0.55 * BODY_VISUAL_HEIGHT),  # 1
    'l_shoulder': (-0.15 * BODY_VISUAL_WIDTH, -0.3 * BODY_VISUAL_HEIGHT), # 2
    'r_shoulder': (0.15 * BODY_VISUAL_WIDTH, -0.3 * BODY_VISUAL_HEIGHT),  # 3
    'l_elbow':    (-0.25 * BODY_VISUAL_WIDTH, -0.05 * BODY_VISUAL_HEIGHT), # 4
    'r_elbow':    (0.25 * BODY_VISUAL_WIDTH, -0.05 * BODY_VISUAL_HEIGHT),  # 5
    'l_wrist':    (-0.3 * BODY_VISUAL_WIDTH, 0.15 * BODY_VISUAL_HEIGHT),  # 6
    'r_wrist':    (0.3 * BODY_VISUAL_WIDTH, 0.15 * BODY_VISUAL_HEIGHT),   # 7
    'l_hip':      (-0.1 * BODY_VISUAL_WIDTH, 0.1 * BODY_VISUAL_HEIGHT),   # 8
    'r_hip':      (0.1 * BODY_VISUAL_WIDTH, 0.1 * BODY_VISUAL_HEIGHT),    # 9
    'l_knee':     (-0.15 * BODY_VISUAL_WIDTH, 0.35 * BODY_VISUAL_HEIGHT), # 10
    'r_knee':     (0.15 * BODY_VISUAL_WIDTH, 0.35 * BODY_VISUAL_HEIGHT),  # 11
    'l_ankle':    (-0.2 * BODY_VISUAL_WIDTH, 0.45 * BODY_VISUAL_HEIGHT),  # 12
    'r_ankle':    (0.2 * BODY_VISUAL_WIDTH, 0.45 * BODY_VISUAL_HEIGHT),   # 13
    'l_foot':     (-0.22 * BODY_VISUAL_WIDTH, 0.5 * BODY_VISUAL_HEIGHT),  # 14
    'r_foot':     (0.22 * BODY_VISUAL_WIDTH, 0.5 * BODY_VISUAL_HEIGHT)    # 15
}

# List of points that will "tuck in" (i.e., limbs)
TUCKING_POINTS = [
    'l_elbow', 'r_elbow', 'l_wrist', 'r_wrist',
    'l_knee', 'r_knee', 'l_ankle', 'r_ankle', 'l_foot', 'r_foot'
]

# --- Helper Functions ---
def rotate_point(x, y, angle_rad):
    """Rotates a point (x, y) around the origin (0,0) by angle_rad."""
    cos_angle = math.cos(angle_rad)
    sin_angle = math.sin(angle_rad)
    new_x = x * cos_angle - y * sin_angle
    new_y = x * sin_angle + y * cos_angle
    return new_x, new_y

def get_tuck_factor(angle_rad):
    """
    Determines the tucking amount based on the current rotation angle.
    The body is most tucked when it is horizontal (e.g., rotating over the back or belly,
    at 90 degrees or 270 degrees relative to upright).
    It is least tucked (fully extended) when vertical (e.g., standing upright or upside down,
    at 0 degrees or 180 degrees).
    The formula `(1 - math.cos(angle_rad * 2)) / 2` creates a sine-like wave that ranges from 0 to 1,
    where 0 is at 0, pi, 2pi (vertical positions) and 1 is at pi/2, 3pi/2 (horizontal positions).
    This value then scales the `TUCK_AMOUNT`.
    """
    tuck_scale = (1 - math.cos(angle_rad * 2)) / 2
    return 1.0 - (tuck_scale * TUCK_AMOUNT) # 1.0 means no tuck, smaller means more tuck

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Forward Roll")
clock = pygame.time.Clock()

# --- Animation State ---
# Initial horizontal position of the body's center of mass.
body_center_x = SCREEN_WIDTH / 4
# Base Y position for the center of the body. This is where the COM would be at its lowest point.
BASE_BODY_CENTER_Y = SCREEN_HEIGHT / 2 + 50 

current_rotation_angle_rad = 0 # Radians, starts at 0 (upright)

running = True
while running:
    dt = clock.tick(FPS) / 1000.0 # Delta time in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update Animation State ---
    # 1. Update horizontal position
    body_center_x += FORWARD_SPEED_PPS * dt
    # Loop back if the figure rolls off-screen to create a continuous animation.
    # Add a margin to ensure the figure fully exits before re-entering.
    if body_center_x > SCREEN_WIDTH + BODY_VISUAL_WIDTH / 2:
        body_center_x = -BODY_VISUAL_WIDTH / 2

    # 2. Update rotation angle
    current_rotation_angle_rad += math.radians(ROLL_SPEED_DPS) * dt
    current_rotation_angle_rad %= (2 * math.pi) # Keep angle within 0 to 2*pi

    # 3. Update vertical position for Center of Mass (COM) bounce/tumble.
    # When vertical (angle 0 or pi), the COM is typically highest in a roll (over feet or head).
    # When horizontal (angle pi/2 or 3pi/2), the COM is typically lowest (rolling over back/belly).
    # `abs(math.cos(current_rotation_angle_rad))` is 1 when vertical (0, pi) and 0 when horizontal (pi/2, 3pi/2).
    # We subtract this value from BASE_BODY_CENTER_Y, so a larger value means a smaller Y-coordinate (higher on screen).
    body_center_y = BASE_BODY_CENTER_Y - VERTICAL_BOUNCE_AMPLITUDE * abs(math.cos(current_rotation_angle_rad))

    # --- Drawing ---
    screen.fill(BLACK)

    # Calculate the tucking factor for limbs based on the current rotation angle.
    tuck_factor = get_tuck_factor(current_rotation_angle_rad)

    for point_name, initial_coords in BODY_POINTS_RELATIVE_INITIAL.items():
        x_rel, y_rel = initial_coords # Start with the original relative coordinates

        # Apply tucking only to limb points (elbows, wrists, knees, ankles, feet)
        if point_name in TUCKING_POINTS:
            # Calculate the distance of the point from the body's center.
            dist = math.sqrt(x_rel**2 + y_rel**2)
            if dist > 0: # Prevent division by zero for points at the origin (though none are defined there).
                # Normalize the vector to the point (unit direction)
                norm_x = x_rel / dist
                norm_y = y_rel / dist
                # Scale the distance by the tuck factor, effectively moving the point closer to the origin.
                x_rel = norm_x * dist * tuck_factor
                y_rel = norm_y * dist * tuck_factor

        # Rotate the (potentially tucked) point around the body's current center.
        rotated_x_rel, rotated_y_rel = rotate_point(x_rel, y_rel, current_rotation_angle_rad)

        # Translate the rotated relative coordinates to absolute screen coordinates.
        screen_x = int(body_center_x + rotated_x_rel)
        screen_y = int(body_center_y + rotated_y_rel)

        # Draw the white point-light.
        pygame.draw.circle(screen, WHITE, (screen_x, screen_y), POINT_RADIUS)

    pygame.display.flip() # Update the full display surface to show the new frame.

pygame.quit() # Uninitialize Pygame modules.
