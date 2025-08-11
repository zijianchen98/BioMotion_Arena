
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

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 3)
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white')

def update(frame):
    # Update the positions of the points
    positions[frame] = [frame, frame % 3]
    points.set_data(*zip(*positions))
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=100, blit=True)

plt.show()
