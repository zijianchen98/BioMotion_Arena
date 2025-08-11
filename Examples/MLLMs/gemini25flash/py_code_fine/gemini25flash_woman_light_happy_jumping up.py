
import pygame
import math
import sys

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
DOT_RADIUS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initial figure position (center of the Pelvis/Lower Torso)
# This serves as the dynamic origin for the entire figure's local coordinates.
FIGURE_CENTER_X = SCREEN_WIDTH // 2
FIGURE_CENTER_Y = SCREEN_HEIGHT * 3 // 4 # Start a bit lower on the screen

# --- Animation Parameters ---
JUMP_HEIGHT_AMPLITUDE = 80 # Max vertical displacement of the entire figure (in pixels)
JUMP_SPEED = 0.05         # Controls how fast the jump cycle progresses (radians per frame)
ARM_SWING_ANGLE_DEG = 60  # Max angle arms swing from neutral vertical position (degrees)
LEG_MAX_BEND_ANGLE_DEG = 70 # Max angle for knee bend from a straight leg position (degrees)
SQUAT_DEPTH_EFFECT = 15 # A base value for how much knees/ankles move up during squat (for simplified bending)

JUMP_CYCLE_LENGTH = 2 * math.pi # A full animation cycle (0 to 2*pi radians)

# --- Point Mapping (15 points) ---
# 0: Head
# 1: Left Shoulder
# 2: Right Shoulder
# 3: Left Elbow
# 4: Right Elbow
# 5: Left Wrist
# 6: Right Wrist
# 7: Neck/Upper Torso
# 8: Left Hip
# 9: Right Hip
# 10: Pelvis/Lower Torso (Reference point, effectively (0,0) in local figure space)
# 11: Left Knee
# 12: Right Knee
# 13: Left Ankle
# 14: Right Ankle

# --- Neutral Relative Coordinates ---
# All coordinates are relative to the Pelvis (point 10), which is considered (0,0) in the figure's local space.
# Y increases downwards in Pygame, so negative Y values represent points above the Pelvis.
NEUTRAL_RELATIVE_COORDS_DICT = {
    # Torso and Head
    0: (0, -150),  # Head
    7: (0, -100),  # Neck/Upper Torso
    10: (0, 0),    # Pelvis/Lower Torso (Origin)

    # Shoulders and Hips (fixed relative to torso)
    1: (-40, -90), # Left Shoulder
    2: (40, -90),  # Right Shoulder
    8: (-20, -10), # Left Hip
    9: (20, -10),  # Right Hip

    # Limbs - initial guess for neutral, will be adjusted dynamically
    # Arm segment lengths (approx): Shoulder-Elbow ~50, Elbow-Wrist ~50
    3: (-60, -40), # Left Elbow
    4: (60, -40),  # Right Elbow
    5: (-70, 10),  # Left Wrist
    6: (70, 10),   # Right Wrist

    # Leg segment lengths (approx): Hip-Knee ~60, Knee-Ankle ~50
    11: (-20, 50),  # Left Knee
    12: (20, 50),   # Right Knee
    13: (-20, 100), # Left Ankle
    14: (20, 100)   # Right Ankle
}

# Convert dict to a list for easier indexing
NEUTRAL_RELATIVE_COORDS = [NEUTRAL_RELATIVE_COORDS_DICT[i] for i in range(15)]

# Calculate segment lengths for arms/legs for rotation
# Using values from NEUTRAL_RELATIVE_COORDS_DICT for robustness
L_SHOULDER_POS = NEUTRAL_RELATIVE_COORDS_DICT[1]
L_ELBOW_POS_NEUTRAL = NEUTRAL_RELATIVE_COORDS_DICT[3]
L_WRIST_POS_NEUTRAL = NEUTRAL_RELATIVE_COORDS_DICT[5]

R_SHOULDER_POS = NEUTRAL_RELATIVE_COORDS_DICT[2]
R_ELBOW_POS_NEUTRAL = NEUTRAL_RELATIVE_COORDS_DICT[4]
R_WRIST_POS_NEUTRAL = NEUTRAL_RELATIVE_COORDS_DICT[6]

