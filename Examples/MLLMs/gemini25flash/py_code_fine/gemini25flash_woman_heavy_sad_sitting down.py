
import pygame
import math

# --- Pygame Setup ---
pygame.init()

# Define screen dimensions. A vertical aspect ratio is typical for full body figures.
WIDTH, HEIGHT = 600, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Woman Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point stimulus properties
POINT_RADIUS = 5  # Size of each point light

# Animation speed and control
FPS = 60  # Frames per second
CLOCK = pygame.time.Clock()

# --- Pose Definitions ---
CENTER_X = WIDTH // 2  # Horizontal center of the screen
GROUND_Y = HEIGHT - 100  # Y-coordinate representing the floor/ground level
CHAIR_SEAT_Y = GROUND_Y - 170 # Y-coordinate representing the chair seat height for hips when sitting (lower for heavier person)

def get_body_points(
    hip_center_y,      # Y coordinate of the hip center
    torso_lean_x,      # X offset for upper body (forward/backward lean)
    torso_lean_y,      # Y offset for upper body (slump/straightening)
    hip_x_spread,      # Half-width of hips
    shoulder_x_spread, # Half-width of shoulders
    arm_x_spread,      # Half-width of arms (at elbows/wrists)
    leg_x_spread,      # Half-width of legs (at knees/ankles/feet)
    head_rel_y, shoulder_rel_y, elbow_rel_y, wrist_rel_y, # Relative Y to hip_center_y for upper body parts
    knee_rel_y, ankle_rel_y, foot_rel_y                   # Relative Y to hip_center_y for lower body parts
):
    """
    Generates 15 point coordinates for a human pose based on relative body part positions
    and overall posture parameters.
    """
    points = [None] * 15 # Ensure exactly 15 points

    # Define points relative to hip_center_y and CENTER_X, applying torso lean
    # Points are indexed as per common motion capture standards for clarity.
    # 0: Head, 1: L_Shoulder, 2: R_Shoulder, 3: L_Elbow, 4: R_Elbow, 5: L_Wrist, 6: R_Wrist
    # 7: L_Hip, 8: R_Hip, 9: L_Knee, 10: R_Knee, 11: L_Ankle, 12: R_Ankle, 13: L_Foot, 14: R_Foot

    # Upper Body points (affected by torso lean)
    points[0] = (CENTER_X + torso_lean_x, hip_center_y + head_rel_y + torso_lean_y) # Head
    points[1] = (CENTER_X - shoulder_x_spread + torso_lean_x * 0.7, hip_center_y + shoulder_rel_y + torso_lean_y * 0.7) # Left Shoulder
    points[2] = (CENTER_X + shoulder_x_spread + torso_lean_x * 0.7, hip_center_y + shoulder_rel_y + torso_lean_y * 0.7) # Right Shoulder
    points[3] = (CENTER_X - arm_x_spread + torso_lean_x * 0.5, hip_center_y + elbow_rel_y + torso_lean_y * 0.5) # Left Elbow
    points[4] = (CENTER_X + arm_x_spread + torso_lean_x * 0.5, hip_center_y + elbow_rel_y + torso_lean_y * 0.5) # Right Elbow
    points[5] = (CENTER_X - arm_x_spread + torso_lean_x * 0.3, hip_center_y + wrist_rel_y + torso_lean_y * 0.3) # Left Wrist
    points[6] = (CENTER_X + arm_x_spread + torso_lean_x * 0.3, hip_center_y + wrist_rel_y + torso_lean_y * 0.3) # Right Wrist

    # Lower Body points (hips are the base, feet are fixed to GROUND_Y)
    points[7] = (CENTER_X - hip_x_spread, hip_center_y) # Left Hip
    points[8] = (CENTER_X + hip_x_spread, hip_center_y) # Right Hip
    points[9] = (CENTER_X - leg_x_spread, hip_center_y + knee_rel_y) # Left Knee
    points[10] = (CENTER_X + leg_x_spread, hip_center_y + knee_rel_y) # Right Knee
    points[11] = (CENTER_X - leg_x_spread, hip_center_y + ankle_rel_y) # Left Ankle
    points[12] = (CENTER_X + leg_x_spread, hip_center_y + ankle_rel_y) # Right Ankle
    
    # Feet always stay on the ground (GROUND_Y)
    points[13] = (CENTER_X - leg_x_spread, GROUND_Y) # Left Foot
    points[14] = (CENTER_X + leg_x_spread, GROUND_Y) # Right Foot

    # Adjust ankle_rel_y and foot_rel_y to ensure feet are precisely on GROUND_Y
    # The `foot_rel_y` parameter here is effectively overridden by GROUND_Y for feet.
    # We must ensure ankle_rel_y aligns such that hip_center_y + ankle_rel_y positions the ankle correctly relative to the foot.
    # The knee_rel_y, ankle_rel_y should ensure plausible leg bending.
    
    # Recalculate ankle_rel_y and foot_rel_y based on the new fixed GROUND_Y for feet
    # ankle_y_target = GROUND_Y - (POINT_RADIUS * 2) # A small offset above the ground for the ankle joint
    # The knee_rel_y and ankle_rel_y values in the function signature need to be carefully chosen for realism.
    # The approach taken here is: knee_rel_y and ankle_rel_y are offsets from hip_center_y.
    # The actual foot points are then fixed to GROUND_Y. This implicitly defines the ankle's height
    # relative to the foot. Let's make sure the ankles are slightly above the feet.
    ankle_offset_from_foot = 25 # Distance from foot point to ankle point
    points[11] = (CENTER_X - leg_x_spread, GROUND_Y - ankle_offset_from_foot) # Left Ankle
    points[12] = (CENTER_X + leg_x_spread, GROUND_Y - ankle_offset_from_foot) # Right Ankle
    
    return points


