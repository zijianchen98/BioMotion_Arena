
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the 3D coordinates of the 15 point lights
num_points = 15
light_positions = np.zeros((num_points, 3))

# Assign positions to the lights to form a rolling motion
for i in range(num_points):
    light_positions[i, 0] = np.sin(2 * np.pi * i / num_points) * 2  # x-coordinate
    light_positions[i, 1] = np.cos(2 * np.pi * i / num_points) * 2  # y-coordinate
    light_positions[i, 2] = 0  # z-coordinate

# Define the 3D coordinates of the sadman's body
body_positions = np.zeros((10, 3))

# Assign positions to the body parts to form a rolling motion
for i in range(10):
    body_positions[i, 0] = np.sin(2 * np.pi * i / 10) * 2  # x-coordinate
    body_positions[i, 1] = np.cos(2 * np.pi * i / 10) * 2  # y-coordinate
    body_positions[i, 2] = 0  # z-coordinate

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.set_facecolor('black')

    # Update the light positions to create a rolling motion
    light_positions[:, 0] = np.sin(2 * np.pi * (i + np.arange(num_points)) / num_points) * 2
    light_positions[:, 1] = np.cos(2 * np.pi * (i + np.arange(num_points)) / num_points) * 2

    # Plot the lights
    ax.scatter(light_positions[:, 0], light_positions[:, 1], light_positions[:, 2], c='white')

    # Plot the body parts
    ax.plot(body_positions[:, 0], body_positions[:, 1], body_positions[:, 2], c='white')

# Create a new figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the animation
ani = animation.FuncAnimation(fig, animate, frames=200, blit=False, interval=50)

# Show the animation
plt.show()
