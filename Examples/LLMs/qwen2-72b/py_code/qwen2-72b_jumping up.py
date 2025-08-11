
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the skeleton structure of the human body
skeleton = {
    'pelvis': ['left_hip', 'right_hip'],
    'left_hip': ['left_knee'],
    'right_hip': ['right_knee'],
    'left_knee': ['left_ankle'],
    'right_knee': ['right_ankle'],
    'left_ankle': [],
    'right_ankle': [],
    'spine': ['left_shoulder', 'right_shoulder'],
    'left_shoulder': ['left_elbow'],
    'right_shoulder': ['right_elbow'],
    'left_elbow': ['left_wrist'],
    'right_elbow': ['right_wrist'],
    'left_wrist': [],
    'right_wrist': [],
    'neck': ['head'],
    'head': []
}

# Define initial positions for each joint
initial_positions = {
    'pelvis': [0, 0],
    'left_hip': [-1, -1],
    'right_hip': [1, -1],
    'left_knee': [-2, -2],
    'right_knee': [2, -2],
    'left_ankle': [-3, -3],
    'right_ankle': [3, -3],
    'spine': [0, 1],
    'left_shoulder': [-1, 2],
    'right_shoulder': [1, 2],
    'left_elbow': [-2, 3],
    'right_elbow': [2, 3],
    'left_wrist': [-3, 4],
    'right_wrist': [3, 4],
    'neck': [0, 5],
    'head': [0, 6]
}

# Define the jumping motion
def jump_motion(t):
    amplitude = 0.5
    frequency = 0.5
    phase = 0
    return amplitude * np.sin(2 * np.pi * frequency * t + phase)

# Function to update the positions based on the motion
def update_positions(t):
    positions = {joint: list(pos) for joint, pos in initial_positions.items()}
    positions['pelvis'][1] += jump_motion(t)
    # Update other joints based on pelvis position
    for joint in skeleton:
        if joint != 'pelvis':
            parent = skeleton[joint][0]
            positions[joint][1] += jump_motion(t) - jump_motion(0)
    return positions

# Animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_facecolor('black')
    positions = update_positions(i / 10.0)
    for joint in skeleton:
        x, y = positions[joint]
        ax.plot(x, y, 'o', color='white')

# Set up the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()