# Define Key Poses for the "sad woman sitting down" animation
# These are empirically chosen values to represent a biomechanically plausible motion
# with subtle cues for "sadness" (slight slump) and "heavy weight" (deliberate, wider base).

# 1. P_STANDING: Standing upright, slightly relaxed initial pose.
P_STANDING = get_body_points(
    hip_center_y=GROUND_Y - 180, # Hips are 180px above ground
    torso_lean_x=0, torso_lean_y=0, # No lean
    hip_x_spread=30, shoulder_x_spread=60, arm_x_spread=70, leg_x_spread=25,
    head_rel_y=-170, shoulder_rel_y=-130, elbow_rel_y=-40, wrist_rel_y=60,
    knee_rel_y=90, ankle_rel_y=180, foot_rel_y=180 # foot_rel_y here acts as a placeholder
)

# 2. P_SQUAT_LEAN: Initial squat and forward lean, showing preparation and a slight sag.
# This stage suggests the "heavy" aspect with a deliberate initial movement.
P_SQUAT_LEAN = get_body_points(
    hip_center_y=GROUND_Y - 130, # Hips descend
    torso_lean_x=20, torso_lean_y=10, # Pronounced forward and slightly downward lean for upper body
    hip_x_spread=35, shoulder_x_spread=65, arm_x_spread=65, leg_x_spread=35, # Wider stance for stability
    head_rel_y=-160, shoulder_rel_y=-120, elbow_rel_y=-40, wrist_rel_y=40,
    knee_rel_y=40, ankle_rel_y=140, foot_rel_y=140
)

# 3. P_MID_DESCENT: Mid-way through descent, knees deeply bent, body continues to lower.
P_MID_DESCENT = get_body_points(
    hip_center_y=GROUND_Y - 80, # Hips significantly lower
    torso_lean_x=10, torso_lean_y=5, # Starting to straighten up slightly
    hip_x_spread=40, shoulder_x_spread=60, arm_x_spread=60, leg_x_spread=45, # Legs spread further
    head_rel_y=-140, shoulder_rel_y=-110, elbow_rel_y=-50, wrist_rel_y=20,
    knee_rel_y=20, ankle_rel_y=100, foot_rel_y=100
)

