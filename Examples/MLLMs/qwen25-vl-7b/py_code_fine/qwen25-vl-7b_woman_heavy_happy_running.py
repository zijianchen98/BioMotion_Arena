
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points for the happy woman running
positions = [
    [0.5, 0.8], [0.4, 0.7], [0.6, 0.7],
    [0.3, 0.6], [0.5, 0.6], [0.7, 0.6],
    [0.2, 0.5], [0.4, 0.5], [0.6, 0.5],
    [0.1, 0.4], [0.3, 0.4], [0.5, 0.4],
    [0.2, 0.3], [0.4, 0.3], [0.6, 0.3]
]

# Function to update the positions of the points in each frame
def update(frame):
    # Update the position of the points based on the running motion
    positions[frame % len(positions)] = [np.random.uniform(0.1, 0.9), np.random.uniform(0.3, 0.7)]
    return positions,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Create the scatter plot
scat = ax.scatter(*zip(*positions), c='white', s=100)

# Create the animation
ani = FuncAnimation(fig, update, frames=len(positions), interval=50, blit=True)

plt.show()
