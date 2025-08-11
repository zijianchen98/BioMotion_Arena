
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the points for the human body
points = np.array([
    [-0.2, 0, 0],  # Left hip
    [0.2, 0, 0],   # Right hip
    [-0.2, 0.5, 0],  # Left knee
    [0.2, 0.5, 0],   # Right knee
    [-0.2, 1, 0],  # Left ankle
    [0.2, 1, 0],   # Right ankle
    [-0.2, 0.5, 0.5],  # Left foot
    [0.2, 0.5, 0.5],   # Right foot
    [-0.2, 1.5, 0],  # Left toe
    [0.2, 1.5, 0],   # Right toe
    [0, -0.5, 0],  # Left shoulder
    [0, 0.5, 0],   # Right shoulder
    [0, -0.5, 0.5],  # Left elbow
    [0, 0.5, 0.5],   # Right elbow
    [0, -0.5, 1],  # Left hand
    [0, 0.5, 1],   # Right hand
    [0, 0, 0],  # Head
])

# Define the initial positions of the points
initial_positions = points.copy()

# Define the movement of the points
def move_points(points, time):
    # Move the legs
    points[1, 0] = 0.2 * np.sin(2 * np.pi * time)
    points[3, 0] = 0.2 * np.sin(2 * np.pi * time)
    points[5, 0] = 0.2 * np.sin(2 * np.pi * time)
    points[7, 0] = 0.2 * np.sin(2 * np.pi * time)
    points[9, 0] = 0.2 * np.sin(2 * np.pi * time)
    points[11, 0] = 0.2 * np.sin(2 * np.pi * time)

    # Move the arms
    points[13, 0] = 0.1 * np.sin(2 * np.pi * time)
    points[15, 0] = 0.1 * np.sin(2 * np.pi * time)

    # Move the head
    points[16, 0] = 0.05 * np.sin(2 * np.pi * time)

    return points

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the plot
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_axis_off()

# Animate the points
def animate(i):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.set_axis_off()

    points = move_points(initial_positions, i / 50)

    # Plot the points
    for point in points:
        ax.plot(point[0], point[1], point[2], 'o', markersize=10, color='w')

# Animate the figure
ani = animation.FuncAnimation(fig, animate, frames=500, interval=20)

plt.show()
