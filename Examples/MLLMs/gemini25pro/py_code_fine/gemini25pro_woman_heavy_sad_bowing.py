
import pygame
import numpy as np
import math
import sys

# --- Constants ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
# Slower duration to convey sadness and weight
ANIMATION_DURATION_S = 7.0
POINT_RADIUS = 6

# --- 3D Projection Setup ---
PROJECTION_CENTER_X = SCREEN_WIDTH / 2
PROJECTION_CENTER_Y = SCREEN_HEIGHT / 2 - 50 # Shift figure up slightly
# Scale controls the size of the figure on screen
PERSPECTIVE_SCALE = 400
# Z_OFFSET moves the whole figure away from the camera to prevent clipping
Z_OFFSET = 6

def define_poses():
    """Defines the start and end poses for the bowing animation."""

    # --- Start Pose: Sad Woman with Heavy Weight Stance ---
    # This pose is characterized by a slumped posture, bent knees, and a bowed head.
    # Coordinates are in a model space where Y is up, X is right, and Z is forward.
    pose_start = [
        # Name         # (x,   y,    z)
        np.array([0,   80, -15]),    # 0: Head (bowed forward)
        np.array([0,   55, -8]),     # 1: Sternum (slumped)
        np.array([0,   15,  0]),     # 2: Pelvis
        np.array([-20, 50, -12]),    # 3: Left Shoulder (slumped)
        np.array([20,  50, -12]),    # 4: Right Shoulder (slumped)
        np.array([-23, 20, -15]),    # 5: Left Elbow
        np.array([23,  20, -15]),    # 6: Right Elbow
        np.array([-25, -10, -12]),   # 7: Left Wrist
        np.array([25, -10, -12]),    # 8: Right Wrist
        np.array([-12, 15,  0]),     # 9: Left Hip
        np.array([12,  15,  0]),     # 10: Right Hip
        np.array([-10, -35, -5]),    # 11: Left Knee (bent under weight)
        np.array([10, -35, -5]),     # 12: Right Knee (bent under weight)
        np.array([-10, -85,  0]),    # 13: Left Ankle
        np.array([10, -85,  0]),     # 14: Right Ankle
    ]

    # --- End Pose: Full Bow ---
    # The figure squats and bows deeply, with arms hanging loosely.
    pose_end = [np.zeros(3) for _ in range(15)]
    
    # Parameters for the bow and squat motion
    bow_angle_rad = np.radians(-85) # Deep bow
    squat_y_offset = -35           # How much the body lowers
    squat_z_offset = 20            # How much the hips move back for balance

    # Calculate lower body positions in the end pose
    # Ankles are fixed points on the ground
    pose_end[13] = pose_start[13]
    pose_end[14] = pose_start[14]
    # Knees bend and move forward
    pose_end[11] = np.array([-10, -45 + squat_y_offset, 45])
    pose_end[12] = np.array([10,  -45 + squat_y_offset, 45])
    # Hips lower and move back
    pose_end[9] = np.array([-12, 15 + squat_y_offset, squat_z_offset])
    pose_end[10] = np.array([12, 15 + squat_y_offset, squat_z_offset])
    pose_end[2] = np.array([0,   15 + squat_y_offset, squat_z_offset])

    # Calculate upper body positions by rotating around the hip/pelvis area
    c, s = np.cos(bow_angle_rad), np.sin(bow_angle_rad)
    rotation_matrix_x = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    
    pelvis_start_pos = pose_start[2]
    pelvis_end_pos = pose_end[2]

    # Rotate head, sternum, and shoulders
    for i in [0, 1, 3, 4]:
        vec_from_pelvis = pose_start[i] - pelvis_start_pos
        rotated_vec = rotation_matrix_x @ vec_from_pelvis
        pose_end[i] = pelvis_end_pos + rotated_vec

    # Calculate arm positions (hanging due to gravity)
    # Get limb lengths from the start pose
    l_sh_elb_dist = np.linalg.norm(pose_start[3] - pose_start[5])
    l_elb_wr_dist = np.linalg.norm(pose_start[5] - pose_start[7])
    
    # A vector representing the direction arms hang (mostly down, slightly forward)
    arm_hang_vec = np.array([0.05, -0.95, 0.3])
    arm_hang_vec /= np.linalg.norm(arm_hang_vec)

    # Left arm
    pose_end[5] = pose_end[3] + arm_hang_vec * l_sh_elb_dist
    pose_end[7] = pose_end[5] + arm_hang_vec * l_elb_wr_dist
    # Right arm (mirror x component)
    pose_end[6] = pose_end[4] + np.array([-1, 1, 1]) * arm_hang_vec * l_sh_elb_dist
    pose_end[8] = pose_end[6] + np.array([-1, 1, 1]) * arm_hang_vec * l_elb_wr_dist

    return pose_start, pose_end

def main():
    """Main function to run the Pygame animation."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Woman Bowing")
    clock = pygame.time.Clock()

    pose_start, pose_end = define_poses()
    start_time = pygame.time.get_ticks()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # --- Animation Logic ---
        # Calculate a time-based phase (0.0 to 1.0) for the looping animation
        elapsed_time_s = (pygame.time.get_ticks() - start_time) / 1000.0
        phase = (elapsed_time_s % ANIMATION_DURATION_S) / ANIMATION_DURATION_S
        
        # Use a cosine easing function for smooth acceleration and deceleration
        # This makes the motion go from start -> end -> start in one cycle
        interp_factor = (1 - math.cos(phase * 2 * math.pi)) / 2.0

        # --- Interpolate and Project Points ---
        screen.fill(BLACK)
        
        projected_points = []
        for i in range(len(pose_start)):
            # Linearly interpolate between the start and end pose
            p3d = pose_start[i] * (1 - interp_factor) + pose_end[i] * interp_factor
            
            # Add a slight tremor to upper body to convey strain/weight
            if i <= 8: # Head, torso, arms
                tremor_amount = 0.5
                tremor = np.random.uniform(-tremor_amount, tremor_amount, 3)
                # Reduce tremor as the body lowers to rest
                tremor *= (1 - interp_factor)
                p3d += tremor

            # Perspective projection from 3D to 2D
            z_with_offset = p3d[2] + Z_OFFSET
            if z_with_offset > 0:
                # The perspective division
                scale_factor = PERSPECTIVE_SCALE / z_with_offset
                # Project and center on screen
                # Y is inverted because Pygame's Y-axis goes down
                x = PROJECTION_CENTER_X + p3d[0] * scale_factor
                y = PROJECTION_CENTER_Y - p3d[1] * scale_factor
                projected_points.append((int(x), int(y)))

        # Draw the projected points
        for p2d in projected_points:
            pygame.draw.circle(screen, WHITE, p2d, POINT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
