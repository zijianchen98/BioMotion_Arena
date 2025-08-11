
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
    [1, -3],  # Left knee
    [-1, -3],  # Right knee
    [0, -4],  # Left ankle
    [2, -4],  # Right ankle
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate a smooth movement by slightly adjusting each point's position
    for i in range(len(positions)):
        positions[i] = [positions[i][0] + np.random.normal(0, 0.1), positions[i][1] + np.random.normal(0, 0.1)]
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 0)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
