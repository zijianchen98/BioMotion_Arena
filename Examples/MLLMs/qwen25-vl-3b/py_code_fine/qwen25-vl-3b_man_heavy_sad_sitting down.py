
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the 15 point-lights
point_lights = np.array([
    [0.5, 0.5], [0.6, 0.4], [0.7, 0.3], [0.8, 0.4],
    [0.9, 0.5], [0.5, 0.6], [0.6, 0.7], [0.7, 0.8],
    [0.8, 0.7], [0.9, 0.6], [0.5, 0.7], [0.6, 0.8],
    [0.7, 0.9], [0.8, 0.8], [0.9, 0.7]
])

# Define the weights and actions
weights = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
actions = np.array(['sad', 'sad', 'sad', 'sad', 'sad', 'sad', 'sad', 'sad', 'sad', 'sad', 'sad', 'sad', 'sad', 'sad', 'sad'])

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Plot the point-lights
ax.scatter(point_lights[:, 0], point_lights[:, 1], s=100, c='white')

# Animate the point-lights
for i in range(len(weights)):
    # Move the point-lights based on their weight and action
    if actions[i] == 'sad':
        point_lights[i, 0] -= 0.01 * weights[i]
        point_lights[i, 1] += 0.01 * weights[i]
    else:
        point_lights[i, 0] += 0.01 * weights[i]
        point_lights[i, 1] -= 0.01 * weights[i]

    # Update the plot
    ax.clear()
    ax.scatter(point_lights[:, 0], point_lights[:, 1], s=100, c='white')
    plt.pause(0.01)

plt.show()