L_HIP_POS = NEUTRAL_RELATIVE_COORDS_DICT[8]
L_KNEE_POS_NEUTRAL = NEUTRAL_RELATIVE_COORDS_DICT[11]
L_ANKLE_POS_NEUTRAL = NEUTRAL_RELATIVE_COORDS_DICT[13]

HIP_KNEE_LEN = math.sqrt((L_KNEE_POS_NEUTRAL[0] - L_HIP_POS[0])**2 + (L_KNEE_POS_NEUTRAL[1] - L_HIP_POS[1])**2)
KNEE_ANKLE_LEN = math.sqrt((L_ANKLE_POS_NEUTRAL[0] - L_KNEE_POS_NEUTRAL[0])**2 + (L_ANKLE_POS_NEUTRAL[1] - L_KNEE_POS_NEUTRAL[1])**2)
SHOULDER_ELBOW_LEN = math.sqrt((L_ELBOW_POS_NEUTRAL[0] - L_SHOULDER_POS[0])**2 + (L_ELBOW_POS_NEUTRAL[1] - L_SHOULDER_POS[1])**2)
ELBOW_WRIST_LEN = math.sqrt((L_WRIST_POS_NEUTRAL[0] - L_ELBOW_POS_NEUTRAL[0])**2 + (L_WRIST_POS_NEUTRAL[1] - L_ELBOW_POS_NEUTRAL[1])**2)

# --- Helper Function ---
def rotate_point(px, py, ox, oy, theta_rad):
    """Rotates a point (px, py) around an origin (ox, oy) by an angle theta (in radians)."""
    s = math.sin(theta_rad)
    c = math.cos(theta_rad)
    # Translate point back to origin
    px_translated = px - ox
    py_translated = py - oy
    # Rotate point
    x_new = px_translated * c - py_translated * s
    y_new = px_translated * s + py_translated * c
    # Translate point back
    px_rotated = x_new + ox
    py_rotated = y_new + oy
    return px_rotated, py_rotated

