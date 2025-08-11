
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters
n_points = 100
x = np.linspace(-10, 10, n_points)
y = np.linspace(-10, 10, n_points)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create a figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the axis limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

# Define the point-light source parameters
source_radius = 1
source_distance = 10

# Create the point-lights
for i in range(15):
    angle = i * np.pi / 8
    x_light = source_distance * np.cos(angle)
    y_light = source_distance * np.sin(angle)
    z_light = 0
    light = np.array([x_light, y_light, z_light])
    ax.plot3D(*zip(X[i], Y[i], Z[i]), c='w')

# Set the camera position and orientation
ax.view_init(elev=30, azim=0)

# Animate the point-lights
for i in range(100):
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)
    for j in range(15):
        angle = j * np.pi / 8
        x_light = source_distance * np.cos(angle + i * np.pi / 50)
        y_light = source_distance * np.sin(angle + i * np.pi / 50)
        z_light = 0
        light = np.array([x_light, y_light, z_light])
        ax.plot3D(*zip(X[j], Y[j], Z[j]), c='w')
    plt.pause(0.02)

plt.show()
