
"""
Point–light biological–motion stimulus
--------------------------------------

Fifteen white dots portray a sad, heavy woman who jumps forward.  The motion
is shown on a solid black background and is biomechanically plausible (crouch
→ take-off → flight → landing → recovery).

Running the script pops up a Matplotlib window that plays the animation in a
continuous loop.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------------------------------------------------------
# 1.  Skeleton layout
# ------------------------------------------------------------------
#
# We use exactly 15 anatomical landmarks (indices below):
#
#   0  head            8  spine / pelvis centre
#   1  neck            9  left–hip          10 right–hip
#   2  left-shoulder  3  right-shoulder
#   4  left-elbow     5  right-elbow
#   6  left-wrist     7  right-wrist
#  11  left-knee      12 right-knee
#  13  left-ankle     14 right-ankle
#
# Each pose below is given as absolute X/Y coordinates in an upright
# reference frame where (0,0) is the pelvis in the initial crouch.
# Poses are *relative* – a forward translation that grows with time is
# added later so the character travels forward while jumping.

key_times = np.asarray([0.00, 0.25, 0.50, 0.75, 1.00])     # normalised timeline

# Key-frame poses (shape: n_keyframes × 15 joints × 2 coordinates)
poses = np.array(
    # x,  y
    [
        # ─────────────────────────────────────  t = 0.00  (deep crouch, sad posture)
        [[ 0.00,  1.00],   # head
         [ 0.00,  0.80],   # neck
         [-0.30,  0.75],   # L shoulder
         [ 0.30,  0.75],   # R shoulder
         [-0.45,  0.50],   # L elbow
         [ 0.45,  0.50],   # R elbow
         [-0.45,  0.20],   # L wrist
         [ 0.45,  0.20],   # R wrist
         [ 0.00,  0.00],   # spine / pelvis
         [-0.20,  0.00],   # L hip
         [ 0.20,  0.00],   # R hip
         [-0.25, -0.50],   # L knee
         [ 0.25, -0.50],   # R knee
         [-0.25, -1.00],   # L ankle
         [ 0.25, -1.00]],  # R ankle

        # ─────────────────────────────────────  t = 0.25  (take-off)
        [[ 0.00,  1.25],
         [ 0.00,  1.05],
         [-0.30,  1.00],
         [ 0.30,  1.00],
         [-0.35,  0.80],
         [ 0.35,  0.80],
         [-0.35,  0.50],
         [ 0.35,  0.50],
         [ 0.00,  0.20],
         [-0.20,  0.20],
         [ 0.20,  0.20],
         [-0.25, -0.15],
         [ 0.25, -0.15],
         [-0.25, -0.90],
         [ 0.25, -0.90]],

        # ─────────────────────────────────────  t = 0.50  (flight apex)
        [[ 0.00,  1.60],
         [ 0.00,  1.40],
         [-0.30,  1.35],
         [ 0.30,  1.35],
         [-0.35,  1.10],
         [ 0.35,  1.10],
         [-0.40,  0.90],
         [ 0.40,  0.90],
         [ 0.00,  0.50],
         [-0.20,  0.50],
         [ 0.20,  0.50],
         [-0.25,  0.10],
         [ 0.25,  0.10],
         [-0.25, -0.70],
         [ 0.25, -0.70]],

        # ─────────────────────────────────────  t = 0.75  (landing – knees flex)
        [[ 0.00,  1.30],
         [ 0.00,  1.10],
         [-0.30,  1.05],
         [ 0.30,  1.05],
         [-0.35,  0.80],
         [ 0.35,  0.80],
         [-0.35,  0.50],
         [ 0.35,  0.50],
         [ 0.00,  0.05],
         [-0.20,  0.05],
         [ 0.20,  0.05],
         [-0.30, -0.45],
         [ 0.30, -0.45],
         [-0.30, -1.00],
         [ 0.30, -1.00]],

        # ─────────────────────────────────────  t = 1.00  (recovery – slight crouch)
        [[ 0.00,  1.15],
         [ 0.00,  0.95],
         [-0.30,  0.90],
         [ 0.30,  0.90],
         [-0.45,  0.65],
         [ 0.45,  0.65],
         [-0.45,  0.35],
         [ 0.45,  0.35],
         [ 0.00,  0.00],
         [-0.20,  0.00],
         [ 0.20,  0.00],
         [-0.25, -0.40],
         [ 0.25, -0.40],
         [-0.25, -1.00],
         [ 0.25, -1.00]],
    ]
)

# Total forward travel (in the same units as the above coordinates)
FORWARD_DISTANCE = 3.0


# ------------------------------------------------------------------
# 2.  Helper: interpolate a pose for an arbitrary time t ∈ [0, 1]
# ------------------------------------------------------------------
def interpolate_pose(t):
    """
    Linearly interpolate the 15 joint positions for normalised time t.
    Adds a forward (x) translation so the stimulus travels left → right.
    """
    # Find which keyframe interval t falls into
    i = np.searchsorted(key_times, t) - 1
    i = np.clip(i, 0, len(key_times) - 2)
    t0, t1 = key_times[i], key_times[i + 1]
    alpha = (t - t0) / (t1 - t0)

    # Linear interpolation of joint coordinates
    pose = (1 - alpha) * poses[i] + alpha * poses[i + 1]

    # Add forward progression
    forward_x = FORWARD_DISTANCE * t
    pose = pose.copy()
    pose[:, 0] += forward_x
    return pose


# ------------------------------------------------------------------
# 3.  Animation with Matplotlib
# ------------------------------------------------------------------
frames = 200                      # number of animation frames per cycle
interval_ms = 1000 / 60           # ~60 Hz playback

fig, ax = plt.subplots(figsize=(4, 6), facecolor="black")
ax.set_facecolor("black")
ax.set_aspect("equal")
ax.set_xlim(-1, FORWARD_DISTANCE + 1)
ax.set_ylim(-1.5, 2.0)
ax.axis("off")

# Scatter plot for the 15 white points (initialised at t=0)
scatter = ax.scatter([], [], s=50, c="white")

def init():
    scatter.set_offsets(np.zeros((15, 2)))
    return scatter,

def update(frame_number):
    # Normalised time t in [0, 1]; repeat forever
    t = (frame_number % frames) / (frames - 1)
    pose = interpolate_pose(t)
    scatter.set_offsets(pose)
    return scatter,

ani = FuncAnimation(fig,
                    update,
                    init_func=init,
                    frames=frames,
                    interval=interval_ms,
                    blit=True)

plt.show()
