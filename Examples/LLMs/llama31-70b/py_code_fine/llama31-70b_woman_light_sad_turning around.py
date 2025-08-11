
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These positions are chosen to represent the joints of a human body
joints = np.array([
    [0, 0],  # head
    [-0.2, 0.5],  # left shoulder
    [0.2, 0.5],  # right shoulder
    [-0.3, 0.2],  # left elbow
    [0.3, 0.2],  # right elbow
    [-0.4, 0],  # left hand
    [0.4, 0],  # right hand
    [0, -0.2],  # hip
    [-0.2, -0.4],  # left knee
    [0.2, -0.4],  # right knee
    [-0.3, -0.6],  # left ankle
    [0.3, -0.6],  # right ankle
    [-0.1, 0.1],  # left breast
    [0.1, 0.1],  # right breast
    [0, -0.5]  # torso
])

# Define the rotation angle as a function of time
def rotation_angle(t):
    return np.pi / 2 * np.sin(t / 10)

# Define the movement of each joint as a function of time
def animate(t):
    angle = rotation_angle(t)
    rotated_joints = np.zeros((15, 2))
    rotated_joints[0] = [0, 0]  # head
    rotated_joints[1] = [-0.2 * np.cos(angle), 0.5]  # left shoulder
    rotated_joints[2] = [0.2 * np.cos(angle), 0.5]  # right shoulder
    rotated_joints[3] = [-0.3 * np.cos(angle - np.pi / 4), 0.2]  # left elbow
    rotated_joints[4] = [0.3 * np.cos(angle - np.pi / 4), 0.2]  # right elbow
    rotated_joints[5] = [-0.4 * np.cos(angle - np.pi / 2), 0]  # left hand
    rotated_joints[6] = [0.4 * np.cos(angle - np.pi / 2), 0]  # right hand
    rotated_joints[7] = [0, -0.2]  # hip
    rotated_joints[8] = [-0.2 * np.cos(angle + np.pi / 4), -0.4]  # left knee
    rotated_joints[9] = [0.2 * np.cos(angle + np.pi / 4), -0.4]  # right knee
    rotated_joints[10] = [-0.3 * np.cos(angle + np.pi / 2), -0.6]  # left ankle
    rotated_joints[11] = [0.3 * np.cos(angle + np.pi / 2), -0.6]  # right ankle
    rotated_joints[12] = [-0.1 * np.cos(angle), 0.1]  # left breast
    rotated_joints[13] = [0.1 * np.cos(angle), 0.1]  # right breast
    rotated_joints[14] = [0, -0.5]  # torso
    return rotated_joints

# Create a new figure
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
points = ax.scatter(joints[:, 0], joints[:, 1], c='white', s=10)

# Define the animation function
def update(t):
    joints = animate(t)
    points.set_offsets(joints)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
