
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15          # Number of point-lights
duration = 5             # Duration of the animation in seconds
fps = 30                 # Frames per second
total_frames = duration * fps  # Total number of frames

# Initial positions of point-lights (specified for lying down posture)
# Y-coordinates represent the height, X-coordinates are spaced evenly
x_positions = np.linspace(-0.1, 0.1, num_points)
y_positions = np.linspace(-0.2, -0.2, num_points)  # Lying down on the y-axis

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(-0.2, 0.2)
ax.set_ylim(-0.5, 0.1)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=10)

# Function to update the point-lights based on a simple motion pattern
def update(frame):
    # Example motion: slight oscillation to simulate breathing
    oscillation = 0.02 * np.sin(2 * np.pi * frame / total_frames)
    y_positions = -0.2 + oscillation
    points.set_data(x_positions, y_positions)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=total_frames, blit=True, interval=1000/fps)

# Show the animation
plt.show()
