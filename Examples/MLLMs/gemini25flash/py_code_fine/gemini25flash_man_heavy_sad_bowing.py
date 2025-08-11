
import pygame
import math
import numpy as np

# --- Configuration ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
POINT_RADIUS = 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30
ANIMATION_DURATION_SECONDS = 8 # Total time for one full bow cycle (down, hold, up)

# --- Biomechanical Model Parameters ---
# These lengths are relative units, scaled later to screen pixels.
# They define the proportions of the human figure.
NECK_HEAD_LEN = 20
NECK_UPPER_TORSO_LEN = 30
UPPER_TORSO_LOWER_TORSO_LEN = 60 # Length from chest to pelvis center
PELVIS_HIP_LATERAL_OFFSET = 30 # X distance from pelvis center to hip joint (lateral spread)
HIP_THIGH_LEN = 90
THIGH_SHIN_LEN = 80 # Length from knee to foot center (effectively combined shin and foot)
SHOULDER_LATERAL_OFFSET = 40 # X distance from upper torso center to shoulder joint (shoulder width)
SHOULDER_UPPER_ARM_LEN = 70
UPPER_ARM_FOREARM_LEN = 60

# Initial static pose angles (degrees)
# These define the starting "upright" posture.
# Angles are relative to the parent segment or global vertical/horizontal.
INITIAL_TORSO_ANGLE = 0 # Torso vertical (0 = upright)
INITIAL_HEAD_NECK_ANGLE = 0 # Head aligned with neck
INITIAL_KNEE_ANGLE = 5 # Slight initial knee bend (deviation from straight, 0=straight)
INITIAL_SHOULDER_ANGLE = 15 # Arms slightly forward from vertical (hanging slightly forward)
INITIAL_ELBOW_ANGLE = 160 # Slight bend at elbow (180 = straight)

# Animation specific parameters
MAX_TORSO_BEND_ANGLE = 75 # Max forward bend of torso from vertical (degrees). Deeper for "heavy weight".
MAX_KNEE_BEND_ANGLE = 25 # Max knee bend (degrees). More bend for "heavy weight" / "sadman".
MAX_ARM_SWING_ANGLE = 20 # Additional forward swing of arms during the bow (degrees). For hanging.
HIP_VERTICAL_SINK = 20 # How much the central hip point sinks vertically during the deepest bow (model units).


