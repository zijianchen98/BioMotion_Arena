
"""
Point-light biological–motion stimulus
Heavy, happy man repeatedly JUMPING UP
15 white dots on a black background
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --------------------------------------------------
#  Basic anthropometric proportions (metres)
# --------------------------------------------------
HEAD        = 0.25           # head height
NECK        = 0.05           # neck segment
TRUNK       = 0.55           # neck-to-pelvis
UPPER_ARM   = 0.30
LOWER_ARM   = 0.30
PELVIS_W    = 0.30
UPPER_LEG   = 0.50
LOWER_LEG   = 0.50
TOTAL_LEG   = UPPER_LEG + LOWER_LEG    # 1.0 m

#  Named joint indices (for readability)
HEAD_J, NECK_J, L_SHOULDER_J, R_SHOULDER_J, \
L_ELBOW_J,   R_ELBOW_J,     L_WRIST_J,  R_WRIST_J, \
PELVIS_J, L_HIP_J,  R_HIP_J, \
L_KNEE_J,  R_KNEE_J, L_ANKLE_J, R_ANKLE_J = range(15)

# --------------------------------------------------
#  Helper functions
# --------------------------------------------------
def rot(v, theta):
    """Rotate 2-D vector v by angle theta (radians) counter-clockwise."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])

def two_link(end, origin, L1, L2, bent=True, side=1):
    """
    Simple planar 2-link inverse kinematics:
    returns (knee, ankle) joint positions that reach `end`
    from `origin`.  If `bent` is False, leg remains straight.
    `side` ∈ {−1, 1} disambiguates the knee bending direction.
    """
    hip = origin
    foot = end
    if not bent:                       # straight leg
        knee = hip + (foot-hip) * L1/(L1+L2)
        return knee, foot
    d  = np.linalg.norm(foot-hip)
    d  = np.clip(d, 1e-6, L1+L2-1e-6)  # avoid domain errors
    # cosine law
    angle_knee = np.arccos((L1**2 + L2**2 - d**2)/(2*L1*L2))
    angle_hip  = np.arccos((L1**2 + d**2 - L2**2)/(2*L1*d))
    dir_vec    = (foot-hip)/d
    # rotate to get knee position
    knee_dir   = rot(dir_vec, side*angle_hip)
    knee       = hip + knee_dir*L1
    return knee, foot

# --------------------------------------------------
#  Master pose generator
# --------------------------------------------------
def skeleton_points(phase):
    """
    Generate 15 joint coordinates for a given phase ∈ [0,1).
    One complete cycle: crouch → jump → airborne → land
    """
    # ----- Pelvis vertical trajectory -----
    BASE_PELVIS = TOTAL_LEG            # 1.0 m (standing)
    CROUCH_D    = 0.30                 # how deep we crouch
    JUMP_D      = 0.50                 # aerial peak displacement

    if phase < 0.25:                               # crouch
        p = phase/0.25
        pelvis_y = BASE_PELVIS - CROUCH_D*p        # go down
        airborne = False
    elif phase < 0.50:                             # push upward
        p = (phase-0.25)/0.25
        pelvis_y = BASE_PELVIS - CROUCH_D*(1-p) + JUMP_D*p
        airborne = False                           # still on ground
    elif phase < 0.75:                             # airborne apex
        p = (phase-0.50)/0.25
        pelvis_y = BASE_PELVIS + JUMP_D*(1-p)      # descend
        airborne = True
    else:                                          # landing (reverse crouch)
        p = (phase-0.75)/0.25
        pelvis_y = BASE_PELVIS - CROUCH_D*p
        airborne = False

    # Lateral offsets (so he looks "heavy": wide stance)
    shoulder_w = 0.40
    hip_w      = PELVIS_W/2
    foot_w     = 0.20

    # ---- Torso & head ----
    pelvis   = np.array([0.0, pelvis_y])
    neck     = pelvis + np.array([0, TRUNK])
    head     = neck  + np.array([0, HEAD])

    l_shldr  = neck + np.array([-shoulder_w/2, 0])
    r_shldr  = neck + np.array([ shoulder_w/2, 0])

    # ---- Arm swing (simple sinusoid) ----
    #   back (crouch)  → forward-up (airborne)
    swing = np.sin(2*np.pi*phase)                 # (−1 → 1)
    # heavy man: smaller amplitude behind, larger forwards
    arm_forward = np.deg2rad(60 + 30*swing)       # front (0° = down)
    arm_backward= np.deg2rad(190 + 10*swing)      # back

    # Left arm swings forward, right arm too (symmetric)
    def arm(joint, theta, side):
        upper = rot(np.array([0, -UPPER_ARM]), theta)*side
        elbow = joint + upper
        fore  = rot(np.array([0, -LOWER_ARM]), theta)*side
        wrist = elbow + fore
        return elbow, wrist

    l_elbow, l_wrist = arm(l_shldr, arm_forward, side=-1)
    r_elbow, r_wrist = arm(r_shldr, arm_forward, side=1)

    # ----- Legs -----
    # Desired foot positions
    if airborne:
        # Feet leave ground, travel with pelvis (leg straight)
        l_foot = pelvis + np.array([-foot_w, -TOTAL_LEG])
        r_foot = pelvis + np.array([ foot_w, -TOTAL_LEG])
        bent   = False
    else:
        # Feet planted on ground (y=0)
        l_foot = np.array([-foot_w, 0.0])
        r_foot = np.array([ foot_w, 0.0])
        bent   = True

    l_hip = pelvis + np.array([-hip_w, 0])
    r_hip = pelvis + np.array([ hip_w, 0])

    # Inverse kinematics to retrieve knee & ankle
    l_knee, l_ankle = two_link(l_foot, l_hip, UPPER_LEG, LOWER_LEG,
                               bent=bent, side=-1)
    r_knee, r_ankle = two_link(r_foot, r_hip, UPPER_LEG, LOWER_LEG,
                               bent=bent, side=1)

    # Assemble in order
    joints = np.stack([head, neck,
                       l_shldr, r_shldr,
                       l_elbow, r_elbow,
                       l_wrist, r_wrist,
                       pelvis, l_hip, r_hip,
                       l_knee, r_knee,
                       l_ankle, r_ankle])
    return joints[:,0], joints[:,1]     # (x, y)

# --------------------------------------------------
#  Matplotlib animation
# --------------------------------------------------
fig, ax = plt.subplots(figsize=(4,8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-0.2, 2.2)
ax.set_aspect('equal')
ax.axis('off')

# Initial scatter
xs, ys = skeleton_points(0)
scat = ax.scatter(xs, ys, c='white', s=50)

def update(frame):
    phase = (frame % 120) / 120.0      # one jump = 120 frames
    xs, ys = skeleton_points(phase)
    scat.set_offsets(np.c_[xs, ys])
    return scat,

anim = FuncAnimation(fig, update, frames=240, interval=25, blit=True)

plt.show()
