
"""
This Python program shows an animation of a 15‐point biological motion stimulus.
The stimulus is intended to represent a “sadman with light weight” sitting down.
Each frame displays exactly 15 white point‐lights (as scatter markers)
against a solid black background. The motion from a standing posture to a sitting posture
is produced with smooth, biomechanically plausible interpolation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Total number of frames for the animation
num_frames = 100
interval = 40  # in milliseconds

# Define the indices for the 15 joints (points)
# Our chosen joints:
# 0: Head
# 1: Left Shoulder
# 2: Right Shoulder
# 3: Left Elbow
# 4: Right Elbow
# 5: Left Hand
# 6: Right Hand
# 7: Thorax (center upper torso)
# 8: Left Hip
# 9: Right Hip
# 10: Left Knee
# 11: Right Knee
# 12: Left Ankle
# 13: Right Ankle
# 14: Spine Base

# Define the starting positions (standing posture) for each joint (x, y)
standing = np.array([
    [0.0, 8.0],    # Head
    [-1.0, 7.0],   # Left Shoulder
    [1.0, 7.0],    # Right Shoulder
    [-1.5, 6.0],   # Left Elbow
    [1.5, 6.0],    # Right Elbow
    [-1.5, 5.0],   # Left Hand
    [1.5, 5.0],    # Right Hand
    [0.0, 7.0],    # Thorax
    [-0.5, 5.5],   # Left Hip
    [0.5, 5.5],    # Right Hip
    [-0.5, 4.0],   # Left Knee
    [0.5, 4.0],    # Right Knee
    [-0.5, 2.0],   # Left Ankle
    [0.5, 2.0],    # Right Ankle
    [0.0, 5.0]     # Spine Base
])

# Define the ending positions (sitting posture) for each joint (x, y).
# The posture suggests the figure has lowered and bent its legs.
sitting = np.array([
    [0.0, 7.2],    # Head slightly lowered
    [-1.0, 6.5],   # Left Shoulder
    [1.0, 6.5],    # Right Shoulder
    [-1.2, 6.0],   # Left Elbow closer to body
    [1.2, 6.0],    # Right Elbow closer to body
    [-1.2, 5.5],   # Left Hand
    [1.2, 5.5],    # Right Hand
    [0.0, 6.5],    # Thorax
    [-0.5, 4.8],   # Left Hip (moved down)
    [0.5, 4.8],    # Right Hip (moved down)
    [-0.2, 4.0],   # Left Knee bent forward
    [0.2, 4.0],    # Right Knee bent forward
    [-0.2, 3.0],   # Left Ankle
    [0.2, 3.0],    # Right Ankle
    [0.0, 4.8]     # Spine Base lowered to hip level
])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(5, 8))
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot with white dot markers (point-lights)
scatter = ax.scatter(standing[:, 0], standing[:, 1], s=100, c='white')

# Easing function for smooth interpolation (using cosine easing)
def ease(t):
    # t goes from 0 to 1; use half cosine to start and slow down at the end.
    # This results in a smooth start and finish.
    return 0.5 * (1 - np.cos(np.pi * t))

def interpolate_points(p0, p1, t):
    """Interpolate between two sets of points p0 and p1 given parameter t."""
    s = ease(t)
    return p0 + s * (p1 - p0)

def update(frame):
    # Calculate progress from 0 to 1
    t = frame / (num_frames - 1)
    # Compute the new positions
    new_positions = interpolate_points(standing, sitting, t)
    # Update the scatter data
    scatter.set_offsets(new_positions)
    return scatter,

# Create the animation
anim = FuncAnimation(fig, update, frames=num_frames, interval=interval, blit=True)

# To display the animation in a blocking window, use plt.show().
# Alternatively, save the animation to a file (e.g., mp4 or gif) if desired.
if __name__ == "__main__":
    plt.show()