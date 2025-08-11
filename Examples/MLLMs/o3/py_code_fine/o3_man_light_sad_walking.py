
"""
Point-light biological motion stimulus
15 white dots depicting a lightweight sadman walking
The resulting animation is saved as “point_light_walking.gif”.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")               # head-less (non-interactive) backend
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


# ------------------------------------------------------------
# Biomechanical skeleton description (all lengths in arbitrary
# but self-consistent units)
# ------------------------------------------------------------
L_TORSO      = 3.0     # pelvis -> shoulders
L_NECK       = 1.0     # shoulders -> top of head
L_UPPER_ARM  = 1.2
L_LOWER_ARM  = 1.2
L_THIGH      = 1.5
L_SHANK      = 1.5

HIP_OFFSET_X      = 0.25   # half pelvis width
SHOULDER_OFFSET_X = 0.35   # half shoulder width


def rot_vec(angle, length):
    """
    Helper that returns a 2-D vector of given length rotated by angle
    (angle 0 points straight down along –y; positive angles rotate the
    limb forward, negative backward – convenient for sagittal view).
    """
    return np.array([length * np.sin(angle),
                     -length * np.cos(angle)])


def compute_frame(phase):
    """
    Computes 2-D coordinates for all 15 markers for a single animation
    frame. `phase` ∊ [0, 2π) is the gait phase.
    Returns a (15, 2) array: [x, y] for every marker.
    Marker order (Johansson style):
        0  head
        1  mid-shoulder / neck base
        2  pelvis (mid-hip)
        3  r-shoulder   4  l-shoulder
        5  r-elbow      6  l-elbow
        7  r-wrist      8  l-wrist
        9  r-hip        10 l-hip
        11 r-knee       12 l-knee
        13 r-ankle      14 l-ankle
    """
    # ----------------------------
    # Global body motion (small bob)
    # ----------------------------
    bob = 0.12 * np.sin(2 * phase)
    pelvis = np.array([0.0, bob])        # origin of kinematic chain

    # ----------------------------
    # Torso & head
    # ----------------------------
    shoulder_mid = pelvis + np.array([0.0, L_TORSO])
    head = shoulder_mid + np.array([0.0, L_NECK])

    # ----------------------------
    # LEG PARAMETERS (sagittal)
    # ----------------------------
    hip_amp    = np.deg2rad(25)          # hip swing amplitude
    knee_amp   = np.deg2rad(35)          # knee flex amplitude

    hip_angle_r =  hip_amp * np.sin(phase)         # right hip
    hip_angle_l = -hip_angle_r                      # left hip 180° out of phase

    # Knee flex peaks when leg is swung forward
    knee_angle_r = knee_amp * (1 + np.sin(phase - np.pi / 2)) * 0.5
    knee_angle_l = knee_amp * (1 + np.sin(phase + np.pi / 2)) * 0.5

    hip_r = pelvis + np.array([ HIP_OFFSET_X, 0.0])
    hip_l = pelvis + np.array([-HIP_OFFSET_X, 0.0])

    knee_r  = hip_r + rot_vec(hip_angle_r, L_THIGH)
    ankle_r = knee_r + rot_vec(hip_angle_r + knee_angle_r, L_SHANK)

    knee_l  = hip_l + rot_vec(hip_angle_l, L_THIGH)
    ankle_l = knee_l + rot_vec(hip_angle_l + knee_angle_l, L_SHANK)

    # ----------------------------
    # ARM PARAMETERS (opposite phase to legs)
    # ----------------------------
    arm_amp  = np.deg2rad(30)
    elbow_set_angle = np.deg2rad(15)     # keep slight elbow flex

    shoulder_r = shoulder_mid + np.array([ SHOULDER_OFFSET_X, 0.0])
    shoulder_l = shoulder_mid + np.array([-SHOULDER_OFFSET_X, 0.0])

    shoulder_angle_r = -arm_amp * np.sin(phase)    # arms opposite to legs
    shoulder_angle_l =  arm_amp * np.sin(phase)

    elbow_r  = shoulder_r + rot_vec(shoulder_angle_r, L_UPPER_ARM)
    wrist_r  = elbow_r    + rot_vec(shoulder_angle_r + elbow_set_angle,
                                    L_LOWER_ARM)

    elbow_l  = shoulder_l + rot_vec(shoulder_angle_l, L_UPPER_ARM)
    wrist_l  = elbow_l    + rot_vec(shoulder_angle_l + elbow_set_angle,
                                    L_LOWER_ARM)

    # ----------------------------
    # Assemble 15 locations
    # ----------------------------
    pts = np.vstack([head,
                     shoulder_mid,
                     pelvis,
                     shoulder_r, shoulder_l,
                     elbow_r,    elbow_l,
                     wrist_r,    wrist_l,
                     hip_r,      hip_l,
                     knee_r,     knee_l,
                     ankle_r,    ankle_l])
    return pts


# ------------------------------------------------------------
# Build and save animation
# ------------------------------------------------------------
FPS      = 30
N_FRAMES = 150                     # ≈ 5 seconds at 30 fps

fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_aspect("equal")
ax.axis("off")

# Reasonable axis limits so walker stays centred
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 6)

# Scatter plot for 15 points
scat = ax.scatter([], [], s=60, c="white")

def init():
    scat.set_offsets(np.zeros((15, 2)))
    return scat,

def update(frame_idx):
    phase = 2 * np.pi * frame_idx / N_FRAMES
    pts = compute_frame(phase)
    scat.set_offsets(pts)
    return scat,

ani = FuncAnimation(fig,
                    update,
                    frames=N_FRAMES,
                    init_func=init,
                    interval=1000 / FPS,
                    blit=True)

# Save as GIF (Pillow backend is always available with matplotlib)
ani.save("point_light_walking.gif",
         writer=PillowWriter(fps=FPS))

# The script finishes silently; the GIF is written to disk.
