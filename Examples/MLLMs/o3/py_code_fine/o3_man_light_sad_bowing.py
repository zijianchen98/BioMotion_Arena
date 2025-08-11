
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------------------------------------
#  Point-light bowing animation (15 white dots on black)
# -----------------------------------------------------------

# Joint labels (for reference only – the order is important)
JOINTS = [
    "head", "neck",
    "left_shoulder",  "right_shoulder",
    "left_elbow",     "right_elbow",
    "left_hand",      "right_hand",
    "pelvis",
    "left_hip",       "right_hip",
    "left_knee",      "right_knee",
    "left_foot",      "right_foot"
]

# Static, upright reference pose (x, y) for every joint
BASE_POSE = np.array([
    [ 0.0,  3.0],   # head
    [ 0.0,  2.0],   # neck
    [-1.0,  2.0],   # left_shoulder
    [ 1.0,  2.0],   # right_shoulder
    [-1.2,  1.0],   # left_elbow
    [ 1.2,  1.0],   # right_elbow
    [-1.2,  0.0],   # left_hand
    [ 1.2,  0.0],   # right_hand
    [ 0.0,  0.0],   # pelvis (rotation pivot)
    [-0.5,  0.0],   # left_hip
    [ 0.5,  0.0],   # right_hip
    [-0.5, -2.0],   # left_knee
    [ 0.5, -2.0],   # right_knee
    [-0.5, -4.0],   # left_foot
    [ 0.5, -4.0]    # right_foot
], dtype=float)

# Indices of joints that belong to the torso/arms and thus rotate when bowing
UPPER_BODY_IDX = np.array([
    0, 1, 2, 3, 4, 5, 6, 7     # all joints above (and including) shoulders
])

PELVIS_IDX = 8  # rotation pivot

# Pre-compute vectors from pelvis to every upper-body joint (in upright pose)
PELVIS_POS = BASE_POSE[PELVIS_IDX]
VECTORS_FROM_PELVIS = BASE_POSE[UPPER_BODY_IDX] - PELVIS_POS

# Animation parameters
TOTAL_FRAMES = 120          # one full bow cycle
BOW_AMP_DEG  = 45           # maximum forward lean
INTERVAL_MS  = 30           # time between frames (controls playback speed)

# Prepare plot
fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-4, 4)
ax.set_ylim(-5, 4)
ax.axis("off")

# Scatter plot for the 15 points
dots = ax.scatter(BASE_POSE[:, 0],
                  BASE_POSE[:, 1],
                  s=60, c="white")

# ---------------- Animation update function ----------------
def update(frame):
    """
    Compute new joint positions for the given frame and
    update the scatter plot accordingly.
    """
    # Progress through one full bow (0‒1)
    cycle_pos = frame / (TOTAL_FRAMES - 1)
    
    # Bow angle goes 0 → max → 0 (single smooth bow)
    # sin(pi * t) yields 0→1→0
    angle_deg = BOW_AMP_DEG * np.sin(np.pi * cycle_pos)
    angle_rad = np.deg2rad(-angle_deg)  # negative = lean forward
    
    # Rotation matrix (2D)
    c, s = np.cos(angle_rad), np.sin(angle_rad)
    R = np.array([[c, -s],
                  [s,  c]])
    
    # Start with the original pose
    new_pose = BASE_POSE.copy()
    
    # Rotate upper-body joints around the pelvis
    rotated = (R @ VECTORS_FROM_PELVIS.T).T + PELVIS_POS
    new_pose[UPPER_BODY_IDX] = rotated
    
    # Update the scatter plot
    dots.set_offsets(new_pose)
    return dots,

# Create animation
ani = FuncAnimation(fig,
                    update,
                    frames=TOTAL_FRAMES,
                    interval=INTERVAL_MS,
                    blit=True)

plt.show()
