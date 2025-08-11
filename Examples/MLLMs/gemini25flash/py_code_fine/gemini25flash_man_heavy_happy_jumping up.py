
import pygame
import math

# --- Constants ---
WIDTH, HEIGHT = 600, 800
FPS = 60
POINT_RADIUS = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ground level for the animation base (Y-coordinate on the screen for the foot base)
Y_GROUND = HEIGHT - 100 

# Max jump height in pixels. Adjusted for "heavy weight" to be less floaty/high.
MAX_JUMP_HEIGHT = 130 

# --- Point Indices for clarity ---
# These indices correspond to positions in the pose lists
HEAD = 0
NECK = 1
SHOULDER_L, SHOULDER_R = 2, 3
ELBOW_L, ELBOW_R = 4, 5
WRIST_L, WRIST_R = 6, 7
HIP_L, HIP_R = 8, 9
KNEE_L, KNEE_R = 10, 11
ANKLE_L, ANKLE_R = 12, 13
FOOT_BASE = 14 # The reference point for the ground (0,0) in relative poses

# --- Relative Pose Definitions (relative to FOOT_BASE at (0,0)) ---
# (x, y) coordinates, where y=0 is the foot base (ground level), and y decreases upwards (negative values).
# The person is horizontally centered (x=0 is the center).

# Standing pose: Neutral upright posture
STAND_POSE_RELATIVE = [
    (0, -280),  # Head
    (0, -250),  # Neck
    (-30, -230), # Shoulder L
    (30, -230),  # Shoulder R
    (-35, -170), # Elbow L
    (35, -170),  # Elbow R
    (-40, -110), # Wrist L
    (40, -110),  # Wrist R
    (-20, -130), # Hip L
    (20, -130),  # Hip R
    (-20, -70),  # Knee L
    (20, -70),   # Knee R
    (-20, -10),  # Ankle L
    (20, -10),   # Ankle R
    (0, 0)       # Foot Base
]

# Crouch pose: Deep squat for jump preparation
CROUCH_POSE_RELATIVE = [
    (0, -220),  # Head (lower)
    (0, -190),  # Neck (lower)
    (-30, -170), # Shoulder L (lower, slightly back)
    (30, -170),  # Shoulder R
    (-20, -130), # Elbow L (arms swing back)
    (20, -130),  # Elbow R
    (-10, -80),  # Wrist L
    (10, -80),   # Wrist R
    (-20, -90),  # Hip L (lower, slightly back)
    (20, -90),   # Hip R
    (-30, -50),  # Knee L (bent deeply, shins slightly forward)
    (30, -50),   # Knee R
    (-20, -10),  # Ankle L (stable)
    (20, -10),   # Ankle R
    (0, 0)       # Foot Base (stable on ground)
]

# Launch pose: Body extending rapidly, just before leaving the ground
LAUNCH_POSE_RELATIVE = [
    (0, -290),  # Head (highest internal extension)
    (0, -260),  # Neck
    (-20, -240), # Shoulder L (forward, up)
    (20, -240),  # Shoulder R
    (-10, -180), # Elbow L (arms extending up)
    (10, -180),  # Elbow R
    (0, -120),   # Wrist L (arms extended)
    (0, -120),   # Wrist R
    (-10, -140), # Hip L (slightly forward, up)
    (10, -140),  # Hip R
    (-10, -80),  # Knee L (almost straight)
    (10, -80),   # Knee R
    (-10, -20),  # Ankle L (almost straight)
    (10, -20),   # Ankle R
    (0, 0)       # Foot Base (conceptual ground contact point for this pose)
]

# Apex pose: Mid-air at maximum height, body slightly tucked/relaxed
APEX_POSE_RELATIVE = [
    (0, -270),  # Head (relaxed, slightly forward)
    (0, -240),  # Neck
    (-25, -220), # Shoulder L (relaxed, slightly forward)
    (25, -220),  # Shoulder R
    (-20, -160), # Elbow L
    (20, -160),  # Elbow R
    (-10, -100), # Wrist L
    (10, -100),  # Wrist R
    (-15, -120), # Hip L (slightly tucked up)
    (15, -120),  # Hip R
    (-25, -80),  # Knee L (bent slightly for tuck)
    (25, -80),   # Knee R
    (-20, -20),  # Ankle L (feet below knees)
    (20, -20),   # Ankle R
    (0, -10)     # Foot Base (conceptually slightly above ground if it were landing)
]

# Land pose: Initial impact with ground, knees bent to absorb shock
LAND_POSE_RELATIVE = [
    (0, -220),  # Head (lower, like crouch)
    (0, -190),  # Neck
    (-30, -170), # Shoulder L (lower, slightly back for balance)
    (30, -170),  # Shoulder R
    (-20, -130), # Elbow L
    (20, -130),  # Elbow R
    (-10, -80),  # Wrist L
    (10, -80),   # Wrist R
    (-20, -90),  # Hip L (low, like crouch)
    (20, -90),   # Hip R
    (-30, -50),  # Knee L (bent deeply)
    (30, -50),   # Knee R
    (-20, -10),  # Ankle L (near ground)
    (20, -10),   # Ankle R
    (0, 0)       # Foot Base (on ground)
]

# --- Easing Functions for smooth transitions ---
def ease_in_out_cubic(t):
    """Cubic easing for smooth start and end."""
    return t * t * (3 - 2 * t)

def ease_in_quad(t):
    """Quadratic easing for accelerating motion (e.g., gravity)."""
    return t * t

