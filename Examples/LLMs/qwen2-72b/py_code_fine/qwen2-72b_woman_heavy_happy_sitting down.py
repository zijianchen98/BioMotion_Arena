
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions of the points that represent body parts.
# This is a very rough representation for simplicity.
initial_positions = np.array([
    [0.5, 0.9],  # head
    [0.4, 0.7],  # left shoulder
    [0.6, 0.7],  # right shoulder
    [0.3, 0.5],  # left hip
    [0.7, 0.5],  # right hip
    [0.35, 0.4],  # left knee
    [0.65, 0.4],  # right knee
    [0.3, 0.3],  # left foot
    [0.7, 0.3]   # right foot
])

# Define the function to update the positions of the points over time.
def update(frame):
    # Calculate new positions based on frame number (time).
    # For simplicity, we assume the person is sitting down by lowering all points.
    new_positions = initial_positions - frame * 0.01
    scatter.set_offsets(new_positions)

# Set up the plot.
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Create the animation.
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
