
"""
This program displays an animation of a “happyman with heavy weight” performing a forward roll.
The animation uses exactly 15 white “point‐lights” on a solid black background.
The 15 points are interpreted as markers on key body locations of a curled (tucked) human,
so that when the whole configuration rotates and translates horizontally it simulates a biomechanically plausible forward roll.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the 15 points for the body in local (body‐centered) coordinates.
# These coordinates are chosen to give a curled posture that one might see during a forward roll.
#
# Marker assignments (approximate):
#  1: Head
#  2: Left Shoulder      3: Right Shoulder
#  4: Left Elbow         5: Right Elbow
#  6: Left Hand          7: Right Hand
#  8: Spine              9: Left Hip
# 10: Right Hip         11: Left Knee
# 12: Right Knee        13: Left Ankle
# 14: Right Ankle       15: Mid Pelvis
#
# Units are arbitrary (meters, say) but chosen to be roughly proportionate.

local_points = np.array([
    [0.00,  0.15],   # 1. Head (top of head)
    [-0.08, 0.12],   # 2. Left Shoulder
    [0.08,  0.12],   # 3. Right Shoulder
    [-0.12, 0.05],   # 4. Left Elbow
    [0.12,  0.05],   # 5. Right Elbow
    [-0.15, -0.02],  # 6. Left Hand
    [0.15,  -0.02],  # 7. Right Hand
    [0.00,  0.00],   # 8. Spine
    [-0.08, -0.08],  # 9. Left Hip
    [0.08,  -0.08],  # 10. Right Hip
    [-0.10, -0.16],  # 11. Left Knee
    [0.10,  -0.16],  # 12. Right Knee
    [-0.10, -0.24],  # 13. Left Ankle
    [0.10,  -0.24],  # 14. Right Ankle
    [0.00,  -0.10]   # 15. Mid Pelvis (an extra marker near the hips)
])

# Animation parameters
frames = 200       # number of frames in one roll cycle
interval = 30      # interval between frames in milliseconds
total_rolls = 1    # number of complete forward rolls to show

# Pre-calculate total number of frames (if you want multiple rolls, adjust accordingly)
total_frames = frames * total_rolls

# The horizontal distance traveled during one complete roll.
# Assuming a non-slipping roll, the distance equals the arc length that the body “wheel” covers.
# We estimate an effective rolling radius from the body’s dimensions.
effective_radius = 0.12
roll_circumference = 2 * np.pi * effective_radius

# Set up the figure and axis.
fig, ax = plt.subplots(figsize=(6, 4))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Scatter plot of the 15 points (white markers)
scat = ax.scatter([], [], c='white', s=80)

# Set axis limits. We allow some extra space for the translation.
ax.set_xlim(-0.5, roll_circumference * total_rolls + 0.5)
ax.set_ylim(0, 0.6)
ax.set_aspect('equal')
ax.axis('off')  # Hide axes

def rotate_points(points, angle):
    """Rotate points (Nx2) by the given angle (in radians) about the origin."""
    cos_ang = np.cos(angle)
    sin_ang = np.sin(angle)
    R = np.array([[cos_ang, -sin_ang],
                  [sin_ang,  cos_ang]])
    return points.dot(R.T)

def update(frame):
    # Normalized time [0,1]
    t = frame / frames

    # For a complete roll the body rotates 360 degrees.
    angle = 2 * np.pi * t

    # Compute rotated positions from local coordinates.
    rotated = rotate_points(local_points, angle)

    # To simulate roll without sinking below the ground, we shift vertically so that the lowest point touches y=0.
    y_min = np.min(rotated[:, 1])
    vertical_shift = -y_min  # so that min_y becomes 0

    # Horizontal translation: assuming non-slip, translation equals arc length traveled.
    horizontal_shift = roll_circumference * (frame / frames)

    # Global positions = rotated points shifted by the translation
    global_points = rotated + np.array([horizontal_shift, vertical_shift])

    # Update scatter plot data.
    scat.set_offsets(global_points)
    
    return scat,

# Create the animation.
anim = FuncAnimation(fig, update, frames=total_frames, interval=interval, blit=True, repeat=True)

# To display the animation in a window, use plt.show().
# (Alternatively, one can save it as an MP4 or GIF.)
plt.show()