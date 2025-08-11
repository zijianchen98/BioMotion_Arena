
import pygame
import math

# --- Constants ---
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800  # Taller window to accommodate jump height
FPS = 60
POINT_RADIUS = 6     # Size of the white point-lights
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Body scale factor (adjusts overall size of the point figure)
BODY_SCALE = 100  # A base unit for body segment lengths, in pixels

# Define the 15 points representing major body joints
# This list ensures a consistent order for interpolation
POINT_NAMES = [
    "head", "neck",
    "shoulder_L", "shoulder_R",
    "elbow_L", "elbow_R",
    "wrist_L", "wrist_R",
    "pelvis",
    "knee_L", "knee_R",
    "ankle_L", "ankle_R",
    "toe_L", "toe_R"
]
NUM_POINTS = len(POINT_NAMES)  # Must be exactly 15

# Base X-coordinate for the center of the body (pelvis)
PELVIS_X_BASE = WINDOW_WIDTH / 2

# Relative positions for each point (x, y) at different keyframes.
# The origin (0,0) for these relative coordinates is the 'pelvis' point.
# Y-axis points downwards, as is common in Pygame.

# Keyframe 0: Standing (Neutral Pose)
relative_poses_kf0 = {
    "head": (0, -1.8 * BODY_SCALE),
    "neck": (0, -1.2 * BODY_SCALE),
    "shoulder_L": (-0.2 * BODY_SCALE, -1.1 * BODY_SCALE),
    "shoulder_R": (0.2 * BODY_SCALE, -1.1 * BODY_SCALE),
    "elbow_L": (-0.3 * BODY_SCALE, -0.6 * BODY_SCALE),
    "elbow_R": (0.3 * BODY_SCALE, -0.6 * BODY_SCALE),
    "wrist_L": (-0.25 * BODY_SCALE, -0.1 * BODY_SCALE),
    "wrist_R": (0.25 * BODY_SCALE, -0.1 * BODY_SCALE),
    "pelvis": (0, 0),
    "knee_L": (-0.15 * BODY_SCALE, 0.4 * BODY_SCALE),
    "knee_R": (0.15 * BODY_SCALE, 0.4 * BODY_SCALE),
    "ankle_L": (-0.15 * BODY_SCALE, 0.8 * BODY_SCALE),
    "ankle_R": (0.15 * BODY_SCALE, 0.8 * BODY_SCALE),
    "toe_L": (-0.15 * BODY_SCALE, 0.9 * BODY_SCALE),
    "toe_R": (0.15 * BODY_SCALE, 0.9 * BODY_SCALE),
}

# Keyframe 1: Crouch (Preparation for jump) - Body lowers, knees bend, arms slightly back
relative_poses_kf1 = {
    "head": (0, -1.6 * BODY_SCALE),
    "neck": (0, -1.0 * BODY_SCALE),
    "shoulder_L": (-0.2 * BODY_SCALE, -0.9 * BODY_SCALE),
    "shoulder_R": (0.2 * BODY_SCALE, -0.9 * BODY_SCALE),
    "elbow_L": (-0.4 * BODY_SCALE, -0.3 * BODY_SCALE),
    "elbow_R": (0.4 * BODY_SCALE, -0.3 * BODY_SCALE),
    "wrist_L": (-0.3 * BODY_SCALE, 0.2 * BODY_SCALE),
    "wrist_R": (0.3 * BODY_SCALE, 0.2 * BODY_SCALE),
    "pelvis": (0, 0),
    "knee_L": (-0.2 * BODY_SCALE, 0.2 * BODY_SCALE),
    "knee_R": (0.2 * BODY_SCALE, 0.2 * BODY_SCALE),
    "ankle_L": (-0.2 * BODY_SCALE, 0.4 * BODY_SCALE),
    "ankle_R": (0.2 * BODY_SCALE, 0.4 * BODY_SCALE),
    "toe_L": (-0.2 * BODY_SCALE, 0.5 * BODY_SCALE),
    "toe_R": (0.2 * BODY_SCALE, 0.5 * BODY_SCALE),
}

