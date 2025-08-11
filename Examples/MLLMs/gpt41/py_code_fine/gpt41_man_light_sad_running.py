
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point-lights (15: standard for human biological motion)
NUM_POINTS = 15

# Marker names for clarity (not required for display)
MARKERS = [
    "Head",
    "Right Shoulder", "Left Shoulder",
    "Right Elbow", "Left Elbow",
    "Right Wrist", "Left Wrist",
    "Pelvis (Midhip)",
    "Right Hip", "Left Hip",
    "Right Knee", "Left Knee",
    "Right Ankle", "Left Ankle",
    "Weight (Dumbbell)"
]

# "Sadman" running 2D skeleton parameters (arrays are in order of MARKERS)
# These are based on rough biomechanics and can be refined

def get_skeleton_frame(tphase):
    """
    Calculate the 2D positions of all 15 markers at time tphase (0..1 is one running cycle).
    Returns an array of shape (NUM_POINTS, 2): [(x1, y1), (x2, y2), ...]
    The skeleton "runs" horizontally, left-to-right.
    """
    # Scale for the body
    body_len = 1.0   # Total height (normalized)
    shoulder_w = 0.23
    hip_w = 0.20
    arm_l = 0.32
    forearm_l = 0.24
    thigh_l = 0.38
    shank_l = 0.38
    head_h = 0.13
    neck_h = 0.07
    pelvis_drop = 0.08

    # Locomotion phase (for running, two legs alternate)
    phase = tphase * 2 * np.pi

    # Vertical translation (slightly up and down as in running)
    y_pelvis = 0.5 * body_len + 0.06 * np.sin(2 * phase)
    x_pelvis = 0.5 + 0.19 * tphase  # forward progress, runs left to right in frame

    # Shoulder position
    y_shoulders = y_pelvis + pelvis_drop + 0.24
    x_shoulder_mid = x_pelvis

    # Head
    xy_head = [x_shoulder_mid, y_shoulders + neck_h + head_h * 0.5]
    # Shoulders
    xy_rshoulder = [x_shoulder_mid - shoulder_w*0.5, y_shoulders]
    xy_lshoulder = [x_shoulder_mid + shoulder_w*0.5, y_shoulders]
    # Elbows (arms swing out of phase with legs)
    arm_swing = 0.90 * np.sin(phase)
    xy_relbow = [
        xy_rshoulder[0] - arm_l * np.cos(arm_swing) * 0.80, 
        xy_rshoulder[1] - arm_l * np.sin(arm_swing)
    ]
    xy_lelbow = [
        xy_lshoulder[0] + arm_l * np.cos(arm_swing) * 0.80, 
        xy_lshoulder[1] - arm_l * np.sin(arm_swing)
    ]
    # Wrists (further swing)
    forearm_angle = np.pi/4 * np.sin(phase)
    xy_rwrist = [
        xy_relbow[0] - forearm_l * np.cos(arm_swing + forearm_angle) * 0.97, 
        xy_relbow[1] - forearm_l * np.sin(arm_swing + forearm_angle)
    ]
    xy_lwrist = [
        xy_lelbow[0] + forearm_l * np.cos(arm_swing + forearm_angle) * 0.97, 
        xy_lelbow[1] - forearm_l * np.sin(arm_swing + forearm_angle)
    ]

    # Mid-hip/pelvis
    xy_pelvis = [x_pelvis, y_pelvis]

    # Hip positions
    xy_rhip = [x_pelvis - hip_w*0.5, y_pelvis]
    xy_lhip = [x_pelvis + hip_w*0.5, y_pelvis]

    # Leg phasing (legs out of phase with each other)
    leg_swing = 1.0 * np.sin(phase)
    # Right leg is lead leg, left is trail
    thigh_r = thigh_l * 0.97
    thigh_lg = thigh_l * 0.97
    # R thigh swings forward, L backward
    rleg_swing_angle = np.pi / 5 * np.sin(phase + np.pi)  # out of phase
    lleg_swing_angle = np.pi / 5 * np.sin(phase)
    
    # Right knee
    xy_rknee = [
        xy_rhip[0] + thigh_r * np.sin(rleg_swing_angle), 
        xy_rhip[1] - thigh_r * np.cos(rleg_swing_angle)
    ]
    # Left knee
    xy_lknee = [
        xy_lhip[0] + thigh_lg * np.sin(lleg_swing_angle), 
        xy_lhip[1] - thigh_lg * np.cos(lleg_swing_angle)
    ]
    # Knee-to-ankle (knee angle bends with running gait)
    # Bending (assume high knee) - angle is smaller when leg in swing, more extended in stance
    r_bend = np.pi/4 * (0.75 + 0.25*np.sin(phase + np.pi))
    l_bend = np.pi/4 * (0.75 + 0.25*np.sin(phase))

    # Right ankle
    ankle_r_angle = rleg_swing_angle + r_bend
    xy_rankle = [
        xy_rknee[0] + shank_l * np.sin(ankle_r_angle), 
        xy_rknee[1] - shank_l * np.cos(ankle_r_angle)
    ]
    # Left ankle
    ankle_l_angle = lleg_swing_angle + l_bend
    xy_lankle = [
        xy_lknee[0] + shank_l * np.sin(ankle_l_angle), 
        xy_lknee[1] - shank_l * np.cos(ankle_l_angle)
    ]
    # "Sad" effect: head a bit lower, arms more drawn in, tempo down; you may add a little head dip, wrist drag, etc
    xy_head[1] -= 0.02*np.sin(phase) + 0.05
    xy_rwrist[1] += 0.04
    xy_lwrist[1] += 0.04

    # "Light weight": show a point near one wrist (add as 15th marker, bobbing gently)
    weight_wrist = (np.array(xy_rwrist)+np.array(xy_lwrist))/2
    weight = weight_wrist + [0, -0.06 + 0.01*np.sin(2*phase)]  # floats below hand, swings with the gait

    points = np.array([
        xy_head,
        xy_rshoulder, xy_lshoulder,
        xy_relbow, xy_lelbow,
        xy_rwrist, xy_lwrist,
        xy_pelvis,
        xy_rhip, xy_lhip,
        xy_rknee, xy_lknee,
        xy_rankle, xy_lankle,
        weight
    ])
    return points

# Setup matplotlib animation
fig, ax = plt.subplots(figsize=(3, 6))
ax.set_facecolor('black')
plt.axis('off')

scat = ax.scatter([], [], s=48, color='white', edgecolor='none')
ax.set_xlim(0.10, 0.90)
ax.set_ylim(0.0, 1.1)
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

def init():
    scat.set_offsets(np.zeros((NUM_POINTS, 2)))
    return scat,

def animate(frame):
    t = frame / 60.0  # time in seconds
    tphase = (t * 1.60) % 1.0  # running cycle, ~1.6 Hz
    pts = get_skeleton_frame(tphase)
    scat.set_offsets(pts)
    return scat,

ani = animation.FuncAnimation(
    fig, animate, frames=180, interval=16, blit=True, init_func=init, repeat=True
)

plt.show()
