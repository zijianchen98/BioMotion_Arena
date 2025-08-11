
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frame_rate = 30
duration = 5  # in seconds
frames = frame_rate * duration

# Body parts and their relative positions (simplified)
body_parts = ['head', 'torso', 'left_shoulder', 'right_shoulder',
              'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
              'left_hip', 'right_hip', 'left_knee', 'right_knee',
              'left_ankle', 'right_ankle', 'tail']

# Initial positions of the point-lights
positions = {
    'head': np.array([0.5, 0.9]),
    'torso': np.array([0.5, 0.7]),
    'left_shoulder': np.array([0.4, 0.8]),
    'right_shoulder': np.array([0.6, 0.8]),
    'left_elbow': np.array([0.3, 0.6]),
    'right_elbow': np.array([0.7, 0.6]),
    'left_wrist': np.array([0.2, 0.5]),
    'right_wrist': np.array([0.8, 0.5]),
    'left_hip': np.array([0.4, 0.5]),
    'right_hip': np.array([0.6, 0.5]),
    'left_knee': np.array([0.4, 0.3]),
    'right_knee': np.array([0.6, 0.3]),
    'left_ankle': np.array([0.4, 0.1]),
    'right_ankle': np.array([0.6, 0.1]),
    'tail': np.array([0.5, 0.0])
}

# Animation function
def update(frame):
    for part in body_parts:
        if part == 'right_wrist':
            positions[part][0] += 0.01 * np.sin(frame / 5)
        elif part == 'left_wrist':
            positions[part][0] -= 0.01 * np.sin(frame / 5)
    scat.set_offsets(list(positions.values()))

# Setting up the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide the axes
scat = ax.scatter([], [], s=50, color='white')

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/frame_rate)

plt.show()
