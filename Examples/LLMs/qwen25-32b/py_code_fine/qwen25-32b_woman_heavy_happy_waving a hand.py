
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the joint positions for a waving hand motion
joint_positions = {
    'head': [0, 2],
    'torso': [0, 1],
    'hip': [0, 0],
    'shoulder_left': [-0.5, 1.5],
    'elbow_left': [-1, 1],
    'wrist_left': [-1.5, 0.8],
    'shoulder_right': [0.5, 1.5],
    'elbow_right': [1, 1],
    'wrist_right': [1.5, 0.8]
}

# Create a list of joint names in order
joints_order = ['head', 'torso', 'hip', 'shoulder_left', 'elbow_left', 'wrist_left', 'shoulder_right', 'elbow_right', 'wrist_right']

# Define the number of frames for the animation
num_frames = 100

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.axis('off')  # Hide the axes

# Create scatter plot for the point-lights
scatter = ax.scatter([], [], s=50, c='white')

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    # Update the position of the wrist for waving motion
    angle = np.radians(45 * np.sin(2 * np.pi * frame / num_frames))
    wrist_left_x = joint_positions['elbow_left'][0] + 0.7 * np.cos(angle)
    wrist_left_y = joint_positions['elbow_left'][1] - 0.7 * np.sin(angle)
    
    joint_positions['wrist_left'] = [wrist_left_x, wrist_left_y]
    
    # Collect the updated positions
    points = []
    for joint in joints_order:
        points.append(joint_positions[joint])
    
    # Update the scatter plot
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, repeat=True)

plt.show()
