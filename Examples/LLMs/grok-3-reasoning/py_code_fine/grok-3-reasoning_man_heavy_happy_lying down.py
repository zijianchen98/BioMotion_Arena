
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define lying down positions
lying_positions = np.array([
    [1.8, 0],  # head
    [1.7, 0],  # neck
    [1.5, -0.15],  # left shoulder
    [1.5, 0.15],  # right shoulder
    [1.3, -0.25],  # left elbow
    [1.3, 0.25],  # right elbow
    [1.1, -0.35],  # left wrist
    [1.1, 0.35],  # right wrist
    [1.2, 0],  # torso center
    [1.0, -0.1],  # left hip
    [1.0, 0.1],  # right hip
    [0.6, -0.1],  # left knee
    [0.6, 0.1],  # right knee
    [0.2, -0.1],  # left ankle
    [0.2, 0.1]   # right ankle
])

# Set up figure and axes
fig, ax = plt.subplots()
fig.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.5, 2.0)
ax.set_ylim(-0.5, 0.5)
ax.set_aspect('equal')

# Create scatter plot
points = ax.scatter([], [], color='white', s=100)

# Define update function
def update(frame):
    positions = lying_positions.copy()
    # Add motion to wrists
    theta = 2 * np.pi * frame / 20  # period of 20 frames
    positions[6,0] += 0.1 * np.sin(theta)  # left wrist x
    positions[6,1] += 0.1 * np.cos(theta)  # left wrist y
    positions[7,0] += 0.1 * np.sin(theta)  # right wrist x
    positions[7,1] += 0.1 * np.cos(theta)  # right wrist y
    points.set_offsets(positions)
    return points,

# Set total frames
total_frames = 100

# Create animation
ani = FuncAnimation(fig, update, frames=range(total_frames), interval=50, blit=True)

# Show animation
plt.show()
