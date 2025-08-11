#!/usr/bin/env python3
"""
Biological Motion: Point-Light Display of a Woman Waving Her Hand

This script uses matplotlib to create a point-light stimulus animation.
Fifteen white point-lights representing a lightweight "happywoman" are
drawn against a black background. The motion is a simple, coherent,
biologically plausible wave of the right hand.

Usage:
    python3 point_light_waving.py
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -----------------------------------------------------------------------------
# Define base (static) positions for 15 key points (X, Y).
# These coordinates roughly represent a frontal view of a standing person.

BASE_POINTS = np.array([
    [ 0.00, 1.70],  # 0: Head
    [ 0.00, 1.50],  # 1: Neck
    [ 0.00, 1.30],  # 2: Torso center
    [ 0.20, 1.45],  # 3: Right shoulder
    [ 0.35, 1.30],  # 4: Right elbow
    [ 0.45, 1.15],  # 5: Right wrist (this will wave)
    [-0.20, 1.45],  # 6: Left shoulder
    [-0.35, 1.30],  # 7: Left elbow
    [-0.45, 1.15],  # 8: Left wrist
    [ 0.10, 1.10],  # 9: Right hip
    [ 0.10, 0.60],  # 10: Right knee
    [ 0.10, 0.00],  # 11: Right ankle
    [-0.10, 1.10],  # 12: Left hip
    [-0.10, 0.60],  # 13: Left knee
    [-0.10, 0.00],  # 14: Left ankle
], dtype=np.float32)

# Index for key points we will animate:
RIGHT_ELBOW_INDEX = 4
RIGHT_WRIST_INDEX = 5

# Number of animation frames and frames per second
NUM_FRAMES = 60
FPS = 30

# Wave parameters
# We'll pivot the right wrist around the right elbow with a simple sinusoidal motion.
# The elbow is at BASE_POINTS[RIGHT_ELBOW_INDEX], and the rest wrist is at BASE_POINTS[RIGHT_WRIST_INDEX].
# We'll vary the angle from a "resting angle" by a small amplitude for a natural waving motion.

# Calculate the rest angle and radius from elbow to wrist
elbow_x, elbow_y = BASE_POINTS[RIGHT_ELBOW_INDEX]
wrist_x, wrist_y = BASE_POINTS[RIGHT_WRIST_INDEX]
dx = wrist_x - elbow_x
dy = wrist_y - elbow_y
rest_radius = np.hypot(dx, dy)
rest_angle = np.arctan2(dy, dx)

# Let the wave amplitude be +/- 20 degrees around the rest angle
wave_amplitude_deg = 20.0
wave_amplitude_rad = np.deg2rad(wave_amplitude_deg)
rest_angle_rad = rest_angle  # The "average" elbow-to-wrist angle
wave_period = 30  # frames per full wave cycle

def generate_frame_points(frame: int) -> np.ndarray:
    """
    Given a frame index, return the 2D positions of the 15 points.
    We'll wave the right wrist (index 5) around the right elbow (index 4).
    """
    points = BASE_POINTS.copy()

    # Compute wave angle:
    # We'll do a sine wave around the rest_angle with amplitude wave_amplitude_rad.
    # The wave cycles every 'wave_period' frames.
    angle_offset = wave_amplitude_rad * np.sin(2.0 * np.pi * frame / wave_period)
    current_angle = rest_angle_rad + angle_offset

    # Recompute wrist position
    new_wrist_x = elbow_x + rest_radius * np.cos(current_angle)
    new_wrist_y = elbow_y + rest_radius * np.sin(current_angle)
    points[RIGHT_WRIST_INDEX] = [new_wrist_x, new_wrist_y]

    return points


def init_animation():
    """Initialize the animation scatter plot."""
    scat.set_offsets(generate_frame_points(0))
    return (scat,)


def update_animation(frame):
    """Update the scatter plot for each frame."""
    frame_points = generate_frame_points(frame)
    scat.set_offsets(frame_points)
    return (scat,)


# -----------------------------------------------------------------------------
# Set up the matplotlib figure and animation.

fig, ax = plt.subplots()
fig.set_facecolor("black")  # Black background
ax.set_facecolor("black")
ax.set_aspect("equal", adjustable="datalim")

# Scatter plot setup: 15 points, colored white, no edges.
scat = ax.scatter(
    BASE_POINTS[:, 0],
    BASE_POINTS[:, 1],
    c="white",
    edgecolor="none",
    s=40
)

# Hide axis
plt.axis("off")

# Set reasonable viewing limits
all_x = BASE_POINTS[:, 0]
all_y = BASE_POINTS[:, 1]
pad = 0.5
ax.set_xlim(all_x.min() - pad, all_x.max() + pad)
ax.set_ylim(all_y.min() - pad, all_y.max() + pad)

# Create animation
ani = animation.FuncAnimation(
    fig,
    update_animation,
    frames=NUM_FRAMES,
    init_func=init_animation,
    blit=True,
    interval=1000/FPS,
    repeat=True
)

# Show the animation window
if __name__ == "__main__":
    plt.show()