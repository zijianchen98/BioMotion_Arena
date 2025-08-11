
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sadman Running with Heavy Weight")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
DOT_RADIUS = 5

# Animation parameters
FPS = 60
gait_cycle_duration = 2.0  # Seconds per full gait cycle (slower for heavy/sad)
figure_horizontal_speed = 1.0  # Pixels per frame the entire figure moves horizontally

# Biomechanical parameters (adjusted for "sadman with heavy weight")
# These are relative amplitudes and offsets for a running gait, tuned for the specific request.

# Torso/Pelvis motion
vertical_bob_amplitude = 25    # More pronounced vertical movement for "heavy"
forward_lean_angle = math.radians(-8) # Slight forward lean for running and "heavy"
overall_y_offset = 60          # Lower overall posture for "sadman" and "heavy"

# Arm motion (less energetic for "sadman", more contained for "heavy")
arm_swing_amplitude = math.radians(25)  # Reduced swing
elbow_bend_angle = math.radians(70)     # Elbows stay more bent
wrist_offset_forward = 10               # Slight forward bias for wrists

# Leg motion (shorter stride, more bent knees, less "bounce" for "heavy")
hip_swing_amplitude = math.radians(35)  # Shorter stride for "heavy"
base_knee_bend = math.radians(40)       # Always have a base bend for running/heavy
knee_bend_amplitude = math.radians(30)  # Amplitude of additional knee bend
ankle_lift_amplitude = 20               # How much ankle lifts during swing (reduced for "heavy")

# Segment lengths (approximate, relative to a scale factor from a typical human figure)
SCALE = 0.85 # Scale down the whole figure slightly, based on visual reference
segment_lengths = {
    'torso_length': 100 * SCALE, # Spine_pelvis to neck_base
    'head_length': 30 * SCALE,   # Neck_base to head
    'shoulder_width': 90 * SCALE, # Distance between shoulders
    'upper_arm': 50 * SCALE,
    'lower_arm': 50 * SCALE,
    'pelvis_width': 50 * SCALE,  # Distance between hips
    'thigh': 80 * SCALE,
    'shin': 80 * SCALE,
}

# Initial position of the entire figure's reference point (e.g., pelvis center)
# This will be `spine_pelvis`
global_figure_center_x = WIDTH // 2
global_figure_center_y = HEIGHT // 2 + overall_y_offset # Offset downwards for lower posture

# Animation state variables
time_elapsed = 0.0

