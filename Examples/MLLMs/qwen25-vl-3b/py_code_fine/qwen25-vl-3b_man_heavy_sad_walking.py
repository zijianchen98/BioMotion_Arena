
import numpy as np
import matplotlib.pyplot as plt

# Define the number of points
num_points = 15

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Generate random positions for the points
points = np.random.rand(num_points, 2)

# Plot the points in white
ax.plot(points[:, 0], points[:, 1], 'w.', markersize=4)

# Set the limits of the plot to match the example image
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Show the plot
plt.show()
