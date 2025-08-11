
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames and points
num_frames = 60
num_points = 15

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Clear the previous frame
    points.set_data([], [])
    
    # Calculate new positions for the points
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    radius = 0.8 + 0.2 * np.sin(np.linspace(0, 2 * np.pi * frame / num_frames, num_points))
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    
    # Update the points
    points.set_data(x, y)
    
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True)

# Show the animation
plt.show()
