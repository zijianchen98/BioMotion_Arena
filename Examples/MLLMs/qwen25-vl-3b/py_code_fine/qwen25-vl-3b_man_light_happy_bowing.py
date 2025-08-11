
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the 15 white point-lights
light_coords = np.array([
    [0.1, 0.9], [0.2, 0.8], [0.3, 0.7], [0.4, 0.6],
    [0.5, 0.5], [0.6, 0.4], [0.7, 0.3], [0.8, 0.2],
    [0.9, 0.1], [0.1, 0.2], [0.2, 0.3], [0.3, 0.4],
    [0.4, 0.5], [0.5, 0.6], [0.6, 0.7], [0.7, 0.8]
])

# Define the direction of the bowing action
direction = np.array([0.05, -0.05])  # Slightly downward

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Plot the light points
for x, y in light_coords:
    ax.plot(x, y, 'w', markersize=10)

# Animate the bowing action
for t in range(100):
    light_coords[:, 0] += direction[0] * t / 100
    light_coords[:, 1] += direction[1] * t / 100
    ax.clear()
    for x, y in light_coords:
        ax.plot(x, y, 'w', markersize=10)
    fig.canvas.draw()

plt.show()
