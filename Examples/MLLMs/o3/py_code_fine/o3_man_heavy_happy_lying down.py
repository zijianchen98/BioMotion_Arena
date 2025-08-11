
"""
Point-Light Biological Motion Stimulus
Subject : “Happy heavy man, lying down”
Points  : 15 white lights on a solid black background
Usage   : Run the script – a matplotlib window with the animation will appear.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------------------  PARAMETERS  ---------------------------------------- #
N_POINTS           = 15                 # must stay 15
FPS                = 30                 # frames-per-second for the animation
DURATION_SEC       = 8                  # how long the clip lasts
BREATH_CYCLES      = 4                  # number of inhale/exhale cycles
BREATH_AMPLITUDE   = 0.02               # vertical displacement caused by breathing
ARM_WIGGLE_DEG     = 6                  # minor arm rotation (deg) for liveliness
# ----------------------------------------------------------------------------- #

# ----------------------  SKELETON LAYOUT ------------------------------------ #
# The figure is a side view of a person lying along the X-axis (head to the
# right, feet to the left).  Units are arbitrary (0–1 convenient for display).

#                   (y ↑)
#        ankle knee hip shoulder neck head  →  (x →)
#        12    10   8    2        1    0
#
#        13    11   9    3              (lower chain – looking from the side)
#
# A point (#14) marks the belly / centre of mass for the “heavy” impression.

base_positions = np.array([
    [0.80, 0.50],   #  0 – head
    [0.75, 0.50],   #  1 – neck
    [0.70, 0.57],   #  2 – shoulder (upper, visible side)
    [0.70, 0.43],   #  3 – shoulder (lower, hidden side)
    [0.55, 0.62],   #  4 – elbow (upper)
    [0.55, 0.38],   #  5 – elbow (lower)
    [0.40, 0.62],   #  6 – wrist (upper)
    [0.40, 0.38],   #  7 – wrist (lower)
    [0.55, 0.56],   #  8 – hip (upper)
    [0.55, 0.44],   #  9 – hip (lower)
    [0.30, 0.56],   # 10 – knee (upper)
    [0.30, 0.44],   # 11 – knee (lower)
    [0.10, 0.56],   # 12 – ankle (upper)
    [0.10, 0.44],   # 13 – ankle (lower)
    [0.60, 0.50],   # 14 – belly / centre of mass
])

assert base_positions.shape == (N_POINTS, 2), "Exactly 15 points required."

# Indices helpful for subtle motions
BREATH_POINTS = [1, 2, 3, 8, 9, 14]                      # torso & belly
ARM_UPPER     = [4, 6]                                   # upper arm chain (visible side)

# --------------------  ANIMATION SETUP -------------------------------------- #
fig, ax = plt.subplots(figsize=(4, 4))
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

scat = ax.scatter(base_positions[:, 0],
                  base_positions[:, 1],
                  c='white',
                  s=35)

total_frames = int(DURATION_SEC * FPS)
omega_breath = 2 * np.pi * BREATH_CYCLES / total_frames
arm_wiggle   = np.deg2rad(ARM_WIGGLE_DEG)                # convert to radians

def rotate(points, centre, angle_rad):
    """Rotate a set of 2-D points around *centre* by *angle_rad*."""
    c, s = np.cos(angle_rad), np.sin(angle_rad)
    R = np.array([[c, -s],
                  [s,  c]])
    return (R @ (points - centre).T).T + centre

def update(frame):
    t = frame
    pts = base_positions.copy()

    # ------------------- BREATHING (vertical lift) ------------------------- #
    breath = BREATH_AMPLITUDE * np.sin(omega_breath * t)
    pts[BREATH_POINTS, 1] += breath

    # ------------------- ARM WIGGLE (tiny rotation) ------------------------ #
    # rotate upper-arm chain (points 4 & 6) around the shoulder (point 2)
    phase = np.sin(omega_breath * t)       # phase-lock with breathing
    angle = arm_wiggle * phase
    pts[ARM_UPPER] = rotate(pts[ARM_UPPER], centre=pts[2], angle_rad=angle)

    # Push data to the scatter object
    scat.set_offsets(pts)
    return scat,

ani = FuncAnimation(fig,
                    update,
                    frames=total_frames,
                    interval=1000 / FPS,
                    blit=True)

plt.show()
