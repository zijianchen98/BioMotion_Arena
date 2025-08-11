
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the point-lights
def init_positions():
    positions = np.array([
        [0, 1], [-0.5, 0.75], [0.5, 0.75], [-1, 0.5], [1, 0.5],
        [-0.5, 0.5], [0.5, 0.5], [0, 0.25], [-0.5, 0.25], [0.5, 0.25],
        [-1, 0], [1, 0], [0, -0.25], [-0.5, -0.5], [0.5, -0.5], [0, -1]
    ])
    return positions

# Define the update function for the animation
def update(frame, points, positions):
    theta = 2 * np.pi / 30 * frame
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    new_positions = np.dot(positions, rotation_matrix.T)
    points.set_offsets(new_positions)
    return points,

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

positions = init_positions()
points = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Create the animation
ani = animation.FuncAnimation(
    fig, update, fargs=(points, positions), frames=60, interval=50, blit=True
)

plt.show()
