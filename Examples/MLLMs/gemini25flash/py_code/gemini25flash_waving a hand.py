
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Waving Hand")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point properties
POINT_RADIUS = 5

# Frame rate
FPS = 60

# --- Biomechanical Model Parameters ---
# These values define the relative proportions of the human figure.
# They are unitless and will be scaled to screen pixels.
HEAD_SIZE = 0.08        # Approximate radius/half-height of head
NECK_LENGTH = 0.05      # Length from spine top to head base
TORSO_LENGTH = 0.25     # Length from pelvis to spine top
PELVIS_WIDTH = 0.15     # Width of hips
SHOULDER_WIDTH = 0.2    # Width of shoulders

UPPER_ARM_LENGTH = 0.18 # Length of upper arm segment
FOREARM_LENGTH = 0.17   # Length of forearm segment (including hand)

THIGH_LENGTH = 0.2      # Length of thigh segment
SHIN_LENGTH = 0.2       # Length of shin segment (including foot)

# Estimate total relative height for scaling purposes
TOTAL_RELATIVE_HEIGHT_ESTIMATE = HEAD_SIZE + NECK_LENGTH + TORSO_LENGTH + THIGH_LENGTH + SHIN_LENGTH

# Scaling factor to convert relative proportions to screen pixels
# Multiplier (1.3) provides padding around the figure
SCALE_FACTOR = SCREEN_HEIGHT / (TOTAL_RELATIVE_HEIGHT_ESTIMATE * 1.3)

# Base position for the figure (center of pelvis) on the screen.
# Adjusted to position the figure roughly in the middle, with feet near the bottom.
BASE_X = SCREEN_WIDTH // 2
BASE_Y = SCREEN_HEIGHT * 0.4 # Pelvis Y-coordinate

# --- Joint Definitions (symbolic names mapped to their indices) ---
# This dictionary defines the 15 specific points for the point-light display.
# The order corresponds to common biomechanical models.
POINT_NAMES_MAP = {
    "head": 0, "neck": 1, "l_shoulder": 2, "r_shoulder": 3, "spine": 4,
    "l_elbow": 5, "r_elbow": 6, "l_wrist": 7, "r_wrist": 8,
    "l_hip": 9, "r_hip": 10, "l_knee": 11, "r_knee": 12, "l_ankle": 13, "r_ankle": 14
}
NUM_POINTS = len(POINT_NAMES_MAP)
# Initialize a list to store the current [x, y] positions of all points
current_point_positions = [[0, 0] for _ in range(NUM_POINTS)]

# --- Animation State Variables ---
time_counter = 0.0 # Time counter for sinusoidal animations

# Animation speeds (multipliers for time_counter)
WAVE_FREQ = 5.0      # Frequency of the main waving motion
BREATHING_FREQ = 1.5 # Frequency of subtle breathing motion
HEAD_BOB_FREQ = 2.0  # Frequency of subtle head bobbing

