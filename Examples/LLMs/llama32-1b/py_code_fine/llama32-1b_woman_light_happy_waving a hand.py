
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a figure and axis object
fig, ax = plt.subplots()

# Initialize point positions
points = np.array([
    [WIDTH / 2, HEIGHT / 2],
    [WIDTH / 2 + 100, HEIGHT / 2],
    [WIDTH / 2 + 200, HEIGHT / 2],
    [WIDTH / 2 + 300, HEIGHT / 2],
    [WIDTH / 2 + 400, HEIGHT / 2],
    [WIDTH / 2 + 500, HEIGHT / 2],
    [WIDTH / 2, HEIGHT / 2],
])

# Initialize point velocities
velocities = np.array([
    [0, 1],
    [0, -1],
    [2, 0],
    [-2, 0],
    [1, 2],
    [-1, 2],
    [2, -1],
    [-2, -1],
    [1, -2],
    [-1, -2],
])

# Set axis limits
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)

# Function to update the plot
def update(i):
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)

    # Move point lights
    for j, point in enumerate(points):
        ax.add_patch(plt.Rectangle((point[0], point[1]), 1, 1, color=WHITE))
        velocities[j] = np.array([velocities[j][0] + i * 0.01, velocities[j][1] + i * 0.01])

    # Move point lights
    for j, point in enumerate(points):
        ax.add_patch(plt.Rectangle((point[0], point[1]), 1, 1, color=WHITE))
        velocities[j] = np.array([velocities[j][0] + i * 0.01, velocities[j][1] + i * 0.01])

    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.axis('off')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=1000, interval=16)

plt.show()
