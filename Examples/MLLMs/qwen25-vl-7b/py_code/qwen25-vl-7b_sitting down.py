
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Right shoulder
    [-1, 0], # Left shoulder
    [2, 0],  # Right hip
    [-2, 0], # Left hip
    [1, -1], # Right knee
    [-1, -1],# Left knee
    [1, -2], # Right ankle
    [-1, -2],# Left ankle
    [0, 1],  # Right hand
    [0, -1], # Left hand
    [0, -2], # Right foot
    [0, -3], # Left foot
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate a smooth movement of the points
    for i in range(len(positions)):
        positions[i][0] += np.random.normal(0, 0.1)
        positions[i][1] += np.random.normal(0, 0.1)
    
    # Ensure points stay within a reasonable range
    for i in range(len(positions)):
        if positions[i][0] > 3:
            positions[i][0] = 3
        elif positions[i][0] < -3:
            positions[i][0] = -3
        if positions[i][1] > 3:
            positions[i][1] = 3
        elif positions[i][1] < -3:
            positions[i][1] = -3

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white', markersize=10)

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, repeat=False)

plt.show()
