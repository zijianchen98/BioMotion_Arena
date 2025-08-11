
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points for the sadwoman running
positions = [
    [0.5, 0.9], [0.4, 0.8], [0.6, 0.8], [0.7, 0.7], [0.5, 0.6],
    [0.4, 0.5], [0.6, 0.5], [0.7, 0.4], [0.5, 0.3],
    [0.4, 0.2], [0.6, 0.2], [0.7, 0.1], [0.5, 0.0],
    [0.4, -0.1], [0.6, -0.1]
]

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial position
ax.plot(*zip(*positions), 'o', color='white', markersize=10)

# Animate the movement
for i in range(1, len(positions)):
    # Update the positions
    positions[i] = [positions[i-1][0] + 0.1 * (-1 if i % 2 == 0 else 1),
                    positions[i-1][1] + 0.1 * (-1 if i % 2 == 0 else 1)]
    
    # Plot the updated positions
    ax.plot(*zip(*positions), 'o', color='white', markersize=10)
    plt.pause(0.05)

plt.show()
