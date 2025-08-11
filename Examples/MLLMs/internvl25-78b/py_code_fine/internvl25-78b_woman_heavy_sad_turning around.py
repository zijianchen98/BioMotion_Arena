
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define initial positions of the 15 points
initial_positions = np.array([
    [0, 1], [0, -1],
    [-0.5, 0.8], [0.5, 0.8],
    [-0.5, -0.8], [0.5, -0.8],
    [-0.9, 0.5], [-0.9, -0.5],
    [0.9, 0.5], [0.9, -0.5],
    [-0.3, 0], [0.3, 0],
    [0, 0.3], [0, -0.3],
    [0, 0]
])

# Rotate points around the origin
def rotate_points(positions, angle):
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    return np.dot(positions, rotation_matrix.T)

# Initialize figure and scatter plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
point_lights, = ax.plot([], [], 'wo', markersize=10)

# Animation update function
def update(frame):
    angle = np.radians(frame * 5)
    rotated_positions = rotate_points(initial_positions, angle)
    point_lights.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return point_lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=72, interval=50, blit=True)

plt.show()
