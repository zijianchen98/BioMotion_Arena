
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Running Man")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5 # Size of each point-light

# Animation parameters
FPS = 60 # Frames per second
animation_frame = 0
# A full stride cycle (e.g., left leg completes its swing, then right leg completes its swing).
# This value determines the perceived speed and smoothness of the animation.
FRAMES_PER_CYCLE = 60 # One second per full stride at 60 FPS

# Define relative "neutral" positions for 15 body points
# All coordinates are relative to the 'pelvis' point (0,0), which acts as the central reference.
# Y is positive downwards, X is positive rightwards.
# These values are chosen to approximate typical human proportions.
neutral_pose_points = {
    'head': (0, -150),       # Top of the head
    'neck': (0, -120),       # Base of the neck/C7 vertebra
    'shoulder_L': (-40, -100), # Left shoulder joint
    'shoulder_R': (40, -100),  # Right shoulder joint
    'elbow_L': (-60, -50),   # Left elbow joint (slightly bent forward)
    'elbow_R': (60, -50),    # Right elbow joint (slightly bent forward)
    'wrist_L': (-70, 0),     # Left wrist joint
    'wrist_R': (70, 0),      # Right wrist joint
    'pelvis': (0, 0),        # Center of the hips/sacrum - our animation origin
    'hip_L': (-20, 20),      # Left hip joint
    'hip_R': (20, 20),       # Right hip joint
    'knee_L': (-30, 80),     # Left knee joint
    'knee_R': (30, 80),      # Right knee joint
    'ankle_L': (-40, 140),   # Left ankle joint
    'ankle_R': (40, 140),    # Right ankle joint
}

# Motion parameters for running (amplitudes and phase offsets for sine waves)
# These are heuristic values chosen to create a visually plausible running motion.
motion_params = {
    # Overall body bounce (vertical oscillation of the torso)
    'body_bounce_amp': 15, # Vertical amplitude of the whole body
    'body_sway_amp_x': 5,  # Slight horizontal sway

    # Arm swing (arms typically swing opposite to legs)
    'arm_swing_amp_x': 40, # Horizontal amplitude of wrist/elbow swing
    'arm_swing_amp_y': 15, # Vertical amplitude of wrist/elbow swing
    'arm_bend_intensity': 1.5, # Controls how much elbow/wrist bend dynamically
    'arm_phase_offset': math.pi, # Arms counter-phase to legs (180 degrees difference)

    # Leg swing and knee/ankle bending
    'leg_swing_amp_x': 55, # Horizontal amplitude of hip/knee/ankle swing
    'leg_swing_amp_y': 25, # Hip vertical movement during swing (e.g., knee drive)
    'knee_bend_amp_y': 45, # How much knee drops/bends during swing
    'ankle_lift_amp_y': 35, # How much ankle lifts during swing (foot clearance)
}

