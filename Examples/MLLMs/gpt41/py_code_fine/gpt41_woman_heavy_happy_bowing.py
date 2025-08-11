
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the human body model (15 keypoints)
# (head, shoulders, elbows, wrists, hips, knees, ankles, key bones)
JOINTS = [
    'Head',
    'Neck',
    'RShoulder', 'RElbow', 'RWrist',
    'LShoulder', 'LElbow', 'LWrist',
    'MidHip',
    'RHip', 'RKnee', 'RAnkle',
    'LHip', 'LKnee', 'LAnkle'
]

# Indices for connections (viz. human skeleton)
SKELETON = [
    (0, 1),                # Head-Neck
    (1, 2), (2, 3), (3, 4),    # R arm
    (1, 5), (5, 6), (6, 7),    # L arm
    (1, 8),                    # Neck-MidHip
    (8, 9), (9,10), (10,11),   # R leg
    (8,12), (12,13), (13,14),  # L leg
]

# Happy facial expression: can be hinted by arc for mouth in the postural depiction;
# but since only points are allowed, will keep as head dot (for happy, maybe head slightly up)
# Heavy weight: body is thickset and possibly limbs "wider" positioned.

# Animation parameters
FPS = 30
DURATION = 2.0    # seconds for one bow
TOTAL_FRAMES = int(FPS * DURATION)
LOOPS = 2         # show two b/ws

# Basic anthropomorphic sizes and proportions (in arbitrary units)
SCALE = 1.7
HEIGHT = 7.0 * SCALE
SHOULDER_WIDTH = 1.6 * SCALE
PELVIS_WIDTH = 1.1 * SCALE
HIP_HEIGHT = 2.0 * SCALE
NECK_H = HEIGHT - 0.8 * SCALE
SHOULDER_H = HEIGHT - 1.5 * SCALE
ELBOW_H = HEIGHT - 2.2 * SCALE
WRIST_H = HEIGHT - 3.4 * SCALE
MIDHIP_H = HIP_HEIGHT
KNEE_H = HIP_HEIGHT - 1.5 * SCALE
ANKLE_H = 0.1 * SCALE

# For "heavy", widen shoulders/hips/knees/ankles a bit, increase thickness
WEIGHT_WIDEN = 0.12 * SCALE

