#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------------------------------------------------------
# This program displays a 2D point-light biological motion stimulus of a
# "sadman carrying heavy weight" who performs a forward jump. 
# There are exactly 15 white point-lights arranged on a black background.
# The motion is defined by four keyframes that are linearly interpolated
# to produce smooth, biomechanically plausible animation.
# -----------------------------------------------------------------------------

# Define four keyframes, each containing 15 points in 2D (x, y).
# The points here are:
#  0:  head
#  1:  neck
#  2:  right shoulder
#  3:  right elbow
#  4:  right wrist
#  5:  left shoulder
#  6:  left elbow
#  7:  left wrist
#  8:  right hip
#  9:  right knee
# 10:  right ankle
# 11:  left hip
# 12:  left knee
# 13:  left ankle
# 14:  chest center

keyframes = [
    # Keyframe 0: Sad stance, slightly slouched
    np.array([
        [2.0, 8.0],  # head
        [2.0, 7.2],  # neck
        [2.2, 7.2],  # right shoulder
        [2.3, 6.7],  # right elbow
        [2.35, 6.2], # right wrist
        [1.8, 7.2],  # left shoulder
        [1.7, 6.7],  # left elbow
        [1.65, 6.2], # left wrist
        [2.1, 5.5],  # right hip
        [2.1, 4.5],  # right knee
        [2.1, 3.5],  # right ankle
        [1.9, 5.5],  # left hip
        [1.9, 4.5],  # left knee
        [1.9, 3.5],  # left ankle
        [2.0, 6.6],  # chest center
    ]),
    # Keyframe 1: Crouched, preparing to jump
    np.array([
        [2.2, 7.6],  # head
        [2.2, 6.9],  # neck
        [2.4, 6.9],  # right shoulder
        [2.5, 6.4],  # right elbow
        [2.55, 5.9], # right wrist
        [2.0, 6.9],  # left shoulder
        [1.9, 6.4],  # left elbow
        [1.85, 5.9], # left wrist
        [2.3, 5.0],  # right hip
        [2.3, 4.0],  # right knee
        [2.3, 3.2],  # right ankle
        [2.1, 5.0],  # left hip
        [2.1, 4.0],  # left knee
        [2.1, 3.2],  # left ankle
        [2.2, 6.3],  # chest center
    ]),
    # Keyframe 2: Mid-air jump, moving forward and upward
    np.array([
        [3.0, 9.0],  # head
        [3.0, 8.3],  # neck
        [3.2, 8.3],  # right shoulder
        [3.3, 7.8],  # right elbow
        [3.35, 7.3], # right wrist
        [2.8, 8.3],  # left shoulder
        [2.7, 7.8],  # left elbow
        [2.65, 7.3], # left wrist
        [3.1, 6.8],  # right hip
        [3.1, 6.1],  # right knee
        [3.1, 5.5],  # right ankle
        [2.9, 6.8],  # left hip
        [2.9, 6.1],  # left knee
        [2.9, 5.5],  # left ankle
        [3.0, 7.7],  # chest center
    ]),
    # Keyframe 3: Landing, leaning forward with bent knees
    np.array([
        [4.0, 7.8],  # head
        [4.0, 7.0],  # neck
        [4.2, 7.0],  # right shoulder
        [4.3, 6.5],  # right elbow
        [4.35, 6.0], # right wrist
        [3.8, 7.0],  # left shoulder
        [3.7, 6.5],  # left elbow
        [3.65, 6.0], # left wrist
        [4.1, 5.4],  # right hip
        [4.1, 4.4],  # right knee
        [4.1, 3.5],  # right ankle
        [3.9, 5.4],  # left hip
        [3.9, 4.4],  # left knee
        [3.9, 3.5],  # left ankle
        [4.0, 6.4],  # chest center
    ]),
]

# Number of frames in the entire animation
# We'll have 3 segments (0->1, 1->2, 2->3), each with 25 in-between frames => 75 frames total.
FRAMES_PER_SEGMENT = 25
TOTAL_FRAMES = FRAMES_PER_SEGMENT * (len(keyframes) - 1)

# Interpolation function:
def interpolate_keyframes(frame_idx):
    """
    Given the global animation frame index (0..TOTAL_FRAMES-1),
    determine which keyframes we are between and compute an interpolated frame.
    """
    # Each segment covers FRAMES_PER_SEGMENT frames
    segment = frame_idx // FRAMES_PER_SEGMENT        # which pair of keyframes
    alpha = (frame_idx % FRAMES_PER_SEGMENT) / float(FRAMES_PER_SEGMENT)
    
    # Start and end frames for this segment
    start_pts = keyframes[segment]
    end_pts = keyframes[segment + 1]
    
    # Linear interpolation
    return (1 - alpha) * start_pts + alpha * end_pts

# Set up the figure and axes for animation
fig, ax = plt.subplots(figsize=(6, 6))
# Make background black
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Set up scatter for 15 points (white color)
scatter_plot = ax.scatter([], [], s=60, c='white')

# Adjust plot limits so we can see the jump comfortably
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
# Remove axes ticks, spines, etc., to keep just black background with points
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

def init():
    """Initialize scatter data."""
    scatter_plot.set_offsets([])
    return (scatter_plot,)

def update(frame):
    """Update function for animation, called once per frame."""
    points = interpolate_keyframes(frame)
    scatter_plot.set_offsets(points)
    return (scatter_plot,)

# Create the animation
anim = FuncAnimation(
    fig, update, frames=TOTAL_FRAMES, 
    init_func=init, interval=50, blit=True, repeat=True
)

# Show the animation on screen
plt.show()