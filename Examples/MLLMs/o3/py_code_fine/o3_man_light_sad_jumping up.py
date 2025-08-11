
"""
Point–light biological–motion stimulus
--------------------------------------
15 white point–lights of a light-weight “stick-figure” that repeatedly jumps
upwards against a solid black background.  The animation is rendered with
matplotlib and designed to be smooth, coherent and biomechanically plausible
(very simplified, of course).

Written for Python ≥ 3.7
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------------------------------------------------------
# Skeleton layout (15 joints) in an upright standing pose
# ------------------------------------------------------------------
#  0  head
#  1  left shoulder   2  right shoulder
#  3  left elbow      4  right elbow
#  5  left wrist      6  right wrist
#  7  pelvis / hip centre
#  8  left hip        9  right hip
# 10  left knee      11  right knee
# 12  left ankle     13  right ankle
# 14  chest (between shoulders and head)

standing_pose = np.array(
    [
        [0.00, 1.80],   # head
        [-0.30, 1.50],  # L-shoulder
        [0.30, 1.50],   # R-shoulder
        [-0.40, 1.05],  # L-elbow
        [0.40, 1.05],   # R-elbow
        [-0.40, 0.60],  # L-wrist
        [0.40, 0.60],   # R-wrist
        [0.00, 1.00],   # pelvis
        [-0.18, 0.90],  # L-hip
        [0.18, 0.90],   # R-hip
        [-0.18, 0.50],  # L-knee
        [0.18, 0.50],   # R-knee
        [-0.18, 0.00],  # L-ankle
        [0.18, 0.00],   # R-ankle
        [0.00, 1.60],   # chest
    ],
    dtype=float,
)

# Indices for convenience
LEFT = [1, 3, 5, 8, 10, 12]
RIGHT = [2, 4, 6, 9, 11, 13]


def get_pose(phase: float) -> np.ndarray:
    """
    Compute joint coordinates for one animation phase in [0, 1).

    The motion cycle:
      0.00–0.20   crouch down
      0.20–0.25   rapid extension (take-off)
      0.25–0.75   airborne (parabolic flight)
      0.75–0.85   landing, knees flexed
      0.85–1.00   return to upright
    """
    pose = standing_pose.copy()

    # --- Crouch factor -------------------------------------------------------
    if phase < 0.20:                    # going down
        crouch = phase / 0.20
    elif phase < 0.25:                  # take-off (un-crouch quickly)
        crouch = 1.0 - (phase - 0.20) / 0.05
    elif phase < 0.85:                  # airborne / landing (no crouch)
        crouch = 0.0
    else:                               # recovery crouch after landing
        crouch = (phase - 0.85) / 0.15
        crouch = 1.0 - crouch           # goes 1→0

    # Amount the pelvis (and thus body) is lowered during crouch
    crouch_drop = 0.35 * crouch

    # Bend knees & hips sideways/outwards a little while crouched
    knee_side_offset = 0.10 * crouch

    # Apply crouch adjustments
    crouch_mask = np.zeros(len(pose), bool)
    crouch_mask[[7, 8, 9, 10, 11, 14, 0, 1, 2]] = True  # basically torso and thighs
    pose[crouch_mask, 1] -= crouch_drop

    # Move knees forward (x) and down further
    pose[[10, 11], 1] -= 0.15 * crouch
    pose[10, 0] -= knee_side_offset
    pose[11, 0] += knee_side_offset

    # -------------------------------------------------------------------------
    # Jump height (parabolic) and airborne knee tuck
    # -------------------------------------------------------------------------
    jump_height = 0.0
    airborne = False
    if 0.25 <= phase <= 0.75:
        airborne = True
        # Map phase 0.25→0, 0.5→1, 0.75→0
        t = (phase - 0.25) / 0.50        # 0→1
        jump_height = 0.70 * (4 * t * (1 - t))  # simple parabola

    # Shift the entire body up by jump_height
    pose[:, 1] += jump_height

    # While airborne tuck legs a little (knees up, ankles up)
    if airborne:
        tuck = np.sin(np.pi * (phase - 0.25) / 0.50)  # 0→1→0
        lift = 0.25 * tuck
        pose[[10, 11, 12, 13], 1] += lift
        pose[[10, 11], 0] *= 0.8  # knees slightly inward
        pose[[12, 13], 0] *= 0.8  # ankles inward

        # Raise arms up slowly for balance
        arm_raise = 0.3 * tuck
        pose[[3, 4, 5, 6], 1] += arm_raise
        pose[5, 0] -= 0.05 * tuck   # small inward move
        pose[6, 0] += 0.05 * tuck

    # -------------------------------------------------------------------------
    return pose


# ------------------------------------------------------------------
# Graphics / Animation
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Limits chosen so that figure remains centered throughout the jump
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-0.1, 2.6)

# Create scatter plot for 15 white points
scat = ax.scatter(
    standing_pose[:, 0],
    standing_pose[:, 1],
    s=50,
    c='white',
    edgecolors='none',
)

# Number of frames per full cycle
FRAMES = 120


def update(frame):
    phase = (frame % FRAMES) / FRAMES  # 0–1
    joints = get_pose(phase)
    scat.set_offsets(joints)
    return scat,


ani = FuncAnimation(
    fig,
    update,
    frames=FRAMES,
    interval=1000 * 1 / 60,  # ~60 fps
    blit=True,
)

plt.show()
