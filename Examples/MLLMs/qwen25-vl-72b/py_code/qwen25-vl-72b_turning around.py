
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [-0.5, 0.5], [0, 0.5], [0.5, 0.5],
    [-0.7, 0], [-0.3, 0], [0.3, 0], [0.7, 0],
    [-0.5, -0.5], [0, -0.5], [0.5, -0.5],
    [-0.3, -1], [0, -1], [0.3, -1], [0, -1.5]
])

# Define the rotation matrix function
def rotation_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

# Create a figure and axis with a black background
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Create 15 scatter points in white
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Define the update function for the animation
def update(frame):
    theta = frame * np.pi / 60  # Rotate by a small angle each frame
    rotated_positions = np.dot(initial_positions, rotation_matrix(theta).T)
    points.set_offsets(rotated_positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=120, interval=50, blit=True)

plt.show()
