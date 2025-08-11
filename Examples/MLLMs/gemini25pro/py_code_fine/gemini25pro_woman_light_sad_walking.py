
import pygame
import numpy as np

# --- Constants ---
# Screen settings
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
POINT_RADIUS = 6

# --- Animation Parameters ---
CYCLE_DURATION = 2.8  # Seconds for one full walk cycle (slower for sadness)
CAMERA_DISTANCE = 30
PERSPECTIVE_FACTOR = 700

# --- Biomechanical Model (Sad Woman, Light Weight) ---
# Using a hierarchical model with rotations for biomechanical plausibility.
# Coordinates: X=right/left, Y=up/down, Z=forward/backward

# Overall scale of the figure
BODY_SCALE = 120

# Posture characteristics for "sad" walk
SLUMP_ANGLE = np.radians(20)  # Forward torso slump
HEAD_TILT = np.radians(25)    # Additional downward head tilt

# Body segment dimensions
TORSO_LENGTH = 1.6 * BODY_SCALE
NECK_LENGTH = 0.3 * BODY_SCALE
HIP_WIDTH = 0.5 * BODY_SCALE
SHOULDER_WIDTH = 0.6 * BODY_SCALE
THIGH_LENGTH = 1.1 * BODY_SCALE
SHIN_LENGTH = 1.1 * BODY_SCALE
UPPER_ARM_LENGTH = 0.9 * BODY_SCALE
LOWER_ARM_LENGTH = 0.9 * BODY_SCALE

# Kinematic parameters for "sad" walk
VERTICAL_BOB_AMP = 0.04 * BODY_SCALE # Vertical oscillation of the torso
HIP_AMP = np.radians(22)             # Max hip swing angle (reduced for shorter stride)
KNEE_AMP = np.radians(65)            # Max knee flexion angle
SHOULDER_AMP = np.radians(12)        # Max shoulder swing angle (reduced arm swing)
ELBOW_AMP = np.radians(30)           # Max elbow flexion angle

def rot_x(angle):
    """Returns a 3D rotation matrix around the X-axis."""
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])

