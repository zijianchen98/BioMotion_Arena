
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Body segment lengths (in arbitrary units)
TORSO_LEN = 0.6
NECK_LEN = 0.1
HEAD_LEN = 0.2
SHOULDER_SPREAD = 0.5
HIP_SPREAD = 0.4
UPPER_ARM_LEN = 0.3
FOREARM_LEN = 0.3
THIGH_LEN = 0.5
SHIN_LEN = 0.5

# Motion parameters
FRAMES = 120
INTERVAL = 30    # milliseconds between frames
SQUAT_FRAMES_DOWN = 30
SQUAT_FRAMES_UP = 10
FLIGHT_FRAMES = 50
SQUAT_DEPTH = 0.3    # how much hip lowers at full squat
HIP_FLEX_MAX = np.deg2rad(45)   # maximum hip flexion angle at bottom
KNEE_FLEX_MAX = np.deg2rad(60)  # maximum knee flexion at bottom
JUMP_HEIGHT = 0.6               # peak jump height

# Precompute a time array
t = np.arange(FRAMES)

def squash_factor(frame):
    """Compute squat factor s in [0..1] based on frame index."""
    if frame < SQUAT_FRAMES_DOWN:
        # ease-in-out from 0 to 1
        return 0.5 * (1 - np.cos(np.pi * frame / SQUAT_FRAMES_DOWN))
    elif frame < SQUAT_FRAMES_DOWN + SQUAT_FRAMES_UP:
        # ease-out from 1 back to 0
        tt = frame - SQUAT_FRAMES_DOWN
        return 0.5 * (1 + np.cos(np.pi * tt / SQUAT_FRAMES_UP))
    else:
        return 0.0

def jump_offset(frame):
    """Compute vertical jump offset based on frame index."""
    start = SQUAT_FRAMES_DOWN + SQUAT_FRAMES_UP
    end = start + FLIGHT_FRAMES
    if start <= frame < end:
        # simple sine‐shaped flight: starts & ends at 0, peaks at middle
        phi = np.pi * (frame - start) / FLIGHT_FRAMES
        return JUMP_HEIGHT * np.sin(phi)
    else:
        return 0.0

# Setup figure and scatter plot
fig, ax = plt.subplots(figsize=(5, 7))
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-0.5, 2.2)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter (15 points)
pts = ax.scatter(
    np.zeros(15),
    np.zeros(15),
    s=80,
    c='white'
)

def get_joint_positions(frame):
    """
    Return an array of shape (15,2) with the x,y coords of the 15 point-lights:
    0: head top
    1: neck
    2: left shoulder
    3: right shoulder
    4: left elbow
    5: right elbow
    6: left wrist
    7: right wrist
    8: spine midpoint
    9: left hip
    10: right hip
    11: left knee
    12: right knee
    13: left ankle
    14: right ankle
    """
    s = squash_factor(frame)
    y_off = - SQUAT_DEPTH * s + jump_offset(frame)

    # current flex angles
    hip_angle = HIP_FLEX_MAX * s
    knee_angle = KNEE_FLEX_MAX * s

    # local shoulder & hip coords (relative to root = origin)
    left_hip_local  = np.array([-HIP_SPREAD/2, 0.0])
    right_hip_local = np.array([ HIP_SPREAD/2, 0.0])
    spine_local     = np.array([0.0, TORSO_LEN/2])
    left_sho_local  = np.array([-SHOULDER_SPREAD/2, TORSO_LEN])
    right_sho_local = np.array([ SHU‍OULDER_SPREAD/2, TORSO_LEN])
    neck_local      = np.array([0.0, TORSO_LEN + NECK_LEN])
    head_local      = np.array([0.0, TORSO_LEN + NECK_LEN + HEAD_LEN])

    # global translations
    def to_global(pt):
        return pt + np.array([0.0, y_off])

    # Hips
    lh = to_global(left_hip_local)
    rh = to_global(right_hip_local)

    # Knees & Ankles for each leg
    # Thigh direction
    thigh_dir = np.array([np.sin(hip_angle), -np.cos(hip_angle)])
    # Shin direction (rotated by knee flex)
    shin_dir  = np.array([np.sin(hip_angle + knee_angle), -np.cos(hip_angle + knee_angle)])

    lknee = lh + THIGH_LEN * thigh_dir
    rknee = rh + THIGH_LEN * thigh_dir
    lankle = lknee + SHIN_LEN * shin_dir
    rankle = rknee + SHIN_LEN * shin_dir

    # Shoulders, Spine, Neck, Head
    ls = to_global(left_sho_local)
    rs = to_global(right_sho_local)
    sp = to_global(spine_local)
    nk = to_global(neck_local)
    hd = to_global(head_local)

    # Arms (static hanging)
    le = ls + np.array([0.0, -UPPER_ARM_LEN])
    re = rs + np.array([0.0, -UPPER_ARM_LEN])
    lw = le + np.array([0.0, -FOREARM_LEN])
    rw = re + np.array([0.0, -FOREARM_LEN])

    # Assemble
    pts = np.vstack([
        hd,  # 0 head top
        nk,  # 1 neck
        ls,  # 2 left shoulder
        rs,  # 3 right shoulder
        le,  # 4 left elbow
        re,  # 5 right elbow
        lw,  # 6 left wrist
        rw,  # 7 right wrist
        sp,  # 8 spine
        lh,  # 9 left hip
        rh,  # 10 right hip
        lknee,  # 11 left knee
        rknee,  # 12 right knee
        lankle, # 13 left ankle
        rankle  # 14 right ankle
    ])
    return pts

# Animation update function
def update(frame):
    positions = get_joint_positions(frame)
    pts.set_offsets(positions)
    return (pts,)

anim = FuncAnimation(
    fig, update, frames=FRAMES,
    interval=INTERVAL, blit=True, repeat=True
)

plt.show()
