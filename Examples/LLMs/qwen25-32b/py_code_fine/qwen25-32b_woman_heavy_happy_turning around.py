
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the body parts and their initial positions
body_parts = {
    'head': [0, 0],
    'left_shoulder': [-1, -1],
    'right_shoulder': [1, -1],
    'left_elbow': [-2, -2],
    'right_elbow': [2, -2],
    'left_wrist': [-3, -3],
    'right_wrist': [3, -3],
    'left_hip': [-1, -4],
    'right_hip': [1, -4],
    'left_knee': [-2, -6],
    'right_knee': [2, -6],
    'left_ankle': [-3, -8],
    'right_ankle': [3, -8]
}

# Create a list of positions from the dictionary values
positions = np.array(list(body_parts.values()))

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
plt.axis('off')

# Scatter plot for the point lights
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Function to update the frame
def update(frame):
    angle = 2 * np.pi / 360 * frame
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    
    # Apply rotation to each position
    new_positions = np.dot(positions, rotation_matrix)
    scat.set_offsets(new_positions)

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=50)

plt.show()
