
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------  point-light definition (15 joints) -----------------
# (x, y) in meters relative to the hip while standing
JOINTS = np.array([
    [ 0.00, 1.80],   # 0  head
    [ 0.00, 1.60],   # 1  neck
    [ 0.15, 1.55],   # 2  right shoulder
    [-0.15, 1.55],   # 3  left  shoulder
    [ 0.30, 1.30],   # 4  right elbow
    [-0.30, 1.30],   # 5  left  elbow
    [ 0.35, 1.05],   # 6  right wrist
    [-0.35, 1.05],   # 7  left  wrist
    [ 0.00, 1.00],   # 8  hip / pelvis (rotation centre)
    [ 0.12, 0.55],   # 9  right knee
    [-0.12, 0.55],   # 10 left  knee
    [ 0.12, 0.10],   # 11 right ankle
    [-0.12, 0.10],   # 12 left  ankle
    [ 0.18, 0.00],   # 13 right toe
    [-0.18, 0.00],   # 14 left  toe
])

HIP_INDEX = 8                     # hip is the rotation centre
RADIUS     = 0.75                 # “rolling wheel” radius (metres)
N_FRAMES   = 240                  # total frames in the animation
DURATION   = 8                    # seconds (for FuncAnimation)

# -------------  helper functions ----------------------------------
def rotate(points, angle):
    """
    Rotate an (N,2) array of points by 'angle' (radians) around (0,0).
    """
    c, s = np.cos(angle), np.sin(angle)
    R = np.array([[c, -s],
                  [s,  c]])
    return points @ R.T


def posture(frame_idx):
    """
    Compute joint positions for animation frame `frame_idx`.
    Returns (N,2) array in world coordinates.
    """
    # progress 0 … 2π
    a = 2 * np.pi * frame_idx / (N_FRAMES - 1)

    # tuck factor: body compresses while upside-down (a≈π)
    tuck = 0.8 + 0.2 * np.cos(a)         # 1.0 when upright, ~0.6 inverted

    # vector from hip to every joint
    rel = JOINTS - JOINTS[HIP_INDEX]

    # scale (tuck) distances, but keep hip at origin
    rel_scaled          = rel * tuck
    rel_scaled[HIP_INDEX] = [0, 0]

    # rotate entire skeleton
    rotated = rotate(rel_scaled, -a)     # negative -> forward roll

    # horizontal translation so body “rolls” along ground like a wheel
    dx = RADIUS * a                      # arc length s = r a
    # vertical translation to keep lowest joint exactly on ground (y=0)
    min_y = rotated[:, 1].min()
    dy    = -min_y                       # lift upwards so lowest === 0

    world = rotated + [dx, dy]
    return world


# -------------  animation set-up ----------------------------------
plt.rcParams['toolbar'] = 'None'   # cleaner window
fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# scatter plot (white points)
scat = ax.scatter([], [], s=40, c='white')

# set sane limits that contain the full roll
ax.set_xlim(-1, RADIUS * 2 * np.pi + 1)
ax.set_ylim(-0.2, 2.0)

def init():
    scat.set_offsets(np.zeros((15, 2)))
    return scat,

def update(frame):
    pts = posture(frame)
    scat.set_offsets(pts)
    return scat,

ani = FuncAnimation(fig,
                    update,
                    frames=N_FRAMES,
                    init_func=init,
                    interval=1000 * DURATION / N_FRAMES,
                    blit=True,
                    repeat=True)

plt.show()
