
import pygame
import numpy as np
import sys

# --- Constants ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
NUM_POINTS = 15
POINT_RADIUS = 5
# A walking cycle (two steps) is set to take 1 second
CYCLE_DURATION_SECONDS = 1.0
NUM_FRAMES = int(CYCLE_DURATION_SECONDS * FPS)

def generate_walking_data():
    """
    Generates 3D coordinates for a 15-point walker over one walking cycle.
    The model uses forward kinematics with oscillating joint angles to simulate
    a 'happy' walk with a noticeable bounce and arm swing.
    The coordinate system is (X: side-to-side, Y: up-down, Z: forward-backward).
    """
    # --- Body Proportions for a lightweight female figure (in abstract units) ---
    head_size = 0.12
    neck_len = 0.05
    torso_len = 0.30
    shoulder_width = 0.22
    upper_arm_len = 0.18
    lower_arm_len = 0.16
    pelvis_width = 0.18
    upper_leg_len = 0.26
    lower_leg_len = 0.25

    # Array to hold all 3D points for all frames
    all_frames_3d = np.zeros((NUM_FRAMES, NUM_POINTS, 3))
    
    # Time vector for one cycle (angle from 0 to 2*pi)
    t = np.linspace(0, 2 * np.pi, NUM_FRAMES, endpoint=False)

    # --- Kinematic Model based on Oscillators ---

    def rot_x(angle):
        """Rotation matrix for rotation around the X-axis (sagittal plane)."""
        c, s = np.cos(angle), np.sin(angle)
        return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])

    # Pelvis motion (root of the hierarchy)
    # Vertical bounce (2 oscillations per cycle)
    pelvis_y = 0.035 * np.cos(2 * t)
    # Side-to-side sway (1 oscillation per cycle)
    pelvis_x = 0.04 * np.cos(t)
    
    pelvis_pos = np.array([pelvis_x, pelvis_y, np.zeros(NUM_FRAMES)]).T
    
    # Generate points for each frame
    for i in range(NUM_FRAMES):
        ti = t[i]
        
        # --- Core Body Structure ---
        pos_pelvis_center = pelvis_pos[i]
        pos_torso_center = pos_pelvis_center + np.array([0, torso_len, 0])
        pos_head = pos_torso_center + np.array([0, neck_len + head_size / 2, 0])

        # --- Legs ---
        # The right leg's motion is in phase with 't', left leg is phase-shifted by pi.
        vec_upper_leg = np.array([0, -upper_leg_len, 0])
        vec_lower_leg = np.array([0, -lower_leg_len, 0])

        # Right Leg
        phase_r_leg = ti
        hip_angle_r = -0.7 * np.cos(phase_r_leg)
        knee_angle_r = 1.3 * max(0, np.sin(phase_r_leg - 0.2))  # Hinge-like bend
        
        pos_hip_r = pos_pelvis_center + np.array([pelvis_width / 2, 0, 0])
        pos_knee_r = pos_hip_r + rot_x(hip_angle_r) @ vec_upper_leg
        pos_ankle_r = pos_knee_r + rot_x(hip_angle_r + knee_angle_r) @ vec_lower_leg

        # Left Leg
        phase_l_leg = ti + np.pi
        hip_angle_l = -0.7 * np.cos(phase_l_leg)
        knee_angle_l = 1.3 * max(0, np.sin(phase_l_leg - 0.2))
        
        pos_hip_l = pos_pelvis_center + np.array([-pelvis_width / 2, 0, 0])
        pos_knee_l = pos_hip_l + rot_x(hip_angle_l) @ vec_upper_leg
        pos_ankle_l = pos_knee_l + rot_x(hip_angle_l + knee_angle_l) @ vec_lower_leg

        # --- Arms ---
        # Arms swing in opposition to the corresponding leg.
        # Right arm swings with left leg, left arm with right leg.
        vec_upper_arm = np.array([0, -upper_arm_len, 0])
        vec_lower_arm = np.array([0, -lower_arm_len, 0])
        
        # Right Arm (phase of left leg)
        phase_r_arm = ti + np.pi
        shoulder_angle_r = -0.85 * np.cos(phase_r_arm) # Larger swing for "happy"
        elbow_angle_r = 0.9 * max(0, np.sin(phase_r_arm + 0.5))
        
        pos_shoulder_r = pos_torso_center + np.array([shoulder_width / 2, 0, 0])
        pos_elbow_r = pos_shoulder_r + rot_x(shoulder_angle_r) @ vec_upper_arm
        pos_wrist_r = pos_elbow_r + rot_x(shoulder_angle_r + elbow_angle_r) @ vec_lower_arm

        # Left Arm (phase of right leg)
        phase_l_arm = ti
        shoulder_angle_l = -0.85 * np.cos(phase_l_arm)
        elbow_angle_l = 0.9 * max(0, np.sin(phase_l_arm + 0.5))
        
        pos_shoulder_l = pos_torso_center + np.array([-shoulder_width / 2, 0, 0])
        pos_elbow_l = pos_shoulder_l + rot_x(shoulder_angle_l) @ vec_upper_arm
        pos_wrist_l = pos_elbow_l + rot_x(shoulder_angle_l + elbow_angle_l) @ vec_lower_arm
        
        # --- Assign all 15 points to the final array ---
        # The order matches common biological motion stimulus layouts.
        all_frames_3d[i, 0, :] = pos_head
        all_frames_3d[i, 1, :] = pos_shoulder_l
        all_frames_3d[i, 2, :] = pos_shoulder_r
        all_frames_3d[i, 3, :] = pos_elbow_l
        all_frames_3d[i, 4, :] = pos_elbow_r
        all_frames_3d[i, 5, :] = pos_wrist_l
        all_frames_3d[i, 6, :] = pos_wrist_r
        all_frames_3d[i, 7, :] = pos_hip_l
        all_frames_3d[i, 8, :] = pos_hip_r
        all_frames_3d[i, 9, :] = pos_knee_l
        all_frames_3d[i, 10, :] = pos_knee_r
        all_frames_3d[i, 11, :] = pos_ankle_l
        all_frames_3d[i, 12, :] = pos_ankle_r
        all_frames_3d[i, 13, :] = pos_torso_center # Sternum point
        all_frames_3d[i, 14, :] = pos_pelvis_center # Pelvis point
        
    # --- Post-processing ---
    # Center the entire animation vertically around y=0
    avg_y = np.mean(all_frames_3d[:, :, 1])
    all_frames_3d[:, :, 1] -= avg_y
    # Flip Y-axis so positive is 'up' in the model, matching screen coordinates
    all_frames_3d[:, :, 1] *= -1

    return all_frames_3d

