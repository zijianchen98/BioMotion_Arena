
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Initial positions of the point-lights
positions = np.array([
    [0.5, 0.5], [0.4, 0.6], [0.6, 0.6], [0.45, 0.7], [0.55, 0.7],
    [0.4, 0.8], [0.6, 0.8], [0.3, 0.9], [0.7, 0.9], [0.4, 0.75],
    [0.6, 0.75], [0.45, 0.65], [0.55, 0.65], [0.5, 0.85], [0.5, 0.95]
])

# Points represented as scatter plot
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=200)

def update(frame):
    angle = np.pi * 2 * frame / 100
    rot_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_positions = positions @ rot_matrix
    scat.set_offsets(rotated_positions)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=30, blit=True)

plt.show()
