
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Left shoulder
    [-1, 0],  # Right shoulder
    [0, -1],  # Left hip
    [0, -2],  # Right hip
    [0, -3],  # Left knee
    [0, -4],  # Right knee
    [0, -5],  # Left ankle
    [0, -6],  # Right ankle
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate jumping up
    positions[0][1] += 0.1 * np.sin(frame / 10)
    positions[1][1] += 0.1 * np.sin(frame / 10)
    positions[2][1] += 0.1 * np.sin(frame / 10)
    positions[3][1] += 0.1 * np.sin(frame / 10)
    positions[4][1] += 0.1 * np.sin(frame / 10)
    positions[5][1] += 0.1 * np.sin(frame / 10)
    positions[6][1] += 0.1 * np.sin(frame / 10)
    positions[7][1] += 0.1 * np.sin(frame / 10)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-7, 0)
ax.set_aspect('equal')
ax.axis('off')

# Plot the points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialize the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, repeat=False)

plt.show()
