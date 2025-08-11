
import pygame
import math
import time

# --- Pygame Setup ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
POINT_RADIUS = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Bowing Man")
clock = pygame.time.Clock()

# --- Biomechanical Constants (Relative to each other in a conceptual Y-up space) ---
# These define the 'bone lengths' or distances between joints for the initial standing pose.
TORSO_H = 100   # From torso_center (pelvis) to neck/shoulder base
NECK_H = 20     # From neck to base of head (top of head point)
HEAD_SIZE = 20  # Additional height from neck to head point
SHOULDER_W = 40 # Half-width of shoulders
UPPER_ARM_L = 50
FOREARM_L = 45
HIP_W = 30      # Half-width of hips
THIGH_L = 80
SHIN_L = 75

# --- Animation Parameters ---
TOTAL_BOW_DURATION = 2.5  # seconds for one full bow cycle (down and up)
MAX_BOW_ANGLE_TORSO = math.radians(60)  # Max bend forward for torso
MAX_KNEE_BEND_ANGLE = math.radians(10)  # Slight knee bend
MAX_SHOULDER_SWING_ANGLE = math.radians(20) # Arms swing forward slightly
MAX_ELBOW_BEND_ANGLE = math.radians(5)    # Slight elbow bend (forearm up)
MAX_NECK_BEND_ANGLE = math.radians(15)    # Head nods down

# --- Helper Function for Rotation ---
def rotate_point(point_x, point_y, origin_x, origin_y, angle_rad):
    """
    Rotates a point (point_x, point_y) around an origin (origin_x, origin_y) by angle_rad.
    Positive angle_rad means counter-clockwise rotation.
    """
    translated_x = point_x - origin_x
    translated_y = point_y - origin_y

    rotated_x = translated_x * math.cos(angle_rad) - translated_y * math.sin(angle_rad)
    rotated_y = translated_x * math.sin(angle_rad) + translated_y * math.cos(angle_rad)

    new_x = rotated_x + origin_x
    new_y = rotated_y + origin_y
    return new_x, new_y

# --- Initial Pose Points (relative to a conceptual 'root' at torso_center (0,0) ) ---
# These are the points in their initial, upright, un-rotated state.
# In this conceptual space, the Y-axis is pointing UP.
initial_points = {
    "torso_center": (0, 0),

    # Legs (Y values are negative as they extend downwards from torso_center)
    "hip_L": (-HIP_W, 0),
    "hip_R": (HIP_W, 0),
    "knee_L": (-HIP_W, -THIGH_L),
    "knee_R": (HIP_W, -THIGH_L),
    "ankle_L": (-HIP_W, -THIGH_L - SHIN_L),
    "ankle_R": (HIP_W, -THIGH_L - SHIN_L),

    # Torso/Head (Y values are positive as they extend upwards from torso_center)
    "neck": (0, TORSO_H),
    "head": (0, TORSO_H + NECK_H + HEAD_SIZE), # Point at top of head, for simplicity

    # Arms (Y values are based on shoulders, then extend downwards)
    "shoulder_L": (-SHOULDER_W, TORSO_H),
    "shoulder_R": (SHOULDER_W, TORSO_H),
    "elbow_L": (-SHOULDER_W, TORSO_H - UPPER_ARM_L), # Arms hanging straight down
    "elbow_R": (SHOULDER_W, TORSO_H - UPPER_ARM_L),
    "wrist_L": (-SHOULDER_W, TORSO_H - UPPER_ARM_L - FOREARM_L),
    "wrist_R": (SHOULDER_W, TORSO_H - UPPER_ARM_L - FOREARM_L),
}

# Assert exactly 15 points
assert len(initial_points) == 15, f"Expected 15 points, got {len(initial_points)}"

# Global offset to center the figure on the screen
GLOBAL_OFFSET_X = SCREEN_WIDTH // 2
# Place the figure's "ground" point (mid-ankle) at 80% down the screen
GROUND_Y = SCREEN_HEIGHT * 0.8 

# Calculate the initial Y position of the torso_center in Pygame coordinates
# (Pygame Y increases downwards, conceptual Y increases upwards)
# So, initial_torso_center_screen_y = GROUND_Y - (height from torso_center to ground)
initial_torso_center_screen_y = GROUND_Y - (THIGH_L + SHIN_L)

