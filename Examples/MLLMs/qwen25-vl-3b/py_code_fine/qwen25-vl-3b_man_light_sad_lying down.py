
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the 15 point lights
lights = np.array([
    [0.1, 0.1], [0.2, 0.1], [0.3, 0.1], [0.4, 0.1], [0.5, 0.1],
    [0.6, 0.1], [0.7, 0.1], [0.8, 0.1], [0.9, 0.1], [0.1, 0.2],
    [0.2, 0.2], [0.3, 0.2], [0.4, 0.2], [0.5, 0.2], [0.6, 0.2]
])

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Plot the lights
for x, y in lights:
    ax.plot(x, y, 'o', markersize=10, color='white')

# Set the background color to black
ax.set_facecolor('black')

# Show the plot
plt.show()
