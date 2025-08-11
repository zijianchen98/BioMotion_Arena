
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified human stick figure)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8], [2, 8],  # shoulders
    [-4, 6], [4, 6],  # elbows
    [-6, 4], [6, 4],  # wrists
    [0, 0],  # hips
    [-2, -2], [2, -2],  # knees
    [-4, -4], [4, -4]  # ankles
])

# Number of frames for the animation
frames = 60

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Scatter plot for point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Function to update positions for each frame (sitting down motion)
def update(frame):
    if frame < frames // 2:
        # Standing to sitting transition
        t = frame / (frames // 2)
        hip_y = 0 * (1 - t) + (-4) * t  # Move hips down
        knee_y = -2 * (1 - t) + (-6) * t  # Knees bend
        ankle_y = -4 * (1 - t) + (-8) * t  # Ankles lower
    else:
        # Hold sitting position
        t = (frame - frames // 2) / (frames // 2)
        hip_y = -4
        knee_y = -6
        ankle_y = -8

    # Updated positions
    positions = np.array([
        [0, 10 * (1 - t)],  # head moves down slightly
        [-2, 8 * (1 - t)], [2, 8 * (1 - t)],  # shoulders
        [-4, 6 * (1 - t)], [4, 6 * (1 - t)],  # elbows
        [-6, 4 * (1 - t)], [6, 4 * (1 - t)],  # wrists
        [0, hip_y],  # hips
        [-2, knee_y], [2, knee_y],  # knees
        [-4, ankle_y], [4, ankle_y]  # ankles
    ])
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
