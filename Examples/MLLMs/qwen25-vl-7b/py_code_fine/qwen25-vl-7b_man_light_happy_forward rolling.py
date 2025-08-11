
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
    # Update the position of each point
    for i in range(len(positions)):
        positions[i][0] += frame / num_frames * 0.1
        if positions[i][0] > 4:
            positions[i][0] = 0
        elif positions[i][0] < 0:
            positions[i][0] = 4
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 4)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot
scatter = ax.scatter(*zip(*positions), color='white', s=100)

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=100, blit=True)

# Show the animation
plt.show()
