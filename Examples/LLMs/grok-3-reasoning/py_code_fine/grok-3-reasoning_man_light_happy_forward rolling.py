
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Define key frames for the animation
# Each key frame is a list of (x, y) positions for the 15 points

# Standing position
points0 = np.array([
    [0, 1.0],   # head
    [0, 0.9],   # neck
    [-0.1, 0.8],# left shoulder
    [0.1, 0.8], # right shoulder
    [-0.15, 0.7],# left elbow
    [0.15, 0.7],# right elbow
    [-0.2, 0.6],# left wrist
    [0.2, 0.6], # right wrist
    [0, 0.5],   # pelvis
    [-0.05, 0.5],# left hip
    [0.05, 0.5],# right hip
    [-0.05, 0.3],# left knee
    [0.05, 0.3],# right knee
    [-0.05, 0.1],# left ankle
    [0.05, 0.1] # right ankle
])

# Hands on ground position
points1 = np.array([
    [0.5, 0.1],  # head tucked in
    [0.4, 0.2],  # neck
    [0.3, 0.3],  # left shoulder
    [0.5, 0.3],  # right shoulder
    [0.4, 0.1],  # left elbow
    [0.6, 0.1],  # right elbow
    [0.5, 0.0],  # left wrist on ground
    [0.7, 0.0],  # right wrist on ground
    [0.2, 0.4],  # pelvis raised
    [0.15, 0.4], # left hip
    [0.25, 0.4], # right hip
    [0.1, 0.3],  # left knee bent
    [0.3, 0.3],  # right knee bent
    [0.05, 0.1], # left ankle
    [0.35, 0.1]  # right ankle
])

# Mid-roll position
points2 = np.array([
    [1.0, 0.5],  # head
    [0.9, 0.6],  # neck
    [0.8, 0.7],  # left shoulder
    [1.0, 0.7],  # right shoulder
    [0.9, 0.8],  # left elbow
    [1.1, 0.8],  # right elbow
    [0.8, 0.9],  # left wrist
    [1.2, 0.9],  # right wrist
    [0.7, 0.5],  # pelvis
    [0.65, 0.5], # left hip
    [0.75, 0.5], # right hip
    [0.6, 0.6],  # left knee
    [0.8, 0.6],  # right knee
    [0.5, 0.7],  # left ankle
    [0.9, 0.7]   # right ankle
])

# Finishing position (shifted standing position)
points3 = points0 + [1, 0]

# Function to interpolate positions based on time t (0 to 1)
def get_positions(t):
    if t < 1/3:
        factor = t / (1/3)
        points = points0 + factor * (points1 - points0)
    elif t < 2/3:
        factor = (t - 1/3) / (1/3)
        points = points1 + factor * (points2 - points1)
    else:
        factor = (t - 2/3) / (1/3)
        points = points2 + factor * (points3 - points2)
    return points

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(0, 1.2)
ax.set_aspect('equal')

# Create scatter plot for points
scatter = ax.scatter([], [], color='white', s=50)

# Update function for animation
def update(frame):
    t = frame / 100  # Normalize time to [0,1]
    positions = get_positions(t)
    scatter.set_offsets(positions)
    return scatter,

# Create animation
animation = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
