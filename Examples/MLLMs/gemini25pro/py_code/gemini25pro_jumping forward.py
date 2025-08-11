
import pygame
import sys

# --- Constants ---
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 4

# --- Keyframe Data ---
# The animation is defined by a series of key poses and the trajectory of a root point (pelvis).
# The full animation is pre-calculated by interpolating between these keyframes.

# There are exactly 15 points, representing major joints. The order is consistent across all poses:
# 0: Head, 1: Neck, 2: L Shoulder, 3: R Shoulder, 4: L Elbow, 5: R Elbow,
# 6: L Wrist, 7: R Wrist, 8: Pelvis, 9: L Hip, 10: R Hip, 11: L Knee, 12: R Knee,
# 13: L Ankle, 14: R Ankle
#
# All pose coordinates are relative to the Pelvis point (index 8), which acts as the origin.
# The poses incorporate a slight side-on view by offsetting the X-coordinates of left/right limbs.

# Key Pose 0: Standing
pose0 = [
    (5, -90),    # Head
    (5, -70),    # Neck
    (-15, -65),  # L Shoulder
    (25, -65),   # R Shoulder
    (-20, -30),  # L Elbow
    (30, -30),   # R Elbow
    (-22, 10),   # L Wrist
    (32, 10),    # R Wrist
    (0, 0),      # Pelvis (origin for relative coordinates)
    (-15, 5),    # L Hip
    (15, 5),     # R Hip
    (-18, 55),   # L Knee
    (18, 55),    # R Knee
    (-20, 100),  # L Ankle
    (20, 100),   # R Ankle
]

# Key Pose 1: Crouch (preparation for jump)
pose1 = [
    (20, -85),   # Head
    (15, -65),   # Neck
    (-5, -60),   # L Shoulder
    (35, -60),   # R Shoulder
    (-30, -30),  # L Elbow (swinging back)
    (20, -30),   # R Elbow (swinging back)
    (-40, 0),    # L Wrist
    (10, 0),     # R Wrist
    (0, 0),      # Pelvis
    (-15, 5),    # L Hip
    (15, 5),     # R Hip
    (-25, 35),   # L Knee (bent)
    (25, 35),    # R Knee (bent)
    (-22, 60),   # L Ankle
    (22, 60),    # R Ankle
]

# Key Pose 2: Takeoff (fully extended)
pose2 = [
    (30, -95),   # Head
    (25, -75),   # Neck
    (5, -70),    # L Shoulder
    (45, -70),   # R Shoulder
    (15, -40),   # L Elbow (swinging forward)
    (55, -40),   # R Elbow (swinging forward)
    (25, -10),   # L Wrist
    (65, -10),   # R Wrist
    (0, 0),      # Pelvis
    (-15, 5),    # L Hip
    (15, 5),     # R Hip
    (-5, 50),    # L Knee (extending)
    (25, 50),    # R Knee (extending)
    (0, 95),     # L Ankle (pushing off)
    (30, 95),    # R Ankle (pushing off)
]

# Key Pose 3: Apex (tucked in mid-air)
pose3 = [
    (10, -60),   # Head
    (10, -40),   # Neck
    (-10, -35),  # L Shoulder
    (30, -35),   # R Shoulder
    (-15, -10),  # L Elbow
    (35, -10),   # R Elbow
    (-10, 20),   # L Wrist
    (40, 20),    # R Wrist
    (0, 0),      # Pelvis
    (-15, 5),    # L Hip
    (15, 5),     # R Hip
    (-10, 30),   # L Knee (tucked)
    (20, 30),    # R Knee (tucked)
    (-20, 55),   # L Ankle
    (10, 55),    # R Ankle
]