# --- Main Animation Loop ---
running = True
start_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Calculate animation progress (0 to 1 to 0 smoothly over TOTAL_BOW_DURATION)
    elapsed_time = time.time() - start_time
    phase = (elapsed_time % TOTAL_BOW_DURATION) / TOTAL_BOW_DURATION
    animation_progress = (1 - math.cos(phase * 2 * math.pi)) / 2

    # Calculate current angles based on animation progress
    # Note: Positive angles here correspond to the maximum bend defined.
    current_torso_angle = animation_progress * MAX_BOW_ANGLE_TORSO
    current_knee_angle = animation_progress * MAX_KNEE_BEND_ANGLE
    current_shoulder_angle = animation_progress * MAX_SHOULDER_SWING_ANGLE
    current_elbow_angle = animation_progress * MAX_ELBOW_BEND_ANGLE
    current_neck_angle = animation_progress * MAX_NECK_BEND_ANGLE

    # --- Calculate current point positions ---
    current_points = {}

    # Calculate torso_center's position based on knee bend
    # When knees bend, the entire torso lowers slightly.
    # This simplified model assumes a vertical drop proportional to knee bend.
    torso_vertical_shift = animation_progress * (SHIN_L / 5) # Example: lowers by 1/5th of shin length max

    current_torso_center_x = GLOBAL_OFFSET_X
    current_torso_center_y = initial_torso_center_screen_y + torso_vertical_shift # + because Pygame Y-axis is inverted

    # Legs: Hip, Knee, Ankle
    # For a simple bow, assume the hip's X position stays aligned with torso_center.
    # The knee and ankle points will follow. The `torso_vertical_shift` handles the squat effect.
    # The X coordinates of leg points are fixed relative to torso_center_x.
    # The Y coordinates are also fixed relative to torso_center_y, but adjusted for the shift.
    for side in ['L', 'R']:
        hip_name = f"hip_{side}"
        knee_name = f"knee_{side}"
        ankle_name = f"ankle_{side}"

        current_points[hip_name] = (
            current_torso_center_x + initial_points[hip_name][0],
            current_torso_center_y - initial_points[hip_name][1] # Y inverted for Pygame
        )
        current_points[knee_name] = (
            current_torso_center_x + initial_points[knee_name][0],
            current_torso_center_y - initial_points[knee_name][1]
        )
        current_points[ankle_name] = (
            current_torso_center_x + initial_points[ankle_name][0],
            current_torso_center_y - initial_points[ankle_name][1]
        )
    
    # Store torso_center in current_points
    current_points["torso_center"] = (current_torso_center_x, current_torso_center_y)

    # Torso, Neck, Head, Arms: Hierarchical Rotations
    # All these points are defined relative to the torso_center conceptually.
    # We apply the main torso rotation first to these points.
    # The rotation pivot is `initial_points["torso_center"]` in conceptual space.
    # The screen pivot for these points is `(current_torso_center_x, current_torso_center_y)`.

    # List of points that directly belong to the main torso segment (or depend on its rotation)
    points_on_torso_segment = [
        "neck", "head", "shoulder_L", "shoulder_R",
        "elbow_L", "elbow_R", "wrist_L", "wrist_R"
    ]
    
    # Temporarily store points after torso rotation in conceptual space
    temp_torso_rotated_points_concept = {} 

    for p_name in points_on_torso_segment:
        initial_px_rel, initial_py_rel = initial_points[p_name]
        
        # Bowing forward is a clockwise rotation. Our `rotate_point` is CCW, so use -angle.
        rotated_px_rel, rotated_py_rel = rotate_point(
            initial_px_rel, initial_py_rel,
            initial_points["torso_center"][0], initial_points["torso_center"][1],
            -current_torso_angle 
        )
        temp_torso_rotated_points_concept[p_name] = (rotated_px_rel, rotated_py_rel)
        
        # Immediately convert to screen coordinates for drawing, for most of these points.
        # Head, Elbow, Wrist will be overwritten by their specific hierarchical rotations.
        current_points[p_name] = (
            current_torso_center_x + rotated_px_rel,
            current_torso_center_y - rotated_py_rel # Invert Y for Pygame
        )

    # Apply additional rotation for the Head (relative to Neck)
    neck_concept_x, neck_concept_y = temp_torso_rotated_points_concept["neck"]
    
    # Calculate head's initial relative position *from neck* (conceptual)
    head_rel_neck_init_x = initial_points["head"][0] - initial_points["neck"][0]
    head_rel_neck_init_y = initial_points["head"][1] - initial_points["neck"][1]
    
    # Rotate this head_rel_neck vector around (0,0) by neck angle (clockwise for downward nod)
    rotated_head_rel_neck_x, rotated_head_rel_neck_y = rotate_point(
        head_rel_neck_init_x, head_rel_neck_init_y,
        0, 0, # Origin (0,0) for this relative vector rotation
        -current_neck_angle
    )
    
    # Add this rotated vector back to the neck's current conceptual position
    final_head_concept_x = neck_concept_x + rotated_head_rel_neck_x
    final_head_concept_y = neck_concept_y + rotated_head_rel_neck_y
    
    # Update head's screen coordinates
    current_points["head"] = (
        current_torso_center_x + final_head_concept_x,
        current_torso_center_y - final_head_concept_y
    )

    # Apply additional rotations for Arms (Elbow and Wrist relative to Shoulder and Elbow)
    for side in ['L', 'R']:
        shoulder_name = f"shoulder_{side}"
        elbow_name = f"elbow_{side}"
        wrist_name = f"wrist_{side}"

        # Get shoulder's current position (after torso rotation) in *conceptual* relative space
        shoulder_concept_x, shoulder_concept_y = temp_torso_rotated_points_concept[shoulder_name]

        # Elbow's initial relative position *from shoulder* (conceptual)
        elbow_rel_shoulder_init_x = initial_points[elbow_name][0] - initial_points[shoulder_name][0]
        elbow_rel_shoulder_init_y = initial_points[elbow_name][1] - initial_points[shoulder_name][1]

        # Wrist's initial relative position *from elbow* (conceptual)
        wrist_rel_elbow_init_x = initial_points[wrist_name][0] - initial_points[elbow_name][0]
        wrist_rel_elbow_init_y = initial_points[wrist_name][1] - initial_points[elbow_name][1]

        # Apply additional shoulder swing to upper arm (elbow point)
        # Rotate elbow_rel_shoulder vector around (0,0) by shoulder angle (clockwise for forward swing)
        rotated_elbow_rel_shoulder_x, rotated_elbow_rel_shoulder_y = rotate_point(
            elbow_rel_shoulder_init_x, elbow_rel_shoulder_init_y,
            0, 0, # Origin (0,0) for relative vector
            -current_shoulder_angle
        )
        
        # Calculate elbow's current conceptual position
        current_elbow_concept_x = shoulder_concept_x + rotated_elbow_rel_shoulder_x
        current_elbow_concept_y = shoulder_concept_y + rotated_elbow_rel_shoulder_y

        # Apply additional elbow bend to forearm (wrist point)
        # Rotate wrist_rel_elbow vector around (0,0) by elbow angle (counter-clockwise for bending up)
        # Assuming initial pose has arms straight, bending means forearm moves towards upper arm.
        # If arm is hanging down, this is generally a positive (counter-clockwise) rotation.
        rotated_wrist_rel_elbow_x, rotated_wrist_rel_elbow_y = rotate_point(
            wrist_rel_elbow_init_x, wrist_rel_elbow_init_y,
            0, 0, # Origin (0,0) for relative vector
            current_elbow_angle 
        )
        
        # Calculate wrist's current conceptual position by adding rotated forearm vector to current elbow position
        current_wrist_concept_x = current_elbow_concept_x + rotated_wrist_rel_elbow_x
        current_wrist_concept_y = current_elbow_concept_y + rotated_wrist_rel_elbow_y

        # Update screen coordinates for elbow and wrist
        current_points[elbow_name] = (
            current_torso_center_x + current_elbow_concept_x,
            current_torso_center_y - current_elbow_concept_y
        )
        current_points[wrist_name] = (
            current_torso_center_x + current_wrist_concept_x,
            current_torso_center_y - current_wrist_concept_y
        )
        
    # Draw all calculated points on the screen
    for point_name, (x, y) in current_points.items():
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
