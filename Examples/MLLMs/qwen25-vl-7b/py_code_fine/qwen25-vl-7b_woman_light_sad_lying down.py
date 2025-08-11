
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1], # Left shoulder
    [-1, -1],# Right shoulder
    [0, -2], # Left hip
    [1, -2], # Left knee
    [-1, -2],# Right knee
    [0, -3], # Left ankle
    [1, -3], # Left foot
    [-1, -3] # Right foot
]

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial position
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Animate the movement
def update(frame):
    for i, pos in enumerate(positions):
        if frame % 2 == 0:
            positions[i][1] -= 0.1
        else:
            positions[i][1] += 0.1
    for pos in positions:
        ax.plot(pos[0], pos[1], 'o', color='white')

ani = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
