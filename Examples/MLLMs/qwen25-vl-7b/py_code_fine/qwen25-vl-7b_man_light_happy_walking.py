
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Right shoulder
    [-1, 0],  # Left shoulder
    [2, 0],  # Right hip
    [-2, 0],  # Left hip
    [1, 1],  # Right elbow
    [-1, 1],  # Left elbow
    [2, -1],  # Right knee
    [-2, -1],  # Left knee
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate walking by slightly adjusting the positions
    for i in range(len(positions)):
        if i % 2 == 0:
            positions[i][0] += 0.05 * (-1 if i < 4 else 1)
        else:
            positions[i][1] += 0.05 * (-1 if i < 4 else 1)
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
