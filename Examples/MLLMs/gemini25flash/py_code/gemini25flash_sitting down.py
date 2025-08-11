
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 4

# Animation parameters
FPS = 60
ANIMATION_DURATION = 2.5 # seconds for one way (standing to sitting)
TOTAL_FRAMES = int(FPS * ANIMATION_DURATION) * 2 # standing -> sitting -> standing cycle
current_frame = 0

# Body segment lengths (in pixels, scaled for typical human proportions)
# These values are chosen to create a visually plausible human figure.
TORSO_LEN = 60
NECK_LEN_OFFSET = 20 # Distance from neck base to head center
SHOULDER_WIDTH = 25 # Horizontal distance from neck/spine center to shoulder joint
UPPER_ARM_LEN = 45
FOREARM_LEN = 40
PELVIS_WIDTH = 25 # Horizontal distance from pelvis center to hip joint
THIGH_LEN = 70
SHIN_LEN = 65

# Center of the screen for drawing the person (horizontal center)
CENTER_X = SCREEN_WIDTH // 2
# Ground level for the animation (where feet rest when standing/sitting)
GROUND_Y = SCREEN_HEIGHT - 100 

# Joint names for easier reference (exactly 15 points)
JOINT_NAMES = [
    "head", "neck",
    "r_shoulder", "l_shoulder",
    "r_elbow", "l_elbow",
    "r_wrist", "l_wrist",
    "pelvis",
    "r_hip", "l_hip",
    "r_knee", "l_knee",
    "r_ankle", "l_ankle"
]

def get_eased_value(start, end, progress):
    """
    Applies a sine easing function (ease-in-out) to a linear progress.
    progress: float from 0.0 to 1.0
    """
    return start + (end - start) * (0.5 - 0.5 * math.cos(math.pi * progress))

