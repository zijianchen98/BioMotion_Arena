
import pygame
import math
import random

# Screen dimensions
WIDTH, HEIGHT = 800, 600
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point radius
POINT_RADIUS = 5

# Scale factor for the overall skeleton size relative to screen height
SKELETON_DRAW_SCALE = HEIGHT * 0.7

# Proportional lengths of body parts relative to the SKELETON_DRAW_SCALE
# These are rough proportions for a human figure.
PROPORTIONS = {
    "torso_len": 0.25,  # Pelvis to Neck/Shoulder level for a lying figure
    "head_len": 0.05,   # Approximate length for head segment (neck to top of head)
    "upper_arm_len": 0.15,
    "fore_arm_len": 0.15,
    "upper_leg_len": 0.2,
    "lower_leg_len": 0.2,
    "foot_len": 0.05,
    "hip_width": 0.08,  # Horizontal/vertical offset for hips from central pelvis
    "shoulder_width": 0.12 # Horizontal/vertical offset for shoulders from central spine line
}

# Define the 15 points and their hierarchical relationships (parent_idx: child_idx)
# These indices correspond to typical biological motion points (e.g., Johansson displays)
# 0: Head
# 1: Right Shoulder
# 2: Left Shoulder
# 3: Right Elbow
# 4: Left Elbow
# 5: Right Wrist
# 6: Left Wrist
# 7: Pelvis Center (root of the skeleton hierarchy)
# 8: Right Hip
# 9: Left Hip
# 10: Right Knee
# 11: Left Knee
# 12: Right Ankle
# 13: Left Ankle
# 14: Right Foot (assuming one foot point for simplicity/matching 15 total)

# Initial relative vectors (normalized direction vectors) and their parent index.
# This represents the initial "lying down" pose.
# Each vector describes the direction from parent to child in the "model space".
# Pelvis (7) is the root, positioned at (CENTER_X, CENTER_Y) on the screen.
# X points right, Y points down (Pygame convention).
# The person is lying on their back, head to the left, feet to the right.
initial_relative_vectors_and_parents = {
    # Head & Torso segment directions relative to Pelvis (7)
    0: (pygame.math.Vector2(-1, 0), 7),                  # Head: Directly left from pelvis
    1: (pygame.math.Vector2(-1, -0.2).normalize(), 7),   # R Shoulder: Slightly up-left from pelvis
    2: (pygame.math.Vector2(-1, 0.2).normalize(), 7),    # L Shoulder: Slightly down-left from pelvis

    # Arm segments (relative to their parent joint's orientation)
    3: (pygame.math.Vector2(0, 1), 1),                   # R Elbow: Straight down from R Shoulder (arm hanging along side)
    4: (pygame.math.Vector2(0, -1), 2),                  # L Elbow: Straight up from L Shoulder (arm hanging along side)
    5: (pygame.math.Vector2(0, 1), 3),                   # R Wrist: Straight down from R Elbow
    6: (pygame.math.Vector2(0, -1), 4),                  # L Wrist: Straight up from L Elbow

    # Leg segments (relative to their parent joint's orientation)
    8: (pygame.math.Vector2(1, -0.2).normalize(), 7),    # R Hip: Slightly up-right from pelvis
    9: (pygame.math.Vector2(1, 0.2).normalize(), 7),     # L Hip: Slightly down-right from pelvis
    10: (pygame.math.Vector2(1, 0), 8),                  # R Knee: Straight right from R Hip (straight leg)
    11: (pygame.math.Vector2(1, 0), 9),                  # L Knee: Straight right from L Hip
    12: (pygame.math.Vector2(1, 0), 10),                 # R Ankle: Straight right from R Knee
    13: (pygame.math.Vector2(1, 0), 11),                 # L Ankle: Straight right from L Knee
    14: (pygame.math.Vector2(1, -0.2).normalize(), 12),  # R Foot: Slightly up-right from R Ankle (heel slightly up)
}

