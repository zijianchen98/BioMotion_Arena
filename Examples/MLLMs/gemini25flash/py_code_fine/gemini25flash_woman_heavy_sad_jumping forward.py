
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
POINT_RADIUS = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Joint Definitions ---
# The 15 joint names, chosen to represent a human figure.
# 'sternum' is included as the 15th point, common in biological motion stimuli.
JOINT_NAMES = [
    "head", "shoulder_L", "shoulder_R", "elbow_L", "elbow_R",
    "wrist_L", "wrist_R", "sternum", "spine", "hip_L", "hip_R",
    "knee_L", "knee_R", "ankle_L", "ankle_R"
]

# Base Y-coordinate for the ground level of the figure on the screen
GROUND_Y = SCREEN_HEIGHT * 0.8

# Global X position parameters for the "jumping forward" motion
JUMP_DISTANCE = SCREEN_WIDTH * 0.6  # Total horizontal distance covered in one jump cycle
JUMP_START_X = SCREEN_WIDTH * 0.2   # Starting X position of the figure on the screen
JUMP_END_X = JUMP_START_X + JUMP_DISTANCE

# Maximum jump height of the figure's lowest point (ankles) above the ground
MAX_JUMP_HEIGHT_ABOVE_GROUND = SCREEN_HEIGHT * 0.2 

# --- Relative Poses (keyframes) ---
# Each pose defines the (x, y) offset of each joint relative to the 'spine' joint.
# The 'spine' joint is treated as the (0,0) origin for the figure's local coordinate system.
# Y coordinates are positive downwards from the spine.

# Base relative offsets for a general standing person (used as a template for keyframes)
_head_y_base = -110
_shoulder_x_base = 30; _shoulder_y_base = -70
_elbow_x_base = 40; _elbow_y_base = -20
_wrist_x_base = 30; _wrist_y_base = 20
_sternum_y_base = -50
_hip_y_base = 5
_knee_y_base = 55 # Distance from spine
_ankle_y_base = 110 # Distance from spine

def get_pose(head_y, shoulder_x, shoulder_y, elbow_x, elbow_y, wrist_x, wrist_y,
             sternum_y, hip_y, knee_y, ankle_y, arm_swing_factor=1.0):
    """
    Helper function to generate a pose dictionary. Joint positions are relative to the spine (0,0).
    """
    pose = {
        "head":       (0,   head_y),
        "shoulder_L": (-shoulder_x, shoulder_y), "shoulder_R": (shoulder_x, shoulder_y),
        "elbow_L":    (-elbow_x * arm_swing_factor, elbow_y), "elbow_R": (elbow_x * arm_swing_factor, elbow_y),
        "wrist_L":    (-wrist_x * arm_swing_factor, wrist_y), "wrist_R": (wrist_x * arm_swing_factor, wrist_y),
        "sternum":    (0,    sternum_y),
        "spine":      (0,      0), # Spine is the origin for relative coordinates
        "hip_L":      (-25,    hip_y), "hip_R":     (25,    hip_y), # Hip width relatively constant
        "knee_L":     (-20,   knee_y), "knee_R": (20,   knee_y),
        "ankle_L":    (-20,  ankle_y), "ankle_R": (20,  ankle_y)
    }
    return pose

# Keyframes representing the "sad woman with heavy weight jumping forward" action.
# The adjustments in joint positions reflect a slumped posture ('sadness') and
# a more pronounced bending and slower extension ('heavy weight').

# 1. Initial Stand (Sad, Heavy): Slightly slumped, knees slightly bent, arms relaxed down.
kf1_stand = get_pose(
    _head_y_base + 10, # Head slightly down
    _shoulder_x_base, _shoulder_y_base + 5, # Shoulders slightly lower
    _elbow_x_base * 0.9, _elbow_y_base + 10, # Arms closer, slightly lower
    _wrist_x_base * 0.8, _wrist_y_base + 20, # Wrists lower, arms more relaxed
    _sternum_y_base + 5, _hip_y_base + 5, # Body slightly compressed
    _knee_y_base + 10, _ankle_y_base + 20 # Knees more bent, 'heavy' feeling
)