# Keyframe 2: Extension (Push-off) - Body rapidly extends upwards, arms swing up
relative_poses_kf2 = {
    "head": (0, -1.9 * BODY_SCALE),
    "neck": (0, -1.3 * BODY_SCALE),
    "shoulder_L": (-0.1 * BODY_SCALE, -1.2 * BODY_SCALE),
    "shoulder_R": (0.1 * BODY_SCALE, -1.2 * BODY_SCALE),
    "elbow_L": (-0.1 * BODY_SCALE, -0.7 * BODY_SCALE),
    "elbow_R": (0.1 * BODY_SCALE, -0.7 * BODY_SCALE),
    "wrist_L": (-0.05 * BODY_SCALE, -0.2 * BODY_SCALE),
    "wrist_R": (0.05 * BODY_SCALE, -0.2 * BODY_SCALE),
    "pelvis": (0, 0),
    "knee_L": (-0.1 * BODY_SCALE, 0.6 * BODY_SCALE),
    "knee_R": (0.1 * BODY_SCALE, 0.6 * BODY_SCALE),
    "ankle_L": (-0.1 * BODY_SCALE, 1.0 * BODY_SCALE),
    "ankle_R": (0.1 * BODY_SCALE, 1.0 * BODY_SCALE),
    "toe_L": (-0.1 * BODY_SCALE, 1.1 * BODY_SCALE),
    "toe_R": (0.1 * BODY_SCALE, 1.1 * BODY_SCALE),
}

# Keyframe 3: Apex (Peak of jump, airborne, arms slightly raised for "happy" pose)
relative_poses_kf3 = {
    "head": (0, -1.7 * BODY_SCALE),
    "neck": (0, -1.1 * BODY_SCALE),
    "shoulder_L": (-0.2 * BODY_SCALE, -1.0 * BODY_SCALE),
    "shoulder_R": (0.2 * BODY_SCALE, -1.0 * BODY_SCALE),
    "elbow_L": (-0.3 * BODY_SCALE, -0.5 * BODY_SCALE),
    "elbow_R": (0.3 * BODY_SCALE, -0.5 * BODY_SCALE),
    "wrist_L": (-0.25 * BODY_SCALE, 0.0 * BODY_SCALE),
    "wrist_R": (0.25 * BODY_SCALE, 0.0 * BODY_SCALE),
    "pelvis": (0, 0),
    "knee_L": (-0.1 * BODY_SCALE, 0.3 * BODY_SCALE),
    "knee_R": (0.1 * BODY_SCALE, 0.3 * BODY_SCALE),
    "ankle_L": (-0.1 * BODY_SCALE, 0.6 * BODY_SCALE),
    "ankle_R": (0.1 * BODY_SCALE, 0.6 * BODY_SCALE),
    "toe_L": (-0.1 * BODY_SCALE, 0.7 * BODY_SCALE),
    "toe_R": (0.1 * BODY_SCALE, 0.7 * BODY_SCALE),
}

# Keyframe 4: Landing (Absorption) - Body lowers, knees bend to absorb impact
relative_poses_kf4 = {
    "head": (0, -1.65 * BODY_SCALE),
    "neck": (0, -1.05 * BODY_SCALE),
    "shoulder_L": (-0.25 * BODY_SCALE, -0.95 * BODY_SCALE),
    "shoulder_R": (0.25 * BODY_SCALE, -0.95 * BODY_SCALE),
    "elbow_L": (-0.35 * BODY_SCALE, -0.35 * BODY_SCALE),
    "elbow_R": (0.35 * BODY_SCALE, -0.35 * BODY_SCALE),
    "wrist_L": (-0.25 * BODY_SCALE, 0.15 * BODY_SCALE),
    "wrist_R": (0.25 * BODY_SCALE, 0.15 * BODY_SCALE),
    "pelvis": (0, 0),
    "knee_L": (-0.2 * BODY_SCALE, 0.25 * BODY_SCALE),
    "knee_R": (0.2 * BODY_SCALE, 0.25 * BODY_SCALE),
    "ankle_L": (-0.2 * BODY_SCALE, 0.45 * BODY_SCALE),
    "ankle_R": (0.2 * BODY_SCALE, 0.45 * BODY_SCALE),
    "toe_L": (-0.2 * BODY_SCALE, 0.55 * BODY_SCALE),
    "toe_R": (0.2 * BODY_SCALE, 0.55 * BODY_SCALE),
}

# Consolidate all keyframe relative poses into an ordered list of lists
# The last keyframe (index 5) returns to the standing pose (kf0) to complete the loop
all_keyframe_relative_poses = [
    [relative_poses_kf0[name] for name in POINT_NAMES],  # kf0: Standing
    [relative_poses_kf1[name] for name in POINT_NAMES],  # kf1: Crouch
    [relative_poses_kf2[name] for name in POINT_NAMES],  # kf2: Push-off/Extension
    [relative_poses_kf3[name] for name in POINT_NAMES],  # kf3: Apex
    [relative_poses_kf4[name] for name in POINT_NAMES],  # kf4: Landing/Absorption
    [relative_poses_kf0[name] for name in POINT_NAMES]   # kf5: Return to Standing (same as kf0)
]

