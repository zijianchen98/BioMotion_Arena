
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1],  # Left shoulder
    [-1, -1],  # Right shoulder
    [0, -2],  # Left hip
    [0, -3],  # Right hip
    [1, -4],  # Left knee
    [-1, -4],  # Right knee
    [0, -5],  # Left ankle
    [0, -6],  # Right ankle
]

# Define the initial positions
initial_positions = np.array(positions)

# Define the function to update the positions
def update(frame):
    global positions
    # Simulate a bowing motion
    positions[0] = [0, -frame / 10]  # Head moves down
    positions[1] = [1, -1 - frame / 10]  # Left shoulder moves slightly down
    positions[2] = [-1, -1 - frame / 10]  # Right shoulder moves slightly down
    positions[3] = [0, -2 - frame / 10]  # Left hip moves down
    positions[4] = [0, -3 - frame / 10]  # Right hip moves down
    positions[5] = [1, -4 - frame / 10]  # Left knee moves down
    positions[6] = [-1, -4 - frame / 10]  # Right knee moves down
    positions[7] = [0, -5 - frame / 10]  # Left ankle moves down
    positions[8] = [0, -6 - frame / 10]  # Right ankle moves down

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-7, 0)
ax.axis('off')

# Plot the initial positions
for pos in initial_positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
