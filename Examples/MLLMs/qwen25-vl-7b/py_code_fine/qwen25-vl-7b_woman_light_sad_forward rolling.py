
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
    global positions
    # Update the positions of the points in a forward rolling motion
    positions = np.roll(positions, -1, axis=0)
    # Set the position of the last point to the starting position
    positions[-1] = [0, 0]

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')
ax.axis('off')

# Plot the points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=100, repeat=False)

# Show the animation
plt.show()
