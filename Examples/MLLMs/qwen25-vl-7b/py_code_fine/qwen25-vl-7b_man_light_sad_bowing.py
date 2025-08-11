
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [-1, -1],  # Left shoulder
    [1, -1],  # Right shoulder
    [-2, -2],  # Left elbow
    [2, -2],  # Right elbow
    [-3, -3],  # Left wrist
    [3, -3],  # Right wrist
    [-4, -4],  # Left knee
    [4, -4],  # Right knee
    [-5, -5],  # Left ankle
    [5, -5],  # Right ankle
]

# Define the initial positions
initial_positions = np.array(positions)

# Define the function to update the positions
def update(frame):
    global positions
    # Simulate the bowing motion
    positions[0] = [0, -frame / 10]  # Head moves down
    positions[1] = [-1 + frame / 100, -1]  # Left shoulder moves slightly up
    positions[2] = [1 - frame / 100, -1]  # Right shoulder moves slightly up
    positions[3] = [-2 + frame / 100, -2]  # Left elbow moves slightly up
    positions[4] = [2 - frame / 100, -2]  # Right elbow moves slightly up
    positions[5] = [-3 + frame / 100, -3]  # Left wrist moves slightly up
    positions[6] = [3 - frame / 100, -3]  # Right wrist moves slightly up
    positions[7] = [-4 + frame / 100, -4]  # Left knee moves slightly up
    positions[8] = [4 - frame / 100, -4]  # Right knee moves slightly up
    positions[9] = [-5 + frame / 100, -5]  # Left ankle moves slightly up
    positions[10] = [5 - frame / 100, -5]  # Right ankle moves slightly up

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 0)
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*initial_positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, repeat=False)

plt.show()
