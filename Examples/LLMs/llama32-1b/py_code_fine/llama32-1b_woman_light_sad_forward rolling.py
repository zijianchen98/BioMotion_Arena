
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)

# Define the subject's movement parameters
SUBJECT_SPEED = 0.5
SUBJECT_SPEED_VEL = 0.1
SUBJECT_ACCELERATION = 0.1
SUBJECT_ACCELERATION_VEL = 0.01

# Define the action parameters
ACTION_SPEED = 0.5
ACTION_SPEED_VEL = 0.1
ACTION_ACCELERATION = 0.1
ACTION_ACCELERATION_VEL = 0.01

# Create a figure and axis
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Initialize the point-light positions
point_lights = []
for i in range(15):
    angle = np.radians(30 * i)
    x = WIDTH / 2 + np.cos(angle) * 200
    y = HEIGHT / 2 + np.sin(angle) * 200
    z = 0
    point_lights.append([x, y, z])

# Define the action's movement parameters
action_x, action_y = 0, 0
action_vel_x, action_vel_y = 0, 0
action_acceleration = ACTION_SPEED
action_acceleration_vel = ACTION_ACCELERATION

# Define the time parameters
time_step = 0.01
t_max = 10

# Animate the point-light and action movements
for t in np.arange(0, t_max, time_step):
    # Update the action's movement
    action_vel_x += action_acceleration_vel * time_step
    action_vel_y += action_acceleration_vel * time_step
    action_x += action_vel_x * time_step
    action_y += action_vel_y * time_step

    # Update the point-light positions
    for i, point_light in enumerate(point_lights):
        x, y, z = point_light
        x += action_x * time_step
        y += action_y * time_step
        z += action_vel_x * time_step
        z += 100  # Add a small offset to simulate the action's movement
        point_light[0] = x
        point_light[1] = y
        point_light[2] = z

    # Check for collision with the black background
    if np.linalg.norm(action_x, 2) > WIDTH / 2 + 100:
        action_x = WIDTH / 2 + 100
        action_y = 0
        action_vel_x = 0
        action_vel_y = 0

    # Plot the point-light and action movements
    ax.clear()
    ax.set_xlim(-200, 200)
    ax.set_ylim(-200, 200)
    ax.set_zlim(-200, 200)
    ax.scatter(action_x, action_y, 10, c='r')
    ax.scatter(0, 0, 10, c='b')
    ax.set_aspect('equal')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')

    # Update the plot
    plt.pause(0.01)

# Close the plot
plt.show()
