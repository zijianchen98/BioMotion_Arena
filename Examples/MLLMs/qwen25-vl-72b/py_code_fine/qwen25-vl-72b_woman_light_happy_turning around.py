
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [-0.5, 0.7], [0, 0.7], [0.5, 0.7],
    [-0.7, 0.4], [-0.3, 0.4], [0.3, 0.4], [0.7, 0.4],
    [-0.8, 0], [-0.4, 0], [0, 0], [0.4, 0], [0.8, 0],
    [-0.3, -0.4], [0.3, -0.4]
])

# Define the rotation matrix
def rotation_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

# Create a figure and axis with a black background
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Create 15 scatter points
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Animation update function
def update(frame):
    theta = frame * np.pi / 60  # Adjust speed of turning
    rotated_positions = np.dot(initial_positions, rotation_matrix(theta).T)
    points.set_offsets(rotated_positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(120), interval=50, blit=True)

plt.show()
