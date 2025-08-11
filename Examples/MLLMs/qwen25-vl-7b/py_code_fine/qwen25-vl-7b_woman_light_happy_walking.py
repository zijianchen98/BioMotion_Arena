
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points for the walking woman
positions = [
    [0, 0],  # Head
    [1, -1], # Left shoulder
    [2, -1], # Right shoulder
    [3, -1], # Left hip
    [4, -1], # Right hip
    [5, -1], # Left knee
    [6, -1], # Right knee
    [7, -1], # Left ankle
    [8, -1], # Right ankle
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Update the position of each point based on the walking motion
    for i in range(len(positions)):
        if i % 2 == 0:
            positions[i][0] += 0.1 * (-1)**i  # Head moves left and right
        else:
            positions[i][0] += 0.1 * (-1)**(i-1)  # Body parts move forward and backward
    # Ensure the points stay within the frame
    positions = np.clip(positions, 0, 9)
    # Plot the points
    ax.clear()
    ax.scatter(*zip(*positions), color='white', s=100)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 9)
ax.set_ylim(0, 9)
ax.axis('off')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, repeat=False)

plt.show()
