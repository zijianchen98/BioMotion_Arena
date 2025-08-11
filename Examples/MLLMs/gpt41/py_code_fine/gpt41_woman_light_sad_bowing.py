
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
FPS = 60
DURATION = 2.5  # seconds for one bowing cycle
N_FRAMES = int(FPS * DURATION)
N_POINTS = 15

# Body segment lengths (approximate, normalized units)
L_head = 0.12
L_neck = 0.08
L_trunk = 0.27
L_shoulders = 0.20
L_pelvis = 0.18
L_upperarm = 0.16
L_forearm = 0.15
L_hand = 0.11
L_thigh = 0.23
L_shank = 0.22
L_foot = 0.10

# Marker definitions: (name, parent index, vector to marker in rest pose)
# Parent index: -1 means fixed in the body coordinate system (root)
# The 15 point-lights (using classic biological motion conventions)
MARKERS = [
    # Head and neck
    ('head',      -1, np.array([0, L_head + L_neck + L_trunk + L_pelvis/2])),
    ('neck',      -1, np.array([0, L_neck + L_trunk + L_pelvis/2])),
    # Shoulders
    ('r_shoulder', -1, np.array([-L_shoulders/2, L_trunk + L_pelvis/2])),
    ('l_shoulder', -1, np.array([ L_shoulders/2, L_trunk + L_pelvis/2])),
    # Elbows
    ('r_elbow',    -1, np.array([-L_shoulders/2 - L_upperarm, L_trunk + L_pelvis/2])),
    ('l_elbow',    -1, np.array([ L_shoulders/2 + L_upperarm, L_trunk + L_pelvis/2])),
    # Wrists
    ('r_wrist',    -1, np.array([-L_shoulders/2 - L_upperarm - L_forearm, L_trunk + L_pelvis/2])),
    ('l_wrist',    -1, np.array([ L_shoulders/2 + L_upperarm + L_forearm, L_trunk + L_pelvis/2])),
    # Chest (mid trunk)
    ('chest',      -1, np.array([0, L_trunk/2 + L_pelvis/2])),
    # Pelvis (root)
    ('pelvis',     -1, np.array([0, L_pelvis/2])),

    # Knees
    ('r_knee',     -1, np.array([-L_pelvis/2, -L_thigh + L_pelvis/2])),
    ('l_knee',     -1, np.array([ L_pelvis/2, -L_thigh + L_pelvis/2])),
    # Ankles
    ('r_ankle',    -1, np.array([-L_pelvis/2, -L_thigh - L_shank + L_pelvis/2])),
    ('l_ankle',    -1, np.array([ L_pelvis/2, -L_thigh - L_shank + L_pelvis/2])),
    # Toes
    ('r_toe',      -1, np.array([-L_pelvis/2 + L_foot/2, -L_thigh - L_shank + L_pelvis/2 - 0.02])),
    ('l_toe',      -1, np.array([ L_pelvis/2 - L_foot/2, -L_thigh - L_shank + L_pelvis/2 - 0.02])),
]

assert len(MARKERS) == N_POINTS

