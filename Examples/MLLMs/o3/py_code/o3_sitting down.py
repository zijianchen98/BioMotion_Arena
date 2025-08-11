
"""
Point-Light Biological Motion Stimulus
Action: A man sitting down.
Exactly 15 white dots (joints) move against a solid black background
in a smooth, biomechanically plausible manner.
The script creates and stores an animated GIF named
“point_light_sit.gif”.  No user interaction is required.
"""

import numpy as np
import matplotlib
# guarantee head-less behaviour no matter where the code is executed
matplotlib.use("Agg")          # always use a non-interactive backend
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


# ------------------------------------------------------------------
# 1  Define the 15 joints (x, y) for the start (standing) and the
#    end (sitting) postures.  Coordinates are in a simple, abstract
#    “body space” – front view, origin near the feet.
# ------------------------------------------------------------------
# Index / anatomical label (for reference only):
#  0 head
#  1 neck / upper-spine
#  2 shoulder-left   3 shoulder-right
#  4 elbow-left      5 elbow-right
#  6 wrist-left      7 wrist-right
#  8 hip-left        9 hip-right
# 10 knee-left      11 knee-right
# 12 ankle-left     13 ankle-right
# 14 pelvis / spine-base

x_stand = np.array([0, 0,
                    -1, 1,
                    -1.5, 1.5,
                    -1.5, 1.5,
                    -0.8, 0.8,
                    -0.8, 0.8,
                    -0.8, 0.8,
                    0])

y_stand = np.array([9.5, 8.5,
                    8, 8,
                    6.5, 6.5,
                    5, 5,
                    5.5, 5.5,
                    3, 3,
                    1, 1,
                    5.5])

# “Sitting” target positions (heuristically chosen – coherent & smooth)
x_sit = x_stand.copy()                            # no horizontal change
y_sit = np.array([7.5, 6.5,
                  6, 6,
                  4.5, 4.5,
                  3.2, 3.2,
                  3.5, 3.5,
                  2, 2,
                  1, 1,
                  3.5])

start_pose = np.column_stack([x_stand, y_stand])
end_pose   = np.column_stack([x_sit,   y_sit])


# ------------------------------------------------------------------
# 2  Animation set-up
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 6), dpi=100)
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_aspect("equal")
ax.set_xlim(-3, 3)
ax.set_ylim(0, 10)
ax.axis("off")

scatter = ax.scatter(start_pose[:, 0],
                     start_pose[:, 1],
                     s=50, c="white")

frames_total = 60                       # stand → sit → stand loop
half = frames_total // 2


def smoothstep(t: np.ndarray) -> np.ndarray:
    """Cosine easing: 0 → 1 with zero slope at both ends."""
    return 0.5 - 0.5 * np.cos(np.pi * t)


def interpolate_pose(t: float) -> np.ndarray:
    """
    Interpolate between standing (t=0) and sitting (t=1)
    using smooth easing for fluid biological movement.
    """
    eased = smoothstep(t)
    return start_pose * (1 - eased) + end_pose * eased


def update(frame):
    """
    Called by FuncAnimation for every animation frame.
    Creates a sit-down then stand-up cycle (ping-pong).
    """
    if frame < half:
        # going down
        phase_t = frame / half
    else:
        # coming up
        phase_t = 1 - (frame - half) / half

    pose = interpolate_pose(phase_t)
    scatter.set_offsets(pose)
    return scatter,


anim = FuncAnimation(fig,
                     update,
                     frames=frames_total,
                     interval=50,
                     blit=True)

# ------------------------------------------------------------------
# 3  Save as GIF.  (Pillow writer is part of the standard Matplotlib
#    installation and requires no external codecs.)
# ------------------------------------------------------------------
writer = PillowWriter(fps=20)
anim.save("point_light_sit.gif", writer=writer)

# (Optional) If executed interactively one could call plt.show(),
# but for automated / head-less test environments we omit it.
