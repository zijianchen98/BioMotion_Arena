
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified human figure)
def init_positions():
    # Head, shoulders, elbows, wrists, hips, knees, ankles
    positions = np.array([
        [0, 10],    # Head
        [-2, 8],    # Left shoulder
        [2, 8],     # Right shoulder
        [-3, 6],    # Left elbow
        [3, 6],     # Right elbow
        [-4, 4],    # Left wrist
        [4, 4],     # Right wrist
        [0, 2],     # Hip (center)
        [-1, 0],    # Left hip
        [1, 0],     # Right hip
        [-1.5, -2], # Left knee
        [1.5, -2],  # Right knee
        [-2, -4],   # Left ankle
        [2, -4],    # Right ankle
        [0, -6]     # Base (weighted effect)
    ])
    return positions

# Simulate turning around motion with biomechanical plausibility
def update_positions(frame, positions, speed=0.1, angle_increment=5):
    # Rotate around the hip (center) with a slight wobble for weight
    angle = np.radians(angle_increment * frame)
    center = positions[7]  # Hip center
    for i in range(len(positions)):
        if i != 7:  # Exclude hip center from rotation
            # Translate to origin, rotate, and translate back
            rel_pos = positions[i] - center
            rotated_x = rel_pos[0] * np.cos(angle) - rel_pos[1] * np.sin(angle)
            rotated_y = rel_pos[0] * np.sin(angle) + rel_pos[1] * np.cos(angle)
            positions[i] = np.array([rotated_x, rotated_y]) + center
            # Add slight vertical wobble to simulate heavy weight
            if i in [12, 13, 14]:  # Ankles and base
                positions[i][1] += 0.1 * np.sin(frame * 0.5)
    return positions

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-6, 6)
ax.set_ylim(-8, 12)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
positions = init_positions()
scatter = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Animation update function
def update(frame):
    positions = update_positions(frame, positions)
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=range(0, 72), interval=50, blit=True)

plt.show()
