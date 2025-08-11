
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800  # Taller to better fit a standing/walking person
FPS = 60
POINT_RADIUS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Human Model Parameters (relative lengths and proportions) ---
# These are rough estimates for a "standard" human figure and will affect visual plausibility.
BODY_HEIGHT_SCALE = 250  # Overall scale for the human figure (e.g., total height approx 2.5 * 250 = 625px)
HIP_WIDTH = 0.2 * BODY_HEIGHT_SCALE
SHOULDER_WIDTH = 0.25 * BODY_HEIGHT_SCALE

# Segment lengths
HEAD_NECK_LEN = 0.1 * BODY_HEIGHT_SCALE
NECK_MIDTORSO_LEN = 0.15 * BODY_HEIGHT_SCALE
MIDTORSO_HIP_LEN = 0.15 * BODY_HEIGHT_SCALE

UPPER_ARM_LEN = 0.18 * BODY_HEIGHT_SCALE
FOREARM_LEN = 0.18 * BODY_HEIGHT_SCALE

THIGH_LEN = 0.22 * BODY_HEIGHT_SCALE
CALF_LEN = 0.22 * BODY_HEIGHT_SCALE

# --- Animation Parameters ---
WALK_SPEED = 0.08  # Radians per frame, adjusts speed of walk cycle
BODY_BOB_AMPLITUDE = 0.01 * BODY_HEIGHT_SCALE  # Vertical bobbing
BODY_SWAY_AMPLITUDE = 0.005 * BODY_HEIGHT_SCALE  # Horizontal sway (side to side)

# Hip/Thigh swing
HIP_SWING_ANGLE_AMPLITUDE = math.radians(25)  # Max angle forward/backward for thigh
KNEE_BEND_AMPLITUDE = math.radians(45)  # Max additional knee bend during swing
KNEE_BEND_OFFSET = math.radians(10)  # Base knee bend (always slightly bent, even when 'straight')

# Arm swing
SHOULDER_SWING_ANGLE_AMPLITUDE = math.radians(35)
ELBOW_BEND_AMPLITUDE = math.radians(30)
ELBOW_BEND_OFFSET = math.radians(10)  # Base elbow bend

# Initial base positions (center of the screen for the mid-torso)
BASE_X = SCREEN_WIDTH // 2
BASE_Y = SCREEN_HEIGHT // 2 + 100  # Adjust to center vertically on screen

# --- Point Indices (for clarity) ---
# These 15 points are chosen to represent major joints and body landmarks
# for a biological motion display, consistent with typical research stimuli.
HEAD = 0
NECK = 1
MID_TORSO = 2
LEFT_SHOULDER = 3
RIGHT_SHOULDER = 4
LEFT_ELBOW = 5
RIGHT_ELBOW = 6
LEFT_WRIST = 7
RIGHT_WRIST = 8
LEFT_HIP = 9
RIGHT_HIP = 10
LEFT_KNEE = 11
RIGHT_KNEE = 12
LEFT_ANKLE = 13
RIGHT_ANKLE = 14

