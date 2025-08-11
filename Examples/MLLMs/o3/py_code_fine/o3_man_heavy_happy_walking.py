
"""
Point–light biological–motion stimulus: a man performing a smooth forward roll
(‘somersault’) shown with 15 white point–lights on a black background.

The script uses matplotlib’s animation module.  Close the window to stop.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------------------------------------------------------------
# 1.  Fifteen anatomical landmarks (in BODY-CENTRIC coordinates)
#     We work in the sagittal plane (2-D).  Units are metres.
# ---------------------------------------------------------------------
# Naming legend (index : landmark)
#  0  head          1  neck
#  2  shoulder L    3  shoulder R
#  4  elbow L       5  elbow R
#  6  wrist L       7  wrist R
#  8  hip L         9  hip R
# 10  knee L       11  knee R
# 12  ankle L      13  ankle R
# 14  spine / pelvis centre (used as body origin)

# Rough proportions for an adult male in a tuck-position (so he can roll)
# All coordinates are given relative to the pelvis centre (0, 0)
#                                   x (forward),   y (up)
body_points = np.array([
    [ 0.00,  0.64],     # 0  head (approximated – tucked)
    [ 0.00,  0.54],     # 1  neck
    [-0.14,  0.50],     # 2  shoulder L
    [ 0.14,  0.50],     # 3  shoulder R
    [-0.18,  0.30],     # 4  elbow L
    [ 0.18,  0.30],     # 5  elbow R
    [-0.16,  0.10],     # 6  wrist L
    [ 0.16,  0.10],     # 7  wrist R
    [-0.10,  0.00],     # 8  hip L
    [ 0.10,  0.00],     # 9  hip R
    [-0.12, -0.30],     # 10 knee L
    [ 0.12, -0.30],     # 11 knee R
    [-0.10, -0.60],     # 12 ankle L
    [ 0.10, -0.60],     # 13 ankle R
    [ 0.00,  0.00]      # 14 pelvis / root
])

NUM_POINTS = body_points.shape[0]
assert NUM_POINTS == 15, "We need exactly 15 point lights."


# ---------------------------------------------------------------------
# 2.  Roll kinematics
#     We approximate the body as a rigid cluster of points that rotates
#     around its geometric centre while the centre travels along the
#     ground such that the man ‘rolls’ without slipping (pure rolling
#     condition).  This is a good visual approximation of a forward roll.
# ---------------------------------------------------------------------
RADIUS = 0.65            # effective ‘wheel’ radius (metres)
ROLL_CIRCUM = 2 * np.pi * RADIUS

DURATION   = 3.5          # seconds for one full forward roll
FPS        = 60           # animation frame-rate
N_FRAMES   = int(DURATION * FPS)

# Precompute centres’ trajectory: x = R * θ, y = R (centre height)
theta_all = np.linspace(0, 2 * np.pi, N_FRAMES, endpoint=False)
x_center  = RADIUS * theta_all                    # no slip
y_center  = np.full_like(theta_all, RADIUS)       # stays one radius above ground


# ---------------------------------------------------------------------
# 3.  Matplotlib figure set-up
# ---------------------------------------------------------------------
plt.style.use('dark_background')                  # black background
fig, ax = plt.subplots(figsize=(4, 4))
ax.set_aspect('equal')
ax.axis('off')

# Set fixed limits so the figure doesn’t jump
ax.set_xlim(-0.5, x_center[-1] + 1.0)
ax.set_ylim(-0.8, 1.4)

# Scatter plot for the 15 points
scat = ax.scatter([], [], s=40, c='white')

# Optional ground line for visual reference
ax.plot([ -1, x_center[-1] + 1.5], [0, 0], lw=1, color='gray', alpha=0.3)


# ---------------------------------------------------------------------
# 4.  Animation update function
# ---------------------------------------------------------------------
def update(frame):
    theta = theta_all[frame]

    # Rotation matrix for current body orientation (positive forward roll)
    c, s = np.cos(-theta), np.sin(-theta)   # negative to roll forward
    R = np.array([[c, -s],
                  [s,  c]])

    # Apply rotation
    rotated = body_points @ R.T

    # Translation – place rotated body at the rolling centre
    translated = rotated + np.array([x_center[frame], y_center[frame]])

    scat.set_offsets(translated)
    return scat,


# ---------------------------------------------------------------------
# 5.  Run animation
# ---------------------------------------------------------------------
ani = FuncAnimation(
        fig, update, frames=N_FRAMES,
        interval=1000 / FPS, blit=True)

plt.show()
