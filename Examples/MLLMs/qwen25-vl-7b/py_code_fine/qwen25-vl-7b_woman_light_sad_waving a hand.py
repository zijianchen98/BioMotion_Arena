
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
]

# Define the initial positions
initial_positions = np.array(positions)

# Define the function to update the positions
def update(frame):
    global positions
    # Simulate a wave-like motion for the hand
    positions[9] += np.sin(frame * 0.1) * 0.5  # Hand moves up and down
    # Ensure the positions stay within a reasonable range
    positions = np.clip(positions, -5, 5)
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*initial_positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Display the animation
plt.show()
