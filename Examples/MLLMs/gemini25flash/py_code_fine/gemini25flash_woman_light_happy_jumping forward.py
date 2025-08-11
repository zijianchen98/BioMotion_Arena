
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 4  # Radius of each point-light
FPS = 60          # Frames per second for smooth animation

# Point indices (for clarity and mapping to human joints)
# These are just symbolic names for the indices 0-14, matching common point-light models.
HEAD = 0
SHOULDER_L, SHOULDER_R = 1, 2
ELBOW_L, ELBOW_R = 3, 4
WRIST_L, WRIST_R = 5, 6
UPPER_TORSO = 7
PELVIS = 8
HIP_L, HIP_R = 9, 10
KNEE_L, KNEE_R = 11, 12
ANKLE_L, ANKLE_R = 13, 14

# Humanoid base dimensions (arbitrary units, will be scaled)
# These are relative coordinates for a neutral standing pose.
# Y increases UPWARDS (so head has largest Y, ankles smallest relative Y=0)
JOINT_DEFAULTS = {
    ANKLE_L: (-10, 0),    # Left Ankle
    ANKLE_R: (10, 0),     # Right Ankle
    KNEE_L: (-10, 25),    # Left Knee
    KNEE_R: (10, 25),     # Right Knee
    HIP_L: (-10, 50),     # Left Hip
    HIP_R: (10, 50),      # Right Hip
    PELVIS: (0, 60),      # Central Pelvis/Center of Mass reference
    WRIST_L: (-20, 60),   # Left Wrist (arms slightly bent)
    WRIST_R: (20, 60),    # Right Wrist
    ELBOW_L: (-20, 80),   # Left Elbow
    ELBOW_R: (20, 80),    # Right Elbow
    SHOULDER_L: (-15, 90), # Left Shoulder
    SHOULDER_R: (15, 90), # Right Shoulder
    UPPER_TORSO: (0, 95),  # Upper Torso/Spine
    HEAD: (0, 115),       # Head
}

# Scale factor for converting internal units to screen pixels
SCALE = 1.8 
# Initial X position of the figure's starting point on the screen
BASE_X_OFFSET = SCREEN_WIDTH * 0.2
# Y coordinate on screen that represents the "ground" level (where ankle Y=0 would be drawn)
BASE_Y_OFFSET = SCREEN_HEIGHT * 0.8 

# --- Easing Function ---
def ease_in_out_quad(t):
    """
    Smoothstep function for interpolation.
    Provides smooth transitions by accelerating and decelerating the interpolation.
    """
    return t * t * (3 - 2 * t)

def lerp(a, b, t):
    """Linear interpolation between two values a and b by factor t."""
    return a + (b - a) * t

def get_interp_point(p1, p2, t):
    """Interpolate a single point (x, y) between two points p1 and p2 by factor t."""
    return (lerp(p1[0], p2[0], t), lerp(p1[1], p2[1], t))

# --- Keyframe Poses ---
def apply_pose_modifier(base_pose, modifiers):
    """
    Applies modifiers (offsets) to a base pose to create a new pose.
    Modifiers are added to the base pose's joint coordinates.
    Returns a new pose dictionary.
    """
    new_pose = dict(base_pose)
    for joint_idx, (x_mod, y_mod) in modifiers.items():
        base_x, base_y = base_pose[joint_idx]
        new_pose[joint_idx] = (base_x + x_mod, base_y + y_mod)
    return new_pose

# Generate base standing pose by scaling JOINT_DEFAULTS to screen size
base_standing_pose_scaled = {}
for idx, (x, y) in JOINT_DEFAULTS.items():
    base_standing_pose_scaled[idx] = (x * SCALE, y * SCALE)

# Define distinct keyframe poses using modifiers applied to the scaled base pose.
# Y-modifiers: positive = move joint up, negative = move joint down (relative to its default scaled position)
# X-modifiers: positive = move joint right, negative = move joint left
# These describe the internal posture changes during the jump.

# Pose 0: Standing (Initial state of a jump cycle)
pose_standing = base_standing_pose_scaled

