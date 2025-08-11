
import pygame
import math

# Pygame setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_RADIUS = 3  # Matches example image style for small white dots

# Animation parameters
ROLL_CYCLE_DURATION_SECONDS = 4  # Time for one full cycle (tuck, roll, unfurl, stand)
TOTAL_FRAMES = FPS * ROLL_CYCLE_DURATION_SECONDS
NUM_ROLLS_PER_CYCLE = 1.5  # How many full body rotations during the roll phase (e.g., 1.5 rotations)
ROLL_HORIZONTAL_DISTANCE = 400  # How far the person moves horizontally across the screen during one cycle

# --- Biomechanical Model (simplified 15 points) ---
# Each point is (x_offset, y_offset) relative to the torso (center of mass).
# Y increases downwards in Pygame.
# These points are roughly based on typical human joint locations, adjusted for
# a "sad, heavy" appearance and tucking for rolling.
#
# Index mapping for clarity (not used directly for list access in the code,
# but helps conceptualize which point is which):
# 0: Head
# 1: Neck
# 2: Right Shoulder, 3: Left Shoulder
# 4: Right Elbow, 5: Left Elbow
# 6: Right Wrist, 7: Left Wrist
# 8: Torso (approx. mid-spine/center of mass)
# 9: Right Hip, 10: Left Hip
# 11: Right Knee, 12: Left Knee
# 13: Right Ankle, 14: Left Ankle

# Base pose: Sad and hunched (standing/kneeling)
# Y values are relative to the torso (index 8) at (0,0).
BASE_POSE_RELATIVE_COORDS = [
    (0, -60),   # 0: Head
    (0, -45),   # 1: Neck
    (20, -30),  # 2: R Shoulder
    (-20, -30), # 3: L Shoulder
    (35, 0),    # 4: R Elbow
    (-35, 0),   # 5: L Elbow
    (40, 20),   # 6: R Wrist
    (-40, 20),  # 7: L Wrist
    (0, 0),     # 8: Torso (reference point)
    (15, 10),   # 9: R Hip
    (-15, 10),  # 10: L Hip
    (25, 40),   # 11: R Knee
    (-25, 40),  # 12: L Knee
    (30, 80),   # 13: R Ankle
    (-30, 80)   # 14: L Ankle
]

# Tucked pose: Curled into a compact ball, ready for rolling
TUCKED_POSE_RELATIVE_COORDS = [
    (0, -10),    # 0: Head
    (0, 0),      # 1: Neck (closer to body center)
    (10, 5),     # 2: R Shoulder
    (-10, 5),    # 3: L Shoulder
    (15, 10),    # 4: R Elbow
    (-15, 10),   # 5: L Elbow
    (15, 20),    # 6: R Wrist (arms drawn in)
    (-15, 20),   # 7: L Wrist
    (0, 0),      # 8: Torso (center of the "ball")
    (10, 15),    # 9: R Hip
    (-10, 15),   # 10: L Hip
    (10, 25),    # 11: R Knee (pulled up)
    (-10, 25),   # 12: L Knee
    (5, 30),     # 13: R Ankle (pulled up)
    (-5, 30)     # 14: L Ankle
]

# Unfurl pose: After rolling, returning to a similar state as base pose for smooth looping.
UNFURL_POSE_RELATIVE_COORDS = BASE_POSE_RELATIVE_COORDS

# Scaling factor to adjust the size of the figure on screen
POINT_DISPLAY_SCALE = 1.5

def lerp(a, b, t):
    """Linear interpolation between a and b by t (0-1)."""
    return a + (b - a) * t

def ease_in_out_quad(t):
    """Quadratic easing function for smoother transitions at start/end."""
    return t * t * (3 - 2 * t)

