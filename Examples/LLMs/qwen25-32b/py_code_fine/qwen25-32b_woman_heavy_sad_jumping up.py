
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the point-lights on the sadwoman's body
body_parts = ['head', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
              'left_wrist', 'right_wrist', 'left_hip', 'right_hip', 'left_knee',
              'right_knee', 'left_ankle', 'right_ankle', 'left_toe', 'right_toe']

# Initial positions for each point-light
initial_positions = {
    'head': (0, 1),
    'left_shoulder': (-0.5, 0.5),
    'right_shoulder': (0.5, 0.5),
    'left_elbow': (-1, 0),
    'right_elbow': (1, 0),
    'left_wrist': (-1.5, -0.5),
    'right_wrist': (1.5, -0.5),
    'left_hip': (-0.5, -1),
    'right_hip': (0.5, -1),
    'left_knee': (-0.75, -1.5),
    'right_knee': (0.75, -1.5),
    'left_ankle': (-1, -2),
    'right_ankle': (1, -2),
    'left_toe': (-1.25, -2.5),
    'right_toe': (1.25, -2.5)
}

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 2)
ax.axis('off')  # Hide the axes

# Scatter plot for point-lights
scat = ax.scatter([], [], color='white')

def init():
    scat.set_offsets([])
    return scat,

def animate(i):
    # Calculate new y positions based on time (i)
    new_positions = {part: (x, y + np.sin(i/10 + offset)) for part, (x, y) in initial_positions.items() for offset in [0, 0.5]}
    
    # Update scatter plot data
    scat.set_offsets(list(new_positions.values()))
    return scat,

# Animation
ani = FuncAnimation(fig, animate, frames=100, init_func=init, blit=True, interval=50)

plt.show()
