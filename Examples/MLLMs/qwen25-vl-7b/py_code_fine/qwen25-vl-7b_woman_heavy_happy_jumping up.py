
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Left shoulder
    [2, 0],  # Right shoulder
    [3, 0],  # Left hip
    [4, 0],  # Right hip
    [5, 0],  # Left knee
    [6, 0],  # Right knee
    [7, 0],  # Left ankle
    [8, 0],  # Right ankle
    [9, 0],  # Left hand
    [10, 0], # Right hand
    [11, 0], # Left foot
    [12, 0], # Right foot
    [13, 0], # Left toe
    [14, 0]  # Right toe
]

# Define the initial positions
initial_positions = np.array(positions)

# Define the function to update the positions
def update(frame):
    global positions
    # Simulate jumping up
    positions[0][1] += frame * 0.1  # Head moves upwards
    positions[1][1] += frame * 0.1  # Left shoulder moves upwards
    positions[2][1] += frame * 0.1  # Right shoulder moves upwards
    positions[3][1] += frame * 0.1  # Left hip moves upwards
    positions[4][1] += frame * 0.1  # Right hip moves upwards
    positions[5][1] += frame * 0.1  # Left knee moves upwards
    positions[6][1] += frame * 0.1  # Right knee moves upwards
    positions[7][1] += frame * 0.1  # Left ankle moves upwards
    positions[8][1] += frame * 0.1  # Right ankle moves upwards
    positions[9][1] += frame * 0.1  # Left hand moves upwards
    positions[10][1] += frame * 0.1  # Right hand moves upwards
    positions[11][1] += frame * 0.1  # Left foot moves upwards
    positions[12][1] += frame * 0.1  # Right foot moves upwards
    positions[13][1] += frame * 0.1  # Left toe moves upwards
    positions[14][1] += frame * 0.1  # Right toe moves upwards

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 15)
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*initial_positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, repeat=False)

plt.show()
