
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions and connections for a bowing human stick figure
class PointLightAnimator:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_facecolor('black')
        self.ax.set_xlim(-1.5, 1.5)
        self.ax.set_ylim(-1.5, 2.0)
        self.ax.axis('off')

        # Initial joint coordinates (15 points: head, torso, shoulders, elbows, wrists, hips, knees, ankles)
        self.joints = np.array([
            [0, 1.8],    # Head
            [0, 1.5],    # Neck
            [-0.5, 1.4], # Left shoulder
            [-0.8, 1.0], # Left elbow
            [-1.0, 0.6], # Left wrist
            [0.5, 1.4],  # Right shoulder
            [0.8, 1.0],  # Right elbow
            [1.0, 0.6],  # Right wrist
            [0, 1.0],    # Spine top
            [0, 0.5],    # Spine bottom
            [-0.2, 0.5], # Left hip
            [-0.3, 0.0], # Left knee
            [-0.4, -0.5],# Left ankle
            [0.2, 0.5],  # Right hip
            [0.3, 0.0],  # Right knee
            [0.4, -0.5]  # Right ankle
        ])

        self.points, = self.ax.plot([], [], 'wo', markersize=10)
        self.lines = [self.ax.plot([], [], 'w-')[0] for _ in range(8)]  # Connections
        self.frame = 0
        self.max_frames = 60  # Total frames for one bowing cycle

    def init(self):
        self.points.set_data([], [])
        for line in self.lines:
            line.set_data([], [])
        return self.points, *self.lines

    def update(self, frame):
        # Parameter for bowing motion (0 to 1 then back to 0)
        t = abs((frame % self.max_frames) / self.max_frames - 0.5) * 2
        # Bowing: bend at hips and spine
        angle = t * np.pi / 6  # Max bend ~30 degrees
        spine_angle = t * np.pi / 8  # Slight spine curve

        # Rotate lower body
        rot_lower = np.array([[np.cos(angle), -np.sin(angle)],
                             [np.sin(angle), np.cos(angle)]])
        upper_body = self.joints[0:9]  # Head to spine top
        lower_body = self.joints[9:]   # Spine bottom to ankles

        # Apply rotation to lower body around spine bottom
        center = self.joints[9]
        lower_body -= center
        lower_body = np.dot(lower_body, rot_lower)
        lower_body += center

        # Apply spine curve
        spine_shift = np.sin(spine_angle) * np.linspace(0, 0.3, 5)
        upper_body[2:7, 1] += spine_shift[1:6]  # Affect shoulders to spine top

        # Combine and update joints
        self.joints = np.vstack((upper_body, lower_body))

        self.points.set_data(self.joints[:, 0], self.joints[:, 1])

        # Define connections (simplified for bowing figure)
        connections = [
            (0, 1), (1, 2), (2, 3), (3, 4),  # Head to left arm
            (1, 5), (5, 6), (6, 7),          # Head to right arm
            (1, 8), (8, 9), (9, 10), (10, 11), (11, 12),  # Torso to left leg
            (9, 13), (13, 14), (14, 15)      # Torso to right leg
        ]
        for i, (start, end) in enumerate(connections):
            self.lines[i].set_data(self.joints[[start, end], 0], self.joints[[start, end], 1])

        return self.points, *self.lines

# Create and display animation
animator = PointLightAnimator()
ani = FuncAnimation(animator.fig, animator.update, frames=range(animator.max_frames),
                    init_func=animator.init, blit=True, interval=50, repeat=True)

plt.show()
