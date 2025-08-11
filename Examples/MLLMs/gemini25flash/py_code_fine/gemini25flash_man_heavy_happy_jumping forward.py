
import pygame
import math
import numpy as np

# --- Configuration ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
POINT_RADIUS = 5
POINT_COLOR = (255, 255, 255)  # White
BACKGROUND_COLOR = (0, 0, 0)  # Black

# --- Animation Parameters for "Heavy Jump Forward" ---
JUMP_DURATION = 1.8  # seconds for one full jump cycle (slightly longer for "heavy weight")
HORIZONTAL_JUMP_DISTANCE = 350  # Pixels moved horizontally during one jump
CROUCH_DEPTH = 70  # How much the pelvis drops during initial crouch
VERTICAL_JUMP_HEIGHT = 180  # Pixels pelvis rises from initial standing to peak jump height

# Define key Y positions for the pelvis (relative to its standing height of 0)
# These are used to calculate the overall vertical movement of the figure.
Y_PELVIS_REST = 0
Y_PELVIS_CROUCH = CROUCH_DEPTH
Y_PELVIS_PEAK = -VERTICAL_JUMP_HEIGHT  # Negative because Pygame Y increases downwards
Y_PELVIS_LAND = CROUCH_DEPTH * 1.5  # Deeper landing crouch for "heavy weight" feel

# Initial screen position for the figure's reference point (pelvis)
# The figure starts at the left quarter of the screen and moves right.
# INITIAL_Y_SCREEN represents the Y-coordinate of the pelvis when standing.
INITIAL_X_SCREEN = SCREEN_WIDTH / 4
INITIAL_Y_SCREEN = SCREEN_HEIGHT * 0.7  # Sets the 'ground' level for the feet approx.

# --- Initial Relative Positions of 15 Body Points ---
# These coordinates are relative to the Pelvis point (index 8), which is (0,0)
# in this relative system. Y-coordinates are positive downwards, mirroring Pygame.
# These values are chosen to approximate a human figure as seen in the example image.
# Index mapping:
# 0: Head, 1: Neck, 2: Right Shoulder, 3: Left Shoulder, 4: Right Elbow, 5: Left Elbow,
# 6: Right Wrist, 7: Left Wrist, 8: Pelvis (mid-torso), 9: Right Hip, 10: Left Hip,
# 11: Right Knee, 12: Left Knee, 13: Right Ankle, 14: Left Ankle
INITIAL_RELATIVE_POSITIONS = np.array([
    (0.0, -120.0), # 0: Head
    (0.0, -80.0),  # 1: Neck
    (30.0, -70.0), # 2: R Shoulder
    (-30.0, -70.0),# 3: L Shoulder
    (40.0, -20.0), # 4: R Elbow
    (-40.0, -20.0),# 5: L Elbow
    (45.0, 30.0),  # 6: R Wrist
    (-45.0, 30.0), # 7: L Wrist
    (0.0, 0.0),    # 8: Pelvis (reference point)
    (20.0, 0.0),   # 9: R Hip
    (-20.0, 0.0),  # 10: L Hip
    (20.0, 80.0),  # 11: R Knee
    (-20.0, 80.0), # 12: L Knee
    (20.0, 160.0), # 13: R Ankle
    (-20.0, 160.0) # 14: L Ankle
])

# --- Animation Phase Percentages (of total JUMP_DURATION) ---
PHASE_CROUCH_END_PCT = 0.2
PHASE_PUSH_OFF_END_PCT = 0.4
PHASE_AIRBORNE_END_PCT = 0.6
PHASE_LANDING_END_PCT = 0.8
PHASE_RECOVERY_END_PCT = 1.0

# --- Easing Function ---
def ease_in_out_sine(t):
    """
    Smoothly interpolates a value from 0 to 1 over a given time 't' (also 0 to 1).
    Uses a sine curve for natural acceleration and deceleration.
    """
    return 0.5 * (1 - math.cos(math.pi * t))

