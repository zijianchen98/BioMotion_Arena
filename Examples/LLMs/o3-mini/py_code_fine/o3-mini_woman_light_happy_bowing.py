
"""
This program creates a point‐light stimulus animation representing biological motion –
a happy, light‐weight woman bowing. The animation consists of exactly 15 white points
displayed on a solid black background. The “skeleton” is defined by 15 key joints,
and a bowing motion is simulated by a biomechanically plausible rotation of the upper
body (head, shoulders, arms, and thorax) about the pelvis. The lower body (pelvis and legs)
remains fixed.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Define the 15 key joint positions for an upright figure.
# Points are given as (x, y) coordinates.
# The coordinate system is arbitrary: units ~ meters.
# The joints:
#  0: Head
#  1: Left Shoulder
#  2: Right Shoulder
#  3: Left Elbow
#  4: Right Elbow
#  5: Left Wrist
#  6: Right Wrist
#  7: Thorax (chest center)
#  8: Pelvis (pivot for bowing)
#  9: Left Hip
# 10: Right Hip
# 11: Left Knee
# 12: Right Knee
# 13: Left Ankle
# 14: Right Ankle

# Positions when standing upright.
points = np.array([
    [0.0, 0.60],    # Head
    [-0.20, 0.55],  # Left Shoulder
    [ 0.20, 0.55],  # Right Shoulder
    [-0.35, 0.45],  # Left Elbow
    [ 0.35, 0.45],  # Right Elbow
    [-0.45, 0.40],  # Left Wrist
    [ 0.45, 0.40],  # Right Wrist
    [0.0, 0.50],    # Thorax
    [0.0, 0.30],    # Pelvis (pivot for bowing)
    [-0.15, 0.30],  # Left Hip
    [ 0.15, 0.30],  # Right Hip
    [-0.15, 0.15],  # Left Knee
    [ 0.15, 0.15],  # Right Knee
    [-0.15, 0.00],  # Left Ankle
    [ 0.15, 0.00]   # Right Ankle
])

# Define indices for joints that should be rotated in the bowing movement.
# We rotate the upper body joints, i.e., Head, both Shoulders, both Elbows, both Wrists, and Thorax.
upper_body_indices = [0, 1, 2, 3, 4, 5, 6, 7]

# Define the pelvis index (the pivot) which is not moved.
pelvis_index = 8

# Bowing parameters
max_bow_angle_deg = 30  # maximum bow in degrees
max_bow_angle = math.radians(max_bow_angle_deg)  # convert to radians

# Animation parameters
num_frames = 100
interval = 30  # milliseconds between frames

# Create a figure and axis with a black background.
fig, ax = plt.subplots(figsize=(5,8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Set the plot limits to frame the figure nicely.
ax.set_xlim(-1, 1)
ax.set_ylim(-0.2, 1)
ax.set_aspect('equal')
ax.axis('off')  # Hide the axes

# Create a scatter plot for the 15 points.
scat = ax.scatter(points[:,0], points[:,1], s=80, c='white')

def rotate_point(point, pivot, angle):
    """Rotate a 2D point around a pivot by a given angle (in radians)."""
    # Translate point to origin
    translated = point - pivot
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    # Apply rotation
    x_new = translated[0]*cos_a - translated[1]*sin_a
    y_new = translated[0]*sin_a + translated[1]*cos_a
    # Translate back
    return np.array([x_new, y_new]) + pivot

def animate(frame):
    # Compute a smooth bowing angle.
    # Using a sine profile to go from 0 at the beginning,
    # to max_bow_angle at the midway, then back to 0.
    t = frame / (num_frames - 1)   # normalized time from 0 to 1
    # Sine wave gives a smooth "bow and return" movement.
    angle = max_bow_angle * math.sin(math.pi * t)
    
    # Copy the base points.
    updated_points = np.copy(points)
    
    # Use the pelvis as the pivot point.
    pivot = points[pelvis_index]
    
    # Apply rotation to each upper-body joint.
    for idx in upper_body_indices:
        updated_points[idx] = rotate_point(points[idx], pivot, angle)
    
    # Update scatter data.
    scat.set_offsets(updated_points)
    
    return scat,

# Create and run the animation.
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=interval, blit=True, repeat=True)

# To display the animation, uncomment the following line:
plt.show()

# Alternatively, to save the animation as an MP4 file, uncomment this block:
# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=30, metadata=dict(artist='Your Name'), bitrate=1800)
# ani.save("bowing_point_light.mp4", writer=writer)
