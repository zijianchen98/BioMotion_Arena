
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters for the subject and action
subject_x, subject_y = 0, 0
subject_z = 0
subject_angle = 0
subject_roll = 0

# Define the parameters for the point-light stimulus
light_x, light_y, light_z = 0, 0, 0
light_w = 1
light_f = 0.1
light_s = 1

# Define the parameters for the action
action_x, action_y = 0, 0
action_z = 0
action_angle = 0
action_roll = 0

# Define the parameters for the animation
num_points = 100
num_steps = 100
dt = 0.01
t_end = 10

# Create a figure and a 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize arrays to store the positions and angles of the points
x = np.zeros(num_points)
y = np.zeros(num_points)
z = np.zeros(num_points)
theta = np.zeros(num_points)
phi = np.zeros(num_points)

# Set the initial positions and angles of the points
for i in range(num_points):
    x[i] = subject_x + (subject_x - subject_y) * dt + (subject_y - subject_z) * dt * np.sin(subject_angle) + (subject_z - subject_y) * dt * np.cos(subject_angle)
    y[i] = subject_y + (subject_x - subject_y) * dt + (subject_y - subject_z) * dt * np.cos(subject_angle) - (subject_z - subject_y) * dt * np.sin(subject_angle)
    z[i] = subject_z + (subject_x - subject_y) * dt * np.sin(subject_angle) + (subject_y - subject_z) * dt * np.cos(subject_angle)
    theta[i] = subject_angle + (action_angle - action_roll) * dt
    phi[i] = np.arctan2(subject_y - subject_z, subject_x - subject_y)

# Set the initial positions of the lights
light_x[::10] = np.linspace(0, 10, 10)
light_y[::10] = np.linspace(0, 10, 10)
light_z[::10] = np.linspace(0, 10, 10)
light_positions = np.array([light_x, light_y, light_z])

# Set the initial colors of the lights
light_colors = np.ones((10, 3))
light_colors[:, 0] = np.linspace(0, 1, 10)
light_colors[:, 1] = np.linspace(0, 1, 10)
light_colors[:, 2] = np.linspace(0, 1, 10)

# Function to update the positions of the points and lights
def update():
    global x, y, z, theta, phi
    for i in range(num_points):
        x[i] = subject_x + (subject_x - subject_y) * dt + (subject_y - subject_z) * dt * np.sin(subject_angle) + (subject_z - subject_y) * dt * np.cos(subject_angle)
        y[i] = subject_y + (subject_x - subject_y) * dt + (subject_y - subject_z) * dt * np.cos(subject_angle) - (subject_z - subject_y) * dt * np.sin(subject_angle)
        z[i] = subject_z + (subject_x - subject_y) * dt * np.sin(subject_angle) + (subject_y - subject_z) * dt * np.cos(subject_angle)
        theta[i] = subject_angle + (action_angle - action_roll) * dt
        phi[i] = np.arctan2(subject_y - subject_z, subject_x - subject_y)
        light_positions[:, 0] = np.linspace(0, 10, 10)
        light_positions[:, 1] = np.linspace(0, 10, 10)
        light_positions[:, 2] = np.linspace(0, 10, 10)
        light_colors[:, 0] = np.linspace(0, 1, 10)
        light_colors[:, 1] = np.linspace(0, 1, 10)
        light_colors[:, 2] = np.linspace(0, 1, 10)
        ax.clear()
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        ax.set_zlim(-15, 15)
        ax.set_axis_off()
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        ax.set_zlim(-15, 15)
        ax.set_axis_off()
        for j in range(10):
            for k in range(10):
                ax.scatter(light_positions[j, k], light_colors[j, k], c='w')
        ax.scatter(x[i], y[i], z[i], c='r')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.draw()
        plt.pause(dt)

# Run the animation
for i in range(num_steps):
    update()

# Close the plot
plt.show()
