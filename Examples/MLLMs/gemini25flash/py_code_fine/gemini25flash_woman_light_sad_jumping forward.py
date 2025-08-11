
import pygame
import math

# --- Configuration ---
WIDTH, HEIGHT = 800, 600
FPS = 60
DOT_RADIUS = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Joint Definitions ---
# Order of joints for consistent indexing
JOINT_NAMES = [
    "Head", "Neck",
    "RShoulder", "LShoulder",
    "RElbow", "LElbow",
    "RWrist", "LWrist",
    "Pelvis",
    "RHip", "LHip",
    "RKnee", "LKnee",
    "RAnkle", "LAnkle"
]
JOINT_INDICES = {name: i for i, name in enumerate(JOINT_NAMES)}
NUM_JOINTS = len(JOINT_NAMES) # Should be 15

# Initial (standing) relative offsets from Pelvis (P_x, P_y)
# (x, y) where x is right/left from center, y is down from center
# Pelvis is (0,0) as reference point for these relative offsets
initial_relative_coords = [None] * NUM_JOINTS
initial_relative_coords[JOINT_INDICES["Head"]]      = (0, -60)
initial_relative_coords[JOINT_INDICES["Neck"]]      = (0, -45)
initial_relative_coords[JOINT_INDICES["RShoulder"]] = (15, -40)
initial_relative_coords[JOINT_INDICES["LShoulder"]] = (-15, -40)
initial_relative_coords[JOINT_INDICES["RElbow"]]    = (20, -10)
initial_relative_coords[JOINT_INDICES["LElbow"]]    = (-20, -10)
initial_relative_coords[JOINT_INDICES["RWrist"]]    = (25, 20)
initial_relative_coords[JOINT_INDICES["LWrist"]]    = (-25, 20)
initial_relative_coords[JOINT_INDICES["Pelvis"]]    = (0, 0) # Reference point
initial_relative_coords[JOINT_INDICES["RHip"]]      = (10, 10)
initial_relative_coords[JOINT_INDICES["LHip"]]      = (-10, 10)
initial_relative_coords[JOINT_INDICES["RKnee"]]     = (10, 40)
initial_relative_coords[JOINT_INDICES["LKnee"]]     = (-10, 40)
initial_relative_coords[JOINT_INDICES["RAnkle"]]    = (10, 70)
initial_relative_coords[JOINT_INDICES["LAnkle"]]    = (-10, 70)

# --- Animation Parameters ---
JUMP_CYCLE_DURATION = 1.8 # seconds for one full jump cycle
TOTAL_ANIMATION_FRAMES = int(JUMP_CYCLE_DURATION * FPS)

# Phase durations (as a fraction of TOTAL_ANIMATION_FRAMES)
# Total fractions should sum to 1.0
PHASES = {
    "crouch":     0.25, # Preparing to jump (down)
    "push_off":   0.15, # Accelerating up and forward
    "flight":     0.40, # In the air
    "landing":    0.10, # Absorbing impact
    "recovery":   0.10  # Back to standing
}

# Define normalized times for key Y and X states of the pelvis
t_crouch_end = PHASES["crouch"]
t_takeoff_start = t_crouch_end
t_push_off_end = PHASES["crouch"] + PHASES["push_off"]
t_flight_end = PHASES["crouch"] + PHASES["push_off"] + PHASES["flight"]
t_landing_start = t_flight_end
t_landing_end = t_landing_start + PHASES["landing"]
t_recovery_end = 1.0 # Ensures full cycle ends at 1.0

# Define key Y values for pelvis relative to standing (positive means lower on screen)
y_stand = 0
y_crouch = 50 # Depth of crouch
y_peak = -80 # Height of jump peak (negative because Y decreases upwards in Pygame)
y_landing_absorb = 20 # Depth of landing absorption

# Define time point for the peak of the Y trajectory (roughly halfway through airborne phase)
t_peak_flight = t_takeoff_start + (t_landing_start - t_takeoff_start) / 2

# Jump specific parameters for overall character position
PELVIS_START_Y = HEIGHT - 150 # Starting Y position for the pelvis (ground level reference)
PELVIS_OFFSET_X = WIDTH // 4 # Starting X position for the pelvis (relative to left edge)
JUMP_DISTANCE = 150 # Total horizontal distance covered in one jump cycle

# Parameters for "sadwoman with light weight" modifiers
HEAD_BOW_AMOUNT = 8 # How much the head bows down during jump
ARM_SWING_FACTOR = 0.6 # Factor to reduce arm swing (1.0 is full swing, 0.0 is no swing)
LEG_BEND_FACTOR = 1.0 # Factor for knee/ankle bend (1.0 is normal)

