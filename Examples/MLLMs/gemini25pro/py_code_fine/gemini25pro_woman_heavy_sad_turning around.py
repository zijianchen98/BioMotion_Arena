
import pygame
import numpy as np
import math

class PointLightStimulus:
    """
    A class to create and run a point-light stimulus animation
    depicting a sad woman with a heavy weight turning around.
    """

    def __init__(self):
        """Initialize the animation environment and parameters."""
        pygame.init()

        # --- Display Constants ---
        self.WIDTH, self.HEIGHT = 600, 800
        self.BACKGROUND_COLOR = (0, 0, 0)
        self.POINT_COLOR = (255, 255, 255)
        self.POINT_RADIUS = 6
        self.FPS = 60

        # --- Animation Parameters ---
        # A longer duration enhances the feeling of weight and sadness.
        self.ANIMATION_DURATION_SECONDS = 8
        self.TOTAL_FRAMES = self.FPS * self.ANIMATION_DURATION_SECONDS

        # --- 3D Projection Parameters ---
        self.FOCAL_LENGTH = 350
        self.DEPTH_OFFSET = 450

        # --- Setup Screen ---
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Biological Motion: Sad Woman Turning")
        self.clock = pygame.time.Clock()
        
        # --- Data Initialization ---
        self.sad_posture = self._create_sad_heavy_posture()
        self.frame_count = 0

    def _create_base_skeleton(self):
        """Defines the 3D coordinates of the 15 joints in a neutral pose."""
        # Using a standard 15-point skeleton model.
        # Origin is at the floor, between the feet. Y is up, X is right, Z is forward.
        return np.array([
            # [x, y, z]
            [0, 170, 0],   # 0: Head
            [0, 155, 0],   # 1: Neck
            [-20, 150, 0], # 2: Left Shoulder
            [20, 150, 0],  # 3: Right Shoulder
            [-25, 120, 0], # 4: Left Elbow
            [25, 120, 0],  # 5: Right Elbow
            [-30, 90, 0],  # 6: Left Wrist
            [30, 90, 0],   # 7: Right Wrist
            [0, 125, 0],   # 8: Spine
            [-15, 100, 0], # 9: Left Hip
            [15, 100, 0],  # 10: Right Hip
            [-18, 50, 0],  # 11: Left Knee
            [18, 50, 0],   # 12: Right Knee
            [-20, 0, 0],   # 13: Left Ankle
            [20, 0, 0]     # 14: Right Ankle
        ], dtype=float)

    def _create_sad_heavy_posture(self):
        """Modifies the base skeleton to reflect a sad, heavy-laden posture."""
        posture = self._create_base_skeleton()
        # Slumped torso and head to show sadness
        posture[0] += [0, -15, 5]  # Head down and forward
        posture[1] += [0, -10, 3]  # Neck forward
        posture[8] += [0, -10, 8]  # Spine curved forward
        # Shoulders slump forward and down
        posture[2] += [0, -8, 10]
        posture[3] += [0, -8, 10]
        # Arms held as if carrying a heavy object in front
        posture[4] += [0, -10, 20] 
        posture[5] += [0, -10, 20] 
        posture[6] += [0, -15, 30] 
        posture[7] += [0, -15, 30] 
        # Body is lowered due to weight and bent knees
        posture[:, 1] -= 15
        return posture

    def _get_rotation_matrix_y(self, angle_rad):
        """Returns a rotation matrix for a given angle around the Y-axis."""
        cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)
        return np.array([
            [cos_a, 0, sin_a],
            [0,     1, 0    ],
            [-sin_a,0, cos_a]
        ])

    def _update_points(self):
        """Calculates the 3D positions of all points for the current frame."""
        # `t` is the progress of the animation cycle (0.0 to 1.0)
        t = (self.frame_count % self.TOTAL_FRAMES) / self.TOTAL_FRAMES

        # 1. Primary Motion: Full 360-degree turn
        total_angle = t * 2 * math.pi
        rotation_matrix = self._get_rotation_matrix_y(total_angle)

        # Start with the static sad posture for this frame
        current_points = self.sad_posture.copy()
        
        # Center of rotation is the midpoint between the hips
        pivot_center = (current_points[9] + current_points[10]) / 2

        # Apply the main rotation to all points around the pivot
        current_points = (current_points - pivot_center) @ rotation_matrix.T + pivot_center

        # 2. Secondary Motion: Simulating effort and steps
        num_steps_per_turn = 4
        
        # Vertical bobbing to simulate heavy, laborious steps
        bob_freq = num_steps_per_turn * math.pi
        bob_amp = 2.5
        bob_offset = -abs(math.sin(t * bob_freq * 2)) * bob_amp
        current_points[:, 1] += bob_offset

        # Shuffling feet to execute the turn
        step_phase = t * bob_freq * 2
        step_signal = math.sin(step_phase)
        
        lift_amp = 4.0
        step_forward_amp = 6.0

        # Alternate feet based on step_signal (positive -> right, negative -> left)
        right_foot_lift = max(0, step_signal) * lift_amp
        right_foot_forward = max(0, step_signal) * step_forward_amp
        left_foot_lift = max(0, -step_signal) * lift_amp
        left_foot_forward = max(0, -step_signal) * step_forward_amp

        # Apply lift on Y-axis
        current_points[14, 1] += right_foot_lift  # Right Ankle
        current_points[13, 1] += left_foot_lift   # Left Ankle

        # Apply forward step relative to the body's current orientation
        forward_vector = np.array([0, 0, 1]) @ rotation_matrix.T
        current_points[14] += forward_vector * right_foot_forward
        current_points[13] += forward_vector * left_foot_forward

        # 3. Kinematic Constraints: Make knees follow hips and ankles
        # Simple interpolation keeps the legs connected plausibly.
        current_points[11] = (current_points[9] + current_points[13]) / 2
        current_points[12] = (current_points[10] + current_points[14]) / 2
        # Add a slight downward offset to ensure knees are bent
        current_points[11:13, 1] -= 5
        
        return current_points

    def _project_3d_to_2d(self, points_3d):
        """Projects 3D points to 2D screen coordinates."""
        projected_points = []
        for point in points_3d:
            x, y, z = point
            scale = self.FOCAL_LENGTH / (z + self.DEPTH_OFFSET)
            px = int(x * scale + self.WIDTH / 2)
            # Y is inverted in Pygame coords, place figure lower on screen
            py = int(-y * scale + self.HEIGHT * 0.85)
            projected_points.append((px, py))
        return projected_points

    def _draw(self, screen_points):
        """Draws the scene."""
        self.screen.fill(self.BACKGROUND_COLOR)
        for point in screen_points:
            pygame.draw.circle(self.screen, self.POINT_COLOR, point, self.POINT_RADIUS)
        pygame.display.flip()

    def run(self):
        """The main animation loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update state
            current_3d_points = self._update_points()
            screen_points = self._project_3d_to_2d(current_3d_points)

            # Draw
            self._draw(screen_points)

            # Advance time
            self.frame_count += 1
            self.clock.tick(self.FPS)

        pygame.quit()


if __name__ == '__main__':
    animation = PointLightStimulus()
    animation.run()
