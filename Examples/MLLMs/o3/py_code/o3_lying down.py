
"""
Point-light biological-motion stimulus: 15 white dots depicting a man lying down.
The script creates a biomechanically plausible, smooth animation using
matplotlib.  The figure window has a solid black background, while the dots are
rendered in white.

The motion is minimal and natural: a gentle breathing cycle (chest expansion)
combined with very light limb oscillations, so the viewer clearly perceives a
person resting supine.
"""

import numpy as np
import matplotlib
# Use a non-interactive backend so the script also works in head-less environments
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------------------------------------------------
# 1.  Static (rest) joint coordinates for a person lying down
# ------------------------------------------------------------
#                        (x  ,  y)
joint_names = [
    "head",            # 0
    "neck",            # 1
    "right_shoulder",  # 2
    "left_shoulder",   # 3
    "right_elbow",     # 4
    "left_elbow",      # 5
    "right_wrist",     # 6
    "left_wrist",      # 7
    "pelvis",          # 8
    "right_hip",       # 9
    "left_hip",        # 10
    "right_knee",      # 11
    "left_knee",       # 12
    "right_ankle",     # 13
    "left_ankle"       # 14
]

# Positions chosen so the body lies along the horizontal axis (x-axis)
# Positive y is "up" relative to the viewer; 0 is mid-line of the trunk.
rest_pose = np.array([
    [ 0.0,  0.0],   # head
    [ 1.0,  0.0],   # neck
    [ 2.0,  0.35],  # right shoulder
    [ 2.0, -0.35],  # left  shoulder
    [ 3.0,  0.45],  # right elbow
    [ 3.0, -0.45],  # left  elbow
    [ 4.0,  0.55],  # right wrist
    [ 4.0, -0.55],  # left  wrist
    [ 5.0,  0.00],  # pelvis (centre)
    [ 5.0,  0.35],  # right hip
    [ 5.0, -0.35],  # left  hip
    [ 6.0,  0.45],  # right knee
    [ 6.0, -0.45],  # left  knee
    [ 7.0,  0.55],  # right ankle
    [ 7.0, -0.55],  # left  ankle
])

# Pre-compute indices that move most during breathing and limb oscillations
chest_pts  = np.array([1, 2, 3])      # neck and shoulders
arm_pts    = np.array([4, 5, 6, 7])   # elbows & wrists
leg_pts    = np.array([11, 12, 13, 14])  # knees & ankles

# ------------------------------------------------------------
# 2.  Animation set-up
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 3))  # wide to emphasise horizontal posture
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_xlim(-0.5, 7.5)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect("equal")
ax.axis("off")

# Create scatter plot with 15 white markers
scatter = ax.scatter(rest_pose[:, 0], rest_pose[:, 1],
                     c="white", s=50, edgecolors="white")

# ------------------------------------------------------------
# 3.  Animation update function
# ------------------------------------------------------------
breathing_period = 5.0      # seconds
limb_period      = 2.5      # seconds
fps              = 30
total_frames     = int(fps * 10)   # 10-second loop

def update(frame):
    t = frame / fps
    pose = rest_pose.copy()

    # 3a. Breathing (vertical displacement of chest)
    breath_amp = 0.07  # max ↑/↓ displacement
    breath = breath_amp * np.sin(2 * np.pi * t / breathing_period)
    pose[chest_pts, 1] += breath      # move chest / upper torso

    # For a subtle whole-body rise/fall, slightly move head & pelvis too
    pose[[0, 8], 1] += 0.4 * breath

    # 3b. Very small limb oscillations (simulate natural micro-movements)
    limb_amp = 0.03
    limb_phase = 2 * np.pi * t / limb_period
    pose[arm_pts, 1] += limb_amp * np.sin(limb_phase + np.pi/4)
    pose[leg_pts, 1] += limb_amp * np.sin(limb_phase - np.pi/6)

    # 3c. Update scatter plot
    scatter.set_offsets(pose)

    return scatter,

# ------------------------------------------------------------
# 4.  Run animation (FuncAnimation)
# ------------------------------------------------------------
ani = FuncAnimation(fig,
                    update,
                    frames=total_frames,
                    interval=1000/fps,
                    blit=True,
                    repeat=True)

# If the script is executed directly (not imported), display the animation.
if __name__ == "__main__":
    plt.show()
