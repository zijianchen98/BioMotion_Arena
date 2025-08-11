
import pygame
import math

# --- Constants ---
# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WINDOW_CAPTION = "Biological Motion: Sad/Heavy Woman Running"

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# Point-light stimulus properties
POINT_RADIUS = 6

# --- Motion Parameters ---
# These parameters are tuned to create the specific "sad/heavy running" motion.

# Overall cycle speed and characteristics
CYCLE_SPEED = 0.07  # A slower pace for a labored, heavy run.
VERTICAL_BOB = 20   # Increased vertical oscillation to simulate heavy footfalls.
FORWARD_LEAN = 35   # A significant forward lean to represent a slumped, sad, or tired posture.

# Body proportions
TORSO_LENGTH = 120
PELVIS_WIDTH = 60
SHOULDER_WIDTH = 80
HEAD_NECK_LENGTH = 25
HEAD_TILT_DOWN = 15 # An additional downward angle for the head to convey sadness.

# Limb lengths
UPPER_ARM_LENGTH = 65
FOREARM_LENGTH = 70
THIGH_LENGTH = 75
CALF_LENGTH = 80

# Limb swing amplitudes (in radians)
ARM_SWING_AMP = 0.4   # Reduced arm swing, suggesting lethargy or sadness.
THIGH_SWING_AMP = 0.7 # Reduced leg range of motion, characteristic of a non-athletic, heavy run.

# Limb bend properties (in radians)
ELBOW_BASE_BEND = 0.7 # Arms are kept partially bent, not swinging freely.
ELBOW_BEND_AMP = 0.6
KNEE_BASE_BEND = 0.1
KNEE_BEND_AMP = 1.2  # Degree of knee flexion during the swing phase of the run.

