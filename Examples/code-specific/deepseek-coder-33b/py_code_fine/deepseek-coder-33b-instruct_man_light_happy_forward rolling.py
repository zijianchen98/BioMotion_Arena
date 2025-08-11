
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the limits of the plot
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

# Create 15 point-lights
points = np.random.rand(15, 3) * 20 - 10

# Function to update the point-lights
def update(num):
    # Move the point-lights forward
    points[:, 0] -= 0.1
    # If a point-light reaches the end, move it back to the start
    points[points[:, 0] < -10, 0] = 10
    # Update the scatter plot
    scatter._offsets3d = (points[:, 0], points[:, 1], points[:, 2])

# Create the scatter plot
scatter = ax.scatter(points[:, 0], points[:, 1], points[:, 2])

# Animate the scatter plot
ani = animation.FuncAnimation(fig, update, interval=50)

# Show the plot
plt.show()