def main():
    """
    Main function to initialize Pygame, run the animation loop, and handle events.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Happy Walking")
    clock = pygame.time.Clock()

    # Generate the 3D motion data before the loop starts
    try:
        motion_data_3d = generate_walking_data()
    except Exception as e:
        print(f"Error generating motion data: {e}")
        pygame.quit()
        sys.exit()
        
    # --- Scaling and Perspective ---
    # Calculate a scale factor to fit the figure nicely on the screen
    max_excursion = np.max(np.abs(motion_data_3d[:, :, :2])) # Use only X and Y for initial scaling
    if max_excursion == 0: max_excursion = 1
    scale_factor = (SCREEN_HEIGHT / 2.2) / max_excursion
    
    # Perspective projection focal length
    focal_length = 500

    frame_index = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- Drawing ---
        screen.fill(BLACK)

        # Get current frame's 3D points
        points_3d = motion_data_3d[frame_index]
        
        # Project 3D points to 2D screen coordinates
        projected_points = []
        for i, point_3d in enumerate(points_3d):
            x, y, z = point_3d
            
            # Simple perspective projection
            z_eff = z * scale_factor
            if focal_length + z_eff <= 0: # Avoid division by zero or negative
                scale_z = 1000 # Put point way off screen if it's at the focal point
            else:
                scale_z = focal_length / (focal_length + z_eff)

            screen_x = x * scale_factor * scale_z + SCREEN_WIDTH / 2
            screen_y = y * scale_factor * scale_z + SCREEN_HEIGHT / 2
            
            # Scale point size based on depth for a better 3D effect
            radius = int(POINT_RADIUS * scale_z)
            if radius < 1: radius = 1
            
            # Store projected position, radius, and original Z for sorting
            projected_points.append(((int(screen_x), int(screen_y)), radius, z))

        # Sort points by depth (Z-coordinate) so closer points are drawn on top
        projected_points.sort(key=lambda p: p[2], reverse=False)

        # Draw the sorted points
        for pos, radius, z in projected_points:
            pygame.draw.circle(screen, WHITE, pos, radius)

        pygame.display.flip()

        # --- Update ---
        frame_index = (frame_index + 1) % NUM_FRAMES
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
