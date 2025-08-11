
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
POINT_RADIUS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Animation parameters for "running with heavy weight"
# Adjusted for a slightly slower, more deliberate, and vertically exaggerated motion.
RUNNING_SPEED = 0.065  # How fast the animation progresses through a cycle (radians per frame) - slightly slower
VERTICAL_BOUNCE_AMPLITUDE = 45 # For torso, head - increased for heavy weight
HORIZONTAL_BODY_SWAY_AMPLITUDE = 5 # Small horizontal sway

# Limb lengths (relative proportions, adjust for visual appeal)
L_HEAD_TO_SHOULDER = 60
L_UPPER_ARM = 50
L_LOWER_ARM = 40
L_SHOULDER_WIDTH = 60
L_TORSO_TO_HIP = 80
L_HIP_WIDTH = 40
L_UPPER_LEG = 80
L_LOWER_LEG = 80
L_FOOT = 20

# Arm swing and bend parameters
ARM_SWING_AMPLITUDE = math.radians(20) # How much arms swing - reduced for heavy weight
# Internal elbow angle: 180 deg (pi) for straight, 90 deg (pi/2) for right angle bend.
# For running, elbows are typically bent around 90-100 degrees. For heavy weight, maybe more bent.
ARM_ELBOW_INTERNAL_ANGLE = math.radians(100) # Angle *inside* the elbow joint

# Leg swing and bend parameters
LEG_SWING_AMPLITUDE = math.radians(30) # How much legs swing - reduced for shorter stride
# Knee bend: this is the maximum additional bend from the straight leg posture.
# For running, knee bends significantly. For heavy weight, potentially more lift.
KNEE_BEND_AMPLITUDE = math.radians(70) # How much knee bends during swing - increased for more lift
FOOT_ANGLE_OFFSET = math.radians(10) # Small angle for foot to point slightly down/up

# --- Helper functions for limb positioning ---
def get_joint_coords_from_parent(origin_x, origin_y, length, angle_from_horizontal):
    """
    Calculates point position based on origin, length, and angle from the positive X-axis (horizontal right).
    Pygame Y increases downwards, so standard trigonometric angles apply:
    0 = right, pi/2 = down, pi = left, 3pi/2 = up.
    """
    x = origin_x + length * math.cos(angle_from_horizontal)
    y = origin_y + length * math.sin(angle_from_horizontal)
    return x, y

