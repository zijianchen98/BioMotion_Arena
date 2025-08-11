#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 15-point skeleton indexing:
# 0: Head
# 1: Neck
# 2: Right Shoulder
# 3: Left Shoulder
# 4: Right Elbow
# 5: Left Elbow
# 6: Right Hand
# 7: Left Hand
# 8: Torso (mid-back)
# 9: Right Hip
# 10: Left Hip
# 11: Right Knee
# 12: Left Knee
# 13: Right Foot
# 14: Left Foot

# Base (neutral standing) positions (x,y):
base_positions = np.array([
    [ 0.00,  0.50],  # Head
    [ 0.00,  0.40],  # Neck
    [ 0.15,  0.35],  # Right Shoulder
    [-0.15,  0.35],  # Left Shoulder
    [ 0.25,  0.25],  # Right Elbow
    [-0.25,  0.25],  # Left Elbow
    [ 0.30,  0.15],  # Right Hand
    [-0.30,  0.15],  # Left Hand
    [ 0.00,  0.20],  # Torso
    [ 0.10,  0.00],  # Right Hip
    [-0.10,  0.00],  # Left Hip
    [ 0.10, -0.35],  # Right Knee
    [-0.10, -0.35],  # Left Knee
    [ 0.10, -0.50],  # Right Foot
    [-0.10, -0.50],  # Left Foot
])

# Indices of points "above" the hips (to rotate for the bow).
above_hips = [0,1,2,3,4,5,6,7,8]

def rotate(x, y, cx, cy, angle_deg):
    """Rotate point (x,y) around center (cx,cy) by angle_deg (degrees)."""
    rad = np.deg2rad(angle_deg)
    xr = (x - cx)*np.cos(rad) - (y - cy)*np.sin(rad) + cx
    yr = (x - cx)*np.sin(rad) + (y - cy)*np.cos(rad) + cy
    return xr, yr

def get_skeleton_positions(t):
    """
    Returns the (15,2) array of skeleton positions for parameter t in [0,1],
    where 0 = upright, 1 = fully bowed.
    """
    # Copy base positions
    pts = base_positions.copy()

    # Mid-hip (rotation center)
    # We'll treat midpoint of right & left hip as rotation center
    hx = (pts[9,0] + pts[10,0]) / 2.0
    hy = (pts[9,1] + pts[10,1]) / 2.0
    
    # Bow angle from 0 (upright) to -40 degrees (fully bowed)
    bow_angle = -40.0 * t

    # Small knee bend: rotate legs around the hips by 10 degrees * t
    knee_angle = 10.0 * t

    # Rotate points above hips around the midpoint
    for i in above_hips:
        x_old, y_old = pts[i]
        x_new, y_new = rotate(x_old, y_old, hx, hy, bow_angle)
        pts[i,0], pts[i,1] = x_new, y_new

    # Rotate lower legs around their respective knees to simulate slight bend
    # Right lower leg: points 13 around point 11
    rx_kx, rx_ky = pts[11]  # Right knee
    rx_fx, rx_fy = pts[13]  # Right foot
    rx_fx2, rx_fy2 = rotate(rx_fx, rx_fy, rx_kx, rx_ky, -knee_angle)
    pts[13,0], pts[13,1] = rx_fx2, rx_fy2

    # Left lower leg: points 14 around point 12
    lx_kx, lx_ky = pts[12]  # Left knee
    lx_fx, lx_fy = pts[14]  # Left foot
    lx_fx2, lx_fy2 = rotate(lx_fx, lx_fy, lx_kx, lx_ky, -knee_angle)
    pts[14,0], pts[14,1] = lx_fx2, lx_fy2

    return pts

# Create the figure and axes (black background)
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Scatter plot for the 15 white points
scatter = ax.scatter(base_positions[:,0], base_positions[:,1], c='white', s=50)

# Adjust plot appearance
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.6, 0.6)
ax.set_aspect('equal')
plt.axis('off')

# Generate frames from 0->1->0 for a single bow cycle
frames = []
num_frames_half = 25
for i in range(num_frames_half):
    f = i / (num_frames_half - 1)
    frames.append(f)
for i in range(num_frames_half):
    f = 1.0 - (i / (num_frames_half - 1))
    frames.append(f)

def update(frame):
    pts = get_skeleton_positions(frame)
    scatter.set_offsets(pts)
    return (scatter,)

ani = FuncAnimation(fig, update, frames=frames, interval=60, blit=True, repeat=True)

plt.show()