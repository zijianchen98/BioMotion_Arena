
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15
time_steps = 200
radius = 1  # Radius of the circle to simulate turning

# Creating figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize points
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    t = frame / time_steps * 2 * np.pi
    # Calculate the positions of the points assuming they're on a circle, turning around an axis
    theta = np.linspace(0, 2 * np.pi, num_points, endpoint=False) + t
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    points.set_data(x, y)
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, time_steps),
                    init_func=init, blit=True)

plt.show()
