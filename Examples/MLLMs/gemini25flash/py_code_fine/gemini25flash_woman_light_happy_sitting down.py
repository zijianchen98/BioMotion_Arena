
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60
POINT_RADIUS = 5 # Size of the white point-lights
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CENTER_X = SCREEN_WIDTH // 2 # Center X-coordinate for the skeleton

# Define the relative positions of the 15 points for each key pose.
# Coordinates are relative to the pelvis_center (which is treated as (0,0) locally).
# Y-axis points downwards, X-axis points right.
# These values are chosen to represent plausible human anatomy and movement.
# The "light weight" aspect is reflected in the generally slender proportions.

# Base scale for the relative coordinates. Adjust if the figure is too small/large.
SCALE_FACTOR = 1.0

# Key Pose 1: Standing upright
STANDING_POSE_REL = {
    "head": (0, -180),
    "neck": (0, -150),
    "left_shoulder": (-40, -130),
    "right_shoulder": (40, -130),
    "left_elbow": (-50, -80),
    "right_elbow": (50, -80),
    "left_wrist": (-60, -30),
    "right_wrist": (60, -30),
    "mid_torso": (0, -90), # A central point representing the chest/upper spine
    "left_hip": (-30, 0), # Pelvis center is (0,0) for relative coordinates
    "right_hip": (30, 0),
    "left_knee": (-30, 90),
    "right_knee": (30, 90),
    "left_ankle": (-30, 180),
    "right_ankle": (30, 180)
}

# Key Pose 2: Mid-squat/Transitioning down
MID_SIT_POSE_REL = {
    "head": (0, -120), # Head moves down and slightly forward (implied by less negative Y)
    "neck": (0, -100),
    "left_shoulder": (-45, -90), # Arms slightly forward and down
    "right_shoulder": (45, -90),
    "left_elbow": (-55, -40),
    "right_elbow": (55, -40),
    "left_wrist": (-65, 10), # Wrists further forward relative to body
    "right_wrist": (65, 10),
    "mid_torso": (0, -60), # Torso bends forward
    "left_hip": (-35, 0), # Hips slightly wider and potentially slightly back
    "right_hip": (35, 0),
    "left_knee": (-50, 40), # Knees move significantly forward and up (relative to pelvis)
    "right_knee": (50, 40),
    "left_ankle": (-40, 100), # Ankles move forward
    "right_ankle": (40, 100)
}

# Key Pose 3: Fully sitting
SITTING_POSE_REL = {
    "head": (0, -80), # Head more upright
    "neck": (0, -60),
    "left_shoulder": (-35, -50), # Arms more relaxed, closer to body
    "right_shoulder": (35, -50),
    "left_elbow": (-40, 0),
    "right_elbow": (40, 0),
    "left_wrist": (-45, 40), # Wrists lower
    "right_wrist": (45, 40),
    "mid_torso": (0, -30), # Torso relatively upright now
    "left_hip": (-30, 0), # Hips back to original width, but body much lower
    "right_hip": (30, 0),
    "left_knee": (-30, 40), # Knees at approximate 90-degree angle
    "right_knee": (30, 40),
    "left_ankle": (-30, 40), # Ankles directly below knees (or slightly forward)
    "right_ankle": (30, 40)
}

# Absolute Y-coordinates for the pelvis_center for each key pose.
# These define the overall vertical movement of the person on the screen.
PELVIS_Y_KEYFRAMES = [
    SCREEN_HEIGHT * 0.5,   # Standing: Pelvis is around the vertical center of the screen
    SCREEN_HEIGHT * 0.65,  # Mid-squat: Pelvis moves down
    SCREEN_HEIGHT * 0.8,   # Sitting: Pelvis is low, closer to the bottom of the screen
]

# Total duration for the "sitting down" or "standing up" phase in seconds
PHASE_DURATION = 1.0 # Each phase (down or up) takes 1 second
LOOP_DURATION = PHASE_DURATION * 2 # Total duration for one full cycle (down and up)

# --- Helper Functions for Animation ---
def lerp(a, b, t):
    """Linear interpolation between a and b by factor t (0.0 to 1.0)."""
    return a * (1 - t) + b * t

def smoothstep(t):
    """Smoother interpolation curve for 't' (0.0 to 1.0).
    Provides natural acceleration and deceleration."""
    return t * t * (3 - 2 * t)

