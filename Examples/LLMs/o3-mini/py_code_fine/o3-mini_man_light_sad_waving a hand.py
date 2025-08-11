
"""
This program displays a point‐light animation (15 white dots on a black background)
representing a “sadman with light weight” who is waving one hand.
We simulate the figure as 15 body joints of a stick‐figure-like structure.
The right arm (right elbow and right hand) moves in an oscillatory (waving) manner
that is biomechanically plausible. The animation is implemented using matplotlib’s
animation module.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to rotate a 2D vector by a given angle (in radians)
def rotate(vec, angle):
    rot_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                           [np.sin(angle),  np.cos(angle)]])
    return rot_matrix @ vec

# Define the fixed base positions (in normalized coordinates) for 15 joint points.
# The coordinate system: x horizontal, y vertical.
# Figure design (base positions):
#  1: Head          (0, 0.9)
#  2: Neck          (0, 0.85)
#  3: Spine         (0, 0.8)
#  4: Left Shoulder (-0.1, 0.85)
#  5: Right Shoulder (0.1, 0.85)
#  6: Left Elbow     (-0.15, 0.75)
#  7: Right Elbow    (0.15, 0.75) --> to be updated during wave motion
#  8: Left Hand      (-0.2, 0.65)
#  9: Right Hand     (0.2, 0.65)  --> to be updated during wave motion
# 10: Left Hip       (-0.1, 0.6)
# 11: Right Hip      (0.1, 0.6)
# 12: Left Knee      (-0.1, 0.4)
# 13: Right Knee     (0.1, 0.4)
# 14: Left Ankle     (-0.1, 0.2)
# 15: Right Ankle    (0.1, 0.2)

# Create a dictionary of base coordinates for all joints.
base_joints = {
    "head":        np.array([0.0, 0.9]),
    "neck":        np.array([0.0, 0.85]),
    "spine":       np.array([0.0, 0.8]),
    "L_shoulder":  np.array([-0.1, 0.85]),
    "R_shoulder":  np.array([0.1, 0.85]),
    "L_elbow":     np.array([-0.15, 0.75]),
    "R_elbow":     np.array([0.15, 0.75]),
    "L_hand":      np.array([-0.2, 0.65]),
    "R_hand":      np.array([0.2, 0.65]),
    "L_hip":       np.array([-0.1, 0.6]),
    "R_hip":       np.array([0.1, 0.6]),
    "L_knee":      np.array([-0.1, 0.4]),
    "R_knee":      np.array([0.1, 0.4]),
    "L_ankle":     np.array([-0.1, 0.2]),
    "R_ankle":     np.array([0.1, 0.2])
}

# For our waving action, we will dynamically update the right arm.
# We define the arm segments relative to the right shoulder.
# Base vector from right shoulder to right hand:
base_R_arm = base_joints["R_hand"] - base_joints["R_shoulder"]
# For a realistic motion, we'll update the right elbow as the midpoint of the rotated arm.
# The right elbow will be placed halfway along the rotated vector.
base_R_elbow_offset = 0.5 * base_R_arm

# Animation parameters
fps = 30            # frames per second
duration = 4        # duration in seconds
total_frames = fps * duration

# Wave motion parameters
# We simulate a smooth waving motion by rotating the entire right arm about the right shoulder.
max_wave_angle = np.pi/6  # maximum rotation of 30 degrees
# omega controls speed; here one full cycle (back and forth) every 1.5 seconds.
omega = 2 * np.pi / 1.5

# Prepare a list of joint names to plot in a fixed order.
joint_names = ["head", "neck", "spine", "L_shoulder", "R_shoulder",
               "L_elbow", "R_elbow", "L_hand", "R_hand",
               "L_hip", "R_hip", "L_knee", "R_knee", "L_ankle", "R_ankle"]

# Initialize an array for joint positions (15,2)
def get_joint_positions(t):
    # Start from base positions
    joints = {name: coord.copy() for name, coord in base_joints.items()}
    
    # Compute wave rotation angle as a function of time (oscillatory motion)
    wave_angle = max_wave_angle * np.sin(omega * t)
    
    # Update right arm joints (elbow and hand) by rotating their base offsets using wave_angle.
    R_shoulder = joints["R_shoulder"]
    # New right hand position: rotate the base_R_arm vector and add to shoulder.
    rotated_R_arm = rotate(base_R_arm, wave_angle)
    joints["R_hand"] = R_shoulder + rotated_R_arm
    # New right elbow position: halfway along the rotated arm.
    joints["R_elbow"] = R_shoulder + 0.5*rotated_R_arm

    # (Optionally, small body sway can be added to other joints for more realism.)
    # Here we let the rest remain fixed.
    return np.array([joints[name] for name in joint_names])

# Set up the plot
fig, ax = plt.subplots(figsize=(5,8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')
# Set axis limits with some margin, coordinates are roughly in [-0.4, 0.4] x [0.1, 1.0]
ax.set_xlim(-0.4, 0.4)
ax.set_ylim(0.0, 1.0)

# Initialize scatter plot with 15 white points.
scatter = ax.scatter([], [], s=100, c='white')

# Update function for each frame
def update(frame):
    t = frame / fps
    positions = get_joint_positions(t)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
anim = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

plt.show()