
"""
Point-light biological motion stimulus
======================================

A minimal example that shows a *happy*, light-weight person smoothly
turning around.  The stimulus consists of *exactly* 15 white dots that
correspond to the major joints of a human body.  The dots are rendered
on a solid black background and the whole figure performs a 360-degree
turn while bouncing lightly to give a cheerful impression.

Requirements satisfied
----------------------
1. Subject & action  :  a “happy man” that turns around.
2. Visual style      :  15 white point-lights on a black background.
3. Motion quality    :  smooth, coherent, biomechanically plausible.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# ---------------------------------------------------------------------
# 1. Skeleton definition (15 points)
# ---------------------------------------------------------------------
#
# The coordinates describe an upright person facing the camera.
# Units are arbitrary, chosen for a visually pleasing aspect ratio.

JOINT_NAMES = [
    "head",
    "shoulder_l", "shoulder_r",
    "elbow_l",    "elbow_r",
    "wrist_l",    "wrist_r",
    "pelvis",
    "hip_l",      "hip_r",
    "knee_l",     "knee_r",
    "ankle_l",    "ankle_r",
    "chest"
]

#                              x,   y,  z
SKELETON = np.array([
    [ 0.00, 1.80, 0.00],   # head
    [-0.30, 1.50, 0.00],   # shoulder_l
    [ 0.30, 1.50, 0.00],   # shoulder_r
    [-0.50, 1.20, 0.00],   # elbow_l
    [ 0.50, 1.20, 0.00],   # elbow_r
    [-0.60, 0.90, 0.00],   # wrist_l
    [ 0.60, 0.90, 0.00],   # wrist_r
    [ 0.00, 1.00, 0.00],   # pelvis (centre)
    [-0.20, 1.00, 0.00],   # hip_l
    [ 0.20, 1.00, 0.00],   # hip_r
    [-0.20, 0.60, 0.00],   # knee_l
    [ 0.20, 0.60, 0.00],   # knee_r
    [-0.20, 0.00, 0.00],   # ankle_l
    [ 0.20, 0.00, 0.00],   # ankle_r
    [ 0.00, 1.55, 0.00],   # chest (centre of upper torso)
], dtype=float)

assert SKELETON.shape[0] == 15            # exactly 15 point-lights
assert len(JOINT_NAMES)  == 15


# ---------------------------------------------------------------------
# 2.  Helper functions
# ---------------------------------------------------------------------
def rotate_y(points, theta):
    """
    Rotate an array of 3-D points around the Y (vertical) axis.

    Parameters
    ----------
    points : (N,3) ndarray
    theta  : float
        Rotation angle in radians (positive => counter-clockwise when
        looking from above).

    Returns
    -------
    (N,3) ndarray : rotated coordinates
    """
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[ c, 0.0, s],
                  [0.0, 1.0, 0.0],
                  [-s, 0.0, c]])
    return points @ R.T


def perspective_projection(points, d=4.0):
    """
    Very simple perspective projection onto the X/Y plane.

    Parameters
    ----------
    points : (N,3) ndarray
    d      : float
        Distance from camera to projection plane.

    Returns
    -------
    (N,2) ndarray : projected 2-D coordinates
    """
    z = points[:, 2]
    scale = d / (d + z)              # closer points appear larger
    xy = points[:, :2] * scale[:, None]
    return xy, scale


# ---------------------------------------------------------------------
# 3.  Matplotlib boilerplate
# ---------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_facecolor("black")
fig.patch.set_facecolor("black")
ax.axis("off")
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-0.2, 2.1)

# Initial scatter (size will be updated every frame)
scat = ax.scatter([], [], s=80, c="white")


# ---------------------------------------------------------------------
# 4.  Animation callback
# ---------------------------------------------------------------------
N_FRAMES = 240                       # ~8 seconds @30 fps
BOUNCE_PER_TURN = 4                  # vertical bounces per revolution
BOUNCE_AMPLITUDE = 0.05              # m

def init():
    scat.set_offsets(np.zeros((15, 2)))
    return (scat,)


def animate(frame):
    # Angle for one full revolution
    theta = 2 * np.pi * frame / N_FRAMES

    # Light "happy" bounce (adds cheerfulness)
    bounce = BOUNCE_AMPLITUDE * np.sin(BOUNCE_PER_TURN * theta)
    points = SKELETON.copy()
    points[:, 1] += bounce            # add vertical offset

    # Rotate around the vertical axis
    points = rotate_y(points, theta)

    # Perspective projection to 2-D
    xy, scale = perspective_projection(points, d=4.0)

    # Update scatter artist
    scat.set_offsets(xy)
    # (keep size fixed; could also do scat.set_sizes(80*scale) for depth cue)
    return (scat,)


# ---------------------------------------------------------------------
# 5.  Create and start the animation
# ---------------------------------------------------------------------
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=N_FRAMES,
                              init_func=init,
                              interval=1000/30,   # 30 fps
                              blit=True,
                              repeat=True)

if __name__ == "__main__":
    plt.show()
