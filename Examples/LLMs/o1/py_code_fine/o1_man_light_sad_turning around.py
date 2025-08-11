#!/usr/bin/env python3
"""
Biological Motion Point-Light Display
Subject: A "sad man" turning around
Visual Style: Exactly 15 white point-lights on black background
Motion Quality: Smooth, natural turning action in a slightly slouched (sad) posture
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------------------------------------------------------
# 1) Define the base (sad, slightly slouched) skeleton with 15 key points in 3D
#    The coordinates below are roughly human-like proportions with a slight hunch
#    (head/shoulders leaning forward). We'll later rotate them in the animation.
# -----------------------------------------------------------------------------
BASE_SKELETON_3D = np.array([
    [ 0.00, 1.80, -0.05],  # Head
    [ 0.00, 1.60, -0.04],  # Neck
    [ 0.20, 1.60, -0.03],  # Right shoulder
    [ 0.30, 1.30, -0.02],  # Right elbow
    [ 0.35, 1.00, -0.02],  # Right wrist
    [-0.20, 1.60, -0.03],  # Left shoulder
    [-0.30, 1.30, -0.02],  # Left elbow
    [-0.35, 1.00, -0.02],  # Left wrist
    [ 0.00, 1.00,  0.00],  # Pelvis / lower torso
    [ 0.10, 1.00,  0.00],  # Right hip
    [ 0.10, 0.60,  0.00],  # Right knee
    [ 0.10, 0.00,  0.00],  # Right ankle
    [-0.10, 1.00,  0.00],  # Left hip
    [-0.10, 0.60,  0.00],  # Left knee
    [-0.10, 0.00,  0.00],  # Left ankle
])

# -----------------------------------------------------------------------------
# 2) Define a function to produce rotation about the Y axis (vertical) so that
#    the skeleton can appear to "turn around" smoothly.
# -----------------------------------------------------------------------------
def rotate_y(points_3d, angle_radians):
    """
    Rotate array of 3D points about the Y-axis by 'angle_radians'.
    points_3d: shape (N, 3)
    Returns a new array of the same shape.
    """
    c = np.cos(angle_radians)
    s = np.sin(angle_radians)
    # Rotation matrix around Y: (assuming y is up)
    R = np.array([
        [ c, 0,  s],
        [ 0, 1,  0],
        [-s, 0,  c]
    ])
    return points_3d @ R.T

# -----------------------------------------------------------------------------
# 3) Project the 3D (x,y,z) points into 2D screen space for display.
#    We'll use a simple orthographic projection (drop the z-axis).
# -----------------------------------------------------------------------------
def orthographic_projection(points_3d):
    """
    Orthographically project 3D points to 2D (x,y),
    ignoring z for display.
    """
    return points_3d[:, [0, 1]]

# -----------------------------------------------------------------------------
# 4) Generate a new skeleton for each animation frame. We'll make the skeleton
#    turn around by some angle. We can optionally add a mild "up-down" shift 
#    to mimic a slight movement, but here we keep it minimal so the main motion 
#    is turning.
# -----------------------------------------------------------------------------
def get_skeleton_for_frame(frame_number, total_frames):
    # Compute rotation angle to turn around
    angle = 2.0 * np.pi * (frame_number / total_frames)  # 0 to 2 pi
    
    # Start from the base skeleton
    skel_3d = BASE_SKELETON_3D.copy()
    
    # Rotate the entire skeleton around Y
    skel_3d = rotate_y(skel_3d, angle)
    
    # Optional small bounce or slump variation to give it a bit of life
    # For a subtle "sad" bobbing, we shift y slightly with a sine wave
    skel_3d[:,1] += 0.02 * np.sin(4.0 * angle)  # light bob
    
    return skel_3d

# -----------------------------------------------------------------------------
# 5) Animation update function: For each frame, compute new skeleton positions,
#    project them to 2D, and update the scatter plot.
# -----------------------------------------------------------------------------
def update(frame):
    skel_3d = get_skeleton_for_frame(frame, total_frames)
    skel_2d = orthographic_projection(skel_3d)
    scatter.set_offsets(skel_2d)
    return (scatter,)

# -----------------------------------------------------------------------------
# Main script to set up the figure and run the animation
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Total number of animation frames
    total_frames = 200

    # Create a figure with black background
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Initialize scatter (15 points) in white
    # We'll update these positions each frame.
    skel_2d_init = orthographic_projection(BASE_SKELETON_3D)
    scatter = ax.scatter(
        skel_2d_init[:,0],
        skel_2d_init[:,1],
        c='white',
        s=30
    )

    # Adjust plot limits so the figure stays stable as skeleton turns
    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(-0.2, 2.0)
    
    # Turn off axes (we only want black background + white dots)
    ax.axis('off')

    # Create the animation
    ani = FuncAnimation(
        fig, update,
        frames=total_frames,
        interval=50,  # milliseconds between frames
        blit=True,
        repeat=True
    )

    plt.show()