
import pygame
import numpy as np
import sys

def create_animation():
    """
    Generates the frames for a point-light animation of a person bowing
    with a heavy weight. The animation consists of 15 points.
    """
    # --- Constants for skeleton definition ---
    # These indices map to the points in the pose arrays
    HEAD, NECK, STERNUM = 0, 1, 2
    R_SHOULDER, L_SHOULDER = 3, 4
    R_ELBOW, L_ELBOW = 5, 6
    R_WRIST, L_WRIST = 7, 8
    R_HIP, L_HIP = 9, 10
    R_KNEE, L_KNEE = 11, 12
    R_ANKLE, L_ANKLE = 13, 14

    # --- Keyframe 1: Standing Pose ---
    # Defines the initial upright position of the 15 points.
    # Coordinates are centered for an 800x600 window.
    center_x, center_y = 400, 280
    standing_pose = np.array([
        [center_x, center_y - 130],      # Head
        [center_x, center_y - 110],      # Neck
        [center_x, center_y - 70],       # Sternum
        [center_x - 40, center_y - 100], # R_Shoulder (figure's right)
        [center_x + 40, center_y - 100], # L_Shoulder
        [center_x - 40, center_y - 50],  # R_Elbow
        [center_x + 40, center_y - 50],  # L_Elbow
        [center_x - 40, center_y],       # R_Wrist
        [center_x + 40, center_y],       # L_Wrist
        [center_x - 30, center_y - 10],  # R_Hip
        [center_x + 30, center_y - 10],  # L_Hip
        [center_x - 30, center_y + 60],  # R_Knee
        [center_x + 30, center_y + 60],  # L_Knee
        [center_x - 30, center_y + 130], # R_Ankle
        [center_x + 30, center_y + 130], # L_Ankle
    ])

    # --- Keyframe 2: Bowed Pose ---
    # Defines the pose at the bottom of the bow, simulating a heavy lift.
    bowed_pose = np.zeros_like(standing_pose)
    
    # Ankles are the base and remain stationary.
    bowed_pose[[R_ANKLE, L_ANKLE]] = standing_pose[[R_ANKLE, L_ANKLE]]

    # To counterbalance, hips move backward and down slightly.
    hip_backward_shift = 70
    bowed_pose[R_HIP] = [standing_pose[R_HIP][0] - hip_backward_shift, standing_pose[R_HIP][1] + 10]
    bowed_pose[L_HIP] = [standing_pose[L_HIP][0] - hip_backward_shift, standing_pose[L_HIP][1] + 10]

    # Knees bend to accommodate the hip shift.
    bowed_pose[R_KNEE] = [standing_pose[R_KNEE][0] - hip_backward_shift / 2, standing_pose[R_KNEE][1] - 20]
    bowed_pose[L_KNEE] = [standing_pose[L_KNEE][0] - hip_backward_shift / 2, standing_pose[L_KNEE][1] - 20]
    
    # Upper body pivots forward around the new hip center.
    old_hip_pivot = np.mean(standing_pose[[R_HIP, L_HIP]], axis=0)
    new_hip_pivot = np.mean(bowed_pose[[R_HIP, L_HIP]], axis=0)
    bow_angle = np.radians(85) # Deep bow, almost horizontal torso
    c, s = np.cos(bow_angle), np.sin(bow_angle)
    rot_matrix = np.array([[c, -s], [s, c]])
    
    # Calculate rotated positions for torso and head.
    upper_body_indices = [NECK, STERNUM, R_SHOULDER, L_SHOULDER, HEAD]
    for i in upper_body_indices:
        rel_pos = standing_pose[i] - old_hip_pivot
        new_rel_pos = rel_pos @ rot_matrix.T
        bowed_pose[i] = new_rel_pos + new_hip_pivot

    # Arms hang straight down as if holding a heavy weight (e.g., a barbell).
    bowed_pose[R_ELBOW] = bowed_pose[R_SHOULDER] + np.array([5, 50])
    bowed_pose[L_ELBOW] = bowed_pose[L_SHOULDER] + np.array([-5, 50])
    bowed_pose[R_WRIST] = bowed_pose[R_ELBOW] + np.array([5, 50])
    bowed_pose[L_WRIST] = bowed_pose[L_ELBOW] + np.array([-5, 50])

    # --- Frame Generation ---
    # Interpolate between keyframes to create a smooth animation.
    
    # Easing function for a natural, weighted feel.
    def ease_in_out_cubic(t):
        t *= 2
        if t < 1:
            return 0.5 * t * t * t
        t -= 2
        return 0.5 * (t * t * t + 2)

    frames = []
    num_transition_frames = 100 # Slower motion for "heavy" feel
    num_pause_frames = 45      # Pause at extremes
    
    # Phase 1: Initial pause
    frames.extend([standing_pose] * num_pause_frames)
    
    # Phase 2: Bowing down
    for i in range(num_transition_frames + 1):
        t = i / num_transition_frames
        eased_t = ease_in_out_cubic(t)
        current_frame = standing_pose * (1 - eased_t) + bowed_pose * eased_t
        frames.append(current_frame)
        
    # Phase 3: Pause at the bottom
    frames.extend([bowed_pose] * num_pause_frames)
    
    # Phase 4: Rising up
    for i in range(num_transition_frames + 1):
        t = i / num_transition_frames
        eased_t = ease_in_out_cubic(t)
        current_frame = bowed_pose * (1 - eased_t) + standing_pose * eased_t
        frames.append(current_frame)
        
    # Phase 5: Final pause
    frames.extend([standing_pose] * num_pause_frames)
    
    return frames


def main():
    """
    Main function to initialize pygame and run the animation loop.
    """
    pygame.init()

    # --- Screen and Animation Setup ---
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FPS = 60
    POINT_RADIUS = 6

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Bowing with Heavy Weight")
    clock = pygame.time.Clock()

    try:
        animation_frames = create_animation()
    except Exception:
        pygame.quit()
        sys.exit()

    frame_count = len(animation_frames)
    current_frame_index = 0

    # --- Main Game Loop ---
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
        
        # Get the coordinates for the current frame
        points = animation_frames[current_frame_index]
        
        # Draw each of the 15 points
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), POINT_RADIUS)

        # --- Update ---
        pygame.display.flip()
        
        # Move to the next frame
        current_frame_index = (current_frame_index + 1) % frame_count
        
        # Control the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
