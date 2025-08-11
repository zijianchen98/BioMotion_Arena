
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the fixed positions
positions = np.array([
    [0, 90],   # 0: head
    [-10, 80], # 1: left shoulder
    [10, 80],  # 2: right shoulder
    [-15, 70], # 3: left elbow
    [15, 70],  # 4: right elbow
    [-20, 60], # 5: left wrist
    [20, 60],  # 6: right wrist initial
    [-22, 58], # 7: left hand
    [22, 58],  # 8: right hand initial
    [-5, 50],  # 9: left hip
    [5, 50],   # 10: right hip
    [-5, 30],  # 11: left knee
    [5, 30],   # 12: right knee
    [-5, 10],  # 13: left ankle
    [5, 10]    # 14: right ankle
])

# Compute R and theta0 for right wrist
xe, ye = positions[4]  # right elbow
xw0, yw0 = positions[6]  # initial right wrist
dxw = xw0 - xe
dyw = yw0 - ye
R = np.sqrt(dxw**2 + dyw**2)
theta0 = np.arctan2(dyw, dxw)

# Compute initial offset for right hand
xh0, yh0 = positions[8]  # initial right hand
dx0 = xh0 - xw0
dy0 = yh0 - yw0

# Define parameters for motion
B = 0.5  # amplitude in radians
frequency = 2  # Hz
omega = 2 * np.pi * frequency

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-30, 30)
ax.set_ylim(0, 100)
ax.axis('off')

# Create scatter plot
points = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

def update(frame):
    t = frame / 50.0  # assuming 50 fps
    theta = theta0 + B * np.sin(omega * t)
    xw = xe + R * np.cos(theta)
    yw = ye + R * np.sin(theta)
    alpha = theta - theta0
    dx = dx0 * np.cos(alpha) - dy0 * np.sin(alpha)
    dy = dx0 * np.sin(alpha) + dy0 * np.cos(alpha)
    xh = xw + dx
    yh = yw + dy
    positions[6] = [xw, yw]
    positions[8] = [xh, yh]
    points.set_offsets(positions)
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), interval=20, blit=True)

plt.show()
