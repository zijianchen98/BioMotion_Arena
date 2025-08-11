
"""
Point-light stimulus animation
15 white dots against a black background
Action : Walking   Actor : (sad) woman carrying body-weight
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------------------------------------------------------------------------- 
# basic kinematics helpers
# ----------------------------------------------------------------------------- 
def rot(vec, ang):
    """rotate a 2-D vector by ang (radians)."""
    c, s = np.cos(ang), np.sin(ang)
    x, y = vec
    return np.array([c * x - s * y, s * x + c * y])

# ----------------------------------------------------------------------------- 
# parameter set (all numbers in an arbitrary ‘body-length’ unit)
# ----------------------------------------------------------------------------- 
UP_LEG   = 0.60   # hip  → knee
LO_LEG   = 0.58   # knee → ankle
TORSO    = 0.95   # pelvis → shoulders
NECK     = 0.20   # shoulder → neck
HEAD     = 0.25   # neck → head (centre)
UP_ARM   = 0.42   # shoulder → elbow
LO_ARM   = 0.40   # elbow   → wrist
SH_OFF   = 0.28   # half shoulder-width
HIP_OFF  = 0.18   # half pelvis-width

SPEED    = 0.018                 # forward translation (world units / ms)
PERIOD   = 2200                  # ms for one gait cycle (slow ‘sad’ pace)
BOUNCE_A = 0.04                  # vertical body bounce amplitude
DROOP    = np.deg2rad(10)        # torso droop  (sad posture)

# indices of the 15 points -----------------------------------------------------
# 0=Head,1=Neck,2=L.Sh,3=R.Sh,4=L.El,5=R.El,6=L.Wr,7=R.Wr,
# 8=Pelvis,9=L.Hip,10=R.Hip,11=L.Knee,12=R.Knee,13=L.Ank,14=R.Ank

def skeleton(t_ms):
    """
    Returns a (15,2) ndarray with XY positions of every marker at time t (ms).
    The global +y axis is upward, +x axis points to walking direction.
    """
    phase = 2 * np.pi * (t_ms % PERIOD) / PERIOD

    # pelvis centre ------------------------------------------------------------
    x_root = SPEED * t_ms
    y_root = BOUNCE_A * np.sin(phase * 2)  # two bounces per step
    pelvis = np.array([x_root, y_root])

    # torso line (pelvis → shoulders, with small forward droop)
    torso_vec = rot(np.array([0,  TORSO]),  DROOP)   # up but pitched forward
    sh_centre = pelvis + torso_vec                  # shoulder centre point

    # shoulders / neck / head --------------------------------------------------
    l_sh = sh_centre + np.array([-SH_OFF, 0])
    r_sh = sh_centre + np.array([ SH_OFF, 0])
    neck = sh_centre + np.array([0,  NECK])
    head = neck      + np.array([0,  HEAD])

    # arm swing : opposite phase to legs ---------------------------------------
    arm_amp  = np.deg2rad(22)            # swing range
    l_arm_a  =  arm_amp * np.sin(phase + np.pi) - np.deg2rad(65)   # hangs down
    r_arm_a  =  arm_amp * np.sin(phase)  - np.deg2rad(65)

    el_l = l_sh + rot(np.array([0, -UP_ARM]), -l_arm_a)   # elbow positions
    el_r = r_sh + rot(np.array([0, -UP_ARM]), -r_arm_a)

    wr_l = el_l + rot(np.array([0, -LO_ARM]), -l_arm_a)
    wr_r = el_r + rot(np.array([0, -LO_ARM]), -r_arm_a)

    # leg angles ---------------------------------------------------------------
    hip_amp = np.deg2rad(32)
    l_hip_a = hip_amp * np.sin(phase)           # left leg angle from vertical
    r_hip_a = hip_amp * np.sin(phase + np.pi)   # right in opposite phase

    # knee flexion : bend when leg moves forward (swing)
    knee_amp  = np.deg2rad(45)
    l_knee_a  = knee_amp * (0.5 - 0.5 * np.cos(phase))     # 0 → π
    r_knee_a  = knee_amp * (0.5 - 0.5 * np.cos(phase+np.pi))

    hip_l = pelvis + np.array([-HIP_OFF, 0])
    hip_r = pelvis + np.array([ HIP_OFF, 0])

    # forward kinematics (left leg) -------------------------------------------
    knee_l = hip_l + rot(np.array([0, -UP_LEG]),  l_hip_a)
    ank_l  = knee_l + rot(np.array([0, -LO_LEG]), l_hip_a + l_knee_a)

    # right leg ---------------------------------------------------------------
    knee_r = hip_r + rot(np.array([0, -UP_LEG]),  r_hip_a)
    ank_r  = knee_r + rot(np.array([0, -LO_LEG]), r_hip_a + r_knee_a)

    # assemble marker list -----------------------------------------------------
    pts = np.vstack([head, neck,
                     l_sh,  r_sh,
                     el_l,  el_r,
                     wr_l,  wr_r,
                     pelvis,
                     hip_l, hip_r,
                     knee_l, knee_r,
                     ank_l, ank_r])
    return pts

# ----------------------------------------------------------------------------- 
# matplotlib set-up
# ----------------------------------------------------------------------------- 
plt.style.use('dark_background')
fig = plt.figure(figsize=(4, 6), facecolor='black')
ax  = fig.add_subplot(111, facecolor='black')
ax.set_aspect('equal')
ax.set_xlim(-1, 3)     # will be panned during walk
ax.set_ylim(-0.5, 2.5)
ax.axis('off')

# 15 white dots
scat = ax.scatter(np.zeros(15), np.zeros(15),
                  s=50, c='white', edgecolors='none')

# ----------------------------------------------------------------------------- 
# animation callback
# ----------------------------------------------------------------------------- 
def update(frame):
    t = frame * 40                       # interval=40ms
    pts = skeleton(t)
    scat.set_offsets(pts)

    # pan camera so actor stays roughly centred
    mid_x = pts[8, 0]
    ax.set_xlim(mid_x - 1, mid_x + 1.6)
    return scat,

ani = FuncAnimation(fig, update, frames=np.arange(0, 300),
                    interval=40, blit=True)

if __name__ == "__main__":
    plt.show()