# Define the actual segment lengths by scaling the proportional lengths
# (parent_idx, child_idx): scaled_length
lengths_dict = {
    (7, 0): (PROPORTIONS["torso_len"] + PROPORTIONS["head_len"]) * SKELETON_DRAW_SCALE,
    (7, 1): (PROPORTIONS["torso_len"] + PROPORTIONS["shoulder_width"]) * SKELETON_DRAW_SCALE, # Approximate length to shoulder
    (7, 2): (PROPORTIONS["torso_len"] + PROPORTIONS["shoulder_width"]) * SKELETON_DRAW_SCALE,
    (1, 3): PROPORTIONS["upper_arm_len"] * SKELETON_DRAW_SCALE,
    (2, 4): PROPORTIONS["upper_arm_len"] * SKELETON_DRAW_SCALE,
    (3, 5): PROPORTIONS["fore_arm_len"] * SKELETON_DRAW_SCALE,
    (4, 6): PROPORTIONS["fore_arm_len"] * SKELETON_DRAW_SCALE,
    (7, 8): PROPORTIONS["hip_width"] * SKELETON_DRAW_SCALE,
    (7, 9): PROPORTIONS["hip_width"] * SKELETON_DRAW_SCALE,
    (8, 10): PROPORTIONS["upper_leg_len"] * SKELETON_DRAW_SCALE,
    (9, 11): PROPORTIONS["upper_leg_len"] * SKELETON_DRAW_SCALE,
    (10, 12): PROPORTIONS["lower_leg_len"] * SKELETON_DRAW_SCALE,
    (11, 13): PROPORTIONS["lower_leg_len"] * SKELETON_DRAW_SCALE,
    (12, 14): PROPORTIONS["foot_len"] * SKELETON_DRAW_SCALE
}

# Global structures to store parent relationships and segment lengths
point_parents = {child_idx: parent_idx for child_idx, (_, parent_idx) in initial_relative_vectors_and_parents.items()}
segment_lengths = lengths_dict

# Initialize current_point_vectors (normalized direction from parent to child)
# These vectors will be perturbed during animation.
current_point_vectors = {child_idx: vec.copy() for child_idx, (vec, _) in initial_relative_vectors_and_parents.items()}

# Absolute position for each point (will be updated each frame)
point_coords = {idx: pygame.math.Vector2(0, 0) for idx in range(15)}

# Order of points for updating, ensuring parents are processed before children
# This ensures the kinematic chain is correctly calculated.
UPDATE_ORDER = [
    0,      # Head (child of Pelvis)
    1, 2,   # Shoulders (children of Pelvis)
    3, 4,   # Elbows (children of Shoulders)
    5, 6,   # Wrists (children of Elbows)
    8, 9,   # Hips (children of Pelvis)
    10, 11, # Knees (children of Hips)
    12, 13, # Ankles (children of Knees)
    14,     # Foot (child of R Ankle)
]

def update_skeleton_pose(current_pelvis_pos, current_point_vectors, segment_lengths, point_parents, point_coords):
    """
    Calculates the absolute position of all skeleton points based on the pelvis position
    and the relative vectors/segment lengths.
    """
    point_coords[7] = current_pelvis_pos  # Pelvis (7) is the root, positioned directly

    for child_idx in UPDATE_ORDER:
        parent_idx = point_parents[child_idx]
        norm_vec = current_point_vectors[child_idx]  # Current (potentially perturbed) normalized direction vector
        length = segment_lengths[(parent_idx, child_idx)]
        # Child's absolute position = Parent's absolute position + (normalized vector * length)
        point_coords[child_idx] = point_coords[parent_idx] + norm_vec * length

# --- Animation Parameters for Subtle Motion ---
# For "sad" and "heavy weight", motion should be very subtle, slow, and possibly downward/slumped.

# Breathing animation (vertical pelvis shift)
BREATH_PERIOD = 3.5  # seconds for one breath cycle
BREATH_AMPLITUDE = SKELETON_DRAW_SCALE * 0.005  # Vertical displacement for breathing (very small)

# Arm movement (subtle angle changes)
ARM_MOVE_PERIOD = 6.0  # seconds for arm cycle
ARM_MOVE_AMPLITUDE = math.pi / 40  # radians for arm swing (very small angle)

# Leg movement (subtle angle changes)
LEG_MOVE_PERIOD = 8.0  # seconds for leg cycle
LEG_MOVE_AMPLITUDE = math.pi / 30  # radians for leg swing (very small angle)

# Head tilt/slump (subtle angle changes)
HEAD_MOVE_PERIOD = 5.0  # seconds for head tilt cycle
HEAD_MOVE_AMPLITUDE = math.pi / 70  # radians for head tilt (extremely small angle)

