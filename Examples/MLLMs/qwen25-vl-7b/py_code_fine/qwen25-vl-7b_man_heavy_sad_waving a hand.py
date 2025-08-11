
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Right shoulder
    [-1, 0],  # Left shoulder
    [2, 0],  # Right elbow
    [0, -1],  # Right wrist
    [-2, 0],  # Left elbow
    [0, -2],  # Left wrist
    [0, -3],  # Hand
    [0, -4],  # Hand
    [0, -5],  # Hand
    [0, -6],  # Hand
    [0, -7],  # Hand
    [0, -8],  # Hand
    [0, -9],  # Hand
    [0, -10]  # Hand
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate a wave-like motion for the hand
    positions[11][1] += 0.1 * np.sin(frame / 10)
    positions[12][1] += 0.1 * np.sin(frame / 10 + np.pi / 2)
    positions[13][1] += 0.1 * np.sin(frame / 10 + np.pi)
    positions[14][1] += 0.1 * np.sin(frame / 10 + 3 * np.pi / 2)
    positions[15][1] += 0.1 * np.sin(frame / 10 + 2 * np.pi)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-11, 1)
ax.set_aspect('equal')
ax.axis('off')

# Plot the points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialize the positions
for i in range(len(positions)):
    positions[i] = [positions[i][0], -positions[i][1]]  # Flip y-axis for proper orientation

# Animate the points
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, init_func=lambda: None)

plt.show()
