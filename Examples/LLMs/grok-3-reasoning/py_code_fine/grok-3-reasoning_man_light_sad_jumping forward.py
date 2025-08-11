
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define key times for pose changes
key_times = [0, 0.4, 0.6, 1.4, 1.6, 2.0]

# Define constant offsets for some points
constant_offsets = {
    'head': (0, 40),
    'neck': (0, 30),
    'torso_center': (0, 0),
    'left_shoulder': (-10, 20),
    'right_shoulder': (10, 20),
    'left_hip': (-5, -20),
    'right_hip': (5, -20),
}

# Define variable offsets for limbs at key times
left_elbow_offsets = [(-20, 10), (-15, 15), (-15, 30), (-15, 30), (-15, 15), (-20, 10)]
left_wrist_offsets = [(-25, 0), (-10, 10), (-20, 40), (-20, 40), (-10, 10), (-25, 0)]
left_knee_offsets = [(-5, -50), (-10, -30), (-5, -60), (-5, -60), (-10, -30), (-5, -50)]
left_ankle_offsets = [(-5, -80), (-5, -40), (-5, -90), (-5, -90), (-5, -40), (-5, -80)]

# Mirror for right side
right_elbow_offsets = [( -x, y) for (x, y) in left_elbow_offsets]
right_wrist_offsets = [( -x, y) for (x, y) in left_wrist_offsets]
right_knee_offsets = [( -x, y) for (x, y) in left_knee_offsets]
right_ankle_offsets = [( -x, y) for (x, y) in left_ankle_offsets]

# Combine all offsets
point_offsets = {
    **constant_offsets,
    'left_elbow': left_elbow_offsets,
    'right_elbow': right_elbow_offsets,
    'left_wrist': left_wrist_offsets,
    'right_wrist': right_wrist_offsets,
    'left_knee': left_knee_offsets,
    'right_knee': right_knee_offsets,
    'left_ankle': left_ankle_offsets,
    'right_ankle': right_ankle_offsets,
}

# Define COM position over time
def com_position(t):
    if t <= 0.4:
        x = 25 * t
        y = 140 - 25 * t
    elif t <= 1.6:
        tau = t - 0.4
        x = 25 * t
        y = 130 + 100 * tau - 83.335 * tau**2
    else:
        x = 25 * t
        y = 130 + 25 * (t - 1.6)
    return x, y

# Function to get offset at time t
def get_offset(t, key_times, offsets):
    for i in range(len(key_times) - 1):
        if key_times[i] <= t <= key_times[i+1]:
            t1, t2 = key_times[i], key_times[i+1]
            off1, off2 = offsets[i], offsets[i+1]
            ratio = (t - t1) / (t2 - t1)
            x = off1[0] + ratio * (off2[0] - off1[0])
            y = off1[1] + ratio * (off2[1] - off1[1])
            return x, y
    if t < key_times[0]:
        return offsets[0]
    else:
        return offsets[-1]

# Set up figure and axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_xlim(-10, 60)
ax.set_ylim(0, 200)
ax.set_facecolor('black')
ax.axis('off')

# Create scatter artists for points
points = ['head', 'neck', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow', 
          'left_wrist', 'right_wrist', 'torso_center', 'left_hip', 'right_hip', 
          'left_knee', 'right_knee', 'left_ankle', 'right_ankle']
points_artists = [ax.scatter([], [], color='white', s=10) for _ in points]

# Update function for animation
def update(t):
    com_x, com_y = com_position(t)
    for i, point in enumerate(points):
        if isinstance(point_offsets[point], tuple):
            offset_x, offset_y = point_offsets[point]
        else:
            offset_x, offset_y = get_offset(t, key_times, point_offsets[point])
        x = com_x + offset_x
        y = com_y + offset_y
        points_artists[i].set_offsets([[x, y]])
    return points_artists

# Create animation
anim = FuncAnimation(fig, update, frames=np.arange(0, 2.01, 0.02), interval=20, blit=True)

plt.show()