def calculate_walking_pose(frame_time):
    """
    Calculates the (x, y) coordinates for all 15 points at a given frame_time.
    Uses forward kinematics with sinusoidal joint movements to simulate walking.
    """
    points = [[0, 0] for _ in range(15)]

    # Normalized time for the walking cycle (0 to 2*PI for one full cycle)
    # The cycle starts with left leg forward, right leg back
    walk_cycle_time = frame_time * WALK_SPEED

    # --- Torso / Core Body Motion ---
    # Vertical bobbing: Body is highest when legs are in mid-stance (double support)
    # and lowest during single support or when legs are furthest apart.
    # The frequency is twice the walk cycle frequency for two up/down motions per cycle.
    body_y_offset = BASE_Y + BODY_BOB_AMPLITUDE * math.sin(walk_cycle_time * 2)

    # Horizontal sway: slight side-to-side movement, synchronized with leg swing
    body_x_sway = BODY_SWAY_AMPLITUDE * math.sin(walk_cycle_time)

    # Mid-Torso is the central reference point for the figure.
    points[MID_TORSO] = [BASE_X + body_x_sway, body_y_offset]

    # --- Upper Body (Head, Neck, Shoulders) relative to Mid-Torso ---
    mid_torso_x, mid_torso_y = points[MID_TORSO]

    # Neck point is above Mid-Torso
    points[NECK] = [mid_torso_x, mid_torso_y - NECK_MIDTORSO_LEN]

    # Head point is above Neck
    points[HEAD] = [points[NECK][0], points[NECK][1] - HEAD_NECK_LEN]

    # Shoulders are positioned horizontally from the Neck point
    points[LEFT_SHOULDER] = [mid_torso_x - SHOULDER_WIDTH / 2, points[NECK][1]]
    points[RIGHT_SHOULDER] = [mid_torso_x + SHOULDER_WIDTH / 2, points[NECK][1]]

    # --- Lower Body (Hips) relative to Mid-Torso ---
    # Hips are positioned below Mid-Torso and spread by HIP_WIDTH
    points[LEFT_HIP] = [mid_torso_x - HIP_WIDTH / 2, mid_torso_y + MIDTORSO_HIP_LEN]
    points[RIGHT_HIP] = [mid_torso_x + HIP_WIDTH / 2, mid_torso_y + MIDTORSO_HIP_LEN]

    # --- Phasing for Limbs ---
    # Left leg leads, Right leg trails (180 degrees out of phase).
    # Arms swing contra-laterally (opposite to same-side leg, with same phase as opposite leg).
    left_leg_phase = walk_cycle_time
    right_leg_phase = walk_cycle_time + math.pi
    left_arm_phase = walk_cycle_time + math.pi  # Left arm swings with right leg
    right_arm_phase = walk_cycle_time  # Right arm swings with left leg

    # Angle convention: 0 radians is along the positive X-axis (right).
    # Increasing angles are counter-clockwise.
    # Vertical downward is math.pi / 2.

    # --- Left Leg calculations ---
    lh_x, lh_y = points[LEFT_HIP]
    # Thigh angle relative to vertical downward.
    # `math.sin(phase)` positive for forward swing, negative for backward swing.
    # Subtracting from `math.pi / 2` means:
    #   - For forward swing (positive sin), angle decreases from `pi/2` (rotates CCW from vertical down, moving right).
    #   - For backward swing (negative sin), angle increases from `pi/2` (rotates CW from vertical down, moving left).
    left_thigh_angle = math.pi / 2 - HIP_SWING_ANGLE_AMPLITUDE * math.sin(left_leg_phase)

    points[LEFT_KNEE][0] = lh_x + THIGH_LEN * math.cos(left_thigh_angle)
    points[LEFT_KNEE][1] = lh_y + THIGH_LEN * math.sin(left_thigh_angle)

    # Knee bend: The knee is straighter when the leg is forward (phase 0)
    # and bends significantly when the leg swings backward (phase pi).
    # `(1 - math.cos(phase - math.pi)) / 2` creates a smooth 0-1 range, peaking at phase `pi`.
    knee_bend_left = KNEE_BEND_OFFSET + KNEE_BEND_AMPLITUDE * (1 - math.cos(left_leg_phase - math.pi)) / 2
    # Calf angle is relative to the thigh's angle.
    left_calf_angle = left_thigh_angle + knee_bend_left

    points[LEFT_ANKLE][0] = points[LEFT_KNEE][0] + CALF_LEN * math.cos(left_calf_angle)
    points[LEFT_ANKLE][1] = points[LEFT_KNEE][1] + CALF_LEN * math.sin(left_calf_angle)

    # --- Right Leg calculations (same logic, different phase) ---
    rh_x, rh_y = points[RIGHT_HIP]
    right_thigh_angle = math.pi / 2 - HIP_SWING_ANGLE_AMPLITUDE * math.sin(right_leg_phase)

    points[RIGHT_KNEE][0] = rh_x + THIGH_LEN * math.cos(right_thigh_angle)
    points[RIGHT_KNEE][1] = rh_y + THIGH_LEN * math.sin(right_thigh_angle)

    knee_bend_right = KNEE_BEND_OFFSET + KNEE_BEND_AMPLITUDE * (1 - math.cos(right_leg_phase - math.pi)) / 2
    right_calf_angle = right_thigh_angle + knee_bend_right

    points[RIGHT_ANKLE][0] = points[RIGHT_KNEE][0] + CALF_LEN * math.cos(right_calf_angle)
    points[RIGHT_ANKLE][1] = points[RIGHT_KNEE][1] + CALF_LEN * math.sin(right_calf_angle)


    # --- Left Arm calculations ---
    ls_x, ls_y = points[LEFT_SHOULDER]
    # Upper arm angle relative to vertical downward from shoulder.
    left_upper_arm_angle = math.pi / 2 - SHOULDER_SWING_ANGLE_AMPLITUDE * math.sin(left_arm_phase)

    points[LEFT_ELBOW][0] = ls_x + UPPER_ARM_LEN * math.cos(left_upper_arm_angle)
    points[LEFT_ELBOW][1] = ls_y + UPPER_ARM_LEN * math.sin(left_upper_arm_angle)

    # Elbow bend: The elbow bends more when the arm swings backward.
    elbow_bend_left = ELBOW_BEND_OFFSET + ELBOW_BEND_AMPLITUDE * (1 - math.cos(left_arm_phase - math.pi)) / 2
    # Forearm angle is relative to the upper arm's angle.
    left_forearm_angle = left_upper_arm_angle + elbow_bend_left

    points[LEFT_WRIST][0] = points[LEFT_ELBOW][0] + FOREARM_LEN * math.cos(left_forearm_angle)
    points[LEFT_WRIST][1] = points[LEFT_ELBOW][1] + FOREARM_LEN * math.sin(left_forearm_angle)

    # --- Right Arm calculations (same logic, different phase) ---
    rs_x, rs_y = points[RIGHT_SHOULDER]
    right_upper_arm_angle = math.pi / 2 - SHOULDER_SWING_ANGLE_AMPLITUDE * math.sin(right_arm_phase)

    points[RIGHT_ELBOW][0] = rs_x + UPPER_ARM_LEN * math.cos(right_upper_arm_angle)
    points[RIGHT_ELBOW][1] = rs_y + UPPER_ARM_LEN * math.sin(right_upper_arm_angle)

    elbow_bend_right = ELBOW_BEND_OFFSET + ELBOW_BEND_AMPLITUDE * (1 - math.cos(right_arm_phase - math.pi)) / 2
    right_forearm_angle = right_upper_arm_angle + elbow_bend_right

    points[RIGHT_WRIST][0] = points[RIGHT_ELBOW][0] + FOREARM_LEN * math.cos(right_forearm_angle)
    points[RIGHT_WRIST][1] = points[RIGHT_ELBOW][1] + FOREARM_LEN * math.sin(right_forearm_angle)

    return points

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Walking Man")
clock = pygame.time.Clock()

# --- Main Animation Loop ---
running = True
frame_count = 0

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Allow Esc key to quit
                running = False

    # Clear screen to black
    screen.fill(BLACK)

    # Calculate the current pose for all 15 points
    current_points = calculate_walking_pose(frame_count)

    # Draw each point as a white circle
    for x, y in current_points:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

    # Update the display to show the new frame
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
    frame_count += 1

# Quit Pygame
pygame.quit()
