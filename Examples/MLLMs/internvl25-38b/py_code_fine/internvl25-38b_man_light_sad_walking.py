
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions for the 15 point-lights
# The positions are arranged to represent a sadman
initial_positions = np.array([
    [0, 3], [1, 2], [2, 3], [3, 2], [4, 3],  # Shoulders and head
    [1, 1], [2, 1], [3, 1],  # Arms
    [0, 0], [1, 0], [2, 0], [3, 0], [4, 0],  # Torso
    [1, -1], [3, -1],  # Legs
    [2, -2]  # Feet
])

# Define the walking animation function
def update(frame):
    dt = 0.1
    # Update positions to simulate walking
    positions[:, 1] = np.sin(frame * dt * np.pi) * 0.5 * (np.cos(positions[:, 0] * np.pi / 2) - 1)
    scatter.set_offsets(positions)

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 6)
ax.set_ylim(-3, 4)
ax.axis('off')
positions = initial_positions.copy()
scatter = ax.scatter(positions[:, 0], positions[:, 1], c='white')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
