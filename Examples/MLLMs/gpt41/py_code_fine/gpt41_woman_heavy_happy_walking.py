
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Point order: (conventional 15 marker set)
POINTS = [
    "Head",
    "Right Shoulder", "Left Shoulder",
    "Right Elbow", "Left Elbow",
    "Right Wrist", "Left Wrist",
    "Chest",
    "Right Hip", "Left Hip",
    "Right Knee", "Left Knee",
    "Right Ankle", "Left Ankle",
    "Pelvis",
]

# Body segment proportions (rough, but enhances realism)
S = {
    "head_height": 0.12,
    "shoulder_width": 0.22,
    "trunk_height": 0.30,
    "hip_width": 0.20,
    "upper_arm": 0.17,
    "lower_arm": 0.15,
    "upper_leg": 0.23,
    "lower_leg": 0.22,
    "pelvis_offset": 0.07,
}

def walk_cycle(t):
    """Generate 3D coordinates of 15 markers for a walking woman (carrying heavy weight) at phase t (in [0, 1])"""
    # Center of mass trajectory (walking, vertical bobbing, forward motion)
    stride = 0.20   # forward/back step amplitude
    height = 1.0    # "height" at pelvis
    sway = 0.04     # side-to-side trunk/hips

    # Simulate a "heavy" walk: reduce arm swing, trunk leans forward
    forward_lean = 0.09

    # Walking cycle phase (0-2pi)
    phase = 2 * np.pi * t

    # Pelvis: moves along x
    x_pelvis = stride * np.sin(phase)
    y_pelvis = height + 0.04 * np.cos(2*phase)
    z_pelvis = 0.0 + sway * np.sin(phase)

    # Hips
    z_hip_r = z_pelvis - S["hip_width"]/2
    z_hip_l = z_pelvis + S["hip_width"]/2
    y_hip_r = y_pelvis - S["pelvis_offset"]/2
    y_hip_l = y_pelvis - S["pelvis_offset"]/2

    # Spine upward
    y_chest = y_pelvis + S["trunk_height"]
    z_chest = z_pelvis

    y_shoulder = y_chest + S["head_height"]/2
    z_shoulder_r = z_chest - S["shoulder_width"]/2
    z_shoulder_l = z_chest + S["shoulder_width"]/2

    # Head: just above chest
    y_head = y_shoulder + S["head_height"]/1.5
    x_head = x_pelvis + forward_lean # small lean
    z_head = z_chest

    # Arms (reduced swing - carrying heavy)
    arm_phase = phase + np.pi
    right_arm_swing = 0.10 * np.sin(arm_phase)   # small swing
    left_arm_swing  = 0.10 * np.sin(arm_phase + np.pi)
    # Arms held closer to body
    right_shoulder = (x_pelvis + forward_lean, y_shoulder, z_shoulder_r)
    left_shoulder  = (x_pelvis + forward_lean, y_shoulder, z_shoulder_l)

    # Elbow (hold "weight" near trunk, flexed arm)
    elbow_angle = np.pi/3 - 0.12*np.sin(arm_phase)
    upper_arm = S["upper_arm"] * 0.82  # flexed
    right_elbow = (
        right_shoulder[0] + upper_arm * np.sin(elbow_angle),
        right_shoulder[1] - upper_arm * np.cos(elbow_angle),
        right_shoulder[2] - 0.02
    )
    left_elbow = (
        left_shoulder[0] + upper_arm * np.sin(elbow_angle),
        left_shoulder[1] - upper_arm * np.cos(elbow_angle),
        left_shoulder[2] + 0.02
    )

    # Wrists (rounded near body, "carrying" the weight)
    lower_arm = S["lower_arm"] * 0.94  # not fully extended
    right_wrist = (
        right_elbow[0] + lower_arm * np.sin(elbow_angle + 0.2),
        right_elbow[1] - lower_arm * np.cos(elbow_angle + 0.2),
        right_elbow[2] - 0.01
    )
    left_wrist = (
        left_elbow[0] + lower_arm * np.sin(elbow_angle + 0.2),
        left_elbow[1] - lower_arm * np.cos(elbow_angle + 0.2),
        left_elbow[2] + 0.01
    )

    # Legs: counter-swing
    leg_phase = phase
    hip_right = (x_pelvis, y_hip_r, z_hip_r)
    hip_left  = (x_pelvis, y_hip_l, z_hip_l)
    # Right leg forward half the cycle, left other half
    right_leg_swing = 0.13 * np.sin(leg_phase)
    left_leg_swing  = 0.13 * np.sin(leg_phase + np.pi)
    # Slight knee bend always, more when lifting
    knee_bend_r = np.pi/16 + 0.29 * np.maximum(np.sin(leg_phase), 0)
    knee_bend_l = np.pi/16 + 0.29 * np.maximum(np.sin(leg_phase + np.pi), 0)

    upper_leg = S["upper_leg"]
    lower_leg = S["lower_leg"]

    # Knees
    knee_r = (
        hip_right[0] + upper_leg * np.sin(knee_bend_r + right_leg_swing),
        hip_right[1] - upper_leg * np.cos(knee_bend_r + right_leg_swing),
        hip_right[2]
    )
    knee_l = (
        hip_left[0] + upper_leg * np.sin(knee_bend_l + left_leg_swing),
        hip_left[1] - upper_leg * np.cos(knee_bend_l + left_leg_swing),
        hip_left[2]
    )

    # Ankles - under knee
    ankle_r = (
        knee_r[0] + lower_leg * np.sin(knee_bend_r + right_leg_swing + 0.12),
        knee_r[1] - lower_leg * np.cos(knee_bend_r + right_leg_swing + 0.12),
        knee_r[2]
    )
    ankle_l = (
        knee_l[0] + lower_leg * np.sin(knee_bend_l + left_leg_swing + 0.12),
        knee_l[1] - lower_leg * np.cos(knee_bend_l + left_leg_swing + 0.12),
        knee_l[2]
    )

    # Now assemble all points
    coords = [
        # 0 Head
        (x_head, y_head, z_head),
        # 1 Right Shoulder
        right_shoulder,
        # 2 Left Shoulder
        left_shoulder,
        # 3 Right Elbow
        right_elbow,
        # 4 Left Elbow
        left_elbow,
        # 5 Right Wrist
        right_wrist,
        # 6 Left Wrist
        left_wrist,
        # 7 Chest (just under neck)
        (x_pelvis + forward_lean, y_chest, z_chest),
        # 8 Right Hip
        hip_right,
        # 9 Left Hip
        hip_left,
        # 10 Right Knee
        knee_r,
        # 11 Left Knee
        knee_l,
        # 12 Right Ankle
        ankle_r,
        # 13 Left Ankle
        ankle_l,
        # 14 Pelvis center
        (x_pelvis, y_pelvis, z_pelvis)
    ]
    return np.array(coords)

