
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15
frames = 60
radius = 0.8
speed = 0.05
weight_factor = 0.5

# Initialize points
theta = np.linspace(0, 2 * np.pi, num_points)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

points, = ax.plot(x, y, 'o', markersize=10, color='white')

def update(frame):
    # Calculate new positions based on turning motion
    angle = speed * frame
    x_new = radius * np.cos(theta + angle)
    y_new = radius * np.sin(theta + angle)
    
    # Apply weight factor to simulate heaviness
    x_new += weight_factor * np.cos(2 * theta + angle)
    y_new += weight_factor * np.sin(2 * theta + angle)
    
    points.set_data(x_new, y_new)
    return points,

ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)
plt.show()
