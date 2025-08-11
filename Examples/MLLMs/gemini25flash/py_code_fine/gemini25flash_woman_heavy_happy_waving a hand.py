
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_RADIUS = 5

# Root position (pelvis center) - adjust for screen center and figure height
ROOT_X = SCREEN_WIDTH // 2
ROOT_Y = SCREEN_HEIGHT // 2 + 100 # Position the base of the figure slightly lower

# --- Body Segment Lengths (approximate for a 'heavy' woman) ---
# These lengths define the proportions of the point-light figure.
# Wider hips and shoulders can visually suggest 'heavy weight' even with abstract points.
HEAD_NECK_LEN = 25  # Distance from head point to upper torso point
TORSO_UPPER_LEN = 60 # Distance from upper torso to lower torso
TORSO_LOWER_LEN = 60 # Distance from lower torso to hip/pelvis line
UPPER_ARM_LEN = 55
FOREARM_LEN = 55
UPPER_LEG_LEN = 75
LOWER_LEG_LEN = 75
SHOULDER_SPAN = 70 # Width between shoulders
HIP_SPAN = 80      # Width between hips (wider for 'heavy' physique)

# --- Initial Pose Definition (Relative to the 'torso_lower' point as origin (0,0)) ---
# Y increases downwards, X increases to the right.
# These relative coordinates define the standing posture.
base_coords = {
    'torso_lower': (0, 0), # Our reference point for figure's base
    'hip_L': (-HIP_SPAN / 2, 0),
    'hip_R': (HIP_SPAN / 2, 0),
    'knee_L': (-HIP_SPAN / 2, UPPER_LEG_LEN),
    'knee_R': (HIP_SPAN / 2, UPPER_LEG_LEN),
    'foot_L': (-HIP_SPAN / 2, UPPER_LEG_LEN + LOWER_LEG_LEN),
    'foot_R': (HIP_SPAN / 2, UPPER_LEG_LEN + LOWER_LEG_LEN),

    'torso_upper': (0, -TORSO_LOWER_LEN),
    'shoulder_L': (-SHOULDER_SPAN / 2, -TORSO_LOWER_LEN - TORSO_UPPER_LEN),
    'shoulder_R': (SHOULDER_SPAN / 2, -TORSO_LOWER_LEN - TORSO_UPPER_LEN),
    'head': (0, -TORSO_LOWER_LEN - TORSO_UPPER_LEN - HEAD_NECK_LEN),

    # Arms initially hanging down, relative to their shoulders
    # Note: These are initial absolute relative positions, not calculated from angles yet.
    'elbow_L': (-SHOULDER_SPAN / 2, -TORSO_LOWER_LEN - TORSO_UPPER_LEN + UPPER_ARM_LEN),
    'hand_L': (-SHOULDER_SPAN / 2, -TORSO_LOWER_LEN - TORSO_UPPER_LEN + UPPER_ARM_LEN + FOREARM_LEN),
    'elbow_R': (SHOULDER_SPAN / 2, -TORSO_LOWER_LEN - TORSO_UPPER_LEN + UPPER_ARM_LEN),
    'hand_R': (SHOULDER_SPAN / 2, -TORSO_LOWER_LEN - TORSO_UPPER_LEN + UPPER_ARM_LEN + FOREARM_LEN),
}

# The names of the 15 points, matching the example image structure.
# This list helps iterate through the points.
point_names = [
    'head', 'torso_upper', 'torso_lower',
    'shoulder_L', 'shoulder_R', 'elbow_L', 'elbow_R', 'hand_L', 'hand_R',
    'hip_L', 'hip_R', 'knee_L', 'knee_R', 'foot_L', 'foot_R'
]

# Ensure we have exactly 15 points as required
assert len(point_names) == 15, f"Error: Expected 15 points, got {len(point_names)}"

