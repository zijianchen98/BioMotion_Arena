
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Left shoulder
    [2, 0],  # Right shoulder
    [3, 0],  # Left hip
    [4, 0],  # Right hip
    [5, 0],  # Left knee
    [6, 0],  # Right knee
    [7, 0],  # Left ankle
    [8, 0],  # Right ankle
]

# Define the initial positions
x, y = zip(*positions)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 9)
ax.set_ylim(-1, 1)
ax.axis('off')

# Plot the points
points, = ax.plot(x, y, 'o', color='white')

def update(frame):
    # Update the positions of the points
    x, y = zip(*positions)
    
    # Move the points in a walking pattern
    if frame % 2 == 0:
        positions[1][1] += 0.1  # Left shoulder up
        positions[2][1] += 0.1  # Right shoulder up
        positions[3][1] -= 0.1  # Left hip down
        positions[4][1] -= 0.1  # Right hip down
    else:
        positions[1][1] -= 0.1  # Left shoulder down
        positions[2][1] -= 0.1  # Right shoulder down
        positions[3][1] += 0.1  # Left hip up
        positions[4][1] += 0.1  # Right hip up
    
    # Update the plot
    points.set_data(x, y)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
