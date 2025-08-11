#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This program generates a point-light stimulus animation (2D) depicting a
# "sad" posture with a heavy weight, waving a hand. The animation uses
# 15 point-lights (white on a black background) in a biomechanically
# plausible manner.

# Number of frames in the animation
NUM_FRAMES = 120

# We define 15 points: 
# (1) Head, (2) Neck, (3) R_Shoulder, (4) R_Elbow, (5) R_Wrist,
# (6) L_Shoulder, (7) L_Elbow, (8) L_Wrist, (9) R_Hip, (10) R_Knee,
# (11) R_Ankle, (12) L_Hip, (13) L_Knee, (14) L_Ankle, (15) Torso_Center.
NUM_POINTS = 15

# Basic body layout in a neutral pose (somewhat slumped forward).
# We'll store relative "rest" positions (x, y). Then we'll apply
# time-varying transformations to generate the wave and sad posture.
body_rest = np.array([
    [0.0,   1.0],  # Head
    [0.0,   0.8],  # Neck
    [0.2,   0.8],  # R_Shoulder
    [0.3,   0.6],  # R_Elbow
    [0.35,  0.4],  # R_Wrist
    [-0.2,  0.8],  # L_Shoulder
    [-0.3,  0.6],  # L_Elbow
    [-0.35, 0.4],  # L_Wrist
    [0.1,   0.4],  # R_Hip
    [0.1,   0.2],  # R_Knee
    [0.1,   0.0],  # R_Ankle
    [-0.1,  0.4],  # L_Hip
    [-0.1,  0.2],  # L_Knee
    [-0.1,  0.0],  # L_Ankle
    [0.0,   0.6]   # Torso_Center
])

def get_joint_positions(frame):
    """
    Returns an array of shape (NUM_POINTS, 2) containing x,y positions
    of the 15 joints for a given animation frame. 
    """

    # Normalize the frame to a fraction of a full wave cycle
    t = frame / NUM_FRAMES  # t goes from 0 to 1

    # Make a deep copy of the resting positions
    joints = body_rest.copy()

    # Simple "bobbing" to show weight (body goes up and down slightly).
    # We'll use a slow sine wave for this.
    bob_amplitude = 0.03
    bob_offset = bob_amplitude * np.sin(2 * np.pi * 0.5 * t)
    joints[:, 1] += bob_offset

    # Slight forward bend to appear "sad":
    # We'll rotate everything (except the legs below hips) a bit.
    # The rotation angle will be small but present at all times.
    angle_sad = np.radians(10)
    rotation_matrix_sad = np.array([
        [np.cos(angle_sad), -np.sin(angle_sad)],
        [np.sin(angle_sad),  np.cos(angle_sad)]
    ])
    # We rotate points that are above the hips. We'll pick indices
    # for Head, Neck, Shoulders, Elbows, Wrists, Torso_Center.
    upper_body_indices = [0, 1, 2, 3, 4, 5, 6, 7, 14]
    for idx in upper_body_indices:
        # Shift to origin, rotate, shift back
        shift = joints[idx] - joints[8]  # shift relative to R_Hip
        shifted_rotated = rotation_matrix_sad @ shift
        joints[idx] = joints[8] + shifted_rotated

    # Wave the right hand. We'll treat the R_Elbow and R_Wrist as
    # rotating around the R_Shoulder. Let's define a wave motion
    # with a small amplitude in the elbow joint.
    wave_angle = 0.4 * np.sin(2 * np.pi * 2.0 * t)  # freq=2 cycles over full
    # Rotate elbow and wrist about the R_Shoulder (index 2)
    r_shoulder_pos = joints[2]
    # Indices for R_Elbow (3), R_Wrist (4)
    wave_indices = [3, 4]
    rot_wave = np.array([
        [np.cos(wave_angle), -np.sin(wave_angle)],
        [np.sin(wave_angle),  np.cos(wave_angle)]
    ])
    for idx in wave_indices:
        shift = joints[idx] - r_shoulder_pos
        shifted_rotated = rot_wave @ shift
        joints[idx] = r_shoulder_pos + shifted_rotated

    # Return final positions for this frame
    return joints

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')  # Figure background
ax.set_facecolor('black')         # Axes background

# Initialize scatter object for points (white color)
scatter = ax.scatter([], [], c='white', s=30)

# Set axis limits and hide axes
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-0.1, 1.2)
plt.axis('off')

def init():
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    # Get the joint positions for this frame
    joints = get_joint_positions(frame)
    scatter.set_offsets(joints)
    return (scatter,)

ani = FuncAnimation(fig, update, frames=NUM_FRAMES, init_func=init,
                    interval=50, blit=True, repeat=True)

plt.show()