# --- Animation Loop ---
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK) # Clear the screen with black background

    # Update animation time based on frame rate
    time_counter += 1.0 / FPS

    # Calculate subtle body movements for realism
    breathing_offset_y = math.sin(time_counter * BREATHING_FREQ) * (2 * SCALE_FACTOR / 100) # Vertical breathing
    head_bob_offset_y = math.sin(time_counter * HEAD_BOB_FREQ * 0.8) * (1 * SCALE_FACTOR / 100) # Head bobbing

    # --- Calculate Joint Positions ---
    # All positions are calculated relative to the `BASE_X`, `BASE_Y` (pelvis center)
    # and then scaled to screen pixel values.

    # 1. Pelvis (implicit origin for hips)
    pelvis_x = BASE_X
    pelvis_y = BASE_Y + breathing_offset_y

    # 2. Hips (relative to pelvis)
    current_point_positions[POINT_NAMES_MAP["l_hip"]] = [pelvis_x - (PELVIS_WIDTH / 2) * SCALE_FACTOR, pelvis_y]
    current_point_positions[POINT_NAMES_MAP["r_hip"]] = [pelvis_x + (PELVIS_WIDTH / 2) * SCALE_FACTOR, pelvis_y]

    # 3. Legs (static, straight down from hips for a standing pose)
    # Left Leg
    lh_x, lh_y = current_point_positions[POINT_NAMES_MAP["l_hip"]]
    lk_x = lh_x
    lk_y = lh_y + THIGH_LENGTH * SCALE_FACTOR
    current_point_positions[POINT_NAMES_MAP["l_knee"]] = [lk_x, lk_y]
    la_x = lk_x
    la_y = lk_y + SHIN_LENGTH * SCALE_FACTOR
    current_point_positions[POINT_NAMES_MAP["l_ankle"]] = [la_x, la_y]

    # Right Leg
    rh_x, rh_y = current_point_positions[POINT_NAMES_MAP["r_hip"]]
    rk_x = rh_x
    rk_y = rh_y + THIGH_LENGTH * SCALE_FACTOR
    current_point_positions[POINT_NAMES_MAP["r_knee"]] = [rk_x, rk_y]
    ra_x = rk_x
    ra_y = rk_y + SHIN_LENGTH * SCALE_FACTOR
    current_point_positions[POINT_NAMES_MAP["r_ankle"]] = [ra_x, ra_y]

    # 4. Spine (mid-torso point)
    spine_x = pelvis_x
    spine_y = pelvis_y - TORSO_LENGTH * SCALE_FACTOR
    current_point_positions[POINT_NAMES_MAP["spine"]] = [spine_x, spine_y]

    # 5. Neck
    neck_x = spine_x
    neck_y = spine_y - NECK_LENGTH * SCALE_FACTOR
    current_point_positions[POINT_NAMES_MAP["neck"]] = [neck_x, neck_y]

    # 6. Head
    head_x = neck_x
    head_y = neck_y - HEAD_SIZE * SCALE_FACTOR / 2 + head_bob_offset_y # Apply head bob
    current_point_positions[POINT_NAMES_MAP["head"]] = [head_x, head_y]

    # 7. Shoulders (relative to neck, slightly outward and down)
    sh_y_offset = NECK_LENGTH * 0.5 * SCALE_FACTOR # Shoulders slightly below neck joint
    current_point_positions[POINT_NAMES_MAP["l_shoulder"]] = [neck_x - (SHOULDER_WIDTH / 2) * SCALE_FACTOR, neck_y + sh_y_offset]
    current_point_positions[POINT_NAMES_MAP["r_shoulder"]] = [neck_x + (SHOULDER_WIDTH / 2) * SCALE_FACTOR, neck_y + sh_y_offset]

    # 8. Arms - Left Arm (static, natural hanging pose)
    ls_x, ls_y = current_point_positions[POINT_NAMES_MAP["l_shoulder"]]
    l_ua_len = UPPER_ARM_LENGTH * SCALE_FACTOR
    l_fa_len = FOREARM_LENGTH * SCALE_FACTOR

    # Angles for left arm (slightly bent, hanging downwards).
    # Angles are measured from the positive X-axis, clockwise.
    # math.pi / 2 is straight down.
    l_shoulder_angle = math.pi * 0.45 # Arm hanging slightly forward
    l_elbow_angle = math.pi * 0.1     # Elbow slightly bent (relative to upper arm segment)

    # Calculate Left Elbow position
    le_x = ls_x + l_ua_len * math.cos(l_shoulder_angle)
    le_y = ls_y + l_ua_len * math.sin(l_shoulder_angle)
    current_point_positions[POINT_NAMES_MAP["l_elbow"]] = [le_x, le_y]

    # Calculate Left Wrist position
    lw_x = le_x + l_fa_len * math.cos(l_shoulder_angle + l_elbow_angle)
    lw_y = le_y + l_fa_len * math.sin(l_shoulder_angle + l_elbow_angle)
    current_point_positions[POINT_NAMES_MAP["l_wrist"]] = [lw_x, lw_y]

    # 9. Arms - Right Arm (Waving Motion)
    rs_x, rs_y = current_point_positions[POINT_NAMES_MAP["r_shoulder"]]
    r_ua_len = UPPER_ARM_LENGTH * SCALE_FACTOR
    r_fa_len = FOREARM_LENGTH * SCALE_FACTOR

    # Base angles for the waving arm (raised, slightly forward).
    # These define the general position of the arm before the wave motion starts.
    # Angle from positive X-axis, clockwise.
    BASE_R_SHOULDER_ANGLE = math.radians(-120) # Arm points slightly up and forward
    BASE_R_ELBOW_ANGLE = math.radians(30)      # Elbow slightly bent

    # Wave parameters (amplitudes of oscillation)
    WAVE_AMP_SHOULDER = math.radians(10) # Small swing at shoulder (flexion/extension)
    WAVE_AMP_ELBOW = math.radians(30)    # Larger swing at elbow (flexion/extension), for the main wave action

    # Oscillating value derived from sine wave, for smooth back-and-forth motion
    wave_value = math.sin(time_counter * WAVE_FREQ)

    # Apply oscillation to angles to create the wave effect
    r_shoulder_angle = BASE_R_SHOULDER_ANGLE + wave_value * WAVE_AMP_SHOULDER
    r_elbow_angle = BASE_R_ELBOW_ANGLE + wave_value * WAVE_AMP_ELBOW

    # Calculate Right Elbow position (based on shoulder position and arm angle)
    re_x = rs_x + r_ua_len * math.cos(r_shoulder_angle)
    re_y = rs_y + r_ua_len * math.sin(r_shoulder_angle)
    current_point_positions[POINT_NAMES_MAP["r_elbow"]] = [re_x, re_y]

    # Calculate Right Wrist position (based on elbow position and relative elbow angle)
    rw_x = re_x + r_fa_len * math.cos(r_shoulder_angle + r_elbow_angle)
    rw_y = re_y + r_fa_len * math.sin(r_shoulder_angle + r_elbow_angle)
    current_point_positions[POINT_NAMES_MAP["r_wrist"]] = [rw_x, rw_y]

    # --- Draw the 15 Points ---
    for i in range(NUM_POINTS):
        x, y = current_point_positions[i]
        # Ensure coordinates are integers for drawing
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

    pygame.display.flip() # Update the full display Surface to the screen

    clock.tick(FPS) # Control the frame rate

pygame.quit() # Uninitialize pygame modules
sys.exit() # Exit the program
