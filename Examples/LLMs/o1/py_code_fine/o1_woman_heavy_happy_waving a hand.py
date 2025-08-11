#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# --------------------------------------------
# 1. Define the base skeleton (15 points) in a neutral pose (x, y).
#    This simple layout approximates a "heavy" figure with slightly wider hips.
# --------------------------------------------
base_skeleton = np.array([
    [ 0.0,  1.80],  # 0: Head
    [ 0.0,  1.60],  # 1: Neck
    [ 0.20, 1.55],  # 2: Right Shoulder
    [-0.20, 1.55],  # 3: Left Shoulder
    [ 0.40, 1.40],  # 4: Right Elbow
    [-0.40, 1.40],  # 5: Left Elbow
    [ 0.50, 1.25],  # 6: Right Hand
    [-0.50, 1.25],  # 7: Left Hand
    [ 0.25, 1.00],  # 8: Right Hip
    [-0.25, 1.00],  # 9: Left Hip
    [ 0.25, 0.60],  # 10: Right Knee
    [-0.25, 0.60],  # 11: Left Knee
    [ 0.25, 0.20],  # 12: Right Foot
    [-0.25, 0.20],  # 13: Left Foot
    [ 0.00, 1.00]   # 14: Center of Pelvis
])

# --------------------------------------------
# 2. Helper function to perform 2D rotation about a pivot.
# --------------------------------------------
def rotate_point(point, pivot, angle_deg):
    """Rotate 'point' around 'pivot' by 'angle_deg' degrees (counterclockwise)."""
    angle_rad = math.radians(angle_deg)
    # Translate point so pivot is origin
    translated = point - pivot
    # Rotation matrix
    c, s = math.cos(angle_rad), math.sin(angle_rad)
    rot = np.array([[c, -s], [s, c]])
    # Rotate and translate back
    rotated = rot.dot(translated)
    return pivot + rotated

# --------------------------------------------
# 3. Compute skeleton coordinates at frame n.
#    - Adds a gentle up-and-down "bounce" to simulate a heavier figure's subtle movement.
#    - Right arm waves (shoulder + elbow).
# --------------------------------------------
def skeleton_at_frame(n):
    # Copy the base skeleton so as not to modify it permanently
    coords = base_skeleton.copy()

    # Total frames in one wave cycle
    T = 50
    # Convert n into a fraction of the wave cycle
    cycle_pos = n % T
    phase = 360.0 * cycle_pos / T  # degrees

    # Subtle bounce (all points): amplitude 0.02, same period as wave
    bounce_amplitude = 0.02
    vertical_shift = bounce_amplitude * math.sin(math.radians(phase)) 
    coords[:,1] += vertical_shift

    # --------------------------------------------
    # Wave the right arm:
    #   - Shoulder rotation
    #   - Elbow rotation (forearm)
    # --------------------------------------------
    # Indices in base_skeleton:
    #   Right Shoulder = 2, Right Elbow = 4, Right Hand = 6
    r_shoulder_idx, r_elbow_idx, r_hand_idx = 2, 4, 6

    # Shoulder wave angle
    shoulder_angle = 20.0 * math.sin(math.radians(phase))
    # Elbow wave angle
    elbow_angle = 30.0 * math.sin(math.radians(phase))

    # Rotate elbow and hand around the shoulder
    shoulder_pos = coords[r_shoulder_idx]
    coords[r_elbow_idx] = rotate_point(coords[r_elbow_idx], shoulder_pos, shoulder_angle)
    coords[r_hand_idx]  = rotate_point(coords[r_hand_idx],  shoulder_pos, shoulder_angle)

    # Then rotate the hand around the elbow
    elbow_pos = coords[r_elbow_idx]
    coords[r_hand_idx] = rotate_point(coords[r_hand_idx], elbow_pos, elbow_angle)

    return coords

# --------------------------------------------
# 4. Set up the plot
# --------------------------------------------
fig, ax = plt.subplots(figsize=(5, 5))
fig.patch.set_facecolor('black')       # Black background for the figure
ax.set_facecolor('black')             # Black background for the axes
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.axis('off')  # Hide axes

# Create a scatter plot of 15 points (white) with some size for visibility
scatter = ax.scatter([], [], c='white', s=50)

# --------------------------------------------
# 5. Initialize animation
# --------------------------------------------
def init():
    scatter.set_offsets([])
    return (scatter,)

# --------------------------------------------
# 6. Update function for animation
# --------------------------------------------
def update(frame):
    coords = skeleton_at_frame(frame)
    scatter.set_offsets(coords)
    return (scatter,)

# --------------------------------------------
# 7. Create and start the animation
# --------------------------------------------
anim = FuncAnimation(fig, update, init_func=init, frames=200, interval=50, blit=True)
plt.show()