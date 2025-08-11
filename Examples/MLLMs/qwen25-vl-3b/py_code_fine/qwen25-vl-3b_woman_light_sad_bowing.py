
import numpy as np
import matplotlib.pyplot as plt

# Define the number of points
num_points = 15

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Generate random positions for the points
positions = np.random.rand(num_points, 2)

# Plot the points in white
ax.scatter(positions[:, 0], positions[:, 1], color='white', s=100)

# Animate the points by shifting them slightly over time
for i in range(10):
    # Shift the points slightly to the right
    positions[:, 0] += 0.01 * np.sin(i * 0.1)
    
    # Update the plot with the new positions
    ax.clear()
    ax.set_facecolor('black')
    ax.scatter(positions[:, 0], positions[:, 1], color='white', s=100)
    fig.canvas.draw()

plt.show()
