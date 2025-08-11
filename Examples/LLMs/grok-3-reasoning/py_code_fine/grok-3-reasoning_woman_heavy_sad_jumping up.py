
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Bone lengths
l_pelvis_chest = 0.3
l_chest_neck = 0.1
l_neck_head = 0.15
d_shoulder = 0.15
l_upperarm = 0.3
l_forearm = 0.25
d_hip = 0.1
l_thigh = 0.4
l_shin = 0.4
l_ankle_toe = 0.15

# Skeletal hierarchy: joint -> (parent, offset)
joints = {
    'pelvis': (None, (0, 0)),
    'chest': ('pelvis', (0, l_pelvis_chest)),
    'neck': ('chest', (0, l_chest_neck)),
    'head': ('neck', (0, l_neck_head)),
    'left_shoulder': ('chest', (d_shoulder, 0)),
    'left_elbow': ('left_shoulder', (0, -l_upperarm)),
    'left_wrist': ('left_elbow', (0, -l_forearm)),
    'right_shoulder': ('chest', (-d_shoulder, 0)),
    'right_elbow': ('right_shoulder', (0, -l_upperarm)),
    'right_wrist': ('right_elbow', (0, -l_forearm)),
    'left_hip': ('pelvis', (d_hip, 0)),
    'left_knee': ('left_hip', (0, -l_thigh)),
    'left_ankle': ('left_knee', (0, -l_shin)),
    'left_toe': ('left_ankle', (l_ankle_toe, 0)),
    'right_hip': ('pelvis', (-d_hip, 0)),
    'right_knee': ('right_hip', (0, -l_thigh)),
    'right_ankle': ('right_knee', (0, -l_shin)),
    'right_toe': ('right_ankle', (-l_ankle_toe, 0)),
}

# Key times
key_times = [0, 1, 2, 3, 4]

# Pelvis y positions at key times
pelvis_y = [0.8, 0.5, 1.2, 0.5, 0.8]

# Angles at key times for each joint
angles = {
    'chest': [0, 10, 0, 10, 0],
    'left_shoulder': [0, -30, 30, -30, 0],
    'left_elbow': [0, 60, 0, 60, 0],
    'right_shoulder': [0, -30, 30, -30, 0],
    'right_elbow': [0, 60, 0, 60, 0],
    'left_hip': [0, 30, 0, 30, 0],
    'left_knee': [0, -60, 0, -60, 0],
    'right_hip': [0, 30, 0, 30, 0],
    'right_knee': [0, -60, 0, -60, 0],
    'left_ankle': [0, 0, 0, 0, 0],
    'right_ankle': [0, 0, 0, 0, 0],
}

# Points to plot
points = ['head', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
          'left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle', 'left_toe', 'right_toe']

def get_pelvis_y(t):
    for i in range(len(key_times) - 1):
        if key_times[i] <= t <= key_times[i + 1]:
            y1 = pelvis_y[i]
            y2 = pelvis_y[i + 1]
            return y1 + (y2 - y1) * (t - key_times[i]) / (key_times[i + 1] - key_times[i])
    return pelvis_y[-1]  # if t > last key time

def get_angle(joint, t):
    if joint in angles:
        for i in range(len(key_times) - 1):
            if key_times[i] <= t <= key_times[i + 1]:
                a1 = angles[joint][i]
                a2 = angles[joint][i + 1]
                return a1 + (a2 - a1) * (t - key_times[i]) / (key_times[i + 1] - key_times[i])
        return angles[joint][-1]  # if t > last key time
    else:
        return 0

def get_position(joint, t):
    if joint == 'pelvis':
        return (0, get_pelvis_y(t))
    else:
        parent, offset = joints[joint]
        parent_pos = get_position(parent, t)
        parent_angle = get_angle(parent, t)
        dx, dy = offset
        theta = math.radians(parent_angle)
        rotated_dx = dx * math.cos(theta) - dy * math.sin(theta)
        rotated_dy = dx * math.sin(theta) + dy * math.cos(theta)
        return (parent_pos[0] + rotated_dx, parent_pos[1] + rotated_dy)

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

# Create scatter plot
scatter = ax.scatter([], [], s=10, color='white')

def init():
    scatter.set_offsets([])
    return scatter,

def animate(t):
    positions = [get_position(point, t) for point in points]
    scatter.set_offsets(positions)
    return scatter,

# Create animation
anim = FuncAnimation(fig, animate, frames=np.arange(0, 4, 0.04), init_func=init, blit=True)

plt.show()