# Key Pose 4: Landing Preparation (legs extending down)
pose4 = [
    (20, -85),   # Head
    (15, -65),   # Neck
    (-5, -60),   # L Shoulder
    (35, -60),   # R Shoulder
    (-25, -30),  # L Elbow (out for balance)
    (55, -30),   # R Elbow (out for balance)
    (-40, 0),    # L Wrist
    (70, 0),     # R Wrist
    (0, 0),      # Pelvis
    (-15, 5),    # L Hip
    (15, 5),     # R Hip
    (-15, 45),   # L Knee (extending for landing)
    (25, 45),    # R Knee (extending for landing)
    (-12, 90),   # L Ankle
    (28, 90),    # R Ankle
]

# Key Pose 5: Landed Crouch (absorbing impact, same as crouch)
pose5 = pose1

# Key Pose 6: Final Stand (recovering, same as stand)
pose6 = pose0

# Assemble keyframes, their timings, and the trajectory of the pelvis.
keyframes = [pose0, pose1, pose2, pose3, pose4, pose5, pose6]
keyframe_times = [0, 20, 30, 60, 90, 105, 125]
keyframe_pelvis_pos = [
    (150, 450),  # Start
    (160, 480),  # Crouch
    (180, 450),  # Takeoff
    (350, 250),  # Apex
    (520, 450),  # Land
    (530, 480),  # Absorb
    (540, 450),  # Stand
]

def lerp(a, b, t):
    """Linearly interpolates between values a and b by a factor t."""
    return a + (b - a) * t

def lerp_point(p1, p2, t):
    """Linearly interpolates between two 2D points."""
    return (lerp(p1[0], p2[0], t), lerp(p1[1], p2[1], t))

def ease_in_out_quad(t):
    """An easing function for smooth acceleration and deceleration."""
    return 2 * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 2) / 2

def generate_all_frames():
    """Pre-calculates the coordinates for all points for every frame of the animation."""
    all_frames = []
    total_duration = keyframe_times[-1]

    for frame_num in range(total_duration):
        # Find which two keyframes the current frame is between
        for i in range(len(keyframe_times) - 1):
            if keyframe_times[i] <= frame_num < keyframe_times[i+1]:
                start_keyframe_idx, end_keyframe_idx = i, i + 1
                break
        
        start_time = keyframe_times[start_keyframe_idx]
        end_time = keyframe_times[end_keyframe_idx]
        segment_duration = end_time - start_time
        
        # Calculate interpolation factor 't' (0 to 1) within the segment
        t = (frame_num - start_time) / segment_duration if segment_duration != 0 else 0
        eased_t = ease_in_out_quad(t)

        # Interpolate the pelvis's global position to get the root of the figure
        start_pos = keyframe_pelvis_pos[start_keyframe_idx]
        end_pos = keyframe_pelvis_pos[end_keyframe_idx]
        current_pelvis_pos = lerp_point(start_pos, end_pos, eased_t)

        # Interpolate the relative positions for each point in the pose
        start_pose = keyframes[start_keyframe_idx]
        end_pose = keyframes[end_keyframe_idx]
        
        current_frame_points = []
        for j in range(len(start_pose)):
            rel_start = start_pose[j]
            rel_end = end_pose[j]
            
            # Interpolate the relative position of the point
            rel_point = lerp_point(rel_start, rel_end, eased_t)
            
            # Add the interpolated relative position to the pelvis's global position
            # This works for the pelvis itself because its relative position is always (0,0).
            abs_point = (current_pelvis_pos[0] + rel_point[0], current_pelvis_pos[1] + rel_point[1])
            current_frame_points.append(abs_point)
            
        all_frames.append(current_frame_points)

    return all_frames

def main():
    """Initializes Pygame and runs the main animation loop."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Jumping Forward")
    clock = pygame.time.Clock()

    all_frames = generate_all_frames()
    num_frames = len(all_frames)
    current_frame_index = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # --- Draw ---
        screen.fill(BLACK)
        
        if num_frames > 0:
            current_points = all_frames[current_frame_index]
            for point in current_points:
                pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), POINT_RADIUS)
        
        pygame.display.flip()

        # --- Update ---
        current_frame_index = (current_frame_index + 1) % num_frames
        
        # --- Timing ---
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
