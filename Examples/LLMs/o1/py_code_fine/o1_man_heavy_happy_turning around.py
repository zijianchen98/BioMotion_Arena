#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def rotation_matrix_y(theta):
    """
    Returns a 3D rotation matrix for rotation about the y-axis by angle theta.
    """
    return np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [            0, 1,            0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def create_skeleton_points():
    """
    Returns a (15, 3) numpy array of 3D coordinates for a simple
    'happy man carrying heavy weight' skeleton in a neutral stance.
    """
    return np.array([
        # (x, y, z)
        [ 0.0, 1.80, 0.0],   # Head
        [ 0.0, 1.60, 0.0],   # Neck
        [ 0.2, 1.60, 0.0],   # Right shoulder
        [ 0.4, 1.40,-0.2],   # Right elbow (slightly forward)
        [ 0.5, 1.20,-0.3],   # Right wrist (carrying weight in front)
        [-0.2, 1.60, 0.0],   # Left shoulder
        [-0.4, 1.40,-0.2],   # Left elbow (slightly forward)
        [-0.5, 1.20,-0.3],   # Left wrist (carrying weight in front)
        [ 0.0, 1.00, 0.0],   # Pelvis (approx center)
        [ 0.2, 1.00, 0.0],   # Right hip
        [ 0.2, 0.60, 0.0],   # Right knee
        [ 0.2, 0.00, 0.0],   # Right ankle
        [-0.2, 1.00, 0.0],   # Left hip
        [-0.2, 0.60, 0.0],   # Left knee
        [-0.2, 0.00, 0.0],   # Left ankle
    ])

# Create figure with black background
fig, ax = plt.subplots(figsize=(6,6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Prepare skeleton points
skeleton_base = create_skeleton_points()

# Scatter plot for the points
scatter = ax.scatter([], [], color='white', s=30)

# Configure axes
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.2, 2.2)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')

def init():
    scatter.set_offsets([])
    return scatter,

def animate(frame):
    # Angle goes from 0 to 2*pi over 120 frames (smooth turn-around)
    theta = 2.0 * np.pi * (frame / 120.0)
    R = rotation_matrix_y(theta)
    rotated_points = skeleton_base @ R.T  # Apply rotation
    x = rotated_points[:, 0]
    y = rotated_points[:, 1]
    scatter.set_offsets(np.column_stack((x, y)))
    return scatter,

anim = FuncAnimation(
    fig, animate, init_func=init, frames=120, interval=50, blit=True
)

plt.show()