# Random phase offsets for each animation to make them desynchronized and natural
breathing_phase = random.uniform(0, 2 * math.pi)
arm_phase_R = random.uniform(0, 2 * math.pi)
arm_phase_L = random.uniform(0, 2 * math.pi)
leg_phase_R = random.uniform(0, 2 * math.pi)
leg_phase_L = random.uniform(0, 2 * math.pi)
head_phase = random.uniform(0, 2 * math.pi)

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Woman Lying Down")
clock = pygame.time.Clock()
FPS = 60

# --- Game Loop ---
running = True
frame_time = 0.0  # Time in seconds since start of animation

while running:
    # Calculate delta time for frame-rate independent animation
    dt = clock.tick(FPS) / 1000.0  # Delta time in seconds
    frame_time += dt

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update Animation State ---

    # 1. Pelvis/Breathing motion: subtle vertical shift
    pelvis_offset_y = math.sin(frame_time * (2 * math.pi / BREATH_PERIOD) + breathing_phase) * BREATH_AMPLITUDE
    current_pelvis_pos = pygame.math.Vector2(CENTER_X, CENTER_Y + pelvis_offset_y)

    # 2. Limb movements (angle perturbations)
    # Create a temporary copy of the initial relative vectors to apply current frame's perturbations.
    # This ensures that each frame starts from the base pose and applies small, oscillating changes.
    temp_current_point_vectors = {child_idx: vec.copy() for child_idx, (vec, _) in initial_relative_vectors_and_parents.items()}

    # Right Arm: perturb the angle of Shoulder(1) -> Elbow(3) segment
    arm_angle_perturbation_R = math.sin(frame_time * (2 * math.pi / ARM_MOVE_PERIOD) + arm_phase_R) * ARM_MOVE_AMPLITUDE
    original_vec_3_1 = initial_relative_vectors_and_parents[3][0] # Get initial normalized vector
    rotated_vec_3_1 = original_vec_3_1.rotate_rad(arm_angle_perturbation_R) # Rotate it
    temp_current_point_vectors[3] = rotated_vec_3_1 # Update for this frame

    # Left Arm: Shoulder(2) -> Elbow(4)
    arm_angle_perturbation_L = math.sin(frame_time * (2 * math.pi / ARM_MOVE_PERIOD) + arm_phase_L) * ARM_MOVE_AMPLITUDE
    original_vec_4_2 = initial_relative_vectors_and_parents[4][0]
    rotated_vec_4_2 = original_vec_4_2.rotate_rad(arm_angle_perturbation_L)
    temp_current_point_vectors[4] = rotated_vec_4_2

    # Right Leg: Hip(8) -> Knee(10)
    leg_angle_perturbation_R = math.sin(frame_time * (2 * math.pi / LEG_MOVE_PERIOD) + leg_phase_R) * LEG_MOVE_AMPLITUDE
    original_vec_10_8 = initial_relative_vectors_and_parents[10][0]
    rotated_vec_10_8 = original_vec_10_8.rotate_rad(leg_angle_perturbation_R)
    temp_current_point_vectors[10] = rotated_vec_10_8

    # Left Leg: Hip(9) -> Knee(11)
    leg_angle_perturbation_L = math.sin(frame_time * (2 * math.pi / LEG_MOVE_PERIOD) + leg_phase_L) * LEG_MOVE_AMPLITUDE
    original_vec_11_9 = initial_relative_vectors_and_parents[11][0]
    rotated_vec_11_9 = original_vec_11_9.rotate_rad(leg_angle_perturbation_L)
    temp_current_point_vectors[11] = rotated_vec_11_9

    # Head tilt/slump: Head(0) relative to Pelvis(7)
    head_angle_perturbation = math.sin(frame_time * (2 * math.pi / HEAD_MOVE_PERIOD) + head_phase) * HEAD_MOVE_AMPLITUDE
    original_vec_0_7 = initial_relative_vectors_and_parents[0][0]
    rotated_vec_0_7 = original_vec_0_7.rotate_rad(head_angle_perturbation)
    temp_current_point_vectors[0] = rotated_vec_0_7

    # Update all point positions based on the perturbed skeleton state for this frame
    update_skeleton_pose(current_pelvis_pos, temp_current_point_vectors, segment_lengths, point_parents, point_coords)

    # --- Drawing ---
    screen.fill(BLACK)  # Solid black background

    # Draw each of the 15 white point-lights
    for i in range(15):
        pos = point_coords[i]
        pygame.draw.circle(screen, WHITE, (int(pos.x), int(pos.y)), POINT_RADIUS)

    pygame.display.flip()

pygame.quit()
