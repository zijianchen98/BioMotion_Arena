
import pygame
import math

def main():
    """
    This program creates a point-light stimulus animation of a person waving.
    It uses the pygame library to generate the graphics.
    The animation depicts a figure made of 15 white points on a black background.
    The motion is designed to be smooth, realistic, and biomechanically plausible,
    following a cyclical pattern of standing, raising an arm, waving, and lowering the arm.
    """
    pygame.init()

    # --- Constants ---
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FPS = 60
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    POINT_RADIUS = 5

    # --- Subject Proportions (in pixels) ---
    # These define the skeleton's dimensions, aiming for a "light weight" build.
    TORSO_LENGTH = 130
    UPPER_ARM_LENGTH = 75
    FOREARM_LENGTH = 80
    THIGH_LENGTH = 95
    SHIN_LENGTH = 90
    HEAD_OFFSET = 30  # Y-offset from the sternum for the head point
    SHOULDER_WIDTH = 90
    HIP_WIDTH = 70
    
    # --- Animation Cycle Parameters ---
    # The entire action sequence loops over a defined period.
    CYCLE_DURATION_S = 9.0
    CYCLE_FRAMES = int(CYCLE_DURATION_S * FPS)
    
    # Define the timing for each phase of the wave action within the cycle
    STILL_1_S = 2.0
    RAISE_S = 1.0
    WAVE_S = 3.0
    LOWER_S = 1.0
    
    RAISE_START_FRAME = int(STILL_1_S * FPS)
    WAVE_START_FRAME = int((STILL_1_S + RAISE_S) * FPS)
    LOWER_START_FRAME = int((STILL_1_S + RAISE_S + WAVE_S) * FPS)
    LOWER_END_FRAME = int((STILL_1_S + RAISE_S + WAVE_S + LOWER_S) * FPS)

    RAISE_DURATION_FRAMES = int(RAISE_S * FPS)
    WAVE_DURATION_FRAMES = int(WAVE_S * FPS)
    LOWER_DURATION_FRAMES = int(LOWER_S * FPS)

    # --- Setup Pygame Window ---
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Waving Hand")
    clock = pygame.time.Clock()

    frame_count = 0
    running = True

    # --- Main Animation Loop ---
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- Update Animation State ---
        time_s = frame_count / FPS

        # --- Calculate Joint Positions for the Current Frame ---
        
        # 1. Torso and Core Points
        # A subtle, natural sway is added to the figure's core for realism.
        sway_amp_x = 2
        sway_amp_y = 1.5
        sway_freq = 0.4 * math.pi
        
        center_x = SCREEN_WIDTH / 2
        base_y = SCREEN_HEIGHT / 2 + 100

        sacrum_pos = (
            center_x + sway_amp_x * math.sin(time_s * sway_freq),
            base_y + sway_amp_y * math.cos(time_s * sway_freq * 2)
        )
        sternum_pos = (sacrum_pos[0], sacrum_pos[1] - TORSO_LENGTH)
        head_pos = (sternum_pos[0], sternum_pos[1] - HEAD_OFFSET)
        
        l_shoulder_pos = (sternum_pos[0] - SHOULDER_WIDTH / 2, sternum_pos[1])
        r_shoulder_pos = (sternum_pos[0] + SHOULDER_WIDTH / 2, sternum_pos[1])
        
        l_hip_pos = (sacrum_pos[0] - HIP_WIDTH / 2, sacrum_pos[1])
        r_hip_pos = (sacrum_pos[0] + HIP_WIDTH / 2, sacrum_pos[1])

        # Helper function to calculate a limb's endpoint from its start point, length, and angle.
        def get_endpoint(start_pos, length, angle_rad):
            return (
                start_pos[0] + length * math.cos(angle_rad),
                start_pos[1] + length * math.sin(angle_rad)
            )

        # 2. Legs
        # Legs have a subtle counter-sway motion.
        leg_sway_amp = math.radians(2)
        r_thigh_angle = math.radians(90) + leg_sway_amp * math.sin(time_s * sway_freq)
        r_shin_angle = r_thigh_angle - math.radians(4) # Slight natural knee bend
        l_thigh_angle = math.radians(90) + leg_sway_amp * math.sin(time_s * sway_freq + math.pi)
        l_shin_angle = l_thigh_angle - math.radians(4)

        r_knee_pos = get_endpoint(r_hip_pos, THIGH_LENGTH, r_thigh_angle)
        r_ankle_pos = get_endpoint(r_knee_pos, SHIN_LENGTH, r_shin_angle)
        l_knee_pos = get_endpoint(l_hip_pos, THIGH_LENGTH, l_thigh_angle)
        l_ankle_pos = get_endpoint(l_knee_pos, SHIN_LENGTH, l_shin_angle)
        
        # 3. Arms
        # Left arm remains in a natural resting position.
        l_upper_arm_angle = math.radians(100)
        l_forearm_angle = math.radians(95)
        l_elbow_pos = get_endpoint(l_shoulder_pos, UPPER_ARM_LENGTH, l_upper_arm_angle)
        l_wrist_pos = get_endpoint(l_elbow_pos, FOREARM_LENGTH, l_forearm_angle)
        
        # Right arm motion is determined by a state machine based on the frame count.
        # Angles are in degrees (0=right, 90=down, -90=up) and converted to radians for calculation.
        rest_upper_arm_deg = 80
        rest_forearm_deg = 85
        
        r_upper_arm_deg = rest_upper_arm_deg
        r_forearm_deg = rest_forearm_deg

        if RAISE_START_FRAME <= frame_count < WAVE_START_FRAME:
            # Phase 1: Raising the arm smoothly.
            progress = (frame_count - RAISE_START_FRAME) / RAISE_DURATION_FRAMES
            eased_progress = 0.5 - 0.5 * math.cos(progress * math.pi) # Ease-in-out interpolation
            
            raised_upper_arm_deg = -45
            raised_forearm_deg = 0
            
            r_upper_arm_deg = rest_upper_arm_deg + (raised_upper_arm_deg - rest_upper_arm_deg) * eased_progress
            r_forearm_deg = rest_forearm_deg + (raised_forearm_deg - rest_forearm_deg) * eased_progress

        elif WAVE_START_FRAME <= frame_count < LOWER_START_FRAME:
            # Phase 2: Waving the hand.
            r_upper_arm_deg = -45  # Arm remains in the raised position.
            
            wave_progress = (frame_count - WAVE_START_FRAME) / WAVE_DURATION_FRAMES
            # 3 full oscillations (waves) are performed.
            wave_cycle_angle = wave_progress * 3 * (2 * math.pi)
            
            wave_center_forearm_deg = 20
            wave_amp_forearm_deg = 40
            
            r_forearm_deg = wave_center_forearm_deg + wave_amp_forearm_deg * math.sin(wave_cycle_angle)

        elif LOWER_START_FRAME <= frame_count < LOWER_END_FRAME:
            # Phase 3: Lowering the arm smoothly.
            progress = (frame_count - LOWER_START_FRAME) / LOWER_DURATION_FRAMES
            eased_progress = 0.5 - 0.5 * math.cos(progress * math.pi)
            
            raised_upper_arm_deg = -45
            # Start forearm angle from where the wave left off to avoid a visual snap.
            start_forearm_deg = 20 

            r_upper_arm_deg = raised_upper_arm_deg + (rest_upper_arm_deg - raised_upper_arm_deg) * eased_progress
            r_forearm_deg = start_forearm_deg + (rest_forearm_deg - start_forearm_deg) * eased_progress

        r_upper_arm_rad = math.radians(r_upper_arm_deg)
        r_forearm_rad = math.radians(r_forearm_deg)
        
        r_elbow_pos = get_endpoint(r_shoulder_pos, UPPER_ARM_LENGTH, r_upper_arm_rad)
        r_wrist_pos = get_endpoint(r_elbow_pos, FOREARM_LENGTH, r_forearm_rad)

        # --- Collect all 15 points for drawing ---
        # This list defines the complete 15-point figure.
        points = [
            head_pos, sternum_pos, sacrum_pos,
            l_shoulder_pos, r_shoulder_pos,
            l_elbow_pos, r_elbow_pos,
            l_wrist_pos, r_wrist_pos,
            l_hip_pos, r_hip_pos,
            l_knee_pos, r_knee_pos,
            l_ankle_pos, r_ankle_pos
        ]

        # --- Draw Everything to the Screen ---
        screen.fill(BLACK)
        for point in points:
            # Convert float coordinates to integers for drawing.
            int_point = (int(point[0]), int(point[1]))
            pygame.draw.circle(screen, WHITE, int_point, POINT_RADIUS)

        pygame.display.flip()

        # --- Advance to the Next Frame ---
        frame_count = (frame_count + 1) % CYCLE_FRAMES
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
