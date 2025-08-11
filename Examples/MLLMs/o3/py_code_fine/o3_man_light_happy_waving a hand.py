
"""
Point–light biological–motion stimulus:
15 white dots (on a black background) depicting a lightweight human
figure happily waving the right hand.  The animation is biomechanically
plausible and smoothly looped.

Simply run the script – a matplotlib window will open and play the
animation until it is closed.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------
def rotvec(angle_rad):
    """Return a 2-D unit vector rotated counter-clockwise by *angle_rad*."""
    return np.array([np.cos(angle_rad), np.sin(angle_rad)])


# ---------------------------------------------------------------------
# Static reference – body geometry in ‘model units’
# ---------------------------------------------------------------------
# Basic segment lengths (roughly Johansson’s values, scaled to ~1.8 units)
L_HEAD      = 0.30       # head (neck→top)
L_TORSO     = 0.50       # neck→hip-centre
L_SHOULDER  = 0.20       # shoulder offset from neck (left / right)
L_UPPERARM  = 0.30       # shoulder→elbow
L_FOREARM   = 0.30       # elbow→wrist
L_HAND      = 0.08       # (wrist→hand) – little stub, not animated
L_HIP       = 0.15       # hip offset from centre (left / right)
L_THIGH     = 0.50       # hip→knee
L_SHANK     = 0.50       # knee→ankle

# Anchor (hip-centre) is origin; +y = up, +x = figure’s right
HIP_CENTRE = np.array([0.0, 0.0])

# Static (left-side) limb positions -----------------------------------
NECK   = HIP_CENTRE + np.array([0, L_TORSO])
HEAD   = NECK       + np.array([0, L_HEAD])

LEFT_SHOULDER = NECK + np.array([-L_SHOULDER, 0])
RIGHT_SHOULDER_BASE = NECK + np.array([+L_SHOULDER, 0])      # dynamic

# Left arm (static, casually down)
theta_ls = np.deg2rad(220)                                   # angle w.r.t. +x
LEFT_ELBOW = LEFT_SHOULDER + L_UPPERARM * rotvec(theta_ls)
theta_lf  = theta_ls - np.deg2rad(20)
LEFT_WRIST = LEFT_ELBOW + L_FOREARM * rotvec(theta_lf)

# Static left hand (small offset)
LEFT_HAND  = LEFT_WRIST + L_HAND * rotvec(theta_lf)

# Left leg (static)
LEFT_HIP   = HIP_CENTRE + np.array([-L_HIP, 0])
LEFT_KNEE  = LEFT_HIP + np.array([0, -L_THIGH])
LEFT_ANKLE = LEFT_KNEE + np.array([0, -L_SHANK])

# Right leg (static)
RIGHT_HIP   = HIP_CENTRE + np.array([+L_HIP, 0])
RIGHT_KNEE  = RIGHT_HIP + np.array([0, -L_THIGH])
RIGHT_ANKLE = RIGHT_KNEE + np.array([0, -L_SHANK])

# ---------------------------------------------------------------------
# Animation parameters
# ---------------------------------------------------------------------
FPS            = 60                    # frames per second
CYCLE_SECONDS  = 2.0                   # duration of one complete hand wave
TOTAL_FRAMES   = int(FPS * CYCLE_SECONDS)

# Wave motion ranges (degrees)
SHOULDER_MIN   = 300                   # 300° ≈  -60° (pointing down/right)
SHOULDER_MAX   =  70                   # 70°   ≈  up
ELBOW_MIN      =  60                   # elbow fairly bent
ELBOW_MAX      = 160                   # almost straight

# Slight happy body bounce
BOUNCE_AMPLITUDE = 0.04                # up/down (model units)


# ---------------------------------------------------------------------
# Matplotlib figure
# ---------------------------------------------------------------------
plt.style.use("dark_background")
fig = plt.figure(figsize=(3.5, 6), facecolor='black')
ax  = fig.add_subplot(111, facecolor='black')
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.25, 2.0)
ax.axis('off')

scatter = ax.scatter([], [], s=40, c='white')


# ---------------------------------------------------------------------
# Frame calculation
# ---------------------------------------------------------------------
def compute_frame(t):
    """
    Return the (x, y) coordinates of the 15 point-lights at time *t*
    (0 … 1, where 1 = one full wave cycle).
    """
    # Smooth sinusoidal shoulder angle between limits
    shoulder_deg = SHOULDER_MIN + 0.5 * (1 - np.cos(2 * np.pi * t)) * (SHOULDER_MAX - SHOULDER_MIN)
    shoulder_rad = np.deg2rad(shoulder_deg)

    # Elbow angle oscillates twice as fast, adding a real waving feel
    elbow_phase  = (t * 2) % 1.0
    elbow_deg    = ELBOW_MIN + 0.5 * (1 - np.cos(2 * np.pi * elbow_phase)) * (ELBOW_MAX - ELBOW_MIN)
    elbow_rad    = np.deg2rad(elbow_deg)

    # Shoulder joint (right) – add a tiny lateral sway
    sway = 0.02 * np.sin(2 * np.pi * t)
    right_shoulder = RIGHT_SHOULDER_BASE + np.array([sway, 0])

    # Upper arm
    right_elbow = right_shoulder + L_UPPERARM * rotvec(shoulder_rad)

    # Compute forearm angle (keep internal elbow angle = elbow_rad)
    forearm_angle = shoulder_rad + (np.pi - elbow_rad)
    right_wrist = right_elbow + L_FOREARM * rotvec(forearm_angle)
    right_hand  = right_wrist + L_HAND   * rotvec(forearm_angle)

    # Vertical body bounce
    bounce = BOUNCE_AMPLITUDE * np.sin(2 * np.pi * t)
    bounce_vec = np.array([0, bounce])

    # Assemble 15 joint positions (order matters, exactly 15)
    points = np.vstack([
        HEAD          + bounce_vec,     # 0 head
        NECK          + bounce_vec,     # 1 neck
        right_shoulder+ bounce_vec,     # 2 right shoulder
        right_elbow   + bounce_vec,     # 3 right elbow
        right_wrist   + bounce_vec,     # 4 right wrist
        LEFT_SHOULDER + bounce_vec,     # 5 left shoulder
        LEFT_ELBOW    + bounce_vec,     # 6 left elbow
        LEFT_WRIST    + bounce_vec,     # 7 left wrist
        HIP_CENTRE    + bounce_vec,     # 8 hip centre
        RIGHT_HIP     + bounce_vec,     # 9 right hip
        RIGHT_KNEE    + bounce_vec,     # 10 right knee
        RIGHT_ANKLE   + bounce_vec,     # 11 right ankle
        LEFT_HIP      + bounce_vec,     # 12 left hip
        LEFT_KNEE     + bounce_vec,     # 13 left knee
        LEFT_ANKLE    + bounce_vec      # 14 left ankle
    ])
    return points.T  # shape (2, 15)


# ---------------------------------------------------------------------
# Animation function
# ---------------------------------------------------------------------
def update(frame_idx):
    t = (frame_idx % TOTAL_FRAMES) / TOTAL_FRAMES  # 0 … 1
    xy = compute_frame(t)
    scatter.set_offsets(xy.T)
    return scatter,

anim = FuncAnimation(fig,
                     update,
                     frames=TOTAL_FRAMES,
                     interval=1000/FPS,
                     blit=True)

# ---------------------------------------------------------------------
# Go!
# ---------------------------------------------------------------------
if __name__ == "__main__":
    plt.show()
