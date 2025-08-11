
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0], [1, 0], [2, 0], [3, 0], [4, 0],
    [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
    [0, 2], [1, 2], [2, 2], [3, 2], [4, 2]
]

# Define the initial positions for the sadman forward rolling
initial_positions = [
    [0, 0], [1, 0], [2, 0], [3, 0], [4, 0],
    [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
    [0, 2], [1, 2], [2, 2], [3, 2], [4, 2]
]

# Define the number of frames
num_frames = 15

# Define the function to update the positions for each frame
def update(frame):
    global positions
    # Update the positions for the sadman forward rolling
    positions = [
        [0, -frame], [1, -frame], [2, -frame], [3, -frame], [4, -frame],
        [0, -frame+1], [1, -frame+1], [2, -frame+1], [3, -frame+1], [4, -frame+1],
        [0, -frame+2], [1, -frame+2], [2, -frame+2], [3, -frame+2], [4, -frame+2]
    ]

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
scatter = ax.scatter(*zip(*initial_positions), color='white', s=100)

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=100, repeat=False)

# Show the animation
plt.show()