# 2. Crouch/Wind-up: Deep crouch, arms swing back for momentum.
kf2_crouch = get_pose(
    _head_y_base + 50, # Head down
    _shoulder_x_base * 1.2, _shoulder_y_base + 40, # Shoulders wide, higher relative to spine
    _elbow_x_base * 1.5, _elbow_y_base + 60, # Arms swung back
    _wrist_x_base * 1.8, _wrist_y_base + 60, # Wrists far back
    _sternum_y_base + 60, _hip_y_base + 70, # Body compressed
    _knee_y_base + 50, _ankle_y_base + 80, # Deep knee bend
    arm_swing_factor=1.5
)

# 3. Takeoff: Legs extending forcefully, arms swinging forward/up for propulsion.
kf3_takeoff = get_pose(
    _head_y_base - 10, # Head up, looking forward
    _shoulder_x_base * 0.8, _shoulder_y_base - 10, # Shoulders forward/up
    _elbow_x_base * 0.5, _elbow_y_base - 40, # Arms swinging forward/up
    _wrist_x_base * 0.3, _wrist_y_base - 40, # Wrists forward/up
    _sternum_y_base - 10, _hip_y_base - 20, # Body extending
    _knee_y_base - 40, _ankle_y_base - 80, # Legs extending rapidly
    arm_swing_factor=0.5
)

# 4. Mid-Air (Peak): Body at highest point of jump, legs slightly tucked or neutral, arms still elevated.
kf4_peak = get_pose(
    _head_y_base - 20, # Head slightly up
    _shoulder_x_base * 0.7, _shoulder_y_base - 20,
    _elbow_x_base * 0.4, _elbow_y_base - 50,
    _wrist_x_base * 0.2, _wrist_y_base - 50,
    _sternum_y_base - 20, _hip_y_base - 30,
    _knee_y_base + 5, _ankle_y_base + 10, # Legs slightly tucked or neutral
    arm_swing_factor=0.4
)

# 5. Descent/Pre-Landing: Body moving down, legs extending forward to prepare for impact absorption.
kf5_pre_land = get_pose(
    _head_y_base + 10,
    _shoulder_x_base * 0.9, _shoulder_y_base - 5,
    _elbow_x_base * 0.7, _elbow_y_base - 10, # Arms coming down
    _wrist_x_base * 0.5, _wrist_y_base + 10,
    _sternum_y_base + 5, _hip_y_base + 10,
    _knee_y_base - 10, _ankle_y_base - 20, # Legs extending forward, slightly bent
    arm_swing_factor=0.7
)

# 6. Landing Impact: Feet touch ground, knees bend sharply to absorb impact, arms might go out for balance.
kf6_land = get_pose(
    _head_y_base + 60,
    _shoulder_x_base * 1.1, _shoulder_y_base + 50, # Shoulders wide for balance
    _elbow_x_base * 1.3, _elbow_y_base + 70, # Arms slightly out/back for balance
    _wrist_x_base * 1.5, _wrist_y_base + 80,
    _sternum_y_base + 70, _hip_y_base + 80,
    _knee_y_base + 70, _ankle_y_base + 90, # Deep knee bend, absorbing
    arm_swing_factor=1.3
)

# 7. Recovery/Final Stand: Slowly returning to a standing or slightly crouched posture.
#    This pose is set to be identical to kf1_stand for seamless looping of the animation.
kf7_recover = kf1_stand.copy()

# Animation sequence of keyframes with their durations in frames
keyframes_sequence = [
    {"pose": kf1_stand, "duration": 40},
    {"pose": kf2_crouch, "duration": 30},
    {"pose": kf3_takeoff, "duration": 20},
    {"pose": kf4_peak, "duration": 30},
    {"pose": kf5_pre_land, "duration": 20},
    {"pose": kf6_land, "duration": 30},
    {"pose": kf7_recover, "duration": 40}
]

