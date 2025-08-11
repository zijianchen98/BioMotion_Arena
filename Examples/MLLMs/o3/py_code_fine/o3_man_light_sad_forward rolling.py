
"""
Point-light biological–motion stimulus
Sad man (light weight) – forward roll (somersault)

Exactly 15 white point-lights on a black background
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ‑-- Parameters --------------------------------------------------------------

N_FRAMES = 120                     # total number of animation frames
FPS       = 30                     # frames-per-second
DPI       = 100                    # resolution for the figure

# phase boundaries (fractions of total duration)
CROUCH_END  = 0.20                 # 0‒20 %   : the actor crouches
ROLL_END    = 0.80                 # 20‒80 %  : the actor performs a forward roll
STAND_END   = 1.00                 # 80‒100 % : the actor stands up again

# horizontal distance covered during the somersault (in data units)
ROLL_TRANSLATION = 2.0


# ‑-- The canonical upright skeleton (15 joints) ------------------------------

# (x , y) positions in **body-centric** coordinates
# ankle-level is y = 0
SKELETON = np.array([
    [ 0.00, 1.70],      #  0 head
    [ 0.00, 1.50],      #  1 neck
    [-0.20, 1.45],      #  2 right shoulder
    [ 0.20, 1.45],      #  3 left  shoulder
    [ 0.00, 1.40],      #  4 sternum / chest
    [-0.35, 1.20],      #  5 right elbow
    [ 0.35, 1.20],      #  6 left  elbow
    [-0.35, 1.00],      #  7 right wrist
    [ 0.35, 1.00],      #  8 left  wrist
    [-0.10, 0.90],      #  9 right hip
    [ 0.10, 0.90],      # 10 left  hip
    [-0.10, 0.45],      # 11 right knee
    [ 0.10, 0.45],      # 12 left  knee
    [-0.10, 0.00],      # 13 right ankle
    [ 0.10, 0.00],      # 14 left  ankle
])


# ‑-- Helper: create one animation frame -------------------------------------

def make_frame(t: int) -> np.ndarray:
    """
    Generate joint positions for animation frame *t* (0-based).
    Returns an array with shape (15, 2).
    """
    progress        = t / (N_FRAMES - 1)        # 0 … 1
    points          = SKELETON.copy()           # start from the canonical pose

    # ── Phase detection ──────────────────────────────────────────────────────
    if progress < CROUCH_END:                   # CROUCH PHASE
        # linear easing 0 … 1
        alpha = progress / CROUCH_END
        crouch_factor = alpha                   # 0 = upright, 1 = fully crouched
        roll_angle    = 0.0
        x_offset      = 0.0

    elif progress < ROLL_END:                   # ROLL (somersault) PHASE
        crouch_factor = 1.0                     # remain tucked
        alpha         = (progress - CROUCH_END) / (ROLL_END - CROUCH_END)
        roll_angle    = -2.0 * np.pi * alpha    # negative = forward rotation
        x_offset      =  ROLL_TRANSLATION * alpha

    else:                                       # STAND-UP PHASE
        alpha         = (progress - ROLL_END) / (STAND_END - ROLL_END)
        crouch_factor = 1.0 - alpha             # return to upright
        roll_angle    = -2.0 * np.pi            # finished full rotation
        x_offset      =  ROLL_TRANSLATION

    # ── 1) apply crouch / tuck ──────────────────────────────────────────────
    #
    # Compress the body towards the ankles (y = 0) and pull arms closer
    #
    scale_y = 1.0 - 0.35 * crouch_factor        # shorten the body
    scale_x = 1.0 - 0.40 * crouch_factor        # pull arms inward

    points[:, 0] *= scale_x
    points[:, 1] *= scale_y

    # additionally shift everything slightly downward while crouching
    points[:, 1] -= 0.25 * crouch_factor

    # ── 2) rotate around (current) hip-centre ───────────────────────────────
    hip_centre = points[[9, 10]].mean(axis=0)   # midpoint of both hips

    # rotation matrix
    ca, sa = np.cos(roll_angle), np.sin(roll_angle)
    R = np.array([[ca, -sa],
                  [sa,  ca]])

    points = (points - hip_centre) @ R.T + hip_centre

    # ── 3) translate the actor forward ──────────────────────────────────────
    points[:, 0] += x_offset

    return points


# ‑-- Matplotlib animation setup ---------------------------------------------

fig, ax = plt.subplots(figsize=(5, 5), facecolor='black', dpi=DPI)

ax.set_facecolor('black')
ax.set_xlim(-1.0, 3.5)
ax.set_ylim(-0.5, 2.5)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
plt.tight_layout()

# The scatter object that will be updated each frame
scatter = ax.scatter([], [], s=30, c='white')

def init():
    scatter.set_offsets(np.empty((0, 2)))
    return scatter,

def update(frame):
    pts = make_frame(frame)
    scatter.set_offsets(pts)
    return scatter,

anim = FuncAnimation(fig,
                     update,
                     frames=N_FRAMES,
                     init_func=init,
                     interval=1000 / FPS,
                     blit=True)


# ‑-- Run stand-alone ---------------------------------------------------------

if __name__ == '__main__':
    # Display the animation (works in interactive environments)
    plt.show()
