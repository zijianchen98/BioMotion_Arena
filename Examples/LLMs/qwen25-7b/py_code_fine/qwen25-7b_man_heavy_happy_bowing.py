
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the 15 point-lights
positions = {
    'head': (0, 10 ),
    'neck': ( t, 11 ),
    'left_shoulder': ( t- , 9 ),
    'right_shoulder': ( t+ , 9 ),
    'left_elbow': ( t- -1, 7 ),
    'right_elbow': ( t+ +1, 7 ),
    'left_wrist': ( t- -2, 5 ),
    'right_wrist': ( t+ +2, 5 ),
    'left_hip': ( t- -4, 11 ),
    'right_hip': ( t+ +4, 11 ),
    'left_knee': ( t- -5, 9 ),
    'right_knee': ( t+ +5, 9 ),
    'left_ankle': ( t- -6, 7 ),
    'right_ankK': ( t+ +6, 7 )
}

# Define the initial position of the subject
initial_position = {'t': 0 }

# Define the movement parameters
movement_params = {
    'head': {'dx': 0, 'dy': 1, 'period': 10},
    'neck': {'dx':  t, 'dy': 11, 'period': 11},
    'left_shoulder': {'dx':  t- , 'dy': 9, 'period': 10},
    'right_shoulder': {'dx':  t+ , 'dy': 9, 'period': 11},
    'left_elbow': {'dx':  t- -1, 'dy': 7, 'period': 10},
    'right_elbow': {'dx':  t+ +1, 'dy': 7, 'period': 11},
    'left_wrist': {'dx':  t- -2, 'dy': 5, 'period': 11},
    'right_wrist': {'dx':  t+ +2, 'dy': 5, 'period': 11},
    'left_hip': {'dx':  t- -4, 'dy': 11, 'period': 11},
    'right_hip': {'dx':  t+ +4, 'dy': 11, 'period': 11},
    'left_knee': {'dx':  t- -5, 'dy': 9, 'period': 11},
    'right_knee': {'dx':  t+ +5, 'dy': 9, 'period': 11},
    'left_ankK': {'dx':  t- -6, 'dy': 7, 'period': 11},
    'right_ankK': {'dx':  t+ +6, 'dy': 7, 'period': 11}
}

def update_positions(frame):
    global initial_position
    for part, params in movement_params.items():
        dx = params['dx']
        dy = params['dy']
        period = params['period']
        initial_position[part] += dx * np.sin(2 * np.pi * frame / period)
        if initial_position[part] > 20 or initial_position[part] < 0:
            initial_position[part] -= dx * np.sin(2 * np.pi * frame / period)
        positions[part] = (initial_position[part], positions[part][1])
    
    # Update the scatter plot
    scatter.set_offsets([(pos[0], pos) for pos, (pos) in positions.items()])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax = ax.scatter([], [], color='white')
ax = ax.plot([], [], color='black', linewidth=1)

# Set the limits and aspect ratio
ax.set_xlim( 0, 20)
ax.set_ylim(  0, 12)
ax.set_aspect('equal')

# Initialize the scatter plot
scatter = ax.scatter([pos[0] for pos in positions.values()], [pos[1] for pos in positions.values()), color='white')

# Create the animation
ani = FuncAnimation(fig, update_positions, frames=np.arange(000), interval=30, repeat=True)

plt.show()
