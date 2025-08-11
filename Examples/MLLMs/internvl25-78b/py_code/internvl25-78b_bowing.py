
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-2, 2)
ax.axis('off')

# Initial coordinates for the point-lights to form the human figure
points = np.array([
    [0, 1],  # Head
    [-0.2, 0.8], [0.2, 0.8],  # Shoulders
    [-0.4, 0.6], [0.4, 0.6],  # Elbows
    [-0.5, 0.4], [0.5, 0.4],  # Hands
    [0, 0],  # Torso
    [-0.1, -0.2], [0.1, -0.2],  # Hips
    [-0.2, -0.5], [0.2, -0.5],  # Knees
    [-0.25, -0.7], [0.25, -0.7],  # Feet
])

# Define the scatter plot
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

# Animation update function
def update(frame):
    if frame < 15:
        angle = np.deg2rad(10 * (1 - frame / 15))
    else:
        angle = np.deg2rad(10 * (frame / 15 - 1))

    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    # Rotate points around the torso (origin for these points)
    rotated_points = points.copy()
    rotated_points[1:, :] -= points[5]
    rotated_points[1:, :] = np.dot(rotated_points[1:, :], rotation_matrix)
    rotated_points[1:, :] += points[5]

    scatter.set_offsets(rotated_points)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=30, interval=50, repeat=True)

plt.show()
