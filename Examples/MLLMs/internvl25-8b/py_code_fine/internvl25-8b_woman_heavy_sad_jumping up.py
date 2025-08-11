
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class SadWomanJumping:
    def __init__(self):
        self.num_joints = 15
        self.joint_positions = np.zeros((self.num_joints, 2))
        self.set_joint_positions()

    def set_joint_positions(self):
        points = [
            [0.1, 0.8], [0.3, 0.5], [0.0, 0.3], [0.2, 0.2], [0.35, 0.05],
            [0.2, 0.0], [0.1, 0.1], [0.0, 0.5], [0.3, 0.85], [0.18, 0.2],
            [0.38, 0.15], [0.5, 0.15], [0.45, 0.05], [0.25, 0.3], [0.08, 0.8]
        ]
        for i in range(self.num_joints):
            self.joint_positions[i] = points[i]

    def draw(self, line_objects):
        line_objects.clear()
        line_objects.append([self.joint_positions[i] for i in range(self.num_joints)])
        line_objects[-1].style = {
           'marker': 'o',
           'markersize': 3,
           'markerfacecolor': 'white',
            'alpha': 1.0,
           'markeredgecolor': 'none'
        }
        line_objects[-1].line.set_color('white')
        line_objects[-1].line.set_linewidth(1)
        if np.all(self.joint_positions == 0):
            line_objects[-1].line.set_visible(False)
        else:
            line_objects[-1].line.set_visible(True)

    def update(self, frame):
        for i in range(1, self.num_joints - 1):
            self.joint_positions[i][0] = np.sin(2 * np.pi * frame / 40 + 2 * np.pi * i / 15) * 0.4 + 0.5
            self.joint_positions[i][1] = 0.95 * np.sin(2 * np.pi * frame / 40 + 2 * np.pi * i / 15) + 0.10
        return self.joint_positions

# Create figure
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', 'box')
ax.set_axis_off()

# Initialize the jump
line_objects = []

# Instantiate the sad woman jumping object
sad_woman = SadWomanJumping()

# Setup the animation
ani = animation.FuncAnimation(
    fig, sad_woman.update, frames=200, fargs=(), init_func=sad_woman.set_joint_positions, 
    blit=False, repeat=True, repeat_delay=200, interval=20, repeat=False, save_count=True)

# Show the animation
plt.show()
