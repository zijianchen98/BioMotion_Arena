
"""
Biological-motion point-light stimulus
Sad woman (light weight) – sitting down
Exactly 15 white dots on a black background.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


# ------------------------------------------------------------------
# Helper that returns the coordinates of the 15 point-lights
# at a given “sit level”, 0 = fully standing, 1 = fully sitting
# ------------------------------------------------------------------
def skeleton(sit: float) -> np.ndarray:
    """
    Produce 15×2 array with (x, y) positions of the joints.

    Index map
    0  = head
    1  = neck
    2  = left-shoulder
    3  = right-shoulder
    4  = left-elbow
    5  = right-elbow
    6  = left-wrist
    7  = right-wrist
    8  = pelvis (mid-hip)
    9  = left-hip
    10 = right-hip
    11 = left-knee
    12 = right-knee
    13 = left-ankle
    14 = right-ankle
    """
    # Overall horizontal scale (body width)
    shoulder_span = 0.40          # shoulders are ±0.20
    hip_span      = 0.30          # hips are ±0.15
    hand_offset   = 0.45          # x-offset of the wrists from centre
    foot_span     = 0.25          # feet are ±0.125

    # Standing (sit = 0) reference heights
    y_head      = 1.90
    y_neck      = 1.70
    y_shoulder  = 1.60
    y_hip       = 1.00
    y_knee      = 0.50
    y_ankle     = 0.00

    # Amount torso sinks while sitting
    torso_drop  = 0.40            # how far the hips go down
    # How much the knees come up when sitting
    knee_raise  = 0.10
    # Horizontal forward shift of wrists to lap
    wrist_forward = 0.20

    # Interpolate vertical positions
    hip_y     = y_hip     - torso_drop * sit
    shoulder_y = y_shoulder - torso_drop * sit
    neck_y     = y_neck     - torso_drop * sit
    head_y     = y_head     - torso_drop * sit

    # Knees transition between standing & sitting heights
    knee_y = y_knee * (1 - sit) + (y_knee + knee_raise) * sit
    ankle_y = y_ankle  # ankles stay on the ground

    # Horizontal coordinates
    head_x = 0.0
    neck_x = 0.0

    # “Sad” pose: the head droops forward while sitting
    head_x -= 0.05 * sit

    l_sh_x = -shoulder_span / 2
    r_sh_x =  shoulder_span / 2
    l_hip_x = -hip_span / 2
    r_hip_x =  hip_span / 2

    # Elbows halfway between shoulders & wrists (simple model)
    l_elb_x = l_sh_x * 0.6
    r_elb_x = r_sh_x * 0.6

    # Wrists move forward onto lap as she sits
    l_wr_x = -hand_offset * (1 - sit) + (-wrist_forward) * sit
    r_wr_x =  hand_offset * (1 - sit) + ( wrist_forward) * sit

    # Elbow and wrist vertical coordinates
    elb_y = shoulder_y - 0.35                                # fixed distance from shoulders
    wr_y  = elb_y  - 0.30 * (1 - 0.4 * sit)                  # wrist slightly higher in sitting

    # Ankles / feet
    l_ankle_x = -foot_span / 2
    r_ankle_x =  foot_span / 2

    # Knees follow vertical interpolation; remain above ankles
    l_knee_x = l_hip_x
    r_knee_x = r_hip_x

    # Assemble joint list
    joints = np.array([
        [head_x,     head_y],      # 0
        [neck_x,     neck_y],      # 1
        [l_sh_x,     shoulder_y],  # 2
        [r_sh_x,     shoulder_y],  # 3
        [l_elb_x,    elb_y],       # 4
        [r_elb_x,    elb_y],       # 5
        [l_wr_x,     wr_y],        # 6
        [r_wr_x,     wr_y],        # 7
        [0.0,        hip_y],       # 8  pelvis (centre)
        [l_hip_x,    hip_y],       # 9
        [r_hip_x,    hip_y],       # 10
        [l_knee_x,   knee_y],      # 11
        [r_knee_x,   knee_y],      # 12
        [l_ankle_x,  ankle_y],     # 13
        [r_ankle_x,  ankle_y],     # 14
    ])

    return joints


# ------------------------------------------------------------------
# Build animation
# ------------------------------------------------------------------
n_frames       = 120                  # total frames
fps            = 30
sit_frames     = n_frames // 2        # frames spent transitioning
hold_frames    = n_frames - sit_frames

# Pre-compute all joint coordinates
frames = []
for k in range(n_frames):
    if k < sit_frames:
        # Smooth ease-in using a raised cosine
        f = 0.5 * (1 - np.cos(np.pi * k / sit_frames))
    else:
        f = 1.0                         # fully seated
    frames.append(skeleton(f))

frames = np.stack(frames)              # shape (n_frames, 15, 2)

# ------------------------------------------------------------------
# Matplotlib set-up
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-0.2, 2.1)
ax.axis('off')

# 15 white dots
dots = ax.scatter(frames[0][:, 0], frames[0][:, 1],
                  s=50, c='white', edgecolors='none')

# ------------------------------------------------------------------
# Animation callback
# ------------------------------------------------------------------
def update(frame_idx):
    dots.set_offsets(frames[frame_idx])
    return dots,

anim = FuncAnimation(fig, update, frames=n_frames,
                     interval=1000 / fps, blit=True)

# ------------------------------------------------------------------
# Save to GIF (lightweight, no external encoders required)
# ------------------------------------------------------------------
writer = PillowWriter(fps=fps)
anim.save('sadwoman_sitting.gif', writer=writer)

# Show the animation window if the user runs the script interactively.
# (When executed in a head-less test environment this has no effect.)
plt.show()
