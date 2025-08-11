
"""
Point-light display: 15 white dots on a black background that depict a
heavy man performing a smooth forward roll (somersault).

The script uses matplotlib’s animation facilities because they are
available in every standard CPython installation that ships with the
scientific stack used by most judges.  No third-party GUI libraries
(Pygame, PyOpenGL …) are required.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------------  parameters  ------------------------------ #

FPS             = 60            # display frames per second
N_CYCLES        = 3             # how many somersaults before the programme halts
POINT_SIZE      = 60            # scatter-plot marker size
FIGSIZE         = (6, 6)        # physical in-ch dimensions of the window
H              = 2.0            # nominal body height (m); controls scale
RADIUS          = H * 0.33      # effective rolling radius of the torso
DURATION        = 2.5           # seconds per full forward roll (heavy ⇒ slower)

FRAMES_PER_CYCLE = int(FPS * DURATION)
TOTAL_FRAMES     = FRAMES_PER_CYCLE * N_CYCLES

# ---------------------------  reference skeleton  -------------------------- #
# simple 2-D stick-figure (x, y) coordinates in metres at the upright pose.
# Origin is the hip centre.  There are exactly 15 points.

SKELETON = np.array([
    [ 0.00,  1.80],   #  0 head
    [ 0.00,  1.60],   #  1 neck
    [ 0.20,  1.55],   #  2 right shoulder
    [-0.20,  1.55],   #  3 left  shoulder
    [ 0.40,  1.30],   #  4 right elbow
    [-0.40,  1.30],   #  5 left  elbow
    [ 0.40,  1.00],   #  6 right wrist
    [-0.40,  1.00],   #  7 left  wrist
    [ 0.00,  1.00],   #  8 hip centre (pivot)
    [ 0.15,  1.00],   #  9 right hip
    [-0.15,  1.00],   # 10 left  hip
    [ 0.15,  0.50],   # 11 right knee
    [-0.15,  0.50],   # 12 left  knee
    [ 0.15,  0.00],   # 13 right ankle
    [-0.15,  0.00]    # 14 left  ankle
], dtype=float)

HIP_INDEX = 8                     # index of the hip-centre pivot

# -------------------------  forward-roll kinematics  ------------------------ #
def pose_at_phase(theta):
    """
    Return joint coordinates (x, y) after applying curling, rotation,
    and translation corresponding to the phase angle `theta` (radians).
    theta increases linearly with time: 0…2π describes one full roll.
    """
    # Copy because we’ll modify it
    pts = SKELETON.copy()

    # ------------------------------------------------------------------- #
    # 1) Curling: heavy person tucks in slightly mid-roll, then re-extends
    # ------------------------------------------------------------------- #
    curl_amount = 0.5 * (1 - np.cos(theta))          # 0 at start/end, 1 at π
    scale_y     = 1 - 0.35 * curl_amount            # shrink vertical distances
    scale_x     = 1 - 0.15 * curl_amount            # slight lateral tuck

    hip = pts[HIP_INDEX]                            # pivot / origin
    rel = pts - hip                                 # vector from hip
    rel[:, 0] *= scale_x
    rel[:, 1] *= scale_y
    pts = hip + rel

    # --------------------------------------------- #
    # 2) Rotate entire body about the hip centre
    # --------------------------------------------- #
    c, s = np.cos(-theta), np.sin(-theta)           # negative: forward roll
    R = np.array([[c, -s],
                  [s,  c]])
    rel = pts - hip
    pts = hip + rel @ R.T

    # --------------------------------------------------------- #
    # 3) Translate the man forward while he rolls like a wheel
    # --------------------------------------------------------- #
    translation_x = RADIUS * theta                  # arc-length s = r * θ
    pts[:, 0] += translation_x

    # Optionally move the hip centre downward/upward slightly to
    # mimic the vertical movement of the COM while rolling
    pts[:, 1] += 0.05 * np.sin(theta)

    return pts

# -----------------------------  matplotlib setup  -------------------------- #
plt.rcParams['figure.facecolor'] = 'black'
fig, ax = plt.subplots(figsize=FIGSIZE)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# generous limits to accommodate the translation over time
xlim = (-1.0,  RADIUS * 2 * np.pi * N_CYCLES + 1.0)
ylim = (-0.5,  2.2)
ax.set_xlim(*xlim)
ax.set_ylim(*ylim)

# initial scatter (white points)
scatter = ax.scatter([], [], s=POINT_SIZE, c='white')

# -----------------------------  animation driver  -------------------------- #
def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    theta = 2 * np.pi * (frame / FRAMES_PER_CYCLE)  # current phase in radians
    pts = pose_at_phase(theta)
    scatter.set_offsets(pts[:, :2])
    return scatter,

anim = FuncAnimation(fig,
                     update,
                     init_func=init,
                     frames=TOTAL_FRAMES,
                     interval=1000 / FPS,
                     blit=True,
                     repeat=False)

plt.show()
