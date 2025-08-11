
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 points representing the sadman
initial_positions = {
    'head': [0.5, 0.7],
    'torso': [0.5, 0.5],
    'left_shoulder': [0.4, 0.6],
    'right_shoulder': [0.6, 0.6],
    'left_elbow': [0.3, 0.5],
    'right_elbow': [0.7, 0.5],
    'left_wrist': [0.2, 0.4],
    'right_wrist': [0.8, 0.4],
    'left_hip': [0.4, 0.4],
    'right_hip': [0.6, 0.4],
    'left_knee': [0.3, 0.3],
    'right_knee': [0.7, 0.3],
    'left_ankle': [0.2, 0.2],
    'right_ankle': [0.8, 0.2],
    'center_of_mass': [0.5, 0.4]
}

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide the axes

# Scatter plot for the initial positions
scatter = ax.scatter(*zip(*initial_positions.values()), color='white')

def update(frame):
    """
    Update the position of each point according to the forward roll motion.
    """
    angle = np.deg2rad(frame * 10 % 360)
    sin_angle, cos_angle = np.sin(angle), np.cos(angle)

    # Apply rotation around the center of mass
    for key in initial_positions:
        if key != 'center_of_mass':
            x, y = initial_positions[key]
            cm_x, cm_y = initial_positions['center_of_mass']
            new_x = cm_x + (x - cm_x) * cos_angle - (y - cm_y) * sin_angle
            new_y = cm_y + (x - cm_x) * sin_angle + (y - cm_y) * cos_angle
            initial_positions[key] = [new_x, new_y]

    scatter.set_offsets(list(initial_positions.values()))

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 36), interval=50)

plt.show()