# Easing functions
def ease_in_out_quad(t):
    # Quadratic easing, accelerates then decelerates
    if t < 0.5:
        return 2 * t * t
    return -2 * t * t + 4 * t - 1

def ease_out_quad(t):
    # Quadratic easing, decelerates
    return t * (2 - t)

def lerp(a, b, t):
    # Linear interpolation
    return a + (b - a) * t

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sadwoman Jumping Forward")
clock = pygame.time.Clock()

# --- Animation State ---
current_frame = 0

def get_joint_positions(frame):
    t_norm = frame / TOTAL_ANIMATION_FRAMES # Normalized time for the entire cycle [0, 1]

    # --- 1. Pelvis (Root) Motion ---
    pelvis_x_offset = 0
    pelvis_y_offset = 0

    # Horizontal motion of the pelvis
    if t_norm >= t_takeoff_start and t_norm < t_landing_start:
        t_horizontal_phase = (t_norm - t_takeoff_start) / (t_landing_start - t_takeoff_start)
        pelvis_x_offset = lerp(0, JUMP_DISTANCE, ease_out_quad(t_horizontal_phase))
    elif t_norm >= t_landing_start: # After landing, stay at the end X position
        pelvis_x_offset = JUMP_DISTANCE
    # Before takeoff, pelvis_x_offset remains 0

    # Vertical motion of the pelvis using piecewise interpolation
    if t_norm <= t_crouch_end:
        # Crouch: From y_stand to y_crouch
        t = t_norm / t_crouch_end
        pelvis_y_offset = lerp(y_stand, y_crouch, ease_in_out_quad(t))
    elif t_norm <= t_peak_flight:
        # Ascent to peak: From y_crouch to y_peak
        t = (t_norm - t_crouch_end) / (t_peak_flight - t_crouch_end)
        pelvis_y_offset = lerp(y_crouch, y_peak, ease_out_quad(t)) # Accelerate up then decelerate
    elif t_norm <= t_landing_start:
        # Descent from peak to landing (back to y_stand)
        t = (t_norm - t_peak_flight) / (t_landing_start - t_peak_flight)
        pelvis_y_offset = lerp(y_peak, y_stand, ease_in_out_quad(t))
    elif t_norm <= t_landing_end:
        # Landing absorption: From y_stand to y_landing_absorb
        t = (t_norm - t_landing_start) / (t_landing_end - t_landing_start)
        pelvis_y_offset = lerp(y_stand, y_landing_absorb, ease_out_quad(t))
    else: # Recovery: From y_landing_absorb to y_stand
        t = (t_norm - t_landing_end) / (t_recovery_end - t_landing_end)
        pelvis_y_offset = lerp(y_landing_absorb, y_stand, ease_in_out_quad(t))

    pelvis_global_x = PELVIS_OFFSET_X + pelvis_x_offset
    pelvis_global_y = PELVIS_START_Y + pelvis_y_offset

    current_positions = [None] * NUM_JOINTS
    current_positions[JOINT_INDICES["Pelvis"]] = (pelvis_global_x, pelvis_global_y)

    # --- 2. Relative Joint Motion (Limb Poses) ---
    current_relative_offsets = list(initial_relative_coords) # Start with standing pose offsets

    # Define common deltas from initial_relative_coords for various limb states
    # Legs (Knee, Ankle Y offsets)
    delta_y_crouch_knee = 30 * LEG_BEND_FACTOR
    delta_y_crouch_ankle = 40 * LEG_BEND_FACTOR
    delta_y_flight_knee = 10 * LEG_BEND_FACTOR # Tucked
    delta_y_flight_ankle = 15 * LEG_BEND_FACTOR
    delta_y_landing_knee = 25 * LEG_BEND_FACTOR
    delta_y_landing_ankle = 35 * LEG_BEND_FACTOR

    # Arms (Elbow, Wrist X/Y offsets - magnitude for right arm, inverted for left)
    delta_x_arm_back = 10 * ARM_SWING_FACTOR
    delta_x_arm_forward = 10 * ARM_SWING_FACTOR
    delta_y_arm_up = 10 * ARM_SWING_FACTOR
    delta_x_arm_out = 10 * ARM_SWING_FACTOR

    # Head (Y offset)
    delta_y_head_bow = HEAD_BOW_AMOUNT

    # Calculate interpolation factor based on t_norm for limb poses
    if t_norm <= t_crouch_end:
        t_phase = t_norm / t_crouch_end
        for i in range(NUM_JOINTS):
            if i == JOINT_INDICES["Pelvis"]: continue
            dx0, dy0 = initial_relative_coords[i]
            
            target_dx, target_dy = 0, 0
            if i in [JOINT_INDICES["RKnee"], JOINT_INDICES["LKnee"]]: target_dy = delta_y_crouch_knee
            elif i in [JOINT_INDICES["RAnkle"], JOINT_INDICES["LAnkle"]]: target_dy = delta_y_crouch_ankle
            elif i == JOINT_INDICES["RElbow"] or i == JOINT_INDICES["RWrist"]: target_dx = -delta_x_arm_back
            elif i == JOINT_INDICES["LElbow"] or i == JOINT_INDICES["LWrist"]: target_dx = delta_x_arm_back
            elif i == JOINT_INDICES["Head"]: target_dy = delta_y_head_bow
            
            current_relative_offsets[i] = (
                lerp(dx0, dx0 + target_dx, ease_in_out_quad(t_phase)),
                lerp(dy0, dy0 + target_dy, ease_in_out_quad(t_phase))
            )

    elif t_norm <= t_landing_start: # Push-off and Flight combined segment
        t_segment_start = t_crouch_end
        t_segment_end = t_landing_start
        t_phase = (t_norm - t_segment_start) / (t_segment_end - t_segment_start)

        # Timepoints within this segment for limb key poses:
        t_segment_takeoff_end = (t_push_off_end - t_segment_start) / (t_segment_end - t_segment_start)
        t_segment_peak_flight = (t_peak_flight - t_segment_start) / (t_segment_end - t_segment_start)
        
        for i in range(NUM_JOINTS):
            if i == JOINT_INDICES["Pelvis"]: continue
            dx0, dy0 = initial_relative_coords[i] # Base offset

            # Relative offsets at the START of this segment (crouch pose)
            start_rel_dx, start_rel_dy = 0, 0
            if i in [JOINT_INDICES["RKnee"], JOINT_INDICES["LKnee"]]: start_rel_dy = delta_y_crouch_knee
            elif i == JOINT_INDICES["RAnkle"] or i == JOINT_INDICES["LAnkle"]: start_rel_dy = delta_y_crouch_ankle
            elif i == JOINT_INDICES["RElbow"] or i == JOINT_INDICES["RWrist"]: start_rel_dx = -delta_x_arm_back
            elif i == JOINT_INDICES["LElbow"] or i == JOINT_INDICES["LWrist"]: start_rel_dx = delta_x_arm_back
            elif i == JOINT_INDICES["Head"]: start_rel_dy = delta_y_head_bow
            
            # Target relative offsets at TAKEOFF (legs straight, arms forward/up)
            takeoff_rel_dx, takeoff_rel_dy = 0, 0
            if i == JOINT_INDICES["RElbow"] or i == JOINT_INDICES["RWrist"]:
                takeoff_rel_dx, takeoff_rel_dy = delta_x_arm_forward, -delta_y_arm_up
            elif i == JOINT_INDICES["LElbow"] or i == JOINT_INDICES["LWrist"]:
                takeoff_rel_dx, takeoff_rel_dy = -delta_x_arm_forward, -delta_y_arm_up
            
            # Target relative offsets at FLIGHT PEAK (legs tucked, arms relaxed, head slightly bowed)
            peak_rel_dx, peak_rel_dy = 0, 0
            if i in [JOINT_INDICES["RKnee"], JOINT_INDICES["LKnee"]]: peak_rel_dy = delta_y_flight_knee
            elif i in [JOINT_INDICES["RAnkle"], JOINT_INDICES["LAnkle"]]: peak_rel_dy = delta_y_flight_ankle
            elif i == JOINT_INDICES["RElbow"] or i == JOINT_INDICES["RWrist"]: peak_rel_dx, peak_rel_dy = delta_x_arm_forward * 0.5, -delta_y_arm_up * 0.5 # Relaxed forward
            elif i == JOINT_INDICES["LElbow"] or i == JOINT_INDICES["LWrist"]: peak_rel_dx, peak_rel_dy = -delta_x_arm_forward * 0.5, -delta_y_arm_up * 0.5
            elif i == JOINT_INDICES["Head"]: peak_rel_dy = delta_y_head_bow * 0.5 # Slightly bowed

            # Target relative offsets at LANDING CONTACT (legs straight, arms neutral, head neutral)
            landing_contact_rel_dx, landing_contact_rel_dy = 0, 0 # Back to standing-like posture

            current_t = t_phase # Normalized time within this segment
            
            # Apply interpolation for legs
            if i in [JOINT_INDICES["RKnee"], JOINT_INDICES["LKnee"]]:
                if current_t < t_segment_takeoff_end: # Crouch to straight
                    target_dy = lerp(start_rel_dy, 0, ease_in_out_quad(current_t / t_segment_takeoff_end))
                elif current_t < t_segment_peak_flight: # Straight to tucked
                    t_sub_phase = (current_t - t_segment_takeoff_end) / (t_segment_peak_flight - t_segment_takeoff_end)
                    target_dy = lerp(0, peak_rel_dy, ease_in_out_quad(t_sub_phase))
                else: # Tucked to straight for landing contact
                    t_sub_phase = (current_t - t_segment_peak_flight) / (1.0 - t_segment_peak_flight)
                    target_dy = lerp(peak_rel_dy, landing_contact_rel_dy, ease_in_out_quad(t_sub_phase))
                current_relative_offsets[i] = (dx0, dy0 + target_dy)
            elif i in [JOINT_INDICES["RAnkle"], JOINT_INDICES["LAnkle"]]:
                if current_t < t_segment_takeoff_end:
                    target_dy = lerp(start_rel_dy, 0, ease_in_out_quad(current_t / t_segment_takeoff_end))
                elif current_t < t_segment_peak_flight:
                    t_sub_phase = (current_t - t_segment_takeoff_end) / (t_segment_peak_flight - t_segment_takeoff_end)
                    target_dy = lerp(0, peak_rel_dy, ease_in_out_quad(t_sub_phase))
                else:
                    t_sub_phase = (current_t - t_segment_peak_flight) / (1.0 - t_segment_peak_flight)
                    target_dy = lerp(peak_rel_dy, landing_contact_rel_dy, ease_in_out_quad(t_sub_phase))
                current_relative_offsets[i] = (dx0, dy0 + target_dy)

            # Apply interpolation for arms
            elif i == JOINT_INDICES["RElbow"] or i == JOINT_INDICES["RWrist"]:
                start_x, start_y = start_rel_dx, start_rel_dy
                if i == JOINT_INDICES["RWrist"]: # Wrist has slightly different starting offset
                    start_x = -delta_x_arm_back * 1.2
                    start_y = delta_y_arm_up * 0.2
                    
                target_x, target_y = 0, 0
                if current_t < t_segment_takeoff_end: # Swing back to forward/up
                    target_x = lerp(start_x, takeoff_rel_dx, ease_in_out_quad(current_t / t_segment_takeoff_end))
                    target_y = lerp(start_y, takeoff_rel_dy, ease_in_out_quad(current_t / t_segment_takeoff_end))
                elif current_t < t_segment_peak_flight: # Forward/up to relaxed/tucked
                    t_sub_phase = (current_t - t_segment_takeoff_end) / (t_segment_peak_flight - t_segment_takeoff_end)
                    target_x = lerp(takeoff_rel_dx, peak_rel_dx, ease_in_out_quad(t_sub_phase))
                    target_y = lerp(takeoff_rel_dy, peak_rel_dy, ease_in_out_quad(t_sub_phase))
                else: # Relaxed to neutral for landing
                    t_sub_phase = (current_t - t_segment_peak_flight) / (1.0 - t_segment_peak_flight)
                    target_x = lerp(peak_rel_dx, landing_contact_rel_dx, ease_in_out_quad(t_sub_phase))
                    target_y = lerp(peak_rel_dy, landing_contact_rel_dy, ease_in_out_quad(t_sub_phase))
                current_relative_offsets[i] = (dx0 + target_x, dy0 + target_y)

            elif i == JOINT_INDICES["LElbow"] or i == JOINT_INDICES["LWrist"]:
                start_x, start_y = start_rel_dx, start_rel_dy
                if i == JOINT_INDICES["LWrist"]: # Wrist has slightly different starting offset
                    start_x = delta_x_arm_back * 1.2
                    start_y = delta_y_arm_up * 0.2
                
                target_x, target_y = 0, 0
                if current_t < t_segment_takeoff_end:
                    target_x = lerp(start_x, takeoff_rel_dx, ease_in_out_quad(current_t / t_segment_takeoff_end))
                    target_y = lerp(start_y, takeoff_rel_dy, ease_in_out_quad(current_t / t_segment_takeoff_end))
                elif current_t < t_segment_peak_flight:
                    t_sub_phase = (current_t - t_segment_takeoff_end) / (t_segment_peak_flight - t_segment_takeoff_end)
                    target_x = lerp(takeoff_rel_dx, peak_rel_dx, ease_in_out_quad(t_sub_phase))
                    target_y = lerp(takeoff_rel_dy, peak_rel_dy, ease_in_out_quad(t_sub_phase))
                else:
                    t_sub_phase = (current_t - t_segment_peak_flight) / (1.0 - t_segment_peak_flight)
                    target_x = lerp(peak_rel_dx, landing_contact_rel_dx, ease_in_out_quad(t_sub_phase))
                    target_y = lerp(peak_rel_dy, landing_contact_rel_dy, ease_in_out_quad(t_sub_phase))
                current_relative_offsets[i] = (dx0 + target_x, dy0 + target_y)

            # Apply interpolation for head
            elif i == JOINT_INDICES["Head"]:
                if current_t < t_segment_takeoff_end: # From bowed to straight
                    target_dy = lerp(start_rel_dy, 0, ease_in_out_quad(current_t / t_segment_takeoff_end))
                elif current_t < t_segment_peak_flight: # From straight to slightly bowed
                    t_sub_phase = (current_t - t_segment_takeoff_end) / (t_segment_peak_flight - t_segment_takeoff_end)
                    target_dy = lerp(0, peak_rel_dy, ease_in_out_quad(t_sub_phase))
                else: # From slightly bowed to neutral for landing
                    t_sub_phase = (current_t - t_segment_peak_flight) / (1.0 - t_segment_peak_flight)
                    target_dy = lerp(peak_rel_dy, landing_contact_rel_dy, ease_in_out_quad(t_sub_phase))
                current_relative_offsets[i] = (dx0, dy0 + target_dy)

            # Neck, Shoulders, Hips remain relatively static to pelvis in this approximation
            else:
                current_relative_offsets[i] = (dx0 + start_rel_dx, dy0 + start_rel_dy)


    else: # Recovery phase (t_norm > t_landing_start)
        t_segment_start = t_landing_start
        t_segment_end = t_recovery_end
        t_phase = (t_norm - t_segment_start) / (t_segment_end - t_segment_start)

        for i in range(NUM_JOINTS):
            if i == JOINT_INDICES["Pelvis"]: continue
            dx0, dy0 = initial_relative_coords[i]
            
            # Start deltas for recovery (from landing absorption pose)
            s_dx, s_dy = 0, 0
            if i in [JOINT_INDICES["RKnee"], JOINT_INDICES["LKnee"]]: s_dy = delta_y_landing_knee
            elif i in [JOINT_INDICES["RAnkle"], JOINT_INDICES["LAnkle"]]: s_dy = delta_y_landing_ankle
            elif i == JOINT_INDICES["RElbow"] or i == JOINT_INDICES["RWrist"]: s_dx = delta_x_arm_out
            elif i == JOINT_INDICES["LElbow"] or i == JOINT_INDICES["LWrist"]: s_dx = -delta_x_arm_out
            elif i == JOINT_INDICES["Head"]: s_dy = delta_y_head_bow * 0.2 # Small bow after landing
            
            # End deltas for recovery (back to standing/initial relative offsets, which are (0,0) deltas)
            e_dx, e_dy = 0, 0

            # Apply interpolation based on s_dx, s_dy (current pose at start of recovery)
            # and e_dx, e_dy (target pose at end of recovery, which is standing/neutral)
            current_relative_offsets[i] = (
                lerp(dx0 + s_dx, dx0 + e_dx, ease_in_out_quad(t_phase)),
                lerp(dy0 + s_dy, dy0 + e_dy, ease_in_out_quad(t_phase))
            )

    # Apply the calculated relative offsets to the global pelvis position
    for i in range(NUM_JOINTS):
        if i == JOINT_INDICES["Pelvis"]:
            continue
        dx, dy = current_relative_offsets[i]
        current_positions[i] = (pelvis_global_x + dx, pelvis_global_y + dy)

    return current_positions


# --- Main Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation frame
    current_frame = (current_frame + 1) % TOTAL_ANIMATION_FRAMES

    # Get current joint positions
    joint_coords = get_joint_positions(current_frame)

    # Drawing
    screen.fill(BLACK) # Black background

    for x, y in joint_coords:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), DOT_RADIUS)

    pygame.display.flip() # Update the full display surface
    clock.tick(FPS) # Control frame rate

pygame.quit()