# Pose 1: Crouch (Preparation phase for jump)
crouch_modifiers = {
    PELVIS: (0, -40 * SCALE), # Pelvis lowers significantly
    KNEE_L: (10 * SCALE, -20 * SCALE), KNEE_R: (-10 * SCALE, -20 * SCALE), # Knees bend, move forward
    ANKLE_L: (5 * SCALE, -10 * SCALE), ANKLE_R: (-5 * SCALE, -10 * SCALE), # Ankles come up (heels lift)
    HIP_L: (0, -20 * SCALE), HIP_R: (0, -20 * SCALE), # Hips lower and slightly forward
    UPPER_TORSO: (0, -10 * SCALE), HEAD: (0, -10 * SCALE), # Torso/Head lean slightly forward
    SHOULDER_L: (10 * SCALE, -10 * SCALE), SHOULDER_R: (-10 * SCALE, -10 * SCALE), # Arms swing back
    ELBOW_L: (15 * SCALE, -20 * SCALE), ELBOW_R: (-15 * SCALE, -20 * SCALE),
    WRIST_L: (15 * SCALE, -30 * SCALE), WRIST_R: (-15 * SCALE, -30 * SCALE),
}
pose_crouch = apply_pose_modifier(base_standing_pose_scaled, crouch_modifiers)

# Pose 2: Launch (Extension/Push-off phase)
launch_modifiers = {
    PELVIS: (0, 20 * SCALE), # Pelvis pushes upwards
    KNEE_L: (0 * SCALE, 0 * SCALE), KNEE_R: (0 * SCALE, 0 * SCALE), # Knees extending to straight
    ANKLE_L: (0 * SCALE, 0 * SCALE), ANKLE_R: (0 * SCALE, 0 * SCALE), # Ankles extend fully
    UPPER_TORSO: (0, 0 * SCALE), HEAD: (0, 0 * SCALE), # Torso/Head upright
    SHOULDER_L: (-10 * SCALE, 10 * SCALE), SHOULDER_R: (10 * SCALE, 10 * SCALE), # Arms swing vigorously forward/up
    ELBOW_L: (-15 * SCALE, 10 * SCALE), ELBOW_R: (15 * SCALE, 10 * SCALE),
    WRIST_L: (-15 * SCALE, 0 * SCALE), WRIST_R: (15 * SCALE, 0 * SCALE),
}
pose_launch = apply_pose_modifier(base_standing_pose_scaled, launch_modifiers)

# Pose 3: Mid-Air (Apex of the jump arc) - incorporates "happy" and "light weight" elements
midair_modifiers = {
    PELVIS: (0, 30 * SCALE), # Pelvis elevated (relative to standing internal posture)
    KNEE_L: (10 * SCALE, -25 * SCALE), KNEE_R: (-10 * SCALE, -25 * SCALE), # Knees bent, legs tucked up (light weight)
    ANKLE_L: (5 * SCALE, -40 * SCALE), ANKLE_R: (-5 * SCALE, -40 * SCALE), # Ankles tucked
    HIP_L: (0, -10 * SCALE), HIP_R: (0, -10 * SCALE), # Hips pulled up
    UPPER_TORSO: (0, 0 * SCALE), HEAD: (0, 0 * SCALE), # Torso relatively upright
    SHOULDER_L: (-20 * SCALE, 20 * SCALE), SHOULDER_R: (20 * SCALE, 20 * SCALE), # Arms slightly out/up ("happy" pose)
    ELBOW_L: (-25 * SCALE, 10 * SCALE), ELBOW_R: (25 * SCALE, 10 * SCALE),
    WRIST_L: (-25 * SCALE, 0 * SCALE), WRIST_R: (25 * SCALE, 0 * SCALE),
}
pose_midair = apply_pose_modifier(base_standing_pose_scaled, midair_modifiers)

# Pose 4: Landing Approach (Preparing to land)
landing_approach_modifiers = {
    PELVIS: (0, 0 * SCALE), # Pelvis returning towards standing level internally
    KNEE_L: (0 * SCALE, 0 * SCALE), KNEE_R: (0 * SCALE, 0 * SCALE), # Knees extending to reach ground
    ANKLE_L: (0 * SCALE, 0 * SCALE), ANKLE_R: (0 * SCALE, 0 * SCALE), # Ankles extending
    UPPER_TORSO: (0, 0 * SCALE), HEAD: (0, 0 * SCALE),
    SHOULDER_L: (-10 * SCALE, 0 * SCALE), SHOULDER_R: (10 * SCALE, 0 * SCALE), # Arms coming down for balance
    ELBOW_L: (-10 * SCALE, 0 * SCALE), ELBOW_R: (10 * SCALE, 0 * SCALE),
    WRIST_L: (-10 * SCALE, 0 * SCALE), WRIST_R: (10 * SCALE, 0 * SCALE),
}
pose_landing_approach = apply_pose_modifier(base_standing_pose_scaled, landing_approach_modifiers)

