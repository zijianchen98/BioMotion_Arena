
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions of the 15 points
initial_positions = np.array([
    [-0.1, 0],   # left ankle
    [0.1, 0],    # right ankle
    [-0.1, 0.4], # left knee
    [0.1, 0.4],  # right knee
    [-0.1, 0.8], # left hip
    [0.1, 0.8],  # right hip
    [0, 0.8],    # waist
    [0, 1.2],    # neck
    [0, 1.4],    # head
    [-0.2, 1.2], # left shoulder
    [0.2, 1.2],  # right shoulder
    [-0.3, 1.0], # left elbow
    [0.3, 1.0],  # right elbow
    [-0.4, 0.8], # left wrist
    [0.4, 0.8]   # right wrist
])

# Indices of fixed and rotating points
fixed_indices = list(range(0, 7))
rotating_indices = list(range(7, 15))

# Waist position
waist_x, waist_y = 0, 0.8

# Maximum rotation angle (in radians)
theta_max = np.pi / 3  # 60 degrees

# Function to rotate a point around the waist
def rotate_point(x, y, theta):
    x_rel = x - waist_x
    y_rel = y - waist_y
    x_rot = x_rel * np.cos(theta) - y_rel * np.sin(theta) + waist_x
    y_rot = x_rel * np.sin(theta) + y_rel * np.cos(theta) + waist_y
    return x_rot, y_rot

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.set_facecolor('black')
ax.set_xlim(-0.7, 0.7)
ax.set_ylim(0, 1.5)
ax.axis('off')

# Initial scatter plot
initial_x = initial_positions[:, 0]
initial_y = initial_positions[:, 1]
scatter = ax.scatter(initial_x, initial_y, color='white', s=50)

# Update function for animation
def update(frame):
    t = frame / 100  # Assuming 100 frames for the cycle
    theta = -theta_max * np.sin(np.pi * t)
    x = np.copy(initial_x)
    y = np.copy(initial_y)
    for i in rotating_indices:
        x[i], y[i] = rotate_point(initial_x[i], initial_y[i], theta)
    offsets = np.column_stack((x, y))
    scatter.set_offsets(offsets)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
