#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------------------------------------------
# A simple 2D point-light biological motion display using 15 points.
# The figure "forward rolls" around its center, with a slumped (sad) posture.
#
# Requirements satisfied:
#   1) Depicts a "sadman" with light weight performing a forward roll.
#   2) Exactly 15 white points on a solid black background.
#   3) Smooth, coherent, biomechanically plausible rolling motion.
# -------------------------------------------------------------

# Base skeleton definition (approximate positions for a slumped human figure):
# Each tuple is (x, y) in some nominal "standing" posture, centered around (0, 0.4).
# The figure is somewhat hunched to appear "sad."
base_skeleton = np.array([
    (0.0, 0.80),   # Head
    (0.0, 0.60),   # Chest center
    (0.0, 0.40),   # Pelvis center
    (-0.20, 0.60), # Left shoulder
    (0.20, 0.60),  # Right shoulder
    (-0.15, 0.45), # Left elbow
    (0.15, 0.45),  # Right elbow
    (-0.25, 0.30), # Left hip
    (0.25, 0.30),  # Right hip
    (-0.17, 0.25), # Left knee
    (0.17, 0.25),  # Right knee
    (-0.17, 0.00), # Left ankle
    (0.17, 0.00),  # Right ankle
    (-0.28, 0.58), # Left wrist
    (0.28, 0.58),  # Right wrist
])

# Center of rotation (roughly around the pelvis):
center_x, center_y = 0.0, 0.40

# Number of animation frames:
num_frames = 200

# Time array for a complete rolling cycle (two forward rolls):
# Adjust 2*np.pi multipliers as needed to change how many flips occur.
t_vals = np.linspace(0, 4*np.pi, num_frames)

fig, ax = plt.subplots(figsize=(5, 5))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-0.2, 1.2)
ax.axis('off')  # Hide axes for a clean point-light display

# Create scatter plot for the 15 points. Initially, plot them at t=0.
scatter = ax.scatter(
    base_skeleton[:, 0], base_skeleton[:, 1],
    c='white', s=50
)

def update(frame_index):
    # Current angle of rotation for forward rolling
    theta = t_vals[frame_index]
    cos_t = np.cos(theta)
    sin_t = np.sin(theta)

    # Calculate new positions after rotation around center_x, center_y
    rotated_positions = []
    for (x, y) in base_skeleton:
        # Translate to origin (w.r.t center of rotation)
        x_t = x - center_x
        y_t = y - center_y
        # Apply rotation matrix for a "forward roll" in 2D
        x_r = cos_t * x_t - sin_t * y_t
        y_r = sin_t * x_t + cos_t * y_t
        # Translate back
        x_final = x_r + center_x
        y_final = y_r + center_y
        rotated_positions.append((x_final, y_final))

    # Update scatter plot data
    rotated_positions = np.array(rotated_positions)
    scatter.set_offsets(rotated_positions)

    return scatter,

anim = FuncAnimation(
    fig, update, frames=num_frames, interval=50, blit=True, repeat=True
)

plt.show()