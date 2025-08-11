
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the 15 body‐point labels:
# 0: head
# 1: neck
# 2: left shoulder
# 3: right shoulder
# 4: left elbow
# 5: right elbow
# 6: left wrist
# 7: right wrist
# 8: mid-torso
# 9: left hip
# 10: right hip
# 11: left knee
# 12: right knee
# 13: left ankle
# 14: right ankle

# Upright pose (x, y) in meters
upright = np.array([
    [ 0.00, 1.80],  # head
    [ 0.00, 1.60],  # neck
    [-0.20, 1.50],  # left shoulder
    [ 0.20, 1.50],  # right shoulder
    [-0.40, 1.20],  # left elbow
    [ 0.40, 1.20],  # right elbow
    [-0.40, 0.90],  # left wrist
    [ 0.40, 0.90],  # right wrist
    [ 0.00, 1.20],  # mid-torso
    [-0.20, 1.00],  # left hip
    [ 0.20, 1.00],  # right hip
    [-0.20, 0.50],  # left knee
    [ 0.20, 0.50],  # right knee
    [-0.20, 0.10],  # left ankle
    [ 0.20, 0.10],  # right ankle
])

# Compute bow pose by rotating the upper body forward around the hip center
hip_center = (upright[9] + upright[10]) / 2.0
angle = -1.0  # about -57 degrees forward
R = np.array([[np.cos(angle), -np.sin(angle)],
              [np.sin(angle),  np.cos(angle)]])

bow = upright.copy()

# Indices of the upper body to rotate:
upper_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
for i in upper_indices:
    bow[i] = hip_center + R.dot(upright[i] - hip_center)

# Bend knees slightly forward/up
bow[11] = upright[11] + np.array([0.07, 0.07])  # left knee
bow[12] = upright[12] + np.array([0.07, 0.07])  # right knee

# Shift ankles slightly forward
bow[13] = upright[13] + np.array([0.05, 0.00])  # left ankle
bow[14] = upright[14] + np.array([0.05, 0.00])  # right ankle

# Set up the plot
fig, ax = plt.subplots(figsize=(5, 8))
ax.set_facecolor('black')
scat = ax.scatter(upright[:, 0], upright[:, 1],
                  c='white', s=100)
ax.set_xlim(-0.6, 0.6)
ax.set_ylim( 0.0, 2.0)
ax.set_aspect('equal')
ax.axis('off')

# Animation parameters
total_frames = 120
half = total_frames // 2

def ease(t):
    """Ease in-out using a cosine ramp 0..1."""
    return (1 - np.cos(np.pi * t)) / 2

def animate(frame):
    # Compute normalized progress 0->1->0 over the animation
    if frame <= half:
        t = frame / half
    else:
        t = (total_frames - frame) / half
    w = ease(t)
    # Interpolate between upright and bow
    current = (1 - w) * upright + w * bow
    scat.set_offsets(current)
    return scat,

anim = FuncAnimation(
    fig, animate,
    frames=total_frames,
    interval=50,
    blit=True
)

plt.show()
