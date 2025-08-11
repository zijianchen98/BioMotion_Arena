
import pygame
import math
import numpy as np

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800  # Taller to match the aspect ratio of the example image

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5

# Biomechanical model parameters (arbitrary units, will be scaled)
# These are initial relative positions, assuming the 'lower_spine' (pelvis center) is (0,0).
# Y-axis in this model: +Y is up, -Y is down. Will be inverted for Pygame's Y-down coordinate system.
SCALE = 2.0  # Adjust to make the figure larger/smaller

initial_poses_relative_to_center = {
    "head":           (0, 80 * SCALE),
    "upper_spine":    (0, 50 * SCALE),
    "lower_spine":    (0, 0),         # Reference point for the whole figure's base
    "left_shoulder":  (-20 * SCALE, 55 * SCALE),
    "right_shoulder": (20 * SCALE, 55 * SCALE),
    "left_elbow":     (-30 * SCALE, 30 * SCALE),
    "right_elbow":    (30 * SCALE, 30 * SCALE),
    "left_wrist":     (-25 * SCALE, 0 * SCALE),
    "right_wrist":    (25 * SCALE, 0 * SCALE),
    "left_hip":       (-15 * SCALE, -10 * SCALE), # Hips slightly lower than lower_spine
    "right_hip":      (15 * SCALE, -10 * SCALE),
    "left_knee":      (-15 * SCALE, -50 * SCALE),
    "right_knee":     (15 * SCALE, -50 * SCALE),
    "left_ankle":     (-15 * SCALE, -90 * SCALE),
    "right_ankle":    (15 * SCALE, -90 * SCALE),
}

# The number of points must be exactly 15 as per requirement
assert len(initial_poses_relative_to_center) == 15, "There must be exactly 15 points."

# Map points to indices for consistent access
POINT_NAMES = list(initial_poses_relative_to_center.keys())
POINT_INDICES = {name: i for i, name in enumerate(POINT_NAMES)}

# Animation parameters
FPS = 60
WALK_CYCLE_DURATION_SECONDS = 2.2 # Slower walk for "sadman with heavy weight" (implies more labored)
TOTAL_FRAMES_PER_CYCLE = int(WALK_CYCLE_DURATION_SECONDS * FPS)

# Amplitudes for oscillations (tuned for "sadman with heavy weight" characteristics)
PELVIS_Y_SWAY_AMPLITUDE = 7 * SCALE # Plodding, slightly more vertical movement
PELVIS_X_SWAY_AMPLITUDE = 3 * SCALE # Side-to-side sway

# Leg movements
HIP_X_AMPLITUDE = 20 * SCALE # Stride length (smaller for 'sadman')
KNEE_BEND_MAX_VERTICAL_DISPLACEMENT = 15 * SCALE # Max vertical drop of knee due to bending
ANKLE_LIFT_MAX_Y = 20 * SCALE # Max vertical lift for foot clearance during swing

# Arm swing (reduced for 'sadman')
ARM_SWING_X_AMPLITUDE = 15 * SCALE
ARM_SWING_Y_AMPLITUDE = 5 * SCALE

# Head bobbing
HEAD_Y_BOB_AMPLITUDE = 3 * SCALE
HEAD_X_BOB_AMPLITUDE = 1 * SCALE

# Posture adjustments for "sadman with heavy weight" (static offsets applied to initial pose)
SAD_HEAD_Y_OFFSET = -8 * SCALE # Head significantly lower
SAD_SHOULDER_Y_OFFSET = -5 * SCALE # Shoulders significantly slumped
SAD_ARM_FORWARD_OFFSET = -7 * SCALE # Arms slightly forward/inward (hunched)
SAD_TORSO_FORWARD_LEAN_X = 5 * SCALE # General forward lean of torso/upper body
SAD_TORSO_FORWARD_LEAN_Y = -2 * SCALE # Slight compression of torso

