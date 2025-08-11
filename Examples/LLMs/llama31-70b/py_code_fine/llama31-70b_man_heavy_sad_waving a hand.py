
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# representing the sad man with heavy weight
lights = np.array([
    [0.5, 0.5],  # head
    [0.4, 0.6],  # left shoulder
    [0.6, 0.6],  # right shoulder
    [0.4, 0.4],  # left elbow
    [0.6, 0.4],  # right elbow
    [0.4, 0.2],  # left hand
    [0.6, 0.2],  # right hand
    [0.5, 0.7],  # neck
    [0.5, 0.8],  # torso top
    [0.5, 0.9],  # torso middle
    [0.5, 1.0],  # torso bottom
    [0.4, 0.7],  # left upper arm
    [0.6, 0.7],  # right upper arm
    [0.4, 0.5],  # left forearm
    [0.6, 0.5],  # right forearm
])

# Define the motion of the point-lights
# Waving the right hand
def update(frame):
    global lights
    lights = np.array([
        [0.5, 0.5],  # head
        [0.4, 0.6],  # left shoulder
        [0.6 + 0.1 * np.sin(frame * 0.1), 0.6],  # right shoulder
        [0.4, 0.4],  # left elbow
        [0.6 + 0.1 * np.sin(frame * 0.1), 0.4],  # right elbow
        [0.4, 0.2],  # left hand
        [0.6 + 0.1 * np.sin(frame * 0.1) + 0.1 * np.cos(frame * 0.1), 0.2],  # right hand
        [0.5, 0.7],  # neck
        [0.5, 0.8],  # torso top
        [0.5, 0.9],  # torso middle
        [0.5, 1.0],  # torso bottom
        [0.4, 0.7],  # left upper arm
        [0.6 + 0.05 * np.sin(frame * 0.1), 0.7],  # right upper arm
        [0.4, 0.5],  # left forearm
        [0.6 + 0.05 * np.sin(frame * 0.1), 0.5],  # right forearm
    ])
    scatter.set_offsets(lights)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot of the point-lights
scatter = ax.scatter(lights[:, 0], lights[:, 1], s=10, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
