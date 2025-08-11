
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a new figure
fig = plt.figure()

# Add a 3d subplot
ax = fig.add_subplot(111, projection='3d')

# Set the limits of the plot
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

# Create a list of 15 points
points = np.random.rand(15, 3) * 20 - 10

# Create a list of 15 colors
colors = ['white'] * 15

# Create a scatter plot
scatter = ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=colors)

# Animation function
def animate(i):
    # Update the points
    points[:, 2] = np.sin(i / 10) * 10
    points[:, 0] = np.cos(i / 10) * 10

    # Update the scatter plot
    scatter._offsets3d = (points[:, 0], points[:, 1], points[:, 2])

# Animate the plot
ani = animation.FuncAnimation(fig, animate, interval=100)

# Show the plot
plt.show()
