
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Define constants
T = 2.0  # total time in seconds
fps = 60
dt = 1.0 / fps
N = int(T / dt)
t1 = 0.2 * T
t2 = 0.3 * T
t3 = 0.7 * T
t4 = 0.8 * T
y0 = 1.3
y_crouch = 1.1
h = 0.3  # jump height
tau = (t3 - t2) / 2  # time to apex
g = (2 * h) / (tau**2)
v0 = g * tau

# Define standing and crouched positions
points_standing = np.array([
    [0, 1.8],  # head
    [0, 1.6],  # neck
    [-0.2, 1.5],  # left shoulder
    [0.2, 1.5],  # right shoulder
    [-0.4, 1.3],  # left elbow
    [0.4, 1.3],  # right elbow
    [-0.5, 1.1],  # left wrist
    [0.5, 1.1],  # right wrist
    [0, 1.3],  # torso center
    [-0.1, 1.0],  # left hip
    [0.1, 1.0],  # right hip
    [-0.1, 0.6],  # left knee
    [0.1, 0.6],  # right knee
    [-0.1, 0.2],  # left ankle
    [0.1, 0.2]  # right ankle
])

points_crouched = np.array([
    [0, 1.6],
    [0, 1.4],
    [-0.2, 1.3],
    [0.2, 1.3],
    [-0.4, 1.1],
    [0.4, 1.1],
    [-0.5, 0.9],
    [0.5, 0.9],
    [0, 1.1],
    [-0.1, 0.8],
    [0.1, 0.8],
    [-0.1, 0.5],
    [0.1, 0.5],
    [-0.1, 0.2],
    [0.1, 0.2]
])

def yравия y_cm(t):
    if t < t1:
        return y0 - (y0 - y_crouch) * (t / t1)
    elif t < t2:
        return y_crouch + (y0 - y_crouch) * ((t - t1) / (t2 - t1))
    elif t < t3:
        dt = t - t2
        return y0 + v0 * dt - 0.5 * g * dt**2
    elif t < t4:
        return y0 - (y0 - y_crouch) * ((t - t3) / (t4 - t3))
    else:
        return y_crouch + (y0 - y_crouch) * ((t - t4) / (T - t4))

def get_points(t):
    if t < t1:
        u = t / t1
        points = (1 - u) * points_standing + u * points_crouched
    elif t < t2:
        u = (t - t1) / (t2 - t1)
        points = (1 - u) * points_crouched + u * points_standing
    elif t < t3:
        points = points_standing.copy()
        dy = y_cm(t) - y0
        points[:, 1] += dy
    elif t < t4:
        u = (t - t3) / (t4 - t3)
        points = (1 - u) * points_standing + u * points_crouched
    else:
        u = (t - t4) / (T - t4)
        points = (1 - u) * points_crouched + u * points_standing
    return points

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2.5)
scatter = ax.scatter([], [], color='white', s=10)

def update(frame):
    t = frame * dt
    points = get_points(t)
    scatter.set_offsets(points)
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=N, interval=1000*dt, blit=True)
plt.show()
