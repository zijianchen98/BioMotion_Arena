
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define base positions of the 15 points
positions = np.array([
    [0, 0],     # head
    [1.5, 0],   # sternum
    [1, 1],     # left shoulder
    [1.5, 1.5], # left elbow
    [2, 1.5],   # left wrist
    [1, -1],    # right shoulder
    [1.5, -1.5],# right elbow
    [2, -1.5],  # right wrist
    [2, 0],     # torso
    [3, 0.5],   # left hip
    [4, 0.5],   # left knee
    [5, 0.5],   # left ankle
    [3, -0.5],  # right hip
    [4, -0.5],  # right knee
    [5, -0.5]   # right ankle
])

# Parameters for movement
amplitude_head = 0.1
frequency_head = 0.1  # Hz
amplitude_breathe = 0.05
frequency_breathe = 0.25  # Hz
fps = 30
n_frames = 300  # 10 seconds

# Set up figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 6)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Plot points
points, = ax.plot([], [], 'o', color='white', markersize=5)

# Update function for animation
def update(frame):
    t = frame / fps
    current_positions = positions.copy()
    # Update head x-position
    current_positions[0, 0] += amplitude_head * np.sin(2 * np.pi * frequency_head * t)
    # Update sternum and torso y-position for breathing
    breathe_offset = amplitude_breathe * np.sin(2 * np.pi * frequency_breathe * t)
    current_positions[1, 1] += breathe_offset
    current_positions[8, 1] += breathe_offset
    points.set_data(current_positions[:, 0], current_positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=1000/fps, blit=True)

plt.show()
