
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the subject and action
subject ='man'
action ='sitting down'

# Define the parameters for the animation
n_points = 1000  # Number of points in the animation
n_steps = 100  # Number of steps in the animation
dt = 0.01  # Time step
t_max = 10  # Maximum time in the animation

# Define the parameters for the point-light stimulus
num_points = 15  # Number of white point-lights
step_size = 0.1  # Step size for each point
angle_step = np.pi / 15  # Angle step for each point
angle_range = 2 * np.pi  # Range of angles for each point
step_angle = angle_range / (n_points - 1)  # Step angle for each point

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the points in the animation
x = np.zeros(n_points)
y = np.zeros(n_points)
z = np.zeros(n_points)

# Define the parameters for the motion
angle = 0
for i in range(n_steps):
    # Calculate the angle for the current point
    angle += step_angle * i

    # Calculate the x, y, and z coordinates for the current point
    x += np.sin(angle) * np.sin(angle_step * i)
    y += np.cos(angle) * np.sin(angle_step * i)
    z += np.sin(angle) * np.cos(angle_step * i)

# Plot the points in the animation
for i in range(n_points):
    ax.scatter(x[i], y[i], z[i], c='w', alpha=0.5)

# Plot the background
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_facecolor('black')

# Plot the point-light stimulus
for i in range(num_points):
    # Calculate the angle and position for the current point-light
    angle = np.radians(angle_step * i)
    x_light = np.sin(angle) * np.cos(angle_step * i)
    y_light = np.sin(angle) * np.sin(angle_step * i)
    z_light = np.cos(angle) * np.cos(angle_step * i)
    x_light = x_light * step_size
    y_light = y_light * step_size
    z_light = z_light * step_size

    # Plot the point-light
    ax.plot3D([x_light, x_light + x[i]], [y_light, y_light + y[i]], [z_light, z_light + z[i]], c='w', alpha=0.5)

# Set the axis limits and labels
ax.set_axis_off()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the animation
plt.show()
