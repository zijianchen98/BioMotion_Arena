#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
# Helper Functions
# -----------------------------

def rotate_point(point, pivot, angle):
    """
    Rotate 'point' around 'pivot' by 'angle' (in radians).
    Returns the rotated point as an (x, y) tuple.
    """
    # Translate point so pivot is at origin
    tx = point[0] - pivot[0]
    ty = point[1] - pivot[1]

    # Apply rotation
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    rx = tx * cos_a - ty * sin_a
    ry = tx * sin_a + ty * cos_a

    # Translate back
    return (rx + pivot[0], ry + pivot[1])

def get_skeleton_points():
    """
    Return a list of the base skeleton's 15 keypoint coordinates in 2D.
    This is the reference posture (a slightly slumped "sad" stance).
    Indices:
      0: Head
      1: Neck
      2: Torso (center)
      3: Right shoulder
      4: Right elbow
      5: Right wrist
      6: Left shoulder
      7: Left elbow
      8: Left wrist
      9: Right hip
     10: Right knee
     11: Right ankle
     12: Left hip
     13: Left knee
     14: Left ankle
    """
    return [
        (0.0, 1.80),  # Head
        (0.0, 1.60),  # Neck
        (0.0, 1.20),  # Torso
        (0.20, 1.50), # Right shoulder
        (0.35, 1.25), # Right elbow
        (0.40, 1.00), # Right wrist
        (-0.20, 1.50),# Left shoulder
        (-0.35, 1.25),# Left elbow
        (-0.40, 1.00),# Left wrist
        (0.10, 1.00), # Right hip
        (0.10, 0.60), # Right knee
        (0.10, 0.20), # Right ankle
        (-0.10, 1.00),# Left hip
        (-0.10, 0.60),# Left knee
        (-0.10, 0.20) # Left ankle
    ]

def transform_skeleton(t, base_points):
    """
    Given a frame index t and the base skeleton points, produce the
    updated (x, y) positions for the skeleton to simulate:
      - a sad posture (slightly slumped forward)
      - a right-hand waving motion
      - smooth, coherent motions
    """
    # Copy the base points so we can transform them
    points = base_points.copy()

    # Slump angle: rotate upper body (head, neck, shoulders) about the torso
    slump_angle = 0.15  # radians, ~8.6 degrees
    torso_center = points[2]

    # Rotate head and neck about torso to create a forward "sad" slump
    points[0] = rotate_point(points[0], torso_center, slump_angle)
    points[1] = rotate_point(points[1], torso_center, slump_angle)
    # Shoulders
    points[3] = rotate_point(points[3], torso_center, slump_angle)
    points[6] = rotate_point(points[6], torso_center, slump_angle)

    # Optional gentle bounce in vertical direction to evoke "life"
    bounce_mag = 0.02
    bounce = bounce_mag * np.sin(2.0 * np.pi * (t / 50.0))
    points = [(x, y + bounce) for (x, y) in points]

    # Define wave cycles
    # We'll have the wave happen primarily at the right elbow and wrist about the shoulder
    wave_elbow_angle = 0.4 * np.sin(2.0 * np.pi * (t / 30.0))        # amplitude of rotation
    wave_wrist_angle = 0.4 * np.sin(2.0 * np.pi * (t / 30.0) + 0.5)  # offset phase for wrist

    # Indices for right shoulder, elbow, wrist
    shoulder_idx = 3
    elbow_idx = 4
    wrist_idx = 5

    # Right shoulder pivot is the shoulder itself
    shoulder_pivot = points[shoulder_idx]

    # First rotate the elbow around the shoulder
    elbow_pos = points[elbow_idx]
    elbow_pos = rotate_point(elbow_pos, shoulder_pivot, wave_elbow_angle)
    points[elbow_idx] = elbow_pos

    # Now rotate the wrist around the elbow
    wrist_pos = points[wrist_idx]
    wrist_pos = rotate_point(wrist_pos, elbow_pos, wave_wrist_angle)
    points[wrist_idx] = wrist_pos

    return points

# -----------------------------
# Main Animation
# -----------------------------

def main():
    # Setup the figure
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("black")      # black background for the figure
    ax.set_facecolor("black")             # black background inside the plot area
    ax.set_xlim(-0.8, 0.8)
    ax.set_ylim(0.0, 2.0)
    ax.axis('off')  # hide axes

    base_skeleton = get_skeleton_points()
    scat = ax.scatter([], [], c="white", s=25)

    def init():
        scat.set_offsets([])
        return (scat,)

    def update(frame):
        # Compute new skeleton positions
        pts = transform_skeleton(frame, base_skeleton)
        scat.set_offsets(pts)
        return (scat,)

    ani = FuncAnimation(
        fig,
        update,
        frames=120,       # number of frames in one loop
        init_func=init,
        interval=50,      # time in ms between frames
        blit=True,
        repeat=True
    )

    plt.show()

if __name__ == "__main__":
    main()