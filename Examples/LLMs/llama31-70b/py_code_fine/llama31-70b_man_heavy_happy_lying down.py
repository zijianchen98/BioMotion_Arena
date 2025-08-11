
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the happy man
point_lights = np.array([
    [0.5, 0.5],  # head
    [0.4, 0.6],  # left shoulder
    [0.6, 0.6],  # right shoulder
    [0.4, 0.7],  # left elbow
    [0.6, 0.7],  # right elbow
    [0.4, 0.8],  # left hand
    [0.6, 0.8],  # right hand
    [0.5, 0.4],  # left hip
    [0.5, 0.3],  # right hip
    [0.4, 0.2],  # left knee
    [0.6, 0.2],  # right knee
    [0.4, 0.1],  # left ankle
    [0.6, 0.1],  # right ankle
    [0.5, 0.9],  # torso
    [0.5, 0.2]  # weight
])

# Define the motion parameters for the lying down action
def get_motion(frame):
    angle = np.pi / 180 * (30 * np.sin(frame / 10.0))
    angle2 = np.pi / 180 * (15 * np.sin(frame / 10.0))
    angle3 = np.pi / 180 * (10 * np.sin(frame / 10.0))

    motion = np.array([
        [0, 0],  # head
        [-0.05 * np.cos(angle), -0.05 * np.sin(angle)],  # left shoulder
        [0.05 * np.cos(angle), -0.05 * np.sin(angle)],  # right shoulder
        [-0.1 * np.cos(angle), -0.1 * np.sin(angle)],  # left elbow
        [0.1 * np.cos(angle), -0.1 * np.sin(angle)],  # right elbow
        [-0.15 * np.cos(angle), -0.15 * np.sin(angle)],  # left hand
        [0.15 * np.cos(angle), -0.15 * np.sin(angle)],  # right hand
        [0, 0.05 * np.cos(angle2)],  # left hip
        [0, -0.05 * np.cos(angle2)],  # right hip
        [0, -0.15 * np.cos(angle2)],  # left knee
        [0, 0.15 * np.cos(angle2)],  # right knee
        [0, -0.2 * np.cos(angle3)],  # left ankle
        [0, 0.2 * np.cos(angle3)],  # right ankle
        [0, 0],  # torso
        [0, -0.05 * np.cos(angle2)]  # weight
    ])

    return motion

# Create a new figure
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-light positions
points = ax.scatter(point_lights[:, 0], point_lights[:, 1], s=50, c='white')

# Animation function
def animate(frame):
    motion = get_motion(frame)
    new_points = point_lights + motion
    points.set_offsets(new_points)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
