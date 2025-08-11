
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setting up the figure
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')

# Number of points
num_points = 15

# Initialize points in the form of a 2D array
points = np.zeros((num_points, 2))

# Set the initial coordinates for the happy man's point lights
# The arrangement is simpler but coherent for visual representation
initial_positions = [
    [0, 1], [0.5, 2], [-0.5, 2],
    [1, 0.5], [0, 0], [-1, 0.5],
    [1, -1], [0, -1], [-1, -1],
    [0.5, -2], [-0.5, -2],
    [1.5, 1], [-1.5, 1],
    [-1.5, -1], [1.5, -1],
    [0, 2.5]
]

points = np.array(initial_positions)

# Visualization element
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Function to update the animation
def update(frame):
    global points
    # Simulate a turning motion
    theta = frame * (np.pi / 90)  # control the rotation speed
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                 [np.sin(theta),  np.cos(theta)]])
    points = points @ rotation_matrix.T
    scat.set_offsets(points)  # Update the scatter positions
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=360, interval=30, blit=True)

plt.show()
