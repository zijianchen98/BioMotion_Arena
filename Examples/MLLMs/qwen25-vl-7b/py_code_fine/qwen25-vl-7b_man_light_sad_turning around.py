
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [-1, -1],  # Left shoulder
    [1, -1],  # Right shoulder
    [-2, -2],  # Left hip
    [2, -2],  # Right hip
    [-3, -3],  # Left knee
    [3, -3],  # Right knee
    [-4, -4],  # Left ankle
    [4, -4],  # Right ankle
]

# Define the initial positions
initial_positions = np.array(positions)

# Define the function to update the positions
def update(frame):
    global positions
    # Simulate turning around by rotating the positions
    angle = frame * 2 * np.pi / 15  # 2pi/15 radians per frame
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    new_positions = np.dot(rotation_matrix, positions.T).T + initial_positions
    positions = new_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(15), interval=100, repeat=False)

plt.show()