def calculate_current_pose(t):
    global global_figure_center_x

    current_pose = {}

    # Normalize time for a single gait cycle (0 to 1)
    # The gait cycle starts from 0 to `gait_cycle_duration` seconds
    t_norm = (t % gait_cycle_duration) / gait_cycle_duration

    # 1. Overall figure horizontal movement (continuous scrolling)
    global_figure_center_x = (global_figure_center_x + figure_horizontal_speed)
    if global_figure_center_x > WIDTH + 100: # Wrap around to create continuous animation
        global_figure_center_x = -100

    # 2. Torso motion (vertical bob and slight forward lean)
    # Sinusoidal vertical bob, twice the frequency of gait cycle for running
    # Phase offset for vertical bob to align with running cycle (e.g., lowest at mid-stride)
    vertical_offset = vertical_bob_amplitude * (0.5 - 0.5 * math.cos(t_norm * 2 * math.pi * 2))
    
    # Pelvis center (`spine_pelvis` point) is our main reference point for the figure's base
    spine_pelvis_x = global_figure_center_x
    spine_pelvis_y = global_figure_center_y + vertical_offset
    current_pose['spine_pelvis'] = (spine_pelvis_x, spine_pelvis_y)

    # Torso points (Head, Neck Base) relative to spine_pelvis, with overall forward lean
    # Angles are measured from the positive Y-axis (downwards in Pygame) clockwise.
    # So, a forward lean (e.g., torso leaning forward) means a negative angle from the vertical.
    
    # Neck Base calculation
    neck_base_x = spine_pelvis_x + segment_lengths['torso_length'] * math.sin(forward_lean_angle)
    neck_base_y = spine_pelvis_y - segment_lengths['torso_length'] * math.cos(forward_lean_angle) # Y is inverted, so subtraction for upward
    current_pose['neck_base'] = (neck_base_x, neck_base_y)

    # Head calculation (relative to neck_base)
    head_x = neck_base_x + segment_lengths['head_length'] * math.sin(forward_lean_angle)
    head_y = neck_base_y - segment_lengths['head_length'] * math.cos(forward_lean_angle)
    current_pose['head'] = (head_x, head_y)

    # Shoulders (relative to neck_base, perpendicular to torso line, adjusted for lean)
    # Shoulder positions are calculated by rotating the static offsets around neck_base.
    shoulder_offset_x_static = segment_lengths['shoulder_width'] / 2
    shoulder_offset_y_static = 0 # Assume shoulders are horizontal from neck_base initially

    # Apply the forward_lean_angle to shoulder positions relative to neck_base
    # Right shoulder (positive X offset from central axis):
    right_shoulder_x = neck_base_x + shoulder_offset_x_static * math.cos(forward_lean_angle) - shoulder_offset_y_static * math.sin(forward_lean_angle)
    right_shoulder_y = neck_base_y + shoulder_offset_x_static * math.sin(forward_lean_angle) + shoulder_offset_y_static * math.cos(forward_lean_angle)
    current_pose['right_shoulder'] = (right_shoulder_x, right_shoulder_y)

    # Left shoulder (negative X offset from central axis):
    left_shoulder_x = neck_base_x - shoulder_offset_x_static * math.cos(forward_lean_angle) - shoulder_offset_y_static * math.sin(forward_lean_angle)
    left_shoulder_y = neck_base_y - shoulder_offset_x_static * math.sin(forward_lean_angle) + shoulder_offset_y_static * math.cos(forward_lean_angle)
    current_pose['left_shoulder'] = (left_shoulder_x, left_shoulder_y)
    
    # Hips (relative to spine_pelvis, also affected by overall lean)
    hip_offset_x_static = segment_lengths['pelvis_width'] / 2
    hip_offset_y_static = 0 # Hips are roughly at the spine_pelvis level
    
    right_hip_x = spine_pelvis_x + hip_offset_x_static * math.cos(forward_lean_angle) - hip_offset_y_static * math.sin(forward_lean_angle)
    right_hip_y = spine_pelvis_y + hip_offset_x_static * math.sin(forward_lean_angle) + hip_offset_y_static * math.cos(forward_lean_angle)
    current_pose['right_hip'] = (right_hip_x, right_hip_y)

    left_hip_x = spine_pelvis_x - hip_offset_x_static * math.cos(forward_lean_angle) - hip_offset_y_static * math.sin(forward_lean_angle)
    left_hip_y = spine_pelvis_y - hip_offset_x_static * math.sin(forward_lean_angle) + hip_offset_y_static * math.cos(forward_lean_angle)
    current_pose['left_hip'] = (left_hip_x, left_hip_y)


    # Arms and Legs motion
    # Running involves counter-lateral limb movement: Right arm swings forward when Right leg swings backward.
    # We use `t_norm` to drive the sinusoidal motion.
    
    # Right Arm:
    # Shoulder swing angle (relative to torso) - needs to be out of phase with right leg
    # Adding `math.pi` to phase makes it opposite to a base phase.
    r_arm_angle_relative_to_torso = arm_swing_amplitude * math.sin(t_norm * 2 * math.pi + math.pi)
    r_arm_absolute_angle = forward_lean_angle + r_arm_angle_relative_to_torso # Absolute angle from vertical

    # Elbow bend (relative to upper arm orientation)
    # The elbow bends more during swing, and less when arm is at extremes.
    # Use a cosine wave, perhaps twice the frequency, to represent flex/extend cycle.
    # Add a base bend as arms are rarely fully straight in running.
    r_elbow_bend_relative = elbow_bend_angle * (0.5 + 0.5 * math.cos(t_norm * 2 * math.pi * 2)) # Min bend when arm is mid-swing
    
    # Calculate right elbow based on right shoulder as origin
    r_elbow_x = current_pose['right_shoulder'][0] + segment_lengths['upper_arm'] * math.sin(r_arm_absolute_angle)
    r_elbow_y = current_pose['right_shoulder'][1] + segment_lengths['upper_arm'] * math.cos(r_arm_absolute_angle)
    current_pose['right_elbow'] = (r_elbow_x, r_elbow_y)
    
    # Calculate right wrist based on right elbow as origin, considering elbow bend
    r_wrist_x = r_elbow_x + segment_lengths['lower_arm'] * math.sin(r_arm_absolute_angle + r_elbow_bend_relative) + wrist_offset_forward
    r_wrist_y = r_elbow_y + segment_lengths['lower_arm'] * math.cos(r_arm_absolute_angle + r_elbow_bend_relative)
    current_pose['right_wrist'] = (r_wrist_x, r_wrist_y)

    # Left Arm (phase shifted by PI from right arm's limb cycle)
    l_arm_angle_relative_to_torso = arm_swing_amplitude * math.sin(t_norm * 2 * math.pi)
    l_arm_absolute_angle = forward_lean_angle + l_arm_angle_relative_to_torso

    l_elbow_bend_relative = elbow_bend_angle * (0.5 + 0.5 * math.cos(t_norm * 2 * math.pi * 2 + math.pi))

    l_elbow_x = current_pose['left_shoulder'][0] + segment_lengths['upper_arm'] * math.sin(l_arm_absolute_angle)
    l_elbow_y = current_pose['left_shoulder'][1] + segment_lengths['upper_arm'] * math.cos(l_arm_absolute_angle)
    current_pose['left_elbow'] = (l_elbow_x, l_elbow_y)

    l_wrist_x = l_elbow_x + segment_lengths['lower_arm'] * math.sin(l_arm_absolute_angle + l_elbow_bend_relative) - wrist_offset_forward # Negative offset for left wrist
    l_wrist_y = l_elbow_y + segment_lengths['lower_arm'] * math.cos(l_arm_absolute_angle + l_elbow_bend_relative)
    current_pose['left_wrist'] = (l_wrist_x, l_wrist_y)

    # Legs motion
    # Right Leg:
    # Hip swing angle (relative to torso) - determines forward/backward motion of thigh
    r_hip_swing_relative = hip_swing_amplitude * math.sin(t_norm * 2 * math.pi)
    r_hip_absolute_angle = forward_lean_angle + r_hip_swing_relative

    # Knee bend (relative to thigh) - more bent during swing phase, less extended during ground contact
    # Combine base_knee_bend (always bent) with a dynamic bend
    r_knee_bend_relative = base_knee_bend + knee_bend_amplitude * (0.5 - 0.5 * math.cos(t_norm * 2 * math.pi * 2)) # Max bend when leg is most forward or back
    
    # Calculate right knee based on right hip as origin
    r_knee_x = current_pose['right_hip'][0] + segment_lengths['thigh'] * math.sin(r_hip_absolute_angle)
    r_knee_y = current_pose['right_hip'][1] + segment_lengths['thigh'] * math.cos(r_hip_absolute_angle)
    current_pose['right_knee'] = (r_knee_x, r_knee_y)

    # Calculate right ankle based on right knee as origin, considering hip and knee angles
    r_ankle_x = r_knee_x + segment_lengths['shin'] * math.sin(r_hip_absolute_angle + r_knee_bend_relative)
    r_ankle_y = r_knee_y + segment_lengths['shin'] * math.cos(r_hip_absolute_angle + r_knee_bend_relative)

    # Add ankle lift for running (foot clears ground)
    # The ankle lifts most when the leg is swinging forward (roughly when t_norm is 0.25 and 0.75 in the cycle)
    # Using abs(sin) for a lift that happens twice per full hip swing
    ankle_lift_offset_amount = ankle_lift_amplitude * abs(math.sin(t_norm * 2 * math.pi * 2))
    r_ankle_y -= ankle_lift_offset_amount # Subtract to move upwards in Pygame coordinates
    current_pose['right_ankle'] = (r_ankle_x, r_ankle_y)

    # Left Leg (phase shifted by PI from right leg)
    l_hip_swing_relative = hip_swing_amplitude * math.sin(t_norm * 2 * math.pi + math.pi)
    l_hip_absolute_angle = forward_lean_angle + l_hip_swing_relative

    l_knee_bend_relative = base_knee_bend + knee_bend_amplitude * (0.5 - 0.5 * math.cos(t_norm * 2 * math.pi * 2 + math.pi))

    l_knee_x = current_pose['left_hip'][0] + segment_lengths['thigh'] * math.sin(l_hip_absolute_angle)
    l_knee_y = current_pose['left_hip'][1] + segment_lengths['thigh'] * math.cos(l_hip_absolute_angle)
    current_pose['left_knee'] = (l_knee_x, l_knee_y)

    l_ankle_x = l_knee_x + segment_lengths['shin'] * math.sin(l_hip_absolute_angle + l_knee_bend_relative)
    l_ankle_y = l_knee_y + segment_lengths['shin'] * math.cos(l_hip_absolute_angle + l_knee_bend_relative)

    l_ankle_lift_offset_amount = ankle_lift_amplitude * abs(math.sin(t_norm * 2 * math.pi * 2 + math.pi))
    l_ankle_y -= l_ankle_lift_offset_amount
    current_pose['left_ankle'] = (l_ankle_x, l_ankle_y)

    # The `current_pose` dictionary now holds the calculated (x, y) coordinates for all 15 points.
    # Their names align with a standard point-light display (Head, Neck Base, Shoulders, Elbows, Wrists,
    # Spine/Pelvis Center, Hips, Knees, Ankles).

    return current_pose

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(BLACK)

    # Calculate time for animation cycle
    time_elapsed += clock.get_time() / 1000.0 # Convert milliseconds to seconds

    current_pose = calculate_current_pose(time_elapsed)

    # Draw the 15 points
    for point_name, (x, y) in current_pose.items():
        pygame.draw.circle(SCREEN, WHITE, (int(x), int(y)), DOT_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
