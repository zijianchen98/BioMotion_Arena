
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and background
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 0.8], [0.2, 0.5], [0.1, 0.2], [-0.1, 0.2], [-0.2, 0.5],
    [0.4, 0.6], [0.3, 0.3], [0, 0.3], [-0.3, 0.3], [-0.4, 0.6],
    [0.3, -0.1], [0.2, -0.4], [0, -0.4], [-0.2, -0.4], [-0.3, -0.1]
])

# Define the jumps for each point-light
jump_offsets = np.array([
    [0, -0.2], [0.1, -0.1], [0.1, 0], [-0.1, 0], [-0.1, -0.1],
    [0.1, 0], [0.1, -0.1], [0, 0], [-0.1, -0.1], [-0.1, 0],
    [0, -0.1], [0, -0.2], [0, -0.2], [0, -0.2], [0, -0.1]
])

# Create a scatter plot
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')

def update(frame):
    offset = frame / 10.0
    positions = initial_positions + jump_offsets * offset
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=20, interval=100, blit=True)

plt.axis('off')
plt.show()
