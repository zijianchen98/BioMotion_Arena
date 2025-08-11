
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Left shoulder
    [2, 0],  # Right shoulder
    [3, 0],  # Left elbow
    [4, 0],  # Right elbow
    [5, 0],  # Left wrist
    [6, 0],  # Right wrist
    [7, 0],  # Left hand
    [8, 0],  # Right hand
    [9, 0],  # Left hip
    [10, 0], # Right hip
    [11, 0], # Left knee
    [12, 0], # Right knee
    [13, 0], # Left ankle
    [14, 0]  # Right ankle
]

# Define the initial positions
initial_positions = np.array(positions)

# Define the function to update the positions
def update(frame):
    global positions
    # Simulate a wave-like motion for the hands
    positions[7][1] = np.sin(frame / 10) * 0.5 + 0.5  # Left hand
    positions[8][1] = -np.sin(frame / 10) * 0.5 + 0.5  # Right hand
    
    # Update the plot
    scatter.set_offsets(positions)
    return scatter,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 1)
ax.axis('off')

# Create the scatter plot
scatter = ax.scatter(*initial_positions.T, color='white', s=100)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

plt.show()
