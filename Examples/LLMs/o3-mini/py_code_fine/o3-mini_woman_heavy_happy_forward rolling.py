
"""
This program shows a point‐light stimulus animation representing a “happy woman with heavy weight”
performing a forward roll. The animation depicts exactly 15 white point‐lights on a solid black
background. The points represent key “joints” of the body. The forward‐rolling motion is achieved
by gradually rotating the figure about its center of mass while translating it forward with a slight
vertical oscillation (to mimic a natural roll of a heavy body in a tucked, “happy” posture).

Press the window’s close button to end the animation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Define the 15 point coordinates ---
# The points represent: 0: head, 1: left_shoulder, 2: right_shoulder, 3: left_elbow, 4: right_elbow,
# 5: left_hand, 6: right_hand, 7: chest, 8: abdomen, 9: left_hip, 10: right_hip, 11: left_knee,
# 12: right_knee, 13: left_ankle, 14: right_ankle.
# These coordinates are chosen to roughly resemble a "tucked" posture for a forward roll.
points = np.array([
    [0.0, 1.0],      # head
    [-0.2, 0.9],     # left_shoulder
    [0.2, 0.9],      # right_shoulder
    [-0.4, 0.6],     # left_elbow
    [0.4, 0.6],      # right_elbow
    [-0.5, 0.3],     # left_hand
    [0.5, 0.3],      # right_hand
    [0.0, 0.8],      # chest
    [0.0, 0.5],      # abdomen
    [-0.2, 0.3],     # left_hip
    [0.2, 0.3],      # right_hip
    [-0.2, 0.0],     # left_knee
    [0.2, 0.0],      # right_knee
    [-0.2, -0.3],    # left_ankle
    [0.2, -0.3]      # right_ankle
])

# Compute the center of mass of the figure (used as rotation center)
center_of_mass = np.mean(points, axis=0)


def rotate_points(pts, angle, center):
    """
    Rotate points by given angle (in radians) about a specified center.
    """
    # Create a 2x2 rotation matrix
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    # Shift points to origin, rotate, and shift back
    rotated = (pts - center) @ R.T + center
    return rotated


# Animation configuration
total_frames = 150          # total number of frames in the animation
roll_total_angle = 2 * np.pi  # full 360 degree roll over the animation
dx_per_frame = 0.03         # horizontal translation per frame (forward movement)
vertical_amp = 0.1          # small vertical oscillation amplitude for bounce effect

# Setup the figure and axis
fig, ax = plt.subplots()
fig.canvas.manager.set_window_title('Forward Rolling Point-Light Animation')
ax.set_facecolor('black')
plt.style.use('dark_background')

# Set up axis limits so that the animation stays visible
ax.set_xlim(-1, 5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Create scatter object; initially plotting the points
scat = ax.scatter(points[:, 0], points[:, 1], s=60, c='white')

def update(frame):
    # Determine the current rotation angle
    angle = roll_total_angle * frame / total_frames

    # Rotate the points about the center of mass
    rotated_points = rotate_points(points, angle, center_of_mass)

    # Compute translation: moving forward along x and slight vertical oscillation
    dx = dx_per_frame * frame
    dy = vertical_amp * np.sin(angle)  # slight up-and-down motion
    translation = np.array([dx, dy])
    transformed = rotated_points + translation

    # Update scatter plot data
    scat.set_offsets(transformed)
    return scat,

# Create animation using FuncAnimation
ani = FuncAnimation(fig, update, frames=total_frames, interval=50, blit=True, repeat=True)

# Display the animation
plt.show()