
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of point-lights
num_points = 15
points = [plt.Circle((0, 0), 0.1, color='white') for _ in range(num_points)]
for point in points:
    ax.add_artist(point)

# Define the jump parameters
jump_height = np.linspace(0, 2, 10)
jump_distance = np.linspace(0, 4, 10)

def update(frame):
    # Calculate the new positions for the points
    if frame < 10:
        # Ascending
        y_positions = jump_height[frame] * np.array([1, 0.5, 0, -0.5, -1] * 3)
        x_positions = np.full_like(y_positions, jump_distance[frame])  # Constant forward movement
    else:
        # Descending
        y_positions = jump_height[19 - frame] * np.array([1, 0.5, 0, -0.5, -1] * 3)
        x_positions = np.full_like(y_positions, jump_distance[-1])  # Constant forward

    # Update the position of each point
    for i, point in enumerate(points):
        point.center = x_positions[i % len(y_positions)], y_positions[i % len(y_positions)]

    return points

# Create and start the animation
ani = FuncAnimation(fig, update, frames=20, interval=100, blit=True)

plt.show()