def get_current_pose(progress):
    """
    Calculates the interpolated pose and overall Y-position based on animation progress.
    'progress' is between 0.0 (standing) and 1.0 (sitting).
    """
    current_pose_rel = {}
    current_pelvis_y = 0

    if progress <= 0.5:
        # Phase 1: Standing to Mid-squat
        # Normalize progress for this phase from 0 to 1
        t_phase = progress * 2
        eased_t = smoothstep(t_phase)

        # Interpolate relative joint positions
        for joint in STANDING_POSE_REL:
            start_x, start_y = STANDING_POSE_REL[joint]
            end_x, end_y = MID_SIT_POSE_REL[joint]
            current_pose_rel[joint] = (
                lerp(start_x, end_x, eased_t),
                lerp(start_y, end_y, eased_t)
            )
        # Interpolate overall vertical position
        current_pelvis_y = lerp(PELVIS_Y_KEYFRAMES[0], PELVIS_Y_KEYFRAMES[1], eased_t)

    else:
        # Phase 2: Mid-squat to Sitting
        # Normalize progress for this phase from 0 to 1
        t_phase = (progress - 0.5) * 2
        eased_t = smoothstep(t_phase)

        # Interpolate relative joint positions
        for joint in MID_SIT_POSE_REL:
            start_x, start_y = MID_SIT_POSE_REL[joint]
            end_x, end_y = SITTING_POSE_REL[joint]
            current_pose_rel[joint] = (
                lerp(start_x, end_x, eased_t),
                lerp(start_y, end_y, eased_t)
            )
        # Interpolate overall vertical position
        current_pelvis_y = lerp(PELVIS_Y_KEYFRAMES[1], PELVIS_Y_KEYFRAMES[2], eased_t)

    return current_pose_rel, current_pelvis_y

def get_drawing_coordinates(pose_rel, pelvis_y):
    """
    Converts relative pose coordinates (from get_current_pose)
    to absolute screen coordinates, applying the global position and scale.
    """
    absolute_coords = {}
    for joint, (rel_x, rel_y) in pose_rel.items():
        # Apply scaling and convert to absolute screen coordinates
        abs_x = CENTER_X + (rel_x * SCALE_FACTOR)
        abs_y = pelvis_y + (rel_y * SCALE_FACTOR)
        absolute_coords[joint] = (int(abs_x), int(abs_y)) # Cast to int for drawing
    return absolute_coords

# --- Main Program ---
def main():
    pygame.init() # Initialize all the Pygame modules

    # Set up the display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sitting Down") # Window title

    clock = pygame.time.Clock() # To control the frame rate

    running = True # Main loop control variable
    start_time = pygame.time.get_ticks() # Get the starting time in milliseconds

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # Stop the loop if the user closes the window

        # Calculate the current time relative to the animation start
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000.0 # Convert to seconds

        # Determine the animation progress (0.0 to 1.0) for a full down-and-up cycle
        # The modulo operator ensures the animation loops
        loop_progress = (elapsed_time % LOOP_DURATION) / LOOP_DURATION

        # Map loop_progress to animation_progress (0.0 to 1.0 for sitting down, then 1.0 to 0.0 for standing up)
        if loop_progress <= 0.5:
            # Sitting down phase: animation_progress goes from 0.0 to 1.0
            animation_progress = loop_progress * 2
        else:
            # Standing up phase: animation_progress goes from 1.0 to 0.0 (by reversing the second half)
            animation_progress = (1.0 - loop_progress) * 2

        # Clamp animation_progress to ensure it stays within [0, 1] due to potential float inaccuracies
        animation_progress = max(0.0, min(1.0, animation_progress))

        # Get the current interpolated relative pose and overall Y-offset
        current_pose_rel, current_pelvis_y = get_current_pose(animation_progress)

        # Convert relative pose to absolute screen coordinates for drawing
        drawing_coords = get_drawing_coordinates(current_pose_rel, current_pelvis_y)

        # --- Drawing ---
        screen.fill(BLACK) # Fill the background with black

        # Draw each of the 15 points
        # The keys correspond to the joint names, ensuring 15 points are drawn.
        for joint_name, (x, y) in drawing_coords.items():
            pygame.draw.circle(screen, WHITE, (x, y), POINT_RADIUS)

        pygame.display.flip() # Update the full display Surface to the screen
        clock.tick(FPS) # Control the frame rate

    pygame.quit() # Uninitialize Pygame modules

if __name__ == "__main__":
    main()
