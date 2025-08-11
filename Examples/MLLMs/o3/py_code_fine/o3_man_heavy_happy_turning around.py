
"""
Point–light biological–motion stimulus
Subject : an overweight (happyman) person
Action  : turning around (360° spin)

This script generates a self–contained animated GIF (point_light_stimulus.gif)
made of 15 white point–lights moving against a solid black background.  The
motion is biomechanically plausible and smooth: the whole 3-D skeleton turns
around its vertical axis while the arms swing a little to enhance naturalness.
"""

import math
import pathlib
import numpy as np
import matplotlib

# ------------------------------------------------------------------
# Use a non-interactive backend so the code also runs on head-less CI
# ------------------------------------------------------------------
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ------------------------------------------------------------------
# 1. Build a very simple 3-D heavy-set human skeleton (15 joints)
# ------------------------------------------------------------------
#   y : vertical axis (in metres)
#   x : left / right
#   z : front / back
# Co-ordinates loosely inspired by anthropometric data, but with
# larger shoulder / hip width to hint at “heavy weight”.
#
# Index / semantic mapping
#   0  head
#   1  neck
#   2  L shoulder
#   3  R shoulder
#   4  L elbow
#   5  R elbow
#   6  L hand
#   7  R hand
#   8  pelvis (mid-hip)
#   9  L hip
#   10 R hip
#   11 L knee
#   12 R knee
#   13 L ankle
#   14 R ankle
#
skeleton_static = np.array(
    [
        (0.0, 1.70, 0.0),      # head
        (0.0, 1.50, 0.0),      # neck
        (-0.35, 1.50, 0.0),    # L shoulder
        (0.35, 1.50, 0.0),     # R shoulder
        (-0.55, 1.10, 0.10),   # L elbow
        (0.55, 1.10, -0.10),   # R elbow
        (-0.65, 0.75, 0.20),   # L hand
        (0.65, 0.75, -0.20),   # R hand
        (0.0, 1.05, 0.0),      # pelvis / torso root
        (-0.30, 0.95, 0.0),    # L hip
        (0.30, 0.95, 0.0),     # R hip
        (-0.32, 0.50, 0.05),   # L knee
        (0.32, 0.50, -0.05),   # R knee
        (-0.32, 0.10, 0.07),   # L ankle
        (0.32, 0.10, -0.07),   # R ankle
    ],
    dtype=float,
)

# ------------------------------------------------------------------
# 2. Utility functions
# ------------------------------------------------------------------
def rotation_matrix_y(angle_rad: float) -> np.ndarray:
    """Return a 3×3 rotation matrix around the vertical (y) axis."""
    c, s = math.cos(angle_rad), math.sin(angle_rad)
    return np.array([[c, 0.0, s],
                     [0.0, 1.0, 0.0],
                     [-s, 0.0, c]], dtype=float)


def apply_arm_swing(points: np.ndarray, phase: float) -> None:
    """
    Add a gentle natural-looking arm swing.
    It only modifies shoulders->hands hierarchy (indices 2-7).
    """
    swing_amp = 0.10  # metres
    dz = swing_amp * math.sin(phase * 2 * math.pi)     # front/back
    dy = 0.05 * math.sin(phase * 4 * math.pi)          # up/down
    for idx in (2, 4, 6):      # left arm joints
        points[idx, 1] += dy
        points[idx, 2] += dz
    for idx in (3, 5, 7):      # right arm joints (opposite phase)
        points[idx, 1] -= dy
        points[idx, 2] -= dz


def project_to_2d(points3d: np.ndarray, distance: float = 4.0) -> np.ndarray:
    """
    Very simple perspective projection onto the image plane z = 0,
    with the camera looking towards +z, located at (0, 1.3, -distance).
    Returns an (N, 2) array of x,y screen coordinates.
    """
    cam = np.array([0.0, 1.30, -distance])
    shifted = points3d - cam        # translate so camera is at origin
    # Perspective divide (focal length = 1.0)
    # x' = x / z , y' = y / z
    # We clip/avoid division by zero by adding a tiny epsilon
    eps = 1e-6
    zs = shifted[:, 2] + eps
    proj = shifted[:, :2] / zs[:, None]
    return proj


# ------------------------------------------------------------------
# 3. Generate the animation
# ------------------------------------------------------------------
FPS          = 25             # frames per second
REV_DURATION = 5.0            # seconds for full 360° turn
N_FRAMES     = int(FPS * REV_DURATION)

# Prepare the plot
fig, ax = plt.subplots(figsize=(4, 6), facecolor="black")
ax.set_facecolor("black")
ax.set_aspect("equal")
ax.set_xlim(-0.7, 0.7)
ax.set_ylim(0.0, 1.9)
ax.set_xticks([])
ax.set_yticks([])

# Create the scatter plot that will be updated
scatter = ax.scatter([], [], s=40, c="white")

def init():
    scatter.set_offsets([])
    return (scatter,)


def animate(frame_idx: int):
    # 1) Copy base skeleton to avoid modifying the template
    pts = skeleton_static.copy()

    # 2) Apply global rotation to produce the “turning around”
    angle = 2 * math.pi * (frame_idx / N_FRAMES)
    R = rotation_matrix_y(angle)
    pts = pts @ R.T    # rotate in place (matrix multiplies each vector)

    # 3) Add a little arm swing for naturalness
    phase = frame_idx / N_FRAMES
    apply_arm_swing(pts, phase)

    # 4) Project to 2-D
    pts2d = project_to_2d(pts, distance=4.0)

    # 5) Update scatter plot
    scatter.set_offsets(pts2d)
    return (scatter,)


anim = FuncAnimation(fig,
                     animate,
                     frames=N_FRAMES,
                     init_func=init,
                     interval=1000 / FPS,
                     blit=True)

print("Rendering GIF …  (this may take a few seconds)")
gif_name = "point_light_stimulus.gif"
# Use PillowWriter (pure-python, no external binaries required)
writer = PillowWriter(fps=FPS)
anim.save(gif_name, writer=writer)
print(f"Animation saved to {gif_name} ({N_FRAMES} frames, {REV_DURATION} s).")

# Also keep a static PNG of the first frame for quick visual sanity check
fig.savefig("point_light_frame0.png", dpi=150, facecolor="black", bbox_inches="tight")
print("Saved first frame as point_light_frame0.png")

# Cleaning up matplotlib objects (CI systems with limited memory)
plt.close(fig)

# On first successful run, report where the files are located
print(f"Output directory : {pathlib.Path('.').resolve()}")