def calculate_pose(progress_factor):
    """
    Calculates joint positions for a given animation progress (0.0 to 1.0).
    Returns a dictionary of {joint_name: (x, y)} coordinates.

    Angles are defined such that a positive value for _flexion_rad means
    the segment moves "forward" (to the right in a side view).
    Rotation for (0, -L) (upward vector): `rotate(-math.degrees(angle))` for clockwise (forward/right lean).
    Rotation for (0, L) (downward vector): `rotate(-math.degrees(angle))` for clockwise (forward/right swing/bend).
    """
    
    # Scale progress for a smooth sit-stand-sit cycle:
    # 0.0 to 0.5: standing to sitting (progress_factor * 2)
    # 0.5 to 1.0: sitting to standing (1.0 - (progress_factor - 0.5) * 2)
    if progress_factor <= 0.5:
        eased_progress = get_eased_value(0, 1, progress_factor * 2)
    else:
        eased_progress = get_eased_value(0, 1, (1 - progress_factor) * 2)

    # Pelvis Y position (relative to ground)
    # Standing: pelvis is THIGH_LEN + SHIN_LEN above ground (feet on ground, legs straight)
    STANDING_PELVIS_Y_OFFSET = THIGH_LEN + SHIN_LEN
    # Sitting: pelvis is roughly SHIN_LEN * 0.75 above ground (approximating chair height)
    SITTING_PELVIS_Y_OFFSET = SHIN_LEN * 0.75

    pelvis_y_relative_to_ground = get_eased_value(STANDING_PELVIS_Y_OFFSET, SITTING_PELVIS_Y_OFFSET, eased_progress)
    pelvis_x = CENTER_X
    pelvis_y = GROUND_Y - pelvis_y_relative_to_ground

    # Joint angles (radians)
    # 0 for straight/upright. Positive values for flexion/forward lean/swing (clockwise in side view)
    STANDING_TORSO_ANGLE = 0
    STANDING_HIP_FLEXION = 0
    STANDING_KNEE_FLEXION = 0
    STANDING_SHOULDER_FLEXION = 0
    STANDING_ELBOW_FLEXION = 0

    SITTING_TORSO_ANGLE = math.radians(10) # Slight forward lean (10 degrees)
    SITTING_HIP_FLEXION = math.radians(95) # Thigh roughly horizontal (95 degrees flexion)
    SITTING_KNEE_FLEXION = math.radians(95) # Shin roughly vertical (95 degrees flexion)
    SITTING_SHOULDER_FLEXION = math.radians(10) # Slight arm swing forward
    SITTING_ELBOW_FLEXION = math.radians(15) # Slight elbow bend

    torso_angle_rad = get_eased_value(STANDING_TORSO_ANGLE, SITTING_TORSO_ANGLE, eased_progress)
    hip_flexion_rad = get_eased_value(STANDING_HIP_FLEXION, SITTING_HIP_FLEXION, eased_progress)
    knee_flexion_rad = get_eased_value(STANDING_KNEE_FLEXION, SITTING_KNEE_FLEXION, eased_progress)
    shoulder_flexion_rad = get_eased_value(STANDING_SHOULDER_FLEXION, SITTING_SHOULDER_FLEXION, eased_progress)
    elbow_flexion_rad = get_eased_value(STANDING_ELBOW_FLEXION, SITTING_ELBOW_FLEXION, eased_progress)

    # Calculate joint positions
    joints = {}
    joints["pelvis"] = pygame.math.Vector2(pelvis_x, pelvis_y)

    # Head and Torso segments (pointing upwards from parent joint initially: (0, -L))
    # For a forward lean (top moves right), the rotation is clockwise (negative degrees for Pygame's CCW rotate)
    joints["neck"] = joints["pelvis"] + pygame.math.Vector2(0, -TORSO_LEN).rotate(-math.degrees(torso_angle_rad))
    joints["head"] = joints["neck"] + pygame.math.Vector2(0, -NECK_LEN_OFFSET).rotate(-math.degrees(torso_angle_rad))

    # Shoulders and Hips are horizontal offsets from neck/pelvis, also affected by torso lean
    joints["r_shoulder"] = joints["neck"] + pygame.math.Vector2(SHOULDER_WIDTH, 0).rotate(-math.degrees(torso_angle_rad))
    joints["l_shoulder"] = joints["neck"] + pygame.math.Vector2(-SHOULDER_WIDTH, 0).rotate(-math.degrees(torso_angle_rad))
    joints["r_hip"] = joints["pelvis"] + pygame.math.Vector2(PELVIS_WIDTH, 0).rotate(-math.degrees(torso_angle_rad))
    joints["l_hip"] = joints["pelvis"] + pygame.math.Vector2(-PELVIS_WIDTH, 0).rotate(-math.degrees(torso_angle_rad))

    # Arms and Legs segments (pointing downwards from parent joint initially: (0, L))
    # For forward swing/bend (segment moves right), the rotation is clockwise (negative degrees for Pygame's CCW rotate)

    # Right Arm
    # The world angle is the sum of torso lean and arm's relative swing/flexion
    r_upper_arm_world_angle = torso_angle_rad + shoulder_flexion_rad
    joints["r_elbow"] = joints["r_shoulder"] + pygame.math.Vector2(0, UPPER_ARM_LEN).rotate(-math.degrees(r_upper_arm_world_angle))
    r_forearm_world_angle = r_upper_arm_world_angle + elbow_flexion_rad
    joints["r_wrist"] = joints["r_elbow"] + pygame.math.Vector2(0, FOREARM_LEN).rotate(-math.degrees(r_forearm_world_angle))

    # Left Arm (symmetric movement in a side view)
    l_upper_arm_world_angle = torso_angle_rad + shoulder_flexion_rad
    joints["l_elbow"] = joints["l_shoulder"] + pygame.math.Vector2(0, UPPER_ARM_LEN).rotate(-math.degrees(l_upper_arm_world_angle))
    l_forearm_world_angle = l_upper_arm_world_angle + elbow_flexion_rad
    joints["l_wrist"] = joints["l_elbow"] + pygame.math.Vector2(0, FOREARM_LEN).rotate(-math.degrees(l_forearm_world_angle))

    # Legs
    r_thigh_world_angle = torso_angle_rad + hip_flexion_rad
    joints["r_knee"] = joints["r_hip"] + pygame.math.Vector2(0, THIGH_LEN).rotate(-math.degrees(r_thigh_world_angle))
    r_shin_world_angle = r_thigh_world_angle + knee_flexion_rad
    joints["r_ankle"] = joints["r_knee"] + pygame.math.Vector2(0, SHIN_LEN).rotate(-math.degrees(r_shin_world_angle))

    l_thigh_world_angle = torso_angle_rad + hip_flexion_rad
    joints["l_knee"] = joints["l_hip"] + pygame.math.Vector2(0, THIGH_LEN).rotate(-math.degrees(l_thigh_world_angle))
    l_shin_world_angle = l_thigh_world_angle + knee_flexion_rad
    joints["l_ankle"] = joints["l_knee"] + pygame.math.Vector2(0, SHIN_LEN).rotate(-math.degrees(l_shin_world_angle))

    # Convert all vector positions to integer tuples for drawing
    return {name: (int(pos.x), int(pos.y)) for name, pos in joints.items()}

# Game loop
running = True
clock = pygame.time.Clock()
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate animation progress for the full sit-stand cycle (0.0 to 1.0)
    progress_val = (current_frame % TOTAL_FRAMES) / TOTAL_FRAMES

    # Calculate current pose based on animation progress
    pose = calculate_pose(progress_val)

    # Drawing
    screen.fill(BLACK) # Solid black background

    # Draw the 15 white point-lights
    for joint_name in JOINT_NAMES:
        pos = pose.get(joint_name)
        if pos:
            pygame.draw.circle(screen, WHITE, pos, POINT_RADIUS)

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

    # Increment frame counter
    current_frame += 1

pygame.quit()
