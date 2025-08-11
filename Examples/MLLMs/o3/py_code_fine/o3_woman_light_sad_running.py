
"""
Biological-motion point–light stimulus
15 white dots (sad, light-weight woman running)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --------------------------  kinematic helpers  --------------------------- #
def rot(angle):
    """2-D rotation matrix"""
    return np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle),  np.cos(angle)]])

def limb(start, angle, length):
    """Return end-point of a limb segment"""
    return start + rot(angle).dot(np.array([0, -length]))  # ‘0,-L’ = down in local frame


# ---------------------------  runner model  ------------------------------- #
class Runner:
    """
    Very small 2-D articulated model with
    15 anatomical landmarks:
      0 head
      1 left shoulder, 2 right shoulder
      3 left elbow,   4 right elbow
      5 left wrist,   6 right wrist
      7 pelvis/hip centre
      8 left hip,     9 right hip
     10 left knee,   11 right knee
     12 left ankle,  13 right ankle
     14 sternum (chest centre)
    """

    # segment lengths (rough proportions, arbitrary units)
    TORSO       = 0.50       # hip → shoulder
    HEAD        = 0.15
    U_ARM       = 0.35
    F_ARM       = 0.30
    THIGH       = 0.45
    SHIN        = 0.45

    HIP_W       = 0.30
    SHOULDER_W  = 0.40

    # motion amplitudes (radians / units)
    HIP_SWING   = np.deg2rad(30)
    KNEE_BEND   = np.deg2rad(60)
    ARM_SWING   = np.deg2rad(40)
    BOB         = 0.05

    def __call__(self, t):
        """
        Return 15×2 array of x,y coordinates for time t (seconds).
        The woman is running in place; cycle frequency ≈ 2 Hz.
        """
        # convert time to phase (one full gait cycle = 2π)
        phase = 2 * np.pi * 2 * t        # 2 Hz → angular speed 4π rad · s⁻¹
        s, c = np.sin(phase), np.cos(phase)

        # vertical body bob
        pelvis = np.array([0.0, self.BOB * np.sin(2*phase)])

        # torso and head (head slightly lowered – sad appearance)
        shoulder_ctr = pelvis + np.array([0.0,  self.TORSO])
        head         = shoulder_ctr + np.array([0.0,  self.HEAD * 0.9])

        # chest / sternum
        chest = (pelvis + shoulder_ctr)/2

        # hips and shoulders (widths)
        l_hip = pelvis + np.array([-self.HIP_W/2, 0.0])
        r_hip = pelvis + np.array([ self.HIP_W/2, 0.0])

        l_sh  = shoulder_ctr + np.array([-self.SHOULDER_W/2, 0.0])
        r_sh  = shoulder_ctr + np.array([ self.SHOULDER_W/2, 0.0])

        # -------------------------  legs  -------------------------- #
        # hip angles
        th_l = -np.pi/2 + self.HIP_SWING * s          # left thigh
        th_r = -np.pi/2 + self.HIP_SWING * (-s)       # right thigh (opposite)

        # knee flex only when leg is lifted (positive swing)
        bend_l = self.KNEE_BEND * max(0.0,  s)
        bend_r = self.KNEE_BEND * max(0.0, -s)

        # left leg kinematics
        l_knee  = limb(l_hip, th_l,        self.THIGH)
        l_ankle = limb(l_knee, th_l-bend_l, self.SHIN)

        # right leg kinematics
        r_knee  = limb(r_hip, th_r,        self.THIGH)
        r_ankle = limb(r_knee, th_r-bend_r, self.SHIN)

        # -------------------------  arms  -------------------------- #
        # arm swing (opposite to legs) – subdued amplitude (sad)
        a_l = -np.pi/2 + 0.7*self.ARM_SWING * (-s)    # left upper arm
        a_r = -np.pi/2 + 0.7*self.ARM_SWING * ( s)    # right upper arm

        # constant slight elbow bend
        ELBOW = np.deg2rad(30)

        l_elb  = limb(l_sh, a_l,        self.U_ARM)
        l_wrist= limb(l_elb, a_l-ELBOW, self.F_ARM)

        r_elb  = limb(r_sh, a_r,        self.U_ARM)
        r_wrist= limb(r_elb, a_r-ELBOW, self.F_ARM)

        # ----------------------  assemble list  -------------------- #
        joints = np.stack([
            head,         # 0
            l_sh,  r_sh,  # 1,2
            l_elb, r_elb, # 3,4
            l_wrist, r_wrist,  # 5,6
            pelvis,       # 7
            l_hip, r_hip, # 8,9
            l_knee, r_knee,     #10,11
            l_ankle, r_ankle,   #12,13
            chest              #14
        ])
        return joints


# --------------------------  animation  ---------------------------------- #
runner = Runner()

fig, ax = plt.subplots(figsize=(4,6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 1.8)
ax.axis('off')

# 15 white dots
scat = ax.scatter(np.zeros(15), np.zeros(15), s=40, color='white')

def update(frame):
    t = frame / 60     # 60 fps time base
    pts = runner(t)
    scat.set_offsets(pts)
    return scat,

ani = FuncAnimation(fig, update, frames=600, interval=1000/60, blit=True)

plt.show()
