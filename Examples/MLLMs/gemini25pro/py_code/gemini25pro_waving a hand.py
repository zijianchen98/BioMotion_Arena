
import pygame
import math

def main():
    """
    Main function to set up and run the Pygame animation of a point-light
    figure waving a hand.
    """
    # --- Setup ---
    pygame.init()

    # Screen dimensions and properties
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 700
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FPS = 60
    POINT_RADIUS = 6

    # Biomechanically plausible body proportions in pixels
    HEAD_NECK_LEN = 45
    NECK_PELVIS_LEN = 120
    SHOULDER_NECK_DIST = 50
    HIP_PELVIS_DIST = 40
    UPPER_ARM_LEN = 70
    FOREARM_LEN = 65
    UPPER_LEG_LEN = 90
    LOWER_LEG_LEN = 85

    # Initialize screen and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Waving Hand")
    clock = pygame.time.Clock()

    time_step = 0
    running = True

    # --- Animation Loop ---
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Kinematic Calculations for 15 points ---
        
        # Base of the figure with a subtle vertical sway for naturalism
        center_x = SCREEN_WIDTH // 2
        base_y = SCREEN_HEIGHT // 2 - 50
        pelvis_y = base_y + 3 * math.sin(time_step * 0.04)

        # 1. Torso points (Pelvis, Neck, Head)
        pelvis_pos = (center_x, pelvis_y)
        neck_pos = (center_x, pelvis_y - NECK_PELVIS_LEN)
        head_pos = (neck_pos[0], neck_pos[1] - HEAD_NECK_LEN)

        # 2. Shoulder and Hip anchor points
        r_shoulder_pos = (neck_pos[0] + SHOULDER_NECK_DIST, neck_pos[1])
        l_shoulder_pos = (neck_pos[0] - SHOULDER_NECK_DIST, neck_pos[1])
        r_hip_pos = (pelvis_pos[0] + HIP_PELVIS_DIST, pelvis_pos[1])
        l_hip_pos = (pelvis_pos[0] - HIP_PELVIS_DIST, pelvis_pos[1])
        
        # 3. Legs (standing relatively still with a slight knee bend)
        l_knee_pos = (l_hip_pos[0] + 5, l_hip_pos[1] + UPPER_LEG_LEN)
        l_ankle_pos = (l_knee_pos[0] - 5, l_knee_pos[1] + LOWER_LEG_LEN)
        r_knee_pos = (r_hip_pos[0] - 5, r_hip_pos[1] + UPPER_LEG_LEN)
        r_ankle_pos = (r_knee_pos[0] + 5, r_knee_pos[1] + LOWER_LEG_LEN)

        # 4. Left Arm (resting naturally at the side)
        l_elbow_pos = (l_shoulder_pos[0] - 10, l_shoulder_pos[1] + UPPER_ARM_LEN)
        l_wrist_pos = (l_elbow_pos[0], l_elbow_pos[1] + FOREARM_LEN)
        
        # 5. Right Arm (performing the waving motion)
        wave_speed = 0.08
        
        # The upper arm is raised and has a slight bobbing motion
        shoulder_bob_angle = 0.15 * math.sin(time_step * wave_speed + math.pi)
        r_shoulder_angle = -math.pi / 2.2 + shoulder_bob_angle
        
        r_elbow_pos_x = r_shoulder_pos[0] + math.cos(r_shoulder_angle) * UPPER_ARM_LEN
        r_elbow_pos_y = r_shoulder_pos[1] + math.sin(r_shoulder_angle) * UPPER_ARM_LEN
        r_elbow_pos = (r_elbow_pos_x, r_elbow_pos_y)

        # The forearm rotates around the elbow to create the wave
        wave_amplitude = math.pi / 3.0
        # The wave oscillates around an angle perpendicular to the upper arm
        forearm_base_angle = r_shoulder_angle + math.pi / 2.0
        forearm_angle = forearm_base_angle + wave_amplitude * math.sin(time_step * wave_speed)

        r_wrist_pos_x = r_elbow_pos[0] + math.cos(forearm_angle) * FOREARM_LEN
        r_wrist_pos_y = r_elbow_pos[1] + math.sin(forearm_angle) * FOREARM_LEN
        r_wrist_pos = (r_wrist_pos_x, r_wrist_pos_y)
        
        # Compile the list of all 15 points for drawing
        points = [
            head_pos, neck_pos, pelvis_pos,
            l_shoulder_pos, r_shoulder_pos,
            l_hip_pos, r_hip_pos,
            l_elbow_pos, r_elbow_pos,
            l_wrist_pos, r_wrist_pos,
            l_knee_pos, r_knee_pos,
            l_ankle_pos, r_ankle_pos
        ]

        # --- Drawing ---
        screen.fill(BLACK)
        for p in points:
            # Convert float coordinates to integers for drawing on screen
            pygame.draw.circle(screen, WHITE, (int(p[0]), int(p[1])), POINT_RADIUS)

        pygame.display.flip()

        time_step += 1
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
