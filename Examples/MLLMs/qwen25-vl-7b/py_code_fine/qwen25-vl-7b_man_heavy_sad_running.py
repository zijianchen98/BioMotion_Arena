
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points for the sadman running
positions = [
    [0.5, 0.8], [0.4, 0.7], [0.6, 0.7], [0.5, 0.6],
    [0.4, 0.5], [0.6, 0.5], [0.5, 0.4],
    [0.4, 0.3], [0.6, 0.3], [0.5, 0.2],
    [0.4, 0.1], [0.6, 0.1], [0.5, 0.0],
    [0.4, -0.1], [0.6, -0.1]
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Smoothly interpolate between frames
    new_positions = []
    for i in range(len(positions)):
        new_pos = positions[i] + (positions[(i+1)%len(positions)] - positions[i]) * frame / 15
        new_positions.append(new_pos)
    positions = new_positions
    return [plt.scatter(x, y, color='white') for x, y in positions]

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Create the scatter plot
scatters = [plt.scatter(x, y, color='white') for x, y in positions]

# Create the animation
ani = FuncAnimation(fig, update, frames=range(15), interval=100, blit=True)

# Show the animation
plt.show()