def project_orthographic(coords3d, azim=0.0, elev=0.0):
    """Project 3D to 2D (orthographic), with azimuth and elevation angles (in radians)."""
    # Construct rotation matrix
    # Rotations: first around Y (azim), then around X (elev)
    Ry = np.array([
        [np.cos(azim), 0, np.sin(azim)],
        [0, 1, 0],
        [-np.sin(azim), 0, np.cos(azim)]
    ])
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(elev), -np.sin(elev)],
        [0, np.sin(elev), np.cos(elev)]
    ])
    rot = Rx @ Ry
    coords3d = coords3d @ rot.T
    # Orthographic projection: x, y (vertical), ignore z
    return coords3d[:, [0, 1]]

# Animation parameters
N_FRAMES = 60
DURATION = 2.2   # seconds per cycle (slow = "heavy walk")

# Prepare animation: precompute all frames
all_frames = []
for fi in range(N_FRAMES):
    t = fi / N_FRAMES
    coords3d = walk_cycle(t)
    # Slightly from the front & above
    pts2d = project_orthographic(coords3d, azim=0.12, elev=0.12)
    all_frames.append(pts2d)

# Matplotlib setup: black bg, white points
fig, ax = plt.subplots(figsize=(3.5, 7))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

scat = ax.scatter([], [], s=45, color="white")
ax.set_xlim(-0.35, 0.35)
ax.set_ylim(0.6, 1.7)
ax.set_aspect('equal')
plt.axis('off')

def init():
    scat.set_offsets([])
    return scat,

def animate(i):
    pts = all_frames[i % N_FRAMES]
    scat.set_offsets(pts)
    return scat,

ani = animation.FuncAnimation(
    fig, animate, frames=N_FRAMES, interval=1000*DURATION/N_FRAMES,
    init_func=init, blit=True, repeat=True
)

plt.show()
