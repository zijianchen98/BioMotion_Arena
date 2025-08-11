
import pygame
import math
import numpy as np

# --- Pygame Setup ---
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DOT_RADIUS = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion - Sadman Turning")
clock = pygame.time.Clock()

# --- 3D Point Definitions ---
# Define 15 key points for the human body in a normalized, standing T-pose.
# Y is up, X is right, Z is forward (towards the viewer from the origin).
# The origin (0,0,0) is set at the approximate pelvis center for easier global transformations.

# Body segment proportions (relative units, adjust for desired shape)
PELVIS_Y = 0.0  # Base for lower body
HIP_WIDTH = 0.16
LEG_LENGTH_UPPER = 0.4
LEG_LENGTH_LOWER = 0.4
FOOT_LENGTH = 0.1

TORSO_HEIGHT = 0.3
NECK_HEIGHT = 0.1
HEAD_HEIGHT = 0.15
SHOULDER_WIDTH = 0.3
ARM_LENGTH_UPPER = 0.25
ARM_LENGTH_LOWER = 0.25

# Initial 3D joint positions (x, y, z) relative to pelvis (0,0,0)
# These form the base "T-pose" or neutral standing pose
initial_points_data = {
    # Upper Body
    "head": np.array([0.0, PELVIS_Y + TORSO_HEIGHT + NECK_HEIGHT + HEAD_HEIGHT, 0.0]),
    "neck": np.array([0.0, PELVIS_Y + TORSO_HEIGHT + NECK_HEIGHT, 0.0]),
    "shoulder_l": np.array([-SHOULDER_WIDTH / 2, PELVIS_Y + TORSO_HEIGHT, 0.0]),
    "shoulder_r": np.array([SHOULDER_WIDTH / 2, PELVIS_Y + TORSO_HEIGHT, 0.0]),
    "elbow_l": np.array([-SHOULDER_WIDTH / 2 - ARM_LENGTH_UPPER, PELVIS_Y + TORSO_HEIGHT - ARM_LENGTH_UPPER, 0.0]),
    "elbow_r": np.array([SHOULDER_WIDTH / 2 + ARM_LENGTH_UPPER, PELVIS_Y + TORSO_HEIGHT - ARM_LENGTH_UPPER, 0.0]),
    "wrist_l": np.array([-SHOULDER_WIDTH / 2 - ARM_LENGTH_UPPER - ARM_LENGTH_LOWER, PELVIS_Y + TORSO_HEIGHT - ARM_LENGTH_UPPER - ARM_LENGTH_LOWER, 0.0]),
    "wrist_r": np.array([SHOULDER_WIDTH / 2 + ARM_LENGTH_UPPER + ARM_LENGTH_LOWER, PELVIS_Y + TORSO_HEIGHT - ARM_LENGTH_UPPER - ARM_LENGTH_LOWER, 0.0]),
    # Torso/Pelvis
    "pelvis": np.array([0.0, PELVIS_Y, 0.0]),
    "hip_l": np.array([-HIP_WIDTH / 2, PELVIS_Y, 0.0]),
    "hip_r": np.array([HIP_WIDTH / 2, PELVIS_Y, 0.0]),
    # Lower Body
    "knee_l": np.array([-HIP_WIDTH / 2, PELVIS_Y - LEG_LENGTH_UPPER, 0.0]),
    "knee_r": np.array([HIP_WIDTH / 2, PELVIS_Y - LEG_LENGTH_UPPER, 0.0]),
    "ankle_l": np.array([-HIP_WIDTH / 2, PELVIS_Y - LEG_LENGTH_UPPER - LEG_LENGTH_LOWER, 0.0]),
    "ankle_r": np.array([HIP_WIDTH / 2, PELVIS_Y - LEG_LENGTH_UPPER - LEG_LENGTH_LOWER, 0.0]),
}

# Verify exactly 15 points
assert len(initial_points_data) == 15, f"Expected 15 points, got {len(initial_points_data)}"

# --- Animation Parameters ---
TOTAL_TURN_ANGLE = 2 * math.pi  # A full 360-degree turn
TURN_DURATION_SECONDS = 8  # Slower turn for "heavy weight" suggestion

# "Sadman" posture: slight forward lean
INITIAL_LEAN_ANGLE_X = math.radians(10) # Rotate around X-axis for forward lean

# "Heavy weight" suggestion: subtle vertical bobbing
BOB_AMPLITUDE = 0.02  # Relative units for vertical sway
BOB_FREQUENCY = 1.0   # Cycles per second

# Subtle limb movements for biomechanical plausibility during turn
ARM_SWING_Z_AMPLITUDE = 0.03 # Small forward/backward arm swing (Z-axis)
ARM_SWING_X_AMPLITUDE = 0.01 # Small lateral arm swing (X-axis)
KNEE_FLEX_AMPLITUDE_Y = 0.01 # Small vertical knee bend (Y-axis)

# --- Coordinate Transformations ---

