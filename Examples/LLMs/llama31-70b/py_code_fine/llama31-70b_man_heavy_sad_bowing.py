
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# Each row represents a point-light, with the first two columns representing the x and y coordinates
# The third column represents the size of the point-light (all are the same size here)
lights = np.array([
    [-0.2, 0.2, 0.05],  # Head
    [-0.1, 0.3, 0.05],  # Shoulder
    [0.1, 0.3, 0.05],   # Shoulder
    [-0.2, 0.1, 0.05],  # Elbow
    [0.2, 0.1, 0.05],   # Elbow
    [-0.3, 0.0, 0.05],  # Hand
    [0.3, 0.0, 0.05],   # Hand
    [-0.1, -0.1, 0.05], # Hip
    [0.1, -0.1, 0.05],  # Hip
    [-0.2, -0.2, 0.05], # Knee
    [0.2, -0.2, 0.05],  # Knee
    [-0.3, -0.3, 0.05], # Ankle
    [0.3, -0.3, 0.05],  # Ankle
    [0.0, 0.4, 0.05],   # Weight
    [0.0, -0.4, 0.05],  # Weight
])

# Define the movement of the point-lights over time
# Each row represents a frame in the animation, with the first two columns representing the x and y coordinates
# The movement is based on a simple sinusoidal function to create a smooth and natural motion
def animate(i):
    global lights
    angle = i / 10.0
    lights[:, 0] = np.array([
        0.0,
        0.1 * np.sin(angle),
        -0.1 * np.sin(angle),
        0.2 * np.sin(angle),
        -0.2 * np.sin(angle),
        0.3 * np.sin(angle),
        -0.3 * np.sin(angle),
        0.1 * np.sin(angle),
        -0.1 * np.sin(angle),
        0.2 * np.sin(angle),
        -0.2 * np.sin(angle),
        0.3 * np.sin(angle),
        -0.3 * np.sin(angle),
        0.0,
        0.0,
    ])
    lights[:, 1] = np.array([
        0.2 + 0.1 * np.cos(angle),
        0.3 + 0.1 * np.cos(angle),
        0.3 + 0.1 * np.cos(angle),
        0.1 + 0.1 * np.cos(angle),
        0.1 + 0.1 * np.cos(angle),
        0.0 + 0.1 * np.cos(angle),
        0.0 + 0.1 * np.cos(angle),
        -0.1 + 0.1 * np.cos(angle),
        -0.1 + 0.1 * np.cos(angle),
        -0.2 + 0.1 * np.cos(angle),
        -0.2 + 0.1 * np.cos(angle),
        -0.3 + 0.1 * np.cos(angle),
        -0.3 + 0.1 * np.cos(angle),
        0.4 + 0.1 * np.cos(angle),
        -0.4 + 0.1 * np.cos(angle),
    ])
    return lights

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the scatter plot of the point-lights
scatter = ax.scatter(lights[:, 0], lights[:, 1], s=lights[:, 2] * 100, c='white')

# Define the animation function
def update(i):
    global scatter
    scatter.set_offsets(animate(i))
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
