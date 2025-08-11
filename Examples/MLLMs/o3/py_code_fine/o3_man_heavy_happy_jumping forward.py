
"""
Point-Light Biological Motion Stimulus
======================================

This script shows a 15-dot point-light animation of a (rather heavy) happy man
jumping forward.  The dots correspond to the major joints of the body and move
in a biomechanically plausible, smooth fashion.  The background is solid black
and every dot is rendered in white, faithfully reproducing the classical
point-light biological-motion style.

Joints (15):
    0  head            8  hip centre
    1  neck            9  left-hip      10 right-hip
    2  left-shoulder   11 left-knee     12 right-knee
    3  right-shoulder  13 left-ankle    14 right-ankle
    4  left-elbow
    5  right-elbow
    6  left-wrist
    7  right-wrist
"""

import math
import numpy as np
import matplotlib
matplotlib.use("Agg")  # use non-interactive backend in headless environments
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------------------- kinematics ------------------------------- #

# Skeleton segment lengths (arbitrary units)
TORSO        = 0.40     # neck  -> hip-centre
HEAD         = 0.25     # neck  -> head
SHOULDER_OFF = 0.15     # neck  -> (left/right) shoulder offset (x)
UPPER_ARM    = 0.30     # shoulder -> elbow
LOWER_ARM    = 0.30     # elbow    -> wrist
UPPER_LEG    = 0.50     # hip -> knee
LOWER_LEG    = 0.50     # knee -> ankle

# Motion parameters
TOTAL_FRAMES      = 240             # frames per full jump cycle
FORWARD_DISTANCE  = 2.0             # metres travelled during one jump
SQUAT_DEPTH       = 0.30            # hip drops before take-off
JUMP_HEIGHT       = 0.60            # maximum vertical displacement
ARM_SWING_AMPL    = 0.60            # radians
KNEE_BEND_MIN     = math.radians(20)   # almost straight during flight
KNEE_BEND_MAX     = math.radians(80)   # deep bend while squatting

def pelvis_trajectory(phi: float):
    """
    Compute pelvis (hip-centre) x/y for a phase value 0..1.

    phi ∈ [0, 1] : 0   - beginning of squat
                   0.25- deepest squat
                   0.65- end of flight (just before landing)
                   1   - upright again
    """
    base_x, base_y = 0.0, 1.0   # neutral standing position

    # horizontal (forward) translation
    x = base_x + FORWARD_DISTANCE * phi

    # vertical trajectory
    if phi < 0.25:                       # squatting down
        y = base_y - SQUAT_DEPTH * (phi / 0.25)
    elif phi < 0.65:                     # take off + flight (parabolic)
        a = (phi - 0.25) / 0.40          # 0..1
        y = base_y + JUMP_HEIGHT * math.sin(math.pi * a)
    else:                                # landing / recovering
        b = (phi - 0.65) / 0.35          # 0..1
        y = base_y - SQUAT_DEPTH * (1 - b)
    return x, y

def knee_bend(phi: float):
    """
    Amount of knee bend (inner knee angle, radians) based on current phase.
    0 .. standing straight
    1 .. deepest squat
    """
    if phi < 0.25:                       # bending down
        s = phi / 0.25
    elif phi < 0.65:                     # in the air (mostly straight)
        s = 0.0
    else:                                # bending again for landing
        s = (1.0 - phi) / 0.35
    return KNEE_BEND_MIN + (KNEE_BEND_MAX - KNEE_BEND_MIN) * s

