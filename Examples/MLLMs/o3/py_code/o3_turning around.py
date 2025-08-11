
"""
Point-Light Biological Motion Stimulus
Action: A man turning around (360° spin)
Exactly 15 white dots on a black background are used to depict the joints.
The resulting animation is saved as “point_light_turning.gif”.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")       # head-less / non-interactive backend
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


# ------------------------------------------------------------------
# 1. 3-D skeleton definition (15 joints)
#    Units are arbitrary but roughly correspond to metres.
#    y = vertical (up), x = left/right, z = depth (towards/away)
# ------------------------------------------------------------------
skeleton_xyz = np.array([
    [ 0.00, 1.80, 0.00],   # 0: head top
    [ 0.00, 1.60, 0.00],   # 1: neck
    [ 0.25, 1.55, 0.00],   # 2: right shoulder
    [-0.25, 1.55, 0.00],   # 3: left  shoulder
    [ 0.35, 1.30, 0.05],   # 4: right elbow
    [-0.35, 1.30, 0.05],   # 5: left  elbow
    [ 0.40, 1.05, 0.10],   # 6: right wrist
    [-0.40, 1.05, 0.10],   # 7: left  wrist
    [ 0.00, 1.00, 0.00],   # 8: pelvis (mid-hip)
    [ 0.18, 1.00, 0.00],   # 9: right hip
    [-0.18, 1.00, 0.00],   # 10: left  hip
    [ 0.10, 0.60, 0.02],   # 11: right knee
    [-0.10, 0.60, 0.02],   # 12: left  knee
    [ 0.05, 0.10, 0.04],   # 13: right ankle
    [-0.05, 0.10, 0.04],   # 14: left  ankle
])


# ------------------------------------------------------------------
# 2. Helper: rotate the skeleton about the vertical (y) axis
# ------------------------------------------------------------------
def rotate_about_y(points, theta):
    """
    Rotate a set of 3-D points about the y-axis by angle `theta` (radians).
    """
    c, s = np.cos(theta), np.sin(theta)
    rot_matrix = np.array([[ c, 0.0,  s],
                           [0.0, 1.0, 0.0],
                           [-s, 0.0,  c]])
    return points @ rot_matrix.T     # (N,3) ⋅ (3,3)^T = (N,3)


# ------------------------------------------------------------------
# 3. Build the 2-D animation with Matplotlib
# ------------------------------------------------------------------
N_FRAMES = 180                     # one full turn (360°) over 180 frames
ANGLES   = np.linspace(0, 2*np.pi, N_FRAMES, endpoint=False)

fig, ax = plt.subplots(figsize=(4, 6), facecolor='black')
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(0.0, 2.0)
ax.set_aspect('equal')
ax.axis('off')                     # remove axes ticks/frame

# Draw initial scatter; marker size tuned for visibility
scatter = ax.scatter([], [], s=40, c='white')

def init():
    scatter.set_offsets(np.zeros((0, 2)))
    return (scatter,)

def update(frame_idx):
    theta = ANGLES[frame_idx]
    rotated = rotate_about_y(skeleton_xyz, theta)
    
    # Orthographic 2-D projection: simply take x & y components
    xy = rotated[:, [0, 1]]
    scatter.set_offsets(xy)
    return (scatter,)

anim = FuncAnimation(
    fig,
    update,
    frames=N_FRAMES,
    init_func=init,
    interval=40,           # milliseconds between frames (~25 fps)
    blit=True
)

# ------------------------------------------------------------------
# 4. Save to GIF (white dots on black background)
# ------------------------------------------------------------------
gif_filename = "point_light_turning.gif"
anim.save(gif_filename, writer=PillowWriter(fps=25))

# The script ends here.  The GIF file can be viewed to see the stimulus.
