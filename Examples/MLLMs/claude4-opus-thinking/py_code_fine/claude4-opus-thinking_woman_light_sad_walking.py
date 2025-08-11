
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set the number of point-lights and number of frames
num_points = 15
num_frames = 60

# Configuration for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Define the coordinates for the point-lights
initial_coords = np.array([
    [0, 1],    # head
    [-0.5, 0.5], [0.5, 0.5], # shoulders
    [-0.7, 0], [0.7, 0],     # upper arms
    [-0.5, -0.5], [0.5, -0.5],# elbows
    [-0.3, -1], [0.3, -1],   # hips
    [-0.4, -1.5], [0.4, -1.5],# knees
    [-0.2, -2], [0.2, -2]    # feet
])

# Function to update the points for each frame
def update(frame):
    # Simulated walking motion with vertical shifts and slight lateral shifting
    y_shift = 0.1 * np.sin(2 * np.pi * (frame / num_frames))  # Oscillation effect for walking
    x_shift = 0.05 * np.cos(4 * np.pi * (frame / num_frames))  # Side to side movement
    new_coords = initial_coords + np.array([x_shift, y_shift])
    points.set_data(new_coords[:, 0], new_coords[:, 1])
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
