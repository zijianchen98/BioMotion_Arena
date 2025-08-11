
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions of the 15 points in 3D
points_initial = np.array([
    [0, 0.5, 0],  # head
    [0, 0.4, 0],  # neck
    [-0.1, 0.35, -0.05],  # left shoulder
    [0.1, 0.35, 0.05],  # right shoulder
    [-0.15, 0.25, -0.05],  # left elbow
    [0.15, 0.25, 0.05],  # right elbow
    [-0.15, 0.15, -0.05],  # left wrist
    [0.15, 0.15, 0.05],  # right wrist
    [0, 0, 0],  # pelvis
    [-0.05, -0.05, -0.02],  # left hip
    [0.05, -0.05, 0.02],  # right hip
    [-0.05, -0.25, -0.02],  # left knee
    [0.05, -0.25, 0.02],  # right knee
    [-0.05, -0.45, -0.02],  # left ankle
    [0.05, -0.45, 0.02],  # right ankle
])

def rotate_points(points, theta):
    # Rotation matrix for rotation around y-axis
    rotation_matrix = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return points @ rotation_matrix

# Set up the figure and axis
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.2, 0.2)
ax.set_ylim(-0.5, 0.6)
ax.set_aspect('equal')
ax.set_axis_off()

# Create scatter plot for the points
scatter = ax.scatter(points_initial[:, 0], points_initial[:, 1], color='white', s=10)

# Animation update function
def update(frame):
    theta = (frame / 60) * np.pi  # Rotate from 0 to pi over 60 frames
    rotated_points = rotate_points(points_initial, theta)
    scatter.set_offsets(rotated_points[:, :2])
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=60, interval=33, blit=True)

plt.show()
