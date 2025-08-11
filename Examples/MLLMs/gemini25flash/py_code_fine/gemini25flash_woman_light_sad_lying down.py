
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
POINT_RADIUS = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Global offset for drawing the entire figure on screen.
# This point (SCREEN_OFFSET_X, SCREEN_OFFSET_Y) will correspond to the (0,0) reference
# point for all relative coordinates defined in the keyframe poses (specifically, the MID_TORSO point
# in the STANDING_POSE_REL).
SCREEN_OFFSET_X = SCREEN_WIDTH // 2
SCREEN_OFFSET_Y = int(SCREEN_HEIGHT * 0.7)  # Y position for the standing person's mid-torso/pelvis

# Easing function for smooth transitions (smoothstep variant)
# This function takes a linear progress 't' (0 to 1) and returns an eased progress.
def ease_in_out_quad(t):
    if t < 0.5:
        return 2 * t * t
    else:
        return -2 * t * t + 4 * t - 1

# --- Joint Indices ---
# These indices are used to refer to specific points in the `current_points` list
# and in the keyframe pose definitions.
HEAD = 0
NECK = 1
R_SHOULDER = 2
L_SHOULDER = 3
R_ELBOW = 4
L_ELBOW = 5
R_WRIST = 6
L_WRIST = 7
MID_TORSO = 8  # This serves as the anchor point (0,0) for the STANDING_POSE_REL
R_HIP = 9
L_HIP = 10
R_KNEE = 11
L_KNEE = 12
R_ANKLE = 13
L_ANKLE = 14

# --- Keyframe Poses (relative coordinates) ---
# Each pose is a list of (x, y) tuples, representing the relative position of each
# of the 15 points from the `MID_TORSO` point of the standing figure (which is at (0,0)
# in the STANDING_POSE_REL). The global SCREEN_OFFSET_X/Y is added when drawing.
# The Y-axis is positive downwards, consistent with Pygame's coordinate system.
# Proportions are set to represent a 'sadwoman with light weight' - slightly slender.

STANDING_POSE_REL = [
    (0, -170),  # Head (topmost)
    (0, -130),  # Neck (below head)
    (-30, -120), # R_Shoulder
    (30, -120),  # L_Shoulder
    (-50, -60),  # R_Elbow (arms slightly bent, by sides)
    (50, -60),   # L_Elbow
    (-60, 0),    # R_Wrist (aligned with or slightly forward of hips)
    (60, 0),     # L_Wrist
    (0, 0),      # MID_TORSO (our reference (0,0) point for relative coords)
    (-20, 20),   # R_Hip
    (20, 20),    # L_Hip
    (-20, 80),   # R_Knee
    (20, 80),    # L_Knee
    (-20, 140),  # R_Ankle (feet at bottom)
    (20, 140)    # L_Ankle
]

# Squatting pose: The body lowers, knees bend significantly. Arms may come forward for balance.
# The relative Y coordinates are adjusted to simulate the overall downward shift of the body.
SQUATTING_POSE_REL = [
    (0, -80 + 70),   # Head (lowered by ~70 relative to standing head)
    (0, -40 + 70),   # Neck
    (-30, -30 + 70), # R_Shoulder
    (30, -30 + 70),  # L_Shoulder
    (-20, 10 + 70),  # R_Elbow (arms forward for balance)
    (20, 10 + 70),   # L_Elbow
    (-10, 50 + 70),  # R_Wrist
    (10, 50 + 70),   # L_Wrist
    (0, 50 + 70),    # MID_TORSO (lowered by ~70 relative to standing mid-torso)
    (-20, 70 + 70),  # R_Hip
    (20, 70 + 70),   # L_Hip
    (-20, 100 + 70), # R_Knee (more bent relative to hip)
    (20, 100 + 70),  # L_Knee
    (-20, 140 + 70), # R_Ankle (feet stay close to original ground level, but body descended)
    (20, 140 + 70)   # L_Ankle
]