TOTAL_ANIM_FRAMES = sum(kf["duration"] for kf in keyframes_sequence)

# --- Absolute Y positions for the spine point for trajectory calculation ---
# These values represent the Y-coordinate of the 'spine' joint on the screen
# when the figure is in specific states (standing, crouched, or at jump peak).
# They are derived from the GROUND_Y and the relative ankle position in each pose.
SPINE_Y_AT_STAND = GROUND_Y - kf1_stand["ankle_L"][1]
SPINE_Y_AT_CROUCH = GROUND_Y - kf2_crouch["ankle_L"][1]

# SPINE_Y_AT_PEAK is calculated based on the maximum jump height and the relative ankle position in the peak pose.
SPINE_Y_AT_PEAK = (GROUND_Y - MAX_JUMP_HEIGHT_ABOVE_GROUND) - kf4_peak["ankle_L"][1]

# Specific Y values for the parabolic jump trajectory.
Y_takeoff_parabola = GROUND_Y - kf3_takeoff["ankle_L"][1]
Y_peak_parabola = SPINE_Y_AT_PEAK
Y_landing_parabola = GROUND_Y - kf5_pre_land["ankle_L"][1]


def get_spine_trajectory(frame_num, total_anim_frames, keyframes_durations):
    """
    Calculates the absolute (x, y) position of the 'spine' joint for a given frame.
    This defines the overall motion (horizontal forward movement and vertical jump arc).
    """
    current_x = JUMP_START_X
    current_y = SPINE_Y_AT_STAND

    # Pre-calculate cumulative durations to easily find current phase
    phase_frames_sum = [0] * len(keyframes_durations)
    current_sum = 0
    for i, kf_data in enumerate(keyframes_durations):
        current_sum += kf_data["duration"]
        phase_frames_sum[i] = current_sum

    # X-trajectory: horizontal movement occurs from the start of kf2 (deep crouch)
    # to the end of kf6 (landing impact), implying movement while pushing off and landing.
    x_move_start_frame = phase_frames_sum[0] # End of kf1, start of kf2
    x_move_end_frame = phase_frames_sum[5]   # End of kf6

    if frame_num < x_move_start_frame:
        current_x = JUMP_START_X
    elif frame_num >= x_move_end_frame:
        current_x = JUMP_END_X
    else:
        t_x = (frame_num - x_move_start_frame) / (x_move_end_frame - x_move_start_frame)
        current_x = JUMP_START_X + t_x * JUMP_DISTANCE

    # Y-trajectory: vertical movement based on animation phases
    
    # Phase 0: Initial Stand to Crouch prep (kf1 duration)
    if frame_num < phase_frames_sum[0]:
        t_y = frame_num / keyframes_durations[0]["duration"]
        current_y = SPINE_Y_AT_STAND * (1 - t_y) + SPINE_Y_AT_CROUCH * t_y

    # Phase 1: Deep crouch (kf2 duration) - holds the lowest Y position before takeoff
    elif frame_num < phase_frames_sum[1]:
        current_y = SPINE_Y_AT_CROUCH
    
    # Combined Airborne Phase: kf3 (takeoff) -> kf4 (peak) -> kf5 (pre-land)
    # This phase uses a parabolic trajectory for smooth vertical motion.
    elif frame_num < phase_frames_sum[4]: # Covers frames from kf3 start to kf5 end
        start_airborne_frame = phase_frames_sum[1] # End of kf2, start of kf3
        airborne_duration = keyframes_durations[2]["duration"] + keyframes_durations[3]["duration"] + keyframes_durations[4]["duration"]
        
        t_airborne = (frame_num - start_airborne_frame) / airborne_duration
        
        # Parabolic function y = A*t^2 + B*t + C
        # Defined by three points: (t=0, Y_takeoff), (t=0.5, Y_peak), (t=1, Y_landing)
        A = 4 * (0.5 * Y_landing_parabola + 0.5 * Y_takeoff_parabola - Y_peak_parabola)
        B = Y_landing_parabola - A - Y_takeoff_parabola
        C = Y_takeoff_parabola
        
        current_y = A * t_airborne**2 + B * t_airborne + C

    # Phase 3: Landing (kf6 duration) + Recovery (kf7 duration)
    # Interpolates back from crouched landing position to standing.
    else: # Covers frames from end of kf5 through kf6 and kf7, up to TOTAL_ANIM_FRAMES
        start_land_recover_frame = phase_frames_sum[4] # End of kf5, start of kf6
        land_recover_duration = keyframes_durations[5]["duration"] + keyframes_durations[6]["duration"]
        
        if land_recover_duration == 0: 
            current_y = SPINE_Y_AT_STAND
        else:
            t_y = (frame_num - start_land_recover_frame) / land_recover_duration
            # Clamp t_y to 1.0 to ensure it doesn't go beyond final state when looping
            t_y = min(t_y, 1.0) 
            current_y = SPINE_Y_AT_CROUCH * (1 - t_y) + SPINE_Y_AT_STAND * t_y
        
    return current_x, current_y

