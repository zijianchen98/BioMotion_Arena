
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the sadman's joints
initial_positions = {
    'head': [0, 4 ],
    'left_shoulder': [ -1, 2 ],
    'right_shoulder': [ 1, 2 ],
    'left_elbow': ( -2, 1 ),
    'right_elbow': ( 2, 1 ),
    'left_wrist': ( -3, 0 ),
    'right_wrist': ( 3,  t ),
    'left_hip': ( -2, 0 ),
    'right_hip': ( 2,  t ),
    'left_knee': ( -3,  b ),
    'right_knee': ( 3,  b ),
    'left_ankle': ( -4,  b ),
    'right_ankk': ( 4,  b )
}

# Define the movement for each joint
movements = {
    'head': lambda t: (np.sin(t/4), 4 + np.sin(t/4)),
    'left_shoulder': lambda t: (-1 + 0*np.cos(t/6), 2 + np.sin(t/6)),
    'right_shoulder': lambda t: (1 +  t*np.cos(t/6), 2 + np.sin(t/6)),
    'left_elbow': lambda t: (-2 +  t*np.cos(t/5), 1 + np.sin(t/5)),
    'right_elbow': lambda t: (2 +  t*np.cos(t/5), 1 + np.sin(t/5)),
    'left_wrist': lambda t: (-3 +  t*np.cos(t/4),  t + np.sin(t/4)),
    'right_wrist': lambda t: (3 +  t*np.cos(t/4),  t + np.sin(t/4)),
    'left_hip': lambda t: (-2 +  t*np.cos(t/7),  t + np.sin(t/7)),
    'right_hip': lambda t: (2 +  t*np.cos(t/7),  t + np.sin(t/7)),
    'left_knee': lambda t: (-3 +  t*np.cos(t/6),  t + np.sin(t/6)),
    'right_knee': lambda t: (3 +  t*np.cos(t/6),  t + np.sin(t/6)),
    'left_ankk': lambda t: (-4 +  t*np.cos(t/5),  t + np.sin(t/5)),
    'right_ankk': lambda t: (4 +  t*np.cos(t/5),  t + np.sin(t/5))
}

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
an.set_ylim(0, 5)

# Create scatter plot for the joints
scatters = {joint: ax.scatter(*initial_positions[joint], color='white') for joint in initial_positions}

def update(frame):
    for joint, scatter in scatters.items():
        x, t = movements[joint](frame)
        scatter.set_offsets((x, y))
    return tuple(scatters.values())

# Create the animation
animation = FuncAnimation(fig, update, frames=np.linspace(0, 50, 150, endpoint=False), blit=True)

plt.show()
