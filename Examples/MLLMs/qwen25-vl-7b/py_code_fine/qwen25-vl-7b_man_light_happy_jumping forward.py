
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points for the happyman jumping forward
positions = [
    [0, 0],  # Left foot
    [1, 0],  # Right foot
    [0, 1],  # Left knee
    [1, 1],  # Right knee
    [0, 2],  # Left hip
    [1, 2],  # Right hip
    [0.5, 3],  # Left shoulder
    [1.5, 3],  # Right shoulder
    [0.75, 4],  # Left elbow
    [1.25, 4],  # Right elbow
    [0.5, 5],  # Left hand
    [1.5, 5],  # Right hand
    [0.5, 6],  # Left knee
    [1.5, 6],  # Right knee
    [0, 7]  # Left foot
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate a jump by slightly adjusting the positions
    for i in range(len(positions)):
        positions[i][0] += 0.05 * (-1 if i % 2 == 0 else 1)
        positions[i][1] += 0.05 * (-1 if i % 2 == 0 else 1)
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 2)
ax.set_ylim(0, 8)
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
