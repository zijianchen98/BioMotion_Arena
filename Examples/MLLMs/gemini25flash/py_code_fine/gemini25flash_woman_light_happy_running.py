
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Stimulus - Running Woman")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point properties
POINT_RADIUS = 5

# Animation parameters
FPS = 60
RUN_CYCLE_DURATION_SEC = 0.7  # Duration of one full stride cycle (e.g., 0.7 seconds for a typical run)

# Body segment lengths in pixels (approximate for a person ~250-300 pixels tall)
P_HEIGHT_TOTAL = 280 # Total height of the person from head to ankle in resting pose

SEGMENT_LENGTHS = {
    'torso_neck_to_mid': P_HEIGHT_TOTAL * 0.1,  # Neck to mid-torso
    'torso_mid_to_pelvis': P_HEIGHT_TOTAL * 0.1, # Mid-torso to pelvis (Pelvis is point 3)
    'neck_to_head': P_HEIGHT_TOTAL * 0.05,      # Neck point to head point
    'head_radius': P_HEIGHT_TOTAL * 0.04,       # For visual head point placement
    'shoulder_offset_y': P_HEIGHT_TOTAL * 0.01, # Shoulders slightly below neck point
    'shoulder_width_half': P_HEIGHT_TOTAL * 0.08, # Half the shoulder width
    'upper_arm': P_HEIGHT_TOTAL * 0.14,
    'forearm': P_HEIGHT_TOTAL * 0.12,
    'hip_offset_x': P_HEIGHT_TOTAL * 0.05,      # Half hip width for hip points relative to pelvis center
    'thigh': P_HEIGHT_TOTAL * 0.22,
    'shank': P_HEIGHT_TOTAL * 0.22,
}

# Animation amplitudes and angles
VERTICAL_BOB_AMPLITUDE = 12       # Max vertical movement of pelvis base
ARM_SWING_DEG = 35                # Max arm swing angle from vertical (forwards/backwards)
ELBOW_BEND_DEG_MIN = 30           # Min elbow bend (straighter)
ELBOW_BEND_DEG_MAX = 80           # Max elbow bend (more bent)
LEG_HIP_SWING_DEG = 35            # Max hip swing angle from vertical (forward/backward)
KNEE_BEND_DEG_MIN = 5             # Min knee bend (straighter)
KNEE_BEND_DEG_MAX = 110           # Max knee bend (more bent, during recovery)

# Initial position for the 'center' of the person (e.g., mid-pelvis)
# The figure will be centered horizontally and placed vertically.
INITIAL_PELVIS_X = WIDTH / 2
INITIAL_PELVIS_Y = HEIGHT - (P_HEIGHT_TOTAL * 0.4) # Place pelvis point about 40% up from bottom of screen for centering

# Frame counter
frame_count = 0

