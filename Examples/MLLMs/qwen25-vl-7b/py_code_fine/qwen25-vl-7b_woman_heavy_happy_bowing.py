
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1],  # Left shoulder
    [-1, -1],  # Right shoulder
    [0, -2],  # Left hip
    [2, -2],  # Right hip
    [0, -3],  # Left knee
    [2, -3],  # Right knee
    [0, -4],  # Left ankle
    [2, -4]   # Right ankle
]

# Define the initial positions
initial_positions = positions.copy()

# Define the function to update the positions
def update(frame):
    global positions
    for i in range(len(positions)):
        if i % 2 == 0:
            positions[i][1] += 0.1 * (-1 if i == 0 else 1)
        else:
            positions[i][1] += 0.1 * (1 if i == 1 or i == 3 else -1)
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 0)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
for pos in initial_positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