# --- Main Pose Calculation Function ---
def get_current_pose(time_in_cycle):
    """
    Calculates the screen coordinates for all 15 points based on the current
    normalized time (0 to 1) within the jump cycle.
    """
    # Start with a copy of the initial relative positions
    current_relative_positions = np.copy(INITIAL_RELATIVE_POSITIONS)

    # --- 1. Overall Body Movement (Pelvis reference point) ---
    # Horizontal movement: progresses linearly across the screen
    current_x_offset = time_in_cycle * HORIZONTAL_JUMP_DISTANCE

    # Vertical movement for pelvis: follows the jump arc based on phases
    pelvis_y_offset = 0 # This offset is relative to Y_PELVIS_REST (0)

    if 0.0 <= time_in_cycle < PHASE_CROUCH_END_PCT:
        # Crouch phase: pelvis moves from REST (0) down to CROUCH_DEPTH
        t = (time_in_cycle - 0.0) / (PHASE_CROUCH_END_PCT - 0.0)
        pelvis_y_offset = ease_in_out_sine(t) * Y_PELVIS_CROUCH
    elif PHASE_CROUCH_END_PCT <= time_in_cycle < PHASE_PUSH_OFF_END_PCT:
        # Push-off phase: pelvis moves from CROUCH_DEPTH up to PEAK height
        t = (time_in_cycle - PHASE_CROUCH_END_PCT) / (PHASE_PUSH_OFF_END_PCT - PHASE_CROUCH_END_PCT)
        pelvis_y_offset = Y_PELVIS_CROUCH + (ease_in_out_sine(t) * (Y_PELVIS_PEAK - Y_PELVIS_CROUCH))
    elif PHASE_PUSH_OFF_END_PCT <= time_in_cycle < PHASE_AIRBORNE_END_PCT:
        # Airborne phase (rising to slight fall): remains at peak or slightly drops
        # A small linear drop to simulate gravity's effect before the main descent
        t = (time_in_cycle - PHASE_PUSH_OFF_END_PCT) / (PHASE_AIRBORNE_END_PCT - PHASE_PUSH_OFF_END_PCT)
        pelvis_y_offset = Y_PELVIS_PEAK + (t * (Y_PELVIS_LAND * 0.1)) 
    elif PHASE_AIRBORNE_END_PCT <= time_in_cycle < PHASE_LANDING_END_PCT:
        # Landing phase: pelvis moves from mid-air descent down to deep landing crouch
        t = (time_in_cycle - PHASE_AIRBORNE_END_PCT) / (PHASE_LANDING_END_PCT - PHASE_AIRBORNE_END_PCT)
        # Starting point for this phase: Y_PELVIS_PEAK + Y_PELVIS_LAND * 0.1 (from previous phase's end)
        start_y = Y_PELVIS_PEAK + (Y_PELVIS_LAND * 0.1)
        pelvis_y_offset = start_y + (ease_in_out_sine(t) * (Y_PELVIS_LAND - start_y))
    else: # Recovery phase (PHASE_LANDING_END_PCT to PHASE_RECOVERY_END_PCT)
        # Recovery: pelvis moves from deep landing crouch back to REST (0)
        t = (time_in_cycle - PHASE_LANDING_END_PCT) / (PHASE_RECOVERY_END_PCT - PHASE_LANDING_END_PCT)
        pelvis_y_offset = Y_PELVIS_LAND - (ease_in_out_sine(t) * Y_PELVIS_LAND)
    
    # Calculate global screen position for the pelvis
    figure_x = INITIAL_X_SCREEN + current_x_offset
    figure_y = INITIAL_Y_SCREEN + pelvis_y_offset

    # --- 2. Joint-specific movements (relative to Pelvis) ---
    # These adjustments modify the points' positions relative to the pelvis,
    # simulating limb movements during the jump.
    
    # Legs (knees and ankles) bending and extending
    leg_bend_factor = 0 # 0 for straight, 1 for max bend
    if 0.0 <= time_in_cycle < PHASE_CROUCH_END_PCT:
        t = (time_in_cycle - 0.0) / (PHASE_CROUCH_END_PCT - 0.0)
        leg_bend_factor = ease_in_out_sine(t) # Bend deeply during crouch
    elif PHASE_CROUCH_END_PCT <= time_in_cycle < PHASE_PUSH_OFF_END_PCT:
        t = (time_in_cycle - PHASE_CROUCH_END_PCT) / (PHASE_PUSH_OFF_END_PCT - PHASE_CROUCH_END_PCT)
        leg_bend_factor = 1 - ease_in_out_sine(t) # Straighten for powerful push-off
    elif PHASE_PUSH_OFF_END_PCT <= time_in_cycle < PHASE_AIRBORNE_END_PCT:
        t = (time_in_cycle - PHASE_PUSH_OFF_END_PCT) / (PHASE_AIRBORNE_END_PCT - PHASE_PUSH_OFF_END_PCT)
        leg_bend_factor = ease_in_out_sine(t) * 0.4 # Slight tuck in air
    elif PHASE_AIRBORNE_END_PCT <= time_in_cycle < PHASE_LANDING_END_PCT:
        t = (time_in_cycle - PHASE_AIRBORNE_END_PCT) / (PHASE_LANDING_END_PCT - PHASE_AIRBORNE_END_PCT)
        leg_bend_factor = 0.4 + ease_in_out_sine(t) * 0.6 # Extend for landing, then absorb impact
    else: # Recovery
        t = (time_in_cycle - PHASE_LANDING_END_PCT) / (PHASE_RECOVERY_END_PCT - PHASE_LANDING_END_PCT)
        leg_bend_factor = 1 - ease_in_out_sine(t) # Return to straight standing position

    # Max pixel displacement for knee and ankle points due to bending
    KNEE_MAX_BEND_Y = 50
    KNEE_MAX_BEND_X = 20  # Knees move slightly forward when bending
    ANKLE_MAX_BEND_Y = 50  # Ankles move more vertically relative to knees
    ANKLE_MAX_BEND_X = 30  # Ankles move further forward

    # Apply leg bend adjustments to relative positions
    current_relative_positions[11, 1] += KNEE_MAX_BEND_Y * leg_bend_factor # R Knee Y
    current_relative_positions[12, 1] += KNEE_MAX_BEND_Y * leg_bend_factor # L Knee Y
    current_relative_positions[11, 0] += KNEE_MAX_BEND_X * leg_bend_factor # R Knee X (forward)
    current_relative_positions[12, 0] -= KNEE_MAX_BEND_X * leg_bend_factor # L Knee X (forward)
    
    current_relative_positions[13, 1] += (KNEE_MAX_BEND_Y + ANKLE_MAX_BEND_Y) * leg_bend_factor # R Ankle Y
    current_relative_positions[14, 1] += (KNEE_MAX_BEND_Y + ANKLE_MAX_BEND_Y) * leg_bend_factor # L Ankle Y
    current_relative_positions[13, 0] += ANKLE_MAX_BEND_X * leg_bend_factor # R Ankle X
    current_relative_positions[14, 0] -= ANKLE_MAX_BEND_X * leg_bend_factor # L Ankle X

    # Arms swinging for momentum
    arm_swing_factor = 0 # 0 for arms down, 1 for max swing forward/up, negative for backswing
    if 0.0 <= time_in_cycle < PHASE_CROUCH_END_PCT:
        t = (time_in_cycle - 0.0) / (PHASE_CROUCH_END_PCT - 0.0)
        arm_swing_factor = ease_in_out_sine(t) * -0.3 # Arms pull back slightly (backswing)
    elif PHASE_CROUCH_END_PCT <= time_in_cycle < PHASE_PUSH_OFF_END_PCT:
        t = (time_in_cycle - PHASE_CROUCH_END_PCT) / (PHASE_PUSH_OFF_END_PCT - PHASE_CROUCH_END_PCT)
        arm_swing_factor = -0.3 + ease_in_out_sine(t) * 1.3 # Arms swing powerfully forward
    elif PHASE_PUSH_OFF_END_PCT <= time_in_cycle < PHASE_AIRBORNE_END_PCT:
        t = (time_in_cycle - PHASE_PUSH_OFF_END_PCT) / (PHASE_AIRBORNE_END_PCT - PHASE_PUSH_OFF_END_PCT)
        arm_swing_factor = 1.0 - ease_in_out_sine(t) * 0.4 # Arms slightly retract/lower
    elif PHASE_AIRBORNE_END_PCT <= time_in_cycle < PHASE_LANDING_END_PCT:
        t = (time_in_cycle - PHASE_AIRBORNE_END_PCT) / (PHASE_LANDING_END_PCT - PHASE_AIRBORNE_END_PCT)
        arm_swing_factor = 0.6 - ease_in_out_sine(t) * 0.6 # Arms drop for balance
    else: # Recovery
        t = (time_in_cycle - PHASE_LANDING_END_PCT) / (PHASE_RECOVERY_END_PCT - PHASE_LANDING_END_PCT)
        arm_swing_factor = 0.0 + ease_in_out_sine(t) * 0.1 # Slight sway before returning to neutral

    ARM_X_MAX_SWING = 50
    ARM_Y_MAX_SWING = 40

    # Apply arm swing adjustments to relative positions (symmetrical)
    for i in [4, 6]: # Right Elbow, Right Wrist
        current_relative_positions[i, 0] += ARM_X_MAX_SWING * (1.0 + (i==6)*0.2) * arm_swing_factor
        current_relative_positions[i, 1] -= ARM_Y_MAX_SWING * (1.0 + (i==6)*0.2) * arm_swing_factor
    for i in [5, 7]: # Left Elbow, Left Wrist
        current_relative_positions[i, 0] -= ARM_X_MAX_SWING * (1.0 + (i==7)*0.2) * arm_swing_factor
        current_relative_positions[i, 1] -= ARM_Y_MAX_SWING * (1.0 + (i==7)*0.2) * arm_swing_factor

    # Head and Neck: slight forward lean for momentum
    HEAD_MAX_LEAN_X = 15
    NECK_MAX_LEAN_X = 10
    head_lean_factor = 0
    if 0.0 <= time_in_cycle < PHASE_PUSH_OFF_END_PCT:
        t = time_in_cycle / PHASE_PUSH_OFF_END_PCT
        head_lean_factor = ease_in_out_sine(t) # Lean forward during crouch and push-off
    elif PHASE_PUSH_OFF_END_PCT <= time_in_cycle < PHASE_LANDING_END_PCT:
        t = (time_in_cycle - PHASE_PUSH_OFF_END_PCT) / (PHASE_LANDING_END_PCT - PHASE_PUSH_OFF_END_PCT)
        head_lean_factor = 1.0 - ease_in_out_sine(t) # Straighten during airborne and landing
    else: # Recovery
        head_lean_factor = 0 # Return to neutral
    
    current_relative_positions[0, 0] += HEAD_MAX_LEAN_X * head_lean_factor # Head X
    current_relative_positions[1, 0] += NECK_MAX_LEAN_X * head_lean_factor # Neck X

    # --- 3. Final Global Translation ---
    # Translate all points by the calculated global figure position (pelvis as reference)
    final_positions = np.array([
        (figure_x + pos[0], figure_y + pos[1])
        for pos in current_relative_positions
    ])
    
    return final_positions

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Heavy Jump Forward")
clock = pygame.time.Clock()

# --- Main Animation Loop ---
running = True
current_time = 0.0 # Time in seconds within the jump cycle (will loop from 0 to JUMP_DURATION)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Allow ESC to quit
                running = False

    screen.fill(BACKGROUND_COLOR)

    # Update animation time based on delta time (time since last frame)
    # The modulo operator ensures 'current_time' loops seamlessly within JUMP_DURATION.
    dt = clock.tick(FPS) / 1000.0 # delta time in seconds
    current_time = (current_time + dt) % JUMP_DURATION

    # Calculate the normalized time (0 to 1) for the current point in the cycle
    time_in_cycle = current_time / JUMP_DURATION
    
    # Get the coordinates for all points for the current frame
    points_coords = get_current_pose(time_in_cycle)

    # Draw each point as a white circle
    for x, y in points_coords:
        pygame.draw.circle(screen, POINT_COLOR, (int(x), int(y)), POINT_RADIUS)

    # Update the display
    pygame.display.flip()

pygame.quit()
