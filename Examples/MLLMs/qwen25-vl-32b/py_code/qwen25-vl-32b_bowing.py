
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights
initial_positions = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, 0.5],
    'right_shoulder': [0.5, 0.5],
    'left_elbow': [-1, 0.25],
    'right_elbow': [1, 0.25],
    'left_hand': [-1.5, -0.25],
    'right_hand': [1.5, -0.25],
    'left_hip': [-0.5, -0.5],
    'right_hip': [0.5, -0.5],
    'left_knee': [-1, -1],
    'right_knee': [1, -1],
    'left_foot': [-1.5, -1.5],
    'right_foot': [1.5, -1.5]
}

# Convert to numpy array for easier manipulation
positions = np.array(list(initial_positions.values()))

# Define the range of motion for each joint
joint_ranges = {
    'head': (-0.2, 0.2),
    'torso': (-0.2, 0.2),
    'left_shoulder': (-0.5, 0.5),
    'right_shoulder': (-0.5, 0.5),
    'left_elbow': (-0.5, 0.5),
    'right_elbow': (-0.5, 0.5),
    'left_hand': (-0.5, 0.5),
    'right_hand': (-0.5, 0.5),
    'left_hip': (-0.5, 0.5),
    'right_hip': (-0.5, 0.5),
    'left_knee': (-0.5, 0.5),
    'right_knee': (-0.5, 0.5),
    'left_foot': (-0.5, 0.5),
    'right_foot': (-0.5, 0.5)
}

# Define the animation parameters
num_frames = 100
frame_rate = 30  # frames per second

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Initialize the scatter plot
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

def update(frame):
    # Update the positions based on the frame number
    for i, joint in enumerate(initial_positions.keys()):
        if joint == 'head':
            positions[i] += [0, np.sin(frame / 10) * 0.1]
        elif joint == 'torso':
            positions[i] += [0, np.sin(frame / 10) * 0.1]
        elif joint == 'left_shoulder':
            positions[i] += [np.sin(frame / 10) * 0.1, np.cos(frame / 10) * 0.1]
        elif joint == 'right_shoulder':
            positions[i] += [-np.sin(frame / 10) * 0.1, np.cos(frame / 10) * 0.1]
        elif joint == 'left_elbow':
            positions[i] += [np.sin(frame / 10) * 0.1, np.cos(frame / 10) * 0.1]
        elif joint == 'right_elbow':
            positions[i] += [-np.sin(frame / 10) * 0.1, np.cos(frame / 10) * 0.1]
        elif joint == 'left_hand':
            positions[i] += [np.sin(frame / 10) * 0.1, np.cos(frame / 10) * 0.1]
        elif joint == 'right_hand':
            positions[i] += [-np.sin(frame / 10) * 0.1, np.cos(frame / 10) * 0.1]
        elif joint == 'left_hip':
            positions[i] += [np.sin(frame / 10) * 0.1, np.cos(frame / 10) * 0.1]
        elif joint == 'right_hip':
            positions[i] += [-np.sin(frame / 10) * 0.1, np.cos(frame / 10) * 0.1]
        elif joint == 'left_knee':
            positions[i] += [np.sin(frame / 10) * 0.1, np.cos(frame / 10) * 0.1]
        elif joint == 'right_knee':
            positions[i] += [-np.sin(frame / 10) * 0.1, np.cos(frame / 10) * 0.1]
        elif joint == 'left_foot':
            positions[i] += [np.sin(frame / 10) * 0.1, np.cos(frame / 10) * 0.1]
        elif joint == 'right_foot':
            positions[i] += [-np.sin(frame / 10) * 0.1, np.cos(frame / 10) * 0.1]

    # Update the scatter plot
    scatter.set_offsets(positions)

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=1000/frame_rate)

# Display the animation
plt.show()
