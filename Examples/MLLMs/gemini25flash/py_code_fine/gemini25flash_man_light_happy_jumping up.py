
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 5

FPS = 60
ANIMATION_DURATION_SECONDS = 3.0  # Total duration of one jump cycle
TOTAL_FRAMES = int(FPS * ANIMATION_DURATION_SECONDS)

# --- Biomechanical Parameters (relative lengths and initial angles) ---
# Scale factor to convert normalized human dimensions to screen pixels.
SCALE_FACTOR = 250  # Roughly how many pixels tall the standing figure is from hip to head.

# Relative lengths of body segments (normalized to total figure height)
SEGMENT_LEN_RATIOS = {
    'head_to_neck_top': 0.08,  # From shoulder line to top of head
    'neck_to_shoulder_horizontal': 0.08, # Half distance between shoulders
    'shoulder_to_hip_vertical': 0.35, # From shoulder line to hip line (midpoint)
    'upper_arm': 0.17,
    'forearm': 0.15,
    'hand': 0.05,
    'upper_leg': 0.23,
    'lower_leg': 0.23,
    'foot': 0.10,
    'hip_horizontal_offset': 0.08, # Half distance between hip joints
}

# Calculate actual lengths in pixels
SEGMENT_LENS = {k: v * SCALE_FACTOR for k, v in SEGMENT_LEN_RATIOS.items()}

# Initial Pelvis Y position (midpoint between hips)
# This positions the figure so feet are near the bottom of the screen.
# Standing figure base_y (hip level) starts at:
# SCREEN_HEIGHT - foot_length - lower_leg_length - upper_leg_length
INITIAL_BASE_Y = SCREEN_HEIGHT - SEGMENT_LENS['foot'] - SEGMENT_LENS['lower_leg'] - SEGMENT_LENS['upper_leg']

# --- Point Mapping (15 points as required) ---
# This is a standard 15-point configuration for biological motion:
# Head, L/R Shoulder, L/R Elbow, L/R Wrist, L/R Hip, L/R Knee, L/R Ankle, L/R Foot.
JOINT_NAMES = [
    "HEAD", "L_SHOULDER", "R_SHOULDER", "L_ELBOW", "R_ELBOW", "L_WRIST", "R_WRIST",
    "L_HIP", "R_HIP", "L_KNEE", "R_KNEE", "L_ANKLE", "R_ANKLE", "L_FOOT", "R_FOOT"
]

# --- Helper Functions ---
def lerp(a, b, t):
    """Linear interpolation."""
    return a + (b - a) * t