def main():
    """
    Initializes pygame and runs the main animation loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_CAPTION)
    clock = pygame.time.Clock()

    time = 0.0
    is_running = True

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        # --- Update Animation State ---
        time += CYCLE_SPEED

        # --- Kinematic Calculations ---
        # Calculate the 15 joint positions for the current frame based on a cyclic time variable.
        # A hierarchical model is used: body center -> torso -> limbs.

        # 1. Core Body Position
        # The entire figure oscillates vertically and is centered with a forward lean.
        center_x = SCREEN_WIDTH / 2
        vertical_offset = VERTICAL_BOB * math.sin(time * 2)
        base_x = center_x - FORWARD_LEAN
        base_y = SCREEN_HEIGHT / 2 - 20 + vertical_offset

        # 2. Torso Points
        # These form the central structure: pelvis, spine, neck, head, shoulders.
        pelvis_center_y = base_y + TORSO_LENGTH / 2
        shoulder_center_y = base_y - TORSO_LENGTH / 2

        # Define the 15 points based on the standard biological motion marker set.
        
        # Point 5: Spine (a central point on the torso)
        spine_pt = (base_x + FORWARD_LEAN * 0.5, base_y)
        
        # Point 2: Neck
        neck_pt = (base_x + FORWARD_LEAN, shoulder_center_y)
        
        # Point 1: Head
        head_pt = (neck_pt[0] + FORWARD_LEAN * 0.2, neck_pt[1] - HEAD_NECK_LENGTH + HEAD_TILT_DOWN)
        
        # Points 3 & 4: Shoulders
        shoulder_sway = 5 * math.cos(time)
        l_shoulder_pt = (neck_pt[0] - SHOULDER_WIDTH / 2 - shoulder_sway, neck_pt[1])
        r_shoulder_pt = (neck_pt[0] + SHOULDER_WIDTH / 2 + shoulder_sway, neck_pt[1])
        
        # Points 6 & 7: Pelvis (Hips)
        hip_rock = 8 * math.sin(time)
        l_pelvis_pt = (base_x - PELVIS_WIDTH / 2, pelvis_center_y - hip_rock)
        r_pelvis_pt = (base_x + PELVIS_WIDTH / 2, pelvis_center_y + hip_rock)

        # 3. Limbs
        # Limbs move in opposition. phase1 drives right leg/left arm, phase2 drives left leg/right arm.
        phase1 = time
        phase2 = time + math.pi

        # Leg Calculations
        thigh_angle_r = THIGH_SWING_AMP * math.sin(phase1)
        knee_angle_r = KNEE_BASE_BEND + KNEE_BEND_AMP * (math.sin(phase1 + math.pi / 2) + 1) / 2
        thigh_angle_l = THIGH_SWING_AMP * math.sin(phase2)
        knee_angle_l = KNEE_BASE_BEND + KNEE_BEND_AMP * (math.sin(phase2 + math.pi / 2) + 1) / 2

        # Points 12 & 13: Knees
        l_knee_pt = (l_pelvis_pt[0] + THIGH_LENGTH * math.sin(thigh_angle_l),
                     l_pelvis_pt[1] + THIGH_LENGTH * math.cos(thigh_angle_l))
        r_knee_pt = (r_pelvis_pt[0] + THIGH_LENGTH * math.sin(thigh_angle_r),
                     r_pelvis_pt[1] + THIGH_LENGTH * math.cos(thigh_angle_r))

        # Points 14 & 15: Ankles
        l_ankle_pt = (l_knee_pt[0] + CALF_LENGTH * math.sin(thigh_angle_l + knee_angle_l),
                      l_knee_pt[1] + CALF_LENGTH * math.cos(thigh_angle_l + knee_angle_l))
        r_ankle_pt = (r_knee_pt[0] + CALF_LENGTH * math.sin(thigh_angle_r + knee_angle_r),
                      r_knee_pt[1] + CALF_LENGTH * math.cos(thigh_angle_r + knee_angle_r))

        # Arm Calculations
        upper_arm_angle_l = ARM_SWING_AMP * math.sin(phase1)
        elbow_angle_l = ELBOW_BASE_BEND + ELBOW_BEND_AMP * (math.sin(phase1 + math.pi) + 1) / 2
        upper_arm_angle_r = ARM_SWING_AMP * math.sin(phase2)
        elbow_angle_r = ELBOW_BASE_BEND + ELBOW_BEND_AMP * (math.sin(phase2 + math.pi) + 1) / 2

        # Points 8 & 9: Elbows
        l_elbow_pt = (l_shoulder_pt[0] + UPPER_ARM_LENGTH * math.sin(upper_arm_angle_l),
                      l_shoulder_pt[1] + UPPER_ARM_LENGTH * math.cos(upper_arm_angle_l))
        r_elbow_pt = (r_shoulder_pt[0] + UPPER_ARM_LENGTH * math.sin(upper_arm_angle_r),
                      r_shoulder_pt[1] + UPPER_ARM_LENGTH * math.cos(upper_arm_angle_r))

        # Points 10 & 11: Wrists
        l_wrist_pt = (l_elbow_pt[0] + FOREARM_LENGTH * math.sin(upper_arm_angle_l + elbow_angle_l),
                      l_elbow_pt[1] + FOREARM_LENGTH * math.cos(upper_arm_angle_l + elbow_angle_l))
        r_wrist_pt = (r_elbow_pt[0] + FOREARM_LENGTH * math.sin(upper_arm_angle_r + elbow_angle_r),
                      r_elbow_pt[1] + FOREARM_LENGTH * math.cos(upper_arm_angle_r + elbow_angle_r))

        # Assemble all 15 points into a single list for drawing.
        points = [
            head_pt, neck_pt, l_shoulder_pt, r_shoulder_pt, spine_pt,
            l_pelvis_pt, r_pelvis_pt, l_elbow_pt, r_elbow_pt, l_wrist_pt,
            r_wrist_pt, l_knee_pt, r_knee_pt, l_ankle_pt, r_ankle_pt
        ]

        # --- Drawing ---
        screen.fill(COLOR_BLACK)
        for point in points:
            pygame.draw.circle(screen, COLOR_WHITE, (int(point[0]), int(point[1])), POINT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
