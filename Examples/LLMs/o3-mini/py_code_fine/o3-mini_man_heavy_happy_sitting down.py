
"""
This program displays an animation of a 15‐point “point‐light” stimulus against a black background.
The 15 points represent a simplified human skeleton (head, shoulders, elbows, hands, chest,
belly, hips, knees, and feet) whose pose transitions in a biomechanically plausible way from
standing to sitting. The character is a "happy man with heavy weight" sitting down.
The animation is generated using matplotlib’s animation module.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Define the initial (standing) and final (sitting) poses.
# We use 15 points corresponding to: 
#  0: Head
#  1: Left Shoulder,  2: Right Shoulder
#  3: Left Elbow,     4: Right Elbow
#  5: Left Hand,      6: Right Hand
#  7: Chest
#  8: Belly
#  9: Left Hip,      10: Right Hip
# 11: Left Knee,     12: Right Knee
# 13: Left Foot,     14: Right Foot

# Standing pose coordinates (x, y). These are chosen to provide a natural standing posture.
standing = np.array([
    [0.0, 0.90],    # Head
    [-0.10, 0.80],  # Left Shoulder
    [ 0.10, 0.80],  # Right Shoulder
    [-0.20, 0.70],  # Left Elbow
    [ 0.20, 0.70],  # Right Elbow
    [-0.25, 0.60],  # Left Hand
    [ 0.25, 0.60],  # Right Hand
    [0.0, 0.75],    # Chest
    [0.0, 0.65],    # Belly
    [-0.10, 0.60],  # Left Hip
    [ 0.10, 0.60],  # Right Hip
    [-0.10, 0.40],  # Left Knee
    [ 0.10, 0.40],  # Right Knee
    [-0.10, 0.20],  # Left Foot
    [ 0.10, 0.20]   # Right Foot
])

# Sitting pose coordinates.
# In a sitting pose the whole body is lowered, the trunk is maintained but slightly reclined,
# and the legs are bent. To mimic heaviness, the motion is slower and the body settles more.
sitting = np.array([
    [0.0, 0.60],    # Head (lowered)
    [-0.10, 0.55],  # Left Shoulder (lowered)
    [ 0.10, 0.55],  # Right Shoulder (lowered)
    [-0.20, 0.55],  # Left Elbow (arm moved slightly down)
    [ 0.20, 0.55],  # Right Elbow
    [-0.25, 0.55],  # Left Hand
    [ 0.25, 0.55],  # Right Hand
    [0.0, 0.55],    # Chest
    [0.0, 0.55],    # Belly (the torso becomes nearly horizontal)
    [-0.10, 0.55],  # Left Hip (shifted slightly)
    [ 0.10, 0.55],  # Right Hip
    [-0.10, 0.45],  # Left Knee (bent)
    [ 0.10, 0.45],  # Right Knee
    [-0.10, 0.35],  # Left Foot (shifted back)
    [ 0.10, 0.35]   # Right Foot
])

# Define the number of frames and interval for the animation.
num_frames = 120
interval_ms = 30  # time delay between frames in milliseconds

def ease_in_out(t):
    """
    Smooth interpolation using a cosine easing.
    t: a value from 0 (start) to 1 (end)
    returns an eased value from 0 to 1.
    """
    return 0.5 * (1 - math.cos(math.pi * t))

# Create the figure and axes.
fig, ax = plt.subplots(figsize=(5, 8))
ax.set_facecolor('black')
plt.style.use('dark_background')
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')  # hide axes

# Create a scatter plot for the 15 white point-lights.
scatter = ax.scatter(standing[:, 0], standing[:, 1], s=100, c='white', zorder=10)

def update(frame):
    # Normalize the frame index to [0,1] for interpolation.
    t = frame / (num_frames - 1)
    smooth_t = ease_in_out(t)
    # Interpolate each of the 15 joints.
    current_pose = standing + smooth_t * (sitting - standing)
    scatter.set_offsets(current_pose)
    return scatter,

# Create the animation using FuncAnimation.
ani = FuncAnimation(fig, update, frames=num_frames, interval=interval_ms, blit=True)

# Display the animation.
plt.show()