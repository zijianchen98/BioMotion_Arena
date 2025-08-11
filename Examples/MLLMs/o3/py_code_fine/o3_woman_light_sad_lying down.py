
"""
Point–light biological–motion stimulus
15 white dots (joints) against a black background.
Action: a sad, light-weight woman lying down
         – from standing to supine, followed by subtle “breathing”.
Author: ChatGPT
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import rcParams

# ------------- configuration -------------------------------------------------
FPS            = 30                  # frames-per-second
SEC_STAND2LAY  = 3                   # seconds: standing → lying
SEC_BREATH     = 3                   # seconds: breathing while supine
N_FRAMES       = int(FPS * (SEC_STAND2LAY + SEC_BREATH))
DOT_SIZE       = 60                  # scatter marker size
FIGSIZE        = (6, 6)              # inches
# -----------------------------------------------------------------------------

# ---- helper (easing) --------------------------------------------------------
def smoothstep(t: float) -> float:
    """Smoothstep easing (0→1)."""
    return t * t * (3 - 2 * t)

# ---- skeleton model (15 joints) --------------------------------------------
JOINTS = [
    "head",
    "neck",
    "l_shoulder",
    "r_shoulder",
    "l_elbow",
    "r_elbow",
    "l_wrist",
    "r_wrist",
    "spine",
    "l_hip",
    "r_hip",
    "l_knee",
    "r_knee",
    "l_ankle",
    "r_ankle",
]

# Standing pose (x,y) coordinates
# units: arbitrary; origin roughly at feet mid-point
STAND = {
    "head":       (0.0, 7.2),
    "neck":       (0.0, 6.2),
    "l_shoulder": (-1.2, 6.0),
    "r_shoulder": ( 1.2, 6.0),
    "l_elbow":    (-1.6, 4.7),
    "r_elbow":    ( 1.6, 4.7),
    "l_wrist":    (-1.4, 3.3),
    "r_wrist":    ( 1.4, 3.3),
    "spine":      (0.0, 4.8),
    "l_hip":      (-0.6, 4.0),
    "r_hip":      ( 0.6, 4.0),
    "l_knee":     (-0.6, 2.0),
    "r_knee":     ( 0.6, 2.0),
    "l_ankle":    (-0.6, 0.0),
    "r_ankle":    ( 0.6, 0.0),
}

# Supine (lying on back) pose (coordinates)
# Rotated 90° clockwise, then shifted downward a bit.
SUPINE = {
    "head":       ( 6.8, 2.0),
    "neck":       ( 5.8, 2.0),
    "l_shoulder": ( 5.6, 0.8),
    "r_shoulder": ( 5.6, 3.2),
    "l_elbow":    ( 4.3, 0.4),
    "r_elbow":    ( 4.3, 3.6),
    "l_wrist":    ( 3.0, 0.6),
    "r_wrist":    ( 3.0, 3.4),
    "spine":      ( 4.8, 2.0),
    "l_hip":      ( 3.8, 1.2),
    "r_hip":      ( 3.8, 2.8),
    "l_knee":     ( 2.0, 1.2),
    "r_knee":     ( 2.0, 2.8),
    "l_ankle":    ( 0.0, 1.2),
    "r_ankle":    ( 0.0, 2.8),
}

# Convert skeleton dict to ordered numpy arrays
def dict_to_array(d):
    arr = np.zeros((len(JOINTS), 2))
    for i, j in enumerate(JOINTS):
        arr[i] = d[j]
    return arr

STAND_ARR  = dict_to_array(STAND)
SUPINE_ARR = dict_to_array(SUPINE)

# ---- animation generation ---------------------------------------------------
rcParams['figure.facecolor'] = 'black'

fig, ax = plt.subplots(figsize=FIGSIZE)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-2, 8)
ax.set_ylim(-1, 8)
ax.axis('off')

scatter = ax.scatter(
    STAND_ARR[:, 0],
    STAND_ARR[:, 1],
    c='white',
    s=DOT_SIZE,
    edgecolors='none'
)

def animate(frame):
    # 0 … FRA_STAND2LAY-1  => transition
    # remaining            => breathing (supine + breathing motion)
    if frame < FPS * SEC_STAND2LAY:
        # Transition phase
        t = frame / (FPS * SEC_STAND2LAY - 1)
        w = smoothstep(t)          # easing weight
        coords = (1 - w) * STAND_ARR + w * SUPINE_ARR
    else:
        # Breathing phase
        breath_frame = frame - FPS * SEC_STAND2LAY
        t = breath_frame / FPS      # seconds into breathing
        # small sinusoidal vertical movement of chest/spine/head (sad, subtle)
        breath_offset = 0.08 * np.sin(2 * np.pi * 0.33 * t)    # amplitude
        coords = SUPINE_ARR.copy()
        chest_idx = JOINTS.index("spine")
        neck_idx  = JOINTS.index("neck")
        head_idx  = JOINTS.index("head")
        coords[[chest_idx, neck_idx, head_idx], 1] += breath_offset

    scatter.set_offsets(coords)
    return scatter,

ani = anim.FuncAnimation(
    fig,
    animate,
    frames=N_FRAMES,
    interval=1000 / FPS,
    blit=True,
    repeat=True,
)

plt.show()
