#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This program will display a 2D point-light figure (15 white points) 
# on a black background performing a jumping motion.

# Define segment lengths (arbitrary plausible proportions)
L_HEAD = 0.15     # Head height
L_TORSO = 0.35    # Neck to pelvis
L_SHOULDER_OFFSET = 0.25  # Horizontal distance from torso center to each shoulder
L_UPPER_ARM = 0.20
L_FOREARM = 0.18
L_HIP_OFFSET = 0.20       # Horizontal distance from torso center to each hip
L_THIGH = 0.30
L_SHIN = 0.30

# We will have 15 points:
# 1: Head
# 2: Left Shoulder
# 3: Right Shoulder
# 4: Left Elbow
# 5: Right Elbow
# 6: Left Wrist
# 7: Right Wrist
# 8: Pelvis (center)
# 9: Left Hip
# 10: Right Hip
# 11: Left Knee
# 12: Right Knee
# 13: Left Ankle
# 14: Right Ankle
# 15: Mid-Torso (near chest)

# Time parameters
fps = 30
duration = 2.0  # total seconds
frames = int(fps * duration)
ts = np.linspace(0, 1, frames)

# Define smooth parameter transitions for jump:
# - t in [0, 0.2]: descend into squat
# - t in [0.2, 0.3]: powerful extension
# - t in [0.3, 0.5]: in the air (peak around t=0.4)
# - t in [0.5, 0.7]: coming down
# - t in [0.7, 1.0]: recovering
def smoothstep(x0, x1, t):
    # Clamps t to [0,1] and smooth step between x0 and x1
    t_clamped = max(0.0, min(1.0, t))
    return x0 + (x1 - x0) * (3*t_clamped**2 - 2*t_clamped**3)

def pelvis_height(t):
    # Piecewise definition of pelvis vertical motion (simple approximation)
    if t < 0.2:
        # Move pelvis slightly down
        return 0.0 - 0.05 * smoothstep(0, 1, t/0.2)
    elif t < 0.3:
        # Explosive upward movement
        return -0.05 + 0.40 * smoothstep(0, 1, (t-0.2)/0.1)
    elif t < 0.5:
        # In the air to apex
        return 0.35 + 0.05 * np.sin(np.pi * smoothstep(0, 1, (t-0.3)/0.2))
    elif t < 0.7:
        # Coming down
        return 0.35 * (1 - smoothstep(0, 1, (t-0.5)/0.2))
    else:
        # Recovery
        return 0.0

def knee_bend_angle(t):
    # 0 degrees = fully extended
    # We'll let knees bend from ~0 to ~60 degrees
    # Heaviest bend around t=0.2, then extend, bend on landing, etc.
    if t < 0.2:
        return 60.0 * smoothstep(0, 1, t/0.2)
    elif t < 0.3:
        return 60.0 * (1 - smoothstep(0, 1, (t-0.2)/0.1))
    elif t < 0.5:
        return 0.0
    elif t < 0.6:
        # Start bending again for landing
        return 60.0 * smoothstep(0, 1, (t-0.5)/0.1)
    elif t < 0.7:
        return 60.0 * (1 - smoothstep(0, 1, (t-0.6)/0.1))
    else:
        return 0.0

def arm_swing_angle(t):
    # Negative angle: arms behind, positive: arms forward
    # We'll do a minor arm swing to add realism
    return 20.0 * np.sin(2 * np.pi * t)

