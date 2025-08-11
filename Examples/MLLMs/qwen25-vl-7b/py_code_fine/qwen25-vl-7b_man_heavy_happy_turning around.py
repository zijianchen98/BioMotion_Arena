
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Right shoulder
    [-1, 0],  # Left shoulder
    [2, 0],  # Right hip
    [-2, 0],  # Left hip
    [1, 1],  # Right elbow
    [-1, 1],  # Left elbow
    [2, -1],  # Right knee
    [-2, -1],  # Left knee
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate turning around by rotating the body
    angle = frame * 2 * np.pi / 15  # 24 degrees per frame
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    new_positions = []
    for pos in positions:
        new_pos = np.dot(rotation_matrix, pos)
        new_positions.append(new_pos)
    positions = new_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=15, interval=100)

plt.show()
