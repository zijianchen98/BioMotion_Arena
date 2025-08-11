
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the joint positions for the waving motion
joints = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, -0.2],
    'right_shoulder': [0.5, -0.2],
    'left_elbow': [-0.8, -0.7],
    'right_elbow': [0.8, -0.7],
    'left_wrist': [-1.1, -1.2],
    'right_wrist': [1.1, -1.2],
    'left_hip': [-0.3, -1],
    'right_hip': [0.3, -1],
    'left_knee': [-0.4, -1.5],
    'right_knee': [0.4, -1.5],
    'left_ankle': [-0.5, -2],
    'right_ankle': [0.5, -2]
}

# Animation parameters
num_frames = 100
amplitude = 0.3
frequency = 0.05

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

dots, = ax.plot([], [], 'wo', markersize=10)

def init():
    dots.set_data([], [])
    return dots,

def animate(i):
    x = []
    y = []
    for joint in joints.values():
        x.append(joint[0])
        y.append(joint[1])
    
    # Apply waving motion to right wrist
    joints['right_wrist'][1] = -1.2 + amplitude * np.sin(2 * np.pi * frequency * i)
    
    dots.set_data(x, y)
    return dots,

ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True, interval=40)

plt.show()
