
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the 3D coordinates of the 15 point-lights on the body
points = np.array([
    [-0.1, 0, 0.2],  # head
    [0.1, 0, 0.2],   # head
    [-0.2, 0, 0.1],  # left shoulder
    [0.2, 0, 0.1],   # right shoulder
    [-0.2, 0.2, 0.1], # left hip
    [0.2, 0.2, 0.1],  # right hip
    [-0.2, 0.4, 0.1], # left knee
    [0.2, 0.4, 0.1],  # right knee
    [-0.2, 0.6, 0.1], # left ankle
    [0.2, 0.6, 0.1],  # right ankle
    [-0.1, 0.2, 0.3], # left elbow
    [0.1, 0.2, 0.3],  # right elbow
    [-0.1, 0.4, 0.3], # left wrist
    [0.1, 0.4, 0.3],  # right wrist
    [-0.1, 0.6, 0.3]  # heavy weight
])

# Define the 3D coordinates of the body
body_points = np.array([
    [-0.3, 0, 0.3],  # left foot
    [0.3, 0, 0.3],   # right foot
    [-0.2, 0.8, 0.2], # left hand
    [0.2, 0.8, 0.2]   # right hand
])

# Define the animation parameters
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(0, 1)
ax.set_facecolor('black')

def animate(i):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(0, 1)
    ax.set_facecolor('black')

    # Rotate the points around the y-axis
    rotation_angle = i / 10.0
    rotation_matrix = np.array([
        [np.cos(rotation_angle), 0, np.sin(rotation_angle)],
        [0, 1, 0],
        [-np.sin(rotation_angle), 0, np.cos(rotation_angle)]
    ])
    points_rotated = np.dot(points, rotation_matrix)

    # Draw the points
    ax.scatter(points_rotated[:, 0], points_rotated[:, 1], points_rotated[:, 2], c='white', s=50)

    # Draw the body
    ax.plot([points_rotated[0, 0], body_points[0, 0]], [points_rotated[0, 1], body_points[0, 1]], [points_rotated[0, 2], body_points[0, 2]], c='white', lw=2)
    ax.plot([points_rotated[0, 0], body_points[1, 0]], [points_rotated[0, 1], body_points[1, 1]], [points_rotated[0, 2], body_points[1, 2]], c='white', lw=2)
    ax.plot([points_rotated[1, 0], body_points[0, 0]], [points_rotated[1, 1], body_points[0, 1]], [points_rotated[1, 2], body_points[0, 2]], c='white', lw=2)
    ax.plot([points_rotated[1, 0], body_points[1, 0]], [points_rotated[1, 1], body_points[1, 1]], [points_rotated[1, 2], body_points[1, 2]], c='white', lw=2)

ani = animation.FuncAnimation(fig, animate, frames=360, interval=20)

plt.show()
