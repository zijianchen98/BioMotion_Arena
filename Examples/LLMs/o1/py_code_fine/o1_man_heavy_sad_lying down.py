#!/usr/bin/env python3
"""
Point-Light Biological Motion: A Sad Person Lying Down
-----------------------------------------------------
This program creates a 2D animation of 15 white point-lights representing
a sad person (heavily weighted) transitioning from standing to lying down
on a solid black background. The motion is kept smooth and biomechanically
plausible in a simplified way. After lying down, the figure exhibits a slow
"heavy breathing" motion.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -------------------------------------------------
# 1) DEFINE KEY FRAMES FOR 15 JOINTS (x, y)
# -------------------------------------------------
# Standing pose (frame 0)
KEYFRAME0 = np.array([
    [0.0, 1.80],  # Head
    [0.0, 1.60],  # Neck
    [-0.2, 1.60], # Shoulder L
    [ 0.2, 1.60], # Shoulder R
    [0.0, 1.40],  # Chest
    [-0.2, 1.10], # Hip L
    [ 0.2, 1.10], # Hip R
    [-0.2, 0.70], # Knee L
    [ 0.2, 0.70], # Knee R
    [-0.2, 0.30], # Foot L
    [ 0.2, 0.30], # Foot R
    [-0.3, 1.40], # Elbow L
    [ 0.3, 1.40], # Elbow R
    [-0.4, 1.20], # Hand L
    [ 0.4, 1.20]  # Hand R
])

# Lying-down pose (frame 1)
KEYFRAME1 = np.array([
    [0.50, 0.30],  # Head
    [0.45, 0.30],  # Neck
    [0.30, 0.32],  # Shoulder L
    [0.60, 0.32],  # Shoulder R
    [0.45, 0.30],  # Chest
    [0.30, 0.30],  # Hip L
    [0.60, 0.30],  # Hip R
    [0.30, 0.25],  # Knee L
    [0.60, 0.25],  # Knee R
    [0.30, 0.20],  # Foot L
    [0.60, 0.20],  # Foot R
    [0.28, 0.33],  # Elbow L
    [0.62, 0.33],  # Elbow R
    [0.25, 0.30],  # Hand L
    [0.65, 0.30]   # Hand R
])

# -------------------------------------------------
# 2) INTERPOLATION & BREATHING
# -------------------------------------------------
def smooth_step(t):
    """
    Smooth step function for blending between key frames.
    Range of t: 0 -> 1
    Returns a value in [0, 1] with slow in/out.
    """
    return 0.5 - 0.5 * np.cos(np.pi * t)

def get_positions(frame, total_frames=100):
    """
    Returns the (x, y) positions of all 15 points at the given animation frame.
    0 <= frame < total_frames
    """
    # Phase A: Transition from standing to lying (frames 0..50)
    # Phase B: Lying with slight "heavy breathing" (frames 51..99)
    midpoint = 50
    if frame <= midpoint:
        # Normalize t in [0, 1] for the transition
        t = frame / midpoint
        s = smooth_step(t)
        positions = KEYFRAME0 + s * (KEYFRAME1 - KEYFRAME0)
    else:
        # After lying down: slight up/down motion to simulate heavy breathing
        positions = KEYFRAME1.copy()
        # Let's have the chest and shoulders move a bit sinusoidally
        # so it looks like breathing. Frame 51..99 -> t in [0, 1]
        t = (frame - midpoint) / float(total_frames - midpoint - 1)
        # amplitude for breathing
        breath_amp = 0.02
        # sinusoidal offset
        offset = breath_amp * np.sin(2 * np.pi * 1.0 * t)
        # apply offset to chest(4) and shoulders(2,3) and neck(1)
        positions[4, 1] += offset  # Chest
        positions[1, 1] += 0.8 * offset  # Neck
        positions[2, 1] += 0.7 * offset  # Shoulder L
        positions[3, 1] += 0.7 * offset  # Shoulder R
    return positions

# -------------------------------------------------
# 3) ANIMATION SETUP
# -------------------------------------------------
fig, ax = plt.subplots()
# Make the background black
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Prepare scatter for 15 white points against black background
scatter = ax.scatter([], [], s=50, c='white')
ax.set_xlim(-1.0, 1.5)
ax.set_ylim(0.0, 2.0)
ax.set_aspect('equal')
plt.axis('off')

def init():
    """Initialize the scatter object with empty data."""
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    """Update scatter data for each animation frame."""
    positions = get_positions(frame)
    scatter.set_offsets(positions)
    return (scatter,)

# -------------------------------------------------
# 4) RUN THE ANIMATION
# -------------------------------------------------
ani = animation.FuncAnimation(
    fig, update, frames=100, init_func=init, blit=True, interval=60
)

plt.show()