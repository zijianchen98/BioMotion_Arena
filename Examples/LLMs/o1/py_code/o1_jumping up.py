#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# This program creates a 2D point-light animation of a man jumping up,
# using 15 white points on a black background.

# Define time parameters
FPS = 30
DURATION = 2.0  # seconds
N_FRAMES = int(FPS * DURATION)
TIMES = np.linspace(0, DURATION, N_FRAMES, endpoint=False)

# We will define 15 distinct points composing a simple "skeleton"
# for a man performing a jump. The indices will be:
#  0: Head
#  1: Neck
#  2: Right Shoulder
#  3: Right Elbow
#  4: Right Wrist
#  5: Left Shoulder
#  6: Left Elbow
#  7: Left Wrist
#  8: Right Hip
#  9: Right Knee
# 10: Right Ankle
# 11: Left Hip
# 12: Left Knee
# 13: Left Ankle
# 14: Torso Center

def interpolate(a, b, t):
    """Linear interpolation from a to b over parameter t in [0,1]."""
    return a + (b - a) * t

def get_skeleton_positions(t):
    """
    Return an array of shape (15, 2) containing (x, y) coords
    of the 15 points at time t (in seconds).
    We'll define a roughly plausible jump cycle from t=0s to t=2s.
    """

    # We define four key time intervals:
    #  1) 0.0 - 0.4s: crouch
    #  2) 0.4 - 1.0s: upward thrust
    #  3) 1.0 - 1.4s: in-air (peak)
    #  4) 1.4 - 2.0s: landing
    
    # Base positions (standing):
    # These baseline coords are for a standing posture at t=0 (x, y).
    # We'll adjust them during the phases of jump.
    base = np.array([
        [ 0.00, 1.60],  # Head
        [ 0.00, 1.45],  # Neck
        [ 0.20, 1.40],  # Right Shoulder
        [ 0.25, 1.15],  # Right Elbow
        [ 0.25, 0.95],  # Right Wrist
        [-0.20, 1.40],  # Left Shoulder
        [-0.25, 1.15],  # Left Elbow
        [-0.25, 0.95],  # Left Wrist
        [ 0.15, 1.00],  # Right Hip
        [ 0.15, 0.55],  # Right Knee
        [ 0.15, 0.00],  # Right Ankle
        [-0.15, 1.00],  # Left Hip
        [-0.15, 0.55],  # Left Knee
        [-0.15, 0.00],  # Left Ankle
        [ 0.00, 1.20],  # Torso Center
    ])

    # We'll move the entire skeleton up/down, plus bend knees/arms slightly.
    # Define piecewise t in [0, 2]
    # We'll compress/extend the legs to reflect the jump cycle,
    # as well as shift arms slightly.

    # Phase definitions:
    if 0.0 <= t < 0.4:
        # Crouch: pelvis goes from y=1.0 down to y=0.7
        phase_t = (t - 0.0) / 0.4
        pelvis_shift = interpolate(0.0, -0.3, phase_t)  # shift entire body down
        knee_bend_factor = interpolate(0.0, 0.2, phase_t)  # bend knees
        arm_bend_factor = interpolate(0.0, 0.1, phase_t)
    elif 0.4 <= t < 1.0:
        # Upward thrust: pelvis goes from y=0.7 to y=1.4
        phase_t = (t - 0.4) / 0.6
        pelvis_shift = interpolate(-0.3, 0.4, phase_t)
        knee_bend_factor = interpolate(0.2, -0.1, phase_t)
        arm_bend_factor = interpolate(0.1, 0.05, phase_t)
    elif 1.0 <= t < 1.4:
        # In-air: pelvis around the peak
        phase_t = (t - 1.0) / 0.4
        pelvis_shift = interpolate(0.4, 0.5, phase_t)
        knee_bend_factor = interpolate(-0.1, 0.0, phase_t)
        arm_bend_factor = interpolate(0.05, 0.0, phase_t)
    else:
        # Landing: pelvis returns to y=1.0 by 2.0s
        phase_t = (t - 1.4) / 0.6
        pelvis_shift = interpolate(0.5, 0.0, phase_t)
        knee_bend_factor = interpolate(0.0, 0.2, phase_t)
        arm_bend_factor = interpolate(0.0, 0.1, phase_t)

    coords = base.copy()

    # Shift entire body in the y direction
    coords[:,1] += pelvis_shift

    # Bend the knees: move knees and ankles up toward hips
    # We'll move knee up and keep ankle a bit closer.
    # Right Knee (idx=9), Left Knee (idx=12)
    knee_indices = [9, 12]
    for k in knee_indices:
        coords[k,1] -= knee_bend_factor * 0.25
    # Shift ankles up less
    ankle_indices = [10, 13]
    for a in ankle_indices:
        coords[a,1] -= knee_bend_factor * 0.15

    # Arms bend: shift elbows/wrists upward a bit
    # Right Elbow (3), Left Elbow (6), Right Wrist (4), Left Wrist (7)
    elbow_indices = [3, 6]
    wrist_indices = [4, 7]
    for e in elbow_indices:
        coords[e,1] += arm_bend_factor * 0.10
    for w in wrist_indices:
        coords[w,1] += arm_bend_factor * 0.15

    return coords

# Create figure and axes
fig, ax = plt.subplots(figsize=(5, 5))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-0.2, 2.0)
ax.set_aspect("equal")
ax.axis("off")

# Initialize scatter plot for 15 points
scatter = ax.scatter([], [], c="white", s=50)

def init():
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    t = TIMES[frame]
    coords = get_skeleton_positions(t)
    scatter.set_offsets(coords)
    return (scatter,)

ani = animation.FuncAnimation(
    fig, update, frames=N_FRAMES, init_func=init, interval=1000/FPS, blit=True
)

plt.show()