
"""
Point-light biological-motion stimulus

A sad, heavy woman who is lying down and gently breathing.
The stimulus consists of exactly 15 white point-lights that move
coherently against a solid black background.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------------------------------------------------
# 1.  Static, ‘neutral’ (no-motion) 2-D locations of the joints
# ------------------------------------------------------------
# The body lies horizontally (head on the left, feet on the right)
# Units are arbitrary; chosen for a visually pleasing aspect ratio.
#
# Index  Joint
#   0    Head centre
#   1    Neck / upper-sternum
#   2    Left shoulder
#   3    Right shoulder
#   4    Left elbow
#   5    Right elbow
#   6    Left wrist
#   7    Right wrist
#   8    Left hip
#   9    Right hip
#  10    Left knee
#  11    Right knee
#  12    Left ankle
#  13    Right ankle
#  14    Pelvis centre
base = np.array([
    [ 0.0,  0.0],   # head
    [ 0.8,  0.0],   # neck / chest
    [ 0.8, -0.50],  # L shoulder
    [ 0.8,  0.50],  # R shoulder
    [ 1.7, -0.60],  # L elbow
    [ 1.7,  0.60],  # R elbow
    [ 2.7, -0.60],  # L wrist
    [ 2.7,  0.60],  # R wrist
    [ 3.0, -0.40],  # L hip
    [ 3.0,  0.40],  # R hip
    [ 4.0, -0.45],  # L knee
    [ 4.0,  0.45],  # R knee
    [ 5.0, -0.30],  # L ankle
    [ 5.0,  0.30],  # R ankle
    [ 3.0,  0.0],   # pelvis (centre)
])

# Which joints participate in the ‘breathing’ rise/fall motion?
upper_body_idx = [0, 1, 2, 3, 4, 5, 6, 7]  # head, shoulders, arms

# ------------------------------------------------------------
# 2.  Animation parameters
# ------------------------------------------------------------
FPS            = 30                # frames per second
BREATH_PERIOD  = 4.0               # seconds per inhale/exhale cycle
BREATH_AMPL    = 0.12              # amplitude of the up-down motion
SMALL_TWITCH   = 0.015             # noise for subtle, random movement
DURATION       = 20                # total seconds of animation

n_frames = int(DURATION * FPS)

# ------------------------------------------------------------
# 3.  Matplotlib figure
# ------------------------------------------------------------
plt.style.use('default')           # ensure consistent appearance
fig, ax = plt.subplots(figsize=(8, 3))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Remove all spines, ticks, etc.
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

# Scatter plot of 15 points
scatter = ax.scatter(base[:, 0], base[:, 1],
                     s=40, c='white', edgecolors='none')

# Set axis limits slightly larger than the body for padding
ax.set_xlim(-0.7, 5.7)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')

# ------------------------------------------------------------
# 4.  Frame-update function
# ------------------------------------------------------------
rng = np.random.default_rng()

def update(frame_number: int):
    t = frame_number / FPS                       # time in seconds
    offsets = np.copy(base)

    # Smooth, sinusoidal breathing (upper body moves vertically)
    breath_offset = BREATH_AMPL * np.sin(2 * np.pi * t / BREATH_PERIOD)
    offsets[upper_body_idx, 1] += breath_offset

    # Gentle downward sag of the heavy body – pelvis drops slightly
    sag = 0.04 * (1 - np.cos(2 * np.pi * t / BREATH_PERIOD))  # twice per cycle
    offsets[14, 1] -= sag                # pelvis centre
    offsets[8:10, 1] -= sag * 0.6        # hips follow, slightly less
    offsets[10:14, 1] -= sag * 0.3       # knees & ankles follow even less

    # Subtle random twitches for naturalness
    jitter = SMALL_TWITCH * rng.standard_normal(size=offsets.shape)
    offsets += jitter

    # Update the scatter plot
    scatter.set_offsets(offsets)
    return scatter,

# ------------------------------------------------------------
# 5.  Create and display / save the animation
# ------------------------------------------------------------
ani = FuncAnimation(fig,
                    update,
                    frames=n_frames,
                    interval=1000 / FPS,
                    blit=True,
                    repeat=True)

# If this script is run directly, show the animation window.
# (When executed in an environment without a GUI backend,
#  this will simply do nothing.)
if __name__ == '__main__':
    plt.show()
