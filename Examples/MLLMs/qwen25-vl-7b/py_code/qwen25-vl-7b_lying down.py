
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1], # Left shoulder
    [2, -1], # Right shoulder
    [3, -1], # Left hip
    [4, -1], # Right hip
    [5, -1], # Left knee
    [6, -1], # Right knee
    [7, -1], # Left ankle
    [8, -1], # Right ankle
    [9, -1], # Left hand
    [10, -1],# Right hand
    [11, -1],# Left elbow
    [12, -1],# Right elbow
    [13, -1],# Left wrist
    [14, -1] # Right wrist
]

# Function to update the positions of the points
def update(frame):
    global positions
    positions[frame % len(positions)] = [frame, frame]
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 15)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(15), interval=100)

plt.show()
