
"""
Biological-motion point-light display
15 white dots – “happy, light-weight woman running”
The animation is exported to  running_point_light.gif  in the working directory
and can be inspected with any image viewer afterwards.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")                  # head-less (no GUI) backend
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


# ------------------------------------------------------------------
# basic helpers
# ------------------------------------------------------------------
def rot(angle: float) -> np.ndarray:
    """
    2-D rotation matrix (counter-clockwise, mathematical positive
    but in our coordinate system +y is upward and we want 0° to point
    straight down, so later we use it accordingly)
    """
    s, c = np.sin(angle), np.cos(angle)
    return np.array([[c, -s],
                     [s,  c]])


# ------------------------------------------------------------------
# skeleton / anthropometric constants               (all in metres)
# ------------------------------------------------------------------
L_NECK       = 0.25
L_TORSO      = 0.60          # shoulder-to-hip
L_THIGH      = 0.50
L_SHANK      = 0.50
L_UPPERARM   = 0.35
L_FOREARM    = 0.35
SHOULDER_W   = 0.30
HIP_W        = 0.22

# names of the 15 landmarks (just for reference / documentation)
PT_NAMES = ['head',
            'sho_l', 'sho_r',
            'elb_l', 'elb_r',
            'wri_l', 'wri_r',
            'spine',
            'hip_l', 'hip_r',
            'kne_l', 'kne_r',
            'ank_l', 'ank_r',
            'pelvis_root' ]

N_PTS = 15


# ------------------------------------------------------------------
# gait parameters
# ------------------------------------------------------------------
FPS          = 30            # frames / second in the exported GIF
N_FRAMES     = 150           # → 5 seconds
STEP_FREQ    = 2.5           # strides / second  (pretty light/faster than walk)
OMEGA        = 2.0 * np.pi * STEP_FREQ / FPS   # rad / frame
HIP_AMP      = np.deg2rad(35.0)     # hip flex / ext amplitude
KNEE_AMP     = np.deg2rad(70.0)     # knee flex amplitude (running has lot of bending)
SHO_AMP      = np.deg2rad(25.0)     # shoulder swing
ELBOW_AMP    = np.deg2rad(60.0)     # elbow flex
VERT_BOUNCE  = 0.05                  # vertical COM oscillation  (metres)
# ------------------------------------------------------------------


def one_frame(k) -> np.ndarray:
    """returns  (15 , 2)  array of xy positions for frame index k"""
    t = k * OMEGA                                         # phase angle

    # ------------------------------------------------------------------
    # pelvic root (mid-point between hips)
    # ------------------------------------------------------------------
    root = np.array([0.0,
                     1.1 + VERT_BOUNCE * np.sin(2 * t)])  # vertical up/down bounce
    # (root.x stays 0 – we keep the figure centred on screen)

    # ------------------------------------------------------------------
    # shoulders & spine
    # ------------------------------------------------------------------
    spine = root + np.array([0.0, 0.5 * L_TORSO])
    shoulder_centre = root + np.array([0.0, L_TORSO])
    shoulder_left  = shoulder_centre + np.array([-SHOULDER_W / 2, 0.0])
    shoulder_right = shoulder_centre + np.array([+SHOULDER_W / 2, 0.0])

    head = shoulder_centre + np.array([0.0, L_NECK])

    # ------------------------------------------------------------------
    # hips (left / right)
    # ------------------------------------------------------------------
    hip_left  = root + np.array([-HIP_W / 2, 0.0])
    hip_right = root + np.array([+HIP_W / 2, 0.0])

    # ------------------------------------------------------------------
    # legs (forward kinematics)
    #   angles measured from **vertical downward** direction
    # ------------------------------------------------------------------
    pts = np.zeros((N_PTS, 2))

    for side, hip_pt, phase, idx_knee, idx_ank in (
            ('L', hip_left,   0.0,                PT_NAMES.index('kne_l'), PT_NAMES.index('ank_l')),
            ('R', hip_right,  np.pi,              PT_NAMES.index('kne_r'), PT_NAMES.index('ank_r'))
        ):

        hip_angle   = HIP_AMP  * np.sin(t + phase)                          # thigh w.r.t vertical
        knee_angle  = (KNEE_AMP * (1.0 + np.sin(t + phase))) / 2.0          # always ≥ 0

        thigh_vec   = rot(hip_angle) @ np.array([0.0, -L_THIGH])
        knee_pt     = hip_pt   + thigh_vec

        shank_vec   = rot(hip_angle + knee_angle) @ np.array([0.0, -L_SHANK])
        ankle_pt    = knee_pt + shank_vec

        pts[idx_knee] = knee_pt
        pts[idx_ank ] = ankle_pt

    # ------------------------------------------------------------------
    # arms
    # shoulders already known, now compute elbows & wrists
    #   opposite phase wrt legs for natural gait
    # ------------------------------------------------------------------
    for side, sho_pt, phase, idx_elb, idx_wri in (
            ('L', shoulder_left,  np.pi,              PT_NAMES.index('elb_l'), PT_NAMES.index('wri_l')),
            ('R', shoulder_right, 0.0,               PT_NAMES.index('elb_r'), PT_NAMES.index('wri_r'))
        ):

        sho_angle  = SHO_AMP   * np.sin(t + phase)                        # upper arm wrt vertical
        elb_angle  = (ELBOW_AMP * (1.0 + np.sin(t + phase + np.pi/2))) / 2.0

        upper_vec  = rot(sho_angle) @ np.array([0.0, -L_UPPERARM])
        elb_pt     = sho_pt + upper_vec

        fore_vec   = rot(sho_angle + elb_angle) @ np.array([0.0, -L_FOREARM])
        wri_pt     = elb_pt + fore_vec

        pts[idx_elb] = elb_pt
        pts[idx_wri] = wri_pt

    # ------------------------------------------------------------------
    # fill remaining fixed points
    # ------------------------------------------------------------------
    pts[PT_NAMES.index('head')]        = head
    pts[PT_NAMES.index('sho_l')]       = shoulder_left
    pts[PT_NAMES.index('sho_r')]       = shoulder_right
    pts[PT_NAMES.index('spine')]       = spine
    pts[PT_NAMES.index('hip_l')]       = hip_left
    pts[PT_NAMES.index('hip_r')]       = hip_right
    pts[PT_NAMES.index('pelvis_root')] = root

    return pts


# ------------------------------------------------------------------
# build animation
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 6), facecolor="black")
ax.set_facecolor("black")
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-0.2, 2.6)
ax.axis('off')

scat = ax.scatter([], [], s=35, c="white")


def init():
    scat.set_offsets(np.zeros((N_PTS, 2)))
    return scat,


def update(frame):
    pts = one_frame(frame)
    scat.set_offsets(pts)
    return scat,


ani = FuncAnimation(fig,
                    update,
                    frames=N_FRAMES,
                    init_func=init,
                    blit=True,
                    interval=1000/FPS)

# ------------------------------------------------------------------
# save to GIF (PillowWriter does not need external dependencies)
# ------------------------------------------------------------------
writer = PillowWriter(fps=FPS)
ani.save("running_point_light.gif", writer=writer)

# script end (nothing to display because we are in headless mode)
