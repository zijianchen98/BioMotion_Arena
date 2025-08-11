
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the 15 point lights
lights = np.array([
    [0.4, 0.6], [0.5, 0.7], [0.6, 0.8],
    [0.7, 0.9], [0.8, 0.8], [0.9, 0.7],
    [0.4, 0.4], [0.5, 0.5], [0.6, 0.6],
    [0.7, 0.7], [0.8, 0.8], [0.9, 0.9],
    [0.4, 0.2], [0.5, 0.3], [0.6, 0.4]
])

# Define the weights and direction of the bowing action
weights = np.array([0.5, 0.4, 0.3])
directions = np.array([-0.1, -0.2, -0.3])

# Calculate the new positions of the lights based on their weights and direction
new_positions = weights * directions[:, None] + lights

# Plot the lights
plt.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=100)
plt.gca().set_aspect('equal')
plt.axis('off')
plt.show()
