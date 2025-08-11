
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the fixed positions
points = np.array([
    [0,10],  # head
    [0,9],   # neck
    [0,7],   # torso center
    [-1,9],  # left shoulder
    [1,9],   # right shoulder
    [-1,7],  # left elbow
    [1,7],   # right elbow
    [-1,5],  # left wrist
    [1,5],   # right wrist (initial)
    [-0.5,5],# left hip
    [0.5,5], # right hip
    [-0.5,3],# left knee
    [0.5,3], # right knee
    [-0.5,1],# left ankle
    [0.5,1]  # right ankle
], dtype=float)

fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_xlim(-3,3)
ax.set_ylim(0,12)
ax.axis('off')
points_plot = ax.scatter(points[:,0], points[:,1], color='white', s=20)

def update(frame):
    t = frame * 0.02  # seconds
    theta = (np.pi / 4) * np.sin(2 * np.pi * 0.5 * t)
    points[8,0] = 1 + 2 * np.sin(theta)
    points[8,1] = 7 - 2 * np.cos(theta)
    points_plot.set_offsets(points)
    return points_plot,

ani = FuncAnimation(fig, update, interval=20, blit=True)
plt.show()
