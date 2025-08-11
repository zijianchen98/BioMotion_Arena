
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the 3D points of the human body
points = np.array([
    [-0.1, 0, 0],  # left heel
    [0.1, 0, 0],   # right heel
    [0, -0.1, 0],  # left toe
    [0, 0.1, 0],   # right toe
    [-0.1, 0, 0.1],  # left ankle
    [0.1, 0, 0.1],   # right ankle
    [0, -0.1, 0.1],  # left knee
    [0, 0.1, 0.1],   # right knee
    [0, 0, 0.2],   # hips
    [0, 0, 0.3],   # head
    [-0.1, 0, 0.4],  # left shoulder
    [0.1, 0, 0.4],   # right shoulder
    [0, -0.1, 0.4],  # left elbow
    [0, 0.1, 0.4],   # right elbow
    [0, 0, 0.5]    # left hand
])

# Define the 3D rotation matrices for the human body
def rotate_x(angle):
    return np.array([
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)]
    ])

def rotate_y(angle):
    return np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])

def rotate_z(angle):
    return np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])

# Define the animation function
def animate(frame):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Rotate the human body
    angle = frame / 10.0
    rotation_x = rotate_x(angle)
    rotation_y = rotate_y(angle)
    rotation_z = rotate_z(angle)

    # Calculate the new positions of the points
    new_points = np.dot(points, rotation_x)
    new_points = np.dot(new_points, rotation_y)
    new_points = np.dot(new_points, rotation_z)

    # Plot the points
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.scatter(new_points[:, 0], new_points[:, 1], new_points[:, 2])

# Create the animation
ani = animation.FuncAnimation(fig=None, func=animate, frames=300, interval=50, repeat=False)

plt.show()