# --- Animation Logic Function ---
def get_current_pose(frame_time):
    """
    Calculates the position of all 15 points for the current animation frame.
    
    Args:
        frame_time (float): Current time in seconds, used to drive the animation.
    
    Returns:
        dict: A dictionary where keys are point names (e.g., 'head') and values are
              [x, y] coordinates representing their screen position.
    """
    current_pose = {}
    
    # 1. Initialize all points based on their static base_coords,
    #    translated by the global root position.
    for name in point_names:
        current_pose[name] = [ROOT_X + base_coords[name][0], ROOT_Y + base_coords[name][1]]

    # 2. Animate the right arm for waving.
    #    The 'shoulder_R' point serves as the pivot for the upper arm.
    shoulder_R_x, shoulder_R_y = current_pose['shoulder_R']

    # --- Shoulder Rotation Animation ---
    # Controls the lift and swing of the upper arm.
    # `wave_lift_progress`: A slow oscillation (0 to 1 and back) for arm lifting.
    # `wave_swing_progress`: A faster oscillation (-1 to 1) for the back-and-forth wave.
    wave_lift_progress = (math.sin(frame_time * 1.0) + 1) / 2.0 # Slower lift/lower
    wave_swing_progress = math.sin(frame_time * 2.5) # Faster side-to-side swing

    # Angles are in radians.
    # `math.pi / 2` represents the arm hanging straight down relative to horizontal right.
    # `max_lift_angle_from_vertical`: How much the arm lifts up from hanging.
    # `max_swing_angle_horizontal`: How much the arm swings forward/backward horizontally.
    max_lift_angle_from_vertical = math.radians(70) 
    max_swing_angle_horizontal = math.radians(30)
    
    # Calculate the current absolute angle of the upper arm relative to horizontal right.
    # It starts at `math.pi / 2` (down), then lifts up by subtracting `max_lift * progress`,
    # and also swings horizontally by adding `max_swing * progress`.
    shoulder_current_angle = (math.pi / 2) - (max_lift_angle_from_vertical * wave_lift_progress) \
                             + (max_swing_angle_horizontal * wave_swing_progress)

    # Calculate the new position of the right elbow based on shoulder rotation.
    current_pose['elbow_R'][0] = shoulder_R_x + UPPER_ARM_LEN * math.cos(shoulder_current_angle)
    current_pose['elbow_R'][1] = shoulder_R_y + UPPER_ARM_LEN * math.sin(shoulder_current_angle)

    # --- Elbow Bend Animation ---
    # Controls the bending and straightening of the forearm.
    # `elbow_bend_progress`: A faster oscillation for the bending motion.
    elbow_bend_progress = (math.sin(frame_time * 4.0) + 1) / 2.0 # Faster bend/straighten
    
    # `max_elbow_bend_angle`: Maximum angle the elbow bends from a straight arm.
    max_elbow_bend_angle = math.radians(60)
    
    # Calculate the current bend angle.
    elbow_current_bend = max_elbow_bend_angle * elbow_bend_progress
    
    # Get the current elbow_R position (pivot point for forearm).
    elbow_R_x, elbow_R_y = current_pose['elbow_R']
    
    # Calculate the absolute angle of the forearm relative to horizontal right.
    # If the upper arm is at `shoulder_current_angle`, a straight forearm would be at
    # `shoulder_current_angle + math.pi` (180 degrees relative to upper arm's direction).
    # Then add `elbow_current_bend` to simulate the actual bend.
    forearm_current_angle = shoulder_current_angle + math.pi + elbow_current_bend

    # Calculate the new position of the right hand based on elbow bend.
    current_pose['hand_R'][0] = elbow_R_x + FOREARM_LEN * math.cos(forearm_current_angle)
    current_pose['hand_R'][1] = elbow_R_y + FOREARM_LEN * math.sin(forearm_current_angle)

    # 3. Add subtle body sway for realism and to convey 'heavy weight'.
    # This applies a small sinusoidal shift to the entire body except the waving arm.
    sway_amplitude_x = 5 # Max horizontal sway in pixels
    sway_amplitude_y = 2 # Max vertical sway in pixels
    sway_speed = 0.5 # Speed of the general body sway

    sway_x = sway_amplitude_x * math.sin(frame_time * sway_speed)
    sway_y = sway_amplitude_y * math.cos(frame_time * sway_speed * 1.2) # Different speed for Y for naturalness

    for name in point_names:
        # Do not apply sway to the points of the waving arm as they are already specifically animated.
        if name not in ['shoulder_R', 'elbow_R', 'hand_R']:
            current_pose[name][0] += sway_x
            current_pose[name][1] += sway_y
            
    return current_pose

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Waving Woman")
clock = pygame.time.Clock()

# --- Main Animation Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with a black background
    screen.fill(BLACK)

    # Get current time in seconds to drive the animation
    current_time = pygame.time.get_ticks() / 1000.0

    # Calculate the positions of all points for the current frame
    current_pose = get_current_pose(current_time)

    # Draw each point as a white circle
    for name in point_names:
        x, y = int(current_pose[name][0]), int(current_pose[name][1])
        pygame.draw.circle(screen, WHITE, (x, y), POINT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# --- Quit Pygame ---
pygame.quit()
