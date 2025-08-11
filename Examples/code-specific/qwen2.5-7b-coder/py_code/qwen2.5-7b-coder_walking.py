
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters
num_points = 15
frames = 60
walking_speed = 0.05
frame_duration = 100  # in ms

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the points
points, = ax.plot([], [], 'wo', markersize=10)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Calculate new positions based on walking motion
    theta = np.linspace(0, 2 * np.pi, num_points)
    radius = np.linspace(0.8, 0.9, num_points)
    x = radius * np.cos(theta + frame * walking_speed)
    y = radius * np.sin(theta + frame * walking_speed)
    
    points.set_data(x, y)
    return points,

ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=frame_duration)

plt.show()
