
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points for the happyman jumping up
positions = [
    [0, 0],  # Left foot
    [1, 0],  # Right foot
    [0, 1],  # Left knee
    [1, 1],  # Right knee
    [0, 2],  # Left hip
    [1, 2],  # Right hip
    [0.5, 3],  # Left shoulder
    [1.5, 3],  # Right shoulder
    [0.75, 4],  # Left elbow
    [1.25, 4],  # Right elbow
    [0.5, 5],  # Left hand
    [1.5, 5],  # Right hand
    [0.5, 6],  # Left knee
    [1.5, 6],  # Right knee
    [0, 7]  # Left foot
]

# Function to update the positions of the points
def update(frame):
    global positions
    positions[0][1] += 0.1 * np.sin(frame / 10)
    positions[1][1] += 0.1 * np.sin(frame / 10)
    positions[2][1] += 0.1 * np.cos(frame / 10)
    positions[3][1] += 0.1 * np.cos(frame / 10)
    positions[4][1] += 0.1 * np.sin(frame / 10)
    positions[5][1] += 0.1 * np.sin(frame / 10)
    positions[6][1] += 0.1 * np.cos(frame / 10)
    positions[7][1] += 0.1 * np.cos(frame / 10)
    positions[8][1] += 0.1 * np.sin(frame / 10)
    positions[9][1] += 0.1 * np.sin(frame / 10)
    positions[10][1] += 0.1 * np.cos(frame / 10)
    positions[11][1] += 0.1 * np.cos(frame / 10)
    positions[12][1] += 0.1 * np.sin(frame / 10)
    positions[13][1] += 0.1 * np.sin(frame / 10)
    positions[14][1] += 0.1 * np.cos(frame / 10)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 2)
ax.set_ylim(0, 8)
ax.axis('off')

# Plot the points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialize the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, repeat=False)

plt.show()
