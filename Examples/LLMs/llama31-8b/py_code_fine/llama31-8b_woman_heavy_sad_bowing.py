
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define the 3D coordinates of the point lights
num_lights = 15
lights = np.random.rand(num_lights, 3) * 2 - 1  # Randomly position the lights within a 2x2x2 cube

# Define the action: bowing
def bowing(t):
    # Move the lights in a smooth, natural motion
    x, y, z = lights.T
    x = 0.5 * np.sin(2 * np.pi * 0.5 * t) + 0.5  # Move the lights in a sinusoidal motion along the x-axis
    y = 0.5 * np.sin(2 * np.pi * 0.7 * t) + 0.5  # Move the lights in a sinusoidal motion along the y-axis
    z = 0.5 * np.sin(2 * np.pi * 0.9 * t) + 0.5  # Move the lights in a sinusoidal motion along the z-axis
    return np.column_stack((x, y, z))

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the plot
ax.set_axis_off()
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_zlim(-1.1, 1.1)
ax.view_init(azim=120)  # Set the initial camera angle

# Animate the points
def animate(i):
    ax.clear()
    ax.set_axis_off()
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_zlim(-1.1, 1.1)
    ax.view_init(azim=120)  # Keep the camera angle constant
    points = bowing(i)
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=50, c='w', marker='o')

ani = animation.FuncAnimation(fig, animate, frames=range(0, 100, 2), interval=20, blit=False)

plt.show()
