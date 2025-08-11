
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points for the happyman jumping up
positions = [
    [0, 0],  # Left foot
    [1, 0],  # Right foot
    [2, 0],  # Left knee
    [3, 0],  # Right knee
    [4, 0],  # Left hip
    [5, 0],  # Right hip
    [6, 0],  # Left shoulder
    [7, 0],  # Right shoulder
    [8, 0],  # Left elbow
    [9, 0],  # Right elbow
    [10, 0], # Left hand
    [11, 0], # Right hand
    [12, 0], # Head
    [13, 0], # Left eye
    [14, 0]  # Right eye
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate jumping up by slightly moving the points upwards
    positions = [[x, y + frame / 10] for x, y in positions]
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 1)
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(15), interval=100)

plt.show()
