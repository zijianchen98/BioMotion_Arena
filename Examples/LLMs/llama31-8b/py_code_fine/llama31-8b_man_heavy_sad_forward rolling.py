
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters
num_points = 15
num_frames = 100
time_step = 0.01
radius = 0.5

# Define the initial positions and velocities of the points
theta = np.linspace(0, 2*np.pi, num_points)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
z = np.zeros(num_points)
vx = np.zeros(num_points)
vy = np.zeros(num_points)
vz = np.zeros(num_points)

# Define the forward rolling motion
for i in range(num_frames):
    for j in range(num_points):
        # Rotate the points around the y-axis
        x[j] = radius * np.cos(theta[j] + 0.01*i)
        y[j] = radius * np.sin(theta[j] + 0.01*i)
        # Move the points forward
        z[j] += 0.01
        # Limit the z position to prevent points from moving off-screen
        if z[j] > 2:
            z[j] = 2
    # Update the plot
    plt.clf()
    ax = plt.subplot(111, projection='3d')
    ax.set_axis_off()
    ax.scatter(x, y, z, c='w', s=100)
    plt.draw()
    plt.pause(time_step)

plt.show()
