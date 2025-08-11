
import pygame
import math
import random

def main():
    """
    Main function to run the point-light stimulus animation.
    This program displays an animation of a sad man with a heavy weight bowing.
    The animation consists of 15 white points on a black background,
    simulating biological motion in a biomechanically plausible way.
    """
    # --- Pygame Initialization ---
    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Bowing")
    clock = pygame.time.Clock()

    # --- Constants ---
    FPS = 60
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    DOT_RADIUS = 7

    # --- Animation Parameters ---
    ANIMATION_DURATION_SECONDS = 6.0
    TOTAL_FRAMES = int(ANIMATION_DURATION_SECONDS * FPS)
    
    # Timeline percentages for the animation cycle
    DOWN_PHASE_END = 0.40
    DOWN_HOLD_END = 0.55
    UP_PHASE_END = 0.95
    # The remaining time (0.95 to 1.0) is a hold at the top

    # --- Skeletal Parameters (in pixels) ---
    # These define the proportions of the figure.
    SPINE_LENGTH = 170
    NECK_LENGTH = 35
    UPPER_ARM_LENGTH = 110
    LOWER_ARM_LENGTH = 100
    UPPER_LEG_LENGTH = 130
    LOWER_LEG_LENGTH = 120
    SHOULDER_WIDTH = 120
    HIP_WIDTH = 90

    # --- Posture and Motion Angles (in radians) ---
    # Initial "sad/heavy" posture
    INITIAL_SPINE_BEND = math.radians(20)
    INITIAL_KNEE_BEND = math.radians(25)
    INITIAL_HEAD_DROOP = math.radians(30) # Relative to torso

    # Parameters for the bowing motion
    MAX_SPINE_BEND = math.radians(90)
    MAX_KNEE_BEND_ADD = math.radians(20) # Extra bend at the bottom of the bow

    # Parameters for secondary motion (to convey weight and sadness)
    BOB_AMPLITUDE = 3
    BOB_FREQUENCY = 2 # Number of bobs per full cycle
    TREMOR_AMPLITUDE = 0.8

    def ease_in_out_sine(t):
        """Easing function for smooth acceleration and deceleration."""
        return -(math.cos(math.pi * t) - 1) / 2

    # --- Main Loop ---
    frame_count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- UPDATE ---
        
        # Calculate current progress in the animation cycle (0.0 to 1.0)
        progress = (frame_count / TOTAL_FRAMES)

        # Determine current primary angles based on the animation phase
        spine_bend = INITIAL_SPINE_BEND
        knee_bend = INITIAL_KNEE_BEND

        if 0 <= progress < DOWN_PHASE_END:
            # Phase 1: Bowing down
            phase_progress = progress / DOWN_PHASE_END
            eased_progress = ease_in_out_sine(phase_progress)
            spine_bend = INITIAL_SPINE_BEND + eased_progress * (MAX_SPINE_BEND - INITIAL_SPINE_BEND)
            knee_bend = INITIAL_KNEE_BEND + eased_progress * MAX_KNEE_BEND_ADD
        elif DOWN_PHASE_END <= progress < DOWN_HOLD_END:
            # Phase 2: Holding at the bottom
            spine_bend = MAX_SPINE_BEND
            knee_bend = INITIAL_KNEE_BEND + MAX_KNEE_BEND_ADD
        elif DOWN_HOLD_END <= progress < UP_PHASE_END:
            # Phase 3: Rising up
            phase_progress = (progress - DOWN_HOLD_END) / (UP_PHASE_END - DOWN_HOLD_END)
            eased_progress = ease_in_out_sine(phase_progress)
            spine_bend = MAX_SPINE_BEND - eased_progress * (MAX_SPINE_BEND - INITIAL_SPINE_BEND)
            knee_bend = (INITIAL_KNEE_BEND + MAX_KNEE_BEND_ADD) - eased_progress * MAX_KNEE_BEND_ADD
        else: # UP_PHASE_END <= progress < 1.0
            # Phase 4: Holding at the top (initial slumped pose)
            spine_bend = INITIAL_SPINE_BEND
            knee_bend = INITIAL_KNEE_BEND

        # --- Kinematic Calculations ---
        # Calculate the (x, y) coordinates of all 15 joints for the current frame.
        # The origin of the figure is centered horizontally and placed in the lower half of the screen.
        center_x = SCREEN_WIDTH / 2
        base_y = SCREEN_HEIGHT * 0.75
        
        # Add vertical bobbing to simulate strain
        vertical_offset = BOB_AMPLITUDE * math.sin(progress * BOB_FREQUENCY * 2 * math.pi)

        # 1. Sacral (Pelvis/Root): The root of the skeleton
        p_sacral = (center_x, base_y + vertical_offset)

        # 2. Sternum (Upper Torso): Positioned relative to the sacral point based on spine bend
        p_sternum = (
            p_sacral[0] + SPINE_LENGTH * math.sin(spine_bend),
            p_sacral[1] - SPINE_LENGTH * math.cos(spine_bend)
        )

        # 3. Head: Positioned relative to the sternum, with an additional droop
        head_angle = spine_bend + INITIAL_HEAD_DROOP
        p_head = (
            p_sternum[0] + NECK_LENGTH * math.sin(head_angle),
            p_sternum[1] - NECK_LENGTH * math.cos(head_angle)
        )

        # 4, 5. Shoulders: Positioned on a line perpendicular to the spine
        shoulder_perp_angle = spine_bend + math.pi / 2
        p_l_shoulder = (
            p_sternum[0] + (SHOULDER_WIDTH / 2) * math.cos(shoulder_perp_angle),
            p_sternum[1] - (SHOULDER_WIDTH / 2) * math.sin(shoulder_perp_angle)
        )
        p_r_shoulder = (
            p_sternum[0] - (SHOULDER_WIDTH / 2) * math.cos(shoulder_perp_angle),
            p_sternum[1] + (SHOULDER_WIDTH / 2) * math.sin(shoulder_perp_angle)
        )
        
        # Arms (6-9): Hang loosely, influenced by the spine's bend
        arm_hang_angle = spine_bend + math.radians(10) # Base angle
        forearm_hang_angle = arm_hang_angle + math.radians(20) # Slight elbow bend

        p_l_elbow = (p_l_shoulder[0] + UPPER_ARM_LENGTH * math.sin(arm_hang_angle), p_l_shoulder[1] + UPPER_ARM_LENGTH * math.cos(arm_hang_angle))
        p_l_wrist = (p_l_elbow[0] + LOWER_ARM_LENGTH * math.sin(forearm_hang_angle), p_l_elbow[1] + LOWER_ARM_LENGTH * math.cos(forearm_hang_angle))
        
        p_r_elbow = (p_r_shoulder[0] + UPPER_ARM_LENGTH * math.sin(arm_hang_angle), p_r_shoulder[1] + UPPER_ARM_LENGTH * math.cos(arm_hang_angle))
        p_r_wrist = (p_r_elbow[0] + LOWER_ARM_LENGTH * math.sin(forearm_hang_angle), p_r_elbow[1] + LOWER_ARM_LENGTH * math.cos(forearm_hang_angle))

        # 10, 11. Hips: Positioned horizontally relative to the sacral point
        p_l_hip = (p_sacral[0] - HIP_WIDTH / 2, p_sacral[1])
        p_r_hip = (p_sacral[0] + HIP_WIDTH / 2, p_sacral[1])

        # Legs (12-15): Bent to support the weight and movement
        shin_angle_from_vertical = -math.radians(5) # Shins are kept almost vertical

        p_l_knee = (p_l_hip[0] + UPPER_LEG_LENGTH * math.sin(knee_bend), p_l_hip[1] + UPPER_LEG_LENGTH * math.cos(knee_bend))
        p_l_ankle = (p_l_knee[0] + LOWER_LEG_LENGTH * math.sin(shin_angle_from_vertical), p_l_knee[1] + LOWER_LEG_LENGTH * math.cos(shin_angle_from_vertical))

        p_r_knee = (p_r_hip[0] + UPPER_LEG_LENGTH * math.sin(knee_bend), p_r_hip[1] + UPPER_LEG_LENGTH * math.cos(knee_bend))
        p_r_ankle = (p_r_knee[0] + LOWER_LEG_LENGTH * math.sin(shin_angle_from_vertical), p_r_knee[1] + LOWER_LEG_LENGTH * math.cos(shin_angle_from_vertical))

        # Compile the list of all 15 points
        all_points = [
            p_head, p_sternum, p_sacral,
            p_l_shoulder, p_r_shoulder,
            p_l_elbow, p_r_elbow,
            p_l_wrist, p_r_wrist,
            p_l_hip, p_r_hip,
            p_l_knee, p_r_knee,
            p_l_ankle, p_r_ankle
        ]

        # Add a subtle tremor to all points to simulate strain
        def tremor(p):
            return (p[0] + random.uniform(-TREMOR_AMPLITUDE, TREMOR_AMPLITUDE),
                    p[1] + random.uniform(-TREMOR_AMPLITUDE, TREMOR_AMPLITUDE))
        
        final_points = [tremor(p) for p in all_points]

        # --- DRAW ---
        screen.fill(BLACK)
        for point in final_points:
            pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), DOT_RADIUS)
        
        pygame.display.flip()

        # --- Tick ---
        frame_count = (frame_count + 1) % TOTAL_FRAMES
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
