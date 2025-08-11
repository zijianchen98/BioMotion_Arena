
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the skeleton joints in 2D (x, y)
# 15 points: head, neck, left shoulder, right shoulder, left elbow, right elbow,
# left wrist, right wrist, mid-torso, left hip, right hip, left knee, right knee, left ankle, right ankle
rest_joints = np.array([
    [ 0.0,  4.0],  # head
    [ 0.0,  3.5],  # neck
    [-0.5,  3.0],  # left shoulder
    [ 0.5,  3.0],  # right shoulder
    [-0.8,  2.5],  # left elbow
    [ 0.8,  2.5],  # right elbow
    [-1.0,  2.0],  # left wrist
    [ 1.0,  2.0],  # right wrist
    [ 0.0,  2.5],  # mid-torso
    [-0.3,  2.0],  # left hip
    [ 0.3,  2.0],  # right hip
    [-0.3,  1.0],  # left knee
    [ 0.3,  1.0],  # right knee
    [-0.3,  0.0],  # left ankle
    [ 0.3,  0.0],  # right ankle
])

# Pre-compute bow posture by rotating all joints around hip center
hip_center = (rest_joints[9] + rest_joints[10]) / 2
angle_bow = np.deg2rad(-30)  # 30 degrees forward (clockwise)
cos_a, sin_a = np.cos(angle_bow), np.sin(angle_bow)
R = np.array([[cos_a, -sin_a], [sin_a, cos_a]])

# Apply rotation for bow posture
bow_joints = (rest_joints - hip_center) @ R.T + hip_center

# Animation setup
fig, ax = plt.subplots(figsize=(5, 8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 4.5)
ax.set_aspect('equal')
ax.axis('off')

# Scatter for the 15 point-lights
points, = ax.plot([], [], 'o', color='white', markersize=8)

# Number of frames and animation function
frames = 120
def update(frame):
    # Normalize frame to t in [0, 1]
    t = frame / (frames - 1)
    # Use a sinusoidal ease to bow forward then return
    # sin(pi * t) goes 0->1->0 as t goes 0->1
    weight = np.sin(np.pi * t)
    current = rest_joints * (1 - weight) + bow_joints * weight
    points.set_data(current[:, 0], current[:, 1])
    return points,

ani = FuncAnimation(fig, update, frames=frames, interval=30, blit=True)

plt.show()
