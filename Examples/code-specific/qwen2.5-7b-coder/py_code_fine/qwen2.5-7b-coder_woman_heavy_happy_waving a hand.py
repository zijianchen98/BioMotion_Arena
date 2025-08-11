
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point lights
num_lights = 15
positions = np.random.rand(num_lights, 2) * 8 - 4  # Random positions within [-4, 4]

# Define the target positions for waving hands
target_positions = np.array([
    [0, -3], [0, -2], [0, -1], [0, 0], [0, 1], [0, 2], [0, 3],
    [1, -2], [1, -1], [1, 0], [1, 1], [1, 2],
    [-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2]
])

# Function to update the positions of the point lights
def update(frame):
    global positions
    # Interpolate between current and target positions
    positions += 0.05 * (target_positions - positions)
    # Ensure positions stay within bounds
    positions[:, 0] = np.clip(positions[:, 0], -4, 4)
    positions[:, 1] = np.clip(positions[:, 1], -4, 4)
    # Update scatter plot data
    sc.set_offsets(positions)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create scatter plot for the point lights
sc = ax.scatter([], [], s=100, color='white')

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(100), interval=50)

plt.show()
