
"""
A Python program to display an animated point‐light stimulus of a walking man.
The animation uses 15 white points on a black background.
The points represent:
  1. Head
  2. Neck
  3. Right Shoulder
  4. Right Elbow
  5. Right Hand
  6. Left Shoulder
  7. Left Elbow
  8. Left Hand
  9. Torso (mid‐spine)
 10. Right Hip
 11. Right Knee
 12. Right Foot
 13. Left Hip
 14. Left Knee
 15. Left Foot

The joint positions are computed with a biomechanically plausible walking cycle.
The body translates horizontally while the limbs swing with a cyclic pattern.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the animation
fps = 30
duration = 5  # seconds
n_frames = fps * duration

# Walking cycle parameters
cycle_period = 1.0  # seconds per cycle
omega = 2 * np.pi / cycle_period  # angular frequency

# Walking horizontal speed (units per second)
speed = 0.5

# Function to compute all 15 joint positions given time t.
def compute_joint_positions(t):
    # Global horizontal displacement for the body center (pelvis)
    p_x = speed * t
    # Vertical positions (fixed relative to body)
    pelvis_y = 0.0
    torso_y   = 0.4
    neck_y    = 0.65
    head_y    = 0.85

    # Phase of the walking cycle:
    phase = omega * t

    # ---------------------------
    # Define joints:
    # 1. Head: centered above the neck.
    head = np.array([p_x, head_y])

    # 2. Neck: directly above torso.
    neck = np.array([p_x, neck_y])

    # Shoulders: slight lateral offset from center with a small swing
    shoulder_offset = 0.15
    shoulder_swing = 0.05 * np.sin(phase)
    right_shoulder = np.array([p_x + shoulder_offset + shoulder_swing, neck_y])
    left_shoulder  = np.array([p_x - shoulder_offset - shoulder_swing, neck_y])

    # Arms: use simple two-segment arms. The arms swing opposite to the legs.
    # Define amplitudes for arm swing.
    arm_swing_amp = 0.2
    # Right arm: swings with phase
    right_elbow = right_shoulder + np.array([arm_swing_amp * np.sin(phase),
                                              -arm_swing_amp * np.abs(np.cos(phase))])
    right_hand  = right_elbow + np.array([arm_swing_amp * np.sin(phase),
                                           -arm_swing_amp * np.abs(np.cos(phase))])
    # Left arm: swings in counter-phase.
    left_elbow = left_shoulder + np.array([arm_swing_amp * np.sin(phase + np.pi),
                                            -arm_swing_amp * np.abs(np.cos(phase + np.pi))])
    left_hand  = left_elbow + np.array([arm_swing_amp * np.sin(phase + np.pi),
                                         -arm_swing_amp * np.abs(np.cos(phase + np.pi))])

    # 9. Torso (mid-spine): between pelvis and neck.
    torso = np.array([p_x, torso_y])

    # Hips: small lateral offsets from the center (around pelvis)
    hip_offset = 0.1
    right_hip = np.array([p_x + hip_offset, pelvis_y])
    left_hip  = np.array([p_x - hip_offset, pelvis_y])

    # Legs: simulate the swing of the legs.
    leg_swing_amp = 0.1
    # Right leg swings with the cycle phase.
    right_knee = right_hip + np.array([leg_swing_amp * np.sin(phase),
                                        -0.3])
    right_foot = right_hip + np.array([leg_swing_amp * np.sin(phase),
                                        -0.6])
    # Left leg swings in counter-phase.
    left_knee = left_hip + np.array([leg_swing_amp * np.sin(phase + np.pi),
                                      -0.3])
    left_foot = left_hip + np.array([leg_swing_amp * np.sin(phase + np.pi),
                                      -0.6])

    # Arrange positions in order as specified (15 joints):
    points = np.array([head,          # 1. Head
                       neck,          # 2. Neck
                       right_shoulder,# 3. Right Shoulder
                       right_elbow,   # 4. Right Elbow
                       right_hand,    # 5. Right Hand
                       left_shoulder, # 6. Left Shoulder
                       left_elbow,    # 7. Left Elbow
                       left_hand,     # 8. Left Hand
                       torso,         # 9. Torso (mid-spine)
                       right_hip,     # 10. Right Hip
                       right_knee,    # 11. Right Knee
                       right_foot,    # 12. Right Foot
                       left_hip,      # 13. Left Hip
                       left_knee,     # 14. Left Knee
                       left_foot])    # 15. Left Foot

    return points

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor('black')
ax.set_aspect('equal')
# The x limits adjust dynamically with the walking progress
ax.set_xlim(-0.5, speed * duration + 1)
ax.set_ylim(-1.0, 1.2)
ax.axis('off')  # Turn off the axis

# Initialize scatter plot with 15 points.
scatter = ax.scatter([], [], s=80, c='white')

# Animation update function.
def update(frame):
    t = frame / fps
    pts = compute_joint_positions(t)
    scatter.set_offsets(pts)
    return scatter,

# Create the animation.
anim = FuncAnimation(fig, update, frames=n_frames, interval=1000/fps, blit=True)

# Show the animation.
plt.show()