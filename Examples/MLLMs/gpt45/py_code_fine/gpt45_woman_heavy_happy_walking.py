
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
frames = 60
interval = 50
dot_size = 50

# Define biological motion for sadman walking (15 point-lights)
def sad_walk_motion(t):
    angles = np.pi * t
    body = np.array([
        [0, 0.8],                                               # head
        [-0.1*np.sin(angles)-0.15, 0.6],                        # left shoulder
        [0, 0.6],                                               # center shoulder
        [0.1*np.sin(angles)+0.15, 0.6],                         # right shoulder
        [-0.18*np.sin(angles)-0.2, 0.4],                        # left elbow
        [0.18*np.sin(angles)+0.2, 0.4],                         # right elbow
        [-0.08*np.sin(angles)-0.2, 0.2],                        # left hand
        [0.08*np.sin(angles)+0.2, 0.2],                         # right hand
        [-0.1*np.sin(angles+np.pi)-0.08, 0.2],                  # left pelvis
        [0, 0.2],                                               # center pelvis
        [0.1*np.sin(angles+np.pi)+0.08, 0.2],                   # right pelvis
        [-0.1*np.sin(angles)+0.05, -0.1-0.1*np.abs(np.sin(angles))], # left knee
        [0.1*np.sin(angles)-0.05, -0.1-0.1*np.abs(np.sin(angles))],  # right knee
        [-0.1*np.sin(angles)+0.04, -0.4-0.1*np.abs(np.sin(angles))], # left foot
        [0.1*np.sin(angles)-0.04, -0.4-0.1*np.abs(np.sin(angles))],  # right foot
    ])
    return body

# Animation update function
def update(frame):
    plt.cla()
    plt.axis('off')
    plt.axis('equal')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    positions = sad_walk_motion(frame / float(frames))
    plt.scatter(positions[:,0], positions[:,1], s=dot_size, c='white')

# Define figure style
fig = plt.figure(figsize=(6,8),facecolor='black')
anim = animation.FuncAnimation(fig, update, frames=frames, interval=interval, repeat=True)

plt.show()
