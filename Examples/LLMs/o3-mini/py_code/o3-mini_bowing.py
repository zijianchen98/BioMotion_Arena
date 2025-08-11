
"""
This program displays an animation of a point‐light stimulus that depicts a man bowing.
There are exactly 15 white points on a solid black background. The upper body (points 1–9)
rotates about the lower spine (point 10) to simulate a natural, biomechanically plausible bow.
Run the program to see the smooth animation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial joint positions for a standing man (in 2D, arbitrary units)
# Points 1 to 15 (exactly 15 points)
#
# 1. Head:         (0, 10)
# 2. Neck:         (0, 9)
# 3. Left shoulder:(-1, 9)
# 4. Right shoulder:(1, 9)
# 5. Left elbow:   (-1.5, 7.5)
# 6. Right elbow:  (1.5, 7.5)
# 7. Left wrist:   (-1.75, 6)
# 8. Right wrist:  (1.75, 6)
# 9. Middle spine: (0, 8)
# 10. Lower spine: (0, 7) --> Pivot for upper body rotation
# 11. Left hip:    (-0.5, 7)
# 12. Right hip:   (0.5, 7)
# 13. Left knee:   (-0.5, 4)
# 14. Right knee:  (0.5, 4)
# 15. Ankle (combined): (0, 0)

base_points = np.array([
    [0.0, 10.0],    # 1. Head
    [0.0, 9.0],     # 2. Neck
    [-1.0, 9.0],    # 3. Left shoulder
    [1.0, 9.0],     # 4. Right shoulder
    [-1.5, 7.5],    # 5. Left elbow
    [1.5, 7.5],     # 6. Right elbow
    [-1.75, 6.0],   # 7. Left wrist
    [1.75, 6.0],    # 8. Right wrist
    [0.0, 8.0],     # 9. Middle spine
    [0.0, 7.0],     # 10. Lower spine (pivot point)
    [-0.5, 7.0],    # 11. Left hip
    [0.5, 7.0],     # 12. Right hip
    [-0.5, 4.0],    # 13. Left knee
    [0.5, 4.0],     # 14. Right knee
    [0.0, 0.0]      # 15. Ankle (averaged)
])

# Indices for the upper body joints that will rotate while bowing.
# We will rotate points 0 to 8 (i.e. joints 1–9) about the pivot (point 10, index 9).
upper_body_indices = np.arange(0, 9)
# Lower body (including pivot and below) remains fixed
# pivot index: 9

# Parameters for the bowing motion
max_bow_angle_deg = 30  # maximum bow angle in degrees (forward bow, clockwise rotation)
max_bow_angle = np.radians(max_bow_angle_deg)
period = 2000  # period of one full cycle of bowing in milliseconds

# Create a figure with black background.
fig, ax = plt.subplots(figsize=(5, 8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Set up the scatter plot for the 15 white point-lights.
scatter = ax.scatter(base_points[:, 0], base_points[:, 1], s=100, c='white')

# Set the plot limits
ax.set_xlim(-4, 4)
ax.set_ylim(-1, 11)
ax.set_aspect('equal')
ax.axis('off')

def rotate_points(points, angle, pivot):
    """
    Rotate an array of points (N x 2) around a pivot by a given angle (in radians).
    Clockwise rotation is achieved by a negative angle.
    """
    # Translate points to pivot
    translated = points - pivot
    cosA = np.cos(angle)
    sinA = np.sin(angle)
    rotation_matrix = np.array([[cosA, -sinA],
                                [sinA,  cosA]])
    rotated = translated.dot(rotation_matrix.T)
    return rotated + pivot

def update(frame):
    # time parameter using frame number
    # We use a sine function so the bowing goes forward and returns smoothly.
    t = frame / 50.0  # time scale factor, adjust to change speed
    # Oscillate between 0 and max_bow_angle. The minus sign makes the rotation clockwise.
    angle = -max_bow_angle * np.sin(2 * np.pi * t / (period/50.0))
    
    # Copy base points for modification
    new_points = np.copy(base_points)
    
    # Get pivot position (lower spine, point 10)
    pivot = base_points[9]
    
    # Rotate the upper body joints about the pivot.
    new_points[upper_body_indices] = rotate_points(base_points[upper_body_indices], angle, pivot)
    
    # Update scatter plot data.
    scatter.set_offsets(new_points)
    return scatter,

# Create animation: interval in ms; frames; use blit for performance.
ani = FuncAnimation(fig, update, frames=np.linspace(0, period, num=200), interval=20, blit=True)

# Show the animation window.
plt.show()