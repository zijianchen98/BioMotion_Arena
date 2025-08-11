
import pygame
import math

# --- Configuration ---
WIDTH, HEIGHT = 800, 600
FPS = 30
DOT_RADIUS = 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Human Body Model (15 points) ---
# Points are identified by an index 0-14.
# (0,0) for relative coordinates is defined as the PELVIS (point 8).
# Y-coordinates: smaller = higher on screen (standard Pygame coordinate system).
# X-coordinates: positive = right on screen (forward direction for the figure).

# Point mapping:
# 0: Head
# 1: Right Shoulder (from the person's perspective)
# 2: Left Shoulder
# 3: Right Elbow
# 4: Left Elbow
# 5: Right Wrist
# 6: Left Wrist
# 7: Sternum (center of chest)
# 8: Pelvis (center of hips - serves as the relative origin for the body's pose)
# 9: Right Hip (outer / greater trochanter)
# 10: Left Hip (outer / greater trochanter)
# 11: Right Knee
# 12: Left Knee
# 13: Right Ankle
# 14: Left Ankle

# Keyframes for 'jumping forward' animation
# Each keyframe is a dictionary mapping point index to its relative (x, y) coordinate.
# These coordinates define the shape of the body relative to its pelvis.

standing_pose = {
    0: (0, -150),  # Head
    1: (40, -100),  # R Shoulder
    2: (-40, -100), # L Shoulder
    3: (50, -50),   # R Elbow
    4: (-50, -50),  # L Elbow
    5: (60, 0),     # R Wrist
    6: (-60, 0),    # L Wrist
    7: (0, -80),    # Sternum
    8: (0, 0),      # Pelvis (relative origin)
    9: (30, 20),    # R Hip
    10: (-30, 20),   # L Hip
    11: (30, 70),    # R Knee
    12: (-30, 70),   # L Knee
    13: (30, 120),   # R Ankle
    14: (-30, 120),  # L Ankle
}

crouch_pose = {
    0: (0, -100),  # Head (lower, preparing for jump)
    1: (40, -60),   # R Shoulder
    2: (-40, -60),  # L Shoulder
    3: (50, -10),   # R Elbow
    4: (-50, -10),  # L Elbow
    5: (60, 40),    # R Wrist (arms swung slightly back/down for momentum)
    6: (-60, 40),   # L Wrist
    7: (0, -40),    # Sternum (lower)
    8: (0, 0),      # Pelvis
    9: (30, 20),    # R Hip
    10: (-30, 20),   # L Hip
    11: (30, 100),   # R Knee (more bent)
    12: (-30, 100),  # L Knee
    13: (30, 140),   # R Ankle
    14: (-30, 140),  # L Ankle
}

takeoff_pose = {
    0: (50, -160),  # Head (forward and up)
    1: (80, -120),  # R Shoulder (forward drive)
    2: (-20, -120), # L Shoulder (slightly back/up for counter-balance)
    3: (100, -60),  # R Elbow (extended forward)
    4: (-50, -60),  # L Elbow
    5: (120, -20),  # R Wrist
    6: (-70, -20),  # L Wrist
    7: (30, -90),   # Sternum (forward/up)
    8: (0, 0),      # Pelvis
    9: (10, 0),     # R Hip (legs driving back to propel)
    10: (-10, 0),   # L Hip
    11: (-30, 50),   # R Knee (more extended backward)
    12: (30, 50),   # L Knee (more extended backward)
    13: (-50, 100),  # R Ankle (pushing off, trailing)
    14: (50, 100),   # L Ankle (pushing off, trailing)
}

peak_jump_pose = {
    0: (80, -120),  # Head (forward, maintaining height)
    1: (90, -80),   # R Shoulder
    2: (-10, -80),  # L Shoulder
    3: (100, -30),  # R Elbow
    4: (-20, -30),  # L Elbow
    5: (110, 20),   # R Wrist
    6: (-30, 20),   # L Wrist
    7: (50, -60),   # Sternum (forward)
    8: (0, 0),      # Pelvis
    9: (10, 20),    # R Hip (legs tucked for aerodynamic/balance)
    10: (-10, 20),   # L Hip
    11: (10, 60),    # R Knee (bent, tucked)
    12: (-10, 60),   # L Knee
    13: (10, 90),    # R Ankle (tucked)
    14: (-10, 90),   # L Ankle
}

landing_pose = {
    0: (100, -100), # Head (forward, preparing for impact)
    1: (110, -60),  # R Shoulder
    2: (10, -60),   # L Shoulder
    3: (120, -10),  # R Elbow
    4: (0, -10),    # L Elbow
    5: (130, 40),   # R Wrist
    6: (-10, 40),   # L Wrist
    7: (70, -40),   # Sternum
    8: (0, 0),      # Pelvis
    9: (30, 20),    # R Hip
    10: (-30, 20),   # L Hip
    11: (30, 100),   # R Knee (bent to absorb impact)
    12: (-30, 100),  # L Knee
    13: (30, 140),   # R Ankle
    14: (-30, 140),  # L Ankle
}

# Sequence of keyframes and their durations (in frames)
# Each tuple is (pose_dictionary, duration_in_frames)
keyframes_sequence = [
    (standing_pose, 30), # Start, hold for 1 second (30 frames @ 30 FPS)
    (crouch_pose, 20),   # Crouch (0.66 seconds)
    (takeoff_pose, 15),  # Take-off (0.5 seconds)
    (peak_jump_pose, 20),# Airborne (0.66 seconds)
    (landing_pose, 15),  # Landing (0.5 seconds)
    (standing_pose, 30), # Return to standing position after landing (before looping)
]