# Lying pose: The body is mostly flat on the ground.
# The orientation shifts from vertical to horizontal. X-coordinates now represent length,
# Y-coordinates represent height/thickness relative to the ground.
# The entire figure is also shifted downwards on the screen.
LYING_POSE_REL = [
    (-120, 150 - 5), # Head (left of Mid_Torso, slightly above the 'ground' Y)
    (-90, 150 - 5),  # Neck
    (-60, 150 - 20), # R_Shoulder (further left along body, spread out for width)
    (-60, 150 + 20), # L_Shoulder
    (-30, 150 - 40), # R_Elbow (arms extended outwards)
    (-30, 150 + 40), # L_Elbow
    (0, 150 - 50),   # R_Wrist
    (0, 150 + 50),   # L_Wrist
    (0, 150),        # MID_TORSO (center of body when lying, lowest point vertically relative to original anchor)
    (30, 150 - 10),  # R_Hip (right of Mid_Torso, legs slightly spread)
    (30, 150 + 10),  # L_Hip
    (60, 150 - 10),  # R_Knee
    (60, 150 + 10),  # L_Knee
    (90, 150 - 10),  # R_Ankle
    (90, 150 + 10)   # L_Ankle
]

# --- Animation Phases ---
# Each phase is defined by: (start_pose, end_pose, duration_in_seconds)
ANIMATION_PHASES = [
    (STANDING_POSE_REL, SQUATTING_POSE_REL, 1.5), # Phase 0: Standing to Squatting (1.5 seconds)
    (SQUATTING_POSE_REL, LYING_POSE_REL, 2.5),   # Phase 1: Squatting to Lying (2.5 seconds)
    (LYING_POSE_REL, LYING_POSE_REL, 2.0)        # Phase 2: Hold Lying pose (2.0 seconds)
]

# Calculate the total duration of one complete animation cycle.
TOTAL_ANIMATION_DURATION = sum([p[2] for p in ANIMATION_PHASES])

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Lying Down")
clock = pygame.time.Clock()

# --- Animation State Variables ---
animation_time = 0.0  # Current time into the total animation cycle
# Initialize current_points with the standing pose to start.
# Create a mutable list by slicing to avoid modifying the constant pose directly.
current_points = list(STANDING_POSE_REL) 

# --- Main Game Loop ---
running = True
while running:
    # Calculate time passed since the last frame.
    # dt is in seconds (pygame.time.Clock.tick returns milliseconds).
    dt = clock.tick(FPS) / 1000.0 

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation time, looping back to 0 when it exceeds total duration.
    animation_time = (animation_time + dt) % TOTAL_ANIMATION_DURATION

    # Determine the current animation phase and progress within that phase.
    current_phase_start_time = 0.0
    for i, (start_pose, end_pose, duration) in enumerate(ANIMATION_PHASES):
        if animation_time < current_phase_start_time + duration:
            # This is the active phase.
            
            # Calculate 't', the linear progress from 0.0 to 1.0 within the current phase.
            t = (animation_time - current_phase_start_time) / duration
            
            # Apply easing function for smooth acceleration/deceleration.
            eased_t = ease_in_out_quad(t)
            
            # Interpolate the position of each of the 15 points.
            for j in range(len(start_pose)):
                x1, y1 = start_pose[j]
                x2, y2 = end_pose[j]
                
                # Linear interpolation between start and end coordinates, using eased_t.
                interp_x = x1 + (x2 - x1) * eased_t
                interp_y = y1 + (y2 - y1) * eased_t
                current_points[j] = (interp_x, interp_y)
            break # Exit loop once the correct phase is found and interpolated.
        
        # If not in this phase, move to the next phase's starting time.
        current_phase_start_time += duration
    
    # --- Drawing ---
    screen.fill(BLACK) # Fill the background with black.

    # Draw each point.
    for x_rel, y_rel in current_points:
        # Convert relative coordinates to absolute screen coordinates by adding the global offset.
        # This offset corresponds to the initial standing MID_TORSO point's screen position.
        screen_x = int(x_rel + SCREEN_OFFSET_X)
        screen_y = int(y_rel + SCREEN_OFFSET_Y)
        
        pygame.draw.circle(screen, WHITE, (screen_x, screen_y), POINT_RADIUS)

    pygame.display.flip() # Update the full display Surface to the screen.

pygame.quit() # Uninitialize pygame modules.
