
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1],  # Left shoulder
    [-1, -1],  # Right shoulder
    [0, -2],  # Left hip
    [2, -2],  # Left knee
    [0, -3],  # Left ankle
    [-2, -2],  # Right knee
    [0, -4],  # Right ankle
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate walking by slightly adjusting the positions
    for i in range(len(positions)):
        if i == 0:  # Head
            positions[i][1] -= 0.05 * frame % 100  # Slight downward movement
        elif i == 1 or i == 2:  # Shoulders
            positions[i][1] += 0.05 * frame % 100  # Slight upward movement
        else:
            positions[i][1] += 0.05 * frame % 100  # Slight upward movement
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 0)
ax.axis('off')

# Animate the points
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
