
import pygame
import math

# --- Main Configuration ---
# Screen and Display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5

# Animation Parameters
CYCLE_SPEED = 0.045  # Controls the speed of the walking cycle
CENTER_X = SCREEN_WIDTH // 2
BASE_Y = SCREEN_HEIGHT // 2 + 70  # Base Y position for the figure's hips

# Body Proportions (in pixels)
TORSO_LENGTH = 90
HEAD_OFFSET = 55
SHOULDER_WIDTH = 70
HIP_WIDTH = 50
THIGH_LENGTH = 90
SHIN_LENGTH = 85
UPPER_ARM_LENGTH = 80
LOWER_ARM_LENGTH = 75

# Motion Amplitudes (degrees are converted to radians)
# These values control the "style" of the walk.
VERTICAL_BOB_AMP = 4
LATERAL_SWAY_AMP = 10
THIGH_SWING_AMP = math.radians(45)
KNEE_BEND_AMP = math.radians(80)
ARM_SWING_AMP = math.radians(50)  # Slightly larger arm swing for a "happy" walk
ELBOW_BEND_AMP = math.radians(90)


def main():
    """
    Main function to initialize Pygame and run the animation loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Walking")
    clock = pygame.time.Clock()

    time_angle = 0.0
    running = True

    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- Update State ---
        # Increment the master angle for the animation cycle
        time_angle += CYCLE_SPEED
        # Loop the angle back to 0 after a full cycle (2*pi)
        if time_angle > 2 * math.pi:
            time_angle -= 2 * math.pi

        # --- Calculate Joint Positions ---
        
        # 1. Torso Motion: Vertical Bob and Lateral Sway
        # The body bobs up and down twice per full walking cycle.
        vertical_bob = VERTICAL_BOB_AMP * math.cos(2 * time_angle)
        # The body sways from side to side once per cycle, towards the supporting leg.
        lateral_sway = LATERAL_SWAY_AMP * math.sin(time_angle)
        
        # 2. Core Body Points (15 total)
        # The pelvis is the base, incorporating sway and bob.
        pelvis_center_x = CENTER_X + lateral_sway
        pelvis_center_y = BASE_Y + vertical_bob
        
        # The main torso point is above the pelvis, with reduced sway.
        torso_center_x = CENTER_X + lateral_sway * 0.5
        torso_center_y = pelvis_center_y - TORSO_LENGTH
        
        # The head sits atop the torso.
        head_x = torso_center_x
        head_y = torso_center_y - HEAD_OFFSET

        # Store all points to be drawn
        points = [
            (head_x, head_y),
            (torso_center_x, torso_center_y),
            (pelvis_center_x, pelvis_center_y)
        ]

        # 3. Shoulders and Hips
        # Shoulders and hips are positioned relative to the torso and pelvis.
        right_shoulder_x = torso_center_x + SHOULDER_WIDTH / 2
        left_shoulder_x = torso_center_x - SHOULDER_WIDTH / 2
        shoulder_y = torso_center_y
        
        right_hip_x = pelvis_center_x + HIP_WIDTH / 2
        left_hip_x = pelvis_center_x - HIP_WIDTH / 2
        hip_y = pelvis_center_y
        
        points.extend([
            (right_shoulder_x, shoulder_y), (left_shoulder_x, shoulder_y),
            (right_hip_x, hip_y), (left_hip_x, hip_y)
        ])
        
        # 4. Legs Motion (Right and Left)
        # Using a hierarchical model: Ankle depends on Knee, which depends on Hip.
        # Angles are calculated relative to vertical (0 = down).
        
        # Right Leg (moves in phase with the primary time_angle)
        thigh_angle_r = THIGH_SWING_AMP * math.sin(time_angle)
        # Knee bend is complex; it's greatest during the leg's forward swing.
        knee_bend_r = KNEE_BEND_AMP * (max(0, math.sin(time_angle - math.pi / 2)) ** 2)

        right_knee_x = right_hip_x + THIGH_LENGTH * math.sin(thigh_angle_r)
        right_knee_y = hip_y + THIGH_LENGTH * math.cos(thigh_angle_r)
        
        shin_angle_r = thigh_angle_r - knee_bend_r
        right_ankle_x = right_knee_x + SHIN_LENGTH * math.sin(shin_angle_r)
        right_ankle_y = right_knee_y + SHIN_LENGTH * math.cos(shin_angle_r)

        # Left Leg (moves out of phase by pi radians)
        thigh_angle_l = THIGH_SWING_AMP * math.sin(time_angle + math.pi)
        knee_bend_l = KNEE_BEND_AMP * (max(0, math.sin(time_angle + math.pi / 2)) ** 2)

        left_knee_x = left_hip_x + THIGH_LENGTH * math.sin(thigh_angle_l)
        left_knee_y = hip_y + THIGH_LENGTH * math.cos(thigh_angle_l)

        shin_angle_l = thigh_angle_l - knee_bend_l
        left_ankle_x = left_knee_x + SHIN_LENGTH * math.sin(shin_angle_l)
        left_ankle_y = left_knee_y + SHIN_LENGTH * math.cos(shin_angle_l)
        
        points.extend([
            (right_knee_x, right_knee_y), (left_knee_x, left_knee_y),
            (right_ankle_x, right_ankle_y), (left_ankle_x, left_ankle_y)
        ])
        
        # 5. Arms Motion (Right and Left)
        # Arms swing in opposition to their corresponding legs.
        
        # Right Arm (swings with the left leg, phase +pi)
        upper_arm_angle_r = ARM_SWING_AMP * math.sin(time_angle + math.pi)
        elbow_bend_r = ELBOW_BEND_AMP * (max(0, -math.sin(time_angle + math.pi)) ** 0.5)

        right_elbow_x = right_shoulder_x + UPPER_ARM_LENGTH * math.sin(upper_arm_angle_r)
        right_elbow_y = shoulder_y + UPPER_ARM_LENGTH * math.cos(upper_arm_angle_r)
        
        lower_arm_angle_r = upper_arm_angle_r - elbow_bend_r
        right_wrist_x = right_elbow_x + LOWER_ARM_LENGTH * math.sin(lower_arm_angle_r)
        right_wrist_y = right_elbow_y + LOWER_ARM_LENGTH * math.cos(lower_arm_angle_r)

        # Left Arm (swings with the right leg, in phase)
        upper_arm_angle_l = ARM_SWING_AMP * math.sin(time_angle)
        elbow_bend_l = ELBOW_BEND_AMP * (max(0, -math.sin(time_angle)) ** 0.5)

        left_elbow_x = left_shoulder_x + UPPER_ARM_LENGTH * math.sin(upper_arm_angle_l)
        left_elbow_y = shoulder_y + UPPER_ARM_LENGTH * math.cos(upper_arm_angle_l)

        lower_arm_angle_l = upper_arm_angle_l - elbow_bend_l
        left_wrist_x = left_elbow_x + LOWER_ARM_LENGTH * math.sin(lower_arm_angle_l)
        left_wrist_y = left_elbow_y + LOWER_ARM_LENGTH * math.cos(lower_arm_angle_l)

        points.extend([
            (right_elbow_x, right_elbow_y), (left_elbow_x, left_elbow_y),
            (right_wrist_x, right_wrist_y), (left_wrist_x, left_wrist_y)
        ])

        # --- Drawing ---
        screen.fill(BACKGROUND_COLOR)
        
        # Draw all 15 points
        for point in points:
            pygame.draw.circle(screen, POINT_COLOR, (int(point[0]), int(point[1])), POINT_RADIUS)

        pygame.display.flip()

        # --- Frame Rate Control ---
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
