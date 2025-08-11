
"""
Point-light biological–motion stimulus
--------------------------------------
15 white markers on a black background depicting a (light-weight) sad stick-man lying
on the ground and breathing slowly.  The code produces a smooth, biomechanically
plausible animation using matplotlib only.

Run the file.  A window will pop-up showing an endlessly looping animation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------------------------------------------------------
# Skeleton definition (15 joints)
#
# 0  head         8  pelvis
# 1  neck         9  r-hip
# 2  r-shoulder  10  r-knee
# 3  r-elbow     11  r-ankle
# 4  r-wrist     12  l-hip
# 5  l-shoulder  13  l-knee
# 6  l-elbow     14  l-ankle
# 7  l-wrist
# ------------------------------------------------------------------

# Base pose (lying on the ground, head on the left, feet on the right)
base = np.array([
    [0.00,  0.00],   # 0 head
    [0.15,  0.00],   # 1 neck
    [0.30,  0.05],   # 2 r-shoulder
    [0.45,  0.05],   # 3 r-elbow
    [0.60,  0.05],   # 4 r-wrist
    [0.30, -0.05],   # 5 l-shoulder
    [0.45, -0.05],   # 6 l-elbow
    [0.60, -0.05],   # 7 l-wrist
    [0.15,  0.00],   # 8 pelvis (co-located with neck in this simple model)
    [0.30,  0.10],   # 9 r-hip
    [0.45,  0.13],   #10 r-knee
    [0.60,  0.16],   #11 r-ankle
    [0.30, -0.10],   #12 l-hip
    [0.45, -0.13],   #13 l-knee
    [0.60, -0.16],   #14 l-ankle
])

# Animation parameters ------------------------------------------------
FPS          = 60       # display frame-rate
BREATH_FREQ  = 0.25     # breathing cycles per second
BREATH_AMP   = 0.02     # breathing amplitude (metres equivalent)
TWITCH_FREQ  = 0.75     # small limb twitches
TWITCH_AMP   = 0.01

# Pre-compute time points for one breathing cycle (looped later)
t = np.linspace(0, 1 / BREATH_FREQ, int(FPS / BREATH_FREQ), endpoint=False)

# Figure / Axes -------------------------------------------------------
plt.rcParams['toolbar'] = 'None'   # neat window
fig, ax = plt.subplots(figsize=(6, 3), dpi=100)
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.05, 0.75)
ax.set_ylim(-0.25, 0.25)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

# Create 15 point lights (white scatter)
scatter = ax.scatter(base[:, 0], base[:, 1], s=60, c='white')
txt = ax.text(0.02, 0.22, '', color='white', fontsize=8)  # subtle caption

# --------------------------------------------------------------------
def animate(frame_idx: int):
    """
    Update function for FuncAnimation.
    Generates a single frame of the lying-down breathing motion.
    """
    # Current absolute time (seconds)
    time = frame_idx / FPS

    # Breathing (vertical chest expansion/contraction)
    breath = BREATH_AMP * np.sin(2 * np.pi * BREATH_FREQ * time)

    # Whole-body tiny twitches/noise (looks more alive)
    twitch = (TWITCH_AMP *
              np.sin(2 * np.pi * (TWITCH_FREQ) * time + np.arange(15))
              .reshape(-1, 1))

    # Build new position array
    pos = base.copy()

    # Apply breathing (lift shoulders, neck, head slightly)
    breath_indices = [0, 1, 2, 5]   # head, neck, both shoulders
    pos[breath_indices, 1] += breath

    # Apply twitches (independent per joint, mostly Y because supine)
    pos[:, 1:2] += twitch

    # Update artist
    scatter.set_offsets(pos)

    # subtle caption scroll (just aesthetic)
    txt.set_text('biological motion – sadman, lying')
    return scatter,

# Create the animation (FuncAnimation keeps a reference on 'fig')
anim = FuncAnimation(fig,
                     animate,
                     interval=1000 / FPS,
                     blit=True)

# --------------------------------------------------------------------
if __name__ == '__main__':
    plt.show()
