
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Left foot
    [1, 0],  # Right foot
    [2, 0],  # Left knee
    [3, 0],  # Right knee
    [4, 0],  # Left hip
    [5, 0],  # Right hip
    [6, 0],  # Left shoulder
    [7, 0],  # Right shoulder
    [8, 0],  # Left elbow
    [9, 0],  # Right elbow
    [10, 0], # Left wrist
    [11, 0], # Right wrist
    [12, 0], # Left hand
    [13, 0], # Right hand
    [14, 0]  # Head
]

# Define the number of frames
num_frames = 15

# Define the time interval between frames in milliseconds
interval = 100

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 1)
ax.axis('off')

# Plot the initial positions
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Define the function to update the positions
def update(frame):
    for i in range(len(positions)):
        if frame % 2 == 0:
            positions[i][1] += 0.1 * (-1)**i  # Jumping up
        else:
            positions[i][1] -= 0.1 * (-1)**i  # Falling down
    for pos in positions:
        ax.plot(pos[0], pos[1], 'o', color='white')
    return ax,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=interval, blit=True)

# Show the animation
plt.show()
