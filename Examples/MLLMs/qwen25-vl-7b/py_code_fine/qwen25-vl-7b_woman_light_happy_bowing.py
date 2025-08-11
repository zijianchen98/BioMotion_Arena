
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1], # Left shoulder
    [-1, -1],# Right shoulder
    [0, -2], # Left hip
    [0, -3], # Right hip
    [1, -4], # Left knee
    [-1, -4],# Right knee
    [0, -5], # Left ankle
    [0, -6], # Right ankle
]

# Define the initial and final positions for the bowing action
initial_positions = np.array(positions)
final_positions = np.array(positions)

# Define the function to update the positions during the animation
def update(frame):
    global positions
    # Simulate a smooth transition from initial to final positions
    positions = (1 - frame / 10) * initial_positions + (frame / 10) * final_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-7, 0)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial positions
for pos in initial_positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, repeat=False)

# Display the animation
plt.show()
