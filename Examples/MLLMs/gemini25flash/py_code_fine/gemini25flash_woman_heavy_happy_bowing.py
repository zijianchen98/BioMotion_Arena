
import pygame
import math

# --- Configuration ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
POINT_RADIUS = 4  # Size of the white point-lights
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30  # Frames per second for the animation

# Global scaling and offset for positioning the figure on the screen
GLOBAL_SCALE = 150  # Adjusts the overall size of the figure
# HIP_CENTER_Y defines the screen Y coordinate for the figure's hip line (relative Y=0)
# We calculate it so the feet are near the bottom of the screen.
# The lowest point (ankle) has a relative Y of 1.4 in BASE_POSE_RELATIVE.
# So, screen_ankle_y = HIP_CENTER_Y + 1.4 * GLOBAL_SCALE.
# If we want feet at Y=700, then HIP_CENTER_Y = 700 - (1.4 * GLOBAL_SCALE)
HIP_CENTER_X = SCREEN_WIDTH // 2
HIP_CENTER_Y = 700 - (1.4 * GLOBAL_SCALE) # Places feet at Y=700

# Duration for each transition between keyframes (in seconds)
DURATION_PER_KEYFRAME_SEC = 1.5 
FRAMES_PER_TRANSITION = int(FPS * DURATION_PER_KEYFRAME_SEC)

# --- Point Definitions ---
# Define the names and order of the 15 body points for consistent processing.
POINT_NAMES = [
    "head", "l_shoulder", "r_shoulder", "l_elbow", "r_elbow", "l_wrist", "r_wrist",
    "upper_torso", "lower_torso",
    "l_hip", "r_hip", "l_knee", "r_knee", "l_ankle", "r_ankle"
]

# Base (standing) pose relative coordinates.
# The origin (0,0) for these relative coordinates is set at the center of the hips.
# Y increases downwards, so points higher on the body have negative Y values.
BASE_POSE_RELATIVE = {
    "head": (0.0, -1.8),
    "l_shoulder": (-0.4, -1.3), "r_shoulder": (0.4, -1.3),
    "l_elbow": (-0.6, -0.7), "r_elbow": (0.6, -0.7),
    "l_wrist": (-0.7, -0.1), "r_wrist": (0.7, -0.1),
    "upper_torso": (0.0, -1.0),
    "lower_torso": (0.0, -0.5),
    "l_hip": (-0.2, 0.0), "r_hip": (0.2, 0.0), # Hips define the 'base' Y=0
    "l_knee": (-0.2, 0.7), "r_knee": (0.2, 0.7),
    "l_ankle": (-0.2, 1.4), "r_ankle": (0.2, 1.4),
}

# --- Utility Functions ---
def rotate_point(px, py, pivot_x, pivot_y, angle):
    """
    Rotates a point (px, py) around a pivot (pivot_x, pivot_y) by angle (radians).
    """
    s = math.sin(angle)
    c = math.cos(angle)

    # Translate point back to origin relative to pivot
    px -= pivot_x
    py -= pivot_y

    # Rotate point
    x_new = px * c - py * s
    y_new = px * s + py * c

    # Translate point back to original position relative to pivot
    return x_new + pivot_x, y_new + pivot_y

def create_bow_pose(angle_deg, hip_sink_y, knee_bend_y_shift, hip_forward_x_shift):
    """
    Generates a pose for bowing based on a target angle and shifts.
    - angle_deg: The forward bend angle of the upper body in degrees.
    - hip_sink_y: How much the hips (and thus the whole body) sink downwards.
    - knee_bend_y_shift: How much the knees (and lower legs) contribute to the sinking.
    - hip_forward_x_shift: How much the hips (and upper body) shift forward horizontally.
    """
    pose = {}
    angle_rad = math.radians(angle_deg)

    # Hip points are the approximate pivot for the main body bend.
    # We apply overall shifts to all points based on hip movement.
    hip_y_pivot = 0.0 # Relative Y where hips are in BASE_POSE_RELATIVE
    hip_x_center = 0.0 # Relative X where hips are centered

    for name in POINT_NAMES:
        rx, ry = BASE_POSE_RELATIVE[name]
        
        new_rx = rx
        new_ry = ry

        if "hip" in name:
            # Hips shift forward and sink
            new_rx += hip_forward_x_shift
            new_ry += hip_sink_y
        elif "knee" in name:
            # Knees shift forward slightly due to bend and sink
            knee_x_adjust = 0.05 * math.sin(angle_rad) # Small X shift for natural knee bend
            if "l_knee" in name: new_rx = rx - knee_x_adjust
            else: new_rx = rx + knee_x_adjust
            new_ry = ry + knee_bend_y_shift # Knee also lowers due to bend
        elif "ankle" in name:
            # Ankles stay relatively fixed, but slightly lower with knee bend
            new_ry = ry + knee_bend_y_shift * 0.5 # Ankles sink less than knees
        else: # Upper body (head, torso, shoulders, arms, etc.)
            # Rotate around the hip's base relative position (0,0)
            rotated_x, rotated_y = rotate_point(rx, ry, hip_x_center, hip_y_pivot, angle_rad)
            
            # Then apply the overall translation of the hip center to these rotated points
            new_rx = rotated_x + hip_forward_x_shift
            new_ry = rotated_y + hip_sink_y
            
        pose[name] = (new_rx, new_ry)
    return pose

