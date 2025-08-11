
"""
Point-light biological–motion stimulus
======================================

A simple demonstration of a 15-dot point–light figure that starts in an
upright posture and – burdened by an imaginary heavy weight – slowly
“collapses” into a lying posture.  The dots are rendered as white points
on a solid black background (à la classic Johansson biological–motion
stimuli).

The script uses matplotlib’s animation framework.  Run it and a window
will pop up that shows the animation in real time.

Author:  OpenAI (ChatGPT)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# ----------------------------------------------------------------------
# 1.  Build a canonical 2-D skeleton (15 landmarks)
# ----------------------------------------------------------------------
#
# Index / Body part
#   0  head
#   1  neck
#   2  left shoulder
#   3  right shoulder
#   4  left elbow
#   5  right elbow
#   6  left wrist
#   7  right wrist
#   8  hip centre
#   9  left hip
#   10 right hip
#   11 left knee
#   12 right knee
#   13 left ankle
#   14 right ankle
#
# All coordinates are given in an upright pose.  Units are arbitrary
# (roughly “head lengths”); the origin is at the hip centre.

skeleton_upright = np.array([
    [0.0, 8.0],     # head
    [0.0, 7.0],     # neck
    [-1.0, 7.0],    # L shoulder
    [1.0, 7.0],     # R shoulder
    [-1.5, 5.5],    # L elbow
    [1.5, 5.5],     # R elbow
    [-1.5, 4.0],    # L wrist
    [1.5, 4.0],     # R wrist
    [0.0, 4.0],     # hip centre
    [-1.0, 4.0],    # L hip
    [1.0, 4.0],     # R hip
    [-1.0, 2.0],    # L knee
    [1.0, 2.0],     # R knee
    [-1.0, 0.0],    # L ankle
    [1.0, 0.0],     # R ankle
], dtype=float)

assert skeleton_upright.shape == (15, 2), "Must have exactly 15 points!"

# ----------------------------------------------------------------------
# 2.  Animation parameters
# ----------------------------------------------------------------------
n_frames      = 120           # total number of frames
fps           = 30            # frames per second (display only)
start_angle   = 0.0           # radians (upright)
end_angle     = -np.pi / 2.0  # –90° → lying on the ground
pivot         = skeleton_upright[8]  # rotate around hip centre

# Pre-compute angles for all frames with a smooth (sinusoidal) ease-in/out
t = np.linspace(0, 1, n_frames)
# ease using a raised-cosine profile (smoothstep)
ease = 0.5 * (1 - np.cos(np.pi * t))
angles = start_angle + (end_angle - start_angle) * ease

# ----------------------------------------------------------------------
# 3.  Matplotlib figure
# ----------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Set axis limits to comfortably accommodate both poses
margin = 1.5
xmin = skeleton_upright[:, 0].min() - margin
xmax = skeleton_upright[:, 0].max() + margin
ymin = skeleton_upright[:, 1].min() - margin
ymax = skeleton_upright[:, 1].max() + margin
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

# 15 white dots
dots = ax.scatter(skeleton_upright[:, 0],
                  skeleton_upright[:, 1],
                  s=50, c='white')

# ----------------------------------------------------------------------
# 4.  Animation callback
# ----------------------------------------------------------------------
def rotate(points, theta, origin):
    """Rotate points (N×2) by angle theta around origin (2-vector)."""
    rot = np.array([[ np.cos(theta), -np.sin(theta)],
                    [ np.sin(theta),  np.cos(theta)]])
    return origin + (points - origin) @ rot.T


def update(frame):
    """Update scatter points for given frame index."""
    theta = angles[frame]
    pts   = rotate(skeleton_upright, theta, pivot)
    dots.set_offsets(pts)
    return dots,


ani = FuncAnimation(fig, update, frames=n_frames,
                    interval=1000 / fps, blit=True, repeat=True)

plt.show()