def get_points(frame):
    current_time = frame / FPS
    # Cycle progress from 0.0 to 1.0 (repeats every RUN_CYCLE_DURATION_SEC)
    cycle_progress = (current_time % RUN_CYCLE_DURATION_SEC) / RUN_CYCLE_DURATION_SEC
    
    # Vertical bobbing (up and down motion of the whole body)
    # The body bobs up twice per stride cycle (e.g., at each mid-stance phase).
    vertical_bob = VERTICAL_BOB_AMPLITUDE * math.sin(cycle_progress * 4 * math.pi)

    # Base reference point: Pelvis. This point moves slightly up/down.
    # The figure as a whole stays centered horizontally.
    p_pelvis_x = INITIAL_PELVIS_X
    p_pelvis_y = INITIAL_PELVIS_Y + vertical_bob

    # Define the 15 points based on a common point-light representation:
    # 1. Head
    # 2. Neck
    # 3. Pelvis (central point, where hips attach)
    # 4. Right Shoulder
    # 5. Left Shoulder
    # 6. Right Elbow
    # 7. Left Elbow
    # 8. Right Wrist
    # 9. Left Wrist
    # 10. Right Hip
    # 11. Left Hip
    # 12. Right Knee
    # 13. Left Knee
    # 14. Right Ankle
    # 15. Left Ankle

    # --- Torso and Head points ---
    # Point 2: Neck
    # The 'neck' point is placed above the pelvis and is used as the base for shoulders and head.
    p_neck = [p_pelvis_x, p_pelvis_y - SEGMENT_LENGTHS['torso_mid_to_pelvis'] - SEGMENT_LENGTHS['torso_neck_to_mid']]
    
    # Point 1: Head
    p_head = [p_pelvis_x, p_neck[1] - SEGMENT_LENGTHS['neck_to_head'] - SEGMENT_LENGTHS['head_radius']]

    # --- Arm kinematics ---
    # `leg_phase` governs the main cycle for both legs and arms.
    # Varies 0 to 2pi over one stride.
    leg_phase = cycle_progress * 2 * math.pi 

    # Arm swing angles: (Positive angle is forward, negative is back relative to vertical)
    # Right arm swings back when right leg swings forward.
    # When `leg_phase` is 0 (right leg back), `cos(0)=1` (arm forward).
    # When `leg_phase` is `pi` (right leg forward), `cos(pi)=-1` (arm back).
    arm_angle_right = ARM_SWING_DEG * math.cos(leg_phase) 
    arm_angle_left  = ARM_SWING_DEG * math.cos(leg_phase + math.pi) # Opposite phase
    arm_angle_right_rad = math.radians(arm_angle_right)
    arm_angle_left_rad  = math.radians(arm_angle_left)

    # Elbow bend: More bend during mid-swing, straighter at extremes of arm swing.
    # This formula creates two peaks of max bend per arm cycle.
    elbow_bend_right_deg = ELBOW_BEND_DEG_MIN + (ELBOW_BEND_DEG_MAX - ELBOW_BEND_DEG_MIN) * (0.5 + 0.5 * math.sin(leg_phase * 2 - math.pi/2))
    elbow_bend_left_deg  = ELBOW_BEND_DEG_MIN + (ELBOW_BEND_DEG_MAX - ELBOW_BEND_DEG_MIN) * (0.5 + 0.5 * math.sin((leg_phase + math.pi) * 2 - math.pi/2))
    elbow_bend_right_rad = math.radians(elbow_bend_right_deg)
    elbow_bend_left_rad  = math.radians(elbow_bend_left_deg)
    
    # Point 4: Right Shoulder
    shoulder_y = p_neck[1] + SEGMENT_LENGTHS['shoulder_offset_y']
    p_r_shoulder = [p_neck[0] + SEGMENT_LENGTHS['shoulder_width_half'], shoulder_y]
    
    # Point 5: Left Shoulder
    p_l_shoulder = [p_neck[0] - SEGMENT_LENGTHS['shoulder_width_half'], shoulder_y]

    # Point 6: Right Elbow
    p_r_elbow = [
        p_r_shoulder[0] + SEGMENT_LENGTHS['upper_arm'] * math.sin(arm_angle_right_rad),
        p_r_shoulder[1] + SEGMENT_LENGTHS['upper_arm'] * math.cos(arm_angle_right_rad)
    ]
    # Point 8: Right Wrist
    p_r_wrist = [
        p_r_elbow[0] + SEGMENT_LENGTHS['forearm'] * math.sin(arm_angle_right_rad + elbow_bend_right_rad),
        p_r_elbow[1] + SEGMENT_LENGTHS['forearm'] * math.cos(arm_angle_right_rad + elbow_bend_right_rad)
    ]

    # Point 7: Left Elbow
    p_l_elbow = [
        p_l_shoulder[0] + SEGMENT_LENGTHS['upper_arm'] * math.sin(arm_angle_left_rad),
        p_l_shoulder[1] + SEGMENT_LENGTHS['upper_arm'] * math.cos(arm_angle_left_rad)
    ]
    # Point 9: Left Wrist
    p_l_wrist = [
        p_l_elbow[0] + SEGMENT_LENGTHS['forearm'] * math.sin(arm_angle_left_rad + elbow_bend_left_rad),
        p_l_elbow[1] + SEGMENT_LENGTHS['forearm'] * math.cos(arm_angle_left_rad + elbow_bend_left_rad)
    ]

    # --- Leg kinematics ---
    hip_y_pos = p_pelvis_y # Hips are at the same y-level as pelvis for simplicity.

    # Point 10: Right Hip (offset from pelvis center)
    p_r_hip = [p_pelvis_x + SEGMENT_LENGTHS['hip_offset_x'], hip_y_pos]
    
    # Point 11: Left Hip (offset from pelvis center)
    p_l_hip = [p_pelvis_x - SEGMENT_LENGTHS['hip_offset_x'], hip_y_pos]

    # Leg swing angles: (Positive angle is forward, negative is back relative to vertical)
    # Right leg phase: 0 (back), pi (forward)
    hip_angle_right = -LEG_HIP_SWING_DEG * math.cos(leg_phase) 
    hip_angle_left  = -LEG_HIP_SWING_DEG * math.cos(leg_phase + math.pi) # Opposite phase
    hip_angle_right_rad = math.radians(hip_angle_right)
    hip_angle_left_rad  = math.radians(hip_angle_left)

    # Knee bend: Max bend during mid-swing recovery and at push-off/impact.
    # This formula creates two peaks of maximum knee bend per full stride cycle:
    # one when the leg is fully back and preparing to push-off/swing forward,
    # and another when the leg is fully forward and recovering/preparing for landing.
    knee_bend_right_deg = KNEE_BEND_DEG_MIN + (KNEE_BEND_DEG_MAX - KNEE_BEND_DEG_MIN) * (0.5 - 0.5 * math.cos(leg_phase * 2 - math.pi))
    knee_bend_left_deg  = KNEE_BEND_DEG_MIN + (KNEE_BEND_DEG_MAX - KNEE_BEND_DEG_MIN) * (0.5 - 0.5 * math.cos((leg_phase + math.pi) * 2 - math.pi))
    knee_bend_right_rad = math.radians(knee_bend_right_deg)
    knee_bend_left_rad  = math.radians(knee_bend_left_deg)
    
    # Point 12: Right Knee
    p_r_knee = [
        p_r_hip[0] + SEGMENT_LENGTHS['thigh'] * math.sin(hip_angle_right_rad),
        p_r_hip[1] + SEGMENT_LENGTHS['thigh'] * math.cos(hip_angle_right_rad)
    ]
    # Point 14: Right Ankle
    p_r_ankle = [
        p_r_knee[0] + SEGMENT_LENGTHS['shank'] * math.sin(hip_angle_right_rad + knee_bend_right_rad),
        p_r_knee[1] + SEGMENT_LENGTHS['shank'] * math.cos(hip_angle_right_rad + knee_bend_right_rad)
    ]

    # Point 13: Left Knee
    p_l_knee = [
        p_l_hip[0] + SEGMENT_LENGTHS['thigh'] * math.sin(hip_angle_left_rad),
        p_l_hip[1] + SEGMENT_LENGTHS['thigh'] * math.cos(hip_angle_left_rad)
    ]
    # Point 15: Left Ankle
    p_l_ankle = [
        p_l_knee[0] + SEGMENT_LENGTHS['shank'] * math.sin(hip_angle_left_rad + knee_bend_left_rad),
        p_l_knee[1] + SEGMENT_LENGTHS['shank'] * math.cos(hip_angle_left_rad + knee_bend_left_rad)
    ]

    # Collect all 15 points in a consistent order
    current_points = [
        p_head,         # 1. Head
        p_neck,         # 2. Neck
        p_pelvis,       # 3. Pelvis (central point, where hips attach)
        p_r_shoulder,   # 4. Right Shoulder
        p_l_shoulder,   # 5. Left Shoulder
        p_r_elbow,      # 6. Right Elbow
        p_l_elbow,      # 7. Left Elbow
        p_r_wrist,      # 8. Right Wrist
        p_l_wrist,      # 9. Left Wrist
        p_r_hip,        # 10. Right Hip
        p_l_hip,        # 11. Left Hip
        p_r_knee,       # 12. Right Knee
        p_l_knee,       # 13. Left Knee
        p_r_ankle,      # 14. Right Ankle
        p_l_ankle       # 15. Left Ankle
    ]

    return current_points

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    SCREEN.fill(BLACK)

    # Get current point positions
    points = get_points(frame_count)

    # Draw points
    for point in points:
        pygame.draw.circle(SCREEN, WHITE, (int(point[0]), int(point[1])), POINT_RADIUS)

    # Update display
    pygame.display.flip()

    # Increment frame count and control frame rate
    frame_count += 1
    clock.tick(FPS)

pygame.quit()
sys.exit()
