#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------------------------------------------------------------------------------
# This Python program displays a point-light stimulus of a "Happy Man" running.
# The animation has exactly 15 white point-lights against a black background.
# The motion is a simplified, smooth, and coherent approximation of human running.
# ----------------------------------------------------------------------------------

# Global parameters for animation
FPS = 30             # Frames per second
DURATION = 3         # Total duration in seconds (feel free to adjust)
N_FRAMES = FPS * DURATION
T = np.linspace(0, 1, N_FRAMES, endpoint=False)  # Normalized time over 1 cycle

# Define body segments / joints to track (15 total points):
# 1: Head
# 2: Neck
# 3: Left Shoulder
# 4: Right Shoulder
# 5: Left Elbow
# 6: Right Elbow
# 7: Left Wrist
# 8: Right Wrist
# 9: Left Hip
# 10: Right Hip
# 11: Left Knee
# 12: Right Knee
# 13: Left Ankle
# 14: Right Ankle
# 15: Mid Torso

# For a simplified runner, we'll model arms and legs as sinusoidal motions
# around a "neutral" position. Vertical bobbing of the torso and head is also included.

def get_biological_motion_points(t):
    """
    Returns the (x, y) positions of the 15 points at time t in [0,1].
    The parameter 't' is normalized so that t=0 -> start of cycle, t=1 -> end of cycle.
    A simple sinusoidal approach approximates a running pattern.
    """

    # Running frequency (one cycle for t in [0,1])
    # We assume 2*pi for a single stride cycle
    phase = 2 * np.pi * t

    # Small vertical bob for torso and head (mimics running bounce)
    vertical_bounce = 0.03 * np.sin(2 * phase)

    # Amplitudes for arms and legs swinging
    arm_amplitude = 0.15
    leg_amplitude = 0.25

    # Arms swing out of phase: left arm forward while right arm back
    # For convenience, define sine for left side, -sine for right side
    left_arm_swing  = arm_amplitude * np.sin(phase)
    right_arm_swing = arm_amplitude * np.sin(phase + np.pi)

    # Legs swing roughly out of phase as well
    left_leg_swing  = leg_amplitude * np.sin(phase)
    right_leg_swing = leg_amplitude * np.sin(phase + np.pi)

    # Base positions (neutral stance) for each point
    # (x_0, y_0)
    base_positions = np.array([
        [0.0, 1.80],  # 1: Head
        [0.0, 1.60],  # 2: Neck
        [-0.10, 1.60],# 3: Left Shoulder
        [ 0.10, 1.60],# 4: Right Shoulder
        [-0.20, 1.45],# 5: Left Elbow
        [ 0.20, 1.45],# 6: Right Elbow
        [-0.25, 1.30],# 7: Left Wrist
        [ 0.25, 1.30],# 8: Right Wrist
        [-0.10, 1.20],# 9: Left Hip
        [ 0.10, 1.20],# 10: Right Hip
        [-0.10, 0.85],# 11: Left Knee
        [ 0.10, 0.85],# 12: Right Knee
        [-0.10, 0.50],# 13: Left Ankle
        [ 0.10, 0.50],# 14: Right Ankle
        [ 0.00, 1.40] # 15: Mid Torso
    ])

    # Apply vertical bounce to torso, head, shoulders, hips, mid torso
    torso_indices = [0, 1, 2, 3, 8, 9, 14]  # Head, Neck, Shoulders, Hips, ankles
    for idx in torso_indices:
        base_positions[idx, 1] += vertical_bounce

    # Arms: shift elbows and wrists horizontally to simulate swinging
    # Left elbow (index 4) and wrist (index 6)
    base_positions[4, 0] += left_arm_swing
    base_positions[6, 0] += left_arm_swing
    # Right elbow (index 5) and wrist (index 7)
    base_positions[5, 0] += right_arm_swing
    base_positions[7, 0] += right_arm_swing

    # Legs: shift knees and ankles horizontally to simulate stride
    # Left knee (index 10) and ankle (index 12)
    base_positions[10, 0] += left_leg_swing
    base_positions[12, 0] += left_leg_swing
    # Right knee (index 11) and ankle (index 13)
    base_positions[11, 0] += right_leg_swing
    base_positions[13, 0] += right_leg_swing

    return base_positions


# Setup the figure and axis (solid black background)
fig, ax = plt.subplots()
fig.set_facecolor("black")
ax.set_facecolor("black")

# Scatter plot for initial frame
points_data = get_biological_motion_points(0)
scatter = ax.scatter(points_data[:, 0], points_data[:, 1],
                     c="white", s=40, edgecolors="none")

# Remove axes for a cleaner stimulus display
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0.0, 2.0)
ax.axis("off")

def update(frame):
    """ Update function for each animation frame """
    t = T[frame]  # normalized time from 0 to 1
    new_points = get_biological_motion_points(t)

    # Update scatter plot with new positions
    scatter.set_offsets(new_points)

    return (scatter,)

# Create animation
anim = FuncAnimation(fig, update, frames=N_FRAMES, interval=1000/FPS, blit=True)

# Display the animation window
plt.show()