
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 15 keypoints: head, neck, l/r shoulder, l/r elbow, l/r wrist,
# torso, l/r hip, l/r knee, l/r ankle
POINTS = [
    "head",      # 0
    "neck",      # 1
    "r_shoulder",# 2
    "l_shoulder",# 3
    "r_elbow",   # 4
    "l_elbow",   # 5
    "r_wrist",   # 6
    "l_wrist",   # 7
    "torso",     # 8
    "r_hip",     # 9
    "l_hip",     # 10
    "r_knee",    # 11
    "l_knee",    # 12
    "r_ankle",   # 13
    "l_ankle",   # 14
]

def base_pose():
    """Returns the initial upright pose (x, y) for each joint."""
    # Y increases upward, X is horizontal.
    # Units are arbitrary, made to look appealing for display.
    X = np.zeros(15)
    Y = np.zeros(15)
    # Torso center
    X[8], Y[8] = 0, 0
    # Neck and head
    X[1], Y[1] = 0, 1.5
    X[0], Y[0] = 0, 2.0
    # Shoulders
    X[2], Y[2] = 0.35, 1.5
    X[3], Y[3] = -0.35, 1.5
    # Elbows
    X[4], Y[4] = 0.55, 1.0
    X[5], Y[5] = -0.55, 1.0
    # Wrists
    X[6], Y[6] = 0.7, 0.5
    X[7], Y[7] = -0.7, 0.5
    # Hips
    X[9], Y[9] = 0.22, 0.0
    X[10], Y[10] = -0.22, 0.0
    # Knees
    X[11], Y[11] = 0.22, -0.65
    X[12], Y[12] = -0.22, -0.65
    # Ankles
    X[13], Y[13] = 0.22, -1.3
    X[14], Y[14] = -0.22, -1.3
    return np.stack([X, Y], axis=-1)

def bow_pose(f):
    """
    Returns pose at fraction f of the bow movement (0..1..0; bowing down and up).
    Bow is parameterized as a time-varying flexion at the hip, and compensation at knees and neck.
    """
    p = base_pose()

    # Bowing amplitude (radians)
    max_angle = np.pi/4  # Max bend = 45 degrees
    # Swing from 0 to max_angle and back to 0 (f from 0->1->0)
    angle = max_angle * np.sin(np.pi * f)
    # Small knee flexion during bow
    max_knee = np.pi/16
    knee_angle = max_knee * np.sin(np.pi * f)
    # Small neck flexion
    neck_bend = max_angle * 0.15 * np.sin(np.pi * f)

    # ----- Bending at hip -----
    # Translation of upper body, wrt hip center (move all above hips)
    hip_center = (p[9]+p[10])/2
    torso_vec = p[1] - hip_center
    sh_r = p[2] - hip_center
    sh_l = p[3] - hip_center
    head_vec = p[0] - hip_center

    # 2D rotation matrix
    ca, sa = np.cos(-angle), np.sin(-angle)
    R = np.array([[ca, -sa], [sa, ca]])

    # Rotate: head, neck, shoulders, elbows, wrists, torso
    for idx in [0,1,2,3,4,5,6,7,8]:
        v = p[idx] - hip_center
        p[idx] = hip_center + R@v

    # -------- Shoulder/arm adjustment: Keep arms hanging in front natural ---------
    # Arms move a little (shoulder pitch raises slightly during bow)
    arm_dangle = angle * 0.3
    for sidx, eidx, widx in [(2,4,6),(3,5,7)]:
        shoulder = p[sidx]
        elbow = p[eidx] - shoulder
        wrist = p[widx] - p[eidx]
        # Rotate elbow and wrist slightly to move forearms forwards
        Re = np.array([[np.cos(-arm_dangle), -np.sin(-arm_dangle)],
                       [np.sin(-arm_dangle), np.cos(-arm_dangle)]])
        elb = Re @ elbow
        wrs = Re @ wrist
        p[eidx] = shoulder + elb
        p[widx] = p[eidx] + wrs

    # --------- Add neck flexion ---------
    neck = p[1]
    neck_head = p[0] - neck
    Rn = np.array([[np.cos(-neck_bend), -np.sin(-neck_bend)],
                   [np.sin(-neck_bend), np.cos(-neck_bend)]])
    p[0] = neck + Rn @ neck_head

    # --------- Add knee flexion ---------
    for hip_idx, knee_idx, ankle_idx in [(9,11,13),(10,12,14)]:
        # Knee rotates forward slightly
        hip = p[hip_idx]
        knee = p[knee_idx] - hip
        ankle = p[ankle_idx] - p[knee_idx]
        Rk = np.array([[np.cos(knee_angle), -np.sin(knee_angle)],
                       [np.sin(knee_angle), np.cos(knee_angle)]])
        knee_v = Rk @ knee
        ankle_v = Rk @ ankle
        p[knee_idx] = hip + knee_v
        p[ankle_idx] = p[knee_idx] + ankle_v

    return p

# -------------------- Animation Code --------------------
fig, ax = plt.subplots(figsize=(3, 6))
ax.set_facecolor("black")
plt.axis("off")

lines = []

# For each of the 15 points, a plot object:
scat = ax.scatter([], [], s=48, color="white", edgecolor="white")

# Set fixed limits that resemble the original image style
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-2.0, 2.3)

# For anatomical lines (for better perception, optional; can comment if only dots wanted)
skeleton = [
    (0, 1), (1, 8), # head-neck-torso
    (1, 2), (1, 3), # neck-shoulders
    (2, 4), (4, 6), # r shoulder->elbow->wrist
    (3, 5), (5, 7), # l shoulder->elbow->wrist
    (8, 9), (8, 10), # torso->hips
    (9, 11), (11, 13), # r hip->knee->ankle
    (10, 12), (12, 14), # l hip->knee->ankle
]

skel_lines = []
for (a,b) in skeleton:
    l, = ax.plot([], [], color="white", lw=1.2, alpha=0.11, zorder=0)
    skel_lines.append(l)

# 120 frames: 60 per bow down, 60 per bow up, ~2 seconds
frames_total = 120

def update(frame):
    # Go bowing down (0..60) then up (61..119)
    if frame < frames_total//2:
        f = frame/(frames_total//2-1)
    else:
        f = 1 - (frame-frames_total//2)/(frames_total//2-1)
    pts = bow_pose(f)

    # Update dots
    scat.set_offsets(pts)
    # Skeleton (for visual clarity - faint lines)
    for line, (a, b) in zip(skel_lines, skeleton):
        line.set_data([pts[a,0], pts[b,0]], [pts[a,1], pts[b,1]])
    return [scat]+skel_lines

ani = animation.FuncAnimation(
    fig, update, frames=frames_total, interval=1000/60, blit=True
)

plt.show()
