
import pygame
import numpy as np

# --- Configuration ---
# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 60
# A longer duration for the turn enhances the feeling of sadness/low energy
NUM_FRAMES = 300  # 5-second loop at 60 FPS
POINT_RADIUS = 5

# --- 3D Model Definition ---
# A 15-point model representing a human figure.
# The posture is designed to convey sadness: slumped shoulders, head tilted down.
# The proportions are for a person of light weight.
# Coordinates are [X, Y, Z] relative to a point on the ground plane.
# +Y is up, +X is to the figure's right, +Z is forward.
# The 15 points correspond to:
# 0: Head, 1: Neck, 2: L Shoulder, 3: R Shoulder, 4: L Elbow, 5: R Elbow,
# 6: L Wrist, 7: R Wrist, 8: Pelvis, 9: L Hip, 10: R Hip,
# 11: L Knee, 12: R Knee, 13: L Ankle, 14: R Ankle
base_pose_3d = np.array([
    # X,    Y,      Z
    [0.0,   1.80,   0.08],   # 0: Head (tilted down/forward)
    [0.0,   1.65,   0.05],   # 1: Neck (forward)
    [-0.20, 1.55,   0.05],   # 2: L Shoulder (slumped)
    [0.20,  1.55,   0.05],   # 3: R Shoulder (slumped)
    [-0.22, 1.25,   0.10],   # 4: L Elbow (hanging loosely)
    [0.22,  1.25,   0.10],   # 5: R Elbow (hanging loosely)
    [-0.24, 0.95,   0.12],   # 6: L Wrist
    [0.24,  0.95,   0.12],   # 7: R Wrist
    [0.0,   1.00,   0.00],   # 8: Pelvis
    [-0.15, 1.00,   0.00],   # 9: L Hip
    [0.15,  1.00,   0.00],   # 10: R Hip
    [-0.17, 0.50,   0.00],   # 11: L Knee
    [0.17,  0.50,   0.00],   # 12: R Knee
    [-0.19, 0.00,   0.00],   # 13: L Ankle
    [0.19,  0.00,   0.00],   # 14: R Ankle
])

# Define indices for body parts to apply differential motion
HEAD_NECK_indices = [0, 1]
# Shoulders are included with arms to create a realistic torso twist
ARMS_indices = [2, 3, 4, 5, 6, 7]
TORSO_LEGS_indices = [8, 9, 10, 11, 12, 13, 14]

def rotate_points_around_y(points, angle):
    """Rotates a set of 3D points around the vertical Y axis."""
    cos_a, sin_a = np.cos(angle), np.sin(angle)
    rotation_matrix_y = np.array([
        [cos_a, 0, sin_a],
        [0, 1, 0],
        [-sin_a, 0, cos_a]
    ])
    return points @ rotation_matrix_y.T

def main():
    """Main function to run the Pygame animation."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Woman Turning Around")
    clock = pygame.time.Clock()

    frame_count = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Animation Update ---
        
        # Create a copy of the base pose for modification in the current frame
        current_pose = base_pose_3d.copy()
        
        # 1. Add subtle, naturalistic secondary motions
        # A slow breathing motion affecting the torso's height (Y-axis)
        breath_period = FPS * 4  # A 4-second breath cycle
        breath_offset = np.sin(2 * np.pi * frame_count / breath_period) * 0.008
        current_pose[HEAD_NECK_indices, 1] += breath_offset
        current_pose[ARMS_indices, 1] += breath_offset
        current_pose[TORSO_LEGS_indices[:3], 1] += breath_offset * 0.5 # Pelvis/Hips

        # A slow, subtle body sway for balance
        sway_period = FPS * 6 # A 6-second sway cycle
        sway_x = np.sin(2 * np.pi * frame_count / sway_period) * 0.02
        sway_z = np.cos(2 * np.pi * frame_count / sway_period) * 0.01

        # 2. Calculate the main rotational movement
        # The turn is not rigid; different body parts turn at slightly different times.
        final_pose = np.zeros_like(current_pose)
        
        # The head and neck lead the turn slightly
        head_lead_frames = 8
        head_frame = (frame_count + head_lead_frames) % NUM_FRAMES
        head_angle = (head_frame / NUM_FRAMES) * 2 * np.pi
        final_pose[HEAD_NECK_indices] = rotate_points_around_y(current_pose[HEAD_NECK_indices], head_angle)

        # The arms and shoulders lag slightly, showing passive dynamics
        arm_lag_frames = 5
        arm_frame = (frame_count - arm_lag_frames + NUM_FRAMES) % NUM_FRAMES
        arm_angle = (arm_frame / NUM_FRAMES) * 2 * np.pi
        final_pose[ARMS_indices] = rotate_points_around_y(current_pose[ARMS_indices], arm_angle)
        
        # The main torso and legs turn at the base rate
        body_angle = (frame_count / NUM_FRAMES) * 2 * np.pi
        final_pose[TORSO_LEGS_indices] = rotate_points_around_y(current_pose[TORSO_LEGS_indices], body_angle)

        # Apply the overall body sway to the final rotated pose
        final_pose[:, 0] += sway_x
        final_pose[:, 2] += sway_z
        
        # --- Drawing ---
        screen.fill(BLACK)

        # Project the 3D points to the 2D screen for display
        scale = 350
        center_x, base_y = SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100

        for point_3d in final_pose:
            x_3d, y_3d, z_3d = point_3d
            
            # Simple orthographic projection
            screen_x = center_x + x_3d * scale
            screen_y = base_y - y_3d * scale  # Invert Y-axis for Pygame's coordinate system

            pygame.draw.circle(screen, WHITE, (int(screen_x), int(screen_y)), POINT_RADIUS)

        pygame.display.flip()

        # --- Timing ---
        frame_count = (frame_count + 1) % NUM_FRAMES
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
