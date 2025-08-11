
"""
This program creates a point‐light stimulus animation of a heavy, sad man turning around.
It displays exactly 15 white point‐lights against a solid black background.
The 15 points represent key body parts of the human form (head, shoulders, elbows, hands,
torso, hips, knees and feet). The movement is biomechanically plausible: a smooth,
ease-in–ease-out 180° turn performed “in place” about the hip center (the pivot).
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Define the 15 marker positions in a neutral pose.
# The coordinates are arranged in (x, y) with y increasing upward.
# The hip center (0,0.4) will be used as the pivot for rotation.
markers = np.array([
    [ 0.0,  0.9],  # Head
    [ 0.0,  0.7],  # Shoulder center
    [-0.2,  0.7],  # Left shoulder
    [ 0.2,  0.7],  # Right shoulder
    [-0.4,  0.5],  # Left elbow
    [ 0.4,  0.5],  # Right elbow
    [-0.5,  0.3],  # Left hand
    [ 0.5,  0.3],  # Right hand
    [ 0.0,  0.4],  # Hip center (pivot)
    [-0.2,  0.4],  # Left hip
    [ 0.2,  0.4],  # Right hip
    [-0.2,  0.2],  # Left knee
    [ 0.2,  0.2],  # Right knee
    [-0.2,  0.0],  # Left foot
    [ 0.2,  0.0]   # Right foot
])

pivot = np.array([0.0, 0.4])  # hip center (pivot of rotation)

# Animation parameters
frames = 200            # total number of frames in the animation
total_turn_rad = math.pi  # total rotation angle (180° in radians)

# Figure and axes setup
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor("black")
ax.set_xlim(-1, 1)
ax.set_ylim(-0.2, 1.2)
ax.set_aspect("equal")
ax.axis("off")

# Create scatter plot for the point-lights (white dots)
scat = ax.scatter(markers[:, 0], markers[:, 1], s=100, color="white")

def ease_in_out(t):
    """
    Ease-in and ease-out function for smooth motion.
    t: normalized time [0, 1]
    Returns a value smoothly varying from 0 to 1.
    """
    return 0.5 - 0.5 * math.cos(math.pi * t)

def rotate_points(points, angle, center):
    """
    Rotates an array of points (shape: (N,2)) by given angle (in radians)
    around a given center.
    """
    # Translate points so that 'center' becomes the origin.
    translated = points - center
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    # Rotation matrix application
    rotation_matrix = np.array([[cos_a, -sin_a],
                                [sin_a, cos_a]])
    rotated = np.dot(translated, rotation_matrix.T)
    # Translate back
    return rotated + center

def update(frame):
    # update the animation for the given frame
    t = frame / (frames - 1)
    # Use the easing function to determine the current angle
    current_angle = total_turn_rad * ease_in_out(t)
    
    # To simulate heavy turning (i.e. inertia and controlled sway), 
    # we add a very small oscillatory sway perpendicular to the turning direction.
    sway_amplitude = 0.02  # small lateral sway
    sway = sway_amplitude * math.sin(2 * math.pi * t * 3)  # 3 oscillations over the turn
    
    # First, rotate the markers about the pivot.
    new_markers = rotate_points(markers, current_angle, pivot)
    
    # Then, add the lateral sway to simulate the biomechanical effect.
    # The sway is applied along the horizontal axis.
    new_markers[:, 0] += sway
    
    # Update scatter plot data.
    scat.set_offsets(new_markers)
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=30, blit=True)

# Display the animation window.
plt.show()