def get_current_pose_and_translation(frame_num, total_frames,
                                     base_pose, tucked_pose, unfurl_pose,
                                     total_roll_angle, roll_horizontal_dist,
                                     initial_center_x, initial_center_y):
    """
    Calculates the current relative joint positions and global translation
    based on the animation progress.
    """
    current_time_in_cycle = frame_num % total_frames
    
    # Define phase timings as fractions of total_frames
    tuck_phase_duration = total_frames * 0.25
    roll_phase_duration = total_frames * 0.50
    unfurl_phase_duration = total_frames * 0.25

    tuck_start = 0
    tuck_end = tuck_phase_duration
    roll_start = tuck_end
    roll_end = roll_start + roll_phase_duration
    unfurl_start = roll_end
    unfurl_end = unfurl_start + unfurl_phase_duration

    current_relative_pose = []
    
    # Determine the internal pose based on the animation phase
    if tuck_start <= current_time_in_cycle < tuck_end:
        # Phase 1: Tuck (interpolate from base to tucked pose)
        t = ease_in_out_quad((current_time_in_cycle - tuck_start) / tuck_phase_duration)
        for i in range(len(base_pose)):
            x = lerp(base_pose[i][0], tucked_pose[i][0], t)
            y = lerp(base_pose[i][1], tucked_pose[i][1], t)
            current_relative_pose.append((x, y))
        current_roll_angle = 0 # No rotation during tuck
    elif roll_start <= current_time_in_cycle < roll_end:
        # Phase 2: Rolling (maintain tucked pose, apply continuous rotation)
        roll_progress_in_phase = (current_time_in_cycle - roll_start) / roll_phase_duration
        current_roll_angle = ease_in_out_quad(roll_progress_in_phase) * total_roll_angle
        current_roll_angle = -current_roll_angle # Clockwise rotation for forward roll (Y-down)
        
        # The internal pose stays as the tucked pose
        current_relative_pose = list(tucked_pose) # Use list() for a shallow copy of the list of tuples
    else: # unfurl_start <= current_time_in_cycle < unfurl_end
        # Phase 3: Unfurl (interpolate from tucked pose back to unfurl pose)
        t = ease_in_out_quad((current_time_in_cycle - unfurl_start) / unfurl_phase_duration)
        for i in range(len(tucked_pose)):
            x = lerp(tucked_pose[i][0], unfurl_pose[i][0], t)
            y = lerp(tucked_pose[i][1], unfurl_pose[i][1], t)
            current_relative_pose.append((x, y))
        # Ensure no rotation is applied during unfurl or for final pose
        current_roll_angle = 0 
    
    # Apply global rotation to the relative points if in the rolling phase
    if roll_start <= current_time_in_cycle < roll_end:
        rotated_pose = []
        for px, py in current_relative_pose:
            # Rotate around the torso point (which is at (0,0) in relative coordinates)
            rotated_px = px * math.cos(current_roll_angle) - py * math.sin(current_roll_angle)
            rotated_py = px * math.sin(current_roll_angle) + py * math.cos(current_roll_angle)
            rotated_pose.append((rotated_px, rotated_py))
        current_relative_pose = rotated_pose

    # Calculate global horizontal translation for the entire cycle
    horizontal_progress_overall = current_time_in_cycle / total_frames
    center_x = initial_center_x + horizontal_progress_overall * roll_horizontal_dist
    center_y = initial_center_y # Vertical position remains constant for simplicity of rolling

    return current_relative_pose, (center_x, center_y)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sadman Rolling Stimulus")
    clock = pygame.time.Clock()

    frame_count = 0

    # Initial screen position for the center of the person (torso)
    # Start slightly left of center, and low to suggest rolling on a surface
    initial_figure_center_x = SCREEN_WIDTH / 4
    initial_figure_center_y = SCREEN_HEIGHT * 0.7 

    # Total angle for rotation during the roll phase (e.g., 1.5 rotations = 3PI radians)
    total_rotation_in_radians = 2 * math.pi * NUM_ROLLS_PER_CYCLE

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Get the current pose (relative point coords) and global center position
        current_pose_relative, current_figure_center = get_current_pose_and_translation(
            frame_count, TOTAL_FRAMES,
            BASE_POSE_RELATIVE_COORDS, TUCKED_POSE_RELATIVE_COORDS, UNFURL_POSE_RELATIVE_COORDS,
            total_rotation_in_radians, ROLL_HORIZONTAL_DISTANCE,
            initial_figure_center_x, initial_figure_center_y
        )

        # Draw each point
        for px_rel, py_rel in current_pose_relative:
            # Scale and translate relative coordinates to screen coordinates
            screen_x = int(current_figure_center[0] + px_rel * POINT_DISPLAY_SCALE)
            screen_y = int(current_figure_center[1] + py_rel * POINT_DISPLAY_SCALE)
            pygame.draw.circle(screen, WHITE, (screen_x, screen_y), POINT_RADIUS)

        pygame.display.flip()

        frame_count += 1
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
