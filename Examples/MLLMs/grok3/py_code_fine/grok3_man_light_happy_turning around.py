
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of 15 point-lights for a human turning around
# Positions represent key joints: head, shoulders, elbows, wrists, hips, knees, ankles
t = np.linspace(0, 2 * np.pi, 100)  # Time steps for one full turn
base_positions = np.array([
    [0, 1.6],  # Head
    [-0.3, 1.3], [0.3, 1.3],  # Shoulders
    [-0.6, 1.0], [0.6, 1.0],  # Elbows
    [-0.9, 0.7], [0.9, 0.7],  # Wrists
    [0, 1.0],  # Spine
    [-0.2, 0.6], [0.2, 0.6],  # Hips
    [-0.3, 0.3], [0.3, 0.3],  # Knees
    [-0.4, 0], [0.4, 0]       # Ankles
]) * 0.5  # Scale down for better visualization

# Function to update positions for turning motion
def update(frame):
    angle = t[frame]
    # Rotate around the vertical axis (y-axis in 2D projection)
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    positions = base_positions @ rotation_matrix.T
    scatter.set_offsets(positions)
    return scatter,

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 2)
ax.axis('off')

# Initialize scatter plot with white point-lights
scatter = ax.scatter([], [], c='white', s=50)

# Create animation
ani = FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)

plt.show()
