
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Sadman Waving")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point radius
POINT_RADIUS = 6 

# --- Skeleton Proportions (relative to a base figure height) ---
# This defines the overall size of the human figure on the screen.
FIGURE_HEIGHT = 500 # pixels for the approximate height of the figure

# Segment lengths, proportional to FIGURE_HEIGHT
# These lengths define the standard proportions of a human body.
NECK_LEN = FIGURE_HEIGHT * 0.07          # Head (1) to Neck (2)
SPINE_UPPER_LEN = FIGURE_HEIGHT * 0.23   # Neck (2) to Mid-Torso (9) - Upper body
SHOULDER_HALF_WIDTH = FIGURE_HEIGHT * 0.11 # Half width of shoulders from central spine
UPPER_ARM_LEN = FIGURE_HEIGHT * 0.18     # Shoulder (3/4) to Elbow (5/6)
LOWER_ARM_LEN = FIGURE_HEIGHT * 0.16     # Elbow (5/6) to Wrist (7/8)
HIP_HALF_WIDTH = FIGURE_HEIGHT * 0.10    # Half width of hips from central torso
UPPER_LEG_LEN = FIGURE_HEIGHT * 0.25     # Hip (10/11) to Knee (12/13)
LOWER_LEG_LEN = FIGURE_HEIGHT * 0.22     # Knee (12/13) to Ankle (14/15)

# --- Initial Pose & Animation Parameters ---
# Point 9 (Mid-Torso/Pelvis) serves as the anchor point for the figure.
# It's centered horizontally and positioned vertically to place the figure appropriately.
TORSO_BASE_X = SCREEN_WIDTH // 2
TORSO_BASE_Y = SCREEN_HEIGHT * 0.4 # Y-position of point 9 (mid-torso/pelvis)

# Angular convention: All angles are measured clockwise from the positive Y-axis (straight down).
# For a segment from (x1, y1) to (x2, y2) with length L and angle A:
# x2 = x1 + L * sin(A)
# y2 = y1 + L * cos(A)

# Parameters for "sadman with heavy weight" posture
# Torso: subtle vertical sway to suggest effort/weight
TORSO_SWAY_AMPLITUDE_Y = 3 # pixels
TORSO_SWAY_FREQ = 0.5     # Hz (slow, subtle sway)

# Spine/Head: hunched/slumped forward
SPINE_FORWARD_LEAN = math.radians(10) # Overall forward lean of the torso/spine
HEAD_TILT_FORWARD = math.radians(15)  # Additional head tilt relative to neck

# Shoulders: slightly slumped downward
SHOULDER_SLUMP_Y_OFFSET = 5 # pixels downward relative to the neck point's horizontal line

# Arms: initial hanging position
ARM_HANG_ANGLE = math.radians(15) # Angle of upper arm outwards from body's vertical line (from shoulder)
ELBOW_INITIAL_BEND = math.radians(25) # Initial bend at elbow (angle between upper and lower arm segments)

# Waving specifics (Right Arm: points 3, 5, 7)
WAVE_FREQUENCY = 1.0 # Cycles per second, a slower, labored wave
# Shoulder movement: from a relaxed hanging position to raised forward/up
WAVE_SHOULDER_START_ANGLE = math.radians(20)  # Initial angle (clockwise from down, slightly outward/forward)
WAVE_SHOULDER_END_ANGLE = math.radians(-70)   # Final angle (counter-clockwise from down, raised forward/up)
WAVE_ELBOW_BEND_AMPLITUDE = math.radians(40) # How much elbow dynamically bends during wave
WAVE_WRIST_FLICK_AMPLITUDE = math.radians(15) # Subtle wrist movement during wave

# Legs: "heavy weight" implies wider stance, slightly bent knees
HIP_OUTWARD_ANGLE = math.radians(10) # Angle of upper leg outwards from body's vertical line (from hip)
KNEE_INITIAL_BEND = math.radians(15) # Initial bend at knee (angle between upper and lower leg segments)