def ease_out_quad(t):
    """Quadratic easing for decelerating motion (e.g., against gravity)."""
    return 1 - (1 - t) * (1 - t)

def linear(t):
    """Linear interpolation."""
    return t

# --- Animation Phases ---
# Each phase defines a segment of the animation cycle:
# (start_frame_in_cycle, end_frame_in_cycle,
#  start_pose_data, end_pose_data,
#  easing_func_for_body_pose_transition,
#  easing_func_for_global_y_offset,
#  start_global_y_offset, end_global_y_offset)

# Durations in frames (at 60 FPS):
# Stand still: 0.5s = 30 frames
# Crouch: 0.3s = 18 frames
# Launch (push-off): 0.2s = 12 frames (fast, powerful)
# Ascent (jump up): 0.4s = 24 frames
# Descent (fall down): 0.4s = 24 frames
# Recover (return to stand): 0.3s = 18 frames
TOTAL_FRAMES_IN_CYCLE = 30 + 18 + 12 + 24 + 24 + 18 # = 126 frames

animation_phases = [
    # Phase 0: Stand still at the beginning of the cycle
    (0, 30, STAND_POSE_RELATIVE, STAND_POSE_RELATIVE, linear, linear, 0, 0),
    # Phase 1: Transition from Standing to deep Crouch
    (30, 30 + 18, STAND_POSE_RELATIVE, CROUCH_POSE_RELATIVE, ease_in_out_cubic, linear, 0, 0),
    # Phase 2: Rapid push-off from Crouch to Launch pose
    (30 + 18, 30 + 18 + 12, CROUCH_POSE_RELATIVE, LAUNCH_POSE_RELATIVE, ease_in_quad, linear, 0, 0),
    # Phase 3: Ascent - body moves upwards from Launch pose to Apex (internal pose also changes)
    (30 + 18 + 12, 30 + 18 + 12 + 24, LAUNCH_POSE_RELATIVE, APEX_POSE_RELATIVE, ease_out_quad, ease_out_quad, 0, -MAX_JUMP_HEIGHT),
    # Phase 4: Descent - body falls from Apex to Landing (internal pose changes for impact)
    (30 + 18 + 12 + 24, 30 + 18 + 12 + 24 + 24, APEX_POSE_RELATIVE, LAND_POSE_RELATIVE, ease_in_quad, ease_in_quad, -MAX_JUMP_HEIGHT, 0),
    # Phase 5: Recovery - from Landing pose back to Standing
    (30 + 18 + 12 + 24 + 24, 30 + 18 + 12 + 24 + 24 + 18, LAND_POSE_RELATIVE, STAND_POSE_RELATIVE, ease_out_quad, linear, 0, 0)
]


def get_current_animation_state(frame_num):
    """
    Calculates the current pose (relative coordinates of points) and the global
    vertical offset of the entire figure based on the current frame number.

    Args:
        frame_num (int): The current frame count since the animation started.

    Returns:
        tuple: (list of (x,y) tuples for the 15 points in the current pose,
                current global vertical offset in pixels).
    """
    current_frame_in_cycle = frame_num % TOTAL_FRAMES_IN_CYCLE

    for start_f, end_f, start_pose, end_pose, easing_body, easing_y_offset, y_offset_start, y_offset_end in animation_phases:
        if start_f <= current_frame_in_cycle < end_f:
            # Calculate normalized time (t) for this specific phase
            t_raw = (current_frame_in_cycle - start_f) / (end_f - start_f)
            
            # Apply easing functions to get eased 't' values
            t_body = easing_body(t_raw)
            t_y_offset = easing_y_offset(t_raw)

            # Interpolate body pose points
            current_pose = []
            for i in range(len(start_pose)):
                x = start_pose[i][0] + (end_pose[i][0] - start_pose[i][0]) * t_body
                y = start_pose[i][1] + (end_pose[i][1] - start_pose[i][1]) * t_body
                current_pose.append((x, y))
            
            # Interpolate global vertical offset
            current_y_global_offset = y_offset_start + (y_offset_end - y_offset_start) * t_y_offset

            return current_pose, current_y_global_offset
    
    # If for some reason the frame falls outside defined phases (shouldn't happen with full cycle coverage)
    return STAND_POSE_RELATIVE, 0 

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Jumping Up")
clock = pygame.time.Clock()

running = True
frame_count = 0
center_x = WIDTH // 2

# --- Main Animation Loop ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current animation state (pose and vertical position)
    current_pose_relative, current_y_global_offset = get_current_animation_state(frame_count)

    # Clear the screen to black
    screen.fill(BLACK)

    # Draw each of the 15 points
    for i, (rel_x, rel_y) in enumerate(current_pose_relative):
        # Convert relative coordinates (relative to FOOT_BASE at (0,0))
        # to absolute screen coordinates.
        # X: centered horizontally
        # Y: Y_GROUND is the screen Y for the foot base. Since relative_y is negative upwards,
        #    we add it. Then add the global offset for jumping.
        screen_x = center_x + rel_x
        screen_y = Y_GROUND + rel_y + current_y_global_offset
        
        # Draw the point as a white circle
        pygame.draw.circle(screen, WHITE, (int(screen_x), int(screen_y)), POINT_RADIUS)

    # Update the display to show the new frame
    pygame.display.flip()

    # Control the animation speed (cap frame rate)
    clock.tick(FPS)
    frame_count += 1

# Quit Pygame when the loop ends
pygame.quit()
