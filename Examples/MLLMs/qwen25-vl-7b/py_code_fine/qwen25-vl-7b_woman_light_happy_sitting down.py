
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Left shoulder
    [-1, 0], # Right shoulder
    [0, -1], # Left hip
    [0, -2], # Right hip
    [0, -3], # Left knee
    [0, -4], # Right knee
    [0, -5], # Left ankle
    [0, -6], # Right ankle
    [0, -7], # Left hand
    [0, -8], # Right hand
    [0, -9], # Left foot
    [0, -10],# Right foot
]

# Define the initial positions
initial_positions = np.array(positions)

# Define the function to update the positions
def update(frame):
    global positions
    # Simulate a sitting down motion
    positions[1][1] -= 0.1  # Left shoulder moves upwards
    positions[2][1] -= 0.1  # Right shoulder moves upwards
    positions[3][1] += 0.1  # Left hip moves downwards
    positions[4][1] += 0.1  # Right hip moves downwards
    positions[5][1] += 0.1  # Left knee moves downwards
    positions[6][1] += 0.1  # Right knee moves downwards
    positions[7][1] += 0.1  # Left ankle moves downwards
    positions[8][1] += 0.1  # Right ankle moves downwards
    positions[9][1] += 0.1  # Left hand moves downwards
    positions[10][1] += 0.1  # Right hand moves downwards
    positions[11][1] += 0.1  # Left foot moves downwards
    positions[12][1] += 0.1  # Right foot moves downwards

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-10, 0)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*initial_positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, repeat=False)

plt.show()
