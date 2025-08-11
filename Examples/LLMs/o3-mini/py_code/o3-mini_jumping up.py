
"""
This program creates an animation of a jumping man represented by 15 white “point‐lights”
against a solid black background. The marker positions are defined in a base “standing”
posture, and then modified over time through a sequence of keyframes (standing, crouching,
push‐off, apex, landing, and recovery), with smooth linear interpolation in between.
The resulting motion is meant to be biomechanically plausible for a jump.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
# Base posture definition (standing)
# Markers are indexed from 0 to 14 and represent:
#  0: Head
#  1: Left Shoulder
#  2: Right Shoulder
#  3: Left Elbow
#  4: Right Elbow
#  5: Left Wrist
#  6: Right Wrist
#  7: Spine
#  8: Left Hip
#  9: Right Hip
# 10: Left Knee
# 11: Right Knee
# 12: Left Ankle
# 13: Right Ankle
# 14: Pelvis (central lower trunk)
base_posture = {
    0:  np.array([ 0.00, 1.80]),    # Head
    1:  np.array([-0.25, 1.60]),    # Left Shoulder
    2:  np.array([ 0.25, 1.60]),    # Right Shoulder
    3:  np.array([-0.55, 1.45]),    # Left Elbow
    4:  np.array([ 0.55, 1.45]),    # Right Elbow
    5:  np.array([-0.75, 1.30]),    # Left Wrist
    6:  np.array([ 0.75, 1.30]),    # Right Wrist
    7:  np.array([ 0.00, 1.50]),    # Spine
    8:  np.array([-0.30, 1.00]),    # Left Hip
    9:  np.array([ 0.30, 1.00]),    # Right Hip
    10: np.array([-0.30, 0.50]),    # Left Knee
    11: np.array([ 0.30, 0.50]),    # Right Knee
    12: np.array([-0.30, 0.00]),    # Left Ankle
    13: np.array([ 0.30, 0.00]),    # Right Ankle
    14: np.array([ 0.00, 1.05])     # Pelvis
}

# -----------------------------
# Keyframes and corresponding offset modifications.
# Each keyframe is a tuple: (time_in_seconds, modifications_dict)
# The modifications_dict maps marker index to an (dx, dy) offset that should be added to the base posture.
#
# The key times:
# 0.0 sec    : Standing (no modifications)
# 0.3 sec    : Crouching (lowering head, shoulders, pelvis, bending elbows/wrists/knees)
# 0.5 sec    : Push off (begin extension, arms swinging upward, pelvis rising)
# 1.0 sec    : Apex of jump (highest vertical position, arms and torso lifted)
# 1.5 sec    : Landing (brief downward adjustment)
# 2.0 sec    : Recovery back to standing (zero offsets)
keyframes = [
    (0.0, {}),  # Standing baseline
    (0.3, {
        0:  (0.0, -0.10),   # Head slightly lowered
        1:  (0.0, -0.10),   # Left Shoulder
        2:  (0.0, -0.10),   # Right Shoulder
        7:  (0.0, -0.10),   # Spine
        8:  (0.0, -0.05),   # Left Hip
        9:  (0.0, -0.05),   # Right Hip
        3:  (0.0, -0.15),   # Left Elbow (bend more)
        4:  (0.0, -0.15),   # Right Elbow
        5:  (0.0, -0.20),   # Left Wrist (hang lower)
        6:  (0.0, -0.20),   # Right Wrist
        10: (0.0, -0.20),   # Left Knee (more bent)
        11: (0.0, -0.20),   # Right Knee
        14: (0.0, -0.15)    # Pelvis lowers noticeably
    }),
    (0.5, {
        0:  (0.0, -0.05),
        1:  (0.0, -0.05),
        2:  (0.0, -0.05),
        7:  (0.0,  0.00),
        3:  (0.0,  0.00),
        4:  (0.0,  0.00),
        5:  (0.0, +0.10),  # Arms swing upward
        6:  (0.0, +0.10),
        8:  (0.0,  0.00),
        9:  (0.0,  0.00),
        10: (0.0,  0.00),
        11: (0.0,  0.00),
        14: (0.0, -0.05)   # Pelvis begins rising
    }),
    (1.0, {
        0:  (0.0, +0.50),   # Head is higher at apex
        1:  (0.0, +0.50),
        2:  (0.0, +0.50),
        7:  (0.0, +0.50),
        3:  (0.0, +0.30),
        4:  (0.0, +0.30),
        5:  (0.0, +0.30),
        6:  (0.0, +0.30),
        8:  (0.0, +0.30),
        9:  (0.0, +0.30),
        10: (0.0, +0.10),
        11: (0.0, +0.10),
        14: (0.0, +0.80)    # Pelvis at its peak displacement
    }),
    (1.5, {
        0:  (0.0, -0.05),
        1:  (0.0, -0.05),
        2:  (0.0, -0.05),
        7:  (0.0,  0.00),
        5:  (0.0, -0.10),   # Arms adjust on landing
        6:  (0.0, -0.10),
        14: (0.0, -0.05)
    }),
    (2.0, {})  # Back to standing posture
]

# Total duration of the jump animation (seconds)
T_total = 2.0

def get_offset_at_time(t, marker):
    """
    Given a time t (in seconds) and a marker index, return the (dx, dy) offset for that marker using
    linear interpolation between the relevant keyframes.
    If a keyframe does not specify an offset for a marker, treat it as (0,0).
    """
    # If t is at or before the first keyframe, return its offset (or (0,0))
    if t <= keyframes[0][0]:
        return np.array(keyframes[0][1].get(marker, (0.0, 0.0)))
    # If t is after the last keyframe, return that offset
    if t >= keyframes[-1][0]:
        return np.array(keyframes[-1][1].get(marker, (0.0, 0.0)))
    
    # Otherwise, find the surrounding keyframes
    for i in range(len(keyframes)-1):
        t0, mods0 = keyframes[i]
        t1, mods1 = keyframes[i+1]
        if t0 <= t <= t1:
            # Get offsets for marker in both frames (default to (0,0) if not specified)
            off0 = np.array(mods0.get(marker, (0.0, 0.0)))
            off1 = np.array(mods1.get(marker, (0.0, 0.0)))
            # Compute interpolation factor (0 at t0, 1 at t1)
            factor = (t - t0) / (t1 - t0)
            return off0 + factor * (off1 - off0)
    return np.array((0.0, 0.0))

def get_current_posture(t):
    """
    Compute the current positions for all 15 markers at time t by adding the base posture and
    the interpolated offset modifications.
    Returns a NumPy array of shape (15, 2) containing x,y coordinates.
    """
    positions = []
    for marker in range(15):
        base = base_posture[marker]
        offset = get_offset_at_time(t, marker)
        pos = base + offset
        positions.append(pos)
    return np.array(positions)

# -----------------------------
# Set up the matplotlib figure and scatter plot.
fig, ax = plt.subplots(figsize=(6,8))
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 3.0)
ax.set_aspect('equal')
ax.axis('off')
scat = ax.scatter([], [], s=100, c='white')  # white point-lights

# -----------------------------
# Animation parameters and update function.
fps = 60
dt = 1/fps
total_frames = int(T_total / dt) + 1

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    t = frame * dt
    pos = get_current_posture(t)
    scat.set_offsets(pos)
    return scat,

anim = FuncAnimation(fig, update, frames=total_frames, init_func=init,
                     interval=dt*1000, blit=True, repeat=True)

# Display the animation
plt.show()