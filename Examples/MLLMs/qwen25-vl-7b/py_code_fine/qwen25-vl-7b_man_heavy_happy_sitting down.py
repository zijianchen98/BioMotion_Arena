
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Right shoulder
    [-1, 0],  # Left shoulder
    [2, -1],  # Right hip
    [-2, -1],  # Left hip
    [1, -2],  # Right knee
    [-1, -2],  # Left knee
    [1.5, -3],  # Right foot
    [-1.5, -3],  # Left foot
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate the movement of the points
    for i in range(len(positions)):
        positions[i][0] += np.random.uniform(-0.1, 0.1)
        positions[i][1] += np.random.uniform(-0.1, 0.1)
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 0)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
