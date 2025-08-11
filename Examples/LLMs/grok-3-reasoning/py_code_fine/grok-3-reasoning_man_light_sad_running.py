
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def head(t):
    return 0, 1.7 + 0.02 * np.sin(2*t)

def left_shoulder(t):
    return -0.2, 1.5 + 0.01 * np.sin(2*t)

def right_shoulder(t):
    return 0.2, 1.5 + 0.01 * np.sin(2*t)

def left_elbow(t):
    return -0.3 + 0.1 * np.sin(t + np.pi), 1.3 + 0.05 * np.sin(t + np.pi)

def right_elbow(t):
    return 0.3 + 0.1 * np.sin(t), 1.3 + 0.05 * np.sin(t)

def left_wrist(t):
    return -0.4 + 0.2 * np.sin(t + np.pi), 1.1 + 0.1 * np.sin(t + np.pi)

def right_wrist(t):
    return 0.4 + 0.2 * np.sin(t), 1.1 + 0.1 * np.sin(t)

def left_hip(t):
    return -0.1, 1.0

def right_hip(t):
    return 0.1, 1.0

def left_knee(t):
    return -0.1 + 0.05 * np.sin(t), 0.7 + 0.1 * np.sin(t - np.pi/2)

def right_knee(t):
    return 0.1 + 0.05 * np.sin(t + np.pi), 0.7 + 0.1 * np.sin(t + np.pi - np.pi/2)

def left_ankle(t):
    return -0.1 + 0.1 * np.sin(t), 0.3 + 0.1 * (1 + np.sin(t - np.pi))

def right_ankle(t):
    return 0.1 + 0.1 * np.sin(t + np.pi), 0.3 + 0.1 * (1 + np.sin(t))

def left_toe(t):
    return -0.1 + 0.15 * np.sin(t), 0.1 + 0.05 * (1 + np.sin(t - np.pi))

def right_toe(t):
    return 0.1 + 0.15 * np.sin(t + np.pi), 0.1 + 0.05 * (1 + np.sin(t))

points = [
    head, left_shoulder, right_shoulder, left_elbow, right_elbow,
    left_wrist, right_wrist, left_hip, right_hip, left_knee,
    right_knee, left_ankle, right_ankle, left_toe, right_toe
]

def get_positions(t):
    positions = [point(t) for point in points]
    x = [pos[0] for pos in positions]
    y = [pos[1] for pos in positions]
    return x, y

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.axis('off')

x0, y0 = get_positions(0)
scat = ax.scatter(x0, y0, color='white', s=50)

def update(frame):
    t = (frame % 60) / 60 * 2 * np.pi
    x, y = get_positions(t)
    scat.set_offsets(np.c_[x, y])
    return scat,

ani = FuncAnimation(fig, update, frames=120, interval=33, blit=True)
plt.show()
