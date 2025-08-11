
"""
Point-light biological–motion stimulus:
15 white dots (joints) of a sad, heavy person turning around continuously.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------------------------------------
# 3-D SKELETON (single, statically-posed frame)
# ---------------------------------------------
# Order: head, neck, r-shoulder, l-shoulder, r-elbow, l-elbow,
#        r-wrist, l-wrist, pelvis, r-hip, l-hip,
#        r-knee, l-knee, r-ankle, l-ankle
# The figure is slightly hunched forward to convey sadness/heaviness.
base_skeleton = np.array([
    [ 0.00, 1.75,  0.00],   # head
    [ 0.00, 1.55, -0.02],   # neck
    [ 0.15, 1.45, -0.05],   # right shoulder
    [-0.15, 1.45, -0.05],   # left  shoulder
    [ 0.30, 1.20, -0.10],   # right elbow
    [-0.30, 1.20, -0.10],   # left  elbow
    [ 0.35, 0.95, -0.15],   # right wrist
    [-0.35, 0.95, -0.15],   # left  wrist
    [ 0.00, 1.00,  0.00],   # pelvis (mid-hip)
    [ 0.12, 0.95,  0.02],   # right hip
    [-0.12, 0.95,  0.02],   # left  hip
    [ 0.15, 0.55,  0.05],   # right knee
    [-0.15, 0.55,  0.05],   # left  knee
    [ 0.18, 0.10,  0.10],   # right ankle
    [-0.18, 0.10,  0.10],   # left  ankle
])

# ---------------------------
# FUNCTIONS FOR THE ANIMATION
# ---------------------------
def rotate(points, yaw):
    """
    Rotate points around the vertical (Y) axis by 'yaw' radians.
    """
    c, s = np.cos(yaw), np.sin(yaw)
    rot_matrix = np.array([[ c, 0,  s],
                           [ 0, 1,  0],
                           [-s, 0,  c]])
    return points @ rot_matrix.T

def project(points):
    """
    Orthographic projection dropping the Z dimension.
    Returns 2-D coordinates for plotting.
    """
    return points[:, [0, 1]]

def sad_bounce(frame, total_frames):
    """
    Produces a small, slow vertical bob (heavy/sluggish feel).
    """
    phase = 2 * np.pi * frame / total_frames
    return 0.03 * np.sin(phase)  # small amplitude, low frequency

# -------------
# Matplotlib set-up
# -------------
fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Scatter for the 15 joints
scat = ax.scatter([], [], s=30, c='white')

# Frame boundary (kept constant)
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)

# ----------------
# Animation driver
# ----------------
TOTAL_FRAMES = 240           # ~8 seconds at 30 fps
FULL_TURN    = 2 * np.pi     # 360° rotation

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    # Compute yaw angle for continuous turn
    yaw = FULL_TURN * frame / TOTAL_FRAMES
    # Apply rotation
    pts3d = rotate(base_skeleton, yaw)
    # Apply vertical bob
    pts3d[:, 1] += sad_bounce(frame, TOTAL_FRAMES)
    # Project to 2-D
    pts2d = project(pts3d)
    # Update the scatter plot
    scat.set_offsets(pts2d)
    return scat,

ani = FuncAnimation(fig,
                    update,
                    frames=TOTAL_FRAMES,
                    init_func=init,
                    interval=33,    # ≈30 fps
                    blit=True)

plt.show()
