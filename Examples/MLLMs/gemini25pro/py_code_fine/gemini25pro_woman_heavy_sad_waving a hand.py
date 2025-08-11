
import pygame
import numpy as np
import sys

def generate_animation_data(num_frames, fps, width, height):
    """
    Generates the kinematic data for the animation.
    
    Returns:
        A list of frames, where each frame is a list of 15 (x, y) coordinates.
    """
    animation_data = []
    duration = num_frames / fps

    # --- Skeleton Proportions ---
    # Factors to represent a "heavy" build
    body_width_factor = 1.15
    body_depth_factor = 1.1 # For subtle posture effects

    # Limb lengths in pixels
    head_radius = 12
    neck_length = 25
    torso_length = 120
    shoulder_width = 95 * body_width_factor
    upper_arm_length = 70
    lower_arm_length = 65
    wrist_to_hand_point = 10
    hip_width = 85 * body_width_factor
    upper_leg_length = 90
    lower_leg_length = 85
    ankle_to_foot_point = 15

    # --- "Sad" Posture Parameters ---
    head_tilt_rad = -0.25  # Forward head tilt
    shoulder_slump_y = 20 # How far shoulders drop
    spine_hunch_x = -20 * body_depth_factor # Forward hunch

    for frame_idx in range(num_frames):
        t = frame_idx / fps
        
        frame_points = {}

        # --- Body Sway (Center of Mass Shift) ---
        # Slow, ponderous sway to suggest weight
        sway_x = 4 * np.sin(t * np.pi * 0.5) 
        sway_y = 2 * np.sin(t * np.pi) 

        # --- Core Body Structure ---
        # Pelvis is the root of the hierarchy
        pelvis_center = np.array([width / 2 + sway_x, height * 0.65 + sway_y])
        
        # Neck base position relative to pelvis, with hunch
        neck_base = pelvis_center + np.array([spine_hunch_x, -torso_length])
        
        # Head
        head_base = neck_base + np.array([0, -neck_length])
        head_top = head_base + np.array([np.sin(head_tilt_rad) * head_radius * 2, 
                                         -np.cos(head_tilt_rad) * head_radius * 2])

        # Shoulders (slumped)
        r_shoulder = neck_base + np.array([shoulder_width / 2, shoulder_slump_y])
        l_shoulder = neck_base + np.array([-shoulder_width / 2, shoulder_slump_y])

        # Hips
        r_hip = pelvis_center + np.array([hip_width / 2, 0])
        l_hip = pelvis_center + np.array([-hip_width / 2, 0])

        # --- Legs ---
        # Legs have slight bend and follow the body sway
        r_knee = r_hip + np.array([5, upper_leg_length])
        l_knee = l_hip + np.array([-5, upper_leg_length])
        r_ankle = r_knee + np.array([0, lower_leg_length])
        l_ankle = l_knee + np.array([0, lower_leg_length])

        # --- Left Arm (Passive) ---
        # Hangs down with slight bend, influenced by torso
        l_arm_hang_angle = 0.15 # Radians, away from vertical
        l_elbow_angle = l_arm_hang_angle + 0.1
        l_elbow = l_shoulder + np.array([-np.sin(l_arm_hang_angle) * upper_arm_length, 
                                          np.cos(l_arm_hang_angle) * upper_arm_length])
        l_wrist = l_elbow + np.array([-np.sin(l_elbow_angle) * lower_arm_length, 
                                       np.cos(l_elbow_angle) * lower_arm_length])

        # --- Right Arm (Waving) ---
        # Easing function for smooth acceleration/deceleration
        def ease_in_out_quad(x):
            return 2 * x * x if x < 0.5 else 1 - pow(-2 * x + 2, 2) / 2

        # Timings for the wave action
        lift_start, lift_end = 0.5, 1.7
        wave_start, wave_end = 1.7, 4.0
        lower_start, lower_end = 4.0, 5.5

        # Base angles for the arm at rest
        shoulder_angle_rest = 0.1
        elbow_angle_rest = 0.2
        
        # Target angles for the wave
        shoulder_angle_lift = -np.pi / 2.1 # Arm raised to the side
        
        # Initialize angles
        current_shoulder_angle = shoulder_angle_rest
        current_elbow_angle = elbow_angle_rest

        if lift_start <= t < lift_end:
            progress = (t - lift_start) / (lift_end - lift_start)
            eased_progress = ease_in_out_quad(progress)
            current_shoulder_angle = shoulder_angle_rest + eased_progress * (shoulder_angle_lift - shoulder_angle_rest)
            current_elbow_angle = elbow_angle_rest + eased_progress * (np.pi/4 - elbow_angle_rest)
        
        elif wave_start <= t < wave_end:
            current_shoulder_angle = shoulder_angle_lift
            # Slow, sad wave motion from the elbow
            wave_time = t - wave_start
            wave_freq = 2 * np.pi * 2.0 / (wave_end - wave_start) # 2 cycles
            wave_amp = np.pi / 5
            current_elbow_angle = np.pi / 4 + wave_amp * np.sin(wave_freq * wave_time)
            
        elif lower_start <= t < lower_end:
            progress = (t - lower_start) / (lower_end - lower_start)
            eased_progress = ease_in_out_quad(progress)
            current_shoulder_angle = shoulder_angle_lift * (1 - eased_progress) + shoulder_angle_rest * eased_progress
            current_elbow_angle = (np.pi/4) * (1-eased_progress) + elbow_angle_rest * eased_progress

        elif t >= lower_end:
             current_shoulder_angle = shoulder_angle_rest
             current_elbow_angle = elbow_angle_rest
        
        # Calculate final joint positions for right arm
        r_elbow = r_shoulder + np.array([np.sin(current_shoulder_angle) * upper_arm_length, 
                                         np.cos(current_shoulder_angle) * upper_arm_length])
        total_elbow_angle = current_shoulder_angle + current_elbow_angle
        r_wrist = r_elbow + np.array([np.sin(total_elbow_angle) * lower_arm_length, 
                                      np.cos(total_elbow_angle) * lower_arm_length])
        
        # --- Assemble 15 points for the frame ---
        # This standard 15-point configuration is ideal for representing biological motion.
        points_in_order = [
            head_top,      # 1. Head
            neck_base,     # 2. Neck
            l_shoulder,    # 3. Left Shoulder
            r_shoulder,    # 4. Right Shoulder
            l_elbow,       # 5. Left Elbow
            r_elbow,       # 6. Right Elbow
            l_wrist,       # 7. Left Wrist
            r_wrist,       # 8. Right Wrist
            pelvis_center, # 9. Pelvis
            l_hip,         # 10. Left Hip
            r_hip,         # 11. Right Hip
            l_knee,        # 12. Left Knee
            r_knee,        # 13. Right Knee
            l_ankle,       # 14. Left Ankle
            r_ankle        # 15. Right Ankle
        ]
        animation_data.append([(int(p[0]), int(p[1])) for p in points_in_order])

    return animation_data