def get_pose(bow_phase):
    """Return 15x2 array of points representing the pose at normalized 'bow phase' [0,1]"""
    # bow_phase: 0=head up, 0.5=max bow down, 1=head up (cycle)

    # Lateral oscillation for happy gesture
    sway = 0.08 * SCALE * np.sin(np.pi * bow_phase)
    
    # Bowing angle: 0 to max, then back
    bow_angle = np.deg2rad(0 + 60 * np.sin(np.pi * bow_phase)) # max 60 deg forward

    # Head slightly up at start/end (happy), chin in on bow
    head_offset = 0.10 * SCALE * np.cos(np.pi * bow_phase)
    
    # Arms: Extend down then forward a bit, or swing as if bowing courteously
    arm_lift = 0.30 * SCALE * np.sin(np.pi * bow_phase)
    hand_fw = 0.20 * SCALE * np.sin(np.pi * bow_phase)
    arm_swing = -0.20 * SCALE * np.sin(np.pi * bow_phase)

    # Hip and knee flexion for realism
    hip_fw = 0.24 * SCALE * np.sin(np.pi * bow_phase)          # pelvis shifts fw when bowing
    knee_bend = 0.18 * SCALE * np.sin(np.pi * bow_phase)
    ankle_move = 0.14 * SCALE * np.sin(np.pi * bow_phase)
    
    # Shoulder join
    neck = np.array([0.0, NECK_H])
    head = neck + [0.0, 0.55 * SCALE + head_offset]
    
    # Wide happy shoulders (heavy):
    r_shoulder = neck + [SHOULDER_WIDTH/2 + WEIGHT_WIDEN, -0.23 * SCALE]
    l_shoulder = neck + [-SHOULDER_WIDTH/2 - WEIGHT_WIDEN, -0.23 * SCALE]

    # Arms (slightly thick-set, arms out a bit)
    r_elbow = r_shoulder + [0.39 * SCALE + WEIGHT_WIDEN, -0.60 * SCALE + arm_lift]
    l_elbow = l_shoulder + [-0.39 * SCALE - WEIGHT_WIDEN, -0.60 * SCALE + arm_lift]

    r_wrist = r_elbow + [0.32 * SCALE + hand_fw, -0.80*SCALE + arm_swing]
    l_wrist = l_elbow + [-0.32 * SCALE - hand_fw, -0.80*SCALE - arm_swing]

    # Mid-hip, hips
    midhip = np.array([0.0 + sway, MIDHIP_H])
    r_hip = midhip + [PELVIS_WIDTH/2 + WEIGHT_WIDEN, 0.0]
    l_hip = midhip + [-PELVIS_WIDTH/2 - WEIGHT_WIDEN, 0.0]

    # Knee bends and forward motion:
    r_knee = r_hip + [0.11 * SCALE, -1.40*SCALE + knee_bend]
    l_knee = l_hip + [-0.11 * SCALE, -1.40*SCALE + knee_bend]

    r_ankle = r_knee + [0.12 * SCALE, -1.20*SCALE + ankle_move]
    l_ankle = l_knee + [-0.12 * SCALE, -1.20*SCALE + ankle_move]

    # Apply bow transform: rotate upper body and arms about midhip
    def rotate_about(p, center, ang):
        d = p - center
        rot = np.array([[np.cos(ang), -np.sin(ang)],
                        [np.sin(ang),  np.cos(ang)]])
        return center + rot @ d

    # Rotate neck, head, shoulders, arms about midhip
    upper_joints_idx = [0, 1, 2, 3, 4, 5, 6, 7]
    points = np.array([
        head,
        neck,
        r_shoulder, r_elbow, r_wrist,
        l_shoulder, l_elbow, l_wrist,
        midhip,
        r_hip, r_knee, r_ankle,
        l_hip, l_knee, l_ankle
    ])
    for idx in upper_joints_idx:
        points[idx] = rotate_about(points[idx], midhip, -bow_angle)
    
    # Also shift forward (projecting heavy weight and balance)
    bow_displacement = np.array([hip_fw * np.sin(bow_angle), 0.0])
    points[:8] += bow_displacement

    # Vertical shift to keep feet on ground during bow
    min_y = min(points[11,1], points[14,1])
    dy = ANKLE_H - min_y
    points[:,1] += dy
    
    return points

# Animation setup

fig, ax = plt.subplots(figsize=(3.5, 7), facecolor='black')
ax.set_facecolor('black')
plt.axis('off')
ax.set_xlim(-3*SCALE, 3*SCALE)
ax.set_ylim(-0.1*SCALE, HEIGHT+0.7*SCALE)

# Draw 15 points
pts, = plt.plot([], [], 'wo', ms=8)
# Optionally, show bones/skeleton faintly
# for s in SKELETON:
#     ax.plot([], [], color="gray", alpha=0.2, lw=2)

def init():
    pts.set_data([], [])
    return (pts,)

def animate(i):
    t_norm = ((i % TOTAL_FRAMES) / (TOTAL_FRAMES - 1))
    # Cycle forward and back: 0->1->0->1...
    t_cycle = 2 * t_norm if t_norm < 0.5 else 2 * (1-t_norm)
    points = get_pose(t_norm)  # or t_cycle for bow up and down
    xs, ys = points[:,0], points[:,1]
    pts.set_data(xs, ys)
    return (pts,)

ani = animation.FuncAnimation(
    fig, animate,
    init_func=init,
    frames=TOTAL_FRAMES*LOOPS,
    interval=1000/FPS, blit=True,
    repeat=True,
)

plt.show()