# --- Keyframe Generation ---
# This list defines the sequence of poses for the animation cycle.
# Each pose is a dictionary mapping point names to their relative (x, y) coordinates.
ALL_KEYFRAMES = []

# 0. Standing Pose (initial and final state)
ALL_KEYFRAMES.append(BASE_POSE_RELATIVE)

# 1. Mid-Bowing Pose
# 30-degree bend, hips sink slightly, knees bend slightly, hips shift slightly forward.
ALL_KEYFRAMES.append(create_bow_pose(30, 0.1, 0.1, 0.05))

# 2. Deep Bowing Pose
# 70-degree bend, hips sink more, knees bend more, hips shift further forward.
ALL_KEYFRAMES.append(create_bow_pose(70, 0.25, 0.2, 0.15))

# 3. Return to Mid-Bowing (re-use previous mid-bow pose for symmetry)
ALL_KEYFRAMES.append(ALL_KEYFRAMES[1])

# 4. Return to Standing (re-use initial standing pose for a smooth loop)
ALL_KEYFRAMES.append(ALL_KEYFRAMES[0])

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Bowing Woman")
clock = pygame.time.Clock()

# --- Animation State Variables ---
current_transition_frame = 0  # Counter for frames within the current transition
current_segment_idx = 0       # Index of the starting keyframe for the current transition

# --- Main Animation Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK) # Clear the screen with black for each frame

    # Determine the start and end keyframes for the current interpolation segment.
    # The last keyframe (ALL_KEYFRAMES[-1]) is identical to the first (ALL_KEYFRAMES[0]),
    # ensuring a seamless loop. We transition through `len(ALL_KEYFRAMES) - 1` segments.
    start_keyframe_relative_coords = ALL_KEYFRAMES[current_segment_idx]
    end_keyframe_relative_coords = ALL_KEYFRAMES[(current_segment_idx + 1) % len(ALL_KEYFRAMES)]

    # Calculate the interpolation factor (alpha) from 0.0 to 1.0.
    # 0.0 means at start_keyframe, 1.0 means at end_keyframe.
    alpha = current_transition_frame / FRAMES_PER_TRANSITION

    current_screen_points = []
    # Interpolate each point's position
    for name in POINT_NAMES:
        p1_rel = start_keyframe_relative_coords[name]
        p2_rel = end_keyframe_relative_coords[name]
        
        # Linear interpolation of relative coordinates
        interp_x_rel = p1_rel[0] * (1 - alpha) + p2_rel[0] * alpha
        interp_y_rel = p1_rel[1] * (1 - alpha) + p2_rel[1] * alpha
        
        # Convert relative coordinates to absolute screen coordinates
        screen_x = HIP_CENTER_X + interp_x_rel * GLOBAL_SCALE
        screen_y = HIP_CENTER_Y + interp_y_rel * GLOBAL_SCALE
        
        current_screen_points.append((int(screen_x), int(screen_y)))

    # Draw all the interpolated points on the screen
    for point_coord in current_screen_points:
        pygame.draw.circle(screen, WHITE, point_coord, POINT_RADIUS)

    pygame.display.flip() # Update the full display Surface to the screen

    # Advance animation state
    current_transition_frame += 1
    if current_transition_frame >= FRAMES_PER_TRANSITION:
        current_transition_frame = 0 # Reset frame counter for next segment
        # Move to the next segment. The modulo operation ensures looping back to 0.
        # We subtract 1 from len(ALL_KEYFRAMES) because the last segment transitions
        # from the second-to-last keyframe to the *last* keyframe (which is also the first).
        current_segment_idx = (current_segment_idx + 1) % (len(ALL_KEYFRAMES) - 1) 

    clock.tick(FPS) # Control the frame rate

pygame.quit()
