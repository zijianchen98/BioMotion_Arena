
import pygame
import numpy as np

# --- Constants ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
POINT_RADIUS = 5

# --- Animation Parameters for "Sad/Heavy Walk" ---
# Slower cycle and horizontal speed for a heavy, labored feel
CYCLE_DURATION = 2.8  # seconds per full walking cycle
HORIZONTAL_SPEED = 40 # pixels per second

# Body Proportions & Slumped Posture
# Vertical distances from a higher joint, adjusted for a slumped posture
NECK_LENGTH = 15      # Short neck -> head tucked down
TORSO_LENGTH = 80     # Shorter torso -> slumped/hunched back
PELVIS_WIDTH = 35
SHOULDER_WIDTH = 80
SHOULDER_SLUMP = 15   # How much shoulders are lowered from their neutral position

UPPER_ARM_LENGTH = 65
LOWER_ARM_LENGTH = 60
UPPER_LEG_LENGTH = 85
LOWER_LEG_LENGTH = 75

# Motion Amplitudes & Offsets
# Characterizing the sad/heavy gait
TORSO_BOB_AMP = 6       # Pronounced vertical bobbing for heavy steps
ARM_SWING_AMP = 0.09    # Minimal arm swing
ELBOW_BEND = 0.2        # Slight, limp bend in the elbows

THIGH_SWING_AMP = 0.45  # Stride length (angle of thigh swing)
KNEE_BEND_AMP = 1.0     # How much the knee bends during swing phase (radians)


