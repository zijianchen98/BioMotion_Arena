
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 50],  # Head
    [4, 7],     # Left shoulder
    (6, 7),   # Right shoulder
    (3, 8),  # Left elbow
    (7, 8),  # Right elbow
    (2, 9),  # Left wrist
    (8, 9),  # Right wrist
    (5, 10),  # Pelvis
    (4, 11),  # Left hip
    (6, 11),  # Right hip
    (3, 12),  # Left knee
    (7, 12),  # Right knee
    (2, 13),  # Left ankle
    (8, 13),  # Right ankle
    (5, 14)   # Left toe
])

# Define the movement function for each joint
def move_joint(position, time):
    x, y = position
    # Simple harmonic motion for a waving hand
    if time % 2 == 0::
        y += 2 * np.sin((time / 20) * np.pi)
    else:
        y -= 2 * np.sin((time / 20) * np.pi)
    return np.array([x, y])

# Create the figure and axis
fig, ax = plt.subplots()
axg = ax.axis([-10, 15, -1, 15])
axg.set_aspect('equal')

# Initialize the scatter plot
scatter = ax.scatter(*initial_positions.T, color='white')

def update(frame):
    scatter.set_offsets(initial_positions)
    for i, pos in enumerate(initial_positions):
        new_pos = move_joint(pos, frame)
        initial_positions[i] = new_pos
    scatter.set_offsets(initial_positions)

# Create the animation
animation = FuncAnimation(fig, update, frames=range(300), interval=20, blit=True)

# Show the animation
plt.show()
