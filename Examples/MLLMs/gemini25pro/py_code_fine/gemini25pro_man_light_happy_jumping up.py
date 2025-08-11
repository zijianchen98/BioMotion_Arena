
import pygame
import numpy as np

def main():
    """
    This program generates and displays a point-light stimulus animation
    of a 'happyman' performing a jump. The animation adheres to the specified
    requirements: 15 white points on a black background, representing a
    biomechanically plausible and smooth jumping motion.
    """

    # --- Setup: Pygame and Animation Constants ---
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Jumping Up")

    # Colors and visual style
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    DOT_RADIUS = 5

    # Animation parameters
    FPS = 60
    TOTAL_FRAMES = 150  # Total frames for one complete jump cycle (2.5 seconds at 60 FPS)
    clock = pygame.time.Clock()

    # --- Skeleton Definition: Proportions and Joints ---
    # Limb lengths define the figure's proportions
    L_UPPER_ARM = 50
    L_LOWER_ARM = 45
    L_UPPER_LEG = 60
    L_LOWER_LEG = 55
    L_SHOULDER = 40  # Distance from sternum to shoulder joint
    L_HIP = 35       # Distance from pelvis to hip joint
    L_SPINE = 60     # Distance from pelvis to sternum
    L_NECK = 20      # Distance from sternum to head

    # Joint indices for the 15 points
    HEAD, STERNUM, PELVIS = 0, 1, 2
    L_SHOULDER_J, R_SHOULDER_J = 3, 4
    L_ELBOW, R_ELBOW = 5, 6
    L_WRIST, R_WRIST = 7, 8
    L_HIP_J, R_HIP_J = 9, 10
    L_KNEE, R_KNEE = 11, 12
    L_ANKLE, R_ANKLE = 13, 14

    def get_jump_state(frame):
        """
        Calculates the 2D coordinates of all 15 joints for a given animation frame.
        The motion is procedurally generated using sinusoidal functions for smooth transitions.
        """
        progress = frame / TOTAL_FRAMES

        # --- Phase Timings (as a fraction of the total animation) ---
        crouch_end = 0.25
        takeoff_end = 0.35
        flight_end = 0.75
        land_end = 0.85
        # recovery_end is 1.0

        # --- 1. Global Body Motion (Center of Mass) ---
        base_x = WIDTH / 2
        ground_y = HEIGHT - 150
        crouch_depth = 80
        jump_height = 250

        # Vertical position of the pelvis (approximates center of mass)
        pelvis_y = ground_y
        if progress < crouch_end:  # Phase 1: Crouch
            p = progress / crouch_end
            pelvis_y = ground_y - crouch_depth * 0.5 * (1 - np.cos(p * np.pi))
        elif progress < takeoff_end:  # Phase 2: Takeoff preparation
            pelvis_y = ground_y - crouch_depth
        elif progress < flight_end:  # Phase 3: Flight
            p = (progress - takeoff_end) / (flight_end - takeoff_end)
            pelvis_y = (ground_y - crouch_depth) - jump_height * np.sin(p * np.pi)
        elif progress < land_end:  # Phase 4: Landing
            p = (progress - flight_end) / (land_end - flight_end)
            p_ease = 0.5 * (1 - np.cos(p * np.pi))
            pelvis_y = ground_y - crouch_depth * p_ease
        else:  # Phase 5: Recovery
            p = (progress - land_end) / (1.0 - land_end)
            pelvis_y = (ground_y - crouch_depth) + crouch_depth * 0.5 * (1 - np.cos(p * np.pi))

        pelvis_pos = np.array([base_x, pelvis_y])

        # --- 2. Joint Angles and Poses ---
        # Angles are calculated for each phase to create coordinated motion.
        
        # Torso angle (lean)
        torso_angle = 0
        if progress < crouch_end:
            p = progress / crouch_end
            torso_angle = np.deg2rad(20 * p)
        elif progress < takeoff_end:
            p = (progress - crouch_end) / (takeoff_end - crouch_end)
            torso_angle = np.deg2rad(20 - 40 * p)
        elif progress < land_end:
            torso_angle = np.deg2rad(-20 * np.sin((progress - takeoff_end)/(land_end - takeoff_end) * np.pi))
        else:
            p = (progress - land_end) / (1.0 - land_end)
            torso_angle = np.deg2rad(0) 

        # Leg angles (flexion)
        hip_angle, knee_angle = 0, 0
        if progress < crouch_end:
            p = progress / crouch_end
            hip_angle, knee_angle = np.deg2rad(80 * p), np.deg2rad(-90 * p)
        elif progress < takeoff_end:
            p = (progress - crouch_end) / (takeoff_end - crouch_end)
            hip_angle, knee_angle = np.deg2rad(80 - 80 * p), np.deg2rad(-90 + 90 * p)
        elif progress < flight_end:
            p = (progress - takeoff_end) / (flight_end - takeoff_end)
            pulse = np.sin(p * np.pi)
            hip_angle, knee_angle = np.deg2rad(60) * pulse, np.deg2rad(-70) * pulse
        elif progress < land_end:
            p = (progress - flight_end) / (land_end - flight_end)
            hip_angle, knee_angle = np.deg2rad(80 * p), np.deg2rad(-90 * p)
        else:
            p = (progress - land_end) / (1.0 - land_end)
            hip_angle, knee_angle = np.deg2rad(80 * (1 - p)), np.deg2rad(-90 * (1 - p))

        # Arm angles (flexion)
        shoulder_angle, elbow_angle = 0, 0
        if progress < crouch_end:
            p = progress / crouch_end
            shoulder_angle, elbow_angle = np.deg2rad(-60 * p), np.deg2rad(30 * p)
        elif progress < takeoff_end:
            p = (progress - crouch_end) / (takeoff_end - crouch_end)
            shoulder_angle = np.deg2rad(-60 + 220 * p)
        elif progress < flight_end:
            shoulder_angle, elbow_angle = np.deg2rad(160), np.deg2rad(30)
        elif progress < land_end:
            p = (progress - flight_end) / (land_end - flight_end)
            shoulder_angle = np.deg2rad(160 - 140 * p)
        else:
            p = (progress - land_end) / (1.0 - land_end)
            shoulder_angle, elbow_angle = np.deg2rad(20 * (1 - p)), np.deg2rad(30 * (1-p))

        # "Happy" pose abduction (sideways spread) during flight
        arm_abduction, leg_abduction = 0, 0
        if flight_end > progress > takeoff_end:
            p = (progress - takeoff_end) / (flight_end - takeoff_end)
            abduction_pulse = np.sin(p * np.pi)
            arm_abduction = np.deg2rad(70) * abduction_pulse
            leg_abduction = np.deg2rad(40) * abduction_pulse

        # --- 3. Forward Kinematics: Calculate Joint Positions ---
        points = [np.zeros(2) for _ in range(15)]
        
        points[PELVIS] = pelvis_pos
        points[STERNUM] = points[PELVIS] + L_SPINE * np.array([np.sin(torso_angle), -np.cos(torso_angle)])
        points[HEAD] = points[STERNUM] + L_NECK * np.array([np.sin(torso_angle), -np.cos(torso_angle)])

        points[L_SHOULDER_J] = points[STERNUM] + L_SHOULDER * np.array([-np.cos(torso_angle), -np.sin(torso_angle)])
        points[R_SHOULDER_J] = points[STERNUM] + L_SHOULDER * np.array([np.cos(torso_angle), -np.sin(torso_angle)])
        points[L_HIP_J] = points[PELVIS] + L_HIP * np.array([-np.cos(torso_angle), -np.sin(torso_angle)])
        points[R_HIP_J] = points[PELVIS] + L_HIP * np.array([np.cos(torso_angle), -np.sin(torso_angle)])

        angle1 = torso_angle + shoulder_angle + arm_abduction
        angle2 = angle1 + elbow_angle
        points[R_ELBOW] = points[R_SHOULDER_J] + L_UPPER_ARM * np.array([np.sin(angle1), -np.cos(angle1)])
        points[R_WRIST] = points[R_ELBOW] + L_LOWER_ARM * np.array([np.sin(angle2), -np.cos(angle2)])

        angle1 = torso_angle - shoulder_angle - arm_abduction
        angle2 = angle1 - elbow_angle
        points[L_ELBOW] = points[L_SHOULDER_J] + L_UPPER_ARM * np.array([np.sin(angle1), -np.cos(angle1)])
        points[L_WRIST] = points[L_ELBOW] + L_LOWER_ARM * np.array([np.sin(angle2), -np.cos(angle2)])

        angle1 = torso_angle + hip_angle + leg_abduction
        angle2 = angle1 + knee_angle
        points[R_KNEE] = points[R_HIP_J] + L_UPPER_LEG * np.array([np.sin(angle1), -np.cos(angle1)])
        points[R_ANKLE] = points[R_KNEE] + L_LOWER_LEG * np.array([np.sin(angle2), -np.cos(angle2)])

        angle1 = torso_angle - hip_angle - leg_abduction
        angle2 = angle1 - knee_angle
        points[L_KNEE] = points[L_HIP_J] + L_UPPER_LEG * np.array([np.sin(angle1), -np.cos(angle1)])
        points[L_ANKLE] = points[L_KNEE] + L_LOWER_LEG * np.array([np.sin(angle2), -np.cos(angle2)])

        return points

    # --- Main Animation Loop ---
    running = True
    start_time = pygame.time.get_ticks()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        elapsed_time = pygame.time.get_ticks() - start_time
        frame_duration_ms = 1000 / FPS
        current_frame = int((elapsed_time / frame_duration_ms) % TOTAL_FRAMES)
        
        points = get_jump_state(current_frame)
        
        screen.fill(BLACK)
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), DOT_RADIUS)
            
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
