
import pygame
import math

class BiologicalMotionAnimator:
    """
    Creates a point-light stimulus animation of a person running.
    The animation is designed to depict a 'happyman with heavy weight is running'.
    This is interpreted as an energetic, powerful, yet labored running motion.
    The stimulus consists of 15 white points on a black background.
    """

    def __init__(self):
        """Initializes Pygame, the display window, and animation parameters."""
        pygame.init()
        # Screen and display setup
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Biological Motion: Heavy Running")
        
        # Animation control
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.time_angle = 0.0

        # --- Body Proportions (in pixels) ---
        self.torso_length = 65
        self.head_offset = 20  # Distance from sternum to head point
        self.shoulder_width = 55
        self.hip_width = 45
        self.upper_arm_length = 50
        self.forearm_length = 55
        self.thigh_length = 65
        self.shin_length = 60

        # --- Motion Style Parameters ---
        # These values are tuned to create the impression of a heavy, effortful, yet energetic run.
        self.forward_lean = math.radians(20)          # Simulates effort/weight
        self.vertical_bounce_amp = 12                 # Energetic, "happy" bounce
        self.stride_angle_amp = math.radians(45)      # A strong but not sprinting stride
        self.knee_bend_amp = math.radians(90)         # High knee lift for running
        self.arm_swing_amp = math.radians(65)         # Vigorous arm swing for balance and power
        self.elbow_bend_amp = math.radians(100)       # Arms are bent, typical for running
        self.animation_speed = 0.09                   # A brisk running pace
        
        # --- Visual Style ---
        self.dot_radius = 6
        self.dot_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)
        self.fps = 60

    def _calculate_joint_positions(self, t):
        """
        Calculates the 2D coordinates of 15 body joints for a given time angle t.
        The motion is cyclic, driven by sine and cosine functions.
        This forms a hierarchical kinematic model starting from the pelvis.
        
        Args:
            t (float): The current time angle in the animation cycle (0 to 2*pi).
        
        Returns:
            list: A list of (x, y) tuples for the 15 joints to be rendered.
        """
        points = {}

        # 1. Torso Motion: Establishes the core body's position and orientation.
        center_x = self.width / 2
        base_y = self.height / 2 + 60
        vertical_offset = self.vertical_bounce_amp * math.sin(2 * t)
        
        points['pelvis'] = (center_x, base_y + vertical_offset)
        points['sternum'] = (
            points['pelvis'][0] - self.torso_length * math.sin(self.forward_lean),
            points['pelvis'][1] - self.torso_length * math.cos(self.forward_lean)
        )

        # 2. Limb Anchor Points: Hips and Shoulders, attached to the torso.
        points['r_hip'] = (points['pelvis'][0] + (self.hip_width / 2) * math.cos(self.forward_lean), points['pelvis'][1] + (self.hip_width / 2) * math.sin(self.forward_lean))
        points['l_hip'] = (points['pelvis'][0] - (self.hip_width / 2) * math.cos(self.forward_lean), points['pelvis'][1] - (self.hip_width / 2) * math.sin(self.forward_lean))
        points['r_shoulder'] = (points['sternum'][0] + (self.shoulder_width / 2) * math.cos(self.forward_lean), points['sternum'][1] + (self.shoulder_width / 2) * math.sin(self.forward_lean))
        points['l_shoulder'] = (points['sternum'][0] - (self.shoulder_width / 2) * math.cos(self.forward_lean), points['sternum'][1] - (self.shoulder_width / 2) * math.sin(self.forward_lean))

        # 3. Leg Kinematics: Legs move in opposition (180-degree phase difference).
        knee_phase = -math.pi * 0.4
        
        # Right Leg
        r_thigh_angle = self.forward_lean + self.stride_angle_amp * math.cos(t)
        points['r_knee'] = (points['r_hip'][0] + self.thigh_length * math.sin(r_thigh_angle), points['r_hip'][1] + self.thigh_length * math.cos(r_thigh_angle))
        r_knee_bend = (self.knee_bend_amp / 2) * (1 + math.cos(t + knee_phase))
        r_shin_angle = r_thigh_angle - r_knee_bend
        points['r_ankle'] = (points['r_knee'][0] + self.shin_length * math.sin(r_shin_angle), points['r_knee'][1] + self.shin_length * math.cos(r_shin_angle))

        # Left Leg
        l_thigh_angle = self.forward_lean + self.stride_angle_amp * math.cos(t + math.pi)
        points['l_knee'] = (points['l_hip'][0] + self.thigh_length * math.sin(l_thigh_angle), points['l_hip'][1] + self.thigh_length * math.cos(l_thigh_angle))
        l_knee_bend = (self.knee_bend_amp / 2) * (1 + math.cos(t + math.pi + knee_phase))
        l_shin_angle = l_thigh_angle - l_knee_bend
        points['l_ankle'] = (points['l_knee'][0] + self.shin_length * math.sin(l_shin_angle), points['l_knee'][1] + self.shin_length * math.cos(l_shin_angle))

        # 4. Arm Kinematics: Arms swing opposite to their corresponding legs.
        elbow_phase = -math.pi * 0.1

        # Left Arm (moves in phase with Right Leg)
        l_arm_angle = self.forward_lean + self.arm_swing_amp * math.cos(t)
        points['l_elbow'] = (points['l_shoulder'][0] + self.upper_arm_length * math.sin(l_arm_angle), points['l_shoulder'][1] + self.upper_arm_length * math.cos(l_arm_angle))
        l_elbow_bend = (self.elbow_bend_amp / 2) * (1 - math.sin(t + elbow_phase))
        l_forearm_angle = l_arm_angle + l_elbow_bend
        points['l_wrist'] = (points['l_elbow'][0] + self.forearm_length * math.sin(l_forearm_angle), points['l_elbow'][1] + self.forearm_length * math.cos(l_forearm_angle))
        
        # Right Arm (moves in phase with Left Leg)
        r_arm_angle = self.forward_lean + self.arm_swing_amp * math.cos(t + math.pi)
        points['r_elbow'] = (points['r_shoulder'][0] + self.upper_arm_length * math.sin(r_arm_angle), points['r_shoulder'][1] + self.upper_arm_length * math.cos(r_arm_angle))
        r_elbow_bend = (self.elbow_bend_amp / 2) * (1 - math.sin(t + math.pi + elbow_phase))
        r_forearm_angle = r_arm_angle + r_elbow_bend
        points['r_wrist'] = (points['r_elbow'][0] + self.forearm_length * math.sin(r_forearm_angle), points['r_elbow'][1] + self.forearm_length * math.cos(r_forearm_angle))

        # 5. Head: Attached to the sternum.
        points['head'] = (points['sternum'][0] - self.head_offset * math.sin(self.forward_lean), points['sternum'][1] - self.head_offset * math.cos(self.forward_lean))
        
        # The 15 points are: head, sternum, pelvis, 2x shoulder, 2x hip, 2x elbow, 2x wrist, 2x knee, 2x ankle.
        return list(points.values())

    def start_animation(self):
        """The main animation loop."""
        while self.is_running:
            # Event handling (to close the window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                   (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.is_running = False

            # Update animation state by advancing the time angle
            self.time_angle = (self.time_angle + self.animation_speed) % (2 * math.pi)
            joint_positions = self._calculate_joint_positions(self.time_angle)

            # Draw the current frame
            self.screen.fill(self.bg_color)
            for pos in joint_positions:
                pygame.draw.circle(self.screen, self.dot_color, (int(pos[0]), int(pos[1])), self.dot_radius)
            
            # Refresh the display
            pygame.display.flip()
            self.clock.tick(self.fps)

        pygame.quit()

if __name__ == '__main__':
    animator = BiologicalMotionAnimator()
    animator.start_animation()
