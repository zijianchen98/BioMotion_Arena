
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
# Basic joint layout (3-D) for a heavy, slightly slumped woman
# -----------------------------
# 15 joints: head, neck, L/R shoulders, L/R elbows, L/R wrists,
#            hip-centre, L/R hips, L/R knees, L/R ankles
joints = np.array([
    [ 0.00, 1.80, -0.10],   # head (slightly forward => negative z)
    [ 0.00, 1.60, -0.12],   # neck
    [-0.40, 1.48, -0.08],   # L-shoulder (broader body -> 0.40)
    [ 0.40, 1.48, -0.08],   # R-shoulder
    [-0.55, 1.15,  0.04],   # L-elbow
    [ 0.55, 1.15, -0.04],   # R-elbow
    [-0.55, 0.88,  0.15],   # L-wrist
    [ 0.55, 0.88, -0.15],   # R-wrist
    [ 0.00, 1.00,  0.00],   # hip centre
    [-0.35, 1.00,  0.02],   # L-hip  (heavy/broad)
    [ 0.35, 1.00, -0.02],   # R-hip
    [-0.35, 0.55,  0.05],   # L-knee
    [ 0.35, 0.55, -0.05],   # R-knee
    [-0.35, 0.00,  0.08],   # L-ankle
    [ 0.35, 0.00, -0.08]    # R-ankle
])

# -----------------------------
# Simple perspective projector
# -----------------------------
def project(pts3, camera_z=4.0):
    """
    Perspective projection onto the x-y plane with camera on +z axis.
    """
    z = pts3[:, 2]
    factor = camera_z / (camera_z - z)  # focal length = camera_z
    xs = pts3[:, 0] * factor
    ys = pts3[:, 1] * factor
    return np.vstack((xs, ys)).T

# -----------------------------
# Animation parameters
# -----------------------------
n_frames   = 240          # ~8 s at 30 fps
fps        = 30
angles     = np.linspace(0, 2*np.pi, n_frames, endpoint=False)  # 0-360° turn

# -----------------------------
# Matplotlib figure
# -----------------------------
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_facecolor('black')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-0.2, 2.0)
ax.set_aspect('equal')
ax.axis('off')

# Initial scatter plot (white points)
scat = ax.scatter([], [], s=35, c='white')

# -----------------------------
# Each frame: rotate + project
# -----------------------------
def update(frame):
    angle = angles[frame]
    cos_a, sin_a = np.cos(angle), np.sin(angle)
    rot_y = np.array([[ cos_a, 0, sin_a],
                      [     0, 1,     0],
                      [-sin_a, 0, cos_a]])
    pts3 = joints @ rot_y.T
    pts2 = project(pts3)
    scat.set_offsets(pts2)
    return scat,

ani = FuncAnimation(fig, update, frames=n_frames, interval=1000/fps, blit=True)

plt.show()
