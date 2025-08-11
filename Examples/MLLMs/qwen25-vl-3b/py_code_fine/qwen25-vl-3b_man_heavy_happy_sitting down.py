
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the 15 point lights
positions = np.array([
    [0.5, 0.8],
    [0.6, 0.7],
    [0.7, 0.6],
    [0.8, 0.5],
    [0.9, 0.4],
    [0.5, 0.3],
    [0.6, 0.2],
    [0.7, 0.1],
    [0.8, 0.2],
    [0.9, 0.3],
    [0.5, 0.4],
    [0.6, 0.5],
    [0.7, 0.6],
    [0.8, 0.7],
    [0.9, 0.8]
])

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Plot the point lights
for x, y in positions:
    ax.plot(x, y, 'o', markersize=10, color='white')

# Set the limits of the plot
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Show the plot
plt.show()
