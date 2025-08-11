
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

# Animate the points to simulate forward rolling
for i in range(10):
    # Rotate the points to simulate forward rolling
    positions = np.dot(positions, np.array([[np.cos(i * np.pi / 4), -np.sin(i * np.pi / 4)],
                                           [np.sin(i * np.pi / 4), np.cos(i * np.pi / 4)]]))
    
    # Update the scatter plot with new positions
    ax.clear()
    ax.scatter(positions[:, 0], positions[:, 1], color='white', s=100)
    fig.canvas.draw()

plt.show()
