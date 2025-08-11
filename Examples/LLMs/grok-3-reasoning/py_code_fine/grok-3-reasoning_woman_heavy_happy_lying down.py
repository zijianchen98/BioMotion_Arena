
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define key frame positions
positions_0 = np.array([
    [0, 1.7],  # head
    [-0.15, 1.5],  # left shoulder
    [0.15, 1.5],  # right shoulder
    [-0.17, 1.3],  # left elbow
    [0.17, 1.3],  # right elbow
    [-0.18, 1.1],  # left wrist
    [0.18, 1.1],  # right wrist
    [0, 1.4],  # chest
    [0, 1.2],  # abdomen
    [-0.1, 0.8],  # left hip
    [0.1, 0.8],  # right hip
    [-0.1, 0.4],  # left knee
    [0.1, 0.4],  # right knee
    [-0.1, 0.05],  # left ankle
    [0.1, 0.05]   # right ankle
])

positions_1 = np.array([
    [0, 1.0],  # head
    [-0.15, 0.9],  # left shoulder
    [0.15, 0.9],  # right shoulder
    [-0.2, 0.7],  # left elbow
    [0.2, 0.7],  # right elbow
    [-0.25, 0.5],  # left wrist
    [0.25, 0.5],  # right wrist
    [0, 0.8],  # chest
    [0, 0.6],  # abdomen
    [-0.1, 0.5],  # left hip
    [0.1, 0.5],  # right hip
    [-0.2, 0.3],  # left knee
    [0.2, 0.3],  # right knee
    [-0.25, 0.1],  # left ankle
    [0.25, 0.1]   # right ankle
])

positions_2 = np.array([
    [0, 0],  # head
    [0.1, 0.2],  # left shoulder
    [0.1, -0.2],  # right shoulder
    [0.3, 0.3],  # left elbow
    [0.3, -0.3],  # right elbow
    [0.5, 0.4],  # left wrist
    [0.5, -0.4],  # right wrist
    [0.2, 0],  # chest
    [0.4, 0],  # abdomen
    [0.6, 0.1],  # left hip
    [0.6, -0.1],  # right hip
    [0.9, 0.1],  # left knee
    [0.9, -0.1],  # right knee
    [1.2, 0.1],  # left ankle
    [1.2, -0.1]   # right ankle
])

# Set up figure and axes
fig = plt.figure(facecolor='black')
ax = plt.axes(xlim=(-0.5, 1.5), ylim=(-0.5, 2.0), facecolor='black')
ax.set_xticks([])
ax.set_yticks([])
points = ax.scatter([], [], color='white', s=50)

def init():
    points.set_offsets([])
    return points,

def animate(i):
    if i < 50:
        t = i / 50
        current_positions = (1 - t) * positions_0 + t * positions_1
    else:
        t = (i - 50) / 50
        current_positions = (1 - t) * positions_1 + t * positions_2
    points.set_offsets(current_positions)
    return points,

N = 100
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=N, interval=50, blit=True)
plt.show()
