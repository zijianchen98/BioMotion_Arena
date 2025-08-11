
"""
Point-light biological–motion stimulus
Action : “lying-down happy man” (15 white markers on a black background)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------------  kinematic helpers  ---------------------------

def rot(vec, ang):
    """Rotate 2-D vector `vec` by `ang` radians (counter-clock-wise)."""
    c, s = np.cos(ang), np.sin(ang)
    x, y = vec
    return np.array([c * x - s * y, s * x + c * y])


# -------------------------------  model constants  -----------------------------

# segment lengths  (arbitrary, but roughly body-proportionate)
HEAD2CHEST = 1.0
CHEST2PELV  = 1.5
UP_ARM      = 0.7   # shoulder→elbow
LO_ARM      = 0.7   # elbow→wrist
THIGH       = 1.0   # hip→knee
SHIN        = 1.0   # knee→ankle
HIP_OFFSET  = 0.5   # half torso width
SHL_OFFSET  = 0.5   # half shoulder width

# indices for easy reference
(
    HEAD, CHEST, PELVIS,
    L_SHO, R_SHO, L_ELB, R_ELB, L_WRI, R_WRI,
    L_HIP, R_HIP, L_KNE, R_KNE, L_ANK, R_ANK
) = range(15)


# -----------------------------  forward kinematics  ---------------------------

def skeleton(t):
    """
    Return (15,2) array with the 2-D marker coordinates
    for animation time `t`  (t in [0, 1] – one gait cycle).
    The lying figure is oriented left-to-right (head -> ankles).
    """

    # -----------------------------------------------------------------
    # 1. Static torso (lying horizontally, small breathing motion)
    # -----------------------------------------------------------------
    # gentle vertical oscillation to emulate breathing
    breathe = 0.05 * np.sin(2 * np.pi * t)
    # basic torso spine (head → chest → pelvis) along +x
    head   = np.array([0.0, breathe])
    chest  = head + np.array([HEAD2CHEST, 0.0])
    pelvis = chest + np.array([CHEST2PELV, 0.0])

    # -----------------------------------------------------------------
    # 2. Shoulders & Hips (fixed w.r.t. torso, but with breathing y-shift)
    # -----------------------------------------------------------------
    l_sho = chest + np.array([0.0,  SHL_OFFSET])
    r_sho = chest + np.array([0.0, -SHL_OFFSET])
    l_hip = pelvis + np.array([0.0,  HIP_OFFSET])
    r_hip = pelvis + np.array([0.0, -HIP_OFFSET])

    # -----------------------------------------------------------------
    # 3. Legs : raise / lower left leg – right leg stays relaxed
    # -----------------------------------------------------------------
    # rhythmic hip-flexion for left leg (30° swing)
    theta = np.deg2rad(30) * np.sin(2 * np.pi * t)
    # rhythmic knee flex/extension (20°) slightly phase-shifted
    phi   = np.deg2rad(20) * np.sin(2 * np.pi * t + np.pi / 3)

    # Left leg
    l_knee  = l_hip + rot(np.array([THIGH, 0.0]), theta)
    l_ankle = l_knee + rot(np.array([SHIN, 0.0]), theta + phi)

    # Right leg – small idle motion
    theta_r = np.deg2rad(10) * np.sin(2 * np.pi * t + np.pi)
    r_knee  = r_hip + rot(np.array([THIGH, 0.0]), theta_r)
    r_ankle = r_knee + rot(np.array([SHIN, 0.0]), theta_r * 0.5)

    # -----------------------------------------------------------------
    # 4. Arms : happy man waving left hand slightly
    # -----------------------------------------------------------------
    # waving with left arm
    alpha = np.deg2rad(25) * np.sin(2 * np.pi * t)
    beta  = np.deg2rad(20) * np.sin(2 * np.pi * t + np.pi / 2)

    l_elb  = l_sho + rot(np.array([UP_ARM, 0.0]), alpha)
    l_wri  = l_elb + rot(np.array([LO_ARM, 0.0]), alpha + beta)

    # right arm idle
    alpha_r = np.deg2rad(10) * np.sin(2 * np.pi * t + np.pi)
    r_elb   = r_sho + rot(np.array([UP_ARM, 0.0]), alpha_r)
    r_wri   = r_elb + rot(np.array([LO_ARM, 0.0]), alpha_r * 0.5)

    # -----------------------------------------------------------------
    # 5. Assemble marker list
    # -----------------------------------------------------------------
    pts = np.vstack([
        head, chest, pelvis,
        l_sho, r_sho, l_elb, r_elb, l_wri, r_wri,
        l_hip, r_hip, l_knee, r_knee, l_ankle, r_ankle
    ])

    return pts


# ------------------------------  visualization  -------------------------------

def main():
    fig, ax = plt.subplots(figsize=(7, 3))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_aspect('equal')
    ax.set_xlim(-1, 6)
    ax.set_ylim(-2.5, 2.5)
    ax.axis('off')

    # initial scatter (15 points)
    pts0 = skeleton(0.0)
    scat = ax.scatter(pts0[:, 0], pts0[:, 1],
                      c='white', s=30, edgecolors='none')

    # update function for FuncAnimation
    def update(frame):
        t = (frame % N_FRAMES) / N_FRAMES
        pts = skeleton(t)
        scat.set_offsets(pts)
        return scat,

    N_FRAMES = 100
    ani = FuncAnimation(fig, update, interval=40, blit=True)

    plt.show()


# ------------------------------------------------------------------------------
# run if executed as script
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
