
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Left shoulder
    [-1, 0],  # Right shoulder
    [0, -1],  # Left hip
    [0, -2],  # Right hip
    [1, -1],  # Left knee
    [-1, -1],  # Right knee
    [1, -2],  # Left ankle
    [-1, -2],  # Right ankle
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate running by slightly adjusting the positions
    for i in range(len(positions)):
        positions[i][0] += 0.05 * np.sign(np.sin(frame / 10))
        positions[i][1] += 0.05 * np.sign(np.cos(frame / 10))
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 1)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
