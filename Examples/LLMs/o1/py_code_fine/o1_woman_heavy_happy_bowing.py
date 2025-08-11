#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------------------------------------------------
# A simple 2D point-light biological motion animation
# Depicting a "happy, heavy woman" bowing with 15 point-lights
# -------------------------------------------------------------------

# Predefine body topology (15 points).
# We'll store base coordinates (standing upright) in a dictionary:
#   Key = point name, Value = (x, y) in some 2D coordinate system
#
# Points (in order):
#   1. Head
#   2. Neck
#   3. Right Shoulder
#   4. Left Shoulder
#   5. Right Elbow
#   6. Left Elbow
#   7. Right Wrist
#   8. Left Wrist
#   9. Mid Torso (roughly chest/upper back)
#   10. Right Hip
#   11. Left Hip
#   12. Right Knee
#   13. Left Knee
#   14. Right Ankle
#   15. Left Ankle
#
# To create a "heavy" figure, the shoulders/hips are set a bit wider.

BODY_BASE = {
    "Head":          (0.0,  0.0),
    "Neck":          (0.0,  1.0),
    "RShoulder":     (0.6,  1.0),
    "LShoulder":     (-0.6, 1.0),
    "RElbow":        (1.0,  2.0),
    "LElbow":        (-1.0, 2.0),
    "RWrist":        (1.0,  3.0),
    "LWrist":        (-1.0, 3.0),
    "MidTorso":      (0.0,  2.0),
    "RHip":          (0.6,  3.0),
    "LHip":          (-0.6, 3.0),
    "RKnee":         (0.6,  4.0),
    "LKnee":         (-0.6, 4.0),
    "RAnkle":        (0.6,  5.0),
    "LAnkle":        (-0.6, 5.0),
}

# For bowing, we'll define the pivot as the midpoint of the hips (this is
# an approximation for "heavy woman" center of rotation). We will rotate
# the upper body (above hips) around this pivot. The legs will bend a bit
# for realism.

PIVOT = np.array([0.0, 3.0])  # midpoint of hips around y=3

# Angles (in degrees) for frames 0..9 (then repeat)
#   This creates a bowing sequence: start upright, bend forward to ~60 deg,
#   then return to upright, etc.
ANGLES = [0, 10, 20, 30, 40, 60, 40, 20, 10, 0]

# We'll define a function to rotate a point (x, y) around the pivot
# by a given angle in degrees.
def rotate_point(x, y, pivot_x, pivot_y, angle_deg):
    # Shift to pivot
    dx = x - pivot_x
    dy = y - pivot_y
    # Convert angle to radians
    theta = np.radians(angle_deg)
    # Apply rotation (2D rotation matrix)
    rx = dx * np.cos(theta) - dy * np.sin(theta)
    ry = dx * np.sin(theta) + dy * np.cos(theta)
    # Shift back
    return rx + pivot_x, ry + pivot_y

def get_frame_coordinates(frame_index):
    """
    Return a list of (x, y) coordinate pairs for the 15 points
    at the given frame_index. The frame_index will be mod 10
    to select the angle in ANGLES, and we apply some knee bending
    for a more natural bow.
    """
    # Use cyclical index
    idx = frame_index % len(ANGLES)
    angle = ANGLES[idx]

    coords = []
    # We'll define a small knee offset to simulate bending
    #   As the angle gets larger, bend more. Let knee
    #   shift upward slightly (reduce y).
    #   For angle up to 60, let's bend up to ~0.3 in y
    knee_bend = (angle / 60.0) * 0.3

    for i, point_name in enumerate(BODY_BASE.keys()):
        base_x, base_y = BODY_BASE[point_name]

        # Decide if we rotate the point or not. We'll rotate everything from
        # the hips upward: Head, Neck, Shoulders, Elbows, Wrists, MidTorso.
        # The hips themselves stay fixed, but the "torso pivot" is an average
        # of the hips. We'll leave the legs (knees, ankles) unrotated, but
        # we slightly shift them up for bending.
        if point_name in ["Head", "Neck",
                          "RShoulder", "LShoulder",
                          "RElbow", "LElbow",
                          "RWrist", "LWrist",
                          "MidTorso"]:
            # Rotate about the pivot
            rx, ry = rotate_point(base_x, base_y, PIVOT[0], PIVOT[1], angle)
        else:
            # Hips, knees, ankles - no rotation, but knees bend up
            # for frames with a nonzero angle.
            rx, ry = (base_x, base_y)

            # If it's a knee or ankle, shift it slightly upward
            # (i.e., reduce the y coordinate) relative to pivot,
            # to simulate knee bending. We'll do it for angle>0.
            if point_name in ["RKnee", "LKnee", "RAnkle", "LAnkle"]:
                # Shift upward by knee_bend
                # We'll do a fraction if it's an ankle, e.g. half
                if "Ankle" in point_name:
                    ry -= knee_bend * 0.5
                else:
                    ry -= knee_bend

        coords.append((rx, ry))

    return coords

# ---------------------------------------------------------
# Set up the matplotlib figure/animation
# ---------------------------------------------------------
fig, ax = plt.subplots()
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_xlim(-2.0, 2.0)
ax.set_ylim(6.0, -1.0)  # inverted so that "down" is positive Y visually
ax.set_aspect("equal")
ax.axis("off")

# We'll use a scatter plot to represent the 15 points of light
scatter = ax.scatter([], [], c="white", s=30)

def init():
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    # Get the new coordinates
    coords = get_frame_coordinates(frame)
    # Update scatter
    scatter.set_offsets(coords)
    return (scatter,)

ani = FuncAnimation(
    fig,
    update,
    frames=200,      # number of frames to cycle through
    init_func=init,
    interval=100,    # delay between frames in milliseconds
    blit=True,
    repeat=True
)

plt.show()