# Pose 5: Landing (Impact Absorption)
landing_impact_modifiers = {
    PELVIS: (0, -30 * SCALE), # Pelvis lowers to absorb impact
    KNEE_L: (10 * SCALE, -20 * SCALE), KNEE_R: (-10 * SCALE, -20 * SCALE), # Knees bent sharply
    ANKLE_L: (5 * SCALE, -10 * SCALE), ANKLE_R: (-5 * SCALE, -10 * SCALE), # Ankles slightly lifted (heels)
    HIP_L: (0, -10 * SCALE), HIP_R: (0, -10 * SCALE), # Hips lowered
    UPPER_TORSO: (0, -10 * SCALE), HEAD: (0, -10 * SCALE), # Torso/Head lean forward for balance
    SHOULDER_L: (5 * SCALE, -5 * SCALE), SHOULDER_R: (-5 * SCALE, -5 * SCALE), # Arms forward for balance
    ELBOW_L: (5 * SCALE, -10 * SCALE), ELBOW_R: (-5 * SCALE, -10 * SCALE),
    WRIST_L: (5 * SCALE, -15 * SCALE), WRIST_R: (-5 * SCALE, -15 * SCALE),
}
pose_landing_impact = apply_pose_modifier(base_standing_pose_scaled, landing_impact_modifiers)

# Pose 6: Recovery (Returning to standing after landing)
pose_recovery = base_standing_pose_scaled 

# List of keyframes and their relative durations within one complete jump cycle.
# The relative durations should sum to 1.0 for a complete cycle.
TOTAL_JUMP_DURATION_SECONDS = 2.5 # Duration of one full jump cycle in seconds
TOTAL_JUMP_DURATION_FRAMES = int(TOTAL_JUMP_DURATION_SECONDS * FPS)

PHASE_DURATIONS_RELATIVE = [
    (pose_standing, 0.1),         # Brief pause at standing
    (pose_crouch, 0.2),           # Crouch
    (pose_launch, 0.2),           # Launch
    (pose_midair, 0.2),           # Mid-air arc
    (pose_landing_approach, 0.1), # Landing approach
    (pose_landing_impact, 0.1),   # Landing impact
    (pose_recovery, 0.1),         # Recovery
]

# Convert relative durations to actual frame counts for each phase.
PHASE_DURATIONS_FRAMES = []
for pose, rel_duration in PHASE_DURATIONS_RELATIVE:
    PHASE_DURATIONS_FRAMES.append((pose, int(rel_duration * TOTAL_JUMP_DURATION_FRAMES)))

# Adjust total frames to match exactly TOTAL_JUMP_DURATION_FRAMES due to integer conversion.
current_total_frames = sum([f for _, f in PHASE_DURATIONS_FRAMES])
if current_total_frames != TOTAL_JUMP_DURATION_FRAMES:
    diff = TOTAL_JUMP_DURATION_FRAMES - current_total_frames
    # Add/subtract the difference from the last phase to ensure exact frame count.
    PHASE_DURATIONS_FRAMES[-1] = (PHASE_DURATIONS_FRAMES[-1][0], PHASE_DURATIONS_FRAMES[-1][1] + diff)


# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Jumping Forward")
clock = pygame.time.Clock()