def calculate_pose(base_x, base_y, angles):
    """
    Calculates the (x,y) coordinates of all 15 points based on the base position (mid-hip)
    and joint angles.

    Angle Convention: All angles are absolute angles relative to the global Y-axis (downwards).
    - 0 radians: Straight down (positive Y direction in Pygame)
    - pi/2 radians: Straight right (positive X direction)
    - -pi/2 radians: Straight left (negative X direction)
    - pi radians: Straight up (negative Y direction)

    Joint Angle Definitions:
    - hip_L/R: Angle of upper_leg relative to vertical (0 = straight down, positive = swing forward/clockwise)
    - knee_L/R: Angle of lower_leg relative to upper_leg (0 = straight, positive = bend/flex knee)
    - ankle_L/R: Angle of foot relative to lower_leg (0 = foot straight, positive = plantarflexion/foot down, negative = dorsiflexion/foot up)
    - torso_lean: Angle of torso from mid-hip to shoulder line (0 = vertical, positive = lean forward/clockwise)
    - shoulder_L/R: Angle of upper_arm relative to torso's axis (0 = straight down relative to torso, positive = swing forward/clockwise)
    - elbow_L/R: Angle of forearm relative to upper_arm (0 = straight, positive = bend/flex elbow)
    - wrist_L/R: Angle of hand relative to forearm (0 = straight)
    """
    points = {}

    # 1. Hips (L_HIP, R_HIP) - base of the figure. base_y is the average Y of hips.
    # L_HIP is to the left, R_HIP is to the right of base_x.
    points['L_HIP'] = (base_x - SEGMENT_LENS['hip_horizontal_offset'], base_y)
    points['R_HIP'] = (base_x + SEGMENT_LENS['hip_horizontal_offset'], base_y)

    # 2. Legs: L_HIP/R_HIP -> L_KNEE/R_KNEE -> L_ANKLE/R_ANKLE -> L_FOOT/R_FOOT
    # Upper Leg: L_KNEE / R_KNEE
    points['L_KNEE'] = (
        points['L_HIP'][0] + SEGMENT_LENS['upper_leg'] * math.sin(angles['hip_L']),
        points['L_HIP'][1] + SEGMENT_LENS['upper_leg'] * math.cos(angles['hip_L'])
    )
    points['R_KNEE'] = (
        points['R_HIP'][0] + SEGMENT_LENS['upper_leg'] * math.sin(angles['hip_R']),
        points['R_HIP'][1] + SEGMENT_LENS['upper_leg'] * math.cos(angles['hip_R'])
    )

    # Lower Leg: L_ANKLE / R_ANKLE
    # Absolute angle of lower leg: hip_angle + knee_bend_angle
    points['L_ANKLE'] = (
        points['L_KNEE'][0] + SEGMENT_LENS['lower_leg'] * math.sin(angles['hip_L'] + angles['knee_L']),
        points['L_KNEE'][1] + SEGMENT_LENS['lower_leg'] * math.cos(angles['hip_L'] + angles['knee_L'])
    )
    points['R_ANKLE'] = (
        points['R_KNEE'][0] + SEGMENT_LENS['lower_leg'] * math.sin(angles['hip_R'] + angles['knee_R']),
        points['R_KNEE'][1] + SEGMENT_LENS['lower_leg'] * math.cos(angles['hip_R'] + angles['knee_R'])
    )

    # Foot: L_FOOT / R_FOOT
    # Absolute angle of foot: hip_angle + knee_bend_angle + ankle_bend_angle
    points['L_FOOT'] = (
        points['L_ANKLE'][0] + SEGMENT_LENS['foot'] * math.sin(angles['hip_L'] + angles['knee_L'] + angles['ankle_L']),
        points['L_ANKLE'][1] + SEGMENT_LENS['foot'] * math.cos(angles['hip_L'] + angles['knee_L'] + angles['ankle_L'])
    )
    points['R_FOOT'] = (
        points['R_ANKLE'][0] + SEGMENT_LENS['foot'] * math.sin(angles['hip_R'] + angles['knee_R'] + angles['ankle_R']),
        points['R_ANKLE'][1] + SEGMENT_LENS['foot'] * math.cos(angles['hip_R'] + angles['knee_R'] + angles['ankle_R'])
    )

    # 3. Torso/Arms/Head
    # Mid-hip point: for connecting to torso.
    mid_hip_x = (points['L_HIP'][0] + points['R_HIP'][0]) / 2
    mid_hip_y = (points['L_HIP'][1] + points['R_HIP'][1]) / 2

    # Shoulder line (top of torso)
    # Absolute angle of torso: torso_lean (relative to vertical)
    shoulder_mid_x = mid_hip_x + SEGMENT_LENS['shoulder_to_hip_vertical'] * math.sin(angles['torso_lean'])
    shoulder_mid_y = mid_hip_y - SEGMENT_LENS['shoulder_to_hip_vertical'] * math.cos(angles['torso_lean'])

    # Shoulders (L_SHOULDER, R_SHOULDER)
    # Relative to shoulder_mid and perpendicular to torso_lean.
    # To get perpendicular, add/subtract pi/2 from torso_lean.
    points['L_SHOULDER'] = (
        shoulder_mid_x - SEGMENT_LENS['neck_to_shoulder_horizontal'] * math.cos(angles['torso_lean']),
        shoulder_mid_y - SEGMENT_LENS['neck_to_shoulder_horizontal'] * math.sin(angles['torso_lean'])
    )
    points['R_SHOULDER'] = (
        shoulder_mid_x + SEGMENT_LENS['neck_to_shoulder_horizontal'] * math.cos(angles['torso_lean']),
        shoulder_mid_y + SEGMENT_LENS['neck_to_shoulder_horizontal'] * math.sin(angles['torso_lean'])
    )

    # Head (HEAD)
    # Relative to shoulder_mid, along torso axis upwards.
    points['HEAD'] = (
        shoulder_mid_x - SEGMENT_LENS['head_to_neck_top'] * math.sin(angles['torso_lean']),
        shoulder_mid_y + SEGMENT_LENS['head_to_neck_top'] * math.cos(angles['torso_lean'])
    )

    # Arms: L_SHOULDER/R_SHOULDER -> L_ELBOW/R_ELBOW -> L_WRIST/R_WRIST
    # Upper Arm: L_ELBOW / R_ELBOW
    # Absolute angle of upper arm: torso_lean + shoulder_swing_angle
    points['L_ELBOW'] = (
        points['L_SHOULDER'][0] + SEGMENT_LENS['upper_arm'] * math.sin(angles['torso_lean'] + angles['shoulder_L']),
        points['L_SHOULDER'][1] + SEGMENT_LENS['upper_arm'] * math.cos(angles['torso_lean'] + angles['shoulder_L'])
    )
    points['R_ELBOW'] = (
        points['R_SHOULDER'][0] + SEGMENT_LENS['upper_arm'] * math.sin(angles['torso_lean'] + angles['shoulder_R']),
        points['R_SHOULDER'][1] + SEGMENT_LENS['upper_arm'] * math.cos(angles['torso_lean'] + angles['shoulder_R'])
    )

    # Forearm: L_WRIST / R_WRIST
    # Absolute angle of forearm: torso_lean + shoulder_swing_angle + elbow_bend_angle
    points['L_WRIST'] = (
        points['L_ELBOW'][0] + SEGMENT_LENS['forearm'] * math.sin(angles['torso_lean'] + angles['shoulder_L'] + angles['elbow_L']),
        points['L_ELBOW'][1] + SEGMENT_LENS['forearm'] * math.cos(angles['torso_lean'] + angles['shoulder_L'] + angles['elbow_L'])
    )
    points['R_WRIST'] = (
        points['R_ELBOW'][0] + SEGMENT_LENS['forearm'] * math.sin(angles['torso_lean'] + angles['shoulder_R'] + angles['elbow_R']),
        points['R_ELBOW'][1] + SEGMENT_LENS['forearm'] * math.cos(angles['torso_lean'] + angles['shoulder_R'] + angles['elbow_R'])
    )

    # Consolidate results into a list matching JOINT_NAMES order
    result_coords = [
        points['HEAD'],
        points['L_SHOULDER'], points['R_SHOULDER'],
        points['L_ELBOW'], points['R_ELBOW'],
        points['L_WRIST'], points['R_WRIST'],
        points['L_HIP'], points['R_HIP'],
        points['L_KNEE'], points['R_KNEE'],
        points['L_ANKLE'], points['R_ANKLE'],
        points['L_FOOT'], points['R_FOOT'],
    ]
    return result_coords

