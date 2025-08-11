
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
                   [1, -1], [2, -2], [3, -3], [4, -4],
                   [-1, 1], [-2, 2], [-3, 3], [-4, 4],
                   [-1, -1], [-2, -2], [-3, -3]])

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')

# Create the scatter plot
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

# Define the update function for the animation
def update(frame):
    global points
    # Apply a simple transformation to the points to simulate bowing
    angle = np.radians(10 * np.sin(0.1 * frame))
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    points = np.dot(points, rotation_matrix)
    scatter.set_offsets(points)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
