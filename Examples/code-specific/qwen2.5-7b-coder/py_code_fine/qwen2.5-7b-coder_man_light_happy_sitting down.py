
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and frames
num_points = 15
num_frames = 60

# Create a figure and axis for the plot
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
    
    # Generate new positions for the points
    angles = np.linspace(0, 2 * np.pi, num_points + 1)[:-1]
    radius = 0.8 - frame / num_frames * 0.4
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    
    # Update the points' positions
    points.set_data(x, y)
    
    return points,

# Create the animation
ani = FuncAnimation(fig, update, init_func=init, frames=num_frames, interval=50, blit=True)

plt.show()
