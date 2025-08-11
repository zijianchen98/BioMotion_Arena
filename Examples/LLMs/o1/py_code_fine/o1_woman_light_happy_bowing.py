#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This program displays a point-light stimulus (15 white points) on a black background
# depicting a lightweight "happywoman" performing a bowing motion. The motion
# is simplified but arranged to appear coherent and biomechanically plausible.

# ----------------------------------------------------
# Define base (neutral) coordinates for 15 major body points in a 2D plane:
#   0: Head
#   1: Chest
#   2: Pelvis
#   3: Right Shoulder
#   4: Right Elbow
#   5: Right Wrist
#   6: Left Shoulder
#   7: Left Elbow
#   8: Left Wrist
#   9: Right Hip
#  10: Right Knee
#  11: Right Ankle
#  12: Left Hip
#  13: Left Knee
#  14: Left Ankle
#
# The pelvis (index 2) will serve as the pivot for the bowing motion.

base_positions = np.array([
    [ 0.0,  6.0],  # Head
    [ 0.0,  5.0],  # Chest
    [ 0.0,  4.0],  # Pelvis
    [ 0.6,  5.0],  # Right Shoulder
    [ 0.9,  4.0],  # Right Elbow
    [ 1.0,  3.0],  # Right Wrist
    [-0.6,  5.0],  # Left Shoulder
    [-0.9,  4.0],  # Left Elbow
    [-1.0,  3.0],  # Left Wrist
    [ 0.4,  3.5],  # Right Hip
    [ 0.4,  2.0],  # Right Knee
    [ 0.4,  1.0],  # Right Ankle
    [-0.4,  3.5],  # Left Hip
    [-0.4,  2.0],  # Left Knee
    [-0.4,  1.0],  # Left Ankle
], dtype=float)

# Number of frames in the animation
N_FRAMES = 60

def bow_angle(frame):
    """
    Piecewise linear motion for the bow angle (in degrees).
    Frames 0..30: angle goes from 0° to 60°.
    Frames 31..60: angle goes from 60° back to 0°.
    """
    if frame <= 30:
        return 60.0 * (frame / 30.0)
    else:
        return 60.0 * (1.0 - (frame - 30.0) / 30.0)

def get_positions(frame):
    """
    Returns the 2D positions of the 15 points for the given frame.
    We'll rotate points above the pelvis (index >= 0) except for
    the pelvis and below it (hips, knees, ankles) remain mostly stable,
    aside from a slight shift to maintain coherence.
    """
    positions = base_positions.copy()

    # Convert angle to radians
    angle_deg = bow_angle(frame)
    angle_rad = np.deg2rad(angle_deg)

    # Define pivot (the pelvis) for rotation
    pivot = positions[2]  # [x_pelvis, y_pelvis]

    # Indices to rotate around the pelvis (upper body)
    upper_body_indices = [0, 1, 3, 4, 5, 6, 7, 8]

    # Rotation matrix around 'pivot'
    cos_a = np.cos(angle_rad)
    sin_a = np.sin(angle_rad)

    for i in upper_body_indices:
        # Translate point so pivot is at origin
        translated = positions[i] - pivot
        # Rotate
        rotated = np.array([
            cos_a * translated[0] - sin_a * translated[1],
            sin_a * translated[0] + cos_a * translated[1]
        ])
        # Translate back
        positions[i] = rotated + pivot

    # Optionally, add a slight forward shift of hips to keep balance
    shift_factor = 0.02 * angle_deg
    positions[9:, 0] += shift_factor

    return positions

# Create a figure and axis with black background
fig, ax = plt.subplots(figsize=(5, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Set up limits so the body remains visible
ax.set_xlim(-2, 2)
ax.set_ylim(0, 7)
ax.set_aspect('equal')  # Equal scaling for x and y axes
ax.axis('off')          # Hide axes

# Initialize scatter plot (15 white points)
scat = ax.scatter([], [], c='white', s=50)

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    # Get updated positions
    pos = get_positions(frame)
    scat.set_offsets(pos)
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=N_FRAMES, init_func=init, interval=50, blit=True)

# Show the animation window
plt.show()