
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights representing the happyman sitting down
initial_positions = {
    'head': [0, 2],
    'left_shoulder': [-1, 1],
    'right_shoulder': [1, 1],
    'left_elbow': [-2, 0],
    'right_elbow': [2, 0],
    'left_wrist': [-2, -1],
    'right_wrist': [2, -1],
    'left_hip': [-1, -2],
    'right_hip': [1, -2],
    'left_knee': [-1, -3],
    'right_knee': [1, -3],
    'left_ankle': [-1, -4],
    'right_ankle': [1, -4]
}

# Convert dictionary to list of positions
positions = np.array(list(initial_positions.values()))

# Function to simulate the motion of sitting down
def sit_down(t):
    # Simplified motion for demonstration purposes
    y_offset = max(0, 2 * (1 - t))
    hip_offset = 0.5 * np.sin(np.pi * t)
    knee_offset = 0.5 * np.sin(np.pi * t)
    
    new_positions = positions.copy()
    new_positions[:, 1] -= y_offset
    new_positions[7:9, 0] += hip_offset  # Move hips slightly apart
    new_positions[9:11, 1] -= knee_offset  # Bend knees
    return new_positions

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 3)
ax.axis('off')  # Hide the axes

# Scatter plot for the point-lights
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Update function for animation
def update(frame):
    new_positions = sit_down(frame / 30.0)
    scat.set_offsets(new_positions)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 31), interval=40, repeat=False)

plt.show()
