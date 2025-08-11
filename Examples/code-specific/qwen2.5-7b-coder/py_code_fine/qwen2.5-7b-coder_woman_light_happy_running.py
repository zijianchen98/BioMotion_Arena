
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and frames
num_points = 15
num_frames = 60

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point lights
points, = ax.plot([], [], 'o', markersize=5, color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Calculate new positions based on running motion
    t = frame / num_frames * 4 * np.pi  # Time parameter
    x = np.sin(t + np.linspace(0, 2 * np.pi, num_points))
    y = np.cos(t + np.linspace(0, 2 * np.pi, num_points)) * 0.5
    
    points.set_data(x, y)
    return points

ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True)

plt.show()
