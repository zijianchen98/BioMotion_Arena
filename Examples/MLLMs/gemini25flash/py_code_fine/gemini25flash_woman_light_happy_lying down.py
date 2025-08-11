
import pygame
import math
import numpy as np

# --- Configuration ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
POINT_RADIUS = 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Human Body Model (Simplified Kinematic Chain) ---
# Define segment lengths as proportions of a normalized figure height.
# These values are arbitrary and tuned for visual plausibility.
SEGMENT_LENGTHS = {
    'head_neck': 0.1,
    'neck_torso': 0.15,
    'torso_hip': 0.1, # Distance from torso center to hip joint
    'shoulder_elbow': 0.15,
    'elbow_wrist': 0.15,
    'hip_knee': 0.25,
    'knee_ankle': 0.25,
    'shoulder_width': 0.08, # Half width from neck/torso center
    'hip_width': 0.08, # Half width from torso center
}

# Mapping of point indices to body parts (15 points as per prompt)
# Based on typical point-light display mapping.
# 0: Head, 1: Neck, 2: Left Shoulder, 3: Right Shoulder,
# 4: Left Elbow, 5: Right Elbow, 6: Left Wrist, 7: Right Wrist,
# 8: Torso (center of chest/upper back), 9: Left Hip, 10: Right Hip,
# 11: Left Knee, 12: Right Knee, 13: Left Ankle, 14: Right Ankle

