
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

# Define the parameters for the animation
num_points = 1000
num_points_per_side = 500
angle_step = 2 * np.pi / num_points_per_side
num_sides = 2

# Create a figure and a 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to generate a point-light stimulus
def generate_stimulus(angle, x, y):
    # Define the parameters for the point-light stimulus
    num_points = 15
    step = 0.1

    # Generate the points on the plane
    points = np.zeros((num_points, 3))
    for i in range(num_points):
        t = i / (num_points - 1)
        points[i, 0] = x + t * 10 * np.cos(angle)
        points[i, 1] = y + t * 10 * np.sin(angle)
        points[i, 2] = random.randint(0, 100)

    # Generate the point-lights
    points = np.vstack((points, points))
    points = points[:, :2]  # Remove the z-coordinate
    points = points / 10  # Normalize the points

    # Create the point-lights
    points = points[:num_points_per_side, :]
    points = points / 10  # Normalize the points
    points = points[:, np.newaxis]  # Add a new axis
    points = points / 10  # Normalize the points

    # Plot the points
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='w', s=0.1)

    # Plot the point-lights
    for i in range(num_points):
        ax.plot3D(points[i, 0], points[i, 1], points[i, 2], c='w', lw=0.1)

    # Set the axis limits
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)

    # Set the axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Return the points
    return points

# Generate the points for the stimulus
points = generate_stimulus(0, 10, 10)

# Plot the stimulus
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='w', s=0.1)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

# Set the axis limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

# Show the plot
plt.show()