# For sad bowing: 
# - Center of mass shifts slightly forward.
# - Torso bends significantly forward.
# - Arms hang down, swing a little.
# - Head is down.
# - Shoulders rounded forward.
# Keyframes: up, halfway, full bow, halfway, up.
def get_pose(t):
    # t in [0, 1], one bowing cycle
    # Define the motion as a smooth bowing with sadness: head/neck/shoulders/upperbody forward, arms hang, knees soften a bit.
    # Bow angle: from 0 to -60deg (negative = forward flexion), back to 0.
    bow_max = np.deg2rad(-60)
    bow = 0.5 * (1 - np.cos(np.pi * t)) * bow_max  # Smooth up-down
    
    # Head nod: extra down
    head_nod = 0.3 * bow
    
    # Shoulders slumping: forward, slight up/down
    shoulder_flex = 0.3 * bow
    shoulder_drop = -0.05 * np.sin(np.pi * t)

    # Arms hang down, slight swing to enhance sadness
    arm_swing = 0.06 * np.sin(2 * np.pi * t + np.pi/3)  # slow swing
    elbow_flex = np.deg2rad(35) + 0.1 * -bow  # arms slightly bent, more flex when bowing

    # Knees bend a little for weight
    knee_bend = 0.14 * np.sin(np.pi * t)

    # Trunk (root) shifts forward a bit as she bows
    trunk_shift = 0.08 * (1 - np.cos(np.pi * t))

    # Compose all marker positions from root
    # Root position (pelvis, in the middle of screen)
    pelvis_xy = np.array([0.0, 0.0])

    # Neck position (from pelvis)
    neck_xy = pelvis_xy + np.array([0, L_pelvis / 2 + L_trunk + L_neck])
    chest_xy = pelvis_xy + np.array([0, L_pelvis / 2 + L_trunk/2])

    # Compute trunk vector (with bow angle, forward bend)
    def rotate(p, theta):
        s, c = np.sin(theta), np.cos(theta)
        return np.dot(np.array([[c, -s], [s, c]]), p)
    
    # Shoulders, chest, neck move forward with trunk
    trunk_theta = bow
    trunk_origin = pelvis_xy + np.array([0, L_pelvis / 2])
    chest_rel = np.array([0, L_trunk/2])
    neck_rel = np.array([0, L_trunk + L_neck])
    chest_xy = trunk_origin + rotate(chest_rel, trunk_theta)
    neck_xy = trunk_origin + rotate(neck_rel, trunk_theta)
    # Head position (more bowing than torso)
    head_origin = trunk_origin + rotate(np.array([0, L_trunk + L_neck]), trunk_theta)
    head_rel = np.array([0, L_head])
    head_xy = head_origin + rotate(head_rel, trunk_theta + head_nod)
    # Shoulders, move forward and slump
    shoulders_span = L_shoulders
    r_shoulder_xy = trunk_origin + rotate(np.array([-shoulders_span/2, L_trunk]), trunk_theta + shoulder_flex)
    l_shoulder_xy = trunk_origin + rotate(np.array([shoulders_span/2, L_trunk]), trunk_theta + shoulder_flex)
    r_shoulder_xy = r_shoulder_xy + np.array([0, shoulder_drop])
    l_shoulder_xy = l_shoulder_xy + np.array([0, shoulder_drop])
    # Elbows (shoulders downward, arms hang)
    r_elbow_rel = np.array([0, -L_upperarm])
    l_elbow_rel = np.array([0, -L_upperarm])
    r_elbow_xy = r_shoulder_xy + rotate(r_elbow_rel, trunk_theta + shoulder_flex + np.pi/12 + arm_swing)
    l_elbow_xy = l_shoulder_xy + rotate(l_elbow_rel, trunk_theta + shoulder_flex - np.pi/12 - arm_swing)
    # Wrists
    r_wrist_rel = np.array([0, -L_forearm])
    l_wrist_rel = np.array([0, -L_forearm])
    r_wrist_xy = r_elbow_xy + rotate(r_wrist_rel, trunk_theta + shoulder_flex + np.pi/12 + arm_swing + elbow_flex)
    l_wrist_xy = l_elbow_xy + rotate(l_wrist_rel, trunk_theta + shoulder_flex - np.pi/12 - arm_swing + elbow_flex)
    # Pelvis marker (slightly below root)
    pelvis_marker_xy = pelvis_xy + np.array([0, 0])
    # Knees: under pelvis --> add slight flexion for weight
    r_hip_xy = pelvis_xy + rotate(np.array([-L_pelvis/2, 0]), 0)
    l_hip_xy = pelvis_xy + rotate(np.array([L_pelvis/2, 0]), 0)
    r_knee_rel = np.array([0, -L_thigh])
    l_knee_rel = np.array([0, -L_thigh])
    r_knee_xy = r_hip_xy + rotate(r_knee_rel, knee_bend)
    l_knee_xy = l_hip_xy + rotate(l_knee_rel, knee_bend)
    # Ankles
    r_ankle_rel = np.array([0, -L_shank])
    l_ankle_rel = np.array([0, -L_shank])
    r_ankle_xy = r_knee_xy + rotate(r_ankle_rel, -0.45 * knee_bend)
    l_ankle_xy = l_knee_xy + rotate(l_ankle_rel, -0.45 * knee_bend)
    # Toes
    r_toe_rel = np.array([L_foot/2, -0.02])
    l_toe_rel = np.array([-L_foot/2, -0.02])
    r_toe_xy = r_ankle_xy + rotate(r_toe_rel, 0)
    l_toe_xy = l_ankle_xy + rotate(l_toe_rel, 0)
    # Now collect all marker positions as per MARKERS order
    marker_dict = {
        'head': head_xy + np.array([trunk_shift, 0]),
        'neck': neck_xy + np.array([trunk_shift, 0]),
        'r_shoulder': r_shoulder_xy + np.array([trunk_shift, 0]),
        'l_shoulder': l_shoulder_xy + np.array([trunk_shift, 0]),
        'r_elbow': r_elbow_xy + np.array([trunk_shift, 0]),
        'l_elbow': l_elbow_xy + np.array([trunk_shift, 0]),
        'r_wrist': r_wrist_xy + np.array([trunk_shift, 0]),
        'l_wrist': l_wrist_xy + np.array([trunk_shift, 0]),
        'chest': chest_xy + np.array([trunk_shift, 0]),
        'pelvis': pelvis_marker_xy + np.array([trunk_shift, 0]),
        'r_knee': r_knee_xy + np.array([trunk_shift, 0]),
        'l_knee': l_knee_xy + np.array([trunk_shift, 0]),
        'r_ankle': r_ankle_xy + np.array([trunk_shift, 0]),
        'l_ankle': l_ankle_xy + np.array([trunk_shift, 0]),
        'r_toe': r_toe_xy + np.array([trunk_shift, 0]),
        'l_toe': l_toe_xy + np.array([trunk_shift, 0]),
    }
    return marker_dict

# Generate all frames
frames = []
for i in range(N_FRAMES):
    t = np.clip(i / (N_FRAMES-1), 0, 1)
    pose = get_pose(t)
    xy_pts = []
    # Respecting the marker order
    marker_names = [m[0] for m in MARKERS]
    for name in marker_names:
        xy_pts.append(pose[name])
    frames.append(np.stack(xy_pts))
frames = np.stack(frames)  # (n_frames, n_markers, 2)

# --- Animation ---
fig, ax = plt.subplots(figsize=(4, 7), facecolor='black')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('black')

# Centered human figure, fit nicely in window.
Y_CENTER = 0.7
Y_RANGE = 1.45
X_RANGE = 0.7
ax.set_xlim(-X_RANGE/2, X_RANGE/2)
ax.set_ylim(-0.05, Y_RANGE)

points, = ax.plot([], [], 'wo', markersize=12)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    frame = frames[i % N_FRAMES]
    x = frame[:, 0]
    y = frame[:, 1] + Y_CENTER  # center vertical
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(
    fig, animate, frames=N_FRAMES, interval=1000/FPS, blit=True, init_func=init
)

plt.show()