def get_point_positions(frame):
    """
    Calculates the position of all 15 points for a given animation frame.
    Returns a list of (x, y) tuples in screen coordinates.
    """
    # Start with initial relative positions. These form the "default" pose.
    current_relative_positions = np.array([list(initial_poses_relative_to_center[name]) for name in POINT_NAMES], dtype=float)

    # Calculate current phase of the walking cycle
    cycle_progress = (frame % TOTAL_FRAMES_PER_CYCLE) / TOTAL_FRAMES_PER_CYCLE
    angle = cycle_progress * 2 * math.pi  # 0 to 2*pi over one cycle

    # --- Apply static "sadman" posture adjustments (applied once to the base pose) ---
    # Head and torso lean
    current_relative_positions[POINT_INDICES["head"]][1] += SAD_HEAD_Y_OFFSET
    current_relative_positions[POINT_INDICES["upper_spine"]][0] += SAD_TORSO_FORWARD_LEAN_X
    current_relative_positions[POINT_INDICES["upper_spine"]][1] += SAD_TORSO_FORWARD_LEAN_Y
    current_relative_positions[POINT_INDICES["head"]][0] += SAD_TORSO_FORWARD_LEAN_X

    # Shoulders slumped and arms hunched forward
    current_relative_positions[POINT_INDICES["left_shoulder"]][1] += SAD_SHOULDER_Y_OFFSET
    current_relative_positions[POINT_INDICES["right_shoulder"]][1] += SAD_SHOULDER_Y_OFFSET
    # Arms are relative to shoulders, so the shoulder offset carries down.
    current_relative_positions[POINT_INDICES["left_shoulder"]][0] += SAD_ARM_FORWARD_OFFSET
    current_relative_positions[POINT_INDICES["left_elbow"]][0] += SAD_ARM_FORWARD_OFFSET
    current_relative_positions[POINT_INDICES["left_wrist"]][0] += SAD_ARM_FORWARD_OFFSET
    current_relative_positions[POINT_INDICES["right_shoulder"]][0] -= SAD_ARM_FORWARD_OFFSET  # Opposite for right arm
    current_relative_positions[POINT_INDICES["right_elbow"]][0] -= SAD_ARM_FORWARD_OFFSET
    current_relative_positions[POINT_INDICES["right_wrist"]][0] -= SAD_ARM_FORWARD_OFFSET


    # --- Global body oscillations (pelvis as reference point) ---
    # These offsets apply to the "root" of the figure, 'lower_spine', and thus everything else.
    # Pelvis vertical sway: lowest during mid-stance (when a foot is flat), highest during double support.
    # A full cycle has two steps, so 2 full up/down movements.
    pelvis_y_dynamic_offset = PELVIS_Y_SWAY_AMPLITUDE * (0.5 - 0.5 * math.cos(angle * 2))
    # Pelvis side-to-side sway: minimal, matches frequency of steps.
    pelvis_x_dynamic_offset = PELVIS_X_SWAY_AMPLITUDE * math.sin(angle * 2)

    # --- Dynamic Joint Movements (added to adjusted base pose) ---

    # Head Bobbing (relative to its current (saddened) position)
    # Phase adjusted slightly out of sync with pelvis for natural look
    head_y_dynamic_offset = HEAD_Y_BOB_AMPLITUDE * math.sin(angle * 2 + math.pi / 2)
    head_x_dynamic_offset = HEAD_X_BOB_AMPLITUDE * math.cos(angle * 2)  # Slight side-to-side with step

    current_relative_positions[POINT_INDICES["head"]][0] += head_x_dynamic_offset
    current_relative_positions[POINT_INDICES["head"]][1] += head_y_dynamic_offset

    # Arm Movements (swing opposite to legs for balance)
    # Right arm swings with Left leg (angle), Left arm with Right leg (angle+pi)
    arm_x_right_dynamic = ARM_SWING_X_AMPLITUDE * math.sin(angle)
    arm_y_right_dynamic = ARM_SWING_Y_AMPLITUDE * math.cos(angle * 2)  # Vertical component of arm swing

    arm_x_left_dynamic = ARM_SWING_X_AMPLITUDE * math.sin(angle + math.pi)
    arm_y_left_dynamic = ARM_SWING_Y_AMPLITUDE * math.cos((angle + math.pi) * 2)

    # Apply arm dynamic offsets to elbow and wrist relative to their initial positions from the shoulder
    # Right arm points
    current_relative_positions[POINT_INDICES["right_elbow"]][0] += arm_x_right_dynamic
    current_relative_positions[POINT_INDICES["right_elbow"]][1] += arm_y_right_dynamic
    current_relative_positions[POINT_INDICES["right_wrist"]][0] += arm_x_right_dynamic * 1.5  # Amplified for wrist
    current_relative_positions[POINT_INDICES["right_wrist"]][1] += arm_y_right_dynamic * 1.5

    # Left arm points
    current_relative_positions[POINT_INDICES["left_elbow"]][0] += arm_x_left_dynamic
    current_relative_positions[POINT_INDICES["left_elbow"]][1] += arm_y_left_dynamic
    current_relative_positions[POINT_INDICES["left_wrist"]][0] += arm_x_left_dynamic * 1.5
    current_relative_positions[POINT_INDICES["left_wrist"]][1] += arm_y_left_dynamic * 1.5

    # Leg Movements (coordinated with each other)
    # Left leg leads (angle), Right leg lags (angle + pi)

    # LEFT LEG
    # Hip: Primarily X movement (forward/backward)
    hip_x_left_dynamic = HIP_X_AMPLITUDE * math.sin(angle)
    current_relative_positions[POINT_INDICES["left_hip"]][0] += hip_x_left_dynamic

    # Knee: Bends during swing phase, relatively straight during stance.
    # Angle from 0 to pi is stance, pi to 2pi is swing (for left leg).
    knee_bend_factor_left = 0
    ankle_lift_y_left_dynamic = 0
    if angle < math.pi:  # Stance phase (foot down)
        # Knee slightly bends as weight settles, then straightens for push-off
        # Using a cosine wave for smooth transition. Max bend at pi/2 (mid-stance).
        knee_bend_factor_left = 0.5 * (1 - math.cos(angle * 2))
        ankle_lift_y_left_dynamic = 0  # Foot stays mostly on ground
    else:  # Swing phase (foot up)
        # Knee bends significantly (max bend at midpoint of swing), then straightens as leg swings forward
        swing_angle = angle - math.pi  # Normalize swing phase to 0 to pi
        knee_bend_factor_left = 0.5 * (1 + math.cos(swing_angle))
        # Ankle lifts for foot clearance. Lifts up and then down.
        ankle_lift_y_left_dynamic = ANKLE_LIFT_MAX_Y * (0.5 - 0.5 * math.cos(swing_angle * 2))

    # Apply knee bend: vertical displacement (knee point moves down relative to hip).
    # This is applied to Y coordinate by subtracting from the Y-value.
    knee_y_dynamic_offset_left = KNEE_BEND_MAX_VERTICAL_DISPLACEMENT * knee_bend_factor_left

    current_relative_positions[POINT_INDICES["left_knee"]][0] += hip_x_left_dynamic
    current_relative_positions[POINT_INDICES["left_knee"]][1] -= knee_y_dynamic_offset_left  # Knee moves down

    # Ankle: Lifts during swing phase, touches down during stance.
    current_relative_positions[POINT_INDICES["left_ankle"]][0] += hip_x_left_dynamic
    current_relative_positions[POINT_INDICES["left_ankle"]][1] -= knee_y_dynamic_offset_left  # Ankle also moves down with knee bend
    current_relative_positions[POINT_INDICES["left_ankle"]][1] += ankle_lift_y_left_dynamic  # Then lifts for clearance


    # RIGHT LEG (180 degrees out of phase)
    angle_right = angle + math.pi
    
    hip_x_right_dynamic = HIP_X_AMPLITUDE * math.sin(angle_right)
    current_relative_positions[POINT_INDICES["right_hip"]][0] += hip_x_right_dynamic

    knee_bend_factor_right = 0
    ankle_lift_y_right_dynamic = 0
    if angle_right < math.pi:  # Stance phase
        knee_bend_factor_right = 0.5 * (1 - math.cos(angle_right * 2))
        ankle_lift_y_right_dynamic = 0
    else:  # Swing phase
        swing_angle_right = angle_right - math.pi
        knee_bend_factor_right = 0.5 * (1 + math.cos(swing_angle_right))
        ankle_lift_y_right_dynamic = ANKLE_LIFT_MAX_Y * (0.5 - 0.5 * math.cos(swing_angle_right * 2))

    knee_y_dynamic_offset_right = KNEE_BEND_MAX_VERTICAL_DISPLACEMENT * knee_bend_factor_right

    current_relative_positions[POINT_INDICES["right_knee"]][0] += hip_x_right_dynamic
    current_relative_positions[POINT_INDICES["right_knee"]][1] -= knee_y_dynamic_offset_right

    current_relative_positions[POINT_INDICES["right_ankle"]][0] += hip_x_right_dynamic
    current_relative_positions[POINT_INDICES["right_ankle"]][1] -= knee_y_dynamic_offset_right
    current_relative_positions[POINT_INDICES["right_ankle"]][1] += ankle_lift_y_right_dynamic


    # --- Final Transformation to Screen Coordinates ---
    # Center of the screen where the 'lower_spine' (pelvis) will be positioned.
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2 + 100  # Shift figure slightly down on screen for better vertical centering

    transformed_points_list = []
    for i in range(len(POINT_NAMES)):
        # Get the current relative position of the point from the model's (0,0) after all dynamic offsets
        px_model_relative = current_relative_positions[i][0]
        py_model_relative = current_relative_positions[i][1]

        # Apply the global pelvis sway to all points
        # This effectively shifts the entire figure.
        final_x_model = px_model_relative + pelvis_x_dynamic_offset
        final_y_model = py_model_relative + pelvis_y_dynamic_offset
        
        # Convert to screen coordinates (invert Y, translate to center)
        screen_x = int(center_x + final_x_model)
        screen_y = int(center_y - final_y_model)  # Invert Y-axis for Pygame

        transformed_points_list.append((screen_x, screen_y))
    
    return transformed_points_list

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion Stimulus: Sadman Walking with Heavy Weight")
clock = pygame.time.Clock()

frame_count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    current_points = get_point_positions(frame_count)

    for point in current_points:
        pygame.draw.circle(screen, WHITE, point, POINT_RADIUS)

    pygame.display.flip()

    frame_count += 1
    clock.tick(FPS)

pygame.quit()
