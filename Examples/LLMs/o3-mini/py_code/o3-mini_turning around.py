
"""
This program creates a point‐light biological motion animation of a man "turning around".
It uses 15 white point‐lights on a black background to represent the joints of a human
skeleton. The turning motion is produced by rotating the 3D joint coordinates about the
vertical (y) axis and projecting them onto a 2D plane with a simple perspective.

The 15 joints (in a scaled 3D coordinate system) are:
   0: Head
   1: Neck
   2: Right Shoulder
   3: Right Elbow
   4: Right Hand
   5: Left Shoulder
   6: Left Elbow
   7: Left Hand
   8: Trunk
   9: Right Hip
  10: Right Knee
  11: Right Foot
  12: Left Hip
  13: Left Knee
  14: Left Foot

The rotation is applied in the x–z plane (with y as vertical). A perspective projection
is used so that parts rotating “into depth” are slightly scaled. The result is a smooth,
biomechanically plausible turning animation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----- Parameters for visual scaling and perspective -----
s = 200          # scaling factor for body dimensions (to get pixels roughly)
f = 500          # focal length for perspective projection

# ----- Define the 15 joint (point-light) positions in 3D (x, y, z) -----
# The coordinates are defined so that y is vertical. z=0 initially.
# All coordinates are in "meters", then scaled by s.
joints = np.array([
    [0.0,   1.8, 0.0],   # head
    [0.0,   1.6, 0.0],   # neck
    [-0.2,  1.6, 0.0],   # right shoulder
    [-0.5,  1.4, 0.0],   # right elbow
    [-0.7,  1.2, 0.0],   # right hand
    [0.2,   1.6, 0.0],   # left shoulder
    [0.5,   1.4, 0.0],   # left elbow
    [0.7,   1.2, 0.0],   # left hand
    [0.0,   1.2, 0.0],   # trunk (approx mid-torso)
    [-0.2,  1.0, 0.0],   # right hip
    [-0.2,  0.6, 0.0],   # right knee
    [-0.2,  0.2, 0.0],   # right foot
    [0.2,   1.0, 0.0],   # left hip
    [0.2,   0.6, 0.0],   # left knee
    [0.2,   0.2, 0.0]    # left foot
])
# Scale the coordinates so that the figure appears large enough.
joints *= s

# ----- Set up the matplotlib figure -----
fig, ax = plt.subplots(figsize=(6,8))
ax.set_facecolor("black")
plt.axis("equal")
plt.axis("off")
# Set limits so the full projected figure is visible even during rotation.
margin = s * 1.5
ax.set_xlim(-margin, margin)
ax.set_ylim(0, s*2.5)

# Create a scatter plot for the 15 point-light markers
scat = ax.scatter([], [], s=80, c="white")

# ----- Animation update function -----
def animate(frame):
    # Rotate continuously: 360 degrees every 10 seconds.
    # Assuming 40 ms between frames, 250 frames per cycle => angle in radians.
    theta = 2 * np.pi * (frame / 250)
    
    # Rotation about vertical y-axis: rotate points in the x-z plane.
    # For each joint with original (x, y, z), the rotated coordinates are:
    #   x' = cos(theta)*x + sin(theta)*z   (but originally z=0)
    #   z' = -sin(theta)*x + cos(theta)*z  --> becomes -sin(theta)*x
    #   y' = y (unchanged)
    #
    # So effectively:
    #   x_rotated = cos(theta)*x
    #   z_rotated = - sin(theta)*x
    #   y_rotated = y
    #
    # Then apply a simple perspective projection:
    #   xp = f * (x_rotated) / (f - z_rotated)
    #   yp = f * (y_rotated) / (f - z_rotated)
    rotated = np.empty_like(joints)
    cos_t = np.cos(theta)
    sin_t = np.sin(theta)
    
    # Original x and y (and z=0) from joints:
    X = joints[:, 0]
    Y = joints[:, 1]
    # After rotation:
    X_rot = cos_t * X  # because z=0
    Z_rot = - sin_t * X
    Y_rot = Y
    
    # Perspective projection:
    # To avoid division by zero, assume f - Z_rot is always > 0 (which it will be in our range).
    denominator = (f - Z_rot)
    xp = f * X_rot / denominator
    yp = f * Y_rot / denominator
    
    # Optionally, to give a cue for depth, you can adjust the marker size with depth. 
    # Here we make closer points appear slightly larger.
    # We'll scale the marker size inversely with (f - Z_rot)
    marker_sizes = 80 * (f / denominator)**2
    
    data = np.column_stack([xp, yp])
    scat.set_offsets(data)
    scat.set_sizes(marker_sizes)
    return scat,

# ----- Create and run the animation -----
animation = FuncAnimation(fig, animate, frames=250, interval=40, blit=True)

plt.show()