def compute_pose(phi: float):
    """
    Return 15×2 array with (x, y) for every joint at phase φ (0..1).
    """
    # hip centre coordinates
    hx, hy = pelvis_trajectory(phi)

    # ---------------- torso & head ---------------- #
    neck   = np.array([hx, hy + TORSO])
    head   = np.array([neck[0]      , neck[1] + HEAD])

    # ---------------- shoulders ------------------- #
    l_sh   = neck + np.array([-SHOULDER_OFF, 0.0])
    r_sh   = neck + np.array([ SH0ULDER_OFF, 0.0])

    # ---------------- arms ------------------------ #
    # Shoulder rotation (forward/back) sinusoidal
    arm_base_angle = math.pi / 2     # straight up
    l_sh_angle = arm_base_angle - 0.3 + ARM_SWING_AMPL * math.sin(2*math.pi*phi)
    r_sh_angle = arm_base_angle + 0.3 + ARM_SWING_AMPL * math.sin(2*math.pi*phi + math.pi)

    # Elbow constant bend (slightly bent)
    ELBOW_BEND = math.radians(45)

    # Left arm
    l_el = l_sh + UPPER_ARM * np.array([math.cos(l_sh_angle),
                                        math.sin(l_sh_angle)])
    l_wr_angle = l_sh_angle - (math.pi - ELBOW_BEND)
    l_wr = l_el + LOWER_ARM * np.array([math.cos(l_wr_angle),
                                        math.sin(l_wr_angle)])

    # Right arm
    r_el = r_sh + UPPER_ARM * np.array([math.cos(r_sh_angle),
                                        math.sin(r_sh_angle)])
    r_wr_angle = r_sh_angle - (math.pi - ELBOW_BEND)
    r_wr = r_el + LOWER_ARM * np.array([math.cos(r_wr_angle),
                                        math.sin(r_wr_angle)])

    # ---------------- hips & legs ----------------- #
    l_hip = np.array([hx - 0.10, hy])
    r_hip = np.array([hx + 0.10, hy])

    knee_angle = knee_bend(phi)          # inner knee angle

    # Leg swing angle (slight alternating)
    leg_swing = 0.20 * math.sin(2*math.pi*phi)

    l_thigh_dir = -math.pi/2 + leg_swing
    r_thigh_dir = -math.pi/2 - leg_swing

    # Knee positions
    l_kn = l_hip + UPPER_LEG * np.array([math.cos(l_thigh_dir),
                                         math.sin(l_thigh_dir)])
    r_kn = r_hip + UPPER_LEG * np.array([math.cos(r_thigh_dir),
                                         math.sin(r_thigh_dir)])

    # Shank directions
    l_shank_dir = l_thigh_dir - (math.pi - knee_angle)
    r_shank_dir = r_thigh_dir - (math.pi - knee_angle)

    # Ankle positions
    l_an = l_kn + LOWER_LEG * np.array([math.cos(l_shank_dir),
                                        math.sin(l_shank_dir)])
    r_an = r_kn + LOWER_LEG * np.array([math.cos(r_shank_dir),
                                        math.sin(r_shank_dir)])

    # ---------------- assemble -------------------- #
    joints = np.vstack([
        head,                # 0
        neck,                # 1
        l_sh,                # 2
        r_sh,                # 3
        l_el,                # 4
        r_el,                # 5
        l_wr,                # 6
        r_wr,                # 7
        np.array([hx, hy]),  # 8 hip centre
        l_hip,               # 9
        r_hip,               # 10
        l_kn,                # 11
        r_kn,                # 12
        l_an,                # 13
        r_an                 # 14
    ])
    return joints

# ----------------------------- visualisation ----------------------------- #

fig = plt.figure(figsize=(4, 6), facecolor='black')
ax  = fig.add_subplot(111)
ax.set_facecolor('black')
ax.set_xlim(-1.0, FORWARD_DISTANCE + 1.0)
ax.set_ylim(-0.25, 2.2)
ax.set_aspect('equal')
ax.axis('off')

# initial scatter
pts = ax.scatter([], [], s=50, c='white')

def init():
    pts.set_offsets(np.zeros((15, 2)))
    return (pts,)

def update(frame):
    phi = (frame % TOTAL_FRAMES) / TOTAL_FRAMES
    joints = compute_pose(phi)
    pts.set_offsets(joints)
    return (pts,)

ani = FuncAnimation(
    fig, update,
    frames=TOTAL_FRAMES,
    init_func=init,
    interval=1000/60,   # ~60 Hz
    blit=True
)

# Show the animation (commented out for automated test environments)
# plt.show()

# If run as a script, save a short gif for quick inspection
if __name__ == "__main__":
    try:
        ani.save("jumping_forward_biological_motion.gif",
                 writer="pillow", fps=30, dpi=100)
        print("Animation saved as 'jumping_forward_biological_motion.gif'")
    except Exception as e:
        # fallback: just display interactively if saving fails
        plt.show()
