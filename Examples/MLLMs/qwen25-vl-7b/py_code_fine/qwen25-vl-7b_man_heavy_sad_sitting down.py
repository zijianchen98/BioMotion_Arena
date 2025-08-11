
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
    [1, -4], # Left knee
    [2, -4], # Right knee
    [1, -5], # Left foot
    [2, -5], # Right foot
]

# Define the initial positions
initial_positions = np.array(positions)

# Define the function to update the positions
def update(frame):
    global positions
    # Simulate the movement of the sadman sitting down
    # This is a simple linear interpolation for demonstration purposes
    positions = np.array([
        [0, 0],
        [1, -1],
        [2, -1],
        [1, -2],
        [2, -2],
        [1, -3],
        [2, -3],
        [1, -4],
        [2, -4],
        [1, -5],
        [2, -5]
    ])
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 3)
ax.set_ylim(-6, 1)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
for pos in initial_positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
