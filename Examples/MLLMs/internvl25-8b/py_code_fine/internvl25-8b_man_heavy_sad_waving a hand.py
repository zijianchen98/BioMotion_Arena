
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points
num_points = 15
width = 600
height = 400

fig, ax = plt.subplots(figsize=(width/100, height/100))
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.axis('off')

# Set initial positions
points = np.zeros((num_points, 3))
points[:, 0] = width // 2  # x-coordinates in center
points[:, 1] = height // 2  # y-coordinates in center
points[:, 2] = np.linspace(0, 1, num_points)

# Define the wave speed and wave speed in z
wave_factor_z = np.linspace(0.05, 0.1, num_points)
wave_factor_y = np.copy(wave_factor_z)

def init():
    ax.clear()
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis('off')

def animate(i):
    global points

    # Update x coordinate with simple wave motion
    if i % 2 == 0:  # Adjust for smooth vertical wave motion
        points[:, 0] = width // 2 + np.sin(points[:, 2] + i * 0.01)
    else:
        points[:, 0] = width // 2 + np.sin(points[:, 2] + i * 0.02)

    # Update y coordinate with slight back and forth motion
    points[:, 1] = 0.5 + wave_factor_y[i] * np.sin(0.015 * i)

    # Update z coordinate for depth
    points[:, 2] = np.sin(wave_factor_z[i] * i * 0.05)

    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='white', s=1)

ani = FuncAnimation(fig, animate, init_func=init, frames=200, interval=50)

plt.show()