# --- Define Keyframe Poses ---
# Each pose defines the joint angles and the base_y (mid-hip Y coordinate)
# Angles are in radians.

# STANDING: Normal upright posture
STANDING_POSE = {
    'angles': {
        'hip_L': 0.0, 'knee_L': 0.0, 'ankle_L': 0.0,  # Legs straight down
        'hip_R': 0.0, 'knee_R': 0.0, 'ankle_R': 0.0,
        'shoulder_L': 0.0, 'elbow_L': 0.0, 'wrist_L': 0.0, # Arms straight down
        'shoulder_R': 0.0, 'elbow_R': 0.0, 'wrist_R': 0.0,
        'torso_lean': 0.0, # Torso vertical
    },
    'base_y': INITIAL_BASE_Y
}

# CROUCH_DEEP: Deep squat, arms swung back
CROUCH_DEEP_POSE = {
    'angles': {
        'hip_L': 0.35, 'knee_L': 1.3, 'ankle_L': -0.6, # Bend legs significantly, dorsiflex ankle
        'hip_R': 0.35, 'knee_R': 1.3, 'ankle_R': -0.6,
        'shoulder_L': -0.8, 'elbow_L': 0.2, 'wrist_L': 0.0, # Arms swung back, slight elbow bend
        'shoulder_R': -0.8, 'elbow_R': 0.2, 'wrist_R': 0.0,
        'torso_lean': 0.2, # Slight forward lean
    },
    'base_y': INITIAL_BASE_Y + SCALE_FACTOR * 0.20 # Pelvis moves down by 20% of figure height
}