def calculate_joint_positions(time_elapsed):
    """
    Calculates the 2D coordinates for all 15 biological motion points
    at a given time, based on defined posture and animation.
    """
    points = {}

    # 9. Mid-Torso / Pelvis (anchor point for the entire figure)
    # Adds a subtle vertical sway to convey "heavy weight" or breathing.
    torso_offset_y = TORSO_SWAY_AMPLITUDE_Y * math.sin(time_elapsed * TORSO_SWAY_FREQ * 2 * math.pi)
    torso_center = (TORSO_BASE_X, TORSO_BASE_Y + torso_offset_y)
    points[9] = torso_center

    # Calculate points by chaining from their parent segments.
    # Angles are clockwise from the positive Y-axis (down).

    # 2. Neck / Upper Spine (from point 9 - Mid-Torso)
    # The segment from torso (9) to neck (2) goes upwards with a forward lean.
    neck_angle_from_vertical = math.pi + SPINE_FORWARD_LEAN # PI is straight up, + for forward lean (visual effect in 2D)
    neck_x = torso_center[0] + SPINE_UPPER_LEN * math.sin(neck_angle_from_vertical)
    neck_y = torso_center[1] + SPINE_UPPER_LEN * math.cos(neck_angle_from_vertical)
    points[2] = (neck_x, neck_y)

    # 1. Head (from point 2 - Neck)
    # Head continues the forward tilt from the neck.
    head_angle_from_vertical = neck_angle_from_vertical + HEAD_TILT_FORWARD
    head_x = neck_x + NECK_LEN * math.sin(head_angle_from_vertical)
    head_y = neck_y + NECK_LEN * math.cos(head_angle_from_vertical)
    points[1] = (head_x, head_y)

    # 3. Right Shoulder (from point 2 - Neck) & 4. Left Shoulder (from point 2 - Neck)
    # Shoulders extend horizontally from the neck point, with a slight downward slump.
    points[3] = (neck_x + SHOULDER_HALF_WIDTH, neck_y + SHOULDER_SLUMP_Y_OFFSET)
    points[4] = (neck_x - SHOULDER_HALF_WIDTH, neck_y + SHOULDER_SLUMP_Y_OFFSET)

    # --- Arms ---
    # Right Arm: Waving Motion (points 3, 5, 7)
    # `wave_progress` smoothly goes from 0 to 1 and back to 0 over one wave cycle.
    wave_progress = (0.5 - 0.5 * math.cos(time_elapsed * WAVE_FREQUENCY * 2 * math.pi)) 
    
    # Shoulder angle for waving (global angle relative to vertical-down)
    # Interpolate between start and end angles for a smooth swing.
    shoulder_current_angle_right = WAVE_SHOULDER_START_ANGLE + \
                                   (WAVE_SHOULDER_END_ANGLE - WAVE_SHOULDER_START_ANGLE) * wave_progress
    
    # Elbow bend (relative to upper arm segment)
    # Elbow bends more as the arm is raised for the wave.
    elbow_current_bend_right = ELBOW_INITIAL_BEND + WAVE_ELBOW_BEND_AMPLITUDE * wave_progress
    
    # Wrist flick (relative to lower arm segment)
    # A faster oscillation for a subtle "flick" effect.
    wrist_current_flick_right = WAVE_WRIST_FLICK_AMPLITUDE * math.sin(time_elapsed * WAVE_FREQUENCY * 2 * math.pi * 3)
    
    # 5. Right Elbow (from point 3 - Right Shoulder)
    elbow_right_x = points[3][0] + UPPER_ARM_LEN * math.sin(shoulder_current_angle_right)
    elbow_right_y = points[3][1] + UPPER_ARM_LEN * math.cos(shoulder_current_angle_right)
    points[5] = (elbow_right_x, elbow_right_y)
    
    # 7. Right Wrist (from point 5 - Right Elbow)
    # The angle of the lower arm is the sum of parent angles.
    wrist_right_x = points[5][0] + LOWER_ARM_LEN * math.sin(shoulder_current_angle_right + elbow_current_bend_right + wrist_current_flick_right)
    wrist_right_y = points[5][1] + LOWER_ARM_LEN * math.cos(shoulder_current_angle_right + elbow_current_bend_right + wrist_current_flick_right)
    points[7] = (wrist_right_x, wrist_right_y)

    # Left Arm: Static (points 4, 6, 8) - hanging naturally
    # 6. Left Elbow (from point 4 - Left Shoulder)
    # The X calculation is mirrored using -sin(ARM_HANG_ANGLE) for the left side.
    elbow_left_x = points[4][0] - UPPER_ARM_LEN * math.sin(ARM_HANG_ANGLE) 
    elbow_left_y = points[4][1] + UPPER_ARM_LEN * math.cos(ARM_HANG_ANGLE)
    points[6] = (elbow_left_x, elbow_left_y)
    
    # 8. Left Wrist (from point 6 - Left Elbow)
    wrist_left_x = points[6][0] - LOWER_ARM_LEN * math.sin(ARM_HANG_ANGLE + ELBOW_INITIAL_BEND)
    wrist_left_y = points[6][1] + LOWER_ARM_LEN * math.cos(ARM_HANG_ANGLE + ELBOW_INITIAL_BEND)
    points[8] = (wrist_left_x, wrist_left_y)

    # --- Legs ---
    # 10. Right Hip (from point 9 - Mid-Torso) & 11. Left Hip (from point 9)
    # Hips are spread out horizontally from the torso's center.
    points[10] = (torso_center[0] + HIP_HALF_WIDTH, torso_center[1])
    points[11] = (torso_center[0] - HIP_HALF_WIDTH, torso_center[1])

    # Right Leg (points 10, 12, 14)
    # Initial angle for upper leg relative to vertical (0=down), for outward stance.
    upper_leg_angle_right = HIP_OUTWARD_ANGLE 
    
    # Knee bend (relative to upper leg segment)
    knee_bend_right = KNEE_INITIAL_BEND
    
    # 12. Right Knee (from point 10 - Right Hip)
    knee_right_x = points[10][0] + UPPER_LEG_LEN * math.sin(upper_leg_angle_right)
    knee_right_y = points[10][1] + UPPER_LEG_LEN * math.cos(upper_leg_angle_right)
    points[12] = (knee_right_x, knee_right_y)
    
    # 14. Right Ankle (from point 12 - Right Knee)
    # The angle of the lower leg is the sum of parent angles.
    ankle_right_x = points[12][0] + LOWER_LEG_LEN * math.sin(upper_leg_angle_right + knee_bend_right)
    ankle_right_y = points[12][1] + LOWER_LEG_LEN * math.cos(upper_leg_angle_right + knee_bend_right)
    points[14] = (ankle_right_x, ankle_right_y)

    # Left Leg (points 11, 13, 15)
    # Mirroring angles for the left leg for symmetrical stance.
    upper_leg_angle_left = -HIP_OUTWARD_ANGLE # Spreads outward to the left (negative angle)
    knee_bend_left = KNEE_INITIAL_BEND
    
    # 13. Left Knee (from point 11 - Left Hip)
    knee_left_x = points[11][0] + UPPER_LEG_LEN * math.sin(upper_leg_angle_left)
    knee_left_y = points[11][1] + UPPER_LEG_LEN * math.cos(upper_leg_angle_left)
    points[13] = (knee_left_x, knee_left_y)
    
    # 15. Left Ankle (from point 13 - Left Knee)
    ankle_left_x = points[13][0] + LOWER_LEG_LEN * math.sin(upper_leg_angle_left + knee_bend_left)
    ankle_left_y = points[13][1] + LOWER_LEG_LEN * math.cos(upper_leg_angle_left + knee_bend_left)
    points[15] = (ankle_left_x, ankle_left_y)

    return points

# Main game loop
running = True
clock = pygame.time.Clock()
# Get initial time for animation timing
start_time = pygame.time.get_ticks() / 1000.0 # Convert milliseconds to seconds

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate time elapsed since the start of the animation
    current_time = pygame.time.get_ticks() / 1000.0
    time_elapsed = current_time - start_time

    # Update point positions based on the elapsed time
    joint_positions = calculate_joint_positions(time_elapsed)

    # Drawing
    screen.fill(BLACK) # Clear the screen with black background

    # Draw the 15 white point-lights
    # The keys in joint_positions dictionary are the point numbers (1 to 15).
    for i in range(1, 16): 
        if i in joint_positions:
            # Draw a white circle for each point. Coordinates are converted to integers.
            pygame.draw.circle(screen, WHITE, (int(joint_positions[i][0]), int(joint_positions[i][1])), POINT_RADIUS)

    # Update the display to show the newly drawn points
    pygame.display.flip()

    # Control the frame rate to ensure smooth animation
    clock.tick(60) # Limits the frame rate to 60 frames per second

# Quit Pygame
pygame.quit()
