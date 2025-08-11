
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
Biological-motion point-light stimulus
Subject : happy, heavy-set woman
Action  : waving right hand
Points  : exactly 15 white dots on a black background
Author  : demo – you may adapt freely
"""

# ---------------------------------------------------------------------
# Utility – compute simple forward kinematics for the right arm
# ---------------------------------------------------------------------
def right_arm_positions(shoulder, t):
    """
    Computes elbow and hand coordinates for the waving right arm.
    A very small two–link planar model is used.

    Parameters
    ----------
    shoulder : ndarray shape (2,)
        XY location of the shoulder joint.
    t : float
        Time in seconds (continuous).

    Returns
    -------
    elbow : ndarray shape (2,)
    hand  : ndarray shape (2,)
    """
    # Link lengths (upper-arm, fore-arm)
    L1 = 2.0
    L2 = 1.6

    # Upper-arm angle (degrees) – swings smoothly while arm stays raised
    # 110° means pointing slightly up–left; variation ±40° provides waving arc
    phi = np.deg2rad(110 + 40 * np.sin(2 * np.pi * 1.2 * t))

    # Elbow position
    elbow = shoulder + L1 * np.array([np.cos(phi), np.sin(phi)])

    # Fore-arm extra rotation about the elbow to imitate the actual “wave”
    psi = np.deg2rad(-20 + 60 * np.sin(2 * np.pi * 2.4 * t + np.pi/3))

    # Hand position
    hand = elbow + L2 * np.array([np.cos(phi + psi), np.sin(phi + psi)])

    return elbow, hand


# ---------------------------------------------------------------------
# Static (mean) joint layout for a standing heavy-set woman
# Coordinate system : X (right), Y (up)
# All units are arbitrary but consistent
# ---------------------------------------------------------------------
def template_skeleton():
    """Returns a dictionary of joint → (x, y)."""
    return {
        "head"          : np.array([0.0,  9.0]),
        "neck"          : np.array([0.0,  7.5]),

        "L_shoulder"    : np.array([-2.0, 7.0]),
        "R_shoulder"    : np.array([ 2.0, 7.0]),

        "L_elbow"       : np.array([-2.4, 5.5]),
        "R_elbow"       : None,                 # filled each frame

        "L_hand"        : np.array([-2.4, 4.0]),
        "R_hand"        : None,                 # filled each frame

        "spine"         : np.array([0.0, 6.0]),

        "L_hip"         : np.array([-1.6, 4.0]),
        "R_hip"         : np.array([ 1.6, 4.0]),

        "L_knee"        : np.array([-1.6, 2.0]),
        "R_knee"        : np.array([ 1.6, 2.0]),

        "L_ankle"       : np.array([-1.6, 0.0]),
        "R_ankle"       : np.array([ 1.6, 0.0]),
    }


# Ordered list (exactly 15 joints)
JOINT_ORDER = [
    "head", "neck",
    "L_shoulder", "R_shoulder",
    "L_elbow", "R_elbow",
    "L_hand",  "R_hand",
    "spine",
    "L_hip", "R_hip",
    "L_knee", "R_knee",
    "L_ankle", "R_ankle",
]


# ---------------------------------------------------------------------
# Matplotlib figure setup
# ---------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-6, 6)
ax.set_ylim(-1, 11)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter for the 15 white dots
points = ax.scatter(
    np.zeros(15),
    np.zeros(15),
    s=60,             # marker size (a bit larger for “heavy-set”)
    color='white'
)


# ---------------------------------------------------------------------
# Animation update
# ---------------------------------------------------------------------
FPS = 30
def update(frame):
    t = frame / FPS

    # Base skeleton (copy to avoid in-place modification)
    skel = {k: v.copy() if v is not None else None
            for k, v in template_skeleton().items()}

    # Natural happy “bounce” of the whole body (vertical bobbing)
    bob = 0.12 * np.sin(2 * np.pi * 1.2 * t)
    for k, v in skel.items():
        if v is not None:
            skel[k][1] += bob

    # Compute waving right arm
    shoulder = skel["R_shoulder"]
    elbow, hand = right_arm_positions(shoulder, t)
    skel["R_elbow"] = elbow
    skel["R_hand"]  = hand

    # Concatenate positions in the prescribed order
    XY = np.array([skel[j] for j in JOINT_ORDER])

    # Update scatter plot
    points.set_offsets(XY)
    return points,


# ---------------------------------------------------------------------
# Run the animation
# ---------------------------------------------------------------------
anim = FuncAnimation(
    fig, update, interval=1000/FPS, blit=True
)

plt.show()