class Humanoid:
    """
    Manages the 15 point-lights representing a human figure and their animation.
    """
    def __init__(self, start_pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)):
        # Point indices:
        # 0: Head
        # 1: Neck
        # 2: Left Shoulder
        # 3: Right Shoulder
        # 4: Left Elbow
        # 5: Right Elbow
        # 6: Left Wrist
        # 7: Right Wrist
        # 8: Torso_Upper (Chest/Sternum)
        # 9: Torso_Lower (Pelvis Center) - This will be the main pivot for bowing
        # 10: Left Hip (lateral point on pelvis)
        # 11: Right Hip (lateral point on pelvis)
        # 12: Left Knee
        # 13: Right Knee
        # 14: Foot_Center (midpoint between ankles/ground contact point)

        self.points = {} # Stores (x, y) coordinates in model space (relative to Foot_Center_Model (0,0))
        self.points_screen = [] # Stores (x, y) coordinates for Pygame drawing
        self.start_pos = start_pos # Screen anchor point for Foot_Center (14)

        self.scale = 1.5 # Scale factor for converting model units to screen pixels

        # Initialize scaled body segment lengths
        self.neck_head_len = NECK_HEAD_LEN * self.scale
        self.neck_upper_torso_len = NECK_UPPER_TORSO_LEN * self.scale
        self.upper_torso_lower_torso_len = UPPER_TORSO_LOWER_TORSO_LEN * self.scale
        self.pelvis_hip_lateral_offset = PELVIS_HIP_LATERAL_OFFSET * self.scale
        self.hip_thigh_len = HIP_THIGH_LEN * self.scale
        self.thigh_shin_len = THIGH_SHIN_LEN * self.scale
        self.shoulder_lateral_offset = SHOULDER_LATERAL_OFFSET * self.scale
        self.shoulder_upper_arm_len = SHOULDER_UPPER_ARM_LEN * self.scale
        self.upper_arm_forearm_len = UPPER_ARM_FOREARM_LEN * self.scale

        # Current state angles, these will be animated
        self.torso_angle = INITIAL_TORSO_ANGLE # Degrees, relative to global vertical (0 = upright)
        self.head_neck_angle = INITIAL_HEAD_NECK_ANGLE # Degrees, relative to neck segment
        self.knee_angle = INITIAL_KNEE_ANGLE # Degrees, deviation from straight (0=straight)
        self.shoulder_angle = INITIAL_SHOULDER_ANGLE # Degrees, initial angle of upper arm from global vertical
        self.elbow_angle = INITIAL_ELBOW_ANGLE # Degrees, internal angle of elbow (180 = straight)
        self.arm_swing_angle = 0 # Additional arm swing for animation

        self.update_points() # Initialize point positions

    def _rotate_point(self, point, origin, angle_rad):
        """Rotate a point around an origin by an angle (radians)."""
        ox, oy = origin
        px, py = point

        qx = ox + math.cos(angle_rad) * (px - ox) - math.sin(angle_rad) * (py - oy)
        qy = oy + math.sin(angle_rad) * (px - ox) + math.cos(angle_rad) * (py - oy)
        return qx, qy

    def update_points(self):
        """
        Calculates the (x,y) positions for all 15 points based on current joint angles.
        All calculations are done in a model coordinate system where Foot_Center (P14) is (0,0)
        and positive Y is upwards. These are then converted to screen coordinates.
        """
        # Convert angles to radians for mathematical functions
        torso_angle_rad = math.radians(self.torso_angle)
        head_neck_angle_rad = math.radians(self.head_neck_angle)
        # For knee and elbow, we define the internal angle, so deviation from straight is (180 - angle)
        # We model them as bending forward.
        knee_bend_rad = math.radians(self.knee_angle) # angle from straight (0=straight)
        
        # Arm's overall swing angle (initial hang + animation swing)
        arm_total_angle_rad = torso_angle_rad + math.radians(self.shoulder_angle + self.arm_swing_angle)
        # Forearm angle relative to upper arm: (180 - elbow_angle) from straight
        forearm_relative_angle_rad = math.radians(180 - self.elbow_angle)
        forearm_total_angle_rad = arm_total_angle_rad + forearm_relative_angle_rad

        # Calculate hip drop based on torso bend (simulates body sinking under weight)
        normalized_torso_bend = min(1.0, self.torso_angle / MAX_TORSO_BEND_ANGLE) if MAX_TORSO_BEND_ANGLE > 0 else 0
        current_hip_vertical_sink = normalized_torso_bend * (HIP_VERTICAL_SINK * self.scale)

        # 14: Foot_Center (Base of the model, fixed at (0,0) in model coordinates)
        self.points[14] = (0, 0)

        # Legs: Knees (12, 13) and Hips (10, 11)
        # Assume legs are mostly vertical, with a slight knee bend.
        # X-offset for legs (half foot width or hip-to-center for stance)
        leg_stance_x = self.pelvis_hip_lateral_offset * 0.7 # Feet slightly narrower than hips

        # Left Knee (12)
        # Y-position is shin length, reduced by cosine of knee bend angle
        l_knee_x_model = -leg_stance_x
        l_knee_y_model = self.thigh_shin_len * math.cos(knee_bend_rad)
        self.points[12] = (l_knee_x_model, l_knee_y_model)
        
        # Right Knee (13)
        r_knee_x_model = leg_stance_x
        self.points[13] = (r_knee_x_model, l_knee_y_model) # Symmetric Y

        # Left Hip (10)
        # Y-position is knee_y + thigh_length (reduced by knee bend and hip flex, simplified)
        l_hip_x_model = l_knee_x_model
        l_hip_y_model = l_knee_y_model + self.hip_thigh_len * math.cos(knee_bend_rad) # Approximated vertical leg segment
        self.points[10] = (l_hip_x_model, l_hip_y_model)
        
        # Right Hip (11)
        r_hip_x_model = r_knee_x_model
        self.points[11] = (r_hip_x_model, l_hip_y_model) # Symmetric Y

        # Torso Chain: Pelvis (9), Upper Torso (8), Neck (1), Head (0)
        # The main pivot for the bowing action is the average hip point,
        # which also sinks vertically (`current_hip_vertical_sink`).
        mid_hip_x_model = (self.points[10][0] + self.points[11][0]) / 2
        mid_hip_y_model = (self.points[10][1] + self.points[11][1]) / 2 - current_hip_vertical_sink
        mid_hip_model = (mid_hip_x_model, mid_hip_y_model)

        # 9: Torso_Lower (Pelvis Center)
        # Initial position relative to mid_hip_model when upright.
        # This point will rotate around mid_hip_model during bowing.
        initial_pelvis_offset_y = self.upper_torso_lower_torso_len * 0.1 # Pelvis is slightly above hips
        pelvis_base_pos_model = (mid_hip_model[0], mid_hip_model[1] + initial_pelvis_offset_y)
        self.points[9] = self._rotate_point(pelvis_base_pos_model, mid_hip_model, torso_angle_rad)
        
        # 8: Torso_Upper (Chest)
        # Rotated around Pelvis Center (P9).
        upper_torso_base_pos_model = (self.points[9][0], self.points[9][1] + self.upper_torso_lower_torso_len)
        self.points[8] = self._rotate_point(upper_torso_base_pos_model, self.points[9], torso_angle_rad)
        
        # 1: Neck
        # Rotated around Upper Torso (P8).
        neck_base_pos_model = (self.points[8][0], self.points[8][1] + self.neck_upper_torso_len)
        self.points[1] = self._rotate_point(neck_base_pos_model, self.points[8], torso_angle_rad)
        
        # 0: Head
        # Rotated around Neck (P1). Head angle adds to torso angle.
        head_base_pos_model = (self.points[1][0], self.points[1][1] + self.neck_head_len)
        self.points[0] = self._rotate_point(head_base_pos_model, self.points[1], torso_angle_rad + head_neck_angle_rad)

        # Shoulders (2, 3): Attached to Upper Torso (P8) and rotate with it.
        # Calculate perpendicular vector to the torso segment (P9 to P8) to place shoulders laterally.
        torso_vec_x = self.points[8][0] - self.points[9][0]
        torso_vec_y = self.points[8][1] - self.points[9][1]
        
        perp_vec_x = -torso_vec_y # Perpendicular vector (rotated 90 deg clockwise)
        perp_vec_y = torso_vec_x
        
        perp_len = math.sqrt(perp_vec_x**2 + perp_vec_y**2)
        if perp_len > 0:
            perp_vec_x = (perp_vec_x / perp_len) * self.shoulder_lateral_offset
            perp_vec_y = (perp_vec_y / perp_len) * self.shoulder_lateral_offset
        
        # 2: Left Shoulder
        self.points[2] = (self.points[8][0] - perp_vec_x, self.points[8][1] - perp_vec_y)
        
        # 3: Right Shoulder
        self.points[3] = (self.points[8][0] + perp_vec_x, self.points[8][1] + perp_vec_y)
        
        # Arms: Elbows (4, 5) and Wrists (6, 7)
        # Positioned relative to shoulders, rotated by `arm_total_angle_rad` (upper arm)
        # and `forearm_total_angle_rad` (forearm).
        
        # 4: Left Elbow
        l_elbow_x_model = self.points[2][0] + self.shoulder_upper_arm_len * math.sin(arm_total_angle_rad)
        l_elbow_y_model = self.points[2][1] + self.shoulder_upper_arm_len * math.cos(arm_total_angle_rad)
        self.points[4] = (l_elbow_x_model, l_elbow_y_model)
        
        # 5: Right Elbow
        r_elbow_x_model = self.points[3][0] - self.shoulder_upper_arm_len * math.sin(arm_total_angle_rad) # Mirrored X
        r_elbow_y_model = self.points[3][1] + self.shoulder_upper_arm_len * math.cos(arm_total_angle_rad)
        self.points[5] = (r_elbow_x_model, r_elbow_y_model)
        
        # 6: Left Wrist
        l_wrist_x_model = self.points[4][0] + self.upper_arm_forearm_len * math.sin(forearm_total_angle_rad)
        l_wrist_y_model = self.points[4][1] + self.upper_arm_forearm_len * math.cos(forearm_total_angle_rad)
        self.points[6] = (l_wrist_x_model, l_wrist_y_model)
        
        # 7: Right Wrist
        r_wrist_x_model = self.points[5][0] - self.upper_arm_forearm_len * math.sin(forearm_total_angle_rad) # Mirrored X
        r_wrist_y_model = self.points[5][1] + self.upper_arm_forearm_len * math.cos(forearm_total_angle_rad)
        self.points[7] = (r_wrist_x_model, r_wrist_y_model)

        # Convert model coordinates to screen coordinates
        # Screen Y-axis grows downwards, so model Y (upwards) must be inverted relative to the anchor.
        self.points_screen = []
        for i in range(15):
            x_model, y_model = self.points[i]
            screen_x = int(self.start_pos[0] + x_model)
            screen_y = int(self.start_pos[1] - y_model) # Invert Y-axis for Pygame
            self.points_screen.append((screen_x, screen_y))

    def animate(self, frame_time):
        """
        Updates joint angles based on the current animation progress (0.0 to 1.0).
        Uses a three-phase animation cycle: bow down, hold, stand up.
        """
        # Smooth step interpolation function: `0.5 - 0.5 * math.cos(math.pi * progress)`
        # This provides a smooth start and end to each phase.
        
        if frame_time <= 0.4: # Phase 1: Bowing down (0% to 40% of cycle)
            progress = frame_time / 0.4
            eased_progress = 0.5 - 0.5 * math.cos(math.pi * progress)
            
            self.torso_angle = INITIAL_TORSO_ANGLE + (MAX_TORSO_BEND_ANGLE - INITIAL_TORSO_ANGLE) * eased_progress
            self.head_neck_angle = INITIAL_HEAD_NECK_ANGLE + 10 * eased_progress # Head dips slightly forward
            self.knee_angle = INITIAL_KNEE_ANGLE + (MAX_KNEE_BEND_ANGLE - INITIAL_KNEE_ANGLE) * eased_progress
            self.arm_swing_angle = MAX_ARM_SWING_ANGLE * eased_progress
            
        elif frame_time <= 0.6: # Phase 2: Holding bow (40% to 60% of cycle)
            self.torso_angle = MAX_TORSO_BEND_ANGLE
            self.head_neck_angle = INITIAL_HEAD_NECK_ANGLE + 10
            self.knee_angle = MAX_KNEE_BEND_ANGLE
            self.arm_swing_angle = MAX_ARM_SWING_ANGLE
            
        else: # Phase 3: Standing up (60% to 100% of cycle)
            progress = (frame_time - 0.6) / 0.4
            eased_progress = 0.5 - 0.5 * math.cos(math.pi * progress)
            
            self.torso_angle = MAX_TORSO_BEND_ANGLE - (MAX_TORSO_BEND_ANGLE - INITIAL_TORSO_ANGLE) * eased_progress
            self.head_neck_angle = INITIAL_HEAD_NECK_ANGLE + 10 * (1 - eased_progress)
            self.knee_angle = MAX_KNEE_BEND_ANGLE - (MAX_KNEE_BEND_ANGLE - INITIAL_KNEE_ANGLE) * eased_progress
            self.arm_swing_angle = MAX_ARM_SWING_ANGLE * (1 - eased_progress)
            
        self.update_points()

    def draw(self, screen):
        """Draws all 15 point-lights on the Pygame screen."""
        for i in range(15):
            pygame.draw.circle(screen, WHITE, self.points_screen[i], POINT_RADIUS)


# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Sadman Bowing with Heavy Weight")
clock = pygame.time.Clock()

# --- Create Humanoid ---
# Position the humanoid on the screen. `start_pos` is mapped to Foot_Center (P14).
humanoid = Humanoid(start_pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))

# --- Animation Loop ---
running = True
frame_count = 0
total_frames = FPS * ANIMATION_DURATION_SECONDS

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate animation progress (normalized from 0.0 to 1.0, loops)
    animation_progress = (frame_count % total_frames) / total_frames

    humanoid.animate(animation_progress) # Update the humanoid's pose

    screen.fill(BLACK) # Clear screen with black background
    humanoid.draw(screen) # Draw the updated points
    pygame.display.flip() # Update the full display

    frame_count += 1
    clock.tick(FPS) # Control frame rate

pygame.quit()
