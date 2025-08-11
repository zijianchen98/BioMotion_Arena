
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------  PARAMETERS  ------------------- #
N_POINTS = 15                        # exactly 15 point-lights
FPS       = 30                       # frames per second
N_FRAMES  = 120                      # frames in one bow cycle

# segment lengths (arbitrary, in “body units”)
TORSO_LEN   = 0.6                    # pelvis → neck
HEAD_OFF    = 0.25                   # neck → head
SHOULDER_W  = 0.40                   # shoulder span
UPPER_ARM   = 0.40                   # shoulder → elbow
FOREARM     = 0.40                   # elbow → wrist
HIP_W       = 0.30                   # hip span
THIGH_LEN   = 0.60                   # hip → knee
SHIN_LEN    = 0.60                   # knee → ankle

MAX_BOW = np.deg2rad(60)             # deepest forward lean

# -------------------  SKELETON GENERATION  ------------------- #
def skeleton_points(theta):
    """
    Generate (x, y) coordinates for all 15 joints at a given torso angle.
    Pelvis is origin.  Positive y points upward.
    """
    sin_t, cos_t = np.sin(theta), np.cos(theta)

    # unit torso vector (rotated)
    torso_vec = np.array([sin_t,  cos_t]) * TORSO_LEN          # forward lean → positive x

    # pelvis / hips
    pelvis  = np.array([0.0, 0.0])
    lh      = pelvis + np.array([-HIP_W/2, 0.0])               # left hip
    rh      = pelvis + np.array([ HIP_W/2, 0.0])               # right hip

    # knees & ankles (legs stay vertical)
    lk = lh + np.array([0.0, -THIGH_LEN])
    rk = rh + np.array([0.0, -THIGH_LEN])
    la = lk + np.array([0.0, -SHIN_LEN])
    ra = rk + np.array([0.0, -SHIN_LEN])

    # upper torso
    neck = pelvis + torso_vec
    # perpendicular (rotate torso_vec by +90°) then normalise
    perp = np.array([-cos_t, sin_t])
    perp /= np.linalg.norm(perp)

    ls = neck + perp * (SHOULDER_W/2)                          # left sh.
    rs = neck - perp * (SHOULDER_W/2)                          # right sh.

    # arms (hang roughly downwards in world coordinates)
    le = ls + np.array([0.0, -UPPER_ARM])
    re = rs + np.array([0.0, -UPPER_ARM])
    lw = le + np.array([0.0, -FOREARM])
    rw = re + np.array([0.0, -FOREARM])

    # head centre
    head = neck + torso_vec / np.linalg.norm(torso_vec) * HEAD_OFF

    # order (total = 15)
    pts = [head, neck, ls, rs, le, re, lw, rw,
           pelvis, lh, rh, lk, rk, la, ra]
    return np.stack(pts)

# -------------------  ANIMATION  ------------------- #
fig, ax = plt.subplots(figsize=(4, 7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# fixed limits so figure doesn’t rescale
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-1.6, 1.2)

# create scatter of 15 white points
scat = ax.scatter([], [], s=50, c='white')

def init():
    scat.set_offsets(np.empty((N_POINTS, 2)))
    return scat,

def update(frame):
    # time parameter 0 … 1
    t = frame / N_FRAMES
    # smooth “bow” angle: 0 → MAX_BOW → 0 using cosine ease
    theta = MAX_BOW * 0.5 * (1 - np.cos(2 * np.pi * t))
    pts = skeleton_points(theta)
    scat.set_offsets(pts)
    return scat,

anim = FuncAnimation(fig, update, frames=N_FRAMES, init_func=init,
                     interval=1000/FPS, blit=True, repeat=True)

plt.show()