# --- Main animation class ---
class PointLightMan:
    def __init__(self):
        self.points = {}
        # Base position of the man on screen (center of hips when standing still)
        self.base_x = SCREEN_WIDTH // 2
        self.base_y = SCREEN_HEIGHT // 2 + 100 # Adjusted for typical standing height relative to screen center

    def update(self, t):
        # Body vertical oscillation (running bounce)
        # 1 - cos(2*t) makes the vertical position oscillate from 0 to 2, peaking at t=pi/2, 3pi/2
        # This aligns with the flight phase of running where the body is highest.
        pelvis_y_offset = VERTICAL_BOUNCE_AMPLITUDE * (1 - math.cos(t * 2))
        current_pelvis_y = self.base_y - pelvis_y_offset # Subtract because positive Y is down in Pygame

        # Slight horizontal body sway (for naturalism)
        body_x_sway = HORIZONTAL_BODY_SWAY_AMPLITUDE * math.cos(t)
        
        # --- Head ---
        head_x = self.base_x + body_x_sway
        head_y = current_pelvis_y - L_TORSO_TO_HIP - L_HEAD_TO_SHOULDER
        self.points["Head"] = (head_x, head_y)

        # --- Shoulders ---
        shoulder_y = current_pelvis_y - L_TORSO_TO_HIP
        l_shoulder_x = self.base_x - L_SHOULDER_WIDTH / 2 + body_x_sway
        r_shoulder_x = self.base_x + L_SHOULDER_WIDTH / 2 + body_x_sway
        self.points["L_Shoulder"] = (l_shoulder_x, shoulder_y)
        self.points["R_Shoulder"] = (r_shoulder_x, shoulder_y)

        # --- Arms (Elbows & Wrists) ---
        # Arm swing: counter-phase to contralateral leg.
        # If t=0, right leg is forward. So left arm should be forward (arm_swing_L is max positive).
        # Cosine starts at max (1) at t=0, so `math.cos(t)` works for forward swing.
        arm_swing_L = ARM_SWING_AMPLITUDE * math.cos(t)
        arm_swing_R = ARM_SWING_AMPLITUDE * math.cos(t + math.pi) # Right arm counter-phase to left arm

        # Left Arm:
        # Upper arm angle: 1.5*pi (270 deg) is straight down. Swing forward decreases angle (towards pi).
        upper_arm_angle_L = 1.5 * math.pi - arm_swing_L 
        l_elbow_x, l_elbow_y = get_joint_coords_from_parent(l_shoulder_x, shoulder_y, L_UPPER_ARM, upper_arm_angle_L)
        
        # Lower arm angle: relative to upper arm. (math.pi - ARM_ELBOW_INTERNAL_ANGLE) is the angle to add
        # to the upper arm's absolute angle to get the lower arm's absolute angle.
        # This makes the elbow bend "inward" towards the body.
        lower_arm_angle_L = upper_arm_angle_L + (math.pi - ARM_ELBOW_INTERNAL_ANGLE)
        l_wrist_x, l_wrist_y = get_joint_coords_from_parent(l_elbow_x, l_elbow_y, L_LOWER_ARM, lower_arm_angle_L)
        
        self.points["L_Elbow"] = (l_elbow_x, l_elbow_y)
        self.points["L_Wrist"] = (l_wrist_x, l_wrist_y)

        # Right Arm: (mirrored logic)
        upper_arm_angle_R = 1.5 * math.pi + arm_swing_R # Swing forward increases angle (towards 2pi or 0)
        r_elbow_x, r_elbow_y = get_joint_coords_from_parent(r_shoulder_x, shoulder_y, L_UPPER_ARM, upper_arm_angle_R)
        
        lower_arm_angle_R = upper_arm_angle_R - (math.pi - ARM_ELBOW_INTERNAL_ANGLE) # Bend inward (subtract angle for right arm)
        r_wrist_x, r_wrist_y = get_joint_coords_from_parent(r_elbow_x, r_elbow_y, L_LOWER_ARM, lower_arm_angle_R)
        
        self.points["R_Elbow"] = (r_elbow_x, r_elbow_y)
        self.points["R_Wrist"] = (r_wrist_x, r_wrist_y)

        # --- Hips ---
        hip_y = current_pelvis_y
        self.points["L_Hip"] = (self.base_x - L_HIP_WIDTH / 2 + body_x_sway, hip_y)
        self.points["R_Hip"] = (self.base_x + L_HIP_WIDTH / 2 + body_x_sway, hip_y)

        # --- Legs (Knees, Ankles, Feet) ---
        # Leg swing: counter-phase to each other.
        # If t=0, Right leg swings forward (leg_swing_R is max positive).
        leg_swing_R = LEG_SWING_AMPLITUDE * math.cos(t)
        leg_swing_L = LEG_SWING_AMPLITUDE * math.cos(t + math.pi) # Left leg counter-phase to Right leg

        # Knee bend (more pronounced during swing phase in running)
        # (1 - cos(2*t)) for knee bend makes it max at mid-swing and min at extremes.
        knee_bend_factor_R = KNEE_BEND_AMPLITUDE * (1 - math.cos(2 * t))
        knee_bend_factor_L = KNEE_BEND_AMPLITUDE * (1 - math.cos(2 * t + math.pi)) # Counter-phase

        # Left Leg:
        l_hip_x, l_hip_y = self.points["L_Hip"]
        # Upper leg angle: 1.5*pi is straight down. Swing forward decreases angle (towards pi).
        upper_leg_angle_L = 1.5 * math.pi - leg_swing_L 
        l_knee_x, l_knee_y = get_joint_coords_from_parent(l_hip_x, l_hip_y, L_UPPER_LEG, upper_leg_angle_L)

        # Lower leg angle: Bend "inward" (clockwise for left leg), so add the bend factor to angle.
        lower_leg_angle_L = upper_leg_angle_L + knee_bend_factor_L 
        l_ankle_x, l_ankle_y = get_joint_coords_from_parent(l_knee_x, l_knee_y, L_LOWER_LEG, lower_leg_angle_L)

        # Foot angle: Small offset to keep foot relatively flat or slightly pointed.
        foot_angle_L = lower_leg_angle_L + FOOT_ANGLE_OFFSET
        l_foot_x, l_foot_y = get_joint_coords_from_parent(l_ankle_x, l_ankle_y, L_FOOT, foot_angle_L)

        self.points["L_Knee"] = (l_knee_x, l_knee_y)
        self.points["L_Ankle"] = (l_ankle_x, l_ankle_y)
        self.points["L_Foot"] = (l_foot_x, l_foot_y)

        # Right Leg: (mirrored logic)
        r_hip_x, r_hip_y = self.points["R_Hip"]
        upper_leg_angle_R = 1.5 * math.pi + leg_swing_R # Swing forward increases angle (towards 2pi or 0)
        r_knee_x, r_knee_y = get_joint_coords_from_parent(r_hip_x, r_hip_y, L_UPPER_LEG, upper_leg_angle_R)

        # Lower leg angle: Bend "inward" (counter-clockwise for right leg), so subtract the bend factor from angle.
        lower_leg_angle_R = upper_leg_angle_R - knee_bend_factor_R
        r_ankle_x, r_ankle_y = get_joint_coords_from_parent(r_knee_x, r_knee_y, L_LOWER_LEG, lower_leg_angle_R)

        foot_angle_R = lower_leg_angle_R - FOOT_ANGLE_OFFSET
        r_foot_x, r_foot_y = get_joint_coords_from_parent(r_ankle_x, r_ankle_y, L_FOOT, foot_angle_R)

        self.points["R_Knee"] = (r_knee_x, r_knee_y)
        self.points["R_Ankle"] = (r_ankle_x, r_ankle_y)
        self.points["R_Foot"] = (r_foot_x, r_foot_y)
        
    def draw(self, screen):
        # Draw each point as a white circle
        for point_name, (x, y) in self.points.items():
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Running with Heavy Weight")
clock = pygame.time.Clock()

man = PointLightMan()
time_elapsed = 0.0 # Time counter for animation phase, progresses from 0 to 2*pi

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK) # Clear screen with black background

    # Update man's position based on time
    man.update(time_elapsed)
    man.draw(screen)

    pygame.display.flip() # Update the full display Surface to the screen

    # Increment time for the next frame, looping at 2*pi (one full cycle)
    time_elapsed += RUNNING_SPEED
    if time_elapsed >= 2 * math.pi:
        time_elapsed -= 2 * math.pi

    clock.tick(FPS) # Control frame rate

pygame.quit()
