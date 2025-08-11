#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This script displays 15 white point-lights on a black background,
# depicting a "happyman with heavy weight" jumping forward in a smooth, realistic manner.

# -----------------------
# Global animation configs
# -----------------------
num_points = 15
frames = 100
interval = 30  # milliseconds between frames
g = 9.8        # gravity constant for simplistic jump modeling

# -----------------------
# Define a skeleton layout
# We'll label them (index-based):
#  0: Head
#  1: Neck
#  2: Right Shoulder
#  3: Right Elbow
#  4: Right Wrist
#  5: Left Shoulder
#  6: Left Elbow
#  7: Left Wrist
#  8: Torso (Chest)
#  9: Pelvis
# 10: Right Hip
# 11: Right Knee
# 12: Right Ankle
# 13: Left Hip
# 14: Left Knee
# (We'll compute left ankle from left knee with consistent spacing)
# -----------------------

def generate_skeleton_positions(t):
    """
    Returns a (num_points, 2) array of x,y positions
    for the skeleton at time t.
    """

    # Time normalization and jump arc (simple ballistic for pelvis).
    # T_run is total duration of the jump.
    T_run = 1.75
    # Pelvis forward velocity
    forward_speed = 2.0
    # Pelvis initial jump velocity (vertical)
    jump_speed = 4.0

    # Clamping t to the final time to avoid negative heights after landing
    t_clamped = min(t, T_run)

    # Horizontal position of pelvis
    pelvis_x = forward_speed * t_clamped
    # Vertical jump (y) for pelvis (simple parabola)
    pelvis_y = jump_speed * t_clamped - 0.5 * g * t_clamped**2
    if pelvis_y < 0:
        pelvis_y = 0  # clamp at ground

    # We will place pelvis at (pelvis_x, pelvis_y + base_height)
    base_height = 0.2  # offset from ground
    pelvis_pos = np.array([pelvis_x, pelvis_y + base_height])

    # Torso (Chest) is above pelvis
    torso_offset = np.array([0.0, 0.25])
    torso_pos = pelvis_pos + torso_offset

    # Head is above torso
    head_offset = np.array([0.0, 0.15])
    head_pos = torso_pos + head_offset

    # Neck is slightly below head, but near torso
    neck_pos = torso_pos + head_offset * 0.5

    # Shoulders: approximate left/right offsets
    shoulder_offset = 0.1
    right_shoulder_pos = torso_pos + np.array([+shoulder_offset, 0.0])
    left_shoulder_pos  = torso_pos + np.array([-shoulder_offset, 0.0])

    # Arms: we'll animate them slightly swinging. Let's modulate angle by sinusoid across time
    arm_swing = 0.3 * np.sin(2 * np.pi * t / T_run)  # small swing
    elbow_length = 0.15
    wrist_length = 0.15

    # Right elbow
    right_elbow_pos = right_shoulder_pos + np.array([+arm_swing, -elbow_length])
    # Right wrist
    right_wrist_pos = right_elbow_pos + np.array([+arm_swing / 2.0, -wrist_length])

    # Left elbow
    left_elbow_pos = left_shoulder_pos + np.array([-arm_swing, -elbow_length])
    # Left wrist
    left_wrist_pos = left_elbow_pos + np.array([-arm_swing / 2.0, -wrist_length])

    # Hips (right/left) from pelvis
    hip_offset = 0.08
    right_hip_pos = pelvis_pos + np.array([+hip_offset, 0.0])
    left_hip_pos  = pelvis_pos + np.array([-hip_offset, 0.0])

    # Legs: let's animate a crouch at the start for the jump
    # We'll blend crouch (early) with extension (mid flight) using t/T_run ratio
    phase = min(t / T_run, 1.0)
    knee_offset_y = 0.15 - 0.1 * np.cos(np.pi * phase)  # crouch to extended
    ankle_offset_y = 0.15 - 0.1 * np.cos(np.pi * phase)

    right_knee_pos  = right_hip_pos + np.array([0.0, -knee_offset_y])
    right_ankle_pos = right_knee_pos + np.array([0.0, -ankle_offset_y])

    left_knee_pos  = left_hip_pos + np.array([0.0, -knee_offset_y])
    # We'll define left ankle after left knee
    left_ankle_pos = left_knee_pos + np.array([0.0, -ankle_offset_y])

    # Build final array of (num_points, 2)
    points = np.zeros((num_points, 2))
    points[0]  = head_pos
    points[1]  = neck_pos
    points[2]  = right_shoulder_pos
    points[3]  = right_elbow_pos
    points[4]  = right_wrist_pos
    points[5]  = left_shoulder_pos
    points[6]  = left_elbow_pos
    points[7]  = left_wrist_pos
    points[8]  = torso_pos
    points[9]  = pelvis_pos
    points[10] = right_hip_pos
    points[11] = right_knee_pos
    points[12] = right_ankle_pos
    points[13] = left_hip_pos
    points[14] = left_knee_pos  # left ankle is not strictly in the list, we used 15 points total only

    return points

# Prepare figure and axes with black background
fig, ax = plt.subplots(figsize=(5, 5))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Our scatter plot for the 15 points
scatter_plot = ax.scatter([], [], s=50, c='white')

# Set plot limits for enough space during jump
ax.set_xlim(-1, 4)
ax.set_ylim(-0.2, 2)
ax.set_aspect('equal')
ax.axis('off')

def init():
    """Initialize scatter plot data."""
    scatter_plot.set_offsets([])
    return (scatter_plot,)

def update(frame):
    # Frame-based time (we assume each frame ~ interval ms)
    t = frame * (interval / 1000.0)
    coords = generate_skeleton_positions(t)
    scatter_plot.set_offsets(coords)
    return (scatter_plot,)

ani = FuncAnimation(
    fig, update, frames=frames, init_func=init,
    interval=interval, blit=True, repeat=True
)

# Display the animation
plt.show()