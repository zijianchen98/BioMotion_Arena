
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1], # Left shoulder
    [2, -1], # Right shoulder
    [1, -2], # Left elbow
    [2, -2], # Right elbow
    [1, -3], # Left wrist
    [2, -3], # Right wrist
    [1, -4], # Left hand
    [2, -4], # Right hand
    [1, -5], # Left knee
    [2, -5], # Right knee
    [1, -6], # Left foot
    [2, -6], # Right foot
]

# Define the initial positions
initial_positions = np.array(positions)

# Define the function to update the positions
def update(frame):
    global positions
    # Simulate the movement of the points
    # For simplicity, we'll just shift each point slightly
    positions = np.array([
        [x + np.random.uniform(-0.1, 0.1), y + np.random.uniform(-0.1, 0.1)]
        for x, y in positions
    ])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim([-3, 3])
ax.set_ylim([-7, 1])
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*initial_positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, repeat=False)

# Show the animation
plt.show()
