
import pygame
import numpy as np

# Pygame initialization
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man Walking with Heavy Weight")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
clock = pygame.time.Clock()
FPS = 60
DOT_RADIUS = 7

# Biomechanical model parameters for a "sad man with heavy weight"
# Proportions (scaled for the screen)
SCALE = 2.5
NECK_LENGTH = 25 * SCALE
SHOULDER_WIDTH = 50 * SCALE
TORSO_LENGTH = 60 * SCALE
HIP_WIDTH = 40 * SCALE
UPPER_ARM_LENGTH = 50 * SCALE
LOWER_ARM_LENGTH = 45 * SCALE
THIGH_LENGTH = 60 * SCALE
LOWER_LEG_LENGTH = 55 * SCALE

# Motion characteristics for "sad/heavy" style
CYCLE_SPEED = 0.035  # Slow, heavy pace
FORWARD_LEAN = np.pi / 11 # Leaning forward as if under a burden
HEAD_TILT = np.pi / 9     # Head bowed down in sadness/effort
SHOULDER_SLUMP = 15       # Shoulders slumped down and slightly forward

# Amplitudes of motion (reduced for heavy/sad walk)
BOB_AMP = 3.5 * SCALE      # Pronounced vertical bobbing with each step
SWAY_AMP = 3.0 * SCALE     # Side-to-side sway from shifting weight
HIP_SWING_AMP = np.pi / 9  # Shorter strides
KNEE_BEND_AMP = np.pi / 5  # Reduced knee bend, suggesting heavy/shuffling steps
ARM_SWING_AMP = np.pi / 14 # Limited, passive arm swing
ELBOW_BEND = np.pi / 7     # Limp, bent elbows
SHOULDER_ROT_AMP = np.pi / 32 # Subtle shoulder rotation

# Main animation loop variable
angle = 0

