
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Heavy Man Walking")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5  # Size of the dots

# Animation parameters
FPS = 60
gait_cycle_duration_seconds = 1.6  # Duration of one full gait cycle (slower for "heavy weight")
gait_cycle_duration_frames = int(FPS * gait_cycle_duration_seconds)

# Biomechanical parameters (approximate ratios to body height for natural proportions)
# These are tuned to create a plausible walking motion.
BODY_HEIGHT = SCREEN_HEIGHT * 0.4  # Overall height of the person in pixels
HEAD_HEIGHT = BODY_HEIGHT * 0.12   # Approximate height of the head point above shoulders
TORSO_UPPER_LENGTH = BODY_HEIGHT * 0.15 # From torso_lower to torso_upper
TORSO_LOWER_LENGTH = BODY_HEIGHT * 0.15 # From torso_upper to neck/shoulder level (where shoulder points are)

HIP_WIDTH = BODY_HEIGHT * 0.12   # Horizontal distance between hip joints
SHOULDER_WIDTH = BODY_HEIGHT * 0.18 # Horizontal distance between shoulder joints

UPPER_ARM_LENGTH = BODY_HEIGHT * 0.18
FOREARM_LENGTH = BODY_HEIGHT * 0.15

THIGH_LENGTH = BODY_HEIGHT * 0.22
CALF_LENGTH = BODY_HEIGHT * 0.20

# Oscillation amplitudes and angles for motion
# Vertical oscillation of hip center (for body bobbing)
HIP_Y_OSC_AMP = BODY_HEIGHT * 0.03 # Slightly more pronounced for "heavy"

# Arm swing angles
ARM_SWING_ANGLE_AMP = math.radians(35) # Max angle forward/backward from vertical
ARM_ELBOW_BEND_AMP = math.radians(15) # Max additional bend at elbow during swing

# Leg movement angles
HIP_LEG_ANGLE_AMP = math.radians(25) # Max angle forward/backward from vertical at hip
KNEE_BEND_ANGLE_AMP = math.radians(60) # Max additional bend at knee during swing
BASE_KNEE_BEND = math.radians(10) # Minimum knee bend (always slightly bent)

ANKLE_LIFT_AMP = BODY_HEIGHT * 0.02 # Vertical lift of foot during swing phase

# Define the 15 points and their initial relative positions.
# The 'torso_lower' point serves as the origin (0,0) of the local coordinate system
# from which all other points' positions are derived before global translation.
# Pygame's Y-axis increases downwards.

# Point mapping: head, shoulder_L, shoulder_R, elbow_L, elbow_R, wrist_L, wrist_R,
#                torso_upper, torso_lower, hip_L, hip_R, knee_L, knee_R, ankle_L, ankle_R

# Base Y positions relative to torso_lower (hip_center) in local space
base_rel_y = {
    'head': -(TORSO_UPPER_LENGTH + TORSO_LOWER_LENGTH + HEAD_HEIGHT),
    'torso_upper': -TORSO_UPPER_LENGTH,
    'torso_lower': 0,  # Reference point for local coordinates
    'shoulder_L': -(TORSO_UPPER_LENGTH + TORSO_LOWER_LENGTH),
    'shoulder_R': -(TORSO_UPPER_LENGTH + TORSO_LOWER_LENGTH),
    'hip_L': 0,
    'hip_R': 0,
}

# Base X positions relative to torso_lower (hip_center) in local space
base_rel_x = {
    'head': 0,
    'torso_upper': 0,
    'torso_lower': 0,
    'shoulder_L': -SHOULDER_WIDTH / 2,
    'shoulder_R': SHOULDER_WIDTH / 2,
    'hip_L': -HIP_WIDTH / 2,
    'hip_R': HIP_WIDTH / 2,
}

# Ordered list of point names to ensure exactly 15 points are drawn
point_names_ordered = [
    'head',
    'shoulder_L', 'shoulder_R',
    'elbow_L', 'elbow_R',
    'wrist_L', 'wrist_R',
    'torso_upper', 'torso_lower',
    'hip_L', 'hip_R',
    'knee_L', 'knee_R',
    'ankle_L', 'ankle_R'
]