def rotation_matrix(axis, angle):
    """Generates a 3x3 rotation matrix for a given axis and angle (radians)."""
    axis = np.asarray(axis)
    axis = axis / np.linalg.norm(axis)
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    ux, uy, uz = axis

    # Optimization for standard axes
    if np.allclose(axis, [1, 0, 0]): # X-axis
        return np.array([
            [1, 0, 0],
            [0, cos_a, -sin_a],
            [0, sin_a, cos_a]
        ])
    elif np.allclose(axis, [0, 1, 0]): # Y-axis
        return np.array([
            [cos_a, 0, sin_a],
            [0, 1, 0],
            [-sin_a, 0, cos_a]
        ])
    elif np.allclose(axis, [0, 0, 1]): # Z-axis
        return np.array([
            [cos_a, -sin_a, 0],
            [sin_a, cos_a, 0],
            [0, 0, 1]
        ])
    else: # General Rodrigues' rotation formula
        return np.array([
            [cos_a + ux**2*(1-cos_a), ux*uy*(1-cos_a) - uz*sin_a, ux*uz*(1-cos_a) + uy*sin_a],
            [uy*ux*(1-cos_a) + uz*sin_a, cos_a + uy**2*(1-cos_a), uy*uz*(1-cos_a) - ux*sin_a],
            [uz*ux*(1-cos_a) - uy*sin_a, uz*uy*(1-cos_a) + ux*sin_a, cos_a + uz**2*(1-cos_a)]
        ])

def transform_point(point_name, current_time, lean_angle_x, global_rot_angle_y, bob_offset_y):
    """
    Applies global and subtle individual transformations to a point.
    """
    initial_pos = initial_points_data[point_name]
    
    # 1. Apply static 'sadman' lean (rotation around X-axis for the whole body's initial pose)
    # This assumes the pivot for the lean is the origin (pelvis).
    pos_after_lean = np.dot(rotation_matrix([1, 0, 0], lean_angle_x), initial_pos)
    
    # 2. Apply global turning (rotation around Y-axis for the whole body)
    pos_after_global_rot = np.dot(rotation_matrix([0, 1, 0], global_rot_angle_y), pos_after_lean)
    
    # 3. Apply global bobbing translation
    final_pos = pos_after_global_rot + np.array([0, bob_offset_y, 0])
    
    # 4. Apply subtle individual joint movements (simplified offsets for visual effect)
    # These offsets are added to the globally transformed position.

    # Arm swing (subtle forward/backward and lateral movement of wrists/elbows)
    # Arms typically swing slightly in opposition to torso rotation, or with a slight delay/lead.
    # For a turn, a subtle follow-through or counter-balancing movement is common.
    # Using sine of global_rot_angle_y creates a smooth, cyclical swing.
    if "wrist" in point_name or "elbow" in point_name:
        if "l" in point_name: # Left arm
            # Left arm swings more into negative Z (forward) when turning right (angle decreases)
            # and positive Z (backward) when turning left (angle increases).
            # A simple -sin(angle) fits this.
            final_pos[2] -= ARM_SWING_Z_AMPLITUDE * math.sin(global_rot_angle_y)
            final_pos[0] -= ARM_SWING_X_AMPLITUDE * math.cos(global_rot_angle_y) 
        elif "r" in point_name: # Right arm
            # Opposite for the right arm.
            final_pos[2] += ARM_SWING_Z_AMPLITUDE * math.sin(global_rot_angle_y)
            final_pos[0] += ARM_SWING_X_AMPLITUDE * math.cos(global_rot_angle_y)

    # Subtle knee flexion for "heavy weight" / weight shift
    # Knees may bend slightly more when the body is shifting weight or momentarily paused during a slow turn.
    # Here, we make them bend slightly when the body is facing sideways (max X-displacement).
    if "knee" in point_name or "ankle" in point_name:
        # abs(sin(angle)) ensures the bend is always downwards, peaking at 90/270 degrees.
        flex_offset = -KNEE_FLEX_AMPLITUDE_Y * abs(math.sin(global_rot_angle_y / 2)) # Divide by 2 for a full cycle over 360 turn
        final_pos[1] += flex_offset

    return final_pos

def project_to_2d(point_3d, scale, center_x, center_y):
    """
    Projects a 3D point (already transformed) to 2D screen coordinates.
    """
    x_proj, y_proj, _ = point_3d # Z is not directly used for screen position in simple orthographic

    screen_x = int(center_x + x_proj * scale)
    screen_y = int(center_y - y_proj * scale) # Pygame Y-axis is inverted (larger Y is down)

    return screen_x, screen_y

# Calculate a suitable scale factor for display
# Max height of the figure (head_y - ankle_y)
max_height_unit = initial_points_data["head"][1] - initial_points_data["ankle_l"][1]
DISPLAY_HEIGHT_PIXELS = 400 # Target height of the figure on screen
SCALE_FACTOR = DISPLAY_HEIGHT_PIXELS / (max_height_unit * 1.2) # 1.2 for some padding

# Screen center for drawing
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2 + 100 # Adjust vertical center so feet are not at the bottom edge

# --- Animation Loop ---
running = True
frame_count = 0
total_frames = int(TURN_DURATION_SECONDS * FPS)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Calculate current animation time and angles
    t_normalized = (frame_count % total_frames) / total_frames # Normalized time [0, 1) for the turn cycle
    current_global_angle_rad = t_normalized * TOTAL_TURN_ANGLE

    # Calculate global bobbing offset
    current_bob_offset_y = BOB_AMPLITUDE * math.sin(t_normalized * 2 * math.pi * BOB_FREQUENCY)

    # Calculate and draw each point
    for name in initial_points_data.keys():
        # Get the dynamically transformed 3D position for the current frame
        point_3d = transform_point(name, t_normalized, INITIAL_LEAN_ANGLE_X, 
                                   current_global_angle_rad, current_bob_offset_y)
        
        # Project to 2D screen coordinates
        screen_pos = project_to_2d(point_3d, SCALE_FACTOR, CENTER_X, CENTER_Y)
        
        # Draw the point
        pygame.draw.circle(screen, WHITE, screen_pos, DOT_RADIUS)

    pygame.display.flip()
    frame_count += 1
    clock.tick(FPS)

pygame.quit()
