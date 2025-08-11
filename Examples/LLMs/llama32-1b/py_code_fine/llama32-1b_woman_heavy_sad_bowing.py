
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define the parameters for the point-light stimulus
num_points = 15
x_range = np.linspace(-10, 10, num_points)
y_range = np.linspace(-10, 10, num_points)
x_range, y_range = np.meshgrid(x_range, y_range)
z_range = np.linspace(-5, 5, num_points)

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the point-light stimulus
def point_light(x, y, z):
    return np.array([x, y, z])

# Function to generate the stimulus
def generate_stimulus(x_range, y_range, z_range):
    return np.array([point_light(x, y, z) for x, y, z in zip(x_range, y_range, z_range)])

# Generate the stimulus
stimulus = generate_stimulus(x_range, y_range, z_range)

# Define the action
def action(x, y, z):
    return np.array([1, 1, 0])  # Heavy weight is represented by a positive y-value

# Define the subject
def subject(x, y, z):
    return np.array([1, 0, 0])  # The woman is represented by a positive x-value

# Define the parameters for the animation
param_range = np.linspace(0, 10, 100)
x = param_range
y = param_range
z = param_range

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the axis
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-5, 5)

# Initialize the point-light stimulus
ax.scatter(0, 0, 0, c=stimulus, s=0.1, alpha=0.5)

# Initialize the action and subject
ax.scatter(0, 0, 0, c=action, s=0.1, alpha=0.5)
ax.scatter(0, 0, 0, c=subject, s=0.1, alpha=0.5)

# Define the animation function
def animate(i):
    # Update the parameters
    param_range = np.linspace(i / 10, (i + 1) / 10, 100)
    x = param_range
    y = param_range
    z = param_range

    # Update the point-light stimulus
    stimulus = generate_stimulus(x_range, y_range, z_range)
    ax.scatter(0, 0, 0, c=stimulus, s=0.1, alpha=0.5)

    # Update the action and subject
    ax.scatter(0, 0, 0, c=action, s=0.1, alpha=0.5)
    ax.scatter(0, 0, 0, c=subject, s=0.1, alpha=0.5)

    return ax,

# Animate the stimulus
ani = animation.FuncAnimation(fig, animate, frames=len(param_range), interval=20)

# Show the animation
plt.show()
