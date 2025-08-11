
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
POINT_RADIUS = 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define 15 key points of a human body, relative to its center of mass (Pelvis)
# These are approximate offsets for a person curled into a ball, suitable for rolling.
# The local origin (0,0) for these offsets is assumed to be the body's center of mass (Pelvis).
#
# Index Map (for internal understanding, not explicitly used in iteration):
# 0: Head
# 1: Neck
# 2: L_SHOULDER, 3: R_SHOULDER
# 4: L_ELBOW, 5: R_ELBOW
# 6: L_WRIST, 7: R_WRIST
# 8: PELVIS (center of rotation, assumed CoM)
# 9: L_HIP, 10: R_HIP
# 11: L_KNEE, 12: R_KNEE
# 13: L_ANKLE, 14: R_ANKLE

# Initial relative offsets from the body's local origin (Pelvis at (0,0) in local space)
# Values are in arbitrary units, chosen to represent a tucked human form.
initial_offsets_relative = [
    (0, -30),    # 0 Head (tucked forward/down, highest point relative to CoM)
    (0, -20),    # 1 Neck
    (-15, -10),  # 2 L_SHOULDER
    (15, -10),   # 3 R_SHOULDER
    (-20, 0),    # 4 L_ELBOW (arms tucked close to body)
    (20, 0),     # 5 R_ELBOW
    (-15, 10),   # 6 L_WRIST
    (15, 10),    # 7 R_WRIST
    (0, 0),      # 8 PELVIS (defined as the center of mass/rotation)
    (-10, 5),    # 9 L_HIP
    (10, 5),     # 10 R_HIP
    (-15, 20),   # 11 L_KNEE (drawn up towards chest)
    (15, 20),    # 12 R_KNEE
    (-10, 25),   # 13 L_ANKLE (feet tucked in, lowest point relative to CoM)
    (10, 25)     # 14 R_ANKLE
]

# Scale factor to convert arbitrary units to pixels for on-screen display.
# Adjust this to change the size of the human figure.
SCALE = 2.5 

# Apply the scale to the initial relative offsets.
initial_offsets = [(x * SCALE, y * SCALE) for x, y in initial_offsets_relative]

# Calculate the maximum distance any point is from the local origin (CoM).
# This represents the effective "radius" of the curled-up body, crucial for
# simulating rolling on a flat surface.
max_dist_from_origin = 0
for x, y in initial_offsets:
    dist = math.sqrt(x**2 + y**2)
    max_dist_from_origin = max(max_dist_from_origin, dist)

# --- Animation Parameters ---
# Define the "ground" level on the screen.
GROUND_LEVEL_SCREEN_Y = SCREEN_HEIGHT - 20 # 20 pixels from the bottom edge of the screen

# The Y-coordinate of the body's center of mass (CoM).
# For a circular body rolling on a flat surface, its center remains at a fixed height
# equal to `GROUND_LEVEL - radius`.
COM_Y = GROUND_LEVEL_SCREEN_Y - max_dist_from_origin

# Define the horizontal range for the rolling animation.
# The body starts off-screen to the left and rolls across to off-screen right, then loops.
COM_X_START = -max_dist_from_origin * 2 
COM_X_END = SCREEN_WIDTH + max_dist_from_origin * 2 

# Define the speed of the roll. "Heavy weight" implies a relatively slow and deliberate roll.
ROLL_SPEED_X_PPS = 50 # Linear speed: 50 pixels per second horizontal movement.

# For realistic "rolling without slipping", the angular speed is related to linear speed
# and the effective radius: angular_speed = linear_speed / radius.
ROLL_SPEED_ANGULAR_RADPS = ROLL_SPEED_X_PPS / max_dist_from_origin # Radians per second

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Forward Rolling")
clock = pygame.time.Clock()

# --- Animation Variables ---
current_com_x = COM_X_START
current_angle_rad = 0.0 # Current rotation angle in radians

# --- Game Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate delta time (time elapsed since the last frame) for frame-rate independent motion.
    dt = clock.tick(FPS) / 1000.0 # Time in seconds

    # Update the body's center of mass (CoM) horizontal position.
    current_com_x += ROLL_SPEED_X_PPS * dt
    # Loop the animation: if the body rolls off the right side, reset it to the left.
    if current_com_x > COM_X_END:
        current_com_x = COM_X_START 

    # Update the angular position for continuous rotation.
    current_angle_rad += ROLL_SPEED_ANGULAR_RADPS * dt

    # Clear the screen to black for the new frame.
    screen.fill(BLACK)

    # Calculate and draw each of the 15 points.
    for offset_x, offset_y in initial_offsets:
        # Apply rotation to the point's relative offset.
        # Standard 2D rotation formulas:
        # x' = x * cos(angle) - y * sin(angle)
        # y' = x * sin(angle) + y * cos(angle)
        rotated_x = offset_x * math.cos(current_angle_rad) - offset_y * math.sin(current_angle_rad)
        rotated_y = offset_x * math.sin(current_angle_rad) + offset_y * math.cos(current_angle_rad)

        # Translate the rotated point to its global screen position by adding the CoM position.
        point_screen_x = int(current_com_x + rotated_x)
        point_screen_y = int(COM_Y + rotated_y)

        # Draw the point as a white circle.
        pygame.draw.circle(screen, WHITE, (point_screen_x, point_screen_y), POINT_RADIUS)

    # Update the display to show the newly drawn frame.
    pygame.display.flip()

# Quit Pygame when the loop finishes.
pygame.quit()
