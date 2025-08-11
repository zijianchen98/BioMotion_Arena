
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions for each joint in the "happyman" model
JOINTS = {
    'left_shoulder': [0, 1],
    'right_shoulder': [0, -1],
    'left_elbow': [-1, 1],
    'right_elbow': [1, -1],
    'left_wrist': [-2, 1],
    'right_wrist': [2, -1],
    'left_hip': [0, -2],
    'right_hip': [0, -4],
    'left_knee': [-1, -2],
    'right_knee': [1, -4],
    'left_ankle': [-2, -2],
    'right_ankle': [2, -4],
    'head': [0, 2],
    'neck': [0, 0]
}

# Define the connections between joints
CONNECTIONS = [
    ('left_shoulder', 'left_elbow'), ('left_elbow', 'left_wrist'),
    ('right_shoulder', 'right_elbow'), ('right_elbow', 'right_wrist'),
    ('left_hip', 'left_knee'), ('left_knee', 'left_ankle'),
    ('right_hip', 'right_knee'), ('right_knee', 'right_ankle'),
    ('left_shoulder', 'neck'), ('right_shoulder', 'neck'),
    ('neck', 'head'), ('left_hip', 'neck'), ('right_hip', 'neck')
]

# Walking cycle duration (in frames)
WALKING_CYCLE_DURATION = 20

def walking_animation(frame):
    # Clear the current frame
    ax.clear()
    
    # Update joint positions based on the walking cycle
    phase = frame / WALKING_CYCLE_DURATION
    
    JOINTS['left_hip'][0] = np.sin(2 * np.pi * phase)
    JOINTS['right_hip'][0] = np.sin(2 * np.pi * (phase + 0.5))
    JOINTS['left_knee'][0] = JOINTS['left_hip'][0] - 1
    JOINTS['right_knee'][0] = JOINTS['right_hip'][0] + 1
    JOINTS['left_ankle'][0] = JOINTS['left_knee'][0] - 1
    JOINTS['right_ankle'][0] = JOINTS['right_knee'][0] + 1
    
    # Draw points
    for joint in JOINTS:
        x, y = JOINTS[joint]
        ax.plot(x, y, 'wo', markersize=10)
        
    # Draw lines
    for connection in CONNECTIONS:
        start_joint, end_joint = connection
        start_x, start_y = JOINTS[start_joint]
        end_x, end_y = JOINTS[end_joint]
        ax.plot([start_x, end_x], [start_y, end_y], 'w-')

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 3)
ax.set_aspect('equal')
ax.axis('off')  # Hide the axes

# Create the animation
ani = FuncAnimation(fig, walking_animation, frames=WALKING_CYCLE_DURATION, repeat=True)

plt.show()