def compute_points(t):
    # Convert degrees to radians
    kb = np.radians(knee_bend_angle(t))
    arm = np.radians(arm_swing_angle(t))
    
    # Pelvis coordinates
    px, py = (0.0, pelvis_height(t))
    
    # Torso top (near chest)
    chest_y = py + L_TORSO
    # Head
    head_y = chest_y + L_HEAD

    # Shoulders
    left_shoulder_x = -L_SHOULDER_OFFSET
    right_shoulder_x = L_SHOULDER_OFFSET
    left_shoulder_y = chest_y
    right_shoulder_y = chest_y

    # Hips
    left_hip_x = -L_HIP_OFFSET
    right_hip_x = L_HIP_OFFSET
    left_hip_y = py
    right_hip_y = py

    # Knees (using knee bend)
    # We'll approximate the leg angles with knee bend controlling the thigh-shin
    # For a heavier jump, hips don't shift horizontally, just the angles.
    # We'll let thighs remain mostly vertical, bending at the knee.
    thigh_x_offset_left = left_hip_x
    thigh_x_offset_right = right_hip_x
    # Thigh vertical
    left_knee_y = left_hip_y - L_THIGH * np.cos(kb)
    right_knee_y = right_hip_y - L_THIGH * np.cos(kb)
    left_knee_x = thigh_x_offset_left
    right_knee_x = thigh_x_offset_right

    # Ankle
    left_ankle_y = left_knee_y - L_SHIN * np.cos(kb)
    right_ankle_y = right_knee_y - L_SHIN * np.cos(kb)
    left_ankle_x = left_knee_x
    right_ankle_x = right_knee_x

    # Arms
    # Let shoulders rotate slightly with arm angle
    # We'll swing arms in front-back plane, so the x offset changes
    # For simplicity, keep the elbow offset from the shoulder in x by a function of arm angle
    # and the wrist offset similarly
    # Left arm sweeps behind (negative angle relative to downward)
    # Right arm sweeps forward (positive angle)
    # Baseline arm downward: we say angle=90 deg from x-axis
    # We'll add or subtract "arm" from that 90 deg.

    left_shoulder_angle = np.radians(90.0) + np.radians(-arm_swing_angle(t))
    right_shoulder_angle = np.radians(90.0) + np.radians(arm_swing_angle(t))

    # Elbows
    left_elbow_x = left_shoulder_x + L_UPPER_ARM * np.cos(left_shoulder_angle)
    left_elbow_y = left_shoulder_y - L_UPPER_ARM * np.sin(left_shoulder_angle)
    right_elbow_x = right_shoulder_x + L_UPPER_ARM * np.cos(right_shoulder_angle)
    right_elbow_y = right_shoulder_y - L_UPPER_ARM * np.sin(right_shoulder_angle)

    # Forearms downward from elbow
    left_elbow_angle = left_shoulder_angle
    right_elbow_angle = right_shoulder_angle

    left_wrist_x = left_elbow_x + L_FOREARM * np.cos(left_elbow_angle)
    left_wrist_y = left_elbow_y - L_FOREARM * np.sin(left_elbow_angle)
    right_wrist_x = right_elbow_x + L_FOREARM * np.cos(right_elbow_angle)
    right_wrist_y = right_elbow_y - L_FOREARM * np.sin(right_elbow_angle)

    # Collect 15 points in order:
    # 1: Head
    # 2: Left Shoulder
    # 3: Right Shoulder
    # 4: Left Elbow
    # 5: Right Elbow
    # 6: Left Wrist
    # 7: Right Wrist
    # 8: Pelvis (center)
    # 9: Left Hip
    # 10: Right Hip
    # 11: Left Knee
    # 12: Right Knee
    # 13: Left Ankle
    # 14: Right Ankle
    # 15: Mid-Torso (chest)
    points = [
        (0.0, head_y),                # Head
        (left_shoulder_x, left_shoulder_y),
        (right_shoulder_x, right_shoulder_y),
        (left_elbow_x, left_elbow_y),
        (right_elbow_x, right_elbow_y),
        (left_wrist_x, left_wrist_y),
        (right_wrist_x, right_wrist_y),
        (px, py),                     # Pelvis center
        (left_hip_x, left_hip_y),
        (right_hip_x, right_hip_y),
        (left_knee_x, left_knee_y),
        (right_knee_x, right_knee_y),
        (left_ankle_x, left_ankle_y),
        (right_ankle_x, right_ankle_y),
        (0.0, chest_y),               # Mid-Torso
    ]
    return points

fig, ax = plt.subplots(figsize=(5,5))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_aspect('equal')
ax.axis('off')

scatter = ax.scatter([], [], c='white', s=30)

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    t = ts[frame]
    pts = compute_points(t)
    scatter.set_offsets(pts)
    return scatter,

ani = FuncAnimation(fig, update, frames=frames, init_func=init, interval=1000/fps, blit=True)
plt.show()