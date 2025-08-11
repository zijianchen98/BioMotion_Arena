
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
            positions[i][0] += 0.1 * (-1 if i < 4 else 1)
            positions[i][1] += 0.1 * (-1 if i < 4 else 1)
        else:
            positions[i][0] += 0.1 * (-1 if i < 4 else 1)
            positions[i][1] += 0.1 * (-1 if i < 4 else 1)
    
    # Ensure the points stay within the frame
    for i in range(len(positions)):
        if positions[i][0] > 3 or positions[i][0] < -3:
            positions[i][0] = initial_positions[i][0]
        if positions[i][1] > 3 or positions[i][1] < -3:
            positions[i][1] = initial_positions[i][1]

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