# Define the absolute (x,y) screen coordinates for the PELVIS (point 8)
# at the beginning of each keyframe segment. These values control the
# overall global trajectory (forward and vertical movement) of the entire figure.
pelvis_trajectory_x = [
    WIDTH // 4,            # standing_pose start X
    WIDTH // 4,            # crouch_pose X (same X as start, only Y changes)
    WIDTH // 4 + 100,      # takeoff_pose X (moving significantly forward)
    WIDTH // 4 + 250,      # peak_jump_pose X (further forward, highest X gain)
    WIDTH // 4 + 400,      # landing_pose X (even further forward)
    WIDTH // 4 + 450       # end standing X (final forward position before loop resets)
]
pelvis_trajectory_y = [
    HEIGHT * 0.75,         # standing_pose start Y (ground level)
    HEIGHT * 0.75 + 30,    # crouch_pose Y (pelvis sinks down)
    HEIGHT * 0.75 - 80,    # takeoff_pose Y (pelvis moves up sharply)
    HEIGHT * 0.75 - 150,   # peak_jump_pose Y (pelvis reaches highest point)
    HEIGHT * 0.75 + 30,    # landing_pose Y (pelvis sinks down to absorb impact)
    HEIGHT * 0.75          # end standing Y (pelvis returns to ground level)
]

# Scale factor for the figure's size. Multiplies the relative coordinates.
# A value of 1.0 means 1:1 scale of the relative units. 1.2 makes it 20% larger.
SCALE = 1.2 

# Animation state variables
current_keyframe_idx = 0
frame_in_current_keyframe = 0

# --- Interpolation function ---
def cosine_interpolation(a, b, alpha):
    """
    Performs cosine interpolation between values 'a' and 'b' based on 'alpha'.
    Alpha should be between 0.0 and 1.0.
    Provides smoother transitions than linear interpolation by using a cosine curve.
    """
    alpha_prime = (1 - math.cos(alpha * math.pi)) / 2
    return a + (b - a) * alpha_prime

def interpolate_pose(pose1, pose2, alpha):
    """
    Interpolates between two pose dictionaries.
    Each pose dictionary contains (x, y) coordinates for 15 points.
    Uses cosine interpolation for smooth movement of individual points within the body.
    """
    interpolated_pose = {}
    for i in range(15):
        x1, y1 = pose1[i]
        x2, y2 = pose2[i]
        interpolated_x = cosine_interpolation(x1, x2, alpha)
        interpolated_y = cosine_interpolation(y1, y2, alpha)
        interpolated_pose[i] = (interpolated_x, interpolated_y)
    return interpolated_pose

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Jumping Forward")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK) # Clear screen with solid black background

    # Get data for the current keyframe and the next keyframe in the sequence
    current_pose_dict, current_duration = keyframes_sequence[current_keyframe_idx]
    
    next_keyframe_idx = (current_keyframe_idx + 1) % len(keyframes_sequence)
    next_pose_dict, _ = keyframes_sequence[next_keyframe_idx]

    # Calculate the interpolation alpha for the current segment (progress from 0.0 to 1.0)
    # This alpha determines how far along the transition we are between current_pose and next_pose.
    alpha_segment = frame_in_current_keyframe / current_duration if current_duration > 0 else 1.0

    # Interpolate the relative body pose (i.e., the shape of the human figure)
    current_interpolated_figure_relative = interpolate_pose(current_pose_dict, next_pose_dict, alpha_segment)

    # Interpolate the global pelvis position (i.e., the overall movement/trajectory of the figure)
    current_pelvis_x = cosine_interpolation(
        pelvis_trajectory_x[current_keyframe_idx],
        pelvis_trajectory_x[next_keyframe_idx],
        alpha_segment
    )
    current_pelvis_y = cosine_interpolation(
        pelvis_trajectory_y[current_keyframe_idx],
        pelvis_trajectory_y[next_keyframe_idx],
        alpha_segment
    )

    # Draw each of the 15 points
    for i in range(15):
        # Get the relative (x, y) coordinates for the current point from the interpolated pose
        relative_x, relative_y = current_interpolated_figure_relative[i]
        
        # Apply the global scaling factor to the relative coordinates
        scaled_relative_x = relative_x * SCALE
        scaled_relative_y = relative_y * SCALE
        
        # Add the global pelvis position to get the final screen coordinates for the point
        # Since the pelvis point (index 8) itself has relative (0,0) in all pose dictionaries,
        # its final display position will directly be (current_pelvis_x, current_pelvis_y).
        display_x = int(current_pelvis_x + scaled_relative_x)
        display_y = int(current_pelvis_y + scaled_relative_y)
        
        # Draw the white point-light on the screen
        pygame.draw.circle(screen, WHITE, (display_x, display_y), DOT_RADIUS)

    # Update frame counters for the animation loop
    frame_in_current_keyframe += 1

    # Check if it's time to transition to the next keyframe segment
    if frame_in_current_keyframe >= current_duration:
        frame_in_current_keyframe = 0 # Reset frame counter for the new keyframe segment
        current_keyframe_idx = next_keyframe_idx # Move to the next keyframe in the sequence

    pygame.display.flip() # Update the entire screen to show the newly drawn frame
    clock.tick(FPS) # Control the animation speed to match the desired frames per second

pygame.quit() # Uninitialize all pygame modules when the loop ends
