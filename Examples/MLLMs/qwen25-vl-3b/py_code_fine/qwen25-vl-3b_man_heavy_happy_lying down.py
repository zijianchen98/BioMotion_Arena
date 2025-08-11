
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the 15 point-lights
point_lights = np.array([
    [0.5, 0.8], [0.6, 0.7], [0.7, 0.8], [0.8, 0.9],
    [0.4, 0.6], [0.5, 0.5], [0.6, 0.6], [0.7, 0.7],
    [0.8, 0.6], [0.9, 0.7], [0.4, 0.4], [0.5, 0.3],
    [0.6, 0.4], [0.7, 0.5], [0.8, 0.6]
])

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Plot the point-lights
ax.plot(point_lights[:, 0], point_lights[:, 1], 'o', markersize=10, color='white')

# Set the background color to black
ax.set_facecolor('black')

# Show the plot
plt.show()