# Global Y-coordinates for the pelvis at each keyframe
# These define the overall vertical movement of the person.
# Adjusted to represent "heavy woman" with moderate jump height.
PELVIS_Y_KEYFRAMES = [
    WINDOW_HEIGHT * 0.7,   # kf0: Standing ground level
    WINDOW_HEIGHT * 0.78,  # kf1: Crouch (lower than standing)
    WINDOW_HEIGHT * 0.68,  # kf2: Extension (just leaving ground)
    WINDOW_HEIGHT * 0.3,   # kf3: Apex (max jump height)
    WINDOW_HEIGHT * 0.75,  # kf4: Landing (lower than standing, absorbing impact)
    WINDOW_HEIGHT * 0.7    # kf5: Return to Standing
]

# Animation timing parameters
ANIMATION_DURATION_SECONDS = 2.5  # Total duration of one complete jump cycle.
                                   # Slightly slower for "heavy woman" feel.
TOTAL_FRAMES = int(ANIMATION_DURATION_SECONDS * FPS)

# Durations for each animation segment (proportion of total animation duration)
# These define the pacing of the jump phases.
SEGMENT_DURATIONS = [
    0.20,  # Stand to Crouch (preparation)
    0.20,  # Crouch to Push-off (building momentum)
    0.15,  # Push-off to Apex (fast ascent)
    0.25,  # Apex to Landing (gravity takes over, slower descent)
    0.10,  # Landing to Absorption (quick impact absorption)
    0.10   # Absorption to Stand (recovery)
]
# Ensure the sum is exactly 1.0, otherwise adjust slightly.
assert sum(SEGMENT_DURATIONS) - 1.0 < 1e-9, "Segment durations must sum to 1.0"

# --- Helper Functions ---
def lerp(a, b, t):
    """Linear interpolation between a and b."""
    return a + (b - a) * t

def ease_in_out_cubic(t):
    """Cubic ease-in-out function for smooth transitions (t from 0 to 1)."""
    return t * t * (3 - 2 * t)

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Woman Jumping")
clock = pygame.time.Clock()

# --- Game Loop ---
running = True
current_frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Calculate global animation progress (loops from 0 to 1)
    global_progress = (current_frame % TOTAL_FRAMES) / TOTAL_FRAMES

    # Determine current animation segment and local progress within that segment
    current_segment_idx = 0
    accumulated_duration_ratio = 0.0
    for i, duration_ratio in enumerate(SEGMENT_DURATIONS):
        # Check if global progress falls within the current segment
        # Or if it's the last segment (to catch any floating point inaccuracies)
        if global_progress < accumulated_duration_ratio + duration_ratio or i == len(SEGMENT_DURATIONS) - 1:
            current_segment_idx = i
            break
        accumulated_duration_ratio += duration_ratio

    # Calculate local progress (0 to 1) within the identified segment
    segment_start_progress = sum(SEGMENT_DURATIONS[:current_segment_idx])
    local_progress_raw = (global_progress - segment_start_progress) / SEGMENT_DURATIONS[current_segment_idx]
    
    # Apply easing function for smoother motion
    local_progress_eased = ease_in_out_cubic(local_progress_raw)

    # Interpolate the global Y position of the pelvis
    pelvis_y_start = PELVIS_Y_KEYFRAMES[current_segment_idx]
    pelvis_y_end = PELVIS_Y_KEYFRAMES[current_segment_idx + 1]
    current_pelvis_y = lerp(pelvis_y_start, pelvis_y_end, local_progress_eased)

    # Calculate and draw each of the 15 points
    for i in range(NUM_POINTS):
        # Get start and end relative positions for the current point
        point_start_pos = all_keyframe_relative_poses[current_segment_idx][i]
        point_end_pos = all_keyframe_relative_poses[current_segment_idx + 1][i]

        # Interpolate the point's relative (x, y) position
        interp_x = lerp(point_start_pos[0], point_end_pos[0], local_progress_eased)
        interp_y = lerp(point_start_pos[1], point_end_pos[1], local_progress_eased)

        # Convert relative interpolated position to absolute screen coordinates
        # by adding the global pelvis position
        abs_x = int(PELVIS_X_BASE + interp_x)
        abs_y = int(current_pelvis_y + interp_y)

        # Draw the white point-light
        pygame.draw.circle(screen, WHITE, (abs_x, abs_y), POINT_RADIUS)

    pygame.display.flip()

    # Advance frame and control frame rate
    current_frame += 1
    clock.tick(FPS)

pygame.quit()
