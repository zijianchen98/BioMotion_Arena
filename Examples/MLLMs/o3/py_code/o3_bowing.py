
"""
Point-light biological motion stimulus
Action: Man bowing
Exactly 15 white dots on a black background
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------  Skeleton spec ------------------------------ #

# Index names (only for reference / clarity)
(
    HEAD, NECK,
    L_SHO, R_SHO,
    L_ELB, R_ELB,
    L_WRI, R_WRI,
    L_HIP, R_HIP,
    L_KNE, R_KNE,
    L_ANK, R_ANK,
    PELVIS                         # mid-hip (extra point -> 15 total)
) = range(15)


# Segment lengths (arbitrary, consistent units)
TORSO_LEN     = 0.45          # shoulder → hip
NECK_LEN      = 0.10          # neck  → shoulder midpoint
HEAD_LEN      = 0.15          # neck  → top of head
ARM_UP_LEN    = 0.25          # shoulder → elbow
ARM_LOW_LEN   = 0.25          # elbow    → wrist
LEG_UP_LEN    = 0.45          # hip      → knee
LEG_LOW_LEN   = 0.45          # knee     → ankle

# Horizontal offsets (distance between left / right joints)
HIP_OFFSET    = 0.12
SHOULDER_OFFSET = 0.15

# --------------------------------------------------------------------------- #

def rotate(v, theta):
    """Rotate 2-D vector v by theta (rad) counter-clockwise (CCW)."""
    c, s = np.cos(theta), np.sin(theta)
    rot = np.array([[c, -s], [s, c]])
    return rot @ v


def skeleton_cfg(t):
    """
    Compute 2-D positions (x,y) for all 15 joints at time t (0-1).
    t=0   : upright
    t=0.5 : deepest part of bow
    t=1   : back upright   (cycle repeats)
    Returns: (15,2) array
    """
    # Bow parameters
    max_torso_pitch = np.deg2rad(50)          # maximum forward lean (positive value)
    pitch = max_torso_pitch * np.sin(np.pi * t)   # 0 → max → 0

    # During the bow hips are lowered slightly
    hip_drop = 0.05 * np.sin(np.pi * t)

    # World origin on ground between feet
    origin = np.array([0.0, 0.0])

    # Ankles (feet) – fixed to ground
    l_ank = origin + np.array([-HIP_OFFSET, 0.0])
    r_ank = origin + np.array([ HIP_OFFSET, 0.0])

    # Hips
    base_hip_height = LEG_UP_LEN + LEG_LOW_LEN   # upright hip y
    hip_y = base_hip_height - hip_drop
    l_hip = np.array([-HIP_OFFSET, hip_y])
    r_hip = np.array([ HIP_OFFSET, hip_y])

    # Knee positions (simple geometric interpolation + small forward shift)
    def knee_pos(ank, hip):
        knee_y = (ank[1] + hip[1]) / 2
        knee_x = ank[0] * 0.4 + hip[0] * 0.6    # a bit closer to hip
        return np.array([knee_x, knee_y])
    l_knee = knee_pos(l_ank, l_hip)
    r_knee = knee_pos(r_ank, r_hip)

    # Torso vector (shoulder centre relative to hip centre) – rotated forward
    hip_center = (l_hip + r_hip) / 2
    torso_vec = rotate(np.array([0.0, TORSO_LEN]), -pitch)  # lean forward (negative angle)
    shoulder_center = hip_center + torso_vec

    # Shoulders (left / right)
    l_sho = shoulder_center + np.array([-SHOULDER_OFFSET, 0.0])
    r_sho = shoulder_center + np.array([ SHOULDER_OFFSET, 0.0])

    # Neck & head (continue torso line)
    neck = shoulder_center + rotate(np.array([0.0, NECK_LEN]), -pitch)
    head = neck + rotate(np.array([0.0, HEAD_LEN]), -pitch)

    # Arms hang naturally, rotate with the torso
    arm_down_vec = rotate(np.array([0.0, -ARM_UP_LEN]), -pitch)
    l_elb = l_sho + arm_down_vec
    r_elb = r_sho + arm_down_vec

    forearm_vec = rotate(np.array([0.0, -ARM_LOW_LEN]), -pitch)
    l_wri = l_elb + forearm_vec
    r_wri = r_elb + forearm_vec

    # Assemble into array
    pts = np.vstack([
        head, neck,
        l_sho, r_sho,
        l_elb, r_elb,
        l_wri, r_wri,
        l_hip, r_hip,
        l_knee, r_knee,
        l_ank, r_ank,
        hip_center   # pelvis / 14th index -> 15th point
    ])

    return pts


# -------------------------------  Plotting --------------------------------- #

fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-0.1, 1.8)
ax.set_aspect('equal')
ax.axis('off')

# 15 white point-lights
scatter = ax.scatter([], [], s=50, c='white')

def init():
    scatter.set_offsets(np.zeros((15, 2)))
    return scatter,

def update(frame):
    # frame ranges 0..N-1, convert to t 0..1
    t = (frame % FRAMES) / FRAMES
    pts = skeleton_cfg(t)
    scatter.set_offsets(pts)
    return scatter,

FRAMES = 100
ani = FuncAnimation(fig, update, frames=FRAMES, interval=30,
                    init_func=init, blit=True)

plt.show()