# PUSH_OFF: Legs extending, arms swinging forward/up
PUSH_OFF_POSE = {
    'angles': {
        'hip_L': -0.1, 'knee_L': -0.1, 'ankle_L': 0.5, # Legs extended, pushing off toes (plantarflexion)
        'hip_R': -0.1, 'knee_R': -0.1, 'ankle_R': 0.5,
        'shoulder_L': 0.8, 'elbow_L': 0.0, 'wrist_L': 0.0, # Arms swinging forward/up, straight
        'shoulder_R': 0.8, 'elbow_R': 0.0, 'wrist_R': 0.0,
        'torso_lean': 0.0, # Torso straightens
    },
    'base_y': INITIAL_BASE_Y - SCALE_FACTOR * 0.05 # Pelvis slightly above standing as pushing up
}

# APEX: Airborne, body at peak height, legs slightly tucked, arms overhead
APEX_POSE = {
    'angles': {
        'hip_L': 0.1, 'knee_L': 0.3, 'ankle_L': 0.1, # Legs slightly tucked
        'hip_R': 0.1, 'knee_R': 0.3, 'ankle_R': 0.1,
        'shoulder_L': 1.2, 'elbow_L': 0.0, 'wrist_L': 0.0, # Arms fully overhead
        'shoulder_R': 1.2, 'elbow_R': 0.0, 'wrist_R': 0.0,
        'torso_lean': 0.0, # Torso vertical
    },
    'base_y': INITIAL_BASE_Y - SCALE_FACTOR * 0.45 # Pelvis at peak height
}

# LANDING_IMPACT: Feet touch, legs bending to absorb impact, arms forward
LANDING_IMPACT_POSE = {
    'angles': {
        'hip_L': 0.2, 'knee_L': 0.8, 'ankle_L': -0.3, # Legs bending to absorb, dorsiflexion
        'hip_R': 0.2, 'knee_R': 0.8, 'ankle_R': -0.3,
        'shoulder_L': 0.4, 'elbow_L': 0.2, 'wrist_L': 0.0, # Arms slightly forward/down
        'shoulder_R': 0.4, 'elbow_R': 0.2, 'wrist_R': 0.0,
        'torso_lean': 0.1, # Slight forward lean
    },
    'base_y': INITIAL_BASE_Y + SCALE_FACTOR * 0.10 # Pelvis slightly below standing
}

# RECOVER: Return to initial standing posture
RECOVER_POSE = STANDING_POSE

# Define the sequence of keyframe poses and their duration in frames.
# The total sum of durations should be TOTAL_FRAMES.
KEYFRAMES = [
    (STANDING_POSE, int(FPS * 0.5)),      # Phase 0: Initial standing pause
    (CROUCH_DEEP_POSE, int(FPS * 0.5)),   # Phase 1: Crouch down
    (PUSH_OFF_POSE, int(FPS * 0.4)),      # Phase 2: Push off from ground
    (APEX_POSE, int(FPS * 0.6)),          # Phase 3: Airborne (ascend to apex, then descend) - Apex is mid-point of this phase
    (LANDING_IMPACT_POSE, int(FPS * 0.4)),# Phase 4: Landing and absorbing impact
    (RECOVER_POSE, int(FPS * 0.6))        # Phase 5: Recover to standing
]

