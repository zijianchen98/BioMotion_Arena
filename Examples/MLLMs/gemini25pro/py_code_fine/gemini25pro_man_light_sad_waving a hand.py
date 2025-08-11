
import pygame
import numpy as np
import sys

# --- Configuration ---
WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 6
ANIMATION_DURATION_S = 4.0  # Duration of one wave cycle

# --- Joint Indices (for clarity) ---
HEAD = 0
STERNUM = 1
PELVIS = 2
L_SHOULDER = 3
R_SHOULDER = 4
L_ELBOW = 5
R_ELBOW = 6
L_WRIST = 7
R_WRIST = 8
L_HIP = 9
R_HIP = 10
L_KNEE = 11
R_KNEE = 12
L_ANKLE = 13
R_ANKLE = 14

# --- Skeleton Definition (limb length ratios) ---
SKELETON_GEOMETRY = {
    'torso_len': 1.0,
    'neck_len': 0.35,
    'shoulder_width': 0.9,
    'upper_arm_len': 0.8,
    'forearm_len': 0.8,
    'hip_width': 0.7,
    'thigh_len': 1.0,
    'calf_len': 1.0,
}
SCALE = 70.0  # Master scale to convert geometry to pixels

class BiologicalMotionAnimator:
    """
    Creates a point-light animation of a sad man waving his hand.
    The animation uses a 15-point kinematic model to ensure biomechanical
    plausibility. The "sad" emotion is conveyed through a slumped posture,
    drooping shoulders, a tilted head, and slow, low-energy movements.
    """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Biological Motion: Sad Man Waving")
        self.clock = pygame.time.Clock()
        self.points = np.zeros((15, 2), dtype=float)
        self.time = 0.0

    def calculate_frame(self, t):
        """Calculates the positions of all 15 points at time t."""
        cycle_progress = (t % ANIMATION_DURATION_S) / ANIMATION_DURATION_S

        # --- Base Body Position and Sad Posture ---
        center_x = WIDTH / 2
        pelvis_y_base = HEIGHT * 0.45

        # Subtle body sway and bobbing to indicate sadness
        bob_freq = 0.4
        bob_amp = 2.0
        sway_freq = 0.2
        sway_amp = 1.5
        body_bob = bob_amp * np.sin(2 * np.pi * bob_freq * t)
        body_sway = sway_amp * np.sin(2 * np.pi * sway_freq * t)

        # Sad posture: slumped torso and tilted head
        slump_angle = np.deg2rad(8)
        head_tilt_angle = np.deg2rad(20)

        # --- Kinematic Chain Calculation (from the Pelvis up/down) ---
        # Angles are defined relative to vertical (0 deg = down, positive = CCW)

        # 1. Torso
        self.points[PELVIS] = [center_x + body_sway, pelvis_y_base + body_bob]
        
        sternum_angle_from_vertical = -slump_angle
        self.points[STERNUM] = [
            self.points[PELVIS, 0] + SKELETON_GEOMETRY['torso_len'] * SCALE * np.sin(sternum_angle_from_vertical),
            self.points[PELVIS, 1] - SKELETON_GEOMETRY['torso_len'] * SCALE * np.cos(sternum_angle_from_vertical)
        ]

        # 2. Head
        head_angle_from_vertical = sternum_angle_from_vertical - head_tilt_angle
        self.points[HEAD] = [
            self.points[STERNUM, 0] + SKELETON_GEOMETRY['neck_len'] * SCALE * np.sin(head_angle_from_vertical),
            self.points[STERNUM, 1] - SKELETON_GEOMETRY['neck_len'] * SCALE * np.cos(head_angle_from_vertical)
        ]

        # 3. Shoulders (drooping)
        shoulder_droop = 10
        self.points[L_SHOULDER] = [self.points[STERNUM, 0] - SKELETON_GEOMETRY['shoulder_width'] * SCALE / 2, self.points[STERNUM, 1] + shoulder_droop]
        self.points[R_SHOULDER] = [self.points[STERNUM, 0] + SKELETON_GEOMETRY['shoulder_width'] * SCALE / 2, self.points[STERNUM, 1] + shoulder_droop]

        # 4. Hips
        self.points[L_HIP] = [self.points[PELVIS, 0] - SKELETON_GEOMETRY['hip_width'] * SCALE / 2, self.points[PELVIS, 1]]
        self.points[R_HIP] = [self.points[PELVIS, 0] + SKELETON_GEOMETRY['hip_width'] * SCALE / 2, self.points[PELVIS, 1]]

        # 5. Legs (natural A-stance with slight bend)
        thigh_angle = np.deg2rad(3)
        knee_bend = np.deg2rad(6)
        
        self.points[L_KNEE] = [
            self.points[L_HIP, 0] + SKELETON_GEOMETRY['thigh_len'] * SCALE * np.sin(-thigh_angle),
            self.points[L_HIP, 1] + SKELETON_GEOMETRY['thigh_len'] * SCALE * np.cos(-thigh_angle)
        ]
        self.points[L_ANKLE] = [
            self.points[L_KNEE, 0] + SKELETON_GEOMETRY['calf_len'] * SCALE * np.sin(-thigh_angle + knee_bend),
            self.points[L_KNEE, 1] + SKELETON_GEOMETRY['calf_len'] * SCALE * np.cos(-thigh_angle + knee_bend)
        ]
        self.points[R_KNEE] = [
            self.points[R_HIP, 0] + SKELETON_GEOMETRY['thigh_len'] * SCALE * np.sin(thigh_angle),
            self.points[R_HIP, 1] + SKELETON_GEOMETRY['thigh_len'] * SCALE * np.cos(thigh_angle)
        ]
        self.points[R_ANKLE] = [
            self.points[R_KNEE, 0] + SKELETON_GEOMETRY['calf_len'] * SCALE * np.sin(thigh_angle - knee_bend),
            self.points[R_KNEE, 1] + SKELETON_GEOMETRY['calf_len'] * SCALE * np.cos(thigh_angle - knee_bend)
        ]


        # 6. Left Arm (hanging limply)
        l_shoulder_angle = np.deg2rad(5)
        l_elbow_angle = np.deg2rad(10)
        self.points[L_ELBOW] = [
            self.points[L_SHOULDER, 0] + SKELETON_GEOMETRY['upper_arm_len'] * SCALE * np.sin(l_shoulder_angle),
            self.points[L_SHOULDER, 1] + SKELETON_GEOMETRY['upper_arm_len'] * SCALE * np.cos(l_shoulder_angle)
        ]
        self.points[L_WRIST] = [
            self.points[L_ELBOW, 0] + SKELETON_GEOMETRY['forearm_len'] * SCALE * np.sin(l_shoulder_angle + l_elbow_angle),
            self.points[L_ELBOW, 1] + SKELETON_GEOMETRY['forearm_len'] * SCALE * np.cos(l_shoulder_angle + l_elbow_angle)
        ]

        # 7. Right Arm (waving motion)
        lift_phase, wave_phase, lower_phase = 0.25, 0.50, 0.25

        shoulder_hang_angle = np.deg2rad(-5)
        shoulder_lift_angle = np.deg2rad(95)
        elbow_straight_angle = np.deg2rad(-10)
        elbow_bent_angle = np.deg2rad(-90)
        wave_magnitude = np.deg2rad(25)

        if cycle_progress < lift_phase:
            p = cycle_progress / lift_phase
            p = 0.5 * (1 - np.cos(np.pi * p))
            shoulder_angle = shoulder_hang_angle + (shoulder_lift_angle - shoulder_hang_angle) * p
            elbow_angle = elbow_straight_angle + (elbow_bent_angle - elbow_straight_angle) * p
            wave_offset = 0
        elif cycle_progress < lift_phase + wave_phase:
            p = (cycle_progress - lift_phase) / wave_phase
            shoulder_angle = shoulder_lift_angle
            elbow_angle = elbow_bent_angle
            wave_offset = wave_magnitude * np.sin(p * 2 * np.pi * 2)
        else:
            p = (cycle_progress - lift_phase - wave_phase) / lower_phase
            p = 0.5 * (1 - np.cos(np.pi * p))
            shoulder_angle = shoulder_lift_angle - (shoulder_lift_angle - shoulder_hang_angle) * p
            elbow_angle = elbow_bent_angle - (elbow_bent_angle - elbow_straight_angle) * p
            wave_offset = 0

        self.points[R_ELBOW] = [
            self.points[R_SHOULDER, 0] + SKELETON_GEOMETRY['upper_arm_len'] * SCALE * np.sin(shoulder_angle),
            self.points[R_SHOULDER, 1] + SKELETON_GEOMETRY['upper_arm_len'] * SCALE * np.cos(shoulder_angle)
        ]
        total_forearm_angle = shoulder_angle + elbow_angle + wave_offset
        self.points[R_WRIST] = [
            self.points[R_ELBOW, 0] + SKELETON_GEOMETRY['forearm_len'] * SCALE * np.sin(total_forearm_angle),
            self.points[R_ELBOW, 1] + SKELETON_GEOMETRY['forearm_len'] * SCALE * np.cos(total_forearm_angle)
        ]

    def draw(self):
        """Draws the points on the screen."""
        self.screen.fill(BACKGROUND_COLOR)
        for point in self.points:
            pygame.draw.circle(self.screen, POINT_COLOR, (int(point[0]), int(point[1])), POINT_RADIUS)
        pygame.display.flip()

    def run(self):
        """Main animation loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
            
            delta_time = self.clock.tick(FPS) / 1000.0
            self.time += delta_time

            self.calculate_frame(self.time)
            self.draw()

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    animator = BiologicalMotionAnimator()
    animator.run()
