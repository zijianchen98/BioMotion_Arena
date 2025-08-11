
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define the parameters of the subject's body
body_radius = 0.05
body_x = 0.5
body_y = 0.5

# Define the parameters of the subject's limbs
limb_length = 0.05
limb_width = 0.01

# Define the parameters of the point-lights
point_light_radius = 0.01
point_light_distance = 0.05
point_light_speed = 0.01

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the points of the subject's body
body_points = np.array([[body_x - body_radius, body_y - body_radius, 0],
                       [body_x + body_radius, body_y - body_radius, 0],
                       [body_x + body_radius, body_y + body_radius, 0],
                       [body_x - body_radius, body_y + body_radius, 0],
                       [body_x, body_y - body_radius, 0],
                       [body_x, body_y + body_radius, 0],
                       [body_x - body_radius, body_y, 0],
                       [body_x + body_radius, body_y, 0],
                       [body_x + body_radius, body_y + body_radius, 0],
                       [body_x - body_radius, body_y + body_radius, 0]])

# Define the points of the subject's limbs
limb_points = np.array([[body_x - limb_length / 2, body_y - limb_length / 2, 0],
                       [body_x + limb_length / 2, body_y - limb_length / 2, 0],
                       [body_x + limb_length / 2, body_y + limb_length / 2, 0],
                       [body_x - limb_length / 2, body_y + limb_length / 2, 0],
                       [body_x, body_y - limb_length / 2, 0],
                       [body_x, body_y + limb_length / 2, 0],
                       [body_x - limb_length / 2, body_y, 0],
                       [body_x + limb_length / 2, body_y, 0],
                       [body_x + limb_length / 2, body_y + limb_length / 2, 0],
                       [body_x - limb_length / 2, body_y + limb_length / 2, 0]])

# Define the points of the point-lights
point_light_points = np.array([[point_light_distance, point_light_distance, 0],
                                [point_light_distance, -point_light_distance, 0],
                                [point_light_distance, point_light_distance, 0],
                                [-point_light_distance, point_light_distance, 0],
                                [-point_light_distance, -point_light_distance, 0],
                                [point_light_distance, point_light_distance, 0],
                                [point_light_distance, -point_light_distance, 0]])

# Initialize the figure and axis
ax.set_xlim(-0.1, 0.1)
ax.set_ylim(-0.1, 0.1)
ax.set_zlim(-0.1, 0.1)

# Function to update the points of the subject's body and limbs
def update(frame):
    global body_x, body_y, limb_length, limb_width, point_light_distance, point_light_speed

    # Update the points of the subject's body
    body_x += point_light_speed * frame
    body_y += point_light_speed * frame

    # Update the points of the subject's limbs
    limb_length += point_light_speed * frame
    limb_width += point_light_speed * frame

    # Update the points of the point-lights
    point_light_distance += point_light_speed * frame
    point_light_points[:, 0] += point_light_speed * frame
    point_light_points[:, 1] += point_light_speed * frame
    point_light_points[:, 2] += point_light_speed * frame

    # Ensure the point-lights stay within the boundaries of the figure
    point_light_points[:, 0] = max(-1, min(point_light_points[:, 0], 1))
    point_light_points[:, 1] = max(-1, min(point_light_points[:, 1], 1))
    point_light_points[:, 2] = max(-1, min(point_light_points[:, 2], 1))

    # Ensure the points of the subject's body and limbs stay within the boundaries of the figure
    body_points = np.clip(body_points, -1, 1)
    limb_points = np.clip(limb_points, -1, 1)

    # Clear the previous frame
    ax.clear()

    # Plot the points of the subject's body and limbs
    ax.scatter(body_points[:, 0], body_points[:, 1], body_points[:, 2], s=0.1, c='b', alpha=0.5)
    ax.scatter(limb_points[:, 0], limb_points[:, 1], limb_points[:, 2], s=0.1, c='r', alpha=0.5)

    # Plot the points of the point-lights
    ax.scatter(point_light_points[:, 0], point_light_points[:, 1], point_light_points[:, 2], s=0.1, c='w', alpha=0.5)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=20)

plt.show()