def calculate_points(t):
    """
    Calculates the 15 joint positions for a given time/angle t.
    The model is hierarchical, starting from the pelvis/torso center.
    The kinematics are tuned to represent a sad person walking with a heavy load.
    """
    points = {}

    # 1. Torso Root (Center of mass, between hips)
    # The entire figure is offset to be centered on the screen.
    base_x = WIDTH / 2
    base_y = HEIGHT / 2 + 70 # Lower center of gravity
    pelvis_x = base_x + SWAY_AMP * np.sin(t)
    pelvis_y = base_y + BOB_AMP * np.cos(2 * t)
    
    # 2. Spine, Neck, and Head (Slumped forward)
    torso_lean_angle = -np.pi / 2 - FORWARD_LEAN
    points['neck'] = np.array([pelvis_x, pelvis_y]) + np.array([TORSO_LENGTH * np.cos(torso_lean_angle), TORSO_LENGTH * np.sin(torso_lean_angle)])
    
    head_tilt_angle = torso_lean_angle - HEAD_TILT
    points['head'] = points['neck'] + np.array([NECK_LENGTH * np.cos(head_tilt_angle), NECK_LENGTH * np.sin(head_tilt_angle)])
    
    # A mid-torso point to match the visual structure of having a dot on the torso
    points['mid_torso'] = (np.array([pelvis_x, pelvis_y]) + points['neck']) / 2
    
    # 3. Hips (Relative to pelvis, with slight vertical motion for weight shift)
    hip_lift_amp = 1.8 * SCALE
    points['l_hip'] = np.array([pelvis_x, pelvis_y]) + np.array([-HIP_WIDTH / 2, hip_lift_amp * np.cos(t + np.pi)])
    points['r_hip'] = np.array([pelvis_x, pelvis_y]) + np.array([HIP_WIDTH / 2, hip_lift_amp * np.cos(t)])

    # 4. Legs (Walking motion with short, heavy strides)
    # Left Leg
    l_thigh_angle = HIP_SWING_AMP * np.sin(t)
    l_knee_bend = KNEE_BEND_AMP * (np.cos(t) + 1) / 2 # Knee bends most mid-swing
    l_lower_leg_angle = l_thigh_angle + l_knee_bend
    points['l_knee'] = points['l_hip'] + np.array([THIGH_LENGTH * np.sin(l_thigh_angle), THIGH_LENGTH * np.cos(l_thigh_angle)])
    points['l_ankle'] = points['l_knee'] + np.array([LOWER_LEG_LENGTH * np.sin(l_lower_leg_angle), LOWER_LEG_LENGTH * np.cos(l_lower_leg_angle)])

    # Right Leg (phase-shifted)
    r_thigh_angle = HIP_SWING_AMP * np.sin(t + np.pi)
    r_knee_bend = KNEE_BEND_AMP * (np.cos(t + np.pi) + 1) / 2
    r_lower_leg_angle = r_thigh_angle + r_knee_bend
    points['r_knee'] = points['r_hip'] + np.array([THIGH_LENGTH * np.sin(r_thigh_angle), THIGH_LENGTH * np.cos(r_thigh_angle)])
    points['r_ankle'] = points['r_knee'] + np.array([LOWER_LEG_LENGTH * np.sin(r_lower_leg_angle), LOWER_LEG_LENGTH * np.cos(r_lower_leg_angle)])

    # 5. Shoulders (Slumped and rotating opposite to hips)
    shoulder_rot_angle = SHOULDER_ROT_AMP * np.sin(t + np.pi / 2)
    l_shoulder_pos = np.array([-SHOULDER_WIDTH / 2 * np.cos(shoulder_rot_angle), SHOULDER_SLUMP - SHOULDER_WIDTH / 2 * np.sin(shoulder_rot_angle)])
    r_shoulder_pos = np.array([SHOULDER_WIDTH / 2 * np.cos(shoulder_rot_angle), SHOULDER_SLUMP + SHOULDER_WIDTH / 2 * np.sin(shoulder_rot_angle)])
    points['l_shoulder'] = points['neck'] + l_shoulder_pos
    points['r_shoulder'] = points['neck'] + r_shoulder_pos

    # 6. Arms (Passive swing, bent elbows)
    # Left Arm
    l_arm_swing_angle = ARM_SWING_AMP * np.sin(t + np.pi) # Swings with right leg
    l_elbow_angle = l_arm_swing_angle + ELBOW_BEND
    points['l_elbow'] = points['l_shoulder'] + np.array([UPPER_ARM_LENGTH * np.sin(l_arm_swing_angle), UPPER_ARM_LENGTH * np.cos(l_arm_swing_angle)])
    points['l_wrist'] = points['l_elbow'] + np.array([LOWER_ARM_LENGTH * np.sin(l_elbow_angle), LOWER_ARM_LENGTH * np.cos(l_elbow_angle)])
    
    # Right Arm
    r_arm_swing_angle = ARM_SWING_AMP * np.sin(t) # Swings with left leg
    r_elbow_angle = r_arm_swing_angle + ELBOW_BEND
    points['r_elbow'] = points['r_shoulder'] + np.array([UPPER_ARM_LENGTH * np.sin(r_arm_swing_angle), UPPER_ARM_LENGTH * np.cos(r_arm_swing_angle)])
    points['r_wrist'] = points['r_elbow'] + np.array([LOWER_ARM_LENGTH * np.sin(r_elbow_angle), LOWER_ARM_LENGTH * np.cos(r_elbow_angle)])
    
    # The final list of 15 points, matching the requested stimulus format.
    # This structure (head, neck, torso, shoulders, limbs) is a standard representation.
    final_points = [
        points['head'],
        points['neck'],
        points['mid_torso'],
        points['l_shoulder'],
        points['r_shoulder'],
        points['l_elbow'],
        points['r_elbow'],
        points['l_wrist'],
        points['r_wrist'],
        points['l_hip'],
        points['r_hip'],
        points['l_knee'],
        points['r_knee'],
        points['l_ankle'],
        points['r_ankle'],
    ]

    return final_points

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation angle to drive the cyclical motion
    angle += CYCLE_SPEED
    if angle > 2 * np.pi:
        angle -= 2 * np.pi

    # Calculate current point positions based on the angle
    joint_positions = calculate_points(angle)

    # Drawing phase
    screen.fill(BLACK)
    for pos in joint_positions:
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), DOT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate for smooth, consistent animation speed
    clock.tick(FPS)

pygame.quit()
