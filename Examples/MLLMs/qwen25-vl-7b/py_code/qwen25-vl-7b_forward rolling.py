
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0], [1, 0], [2, 0], [3, 0], [4, 0],
    [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
    [0, 2], [1, 2], [2, 2], [3, 2], [4, 2]
]

# Define the number of frames
num_frames = 15

# Define the function to update the positions of the points
def update(frame):
    # Calculate the new positions based on the forward rolling motion
    new_positions = []
    for i in range(len(positions)):
        x, y = positions[i]
        if i % 2 == 0:
            new_x = x + frame * 0.1
            new_y = y - frame * 0.1
        else:
            new_x = x - frame * 0.1
            new_y = y + frame * 0.1
        new_positions.append([new_x, new_y])
    positions = new_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
scatter = ax.scatter(*zip(*positions), color='white', s=100)

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=100, repeat=False)

# Show the animation
plt.show()
