
import numpy as np
import matplotlib.pyplot as plt

# Define the number of points
num_points = 15

# Generate random positions for the points
points = np.random.rand(num_points, 2)

# Set up the figure and axis
fig, ax = plt.subplots()

# Plot the points
ax.plot(points[:, 0], points[:, 1], 'o', markersize=10, color='white')

# Set the background color to black
ax.set_facecolor('black')

# Set the limits of the plot
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Show the plot
plt.show()
