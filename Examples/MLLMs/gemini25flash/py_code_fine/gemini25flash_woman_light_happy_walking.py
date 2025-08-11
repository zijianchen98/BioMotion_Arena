
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800  # Portrait aspect ratio similar to the example image
FPS = 60
POINT_RADIUS = 4  # Radius for standard body points
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Human Body Proportions (Relative to a base height) ---
# These are rough estimations. Adjust for desired visual.
# "light weight" woman implies somewhat slender proportions.
BODY_SCALE = 1.0  # Overall scaling factor for the figure
BASE_BODY_HEIGHT = 200 * BODY_SCALE  # Total height of the "body" part, excluding head

# Proportions of body segments relative to BASE_BODY_HEIGHT
HEAD_PROPORTION = 0.15
NECK_PROPORTION = 0.05
TORSO_PROPORTION = 0.35  # Neck to Pelvis
PELVIS_WIDTH_PROPORTION = 0.2
SHOULDER_WIDTH_PROPORTION = 0.25
ARM_LENGTH_PROPORTION = 0.3  # Upper arm + forearm
LEG_LENGTH_PROPORTION = 0.5  # Upper leg + lower leg

# Actual lengths in pixels based on proportions
HEAD_POINT_RADIUS = POINT_RADIUS * 2 * BODY_SCALE  # Head point usually slightly larger
NECK_LENGTH = NECK_PROPORTION * BASE_BODY_HEIGHT
TORSO_LENGTH = TORSO_PROPORTION * BASE_BODY_HEIGHT
PELVIS_WIDTH = PELVIS_WIDTH_PROPORTION * BASE_BODY_HEIGHT
SHOULDER_WIDTH = SHOLDER_WIDTH_PROPORTION * BASE_BODY_HEIGHT
UPPER_ARM_LENGTH = ARM_LENGTH_PROPORTION / 2 * BASE_BODY_HEIGHT
FOREARM_LENGTH = ARM_LENGTH_PROPORTION / 2 * BASE_BODY_HEIGHT
UPPER_LEG_LENGTH = LEG_LENGTH_PROPORTION / 2 * BASE_BODY_HEIGHT
LOWER_LEG_LENGTH = LEG_LENGTH_PROPORTION / 2 * BASE_BODY_HEIGHT

# --- Walking Motion Parameters ---
WALK_CYCLE_FRAMES = 60  # Frames for one full gait cycle (e.g., right leg forward, then left, then right again)
WALK_SPEED_X_PIXELS_PER_CYCLE = 120  # How much the person moves horizontally per cycle

# Amplitude of joint oscillations (in degrees)
# Angles are from the vertical, positive for backward swing (clockwise in standard math, counter-clockwise in Pygame-like y-down system)
# Negative for forward swing (counter-clockwise in standard math, clockwise in Pygame-like y-down system)
HIP_SWING_AMP = 30  # Swing of entire leg at hip (forward/backward from vertical)
KNEE_BEND_AMP = 55  # How much knee bends during swing (from straight, forward bend)
ANKLE_BEND_AMP = 10  # Ankle movement (minor lift during swing)
ARM_SWING_AMP = 40  # Arm swing at shoulder (forward/backward from vertical)
ELBOW_BEND_AMP = 15  # Slight elbow bend (from straight, forward bend)

PELVIS_BOB_AMP = 8  # Vertical bobbing of pelvis ("light weight" can imply more bounce)

# Initial vertical position for the pelvis center (main reference point)
INITIAL_Y = SCREEN_HEIGHT / 2

# --- Joint Mapping for 15 Points ---
# This order implicitly defines the connections needed for a skeletal model,
# but we are only drawing the points themselves.
JOINT_NAMES = [
    "head", "neck",
    "r_shoulder", "l_shoulder",
    "r_elbow", "l_elbow",
    "r_wrist", "l_wrist",
    "r_hip", "l_hip",
    "r_knee", "l_knee",
    "r_ankle", "l_ankle",
    "pelvis_center" # The 15th point, a common central reference
]

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion (Walking Woman)")
clock = pygame.time.Clock()

frame_count = 0
running = True

# Dictionary to store current calculated positions of all joints
joint_positions = {}

