
import pygame
import math

# --- Constants ---
# Screen dimensions and frames per second
WIDTH, HEIGHT = 800, 600
FPS = 60

# Visual style
POINT_RADIUS = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- Keyframe Data ---
# The animation is built from a series of key poses (keyframes).
# The 15 points represent the main joints of the human body, following a
# standard model for biological motion stimuli.
#
# Coordinates are defined in a model space where:
# - The origin (0,0) is on the floor between the feet.
# - The Y-axis points upwards.

# Joint indices are defined for clarity when creating poses.
HEAD, NECK, L_SHOULDER, R_SHOULDER, L_ELBOW, R_ELBOW, L_WRIST, R_WRIST, \
TORSO_CENTER, L_HIP, R_HIP, L_KNEE, R_KNEE, L_ANKLE, R_ANKLE = range(15)

# POSE 1: Standing with a sad, heavy, and slumped posture.
# The head is bowed, shoulders are rounded, and posture is not fully upright.
POSE_STAND = [
    (10, 260),    # Head
    (5, 225),     # Neck
    (-30, 215),   # Left Shoulder
    (30, 215),    # Right Shoulder
    (-35, 170),   # Left Elbow
    (35, 170),    # Right Elbow
    (-38, 130),   # Left Wrist
    (38, 130),    # Right Wrist
    (0, 180),     # Torso Center
    (-25, 140),   # Left Hip
    (25, 140),    # Right Hip
    (-28, 70),    # Left Knee
    (28, 70),     # Right Knee
    (-30, 0),     # Left Ankle
    (30, 0)       # Right Ankle
]

# POSE 2: Mid-sit, leaning forward to maintain balance as the hips move down and back.
POSE_MIDSIT = [
    (25, 230),    # Head
    (20, 195),    # Neck
    (-15, 185),   # Left Shoulder
    (45, 185),    # Right Shoulder
    (-20, 140),   # Left Elbow
    (50, 140),    # Right Elbow
    (-23, 100),   # Left Wrist
    (53, 100),    # Right Wrist
    (15, 150),    # Torso Center
    (-60, 100),   # Left Hip
    (10, 100),    # Right Hip
    (-45, 60),    # Left Knee
    (25, 60),     # Right Knee
    (-30, 0),     # Left Ankle
    (30, 0)       # Right Ankle
]

# POSE 3: Seated position, after making contact with the "chair".
POSE_SIT = [
    (5, 205),     # Head
    (0, 170),     # Neck
    (-35, 160),   # Left Shoulder
    (25, 160),    # Right Shoulder
    (-30, 115),   # Left Elbow
    (30, 115),    # Right Elbow
    (-20, 85),    # Left Wrist
    (40, 85),     # Right Wrist
    (-5, 125),    # Torso Center
    (-45, 80),    # Left Hip
    (25, 80),     # Right Hip
    (-10, 65),    # Left Knee
    (50, 65),     # Right Knee
    (-25, 0),     # Left Ankle
    (35, 0)       # Right Ankle
]

# POSE 4: A slightly compressed pose to simulate the "plop" of a heavy landing.
# This pose is derived from POSE_SIT by lowering most joints slightly.
y_drop = 4
POSE_SETTLE = []
for i, (x, y) in enumerate(POSE_SIT):
    if i in [L_ANKLE, R_ANKLE]:
        new_y = y
    elif i in [L_KNEE, R_KNEE]:
        new_y = y - y_drop / 2
    else:
        new_y = y - y_drop
    POSE_SETTLE.append((x, new_y))

# --- Animation Sequence ---
# This list defines the complete, smoothly looping animation cycle.
# Each dictionary specifies a target pose and the duration (in frames)
# of the transition to that pose from the previous one.
ANIMATION_SEQUENCE = [
    {'pose': POSE_STAND,  'duration': 60},  # 1. Hold standing pose
    {'pose': POSE_MIDSIT, 'duration': 75},  # 2. Transition to mid-sit
    {'pose': POSE_SIT,    'duration': 30},  # 3. Transition to seated
    {'pose': POSE_SETTLE, 'duration': 6},   # 4. "Plop" down (quick)
    {'pose': POSE_SIT,    'duration': 24},  # 5. Rebound slightly
    {'pose': POSE_SIT,    'duration': 60},  # 6. Hold seated pose
    {'pose': POSE_MIDSIT, 'duration': 90},  # 7. Begin standing up
    {'pose': POSE_STAND,  'duration': 90},  # 8. Return to standing pose
]

# --- Helper Functions ---
def lerp(p1, p2, t):
    """Linearly interpolates between two 2D points."""
    return (p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t)

def ease_in_out_cubic(t):
    """Applies a cubic easing function for smooth acceleration and deceleration."""
    if t < 0.5:
        return 4 * t * t * t
    else:
        f = t - 1
        return 1 + 4 * f * f * f

def transform_to_screen(point, screen_width, screen_height):
    """Converts model coordinates to Pygame screen coordinates."""
    x, y = point
    # Center horizontally, adjust vertical position, and flip the Y-axis
    screen_x = int(x + screen_width / 2)
    screen_y = int(-y + screen_height / 2 + 150)
    return screen_x, screen_y

# --- Main Application ---
def main():
    """Sets up the Pygame window and runs the animation loop."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Woman with Heavy Weight Sitting Down")
    clock = pygame.time.Clock()

    total_anim_frames = sum(item['duration'] for item in ANIMATION_SEQUENCE)
    current_frame_index = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Animation Logic ---
        frame_in_sequence = current_frame_index % total_anim_frames

        # Determine the current segment of the animation
        segment_start_frame = 0
        for i, segment in enumerate(ANIMATION_SEQUENCE):
            segment_end_frame = segment_start_frame + segment['duration']
            if frame_in_sequence < segment_end_frame:
                start_pose = ANIMATION_SEQUENCE[i - 1]['pose']
                target_pose = segment['pose']
                duration = segment['duration']
                
                if duration > 0:
                    time_in_segment = frame_in_sequence - segment_start_frame
                    t = time_in_segment / duration
                else:
                    t = 1.0 
                break
            segment_start_frame = segment_end_frame

        # Apply easing for a more natural motion
        eased_t = ease_in_out_cubic(t)

        # Interpolate each point's position for the current frame
        current_points = []
        for i in range(len(start_pose)):
            interpolated_point = lerp(start_pose[i], target_pose[i], eased_t)
            current_points.append(interpolated_point)

        # --- Drawing ---
        screen.fill(BLACK)
        for point in current_points:
            screen_pos = transform_to_screen(point, WIDTH, HEIGHT)
            pygame.draw.circle(screen, WHITE, screen_pos, POINT_RADIUS)

        pygame.display.flip()

        # --- Update ---
        current_frame_index += 1
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
