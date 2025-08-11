
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points for the sad woman running
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

# Plot the initial position of the points
for x, y in positions:
    ax.plot(x, y, 'o', color='white')

# Animate the points
for i in range(10):
    # Update the positions of the points
    new_positions = []
    for x, y in positions:
        dx = np.random.normal(0, 0.05)
        dy = np.random.normal(0, 0.05)
        new_x = x + dx
        new_y = y + dy
        new_positions.append([new_x, new_y])
    
    # Plot the updated positions
    for x, y in new_positions:
        ax.plot(x, y, 'o', color='white')
    
    # Show the current frame
    plt.pause(0.1)

plt.show()
