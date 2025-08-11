
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_points = 15
jump_height = 3
frames = 100

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 5)
ax.set_facecolor('black')
ax.set_xticks([])  # Remove x ticks
ax.set_yticks([])  # Remove y ticks

# Initialize point-light positions
# Simulate a happy man with 15 points (head, body, arms, legs)
point_positions = np.array([
    [0, 4],  # head
    [-0.5, 3], [0.5, 3],  # shoulders
    [-1, 2], [1, 2],  # arms
    [0, 2],  # body
    [-0.5, 1], [0.5, 1],  # legs
    [-1, 0], [1, 0],  # feet
    [-1, 4.5], [1, 4.5],  # hands above head (jumping)
])

# Create scatter for points
points = ax.scatter(point_positions[:, 0], point_positions[:, 1], color='white')

def update(frame):
    # Clear previous positions
    new_y_positions = point_positions[:, 1]

    # Calculate the upward jump motion
    if frame <= frames // 2:
        # Ascending
        new_y_positions += 0.1 * (1 - np.cos(np.pi * frame / (frames / 2))) * jump_height
    else:
        # Descending
        new_y_positions -= 0.1 * (1 - np.cos(np.pi * (frame - frames // 2) / (frames / 2))) * jump_height

    # Update the points
    points.set_offsets(np.column_stack((point_positions[:, 0], new_y_positions)))
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50)

# Display the animation
plt.show()
