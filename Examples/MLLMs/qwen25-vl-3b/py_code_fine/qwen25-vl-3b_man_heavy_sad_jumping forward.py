
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

# Plot each point in white
for point in points:
    ax.plot(point[0], point[1], 'w.', markersize=10)

# Set the limits of the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Show the plot
plt.show()