# --- Animation Logic ---
def get_animated_coords(cycle_phase):
    """
    Calculates the current (x, y) coordinates for all 15 points based on the
    current phase of the jump cycle.
    """
    # Create a mutable copy of neutral relative coordinates for manipulation
    current_relative_coords = [list(p) for p in NEUTRAL_RELATIVE_COORDS]

    # 1. Overall vertical jump motion for the core body
    # jump_vertical_offset_factor: 0 (lowest point, start/end of jump) to 1 (highest point, peak of jump)
    # Uses a cosine wave: (0.5 - 0.5 * cos(cycle_phase)) ranges from 0 to 1 smoothly.
    jump_vertical_offset_factor = (0.5 - 0.5 * math.cos(cycle_phase))
    # main_y_offset: negative for upward movement in Pygame's y-coordinates
    main_y_offset = -JUMP_HEIGHT_AMPLITUDE * jump_vertical_offset_factor

    # 2. Arm swing
    ARM_SWING_ANGLE_RAD = math.radians(ARM_SWING_ANGLE_DEG)
    # arm_swing_factor: -1 (arms back, during squat) to +1 (arms up, at jump peak)
    # (0.5 - 0.5 * cos(cycle_phase)) * 2 - 1 ranges from -1 to 1.
    arm_swing_factor = (0.5 - 0.5 * math.cos(cycle_phase)) * 2 - 1
    arm_angle = ARM_SWING_ANGLE_RAD * arm_swing_factor

    # Left Arm: Shoulder (1) -> Elbow (3) -> Wrist (5)
    l_shoulder_rel_x, l_shoulder_rel_y = current_relative_coords[1]
    
    # Calculate elbow position relative to shoulder and rotate
    # Segment vector from shoulder to elbow
    elbow_from_shoulder_x = L_ELBOW_POS_NEUTRAL[0] - L_SHOULDER_POS[0]
    elbow_from_shoulder_y = L_ELBOW_POS_NEUTRAL[1] - L_SHOULDER_POS[1]
    rotated_l_elbow_x, rotated_l_elbow_y = rotate_point(
        elbow_from_shoulder_x, elbow_from_shoulder_y, 0, 0, arm_angle
    )
    current_relative_coords[3][0] = l_shoulder_rel_x + rotated_l_elbow_x
    current_relative_coords[3][1] = l_shoulder_rel_y + rotated_l_elbow_y

    # Calculate wrist position relative to elbow and rotate
    # Segment vector from elbow to wrist
    wrist_from_elbow_x = L_WRIST_POS_NEUTRAL[0] - L_ELBOW_POS_NEUTRAL[0]
    wrist_from_elbow_y = L_WRIST_POS_NEUTRAL[1] - L_ELBOW_POS_NEUTRAL[1]
    rotated_l_wrist_x, rotated_l_wrist_y = rotate_point(
        wrist_from_elbow_x, wrist_from_elbow_y, 0, 0, arm_angle
    )
    current_relative_coords[5][0] = current_relative_coords[3][0] + rotated_l_wrist_x
    current_relative_coords[5][1] = current_relative_coords[3][1] + rotated_l_wrist_y

    # Right Arm: Shoulder (2) -> Elbow (4) -> Wrist (6) (mirror angle for symmetry)
    r_shoulder_rel_x, r_shoulder_rel_y = current_relative_coords[2]
    
    elbow_from_shoulder_x = R_ELBOW_POS_NEUTRAL[0] - R_SHOULDER_POS[0]
    elbow_from_shoulder_y = R_ELBOW_POS_NEUTRAL[1] - R_SHOULDER_POS[1]
    rotated_r_elbow_x, rotated_r_elbow_y = rotate_point(
        elbow_from_shoulder_x, elbow_from_shoulder_y, 0, 0, -arm_angle # Mirror angle
    )
    current_relative_coords[4][0] = r_shoulder_rel_x + rotated_r_elbow_x
    current_relative_coords[4][1] = r_shoulder_rel_y + rotated_r_elbow_y

    wrist_from_elbow_x = R_WRIST_POS_NEUTRAL[0] - R_ELBOW_POS_NEUTRAL[0]
    wrist_from_elbow_y = R_WRIST_POS_NEUTRAL[1] - R_ELBOW_POS_NEUTRAL[1]
    rotated_r_wrist_x, rotated_r_wrist_y = rotate_point(
        wrist_from_elbow_x, wrist_from_elbow_y, 0, 0, -arm_angle # Mirror angle
    )
    current_relative_coords[6][0] = current_relative_coords[4][0] + rotated_r_wrist_x
    current_relative_coords[6][1] = current_relative_coords[4][1] + rotated_r_wrist_y

    # 3. Leg bending/extension
    # Legs bend most when the body is lowest (jump_vertical_offset_factor = 0).
    # Legs are most extended when the body is highest (jump_vertical_offset_factor = 1).
    # Use (1 - jump_vertical_offset_factor) for bend control: 1 (max bend) at 0, 0 (no bend) at 1.
    leg_bend_factor = (1 - jump_vertical_offset_factor)
    
    # Calculate knee and ankle positions relative to their parents (hip/knee)
    # A positive angle bends the leg "forward" (in Pygame coords, this is a combination of X and Y change)
    LEG_MAX_BEND_ANGLE_RAD = math.radians(LEG_MAX_BEND_ANGLE_DEG)
    current_knee_angle = LEG_MAX_BEND_ANGLE_RAD * leg_bend_factor

    # Left Leg: Hip (8) -> Knee (11) -> Ankle (13)
    l_hip_rel_x, l_hip_rel_y = current_relative_coords[8]
    
    # Knee position relative to hip, considering bend
    # The neutral segment vector is (0, HIP_KNEE_LEN) from hip to knee (y positive down)
    # Rotating by current_knee_angle: (HIP_KNEE_LEN * sin(-angle), HIP_KNEE_LEN * cos(-angle)) for left leg bending slightly inward
    # Using negative angle for left leg to push point slightly left (negative X) as it bends for natural look
    rotated_l_knee_x_from_hip = -HIP_KNEE_LEN * math.sin(current_knee_angle) # Negative x for knee moving "forward/inward"
    rotated_l_knee_y_from_hip = HIP_KNEE_LEN * math.cos(current_knee_angle)
    
    current_relative_coords[11][0] = l_hip_rel_x + rotated_l_knee_x_from_hip
    current_relative_coords[11][1] = l_hip_rel_y + rotated_l_knee_y_from_hip
    
    # Ankle position relative to knee, considering bend
    # Similar rotation for the lower leg segment
    rotated_l_ankle_x_from_knee = -KNEE_ANKLE_LEN * math.sin(current_knee_angle)
    rotated_l_ankle_y_from_knee = KNEE_ANKLE_LEN * math.cos(current_knee_angle)
    
    current_relative_coords[13][0] = current_relative_coords[11][0] + rotated_l_ankle_x_from_knee
    current_relative_coords[13][1] = current_relative_coords[11][1] + rotated_l_ankle_y_from_knee

    # Right Leg: Hip (9) -> Knee (12) -> Ankle (14) (mirror angle for symmetry)
    r_hip_rel_x, r_hip_rel_y = current_relative_coords[9]
    
    rotated_r_knee_x_from_hip = HIP_KNEE_LEN * math.sin(current_knee_angle) # Positive x for knee moving "forward/inward"
    rotated_r_knee_y_from_hip = HIP_KNEE_LEN * math.cos(current_knee_angle)
    
    current_relative_coords[12][0] = r_hip_rel_x + rotated_r_knee_x_from_hip
    current_relative_coords[12][1] = r_hip_rel_y + rotated_r_knee_y_from_hip
    
    rotated_r_ankle_x_from_knee = KNEE_ANKLE_LEN * math.sin(current_knee_angle)
    rotated_r_ankle_y_from_knee = KNEE_ANKLE_LEN * math.cos(current_knee_angle)
    
    current_relative_coords[14][0] = current_relative_coords[12][0] + rotated_r_ankle_x_from_knee
    current_relative_coords[14][1] = current_relative_coords[12][1] + rotated_r_ankle_y_from_knee

    # 4. Final conversion to screen coordinates
    final_coords = []
    # All points are currently relative to the Pelvis (point 10)'s neutral position (0,0).
    # We now translate the entire figure by the main_y_offset and position it on screen.
    for i in range(15):
        # Screen X = FIGURE_CENTER_X + relative_x
        # Screen Y = FIGURE_CENTER_Y + relative_y (from Pelvis) + overall_jump_vertical_offset
        final_coords.append((
            FIGURE_CENTER_X + current_relative_coords[i][0],
            FIGURE_CENTER_Y + current_relative_coords[i][1] + main_y_offset
        ))
    
    return final_coords

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion - Happy Woman Jumping")
clock = pygame.time.Clock()

# --- Main Animation Loop ---
current_jump_cycle = 0.0 # Tracks the phase of the jump cycle (from 0 to 2*pi)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Allow Esc to quit
                running = False

    screen.fill(BLACK) # Clear screen with black background

    # Update animation phase for the next frame
    current_jump_cycle = (current_jump_cycle + JUMP_SPEED) % JUMP_CYCLE_LENGTH

    # Get the calculated positions of all 15 points
    animated_points = get_animated_coords(current_jump_cycle)

    # Draw each point as a white circle
    for point_x, point_y in animated_points:
        pygame.draw.circle(screen, WHITE, (int(point_x), int(point_y)), DOT_RADIUS)

    pygame.display.flip() # Update the display to show the new frame
    clock.tick(FPS) # Control the frame rate

# --- Cleanup ---
pygame.quit()
sys.exit()
