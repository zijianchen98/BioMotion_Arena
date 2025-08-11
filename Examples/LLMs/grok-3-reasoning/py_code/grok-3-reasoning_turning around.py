
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define initial points (x, y) with z=0 implied
points = np.array([
    [0, 1],    # head
    [0, 0.85], # neck
    [0, 0.6],  # torso center
    [0.15, 0.75], # left shoulder
    [-0.15, 0.75], # right shoulder
    [0.2, 0.5], # left elbow
    [-0.2, 0.5], # right elbow
    [0.25, 0.3], # left wrist
    [-0.25, 0.3], # right wrist
    [0.1, 0.5], # left hip
    [-0.1, 0.5], # right hip
    [0.1, 0.25], # left knee
    [-0.1, 0.25], # right knee
    [0.1, 0], # left ankle
    [-0.1, 0], # right ankle
])

# Set up figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-0.3, 0.3)
ax.set_ylim(0, 1.1)
ax.set_aspect('equal')
ax.axis('off')

# Create scatter plot for point-lights
scatter = ax.scatter(points[:, 0], points[:, 1], color='white', s=10)

# Animation parameters
delta_theta = np.pi / 40  # Angular step per frame

def update(frame):
    theta = frame * delta_theta
    new_x = points[:, 0] * np.cos(theta)
    scatter.set_offsets(np.c_[new_x, points[:, 1]])
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(1000), interval=50, repeat=True)

plt.show()