# 4. P_SITTING: Final seated pose, slightly slumped to convey "sadness" and relaxed posture.
P_SITTING = get_body_points(
    hip_center_y=CHAIR_SEAT_Y, # Hips are at the chair seat height
    torso_lean_x=10, torso_lean_y=15, # Final slumped position (head/shoulders slightly forward and down)
    hip_x_spread=30, shoulder_x_spread=50, arm_x_spread=50, leg_x_spread=55, # Legs wider and relaxed, arms closer
    head_rel_y=-120, shoulder_rel_y=-90, elbow_rel_y=-20, wrist_rel_y=20,
    knee_rel_y=20, ankle_rel_y=50, foot_rel_y=50 # Knees bent, feet flat
)


# Store all key poses in order of animation
all_key_poses = [P_STANDING, P_SQUAT_LEAN, P_MID_DESCENT, P_SITTING]

# Animation duration and frame calculation
TOTAL_ANIMATION_FRAMES = 240 # 4 seconds at 60 FPS for a deliberate, somewhat slow motion.
FRAMES_PER_STAGE = TOTAL_ANIMATION_FRAMES // (len(all_key_poses) - 1) # Frames for each segment of the animation

def lerp(start_val, end_val, t):
    """Linear interpolation between two values."""
    return start_val + (end_val - start_val) * t

def get_interpolated_pose(frame_num):
    """
    Calculates the pose for a given frame number by interpolating smoothly
    between the defined key poses.
    """
    # If animation is complete, return the final pose
    if frame_num >= TOTAL_ANIMATION_FRAMES:
        return all_key_poses[-1]

    # Determine which two key poses to interpolate between
    stage_idx = frame_num // FRAMES_PER_STAGE
    
    # Ensure stage_idx does not exceed the valid range for key poses
    if stage_idx >= len(all_key_poses) - 1:
        return all_key_poses[-1]

    current_pose = all_key_poses[stage_idx]
    next_pose = all_key_poses[stage_idx + 1]

    # Calculate t (progress within the current stage, from 0.0 to 1.0)
    t_in_stage = (frame_num % FRAMES_PER_STAGE) / FRAMES_PER_STAGE

    # Apply an easing function for smoother acceleration and deceleration
    # This is a cubic ease-in-out function, often used for natural motion.
    if t_in_stage < 0.5:
        t_eased = 4 * t_in_stage * t_in_stage * t_in_stage
    else:
        t_eased = 1 - pow(-2 * t_in_stage + 2, 3) / 2

    interpolated_points = []
    for i in range(15): # Iterate over all 15 points
        x = lerp(current_pose[i][0], next_pose[i][0], t_eased)
        y = lerp(current_pose[i][1], next_pose[i][1], t_eased)
        interpolated_points.append((x, y))
    return interpolated_points

# --- Main Animation Loop ---
current_frame = 0
running = True

# Define how long to display the final pose before looping
show_end_pose_frames = FPS * 2 # 2 seconds
total_loop_frames = TOTAL_ANIMATION_FRAMES + show_end_pose_frames # Total frames for one full cycle

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: # Reset animation on 'r' key press
                current_frame = 0

    # Clear the screen
    SCREEN.fill(BLACK)

    # Get the current pose for the animation frame
    current_pose_points = get_interpolated_pose(current_frame)

    # Draw each point light
    for x, y in current_pose_points:
        pygame.draw.circle(SCREEN, WHITE, (int(x), int(y)), POINT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Advance the animation frame, loop back to start if at the end
    current_frame = (current_frame + 1) % total_loop_frames
    
    # Control animation speed
    CLOCK.tick(FPS)

# Quit Pygame
pygame.quit()
