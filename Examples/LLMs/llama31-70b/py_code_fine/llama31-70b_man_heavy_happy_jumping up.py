
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights representing the happyman's joints
joints = [
    # Head
    {'x': 0, 'y': 10, 'z': 0},
    # Torso
    {'x': 0, 'y': 5, 'z': 0},
    {'x': 0, 'y': 0, 'z': 0},
    # Left arm
    {'x': -5, 'y': 7, 'z': 0},
    {'x': -10, 'y': 5, 'z': 0},
    {'x': -10, 'y': 3, 'z': 0},
    # Right arm
    {'x': 5, 'y': 7, 'z': 0},
    {'x': 10, 'y': 5, 'z': 0},
    {'x': 10, 'y': 3, 'z': 0},
    # Left leg
    {'x': -3, 'y': -5, 'z': 0},
    {'x': -5, 'y': -10, 'z': 0},
    {'x': -5, 'y': -12, 'z': 0},
    # Right leg
    {'x': 3, 'y': -5, 'z': 0},
    {'x': 5, 'y': -10, 'z': 0},
    {'x': 5, 'y': -12, 'z': 0},
]

# Define the movement of each joint
def move_joints(frame):
    joints_moved = joints.copy()
    # Simulate the jumping motion
    for i, joint in enumerate(joints_moved):
        if i < 3:  # Head and torso
            joint['y'] = joint['y'] + np.sin(frame / 10.0) * 2
        elif i < 6:  # Left arm
            joint['x'] = joint['x'] + np.sin(frame / 15.0) * 2
            joint['y'] = joint['y'] + np.sin(frame / 10.0) * 2
        elif i < 9:  # Right arm
            joint['x'] = joint['x'] - np.sin(frame / 15.0) * 2
            joint['y'] = joint['y'] + np.sin(frame / 10.0) * 2
        elif i < 12:  # Left leg
            joint['x'] = joint['x'] + np.sin(frame / 20.0) * 2
            joint['y'] = joint['y'] + np.sin(frame / 15.0) * 4
        else:  # Right leg
            joint['x'] = joint['x'] - np.sin(frame / 20.0) * 2
            joint['y'] = joint['y'] + np.sin(frame / 15.0) * 4
    return joints_moved

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point-light stimulus
def animate(frame):
    ax.clear()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    joints_moved = move_joints(frame)
    xs = [joint['x'] for joint in joints_moved]
    ys = [joint['y'] for joint in joints_moved]
    ax.scatter(xs, ys, color='white', s=10)

ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