class HumanFigure:
    def __init__(self, screen_center):
        self.points = np.zeros((15, 2)) # Store (x, y) coordinates for each of the 15 points
        self.screen_center = np.array(screen_center)
        # Scale the figure. A figure height of 1.0 unit will be SCREEN_HEIGHT / 2.5 pixels tall.
        self.scale = SCREEN_HEIGHT / 2.5 

        # Animation state
        self.animation_time = 0.0
        self.animation_duration = 4.0 # seconds for the full lying down motion
        self.is_animating = True

        # --- Define Start and End Joint Angles (in radians) ---
        # Angle convention: 0 degrees is along positive X-axis (right)
        # Positive angles are counter-clockwise.
        # Body segments are rotated from their parent segment's orientation.
        # Example: if Torso is at 0 degrees (horizontal), a straight arm 'down' would be 270 degrees.

        # Start angles (standing upright pose)
        self.start_angles = {
            'torso_rot': 0, # Overall rotation of the main body axis (spine). 0=upright.
            'neck_bend': 0, # Head/neck segment angle relative to torso. 0=straight.
            'l_shoulder_bend': 0, # Upper arm bend relative to body. 0=straight down.
            'r_shoulder_bend': 0,
            'l_elbow_bend': 0, # Forearm bend relative to upper arm. 0=straight.
            'r_elbow_bend': 0,
            'l_hip_bend': 0, # Upper leg bend relative to body. 0=straight down.
            'r_hip_bend': 0,
            'l_knee_bend': 0, # Lower leg bend relative to upper leg. 0=straight.
            'r_knee_bend': 0,
        }

        # End angles (lying down pose, typically on back, head slightly up, limbs relaxed)
        self.end_angles = {
            'torso_rot': math.radians(90), # Body rotated 90 degrees (from upright to horizontal, head to right)
            'neck_bend': math.radians(-10), # Head slightly lifted (bends 'backward' or 'up' when lying)
            'l_shoulder_bend': math.radians(20), # Left arm slightly out/up (relative to person's side)
            'r_shoulder_bend': math.radians(20), # Right arm slightly out/up (symmetric)
            'l_elbow_bend': math.radians(40), # Elbow slightly bent for relaxation
            'r_elbow_bend': math.radians(40),
            'l_hip_bend': math.radians(15), # Hips slightly bent
            'r_hip_bend': math.radians(15),
            'l_knee_bend': math.radians(35), # Knees slightly bent for relaxation
            'r_knee_bend': math.radians(35),
        }
        
        # Current interpolated angles
        self.joint_angles = self.start_angles.copy()

        # Torso (root) position relative to normalized coordinate system (before scaling)
        # Standing: Torso center is higher to place feet near bottom of screen.
        self.start_torso_pos = np.array([0.0, -0.25]) 
        # Lying: Torso center is lower, effectively at ground level.
        self.end_torso_pos = np.array([0.0, 0.15]) 
        self.current_torso_pos = self.start_torso_pos.copy()


    def update(self, dt):
        if not self.is_animating:
            return

        self.animation_time += dt
        t = min(1.0, self.animation_time / self.animation_duration) # Animation progress (0 to 1)

        if t >= 1.0:
            self.is_animating = False

        # Interpolate all joint angles and the root (torso) position
        for angle_name in self.start_angles:
            start_val = self.start_angles[angle_name]
            end_val = self.end_angles[angle_name]
            self.joint_angles[angle_name] = self.lerp(start_val, end_val, t)

        self.current_torso_pos = self.lerp(self.start_torso_pos, self.end_torso_pos, t)

        # --- Forward Kinematics Calculation ---
        # Calculate global positions for all points based on interpolated angles.
        # The 'Torso' point (index 8) is the root of the hierarchy.
        self.points[8] = self.current_torso_pos

        # Define the body's main axis orientation:
        # 0 deg (from +X) means horizontal (lying), 90 deg means vertical (standing upright).
        # torso_rot is the rotation *from* upright.
        current_body_orientation_rad = math.radians(90) - self.joint_angles['torso_rot']

        # 1. Head (0) and Neck (1) - attached to Torso (8) via Neck (1)
        # Neck segment: Torso -> Neck. Its base direction is along the body's main axis.
        neck_segment_vec = self._get_rotated_vector(SEGMENT_LENGTHS['neck_torso'], current_body_orientation_rad)
        self.points[1] = self.points[8] + neck_segment_vec

        # Head segment: Neck -> Head. Its angle is relative to the neck segment's angle.
        head_segment_angle = current_body_orientation_rad + self.joint_angles['neck_bend']
        head_segment_vec = self._get_rotated_vector(SEGMENT_LENGTHS['head_neck'], head_segment_angle)
        self.points[0] = self.points[1] + head_segment_vec

        # 2. Shoulders (2,3) - attached to Neck (1)
        # Shoulders branch perpendicular to the main body axis (90 deg CCW for left, CW for right).
        shoulder_offset_angle_l = current_body_orientation_rad + math.radians(90)
        shoulder_offset_angle_r = current_body_orientation_rad - math.radians(90)
        
        self.points[2] = self.points[1] + self._get_rotated_vector(SEGMENT_LENGTHS['shoulder_width'], shoulder_offset_angle_l)
        self.points[3] = self.points[1] + self._get_rotated_vector(SEGMENT_LENGTHS['shoulder_width'], shoulder_offset_angle_r)

        # 3. Arms (Elbows 4,5; Wrists 6,7) - attached to Shoulders (2,3)
        # Base direction for hanging arms: 180 degrees from body's main axis (i.e., 'down' relative to person).
        arm_base_angle = current_body_orientation_rad - math.radians(180)

        # Left Arm (Shoulder -> Elbow -> Wrist)
        upper_arm_angle_l = arm_base_angle + self.joint_angles['l_shoulder_bend'] # 'l_shoulder_bend' rotates arm CCW from base
        self.points[4] = self.points[2] + self._get_rotated_vector(SEGMENT_LENGTHS['shoulder_elbow'], upper_arm_angle_l)

        forearm_angle_l = upper_arm_angle_l + self.joint_angles['l_elbow_bend'] # 'l_elbow_bend' rotates forearm CCW from upper arm
        self.points[6] = self.points[4] + self._get_rotated_vector(SEGMENT_LENGTHS['elbow_wrist'], forearm_angle_l)

        # Right Arm (Shoulder -> Elbow -> Wrist) - symmetric to left, so reverse bend sign for consistent visual direction
        upper_arm_angle_r = arm_base_angle - self.joint_angles['r_shoulder_bend'] # 'r_shoulder_bend' rotates arm CW from base
        self.points[5] = self.points[3] + self._get_rotated_vector(SEGMENT_LENGTHS['shoulder_elbow'], upper_arm_angle_r)

        forearm_angle_r = upper_arm_angle_r - self.joint_angles['r_elbow_bend'] # 'r_elbow_bend' rotates forearm CW from upper arm
        self.points[7] = self.points[5] + self._get_rotated_vector(SEGMENT_LENGTHS['elbow_wrist'], forearm_angle_r)

        # 4. Hips (9,10) - attached to Torso (8)
        # Hips branch perpendicular to the main body axis (similar to shoulders).
        hip_offset_angle_l = current_body_orientation_rad + math.radians(90)
        hip_offset_angle_r = current_body_orientation_rad - math.radians(90)
        
        self.points[9] = self.points[8] + self._get_rotated_vector(SEGMENT_LENGTHS['hip_width'], hip_offset_angle_l)
        self.points[10] = self.points[8] + self._get_rotated_vector(SEGMENT_LENGTHS['hip_width'], hip_offset_angle_r)

        # 5. Legs (Knees 11,12; Ankles 13,14) - attached to Hips (9,10)
        # Base direction for legs: same as arms, 180 degrees from body's main axis.
        leg_base_angle = current_body_orientation_rad - math.radians(180)

        # Left Leg (Hip -> Knee -> Ankle)
        upper_leg_angle_l = leg_base_angle + self.joint_angles['l_hip_bend'] # 'l_hip_bend' rotates leg CCW from base
        self.points[11] = self.points[9] + self._get_rotated_vector(SEGMENT_LENGTHS['hip_knee'], upper_leg_angle_l)

        lower_leg_angle_l = upper_leg_angle_l + self.joint_angles['l_knee_bend'] # 'l_knee_bend' rotates lower leg CCW from upper leg
        self.points[13] = self.points[11] + self._get_rotated_vector(SEGMENT_LENGTHS['knee_ankle'], lower_leg_angle_l)

        # Right Leg (Hip -> Knee -> Ankle) - symmetric to left
        upper_leg_angle_r = leg_base_angle - self.joint_angles['r_hip_bend'] # 'r_hip_bend' rotates leg CW from base
        self.points[12] = self.points[10] + self._get_rotated_vector(SEGMENT_LENGTHS['hip_knee'], upper_leg_angle_r)

        lower_leg_angle_r = upper_leg_angle_r - self.joint_angles['r_knee_bend'] # 'r_knee_bend' rotates lower leg CW from upper leg
        self.points[14] = self.points[12] + self._get_rotated_vector(SEGMENT_LENGTHS['knee_ankle'], lower_leg_angle_r)


    def _get_rotated_vector(self, length, angle_rad):
        """
        Calculates a 2D vector (x, y) given a length and an angle.
        Angle is measured counter-clockwise from the positive X-axis.
        """
        return np.array([length * math.cos(angle_rad), length * math.sin(angle_rad)])

    def lerp(self, start, end, t):
        """
        Linear interpolation between start and end values based on progress t (0 to 1).
        """
        return start + (end - start) * t

    def get_display_points(self):
        """
        Transforms normalized point coordinates to screen pixel coordinates.
        """
        display_points = (self.points * self.scale) + self.screen_center
        return display_points.astype(int)

    def draw(self, screen):
        """
        Draws the 15 point-lights on the screen.
        """
        display_points = self.get_display_points()
        for point in display_points:
            pygame.draw.circle(screen, WHITE, point, POINT_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Lying Down")
    clock = pygame.time.Clock()

    screen_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    figure = HumanFigure(screen_center)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: # Press 'R' to restart animation
                    figure = HumanFigure(screen_center)

        dt = clock.tick(FPS) / 1000.0 # Time since last frame in seconds
        figure.update(dt)

        screen.fill(BLACK) # Solid black background
        figure.draw(screen)
        pygame.display.flip() # Update the full display Surface to the screen

    pygame.quit()

if __name__ == "__main__":
    main()
