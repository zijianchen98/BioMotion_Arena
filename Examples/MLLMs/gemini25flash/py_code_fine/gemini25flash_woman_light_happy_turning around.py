
import pygame
import math

# --- Pygame Setup ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60
POINT_RADIUS = 7  # Size of the white dots
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion Stimulus: Woman Turning Around")
clock = pygame.time.Clock()

# --- Human Model Parameters ---
# Proportional distances. Will be scaled to screen pixels.
# Y-axis is vertical (height), X-axis is horizontal (width), Z-axis is depth.
# Origin (0,0,0) for the model's coordinates is at the PELVIS_BASE.

HUMAN_SCALE = 200  # How many pixels per 'unit' in our model
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2 + 100  # Shift slightly down to center the figure vertically

# 15 points definition based on standard biological motion stimulus and example image
# Y values represent relative height. Z values represent initial depth (e.g., hands slightly forward)
POINTS_3D_INITIAL = {
    "HEAD":         (0.0, 0.9, 0.0),
    "SHOULDER_R":   (-0.2, 0.7, 0.0),
    "SHOULDER_L":   (0.2, 0.7, 0.0),
    "ELBOW_R":      (-0.35, 0.45, 0.1),  # Slightly bent forward
    "ELBOW_L":      (0.35, 0.45, 0.1),
    "WRIST_R":      (-0.4, 0.2, 0.2),   # Further bent forward
    "WRIST_L":      (0.4, 0.2, 0.2),
    "TORSO_CENTER": (0.0, 0.55, 0.0),   # Mid-chest/upper spine
    "HIP_R":        (-0.1, 0.0, 0.0),
    "HIP_L":        (0.1, 0.0, 0.0),
    "KNEE_R":       (-0.15, -0.4, 0.1),  # Slightly bent forward
    "KNEE_L":       (0.15, -0.4, 0.1),
    "ANKLE_R":      (-0.15, -0.8, 0.0),
    "ANKLE_L":      (0.15, -0.8, 0.0),
    "PELVIS_BASE":  (0.0, 0.0, 0.0)      # The 15th point, chosen as origin for simplicity
}

# --- Animation Parameters ---
# Base rotation speed for the whole body
ROTATION_SPEED_RAD_PER_SEC = math.radians(60) # 60 degrees per second for full body turn
# Time for one full rotation: 2*pi radians / (radians/sec) = seconds
TIME_PERIOD_FULL_TURN = (2 * math.pi) / ROTATION_SPEED_RAD_PER_SEC 

# Secondary motion parameters to enhance realism and express "light weight" / "happy"
ARM_SWING_AMPLITUDE_X = 0.05 # How much arms swing forward/backward (local X-axis)
ARM_SWING_AMPLITUDE_Z = 0.05 # How much arms swing slightly in/out (local Z-axis)
ARM_SWING_FREQUENCY_MULTIPLIER = 1.5 # Arms swing slightly faster than body rotation

HEAD_LEAD_LAG_AMPLITUDE = math.radians(10) # Head can slightly lead/lag the body turn
HEAD_LEAD_LAG_PHASE_OFFSET = math.pi / 8 # Head turn phase relative to body turn

BOB_AMPLITUDE = 0.02 # Up/down bobbing motion (Y-axis)
BOB_FREQUENCY_MULTIPLIER = 2 # Bob twice per full turn, suggesting a rhythmic step or pivot

# Function to rotate a 3D point around the Y-axis
def rotate_y(point, angle):
    x, y, z = point
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    new_x = x * cos_a + z * sin_a
    new_z = -x * sin_a + z * cos_a
    return (new_x, y, new_z)

# Function to apply specific arm motion
def apply_arm_swing(point_name, initial_pos, current_time):
    x, y, z = initial_pos
    # Create an oscillating motion for arm points relative to their initial position
    # This motion is added in the *local* coordinate system before the main body rotation.
    swing_angle = ARM_SWING_AMPLITUDE_X * math.sin(current_time * ROTATION_SPEED_RAD_PER_SEC * ARM_SWING_FREQUENCY_MULTIPLIER)
    side_swing = ARM_SWING_AMPLITUDE_Z * math.cos(current_time * ROTATION_SPEED_RAD_PER_SEC * ARM_SWING_FREQUENCY_MULTIPLIER)

    # Arms swing in opposition or for balance
    if "RIGHT" in point_name:
        new_x = x + swing_angle
        new_z = z + side_swing
    elif "LEFT" in point_name:
        new_x = x - swing_angle
        new_z = z - side_swing
    else:
        new_x, new_z = x, z # Should not happen for arm points passed here

    return (new_x, y, new_z)

# Function to apply specific head motion (lead/lag)
def apply_head_motion(initial_pos, current_time, base_angle):
    x, y, z = initial_pos
    # Head slightly leads or lags the main body rotation
    head_offset_angle = HEAD_LEAD_LAG_AMPLITUDE * math.sin(current_time * ROTATION_SPEED_RAD_PER_SEC + HEAD_LEAD_LAG_PHASE_OFFSET)
    # Apply this small additional rotation in the head's local frame
    return rotate_y((x, y, z), head_offset_angle)

# Function to apply bobbing motion
def apply_bobbing(initial_pos, current_time):
    x, y, z = initial_pos
    # Smooth up-and-down motion for the whole figure
    bob_offset = BOB_AMPLITUDE * math.sin(current_time * ROTATION_SPEED_RAD_PER_SEC * BOB_FREQUENCY_MULTIPLIER)
    return (x, y + bob_offset, z)

# --- Main Animation Loop ---
running = True
start_time = pygame.time.get_ticks() / 1000.0  # Time in seconds for animation start

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks() / 1000.0 - start_time
    # The total rotation angle for the main body
    total_rotation_angle = (current_time * ROTATION_SPEED_RAD_PER_SEC) % (2 * math.pi)

    screen.fill(BLACK)  # Solid black background

    projected_points_on_screen = []

    for label, initial_pos in POINTS_3D_INITIAL.items():
        # Apply global bobbing motion to all points
        current_pos = apply_bobbing(initial_pos, current_time)

        # Apply specific arm motion to arm points (relative to their local position)
        if "ELBOW" in label or "WRIST" in label:
            current_pos = apply_arm_swing(label, current_pos, current_time)
        
        # Apply specific head motion (lead/lag)
        if label == "HEAD":
            current_pos = apply_head_motion(current_pos, current_time, total_rotation_angle)

        # Apply the main body rotation around the Y-axis (vertical axis)
        rotated_pos = rotate_y(current_pos, total_rotation_angle)

        # Project 3D point (x, y, z) to 2D screen coordinates (screen_x, screen_y)
        # X is horizontal, Y is vertical (inverted for screen coords), Z is depth
        screen_x = int(CENTER_X + rotated_pos[0] * HUMAN_SCALE)
        screen_y = int(CENTER_Y - rotated_pos[1] * HUMAN_SCALE) # Y-axis is inverted in Pygame (0 at top)

        projected_points_on_screen.append((screen_x, screen_y))

    # Draw all points as white circles
    for point_2d in projected_points_on_screen:
        pygame.draw.circle(screen, WHITE, point_2d, POINT_RADIUS)

    pygame.display.flip()  # Update the full display Surface to the screen
    clock.tick(FPS)        # Control the frame rate

pygame.quit()