# Ensure total frames match animation duration
current_sum = sum(duration for _, duration in KEYFRAMES)
if current_sum != TOTAL_FRAMES:
    print(f"Warning: Keyframe durations sum to {current_sum}, but TOTAL_FRAMES is {TOTAL_FRAMES}. Adjusting last phase duration.")
    last_phase_duration = KEYFRAMES[-1][1] + (TOTAL_FRAMES - current_sum)
    KEYFRAMES[-1] = (KEYFRAMES[-1][0], last_phase_duration)

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Jumping Man")
clock = pygame.time.Clock()

running = True
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Determine current phase and progress within that phase
    cumulative_frames = 0
    current_phase_index = 0
    for i, (_, duration) in enumerate(KEYFRAMES):
        if frame_count < cumulative_frames + duration:
            current_phase_index = i
            break
        cumulative_frames += duration

    # Get start and end poses for interpolation
    start_pose = KEYFRAMES[current_phase_index][0]
    # For continuous loop, after the last phase, transition back to the first.
    end_pose = KEYFRAMES[(current_phase_index + 1) % len(KEYFRAMES)][0]
    
    local_frame_in_phase = frame_count - cumulative_frames
    phase_duration = KEYFRAMES[current_phase_index][1]
    
    # Calculate interpolation progress (0.0 to 1.0)
    progress = local_frame_in_phase / phase_duration if phase_duration > 0 else 0

    # Smooth the interpolation using cosine easing (ease-in-out)
    eased_progress = 0.5 - 0.5 * math.cos(math.pi * progress)

    # Interpolate angles for the current frame
    angles_interp = {}
    for joint, start_val in start_pose['angles'].items():
        angles_interp[joint] = lerp(start_val, end_pose['angles'][joint], eased_progress)

    # Special handling for the Airborne phase (Phase 3) Y-movement to create a smooth parabolic arc.
    # The 'APEX_POSE' is the peak of the jump, which occurs in the middle of this phase.
    if current_phase_index == 3:
        # Interpolate Y from PUSH_OFF_POSE to APEX_POSE (first half) then APEX_POSE to LANDING_IMPACT_POSE (second half).
        # The angles are already handled by the general interpolation from PUSH_OFF to APEX, then APEX to LANDING.
        half_phase_duration = phase_duration / 2
        
        if local_frame_in_phase < half_phase_duration:
            # Ascent part: from PUSH_OFF_POSE's base_y to APEX_POSE's base_y
            y_progress_segment = local_frame_in_phase / half_phase_duration
            current_base_y = lerp(PUSH_OFF_POSE['base_y'], APEX_POSE['base_y'], y_progress_segment)
        else:
            # Descent part: from APEX_POSE's base_y to LANDING_IMPACT_POSE's base_y
            y_progress_segment = (local_frame_in_phase - half_phase_duration) / half_phase_duration
            current_base_y = lerp(APEX_POSE['base_y'], LANDING_IMPACT_POSE['base_y'], y_progress_segment)
    else:
        # For other phases, linearly interpolate base_y
        current_base_y = lerp(start_pose['base_y'], end_pose['base_y'], eased_progress)

    # Calculate current figure points using interpolated angles and base_y
    figure_center_x = SCREEN_WIDTH // 2
    current_points_coords = calculate_pose(figure_center_x, current_base_y, angles_interp)

    # Draw the points
    for x, y in current_points_coords:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

    pygame.display.flip()

    frame_count = (frame_count + 1) % TOTAL_FRAMES
    clock.tick(FPS)

pygame.quit()
