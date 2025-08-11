
"""
Biological-motion point-light display
Happy, light-weight woman turning around.
Exactly 15 white dots on a black background.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------- skeleton definition --------------------------- #
# 15 joints (x, y, z) in metres – neutral pose (facing viewer)
JOINTS = np.array([
    [ 0.00, 1.80, 0.00],   # 0 head
    [ 0.00, 1.60, 0.00],   # 1 neck
    [-0.25, 1.50, 0.00],   # 2 right shoulder
    [ 0.25, 1.50, 0.00],   # 3 left shoulder
    [-0.35, 1.20, 0.00],   # 4 right elbow
    [ 0.35, 1.20, 0.00],   # 5 left  elbow
    [-0.40, 0.90, 0.00],   # 6 right wrist
    [ 0.40, 0.90, 0.00],   # 7 left  wrist
    [ 0.00, 1.10, 0.00],   # 8 pelvis (mid-hip)
    [-0.20, 1.05, 0.00],   # 9 right hip
    [ 0.20, 1.05, 0.00],   #10 left  hip
    [-0.20, 0.60, 0.00],   #11 right knee
    [ 0.20, 0.60, 0.00],   #12 left  knee
    [-0.20, 0.10, 0.00],   #13 right ankle
    [ 0.20, 0.10, 0.00],   #14 left  ankle
])

N_JOINTS = JOINTS.shape[0]

# --------------------------- animation setup ------------------------------ #
fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.axis('off')

scat = ax.scatter([], [], s=40, c='white')

# --------------------------- helper functions ----------------------------- #
def rotate_y(points, theta):
    """Rotate points about the y-axis by angle theta (radians)."""
    c, s = np.cos(theta), np.sin(theta)
    rot = np.array([[ c, 0,  s],
                    [ 0, 1,  0],
                    [-s, 0,  c]])
    return points @ rot.T

def project(points3d):
    """Orthographic projection: discard z."""
    return points3d[:, :2]

# --------------------------- animation loop ------------------------------- #
def update(frame):
    # rotation angle (one full turn every 180 frames ≈ 6 s at 30 fps)
    theta = 2 * np.pi * frame / 180
    pts = rotate_y(JOINTS, theta)

    # happy vertical bounce (light weight => light bounce)
    bounce = 0.05 * np.sin(2 * np.pi * frame / 60)
    pts[:, 1] += bounce

    # slight arm sway to add naturalness (±8° swing in sagittal plane)
    sway_angle = np.deg2rad(8) * np.sin(2 * np.pi * frame / 45)
    for idx in (4, 6):  # right elbow & wrist swing forward/back
        x, y, z = pts[idx]
        z_off =  (x * np.sin(sway_angle))
        x_off = -(x * (1 - np.cos(sway_angle)))
        pts[idx, 0] += x_off
        pts[idx, 2] += z_off
    for idx in (5, 7):  # left elbow & wrist (opposite phase)
        x, y, z = pts[idx]
        z_off = -(x * np.sin(sway_angle))
        x_off =  (x * (1 - np.cos(sway_angle)))
        pts[idx, 0] += x_off
        pts[idx, 2] += z_off

    # 2-D projection
    pts2d = project(pts)

    scat.set_offsets(pts2d)
    return scat,

ani = FuncAnimation(fig,
                    update,
                    frames=360,
                    interval=33,     # 30 fps
                    blit=True)

plt.show()
