
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the 15 joints in a standard order:
# 0: head top (nose)
# 1: neck
# 2: right shoulder
# 3: right elbow
# 4: right wrist
# 5: left shoulder
# 6: left elbow
# 7: left wrist
# 8: right hip
# 9: right knee
# 10: right ankle
# 11: left hip
# 12: left knee
# 13: left ankle
# 14: mid hip (pelvis)

# Neutral upright pose (x, y) coordinates
neutral = np.array([
    [ 0.00, 1.80],   # head top
    [ 0.00, 1.60],   # neck
    [ 0.20, 1.50],   # right shoulder
    [ 0.30, 1.30],   # right elbow
    [ 0.30, 1.10],   # right wrist
    [-0.20, 1.50],   # left shoulder
    [-0.30, 1.30],   # left elbow
    [-0.30, 1.10],   # left wrist
    [ 0.15, 1.00],   # right hip
    [ 0.15, 0.60],   # right knee
    [ 0.15, 0.20],   # right ankle
    [-0.15, 1.00],   # left hip
    [-0.15, 0.60],   # left knee
    [-0.15, 0.20],   # left ankle
    [ 0.00, 1.00],   # mid hip (pelvis)
])

# Create the bowed pose by rotating upper body around the mid-hip and slightly bending knees
def make_bow_pose(neutral):
    bow = neutral.copy()
    # Rotation around mid-hip (index 14) by -40 degrees
    mid_hip = neutral[14]
    theta = np.deg2rad(-40)
    R = np.array([[ np.cos(theta), -np.sin(theta)],
                  [ np.sin(theta),  np.cos(theta)]])
    # Indices to rotate: head, neck, shoulders, elbows, wrists
    upper_idx = [0,1,2,3,4,5,6,7]
    for i in upper_idx:
        vec = neutral[i] - mid_hip
        bow[i] = mid_hip + R.dot(vec)
    # Slight knee bend: raise knees a little
    bow[9,1] += 0.10   # right knee
    bow[12,1] += 0.10  # left knee
    # Pelvis and hips stay the same, ankles unchanged
    return bow

bow_pose = make_bow_pose(neutral)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(5,8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(0.0, 2.0)
ax.set_aspect('equal')
ax.axis('off')

pts, = ax.plot([], [], 'o', color='white', markersize=8)

# Number of frames
frames = 100

def update(frame):
    # Smooth back-and-forth interpolation parameter t from 0->1->0
    t = 0.5 * (1 - np.cos(2 * np.pi * frame / frames))
    # Interpolate between neutral and bow poses
    pos = neutral + t * (bow_pose - neutral)
    pts.set_data(pos[:,0], pos[:,1])
    return pts,

anim = FuncAnimation(
    fig, update, frames=frames, interval=50, blit=True, repeat=True
)

plt.show()
