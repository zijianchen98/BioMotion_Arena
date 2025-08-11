
import pygame
import math

def main():
    """
    Main function to run the biological motion animation of a sad, heavy person running.
    """
    # --- Pygame Initialization ---
    pygame.init()

    # --- Constants ---

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Heavy Run")

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Animation parameters
    FPS = 60
    POINT_RADIUS = 6
    # Slower speed for a heavier, sadder motion
    ANIMATION_SPEED = 0.04

    # --- Biomechanical Parameters for "Sad, Heavy Run" ---

    # Base position (center of the animation)
    CENTER_X = WIDTH // 2
    CENTER_Y = HEIGHT // 2 + 80  # Lower center of gravity for a heavy look

    # Body segment lengths
    TORSO_LENGTH = 110
    HEAD_NECK_LENGTH = 45
    UPPER_ARM_LENGTH = 65
    LOWER_ARM_LENGTH = 60
    THIGH_LENGTH = 75
    SHIN_LENGTH = 70
    SHOULDER_WIDTH = 55
    HIP_WIDTH = 45

    # Posture parameters reflecting sadness and weight
    FORWARD_LEAN = 35       # Significant forward hunch
    HEAD_TILT = 20          # Head hanging down

    # Motion dynamics for a heavy, lumbering run
    VERTICAL_BOB_AMP = 6    # Small, heavy vertical steps
    LEG_SWING_AMP = 0.45    # Radians, restricted leg swing
    ARM_SWING_AMP = 0.25    # Radians, very limited arm swing
    KNEE_BEND_OFFSET = 0.8  # Base knee bend, never straightens
    ELBOW_BEND_OFFSET = 1.0 # Base elbow bend, arms held close
    KNEE_BEND_AMP = 0.9      # Additional bend during stride
    ELBOW_BEND_AMP = 0.6    # Additional bend for arm swing

    # --- Main Loop ---
    clock = pygame.time.Clock()
    running = True
    time_step = 0

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- Update Animation State ---
        time_step += 1
        angle = time_step * ANIMATION_SPEED

        # --- Calculate Joint Positions ---

        # 1. Torso Calculation
        # Vertical bobbing motion for the pelvis
        pelvis_y_offset = VERTICAL_BOB_AMP * (math.cos(angle * 2) - 1)
        pelvis_pos = (CENTER_X, CENTER_Y + pelvis_y_offset)

        # Slumped posture: neck is forward of the pelvis
        neck_pos = (pelvis_pos[0] - FORWARD_LEAN, pelvis_pos[1] - TORSO_LENGTH)

        # Sad posture: head is tilted down
        head_pos = (neck_pos[0] - HEAD_TILT, neck_pos[1] - HEAD_NECK_LENGTH)

        # 2. Limb Swing Modifiers
        # Right leg and left arm move together; left leg and right arm move together
        right_leg_mod = math.cos(angle)
        left_leg_mod = math.cos(angle + math.pi)
        right_arm_mod = left_leg_mod
        left_arm_mod = right_leg_mod

        # 3. Leg Calculations
        # Right Leg
        r_hip_pos = (pelvis_pos[0] + HIP_WIDTH / 2, pelvis_pos[1])
        r_hip_angle = math.pi / 2 + LEG_SWING_AMP * right_leg_mod
        r_knee_bend = KNEE_BEND_AMP * (1 - right_leg_mod) / 2
        r_knee_angle = r_hip_angle + KNEE_BEND_OFFSET + r_knee_bend
        r_knee_pos = (
            r_hip_pos[0] + THIGH_LENGTH * math.cos(r_hip_angle),
            r_hip_pos[1] + THIGH_LENGTH * math.sin(r_hip_angle)
        )
        r_ankle_pos = (
            r_knee_pos[0] + SHIN_LENGTH * math.cos(r_knee_angle),
            r_knee_pos[1] + SHIN_LENGTH * math.sin(r_knee_angle)
        )

        # Left Leg
        l_hip_pos = (pelvis_pos[0] - HIP_WIDTH / 2, pelvis_pos[1])
        l_hip_angle = math.pi / 2 + LEG_SWING_AMP * left_leg_mod
        l_knee_bend = KNEE_BEND_AMP * (1 - left_leg_mod) / 2
        l_knee_angle = l_hip_angle + KNEE_BEND_OFFSET + l_knee_bend
        l_knee_pos = (
            l_hip_pos[0] + THIGH_LENGTH * math.cos(l_hip_angle),
            l_hip_pos[1] + THIGH_LENGTH * math.sin(l_hip_angle)
        )
        l_ankle_pos = (
            l_knee_pos[0] + SHIN_LENGTH * math.cos(l_knee_angle),
            l_knee_pos[1] + SHIN_LENGTH * math.sin(l_knee_angle)
        )

        # 4. Arm Calculations
        # Right Arm
        r_shoulder_pos = (neck_pos[0] + SHOULDER_WIDTH / 2, neck_pos[1])
        r_shoulder_angle = math.pi / 2 + ARM_SWING_AMP * right_arm_mod
        r_elbow_bend = ELBOW_BEND_AMP * (1 + right_arm_mod) / 2
        r_elbow_angle = r_shoulder_angle + ELBOW_BEND_OFFSET + r_elbow_bend
        r_elbow_pos = (
            r_shoulder_pos[0] + UPPER_ARM_LENGTH * math.cos(r_shoulder_angle),
            r_shoulder_pos[1] + UPPER_ARM_LENGTH * math.sin(r_shoulder_angle)
        )
        r_wrist_pos = (
            r_elbow_pos[0] + LOWER_ARM_LENGTH * math.cos(r_elbow_angle),
            r_elbow_pos[1] + LOWER_ARM_LENGTH * math.sin(r_elbow_angle)
        )

        # Left Arm
        l_shoulder_pos = (neck_pos[0] - SHOULDER_WIDTH / 2, neck_pos[1])
        l_shoulder_angle = math.pi / 2 + ARM_SWING_AMP * left_arm_mod
        l_elbow_bend = ELBOW_BEND_AMP * (1 + left_arm_mod) / 2
        l_elbow_angle = l_shoulder_angle + ELBOW_BEND_OFFSET + l_elbow_bend
        l_elbow_pos = (
            l_shoulder_pos[0] + UPPER_ARM_LENGTH * math.cos(l_shoulder_angle),
            l_shoulder_pos[1] + UPPER_ARM_LENGTH * math.sin(l_shoulder_angle)
        )
        l_wrist_pos = (
            l_elbow_pos[0] + LOWER_ARM_LENGTH * math.cos(l_elbow_angle),
            l_elbow_pos[1] + LOWER_ARM_LENGTH * math.sin(l_elbow_angle)
        )

        # 5. Collect all 15 points
        torso_points = [head_pos, neck_pos, pelvis_pos]
        arm_points = [l_shoulder_pos, r_shoulder_pos, l_elbow_pos, r_elbow_pos, l_wrist_pos, r_wrist_pos]
        leg_points = [l_hip_pos, r_hip_pos, l_knee_pos, r_knee_pos, l_ankle_pos, r_ankle_pos]
        points = torso_points + arm_points + leg_points

        # --- Drawing ---
        screen.fill(BLACK)
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), POINT_RADIUS)

        pygame.display.flip()

        # Control the frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
