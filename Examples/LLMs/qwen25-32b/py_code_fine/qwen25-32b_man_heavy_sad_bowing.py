
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the lights in the initial state
initial_positions = {
    'head': [0, 0],
    'left_shoulder': [-0.5, -1],
    'right_shoulder': [0.5, -1],
    'left_hip': [-0.5, -2],
    'right_hip': [0.5, -2],
    'left_knee': [-0.5, -3],
    'right_knee': [0.5, -3],
    'left_ankle': [-0.5, -4],
    'right_ankle': [0.5, -4],
}

# Convert dictionary to list of lists
positions = [initial_positions[key] for key in initial_positions]

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-6, 2)
ax.axis('off')  # Hide the axes

# Scatter plot for the point-lights
scat = ax.scatter(*zip(*positions), color='white', s=50)

def update(frame):
    global positions
    
    # Bowing motion simulation
    if frame <= 50:
        angle = np.radians(10 * frame / 50)
        for i, joint in enumerate(initial_positions.keys()):
            if joint in ['left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle']:
                positions[i][1] = initial_positions[joint][1] + np.sin(angle) * 1.5
                positions[i][0] += np.cos(angle) * 0.5 * (-1 if 'left' in joint else 1)
    elif frame > 50 and frame <= 100:
        angle = np.radians(10 * (100 - frame) / 50)
        for i, joint in enumerate(initial_positions.keys()):
            if joint in ['left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle']:
                positions[i][1] = initial_positions[joint][1] + np.sin(angle) * 1.5
                positions[i][0] += np.cos(angle) * 0.5 * (-1 if 'left' in joint else 1)
    
    # Update scatter plot data
    scat.set_offsets(positions)

# Create animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=40)

plt.show()
