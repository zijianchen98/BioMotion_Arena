
import numpy as np
import matplotlib.pyplot as plt

# Define the number of points
num_points = 15

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Create a grid of points
points = np.random.rand(num_points, 2)
points[:, 0] *= 4  # Scale x-coordinates to make them more spread out
points[:, 1] *= 4  # Scale y-coordinates to make them more spread out

# Plot the points in white
ax.plot(points[:, 0], points[:, 1], 'w.', markersize=8)

# Set the limits of the plot to match the example image
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Show the plot
plt.show()
