
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the body parts and their initial positions
body_parts = ['head', 'torso', 'left_shoulder', 'left_elbow', 'left_hand',
              'right_shoulder', 'right_elbow', 'right_hand', 'left_hip',
              'left_knee', 'left_ankle', 'right_hip', 'right_knee', 'right_ankle']
initial_positions = {
    'head': [0, 2],
    'torso': [0, 1],
    'left_shoulder': [-0.5, 1],
    'left_elbow': [-0.75, 0.75],
    'left_hand': [-1, 0.5],
    'right_shoulder': [0.5, 1],
    'right_elbow': [0.75, 0.75],
    'right_hand': [1, 0.5],
    'left_hip': [-0.5, -1],
    'left_knee': [-0.5, -1.5],
    'left_ankle': [-0.5, -2],
    'right_hip': [0.5, -1],
    'right_knee': [0.5, -1.5],
    'right_ankle': [0.5, -2]
}

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Scatter plot for the point-lights
scat = ax.scatter([], [], c='white', s=50)

# Function to update the scatter plot with new positions
def update(frame):
    positions = {part: pos for part, pos in initial_positions.items()}
    # Simulate waving hand motion
    positions['right_hand'] = [np.sin(frame / 10), np.cos(frame / 10)]
    positions['right_elbow'] = [positions['right_hand'][0] * 0.75, positions['right_hand'][1] * 0.75]
    
    x = [pos[0] for pos in positions.values()]
    y = [pos[1] for pos in positions.values()]
    scat.set_offsets(np.c_[x, y])
    return scat,

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

plt.show()
