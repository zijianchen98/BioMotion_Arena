
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the 15 point-lights
point_lights = np.array([
    [0.5, 0.5], [0.6, 0.4], [0.7, 0.3], [0.8, 0.4],
    [0.9, 0.5], [0.5, 0.6], [0.6, 0.7], [0.7, 0.8],
    [0.8, 0.7], [0.9, 0.6], [0.5, 0.7], [0.6, 0.8],
    [0.7, 0.9], [0.8, 0.8], [0.9, 0.7]
])

# Define the direction of the bowing motion
direction = np.array([0.05, -0.05])  # Move slightly forward and downward

# Define the speed of the bowing motion
speed = 0.01

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Plot the point-lights
ax.plot(point_lights[:, 0], point_lights[:, 1], 'w.', markersize=5)

# Animate the point-lights
for t in range(100):
    point_lights[:, 0] += direction[0] * speed
    point_lights[:, 1] += direction[1] * speed
    ax.plot(point_lights[:, 0], point_lights[:, 1], 'w.', markersize=5)
    fig.canvas.draw()
    plt.pause(0.01)

plt.show()