# Animation state variables
current_frame = 0                # Current frame count since animation start
x_total_displacement = 0.0       # Accumulates total horizontal movement of the figure
jump_height_max = 120            # Maximum vertical height of the jump arc in pixels
distance_per_jump_cycle = SCREEN_WIDTH * 0.2 # How much the figure moves forward per jump cycle

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Allow 'ESC' to quit
                running = False

    # Fill the background with black
    screen.fill(BLACK)

    # Calculate overall animation progress within the current jump cycle (0.0 to 1.0)
    cycle_frame = current_frame % TOTAL_JUMP_DURATION_FRAMES
    t_in_cycle = cycle_frame / TOTAL_JUMP_DURATION_FRAMES

    # --- 1. Global Horizontal Movement ---
    # Continuously move the figure forward.
    # The total displacement is the distance covered in completed cycles plus progress in current cycle.
    x_total_displacement = (t_in_cycle * distance_per_jump_cycle) + \
                           (current_frame // TOTAL_JUMP_DURATION_FRAMES * distance_per_jump_cycle)

    # --- 2. Global Vertical Jump Arc ---
    # This defines the overall height of the figure's center from the ground line.
    
    # Define the time points within the t_in_cycle (0.0 to 1.0) for the jump arc.
    # Arc starts after crouch phase.
    arc_start_t = PHASE_DURATIONS_RELATIVE[0][1] + PHASE_DURATIONS_RELATIVE[1][1] 
    # Arc ends before landing impact and recovery phases.
    arc_end_t = 1.0 - (PHASE_DURATIONS_RELATIVE[-1][1] + PHASE_DURATIONS_RELATIVE[-2][1]) 

    y_arc_height = 0.0
    if t_in_cycle >= arc_start_t and t_in_cycle <= arc_end_t:
        # Normalize t for the arc phase (0 to 1 within the jump arc duration)
        t_arc_norm = (t_in_cycle - arc_start_t) / (arc_end_t - arc_start_t)
        # Apply a parabolic curve for the jump arc (peaks at t_arc_norm = 0.5)
        y_arc_height = 4 * jump_height_max * t_arc_norm * (1 - t_arc_norm)
    # else: y_arc_height remains 0.0 (figure is on the ground)

    # --- 3. Internal Joint Interpolation ---
    # Determine the current keyframe poses and interpolation factor within the current phase.
    current_phase_start_frame = 0
    current_pose = None
    next_pose = None
    t_phase = 0.0 # Interpolation factor within current specific phase (0.0 to 1.0)

    for i in range(len(PHASE_DURATIONS_FRAMES)):
        pose, num_frames = PHASE_DURATIONS_FRAMES[i]
        if cycle_frame < current_phase_start_frame + num_frames:
            current_pose = pose
            # Determine the next pose for interpolation. If last phase, loop to first.
            if i + 1 < len(PHASE_DURATIONS_FRAMES):
                next_pose = PHASE_DURATIONS_FRAMES[i+1][0]
            else:
                next_pose = PHASE_DURATIONS_FRAMES[0][0] # Loop back to start (standing pose)
            
            # Calculate interpolation factor within the current phase.
            frame_in_phase = cycle_frame - current_phase_start_frame
            t_phase = frame_in_phase / num_frames if num_frames > 0 else 0.0
            t_phase = ease_in_out_quad(t_phase) # Apply easing for smoother transitions
            break
        current_phase_start_frame += num_frames
    
    # Fallback in case of calculation errors or very short phases, default to first pose.
    if current_pose is None:
        current_pose = PHASE_DURATIONS_FRAMES[0][0]
        next_pose = PHASE_DURATIONS_FRAMES[1][0]
        t_phase = 0.0

    # Interpolate all 15 points between the current and next keyframe poses.
    current_joint_interpolated_relative = {}
    for joint_idx in range(15): # Iterate through all 15 defined points (0-14)
        p1 = current_pose.get(joint_idx, (0,0)) # Get relative position from current pose
        p2 = next_pose.get(joint_idx, (0,0))   # Get relative position from next pose
        current_joint_interpolated_relative[joint_idx] = get_interp_point(p1, p2, t_phase)

    # --- 4. Draw Points ---
    # Draw each of the 15 point-lights on the screen.
    for joint_idx in range(15):
        # Get the interpolated relative (x, y) coordinates for this joint's posture.
        rel_x, rel_y = current_joint_interpolated_relative[joint_idx]
        
        # Calculate absolute screen X coordinate:
        # BASE_X_OFFSET: Initial starting X position.
        # x_total_displacement: Accumulates forward motion of the entire figure.
        # rel_x: Joint's horizontal position relative to the figure's central reference.
        draw_x = int(BASE_X_OFFSET + x_total_displacement + rel_x)
        
        # Calculate absolute screen Y coordinate:
        # BASE_Y_OFFSET: The screen Y coordinate of the "ground" line.
        # y_arc_height: The figure's overall vertical displacement due to jumping (positive = higher, so subtract from screen Y).
        # rel_y: Joint's vertical position relative to the figure's base (positive = higher on body, so subtract from screen Y).
        draw_y = int(BASE_Y_OFFSET - y_arc_height - rel_y) 
        
        pygame.draw.circle(screen, WHITE, (draw_x, draw_y), POINT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Advance to the next frame and cap frame rate
    current_frame += 1
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