def interpolate_pose(pose1, pose2, t):
    """
    Interpolates joint positions between two given poses.
    't' is a float from 0.0 (fully pose1) to 1.0 (fully pose2).
    """
    interp_pose = {}
    for joint in JOINT_NAMES:
        x1, y1 = pose1[joint]
        x2, y2 = pose2[joint]
        interp_x = x1 * (1 - t) + x2 * t
        interp_y = y1 * (1 - t) + y2 * t
        interp_pose[joint] = (interp_x, interp_y)
    return interp_pose

# --- Main Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Woman Jumping Forward")
clock = pygame.time.Clock()

current_frame = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update animation state ---
    # Advance frame and loop back to start if end is reached
    current_frame = (current_frame + 1) % TOTAL_ANIM_FRAMES

    # Determine which keyframe segment the animation is currently in
    frame_in_segment = current_frame
    current_kf_idx = 0
    for i, kf_data in enumerate(keyframes_sequence):
        if frame_in_segment < kf_data["duration"]:
            current_kf_idx = i
            break
        frame_in_segment -= kf_data["duration"]
            
    # Calculate interpolation factor 't' for the current segment
    t_interp = frame_in_segment / keyframes_sequence[current_kf_idx]["duration"]
    
    # Apply ease-in-out (cosine interpolation) for smoother transitions between poses
    t_interp = 0.5 - 0.5 * math.cos(t_interp * math.pi)

    # Get the start and end poses for interpolation within the current segment
    pose_start = keyframes_sequence[current_kf_idx]["pose"]
    # For the last segment, interpolate back to the very first pose for seamless looping
    pose_end = keyframes_sequence[(current_kf_idx + 1) % len(keyframes_sequence)]["pose"]

    # Calculate the current relative pose of all joints
    current_relative_pose = interpolate_pose(pose_start, pose_end, t_interp)

    # Get the absolute position of the 'spine' (center of mass) for this frame
    spine_x, spine_y = get_spine_trajectory(current_frame, TOTAL_ANIM_FRAMES, keyframes_sequence)

    # --- Draw ---
    screen.fill(BLACK) # Clear screen with black background

    # Draw each point at its calculated absolute position
    for joint_name in JOINT_NAMES:
        rel_x, rel_y = current_relative_pose[joint_name]
        abs_x = int(spine_x + rel_x)
        abs_y = int(spine_y + rel_y)
        pygame.draw.circle(screen, WHITE, (abs_x, abs_y), POINT_RADIUS)

    pygame.display.flip() # Update the full display Surface to the screen
    clock.tick(FPS) # Control the frame rate

pygame.quit()