def main():
    """Main function to run the animation."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Walking Woman")
    clock = pygame.time.Clock()

    t = 0.0  # Represents the angle in the walk cycle, from 0 to 2*pi
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # --- Update Animation State ---
        # Increment the cycle angle based on frame rate and desired cycle duration
        dt = 2 * np.pi / (CYCLE_DURATION * FPS)
        t = (t + dt) % (2 * np.pi)

        # --- Calculate 3D Joint Positions using a Hierarchical Model ---
        
        # 1. Root of the model: The center of the torso, which bobs vertically.
        torso_center_y = -VERTICAL_BOB_AMP * np.cos(2 * t)
        torso_center = np.array([0, torso_center_y, 0])
        
        # 2. Torso Structure: Define pelvis and neck relative to the center, applying the slump rotation.
        slump_rotation = rot_x(SLUMP_ANGLE)
        pelvis_pos = torso_center + slump_rotation @ np.array([0, -TORSO_LENGTH / 2, 0])
        neck_pos = torso_center + slump_rotation @ np.array([0, TORSO_LENGTH / 2, 0])
        
        # 3. Head: Positioned relative to the neck, with both slump and additional head tilt.
        head_rotation = rot_x(SLUMP_ANGLE + HEAD_TILT)
        head_pos = neck_pos + head_rotation @ np.array([0, NECK_LENGTH, 0])
        
        # 4. Limb attachment points (Shoulders and Hips)
        r_shoulder_pos = neck_pos + np.array([SHOULDER_WIDTH / 2, 0, 0])
        l_shoulder_pos = neck_pos + np.array([-SHOULDER_WIDTH / 2, 0, 0])
        r_hip_pos = pelvis_pos + np.array([HIP_WIDTH / 2, 0, 0])
        l_hip_pos = pelvis_pos + np.array([-HIP_WIDTH / 2, 0, 0])

        # 5. Limb Kinematics: Calculate angles for each joint based on the cycle time `t`.
        # Angles (alpha=0 corresponds to the limb's resting pose, pointing straight down)
        r_hip_angle = -HIP_AMP * np.cos(t)
        l_hip_angle = -HIP_AMP * np.cos(t + np.pi)
        r_knee_flex = KNEE_AMP * (1 - np.cos(t)) / 2
        l_knee_flex = KNEE_AMP * (1 - np.cos(t + np.pi)) / 2

        r_shoulder_angle = -SHOULDER_AMP * np.cos(t + np.pi)
        l_shoulder_angle = -SHOULDER_AMP * np.cos(t)
        r_elbow_flex = ELBOW_AMP * (1 + np.cos(t)) / 2
        l_elbow_flex = ELBOW_AMP * (1 + np.cos(t + np.pi)) / 2

        # 6. Calculate final limb joint positions by applying rotations.
        # The swing plane of the limbs is also affected by the torso's slump.
        
        # Right Leg
        r_thigh_rot = rot_x(SLUMP_ANGLE + r_hip_angle)
        r_knee_pos = r_hip_pos + r_thigh_rot @ np.array([0, -THIGH_LENGTH, 0])
        r_shin_rot = rot_x(SLUMP_ANGLE + r_hip_angle - r_knee_flex)
        r_ankle_pos = r_knee_pos + r_shin_rot @ np.array([0, -SHIN_LENGTH, 0])

        # Left Leg
        l_thigh_rot = rot_x(SLUMP_ANGLE + l_hip_angle)
        l_knee_pos = l_hip_pos + l_thigh_rot @ np.array([0, -THIGH_LENGTH, 0])
        l_shin_rot = rot_x(SLUMP_ANGLE + l_hip_angle - l_knee_flex)
        l_ankle_pos = l_knee_pos + l_shin_rot @ np.array([0, -SHIN_LENGTH, 0])

        # Right Arm
        r_upper_arm_rot = rot_x(SLUMP_ANGLE + r_shoulder_angle)
        r_elbow_pos = r_shoulder_pos + r_upper_arm_rot @ np.array([0, -UPPER_ARM_LENGTH, 0])
        r_lower_arm_rot = rot_x(SLUMP_ANGLE + r_shoulder_angle - r_elbow_flex)
        r_wrist_pos = r_elbow_pos + r_lower_arm_rot @ np.array([0, -LOWER_ARM_LENGTH, 0])

        # Left Arm
        l_upper_arm_rot = rot_x(SLUMP_ANGLE + l_shoulder_angle)
        l_elbow_pos = l_shoulder_pos + l_upper_arm_rot @ np.array([0, -UPPER_ARM_LENGTH, 0])
        l_lower_arm_rot = rot_x(SLUMP_ANGLE + l_shoulder_angle - l_elbow_flex)
        l_wrist_pos = l_elbow_pos + l_lower_arm_rot @ np.array([0, -LOWER_ARM_LENGTH, 0])

        # --- Assemble the 15 points for rendering ---
        points_3d = np.array([
            head_pos, neck_pos, pelvis_pos,
            r_shoulder_pos, l_shoulder_pos,
            r_elbow_pos, l_elbow_pos,
            r_wrist_pos, l_wrist_pos,
            r_hip_pos, l_hip_pos,
            r_knee_pos, l_knee_pos,
            r_ankle_pos, l_ankle_pos
        ])
        
        # --- Project 3D points to 2D screen coordinates ---
        projected_points = []
        for p in points_3d:
            x, y, z = p
            # Simple perspective projection
            z_effective = z + CAMERA_DISTANCE
            scale = PERSPECTIVE_FACTOR / z_effective if z_effective != 0 else PERSPECTIVE_FACTOR
            
            # Convert to screen coordinates (origin at top-left)
            px = int(x * scale + WIDTH / 2)
            py = int(-y * scale + HEIGHT / 2)  # Y-axis is inverted in screen space
            projected_points.append((px, py))
            
        # --- Drawing ---
        screen.fill(BLACK)
        for p in projected_points:
            pygame.draw.circle(screen, WHITE, p, POINT_RADIUS)
        pygame.display.flip()
        
        # --- Control Frame Rate ---
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
