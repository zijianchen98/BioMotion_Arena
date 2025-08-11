
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
ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Animate the points by shifting them slightly over time
for t in range(10):
    # Shift the points slightly to the right
    points[:, 0] += 0.1 * np.sin(t)
    
    # Update the plot
    ax.clear()
    ax.set_facecolor('black')
    ax.scatter(points[:, 0], points[:, 1], color='white', s=100)
    fig.canvas.draw()

plt.show()