# Main animation loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(BLACK) # Clear the screen with a black background

    # Calculate time parameter for current frame: 't' ranges from 0 to 2*PI over one full cycle
    t = (animation_frame % FRAMES_PER_CYCLE) / FRAMES_PER_CYCLE * (2 * math.pi)

    # Base position for the entire figure on screen: centered horizontally, slightly above vertical center
    center_x = WIDTH // 2
    display_y_offset = HEIGHT // 2 + 50 # Shifts the figure downwards slightly for better vertical placement

    # Dictionary to store calculated positions for the current frame
    current_positions = {}

    # --- Calculate dynamic positions for each point ---
    # Each point's position is calculated based on its neutral pose, plus time-varying offsets.

    # 1. Pelvis (Central body point)
    # Represents the overall body bounce (up/down movement) and slight horizontal sway
    pelvis_current_pos = (
        center_x + motion_params['body_sway_amp_x'] * math.sin(t + math.pi/2), # Slight side-to-side sway
        display_y_offset + neutral_pose_points['pelvis'][1] + motion_params['body_bounce_amp'] * math.sin(t)
    )
    current_positions['pelvis'] = pelvis_current_pos

    # 2. Head & Neck
    # Head and neck follow the body bounce, but with reduced amplitude and a slight phase shift for natural head stabilization
    head_neck_y_offset = 0.5 * motion_params['body_bounce_amp'] * math.sin(t + math.pi/4)
    current_positions['head'] = (
        pelvis_current_pos[0] + neutral_pose_points['head'][0],
        pelvis_current_pos[1] + neutral_pose_points['head'][1] + head_neck_y_offset
    )
    current_positions['neck'] = (
        pelvis_current_pos[0] + neutral_pose_points['neck'][0],
        pelvis_current_pos[1] + neutral_pose_points['neck'][1] + head_neck_y_offset
    )

    # 3. Shoulders (follow the body bounce)
    shoulder_y_offset_main = motion_params['body_bounce_amp'] * math.sin(t)
    current_positions['shoulder_L'] = (
        pelvis_current_pos[0] + neutral_pose_points['shoulder_L'][0],
        pelvis_current_pos[1] + neutral_pose_points['shoulder_L'][1] + shoulder_y_offset_main
    )
    current_positions['shoulder_R'] = (
        pelvis_current_pos[0] + neutral_pose_points['shoulder_R'][0],
        pelvis_current_pos[1] + neutral_pose_points['shoulder_R'][1] + shoulder_y_offset_main
    )

    # 4. Arms (Left and Right arms swing out of phase with each other, and generally opposite to the legs)
    # The right arm swings forward when 't' is near 0, while the left arm swings backward.
    arm_phase_R = t
    arm_phase_L = t + motion_params['arm_phase_offset']

    for side in ['L', 'R']:
        phase = arm_phase_L if side == 'L' else arm_phase_R
        shoulder_pos = current_positions[f'shoulder_{side}']

        # Calculate initial offsets from the shoulder for the elbow and wrist
        initial_elbow_x_offset = neutral_pose_points[f'elbow_{side}'][0] - neutral_pose_points[f'shoulder_{side}'][0]
        initial_elbow_y_offset = neutral_pose_points[f'elbow_{side}'][1] - neutral_pose_points[f'shoulder_{side}'][1]
        initial_wrist_x_offset = neutral_pose_points[f'wrist_{side}'][0] - neutral_pose_points[f'shoulder_{side}'][0]
        initial_wrist_y_offset = neutral_pose_points[f'wrist_{side}'][1] - neutral_pose_points[f'shoulder_{side}'][1]

        # X movement for arm swing (forward/backward motion)
        # Multiplier (1 for R, -1 for L) ensures opposite swings
        arm_x_swing = motion_params['arm_swing_amp_x'] * math.cos(phase) * (1 if side == 'R' else -1)
        # Y movement for arm (slight up/down motion during swing, contributes to elbow bend effect)
        arm_y_swing = motion_params['arm_swing_amp_y'] * math.sin(phase)

        # Elbow position: combines initial relative position with dynamic swing and bend
        # The (1 - math.sin(phase * 2)) term creates a bending motion (y-drop) more pronounced during the swing.
        current_positions[f'elbow_{side}'] = (
            shoulder_pos[0] + initial_elbow_x_offset + arm_x_swing,
            shoulder_pos[1] + initial_elbow_y_offset + arm_y_swing + motion_params['arm_bend_intensity'] * (1 - math.sin(phase * 2))
        )

        # Wrist position: follows elbow's general motion but with larger amplitude due to leverage
        current_positions[f'wrist_{side}'] = (
            shoulder_pos[0] + initial_wrist_x_offset + arm_x_swing * 1.5,
            shoulder_pos[1] + initial_wrist_y_offset + arm_y_swing * 1.5 + motion_params['arm_bend_intensity'] * 1.5 * (1 - math.sin(phase * 2))
        )
            
    # 5. Hips (positions relative to pelvis)
    # The right leg swings forward when 't' is near 0, and the left leg is backward.
    leg_phase_R = t
    leg_phase_L = t + motion_params['arm_phase_offset'] # Legs are 180 degrees out of phase

    for side in ['L', 'R']:
        phase = leg_phase_L if side == 'L' else leg_phase_R
        
        # X movement for hip swing (forward/backward motion)
        hip_x_swing = motion_params['leg_swing_amp_x'] * math.sin(phase) * (1 if side == 'R' else -1)
        # Vertical movement of hip due to weight shift and leg extension (hip rises during push-off/swing-through)
        hip_y_swing = motion_params['leg_swing_amp_y'] * (1 - math.cos(phase * 2))

        current_positions[f'hip_{side}'] = (
            pelvis_current_pos[0] + neutral_pose_points[f'hip_{side}'][0] + hip_x_swing,
            pelvis_current_pos[1] + neutral_pose_points[f'hip_{side}'][1] + hip_y_swing
        )
    
    # 6. Knees (positions relative to hips, with dynamic bending)
    for side in ['L', 'R']:
        phase = leg_phase_L if side == 'L' else leg_phase_R
        hip_pos = current_positions[f'hip_{side}']

        # Initial offset from hip to knee
        initial_knee_x_offset = neutral_pose_points[f'knee_{side}'][0] - neutral_pose_points[f'hip_{side}'][0]
        initial_knee_y_offset = neutral_pose_points[f'knee_{side}'][1] - neutral_pose_points[f'hip_{side}'][1]

        # X movement for knee (follows hip swing, generally slightly less pronounced)
        knee_x_swing = motion_params['leg_swing_amp_x'] * 0.7 * math.sin(phase) * (1 if side == 'R' else -1)
        # Y movement for knee bending (strong bend during the swing phase, causing the knee to drop)
        # (1 + math.cos(phase * 2 + math.pi)) makes it drop most when leg is at extremes of swing.
        knee_y_bend = motion_params['knee_bend_amp_y'] * (1 + math.cos(phase * 2 + math.pi))

        current_positions[f'knee_{side}'] = (
            hip_pos[0] + initial_knee_x_offset + knee_x_swing,
            hip_pos[1] + initial_knee_y_offset + knee_y_bend
        )

    # 7. Ankles (positions relative to knees, with foot lift during swing)
    for side in ['L', 'R']:
        phase = leg_phase_L if side == 'L' else leg_phase_R
        knee_pos = current_positions[f'knee_{side}']

        # Initial offset from knee to ankle
        initial_ankle_x_offset = neutral_pose_points[f'ankle_{side}'][0] - neutral_pose_points[f'knee_{side}'][0]
        initial_ankle_y_offset = neutral_pose_points[f'ankle_{side}'][1] - neutral_pose_points[f'knee_{side}'][1]
        
        # X movement for ankle (follows knee/hip swing, with a slight phase lead/lag for foot strike)
        ankle_x_swing = motion_params['leg_swing_amp_x'] * 0.5 * math.sin(phase + math.pi/4) * (1 if side == 'R' else -1)
        # Y movement for foot lift (lifts during the swing phase, touches ground during stance phase)
        ankle_y_lift = motion_params['ankle_lift_amp_y'] * (1 - math.cos(phase * 2)) # Lifts when leg is swinging forward

        current_positions[f'ankle_{side}'] = (
            knee_pos[0] + initial_ankle_x_offset + ankle_x_swing,
            knee_pos[1] + initial_ankle_y_offset + ankle_y_lift
        )
            
    # Draw all 15 points on the screen
    # Iterate through the defined point names to ensure all 15 points are drawn.
    for point_name in neutral_pose_points.keys():
        pos = current_positions.get(point_name)
        if pos:
            # Draw a white circle for each point-light
            pygame.draw.circle(SCREEN, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)

    # Update the full display Surface to the screen
    pygame.display.flip()

    # Increment animation frame and control the frame rate
    animation_frame += 1
    clock.tick(FPS)

# Uninitialize Pygame and exit
pygame.quit()
