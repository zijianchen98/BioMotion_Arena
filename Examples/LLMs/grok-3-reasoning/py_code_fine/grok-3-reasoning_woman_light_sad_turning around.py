
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial points
points = np.array([
    [0, 1.5, 0],  # head
    [0.15, 1.3, 0],  # left shoulder
    [-0.15, 1.3, 0],  # right shoulder
    [0.2, 1.0, 0],  # left elbow
    [-0.2, 1.0, 0],  # right elbow
    [0.2, 0.8, 0],  # left wrist
    [-0.2, 0.8, 0],  # right wrist
    [0.1, 1.0, 0],  # left hip
    [-0.1, 1.0, 0],  # right hip
    [0.1, 0.5, 0],  # left knee
    [-0.1, 0.5, 0],  # right knee
    [0.1, 0.1, 0],  # left ankle
    [-0.1, 0.1, 0],  # right ankle
    [0.1, 0.0, 0.05],  # left toe
    [-0.1, 0.0, 0.05]  # right toe
])

# Number of frames
num_frames = 60

# Function to rotate points around y-axis
def rotate_y(points, theta):
    rotation_matrix = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return points @ rotation_matrix.T

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0, 1.8)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

# Initialize scatter plot
scatter = ax.scatter([], [], color='white', s=20)

# Update function for animation
def update(frame):
    theta = frame * (np.pi / num_frames)
    rotated_points = rotate_y(points, theta)
    x = rotated_points[:, 0]
    y = rotated_points[:, 1]
    scatter.set_offsets(np.c_[x, y])
    return scatter,

# Create animation
anim = FuncAnimation(fig, update, frames=num_frames, interval=33, blit=True)
plt.show()
