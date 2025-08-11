
import pygame
import numpy as np
import sys

def main():
    """
    This program displays a point-light animation of a sad man bowing.
    The animation consists of 15 white dots on a black background,
    simulating biological motion in a smooth and plausible manner.
    """
    pygame.init()

    # --- Configuration ---
    WIDTH, HEIGHT = 600, 800
    FPS = 60
    BACKGROUND_COLOR = (0, 0, 0)
    DOT_COLOR = (255, 255, 255)
    DOT_RADIUS = 6

    # --- Pygame Setup ---
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Bow")
    clock = pygame.time.Clock()

    # --- Keyframe Data ---
    # Keyframe 1: Standing with a sad, slumped posture
    kf_stand = [
        (300, 230),  # 1. Head (tilted forward)
        (300, 270),  # 2. Neck
        (300, 320),  # 3. Sternum
        (260, 310),  # 4. L Shoulder (rounded forward)
        (340, 310),  # 5. R Shoulder (rounded forward)
        (250, 380),  # 6. L Elbow
        (350, 380),  # 7. R Elbow
        (245, 450),  # 8. L Wrist
        (355, 450),  # 9. R Wrist
        (280, 460),  # 10. L Hip
        (320, 460),  # 11. R Hip
        (285, 540),  # 12. L Knee (slight bend)
        (315, 540),  # 13. R Knee (slight bend)
        (285, 620),  # 14. L Ankle
        (315, 620),  # 15. R Ankle
    ]

    # Keyframe 2: Full bow position
    kf_full_bow = [
        (450, 380),  # 1. Head
        (420, 390),  # 2. Neck
        (370, 410),  # 3. Sternum
        (340, 390),  # 4. L Shoulder
        (390, 430),  # 5. R Shoulder (perspective)
        (335, 470),  # 6. L Elbow (hanging)
        (385, 510),  # 7. R Elbow (hanging)
        (330, 550),  # 8. L Wrist (hanging)
        (380, 590),  # 9. R Wrist (hanging)
        (285, 465),  # 10. L Hip
        (315, 465),  # 11. R Hip
        (290, 545),  # 12. L Knee (more bend)
        (310, 545),  # 13. R Knee (more bend)
        (285, 620),  # 14. L Ankle (fixed)
        (315, 620),  # 15. R Ankle (fixed)
    ]

    # --- Animation Generation ---
    def interpolate_poses(pose1, pose2, num_steps):
        """Generates a sequence of frames between two poses using smoothstep easing."""
        frames = []
        if num_steps == 0:
            return frames
        # Create num_steps frames, where t goes from 0 to 1
        for i in range(num_steps):
            t = i / (num_steps - 1) if num_steps > 1 else 0
            # Smoothstep easing function for natural acceleration/deceleration
            t_eased = t * t * (3.0 - 2.0 * t)
            current_frame = []
            for j in range(len(pose1)):
                p1 = np.array(pose1[j], dtype=float)
                p2 = np.array(pose2[j], dtype=float)
                p_interp = p1 + (p2 - p1) * t_eased
                current_frame.append(tuple(p_interp.astype(int)))
            frames.append(current_frame)
        return frames

    animation_data = []
    
    # Define the duration of each phase of the animation
    num_stand_frames = 20
    num_bow_down_frames = 50
    num_hold_frames = 20
    num_rise_up_frames = 50

    # Phase 1: Stand still
    for _ in range(num_stand_frames):
        animation_data.append(kf_stand)

    # Phase 2: Bow down
    bow_down_frames = interpolate_poses(kf_stand, kf_full_bow, num_bow_down_frames)
    animation_data.extend(bow_down_frames)

    # Phase 3: Hold the bow
    for _ in range(num_hold_frames):
        animation_data.append(kf_full_bow)

    # Phase 4: Rise up
    rise_up_frames = interpolate_poses(kf_full_bow, kf_stand, num_rise_up_frames)
    animation_data.extend(rise_up_frames)

    # --- Main Loop ---
    frame_index = 0
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Drawing
        screen.fill(BACKGROUND_COLOR)

        current_frame_points = animation_data[frame_index]
        for point in current_frame_points:
            pygame.draw.circle(screen, DOT_COLOR, point, DOT_RADIUS)

        pygame.display.flip()

        # Update frame counter for looping animation
        frame_index = (frame_index + 1) % len(animation_data)
        
        # Control frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