# Animation loop variables
frame_count = 0
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Calculate current gait phase (0 to 2*pi radians)
    # This determines the exact pose within the walking cycle.
    phase = (frame_count % gait_cycle_duration_frames) / gait_cycle_duration_frames * (2 * math.pi)

    # Calculate global horizontal translation for the entire character
    # This makes the person appear to walk across the screen and loop.
    # The character moves one stride_length horizontally per full gait cycle.
    stride_length = BODY_HEIGHT * 0.6
    global_x_translation = (frame_count / gait_cycle_duration_frames) * stride_length
    
    # Loop the character's horizontal movement within a defined range on screen
    # This makes the character appear to walk back and forth or just re-appear.
    # For a continuous forward walk, uncomment the line below and remove the modulo and offset:
    # current_center_x = SCREEN_WIDTH // 2 + global_x_translation % (SCREEN_WIDTH * 1.5) - (SCREEN_WIDTH * 0.75)
    # Let's keep it mostly centered to emphasize the biological motion itself.
    x_walk_range = SCREEN_WIDTH * 0.5 # The character will walk across half the screen width
    current_center_x = SCREEN_WIDTH // 2 + (global_x_translation % x_walk_range) - (x_walk_range / 2)

    # Calculate the vertical bobbing of the main body (hip center)
    # The hip center is highest twice per cycle (at mid-stance for each leg).
    # `math.sin(2 * phase)` ensures two vertical oscillations per 2*pi cycle.
    center_y = SCREEN_HEIGHT // 2 + HIP_Y_OSC_AMP * math.sin(2 * phase)

    # Dictionary to store the calculated screen coordinates of each point
    current_points_coords = {}

    # Torso and Head Points
    # These points maintain their relative positions to the dynamic 'torso_lower' (hip center).
    current_points_coords['torso_lower'] = (current_center_x + base_rel_x['torso_lower'], center_y + base_rel_y['torso_lower'])
    current_points_coords['torso_upper'] = (current_center_x + base_rel_x['torso_upper'], center_y + base_rel_y['torso_upper'])
    current_points_coords['head'] = (current_center_x + base_rel_x['head'], center_y + base_rel_y['head'])

    # Shoulder Points
    # Shoulders are positioned relative to 'torso_upper'.
    current_points_coords['shoulder_L'] = (
        current_points_coords['torso_upper'][0] + base_rel_x['shoulder_L'],
        current_points_coords['torso_upper'][1] + (base_rel_y['shoulder_L'] - base_rel_y['torso_upper']) # Vertical offset from torso_upper
    )
    current_points_coords['shoulder_R'] = (
        current_points_coords['torso_upper'][0] + base_rel_x['shoulder_R'],
        current_points_coords['torso_upper'][1] + (base_rel_y['shoulder_R'] - base_rel_y['torso_upper'])
    )

    # Hip Points
    # Hips are positioned relative to 'torso_lower'.
    current_points_coords['hip_L'] = (
        current_points_coords['torso_lower'][0] + base_rel_x['hip_L'],
        current_points_coords['torso_lower'][1] + base_rel_y['hip_L']
    )
    current_points_coords['hip_R'] = (
        current_points_coords['torso_lower'][0] + base_rel_x['hip_R'],
        current_points_coords['torso_lower'][1] + base_rel_y['hip_R']
    )

    # Arm calculations: Angles are relative to the vertical axis (0 = pointing straight down).
    # Positive angle = clockwise (forward swing for right arm, backward for left arm).
    # Arms swing in opposition to legs: right arm swings with left leg, left arm with right leg.
    # Assuming phase=0 is roughly right leg forward, left leg back. So left arm should be forward.
    l_arm_swing_angle = ARM_SWING_ANGLE_AMP * math.cos(phase) # Max forward swing at phase 0
    r_arm_swing_angle = ARM_SWING_ANGLE_AMP * math.cos(phase + math.pi) # Max backward swing at phase 0

    # Elbow bend: Adds a natural flex to the arm, peaking twice per cycle (during max forward/backward swing)
    l_elbow_bend = ARM_ELBOW_BEND_AMP * (1 - math.cos(2 * phase)) / 2
    r_elbow_bend = ARM_ELBOW_BEND_AMP * (1 - math.cos(2 * phase + math.pi)) / 2

    # Right arm: Shoulder -> Elbow -> Wrist
    elbow_R_x = current_points_coords['shoulder_R'][0] + UPPER_ARM_LENGTH * math.sin(r_arm_swing_angle)
    elbow_R_y = current_points_coords['shoulder_R'][1] + UPPER_ARM_LENGTH * math.cos(r_arm_swing_angle)
    current_points_coords['elbow_R'] = (elbow_R_x, elbow_R_y)

    wrist_R_x = elbow_R_x + FOREARM_LENGTH * math.sin(r_arm_swing_angle + r_elbow_bend)
    wrist_R_y = elbow_R_y + FOREARM_LENGTH * math.cos(r_arm_swing_angle + r_elbow_bend)
    current_points_coords['wrist_R'] = (wrist_R_x, wrist_R_y)

    # Left arm: Shoulder -> Elbow -> Wrist
    elbow_L_x = current_points_coords['shoulder_L'][0] + UPPER_ARM_LENGTH * math.sin(l_arm_swing_angle)
    elbow_L_y = current_points_coords['shoulder_L'][1] + UPPER_ARM_LENGTH * math.cos(l_arm_swing_angle)
    current_points_coords['elbow_L'] = (elbow_L_x, elbow_L_y)

    wrist_L_x = elbow_L_x + FOREARM_LENGTH * math.sin(l_arm_swing_angle + l_elbow_bend)
    wrist_L_y = elbow_L_y + FOREARM_LENGTH * math.cos(l_arm_swing_angle + l_elbow_bend)
    current_points_coords['wrist_L'] = (wrist_L_x, wrist_L_y)

    # Leg calculations: Angles are relative to the vertical axis.
    # Right leg swing: `HIP_LEG_ANGLE_AMP * cos(phase)` (forward at phase 0, backward at phase pi)
    # Left leg swing: `HIP_LEG_ANGLE_AMP * cos(phase + pi)` (backward at phase 0, forward at phase pi)
    r_hip_angle_swing = HIP_LEG_ANGLE_AMP * math.cos(phase)
    l_hip_angle_swing = HIP_LEG_ANGLE_AMP * math.cos(phase + math.pi)

    # Knee bend: Max bend during swing phase (when leg is lifted and moving forward/backward)
    # The (1+sin)/2 or (1-cos)/2 patterns create a smooth 0-1 range peaking once or twice per cycle.
    # Right leg's peak bend occurs when it's in its swing phase (roughly phase=pi to 2pi).
    r_knee_bend_total = BASE_KNEE_BEND + KNEE_BEND_ANGLE_AMP * (1 + math.sin(phase - math.pi/2)) / 2
    # Left leg's peak bend occurs during its swing phase (roughly phase=0 to pi).
    l_knee_bend_total = BASE_KNEE_BEND + KNEE_BEND_ANGLE_AMP * (1 + math.sin(phase + math.pi/2)) / 2

    # Ankle lift: Foot lifts off the ground during swing phase to clear the ground.
    # Right leg lifts off around phase = pi (toe-off) and lands around phase = 2pi (heel strike).
    # So peak lift for right leg is around phase = 3pi/2 (mid-swing).
    r_ankle_lift_amount = ANKLE_LIFT_AMP * (1 + math.sin(phase - math.pi/2)) / 2
    # Left leg lifts off around phase = 0 (toe-off) and lands around phase = pi (heel strike).
    # So peak lift for left leg is around phase = pi/2 (mid-swing).
    l_ankle_lift_amount = ANKLE_LIFT_AMP * (1 + math.sin(phase + math.pi/2)) / 2

    # Right leg: Hip -> Knee -> Ankle
    knee_R_x = current_points_coords['hip_R'][0] + THIGH_LENGTH * math.sin(r_hip_angle_swing)
    knee_R_y = current_points_coords['hip_R'][1] + THIGH_LENGTH * math.cos(r_hip_angle_swing)
    current_points_coords['knee_R'] = (knee_R_x, knee_R_y)

    ankle_R_x = knee_R_x + CALF_LENGTH * math.sin(r_hip_angle_swing + r_knee_bend_total)
    ankle_R_y = knee_R_y + CALF_LENGTH * math.cos(r_hip_angle_swing + r_knee_bend_total)
    current_points_coords['ankle_R'] = (ankle_R_x, ankle_R_y - r_ankle_lift_amount) # Subtract lift amount to move ankle up

    # Left leg: Hip -> Knee -> Ankle
    knee_L_x = current_points_coords['hip_L'][0] + THIGH_LENGTH * math.sin(l_hip_angle_swing)
    knee_L_y = current_points_coords['hip_L'][1] + THIGH_LENGTH * math.cos(l_hip_angle_swing)
    current_points_coords['knee_L'] = (knee_L_x, knee_L_y)

    ankle_L_x = knee_L_x + CALF_LENGTH * math.sin(l_hip_angle_swing + l_knee_bend_total)
    ankle_L_y = knee_L_y + CALF_LENGTH * math.cos(l_hip_angle_swing + l_knee_bend_total)
    current_points_coords['ankle_L'] = (ankle_L_x, ankle_L_y - l_ankle_lift_amount) # Subtract lift amount to move ankle up

    # Draw all 15 points
    for point_name in point_names_ordered:
        pos = current_points_coords[point_name]
        # Ensure coordinates are integers for drawing
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Increment frame count and control frame rate
    frame_count += 1
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
