
"""
Biological-motion style point–light animation
15 white dots (joints) on a black background
Action : a light-weight “stickman” waving the right hand
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------------------------------------------------
#  Skeleton description               (total = 15 joints)
# ------------------------------------------------------------
#  0 : head
#  1 : neck
#  2 : left shoulder
#  3 : right shoulder
#  4 : left elbow
#  5 : right elbow
#  6 : left wrist
#  7 : right wrist         <-- waving
#  8 : hip centre
#  9 : left hip
# 10 : right hip
# 11 : left knee
# 12 : right knee
# 13 : left ankle
# 14 : right ankle
# ------------------------------------------------------------

# Anatomical segment lengths (arbitrary, internally-consistent units)
L_HEAD      = 1.0
L_NECK      = 0.5
L_SPINE     = 3.0         # neck→hip-centre
L_SHOULDER  = 1.0         # neck→shoulder (left/right)
L_UPPER_ARM = 1.6         # shoulder→elbow
L_FOREARM   = 1.6         # elbow→wrist
L_PELVIS    = 0.8         # hip-centre → hip (left/right)
L_THIGH     = 2.2         # hip→knee
L_SHANK     = 2.2         # knee→ankle

# ------------------------------------------------------------
#  Helper functions
# ------------------------------------------------------------
def pol2cart(r, theta):
    """Polar (r,θ) → Cartesian (x,y). θ is in radians wrt +x axis (matplotlib convention)"""
    return np.array([r * np.cos(theta), r * np.sin(theta)])

def build_skeleton(t):
    """
    Return the (x,y) coordinates of the 15 joints at animation-time t (seconds)
    Implements simple kinematics with sinusoidal phases to obtain a smooth,
    biomechanically plausible right-hand wave.  All angles in radians.
    """

    # --------------- torso ---------------
    hip_c   = np.array([0.0, 0.0])
    neck    = hip_c + np.array([0.0, L_SPINE])
    head    = neck + np.array([0.0, L_HEAD])

    # small torso sway keeps the figure 'alive'
    sway_amp = np.deg2rad(3)
    torso_angle = sway_amp * np.sin(2 * np.pi * 0.5 * t)  # ±3°
    rot = np.array([[ np.cos(torso_angle), -np.sin(torso_angle)],
                    [ np.sin(torso_angle),  np.cos(torso_angle)]])

    neck    = hip_c + rot @ np.array([0.0, L_SPINE])
    head    = neck  + rot @ np.array([0.0, L_HEAD])

    # --------------- shoulders ---------------
    l_shoulder = neck + rot @ np.array([-L_SHOULDER, 0.0])
    r_shoulder = neck + rot @ np.array([ L_SHOULDER, 0.0])

    # --------------- left arm (static hang) ---------------
    l_elbow  = l_shoulder + rot @ pol2cart(L_UPPER_ARM, -np.pi/2 - np.deg2rad(5))
    l_wrist  = l_elbow    + rot @ pol2cart(L_FOREARM, -np.pi/2 - np.deg2rad(5))

    # --------------- right arm (waving) ---------------
    # upper-arm swings between 20° forward & 60° backward from vertical
    theta_upper = -np.pi/2 + np.deg2rad(20) * np.sin(2*np.pi*0.5*t)
    # forearm oscillates faster to realise hand motion
    theta_fore  = np.deg2rad(70) * np.sin(2*np.pi*1.0*t)

    r_elbow = r_shoulder + rot @ pol2cart(L_UPPER_ARM, theta_upper)
    r_wrist = r_elbow    + rot @ pol2cart(L_FOREARM, theta_upper + theta_fore)

    # --------------- pelvis & legs ---------------
    l_hip   = hip_c + np.array([-L_PELVIS, 0.0])
    r_hip   = hip_c + np.array([ L_PELVIS, 0.0])

    walk_amp = np.deg2rad(10)
    leg_phase = 2*np.pi*0.5*t
    l_thigh_angle = -np.pi/2 + walk_amp * np.sin(leg_phase)
    r_thigh_angle = -np.pi/2 + walk_amp * np.sin(leg_phase + np.pi)

    l_knee  = l_hip + rot @ pol2cart(L_THIGH, l_thigh_angle)
    r_knee  = r_hip + rot @ pol2cart(L_THIGH, r_thigh_angle)

    shank_angle = -np.pi/2  # almost straight down
    l_ankle = l_knee + rot @ pol2cart(L_SHANK, shank_angle)
    r_ankle = r_knee + rot @ pol2cart(L_SHANK, shank_angle)

    # --------------------------------------------------------
    joints = np.vstack([head, neck,
                        l_shoulder, r_shoulder,
                        l_elbow,    r_elbow,
                        l_wrist,    r_wrist,
                        hip_c,
                        l_hip,      r_hip,
                        l_knee,     r_knee,
                        l_ankle,    r_ankle])
    return joints.T   # shape (2,15)

# ------------------------------------------------------------
#  Matplotlib animation
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4,8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(-4, 4)
ax.set_ylim(-6, 8)

# scatter plot for 15 points
points = ax.scatter([], [], s=40, c='white')

def init():
    points.set_offsets(np.zeros((15,2)))
    return points,

def animate(frame):
    t = frame / 30.0               # 30 fps → t in seconds
    xy = build_skeleton(t)
    offsets = np.column_stack((xy[0], xy[1]))
    points.set_offsets(offsets)
    return points,

ani = animation.FuncAnimation(fig, animate,
                              init_func=init,
                              frames=300,      # ~10 s loop
                              interval=33,     # ~30 fps
                              blit=True)

plt.show()
