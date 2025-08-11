
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters
num_points = 15
angle_step = 0.1
time_step = 0.03
frames = int(2 * np.pi / angle_step)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the points
points, = ax.plot([], [], 'wo', markersize=5)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    angles = np.linspace(0, 2 * np.pi, num_points + 1)[:-1]
    radius = 0.8 - frame / frames * 0.6
    x = radius * np.cos(angles + frame * angle_step)
    y = radius * np.sin(angles + frame * angle_step)
    points.set_data(x, y)
    return points,

ani = FuncAnimation(fig, update, frames=frames, interval=int(time_step * 1000), blit=True, init_func=init)
plt.show()
