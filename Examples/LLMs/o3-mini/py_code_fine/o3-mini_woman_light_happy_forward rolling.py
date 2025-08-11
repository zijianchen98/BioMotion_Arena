
"""
This program displays a point‐light animation that simulates a “happy woman with light weight forward rolling.”
It uses 15 white dots (markers) moving against a solid black background. Each dot represents a key body‐joint.
The animation approximates a biomechanically plausible forward roll by making the rigid “body” (defined in 
an initial upright configuration) rotate and translate with small phase offsets applied to individual joints,
giving a non‐rigid, natural “tuck–and “roll” effect.
 
Requirements:
  • 15 white “point‐lights” (dots) against a black background.
  • The action shown is a forward roll (like a somersault) performed by a happy woman.
  • The movement is smooth, coherent, and “biologically plausible”.
 
Note:
  This code uses matplotlib’s animation functionality. Install matplotlib if needed:
      pip install matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
# Define the configuration of the 15 markers.
# Each marker is assigned an (x,y) coordinate in the initial (upright) pose.
#
# The coordinates here are chosen to roughly represent a human figure:
#   0 : Head
#   1 : Left Shoulder
#   2 : Right Shoulder
#   3 : Left Elbow
#   4 : Right Elbow
#   5 : Left Wrist
#   6 : Right Wrist
#   7 : Mid Torso
#   8 : Left Hip
#   9 : Right Hip
#  10 : Left Knee
#  11 : Right Knee
#  12 : Left Ankle
#  13 : Right Ankle
#  14 : Belly (or lower-torso) marker
# 
# The positions are in arbitrary units.
# -----------------------------
initial_positions = np.array([
    [0, 80],    # Head
    [-10, 70],  # Left shoulder
    [10, 70],   # Right shoulder
    [-20, 55],  # Left elbow
    [20, 55],   # Right elbow
    [-25, 40],  # Left wrist
    [25, 40],   # Right wrist
    [0, 50],    # Mid torso
    [-10, 35],  # Left hip
    [10, 35],   # Right hip
    [-10, 20],  # Left knee
    [10, 20],   # Right knee
    [-10, 5],   # Left ankle
    [10, 5],    # Right ankle
    [0, 60]     # Belly (an extra marker near the torso)
])

# We define the body center of mass (COM) for the initial (upright) pose.
# Let’s choose the mid torso as COM.
COM_initial = np.array([0, 50])

# Compute the relative positions of each marker with respect to COM.
rel_positions = initial_positions - COM_initial

# We now assign a small phase offset (in radians) to each marker.
# These offsets will help simulate slight non-rigid deformations during the roll.
phase_shifts = np.array([
    -0.10,   # head
     0.00,   # left shoulder
     0.00,   # right shoulder
     0.10,   # left elbow
     0.10,   # right elbow
     0.15,   # left wrist
     0.15,   # right wrist
     0.00,   # mid torso
    -0.05,   # left hip
    -0.05,   # right hip
    -0.10,   # left knee
    -0.10,   # right knee
    -0.15,   # left ankle
    -0.15,   # right ankle
     0.05    # belly
])

# -----------------------------
# Animation parameters
# -----------------------------
duration = 6       # duration of the animation in seconds
fps = 30           # frames per second
n_frames = duration * fps

# The overall roll: we'll have the body complete one full 360° rotation during the roll.
# So the base roll angle at normalized time u (0 to 1) is:
def roll_angle(u):
    return 2 * np.pi * u   # one full rotation

# The body (COM) also moves horizontally to mimic forward motion.
# We let the COM move to the right by a fixed distance.
def COM_offset(u):
    distance = 300  # total horizontal translation in arbitrary units
    return np.array([distance * u, 0])

# Rotation matrix for a given angle (in radians)
def rotation_matrix(angle):
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    return np.array([[cos_a, -sin_a], [sin_a, cos_a]])

# -----------------------------
# Set up the matplotlib figure and axis.
# -----------------------------
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor("black")
fig.patch.set_facecolor("black")

# Set axis limits to give enough room for the roll.
ax.set_xlim(-50, 350)
ax.set_ylim(-50, 150)
ax.set_aspect('equal')
ax.axis("off")  # Hide the axes

# Scatter plot for the 15 markers.
scat = ax.scatter(initial_positions[:,0], initial_positions[:,1], c="white", s=50)

# -----------------------------
# Update function for the animation.
# -----------------------------
def update(frame):
    # Normalize time between 0 and 1.
    u = frame / n_frames
    base_angle = roll_angle(u)
    
    # Compute the new body center = initial COM + offset.
    current_COM = COM_initial + COM_offset(u)
    
    # For each marker, compute its new position by:
    #   new_pos = current_COM + R(base_angle + phase_offset) * (initial_relative_position)
    new_positions = []
    for i in range(len(rel_positions)):
        angle = base_angle + phase_shifts[i]
        R = rotation_matrix(angle)
        pos = current_COM + (R @ rel_positions[i])
        new_positions.append(pos)
    new_positions = np.array(new_positions)
    
    # Update the scatter plot positions.
    scat.set_offsets(new_positions)
    return scat,

# -----------------------------
# Create the animation.
# -----------------------------
anim = FuncAnimation(fig, update, frames=n_frames, interval=1000/fps, blit=True)

# To display the animation in a window use plt.show()
plt.show()

# Optionally, save the animation as an MP4 video file (requires ffmpeg)
# anim.save("forward_roll.mp4", fps=fps, extra_args=['-vcodec', 'libx264'])