def main():
    """
    Main function to set up Pygame and run the animation loop.
    """
    pygame.init()

    # --- Animation and Display Constants ---
    WIDTH, HEIGHT = 600, 800
    BACKGROUND_COLOR = (0, 0, 0)
    POINT_COLOR = (255, 255, 255)
    POINT_RADIUS = 6
    FPS = 60
    ANIMATION_DURATION_S = 6.0
    NUM_FRAMES = int(ANIMATION_DURATION_S * FPS)

    # --- Set up the display ---
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Woman Waving")
    clock = pygame.time.Clock()

    # --- Generate all animation frames once ---
    print("Generating animation data...")
    animation_frames = generate_animation_data(NUM_FRAMES, FPS, WIDTH, HEIGHT)
    print("...Done.")

    # --- Main Loop ---
    running = True
    current_frame_idx = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- Drawing ---
        screen.fill(BACKGROUND_COLOR)
        
        # Get points for the current frame
        points_to_draw = animation_frames[current_frame_idx]
        
        # Draw each point
        for point in points_to_draw:
            pygame.draw.circle(screen, POINT_COLOR, point, POINT_RADIUS)

        # --- Update ---
        pygame.display.flip()
        
        # --- Advance to next frame ---
        current_frame_idx = (current_frame_idx + 1) % NUM_FRAMES
        
        # --- Control frame rate ---
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
