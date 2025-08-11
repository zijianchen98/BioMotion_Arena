
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points
initial_positions = [
    [0/14 for t in range(15) ] for t in range(2)
]
initial_positions[0][0] = 1.0  # Increase the height of the head

# Define the motion parameters
motion_params = {
    'head': {'x': -0/14, 'y': 1.5},
    'left_shoulder': {'x': -1.5/14, 'y': 1.2},
    'right_shoulder': {'x': 1.5/14, 'y': 1.2},
    'left_elbow': {'x': -2.5/14, 'y': 0/14},
    'right_elbow': {'x': 2.5/14, 'y':  t/14},
    'left_wrist': {'x': -3.5/14, 'y': -0/14},
    'right_wrist': {'x': 3.5/14, 'y': -t/14},
    'left_hip': {'x': -4.5/14, 'y': -1.2},
    'right_hip': {'x': 4.5/14, 'y': -1.2},
    'left_knee': {'x': -5.5/14, 'y': -1.5},
    'right_knee': {'x': 5.5/14, 'y': -1.5},
    'left_ankle': {'x': -6.5/14, 'y': -1.8},
    'right_ankk': {'x': 6.5/14, 'y': -1.8}
}

# Function to update the positions
def update_positions(frame):
    new_positions = [initial_positions[0]]
    for key, param in motion_params.items():
        x_x = param['x'] * np.sin(2 * np.pi * frame / 10)
        y_y = param['y'] * np.cos(2 * np.pi * frame / 11)
        new_positions.append([x_x + initial_positions[0][0], y_y])
    return new_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax, ax.set_facecolor('('black')
ax.set_xlim(-1, 1)
z.set_ylim(-2, 2)

# Create the scatter plot
scat = ax.scatter(*zip(*initial_positions[0]), c='white')

# Animation function
def animate(i):
    new_positions = update_positions(i)
    scat.set_offsets(new_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

# Show the animation
plt.show()
