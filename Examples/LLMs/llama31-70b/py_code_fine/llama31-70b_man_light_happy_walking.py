
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point lights representing the happy man
point_lights = np.array([
    [0.0, 0.0],  # head
    [-0.2, 0.3],  # left shoulder
    [0.2, 0.3],  # right shoulder
    [-0.3, 0.1],  # left elbow
    [0.3, 0.1],  # right elbow
    [-0.4, -0.1],  # left hand
    [0.4, -0.1],  # right hand
    [0.0, -0.3],  # torso
    [-0.1, -0.5],  # left hip
    [0.1, -0.5],  # right hip
    [-0.2, -0.7],  # left knee
    [0.2, -0.7],  # right knee
    [-0.3, -0.9],  # left ankle
    [0.3, -0.9],  # right ankle
    [0.0, -1.0],  # feet
])

# Define the walking animation
def walk(frame):
    global point_lights
    # Move the legs
    point_lights[10, 0] = -0.2 + 0.1 * np.sin(frame / 10.0)  # left knee
    point_lights[11, 0] = 0.2 - 0.1 * np.sin(frame / 10.0)  # right knee
    point_lights[12, 0] = -0.3 + 0.1 * np.sin(frame / 10.0)  # left ankle
    point_lights[13, 0] = 0.3 - 0.1 * np.sin(frame / 10.0)  # right ankle
    # Move the arms
    point_lights[4, 0] = -0.3 + 0.1 * np.cos(frame / 10.0)  # left elbow
    point_lights[5, 0] = 0.3 - 0.1 * np.cos(frame / 10.0)  # right elbow
    point_lights[6, 0] = -0.4 + 0.1 * np.cos(frame / 10.0)  # left hand
    point_lights[7, 0] = 0.4 - 0.1 * np.cos(frame / 10.0)  # right hand
    # Move the torso
    point_lights[7, 1] = -0.3 + 0.05 * np.sin(frame / 20.0)  # torso
    return point_lights

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_axis_off()

# Initialize the plot with the point lights
scatter = ax.scatter(point_lights[:, 0], point_lights[:, 1], s=50, c='w')

# Define the animation function
def animate(frame):
    global point_lights
    point_lights = walk(frame)
    scatter.set_offsets(point_lights)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
