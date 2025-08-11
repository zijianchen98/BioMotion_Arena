
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Right shoulder
    [-1, 0], # Left shoulder
    [2, 0],  # Right elbow
    [0, -1], # Right wrist
    [-2, 0], # Left elbow
    [0, -2], # Left wrist
    [0, -3], # Hand
    [0, -4], # Hand
    [0, -5], # Hand
    [0, -6], # Hand
    [0, -7], # Hand
    [0, -8], # Hand
    [0, -9], # Hand
    [0, -10] # Hand
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate a wave-like motion for the hand
    positions[10][1] += 0.1 * np.sin(frame / 10)
    positions[11][1] += 0.1 * np.sin(frame / 10 + np.pi / 2)
    positions[12][1] += 0.1 * np.sin(frame / 10 + np.pi)
    positions[13][1] += 0.1 * np.sin(frame / 10 + 3 * np.pi / 2)
    positions[14][1] += 0.1 * np.sin(frame / 10 + 2 * np.pi)

    # Update the scatter plot
    scatter.set_offsets(positions)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-10, 0)
ax.set_aspect('equal')
ax.axis('off')

# Create a scatter plot for the points
scatter = ax.scatter(*zip(*positions), color='white', s=50)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

plt.show()
