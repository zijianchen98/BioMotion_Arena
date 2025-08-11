
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------------------------------------------
#  15-marker biological motion – “happy man sitting down”
# -------------------------------------------------------------

# Joint order (15 points):
#   0  head
#   1  neck
#   2  shoulder-left
#   3  shoulder-right
#   4  elbow-left
#   5  elbow-right
#   6  wrist-left
#   7  wrist-right
#   8  hip-left
#   9  hip-right
#  10  knee-left
#  11  knee-right
#  12  ankle-left
#  13  ankle-right
#  14  pelvis (mid-spine)

# --------------------------
#  Key postures (standing / sitting)
# --------------------------
standing = np.array([
    [ 0.00,  1.80],   # head
    [ 0.00,  1.40],   # neck
    [-0.30,  1.30],   # L-shoulder
    [ 0.30,  1.30],   # R-shoulder
    [-0.30,  0.90],   # L-elbow
    [ 0.30,  0.90],   # R-elbow
    [-0.30,  0.50],   # L-wrist
    [ 0.30,  0.50],   # R-wrist
    [-0.20,  0.00],   # L-hip
    [ 0.20,  0.00],   # R-hip
    [-0.20, -1.00],   # L-knee
    [ 0.20, -1.00],   # R-knee
    [-0.20, -2.00],   # L-ankle
    [ 0.20, -2.00],   # R-ankle
    [ 0.00,  0.20],   # pelvis
])

sitting = np.array([
    [-0.15,  1.30],   # head (slightly forward & lower)
    [-0.15,  1.00],   # neck
    [-0.45,  0.90],   # L-shoulder
    [ 0.15,  0.90],   # R-shoulder
    [-0.05,  0.70],   # L-elbow (arms swing forward)
    [ 0.35,  0.70],   # R-elbow
    [ 0.15,  0.50],   # L-wrist
    [ 0.55,  0.50],   # R-wrist
    [-0.35, -1.00],   # L-hip (lower & back)
    [ 0.05, -1.00],   # R-hip
    [ 0.35, -1.00],   # L-knee (forward)
    [ 0.85, -1.00],   # R-knee
    [ 0.35, -2.00],   # L-ankle (under knee)
    [ 0.85, -2.00],   # R-ankle
    [-0.15, -0.40],   # pelvis
])

# --------------------------
#  Animation set-up
# --------------------------
fig, ax = plt.subplots(facecolor='black')
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-2.3, 2.2)
ax.axis('off')

points = ax.scatter(standing[:, 0], standing[:, 1],
                    s=60, c='white', edgecolors='none')

# --------------------------
#  Interpolation helpers
# --------------------------
n_frames = 180  # total frames for one full down-and-up cycle


def smooth_step(x):
    """Cosine ease in/out (0→1)."""
    return 0.5 * (1 - np.cos(np.pi * x))


def frame_to_progress(frame):
    """
    Converts absolute frame number to a progress value (0→1→0).
    A full cycle is standing → sitting → standing.
    """
    phase = (frame % n_frames) / n_frames            # 0 → 1
    if phase <= 0.5:
        return smooth_step(phase * 2)                # down
    else:
        return smooth_step(2 - phase * 2)            # up (reverse)


def update(frame):
    p = frame_to_progress(frame)                     # interpolation parameter
    pose = standing + p * (sitting - standing)       # linear blend of poses
    points.set_offsets(pose)
    return points,


ani = FuncAnimation(
    fig, update, frames=n_frames, interval=1000 / 60, blit=True)

plt.show()
