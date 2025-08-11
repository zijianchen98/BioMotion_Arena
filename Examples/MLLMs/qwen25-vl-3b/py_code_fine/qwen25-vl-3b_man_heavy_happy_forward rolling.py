
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
    # Update the positions of the points
    new_positions = np.roll(positions, -1, axis=0)
    ax.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=100)

    # Update the plot
    fig.canvas.draw()
    plt.pause(0.01)

plt.show()