class BiologicalMotionAnimation:
    """
    Creates a point-light animation of a sad woman with heavy weight walking.
    The animation uses a standard 15-point biomechanical model.
    """
    def __init__(self):
        """
        Initializes Pygame, the display, and animation variables.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Biological Motion: Sad/Heavy Walk")
        self.clock = pygame.time.Clock()
        self.time = 0.0

        # Dictionary to store the 15 points' positions
        self.points = {}

        # Initial position of the walker's core
        self.initial_x = SCREEN_WIDTH + 150  # Start off-screen to the right
        self.base_y = SCREEN_HEIGHT / 2 - 40 # Base vertical position for the pelvis

    def update_points(self, dt):
        """
        Calculates the new position of each of the 15 points for the current frame
        using a forward kinematics model.
        """
        self.time += dt
        
        # Reset animation when the walker is far off-screen to the left
        if self.points.get('head', (self.initial_x, 0))[0] < -150:
            self.time = 0

        # --- Master Clock and Phase ---
        # The phase determines the position in the walking cycle (0 to 2*pi)
        phase = (self.time / CYCLE_DURATION) * 2 * np.pi
        
        # The left side of the body is half a cycle out of phase with the right
        phase_left = phase + np.pi

        # --- Core Body Movement (Torso, Head) ---
        # Overall horizontal movement from right to left
        x_offset = self.initial_x - HORIZONTAL_SPEED * self.time
        
        # Vertical bobbing motion, happens twice per walking cycle
        y_bob = TORSO_BOB_AMP * np.cos(2 * phase)
        
        # Define the three central torso points
        lower_torso_pos = np.array([x_offset, self.base_y + y_bob])
        upper_torso_pos = lower_torso_pos - np.array([0, TORSO_LENGTH])
        head_pos = upper_torso_pos - np.array([0, NECK_LENGTH])
        
        # --- Shoulder and Arm Kinematics ---
        # Shoulders are relative to the upper torso, with a slump
        l_shoulder_pos = upper_torso_pos + np.array([-SHOULDER_WIDTH / 2, SHOULDER_SLUMP])
        r_shoulder_pos = upper_torso_pos + np.array([+SHOULDER_WIDTH / 2, SHOULDER_SLUMP])

        # Arms swing with a very small amplitude, opposite to the legs
        r_upper_arm_angle = ARM_SWING_AMP * np.sin(phase_left)
        l_upper_arm_angle = ARM_SWING_AMP * np.sin(phase)

        # Elbows are positioned relative to shoulders
        r_elbow_pos = r_shoulder_pos + np.array([
            UPPER_ARM_LENGTH * np.sin(r_upper_arm_angle),
            UPPER_ARM_LENGTH * np.cos(r_upper_arm_angle)
        ])
        l_elbow_pos = l_shoulder_pos + np.array([
            UPPER_ARM_LENGTH * np.sin(l_upper_arm_angle),
            UPPER_ARM_LENGTH * np.cos(l_upper_arm_angle)
        ])

        # Wrists are positioned relative to elbows with a slight passive bend
        r_wrist_pos = r_elbow_pos + np.array([
            LOWER_ARM_LENGTH * np.sin(r_upper_arm_angle + ELBOW_BEND),
            LOWER_ARM_LENGTH * np.cos(r_upper_arm_angle + ELBOW_BEND)
        ])
        l_wrist_pos = l_elbow_pos + np.array([
            LOWER_ARM_LENGTH * np.sin(l_upper_arm_angle + ELBOW_BEND),
            LOWER_ARM_LENGTH * np.cos(l_upper_arm_angle + ELBOW_BEND)
        ])

        # --- Hip and Leg Kinematics ---
        # Hips are relative to the lower torso
        l_hip_pos = lower_torso_pos + np.array([-PELVIS_WIDTH / 2, 0])
        r_hip_pos = lower_torso_pos + np.array([+PELVIS_WIDTH / 2, 0])

        # Thighs swing back and forth
        r_thigh_angle = THIGH_SWING_AMP * np.sin(phase)
        l_thigh_angle = THIGH_SWING_AMP * np.sin(phase_left)
        
        # Knees are positioned relative to hips
        r_knee_pos = r_hip_pos + np.array([
            UPPER_LEG_LENGTH * np.sin(r_thigh_angle),
            UPPER_LEG_LENGTH * np.cos(r_thigh_angle)
        ])
        l_knee_pos = l_hip_pos + np.array([
            UPPER_LEG_LENGTH * np.sin(l_thigh_angle),
            UPPER_LEG_LENGTH * np.cos(l_thigh_angle)
        ])
        
        # The knee bends most during the swing phase of the leg
        r_calf_bend = KNEE_BEND_AMP * (np.sin(phase - np.pi / 2) + 1) / 2
        l_calf_bend = KNEE_BEND_AMP * (np.sin(phase_left - np.pi / 2) + 1) / 2

        # Ankles are positioned relative to knees
        r_ankle_pos = r_knee_pos + np.array([
            LOWER_LEG_LENGTH * np.sin(r_thigh_angle + r_calf_bend),
            LOWER_LEG_LENGTH * np.cos(r_thigh_angle + r_calf_bend)
        ])
        l_ankle_pos = l_knee_pos + np.array([
            LOWER_LEG_LENGTH * np.sin(l_thigh_angle + l_calf_bend),
            LOWER_LEG_LENGTH * np.cos(l_thigh_angle + l_calf_bend)
        ])
        
        # --- Store all 15 points for drawing ---
        self.points = {
            'head': head_pos,
            'upper_torso': upper_torso_pos,
            'lower_torso': lower_torso_pos,
            'l_shoulder': l_shoulder_pos,
            'r_shoulder': r_shoulder_pos,
            'l_elbow': l_elbow_pos,
            'r_elbow': r_elbow_pos,
            'l_wrist': l_wrist_pos,
            'r_wrist': r_wrist_pos,
            'l_hip': l_hip_pos,
            'r_hip': r_hip_pos,
            'l_knee': l_knee_pos,
            'r_knee': r_knee_pos,
            'l_ankle': l_ankle_pos,
            'r_ankle': r_ankle_pos
        }


    def draw(self):
        """
        Draws the current frame of the animation, clearing the screen first
        and then drawing each of the 15 points.
        """
        self.screen.fill(BLACK)
        if not self.points:
            return

        for pos in self.points.values():
            pygame.draw.circle(self.screen, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)

        pygame.display.flip()

    def run(self):
        """
        Main animation loop. Handles events, updates state, and draws to the screen.
        """
        running = True
        while running:
            # Get delta time for frame-rate independent movement
            dt = self.clock.tick(FPS) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.update_points(dt)
            self.draw()
            
        pygame.quit()


if __name__ == '__main__':
    animation = BiologicalMotionAnimation()
    animation.run()