# --- Main Animation Loop ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # --- Calculate Joint Positions for Current Frame ---
    # 't' represents progress through one full gait cycle (0 to WALK_CYCLE_FRAMES-1)
    t = frame_count % WALK_CYCLE_FRAMES
    # 'angle' maps 't' to a radian value from 0 to 2*pi
    angle = (t / WALK_CYCLE_FRAMES) * (2 * math.pi)

    # Global horizontal translation for the entire figure
    # The figure walks across the screen from left to right and loops seamlessly.
    # It starts off-screen left and reappears once it's off-screen right.
    # The loop distance covers the screen width plus the figure's approximate width.
    figure_approx_width = SHOULDER_WIDTH
    horizontal_loop_distance = SCREEN_WIDTH + figure_approx_width
    
    # Calculate current horizontal movement based on frame count
    horizontal_movement_progress = (frame_count * (WALK_SPEED_X_PIXELS_PER_CYCLE / WALK_CYCLE_FRAMES))
    
    # Calculate the x-offset for the figure's center within the looping range
    x_offset_within_loop = horizontal_movement_progress % horizontal_loop_distance
    
    # Adjust to start the figure slightly off the left edge (-figure_approx_width / 2)
    current_x_center = -figure_approx_width / 2 + x_offset_within_loop

    # Pelvis Center (base of torso, primary reference point for the entire figure)
    # Pelvis bobbing (vertical oscillation during walking)
    pelvis_y_bob = PELVIS_BOB_AMP * math.sin(angle * 2)  # Bobs up/down twice per cycle
    pelvis_center_pos = (current_x_center, INITIAL_Y + pelvis_y_bob)
    joint_positions["pelvis_center"] = pelvis_center_pos

    # Hips (relative to pelvis center)
    r_hip_x = pelvis_center_pos[0] + PELVIS_WIDTH / 2
    l_hip_x = pelvis_center_pos[0] - PELVIS_WIDTH / 2
    hip_y = pelvis_center_pos[1]
    joint_positions["r_hip"] = (r_hip_x, hip_y)
    joint_positions["l_hip"] = (l_hip_x, hip_y)

    # Torso, Neck, and Head positions
    # Neck is above pelvis center
    neck_pos = (pelvis_center_pos[0], pelvis_center_pos[1] - TORSO_LENGTH)
    joint_positions["neck"] = neck_pos

    # Head (above neck)
    head_pos = (neck_pos[0], neck_pos[1] - NECK_LENGTH - HEAD_POINT_RADIUS / 2)
    joint_positions["head"] = head_pos

    # Shoulders (relative to neck)
    shoulder_y = neck_pos[1] + NECK_LENGTH / 4  # Slightly below neck, top of torso
    r_shoulder_x = neck_pos[0] + SHOULDER_WIDTH / 2
    l_shoulder_x = neck_pos[0] - SHOULDER_WIDTH / 2
    joint_positions["r_shoulder"] = (r_shoulder_x, shoulder_y)
    joint_positions["l_shoulder"] = (l_shoulder_x, shoulder_y)

    # --- Legs Calculation ---
    # Angles are defined relative to the vertical line (straight down is 0 radians).
    # Positive angles indicate a swing backward (clockwise rotation from vertical).
    # Negative angles indicate a swing forward (counter-clockwise rotation from vertical).

    # Hip Swing Angles: Right leg leads with phase 0 (cos(angle)), Left leg trails with phase pi (cos(angle + pi)).
    # This means when right leg is maximally backward (cos(angle)=1, positive angle), left leg is maximally forward (cos(angle+pi)=-1, negative angle).
    hip_swing_R = math.radians(HIP_SWING_AMP) * math.cos(angle)
    hip_swing_L = math.radians(HIP_SWING_AMP) * math.cos(angle + math.pi)

    # Knee Bend Angles: Knee bends most during the mid-swing phase.
    # The (0.5 - 0.5 * cos(2 * angle)) function creates two symmetrical bends per cycle.
    # Bend is a positive value, indicating flexion from a straight leg.
    knee_bend_R_val = math.radians(KNEE_BEND_AMP) * (0.5 - 0.5 * math.cos(2 * angle))
    knee_bend_L_val = math.radians(KNEE_BEND_AMP) * (0.5 - 0.5 * math.cos(2 * (angle + math.pi)))

    # Right Leg: Hip -> Knee -> Ankle
    # Upper leg (thigh) position: calculated from right hip and hip_swing_R
    r_knee_x = r_hip_x + UPPER_LEG_LENGTH * math.sin(hip_swing_R)
    r_knee_y = r_hip_y + UPPER_LEG_LENGTH * math.cos(hip_swing_R)
    joint_positions["r_knee"] = (r_knee_x, r_knee_y)

    # Lower leg (calf) position: calculated from right knee.
    # The calf's absolute angle from vertical is thigh's absolute angle minus knee bend (knee bends forward).
    calf_abs_angle_R = hip_swing_R - knee_bend_R_val
    r_ankle_x = r_knee_x + LOWER_LEG_LENGTH * math.sin(calf_abs_angle_R)
    r_ankle_y = r_knee_y + LOWER_LEG_LENGTH * math.cos(calf_abs_angle_R)
    joint_positions["r_ankle"] = (r_ankle_x, r_ankle_y)

    # Left Leg: Hip -> Knee -> Ankle
    l_knee_x = l_hip_x + UPPER_LEG_LENGTH * math.sin(hip_swing_L)
    l_knee_y = l_hip_y + UPPER_LEG_LENGTH * math.cos(hip_swing_L)
    joint_positions["l_knee"] = (l_knee_x, l_knee_y)

    calf_abs_angle_L = hip_swing_L - knee_bend_L_val
    l_ankle_x = l_knee_x + LOWER_LEG_LENGTH * math.sin(calf_abs_angle_L)
    l_ankle_y = l_knee_y + LOWER_LEG_LENGTH * math.cos(calf_abs_angle_L)
    joint_positions["l_ankle"] = (l_ankle_x, l_ankle_y)

    # --- Arms Calculation ---
    # Arms swing opposite to the corresponding leg (e.g., right arm swings opposite to right leg).
    # If right leg is swinging backward (hip_swing_R is positive), right arm swings forward (arm_swing_R is negative).
    # This means arm phase is (angle + pi) relative to leg phase.
    arm_swing_R = math.radians(ARM_SWING_AMP) * math.cos(angle + math.pi)
    arm_swing_L = math.radians(ARM_SWING_AMP) * math.cos(angle)

    # Elbow Bend Angles: Slight flexion.
    elbow_bend_R_val = math.radians(ELBOW_BEND_AMP) * (0.5 - 0.5 * math.cos(2 * (angle + math.pi)))
    elbow_bend_L_val = math.radians(ELBOW_BEND_AMP) * (0.5 - 0.5 * math.cos(2 * angle))

    # Right Arm: Shoulder -> Elbow -> Wrist
    r_elbow_x = r_shoulder_x + UPPER_ARM_LENGTH * math.sin(arm_swing_R)
    r_elbow_y = r_shoulder_y + UPPER_ARM_LENGTH * math.cos(arm_swing_R)
    joint_positions["r_elbow"] = (r_elbow_x, r_elbow_y)

    # Forearm position: calculated from right elbow.
    # Forearm's absolute angle from vertical is upper arm's absolute angle minus elbow bend (elbow bends forward).
    forearm_abs_angle_R = arm_swing_R - elbow_bend_R_val
    r_wrist_x = r_elbow_x + FOREARM_LENGTH * math.sin(forearm_abs_angle_R)
    r_wrist_y = r_elbow_y + FOREARM_LENGTH * math.cos(forearm_abs_angle_R)
    joint_positions["r_wrist"] = (r_wrist_x, r_wrist_y)

    # Left Arm: Shoulder -> Elbow -> Wrist
    l_elbow_x = l_shoulder_x + UPPER_ARM_LENGTH * math.sin(arm_swing_L)
    l_elbow_y = l_shoulder_y + UPPER_ARM_LENGTH * math.cos(arm_swing_L)
    joint_positions["l_elbow"] = (l_elbow_x, l_elbow_y)

    forearm_abs_angle_L = arm_swing_L - elbow_bend_L_val
    l_wrist_x = l_elbow_x + FOREARM_LENGTH * math.sin(forearm_abs_angle_L)
    l_wrist_y = l_elbow_y + FOREARM_LENGTH * math.cos(forearm_abs_angle_L)
    joint_positions["l_wrist"] = (l_wrist_x, l_wrist_y)

    # --- Draw Points ---
    # Draw all 15 calculated points as white circles on the black background.
    for name, pos in joint_positions.items():
        radius = POINT_RADIUS
        if name == "head":
            radius = HEAD_POINT_RADIUS  # Head point is slightly larger
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), radius)

    # --- Update Display ---
    pygame.display.flip()
    frame_count += 1
    clock.tick(FPS)

pygame.quit()
