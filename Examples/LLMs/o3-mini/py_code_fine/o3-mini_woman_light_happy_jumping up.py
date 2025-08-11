
"""
This program displays an animation of a point‐light stimulus representing biological motion –
a happy, light‐weight woman jumping upward. The figure is represented by exactly 15 white points 
on a solid black background. The motion is smooth and biomechanically plausible over each jump cycle.

The 15 points represent major joints and markers:
  0: Head top (with an extra "happy" marker)
  1: Left shoulder
  2: Right shoulder
  3: Left elbow
  4: Right elbow
  5: Left hand
  6: Right hand
  7: Chest (torso center)
  8: Left hip
  9: Right hip
 10: Left knee
 11: Right knee
 12: Left foot
 13: Right foot
 14: Extra marker near the head (simulating a joyful feature)

The jump cycle is modeled by applying a vertical displacement to all points following a parabola
(for biomechanically plausible upward acceleration and downward deceleration). In addition, to 
enhance the realism, the arms and knees adjust their positions slightly during the jump.

Run this script to see the animation.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Duration of one jump cycle (in seconds) and frames per second
duration = 2.0     # seconds for one full jump cycle
fps = 60
total_frames = int(duration * fps)

# Peak jump height
H = 40  # maximum vertical displacement in pixels

# Define the base positions for the 15 markers (x, y) in a coordinate system.
# These coordinates are chosen to represent a simplistic human figure.
# Units are arbitrary and will be used in the plot limits.
base_points = np.array([
    [0,   170],    # 0: Head (marker)
    [-15, 150],    # 1: Left shoulder
    [15,  150],    # 2: Right shoulder
    [-40, 130],    # 3: Left elbow
    [40,  130],    # 4: Right elbow
    [-55, 110],    # 5: Left hand
    [55,  110],    # 6: Right hand
    [0,   120],    # 7: Chest/Torso center
    [-15, 100],    # 8: Left hip
    [15,  100],    # 9: Right hip
    [-15, 60],     # 10: Left knee
    [15,  60],     # 11: Right knee
    [-15, 0],      # 12: Left foot
    [15,  0],      # 13: Right foot
    [0,   180]     # 14: Extra happy marker near the head
])

# Function that returns vertical displacement (jump arc) given normalized time t in [0,1]
def jump_displacement(t):
    # Parabolic jump movement: This gives 0 at t=0 and t=1, and maximum H at t=0.5.
    return 4 * H * t * (1 - t)

# Additional dynamic adjustments for realism:
def arm_offset(t):
    # Arms swing upward to assist in the jump.
    # Use a sine function that peaks at mid-jump.
    return 10 * np.sin(np.pi * t)

def knee_offset(t):
    # Knees bend (tuck) during the jump.
    return 10 * np.sin(np.pi * t)

# Create the figure and axis with black background.
fig, ax = plt.subplots(figsize=(5, 8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Set the plot limits to comfortably contain our full motion.
ax.set_xlim(-100, 100)
ax.set_ylim(-20, 220)

# Create initial scatter for the 15 white points.
scatter = ax.scatter(base_points[:, 0], base_points[:, 1], s=80, c='white')

# Animation update function. frame is an integer frame index.
def update(frame):
    # Normalize time over one cycle [0,1]
    t = (frame % total_frames) / total_frames

    # Compute the overall vertical displacement for this frame.
    dy = jump_displacement(t)

    # Create a copy of the base points to modify for this frame.
    points = base_points.copy()

    # All points are shifted upward by dy (the jump arc).
    points[:, 1] += dy

    # Adjust arm markers to simulate a natural swing:
    # Modify left elbow (index 3) and left hand (index 5)
    # Modify right elbow (index 4) and right hand (index 6)
    arm_dy = arm_offset(t)
    for i in [3, 5, 4, 6]:
        points[i, 1] += arm_dy

    # Adjust knee markers (indices 10 and 11) to represent leg flexion.
    knee_dy = knee_offset(t)
    for i in [10, 11]:
        points[i, 1] += knee_dy

    # Update scatter plot data.
    scatter.set_offsets(points)
    return scatter,

# Create animation using FuncAnimation.
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

plt.show()