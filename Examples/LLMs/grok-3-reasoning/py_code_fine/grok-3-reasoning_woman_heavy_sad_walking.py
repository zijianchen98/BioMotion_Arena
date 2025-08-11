
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
T = 3.0  # period in seconds for slower walk
fps = 30  # frames per second
dt = 1.0 / fps

# Average positions of the 15 points
points_avg = np.array([
    [0, 1.4],  # head (slightly lowered)
    [-0.2, 1.3],  # left shoulder
    [0.2, 1.3],  # right shoulder
    [-0.2, 1.0],  # left elbow
    [0.2, 1.0],  # right elbow
    [-0.2, 0.7],  # left wrist
    [0.2, 0.7],  # right wrist
    [-0.1, 0.9],  # left hip
    [0.1, 0.9],  # right hip
    [-0.1, 0.5],  # left knee
    [0.1, 0.5],  # right knee
    [-0.1, 0.1],  # left ankle
    [0.1, 0.1],  # right ankle
    [-0.1, 0.0],  # left toe
    [0.1, 0.0]   # right toe
])

# Amplitudes and phases for x and y oscillations
a_x = np.array([0, 0, 0, 0.025, 0.025, 0.05, 0.05, 0, 0, 0.1, 0.1, 0.15, 0.15, 0.15, 0.15])
phi_x = np.array([0, 0, 0, np.pi, 0, np.pi, 0, 0, 0, 0, np.pi, 0, np.pi, 0, np.pi])
a_y = np.array([0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.03, 0.03, 0.05, 0.05, 0.03, 0.03])
phi_y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, np.pi, 0, np.pi, 0, np.pi])

# Function to compute positions at time t
def get_positions(t):
    omega = 2 * np.pi / T
    x = points_avg[:, 0] + a_x * np.sin(omega * t + phi_x)
    y = points_avg[:, 1] + a_y * np.sin(omega * t + phi_y) + 0.1 * np.sin(2 * omega * t)  # global vertical oscillation
    return x, y

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0, 1.6)
scatter = ax.scatter([], [], color='white', s=50)

# Update function for animation
def update(frame):
    t = (frame * dt) % T
    x, y = get_positions(t)
    scatter.set_offsets(np.c_[x, y])
    return scatter,

# Create animation
animation = FuncAnimation(fig, update, interval=1000 / fps)

plt.show()
