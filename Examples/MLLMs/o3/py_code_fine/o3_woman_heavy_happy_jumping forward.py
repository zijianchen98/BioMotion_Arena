
"""
Biological-motion: heavy happy woman – jumping forward
15 point–light stimulus, white on black
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------------------- skeleton (relative coordinates) -------------------- #
# joint order (15):
# 0 head, 1 L_sh, 2 R_sh, 3 L_elb, 4 R_elb, 5 L_wri, 6 R_wri,
# 7 spine, 8 pelvis,
# 9 L_hip, 10 R_hip, 11 L_knee, 12 R_knee, 13 L_ank, 14 R_ank

# “extended / flight” posture (standing, arms up)
extended = np.array([
    [0.0,  0.80],          # head
    [-0.25, 0.60], [0.25, 0.60],          # shoulders
    [-0.40, 0.45], [0.40, 0.45],          # elbows
    [-0.50, 0.60], [0.50, 0.60],          # wrists (arms up)
    [0.0,  0.40],                          # spine / lower chest
    [0.0,  0.00],                          # pelvis / hip-centre (root)
    [-0.20, 0.00], [0.20, 0.00],           # hips
    [-0.20, -0.45], [0.20, -0.45],         # knees
    [-0.20, -0.90], [0.20, -0.90]          # ankles
])

# “crouched / squat” posture (arms down – preparing / landing)
crouched = np.array([
    [0.0,  0.70],          # head
    [-0.25, 0.50], [0.25, 0.50],           # shoulders
    [-0.35, 0.30], [0.35, 0.30],           # elbows
    [-0.35, 0.10], [0.35, 0.10],           # wrists (arms down)
    [0.0,  0.30],                           # spine
    [0.0,  0.00],                           # pelvis (root)
    [-0.20, 0.00], [0.20, 0.00],            # hips
    [-0.25, -0.25], [0.25, -0.25],          # knees (flexed)
    [-0.25, -0.60], [0.25, -0.60]           # ankles
])

# ----------------------------- time parameters ------------------------------ #
FPS        = 30
DURATION   = 2.0                        # seconds
FRAMES     = int(FPS * DURATION)
times      = np.linspace(0, DURATION, FRAMES)

# ------------------------- root trajectory functions ------------------------ #
def root_x(t):
    """
    Horizontal motion: no translation while crouching,
    then forward during flight, small extra slide after landing.
    """
    if t < 0.5:           # preparation & take-off
        return 0.0
    elif t < 1.5:         # flight (1 second) – constant horizontal velocity
        return 1.0 * (t - 0.5)
    else:                 # after landing – short slide/settle
        return 1.0 + 0.5 * (t - 1.5)

def root_y(t):
    """
    Vertical motion – piece-wise:
    crouch down, take-off, projectile flight, landing crouch, recover.
    """
    if t < 0.3:                         # crouch
        return -0.3 * (t / 0.3)
    elif t < 0.5:                       # push / take-off back to y=0
        return -0.3 + 0.3 * (t - 0.3) / 0.2
    elif t < 1.5:                       # flight – projectile (vy0=2, g=4)
        tau = t - 0.5
        return 2.0 * tau - 2.0 * tau ** 2
    elif t < 1.7:                       # landing compression
        return 0.0 - 0.2 * (t - 1.5) / 0.2
    else:                               # recover to stand
        return -0.2 + 0.2 * (t - 1.7) / 0.3

# ------------------ posture weight (crouched ⇄ extended) -------------------- #
def crouch_weight(t):
    """
    1.0 = fully crouched
    0.0 = fully extended
    """
    if t < 0.3:            # initial crouch
        return 1.0
    elif t < 0.5:          # transition to extension
        return 1.0 - (t - 0.3) / 0.2
    elif t < 1.5:          # flight (extended)
        return 0.0
    elif t < 1.7:          # landing crouch
        return (t - 1.5) / 0.2
    else:                  # recover to standing (extended)
        return 1.0 - (t - 1.7) / 0.3

# ------------------------------ animation ----------------------------------- #
fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.set_xlim(-1.0, 2.0)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.axis('off')

# scatter for 15 points
scat = ax.scatter(
    np.zeros(15), np.zeros(15),
    s=60, c='white', edgecolors='none'
)

def animate(frame_idx):
    t = times[frame_idx]
    w = crouch_weight(t)                     # 0..1
    # interpolate joint positions (relative to pelvis)
    rel = extended * (1 - w) + crouched * w
    # global translation of the pelvis/root
    root = np.array([root_x(t), root_y(t)])
    global_pos = rel + root
    scat.set_offsets(global_pos)
    return scat,

ani = FuncAnimation(fig, animate, frames=FRAMES, interval=1000/FPS, blit=True)

plt.show()
