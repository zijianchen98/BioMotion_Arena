
"""
This program displays a point‐light stimulus animation of a “happy woman with light weight” turning around.
Fifteen white dots (point‐lights) representing key body joints are drawn on a solid black background.
The underlying skeleton is defined in a neutral pose, then for each frame the whole skeleton rotates
gradually (simulating a turning‐in‐place action) while adding small biomechanically plausible oscillations
to the arms and legs to evoke a “happy” light‐footed movement.
Press Ctrl+C or close the window to exit.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the base positions (in meters) for 15 points (joints)
# Coordinates are given as (x,y). y is vertical.
# Points:
#  0: Head
#  1: Left shoulder
#  2: Right shoulder
#  3: Left elbow
#  4: Right elbow
#  5: Left wrist
#  6: Right wrist
#  7: Torso (central body)
#  8: Left hip
#  9: Right hip
# 10: Left knee
# 11: Right knee
# 12: Left ankle
# 13: Right ankle
# 14: Right toe (extra point)
base_skeleton = np.array([
    [ 0.00, 1.80],   # Head
    [-0.20, 1.60],   # Left shoulder
    [ 0.20, 1.60],   # Right shoulder
    [-0.40, 1.40],   # Left elbow
    [ 0.40, 1.40],   # Right elbow
    [-0.50, 1.20],   # Left wrist
    [ 0.50, 1.20],   # Right wrist
    [ 0.00, 1.20],   # Torso (center of body)
    [-0.20, 1.00],   # Left hip
    [ 0.20, 1.00],   # Right hip
    [-0.20, 0.60],   # Left knee
    [ 0.20, 0.60],   # Right knee
    [-0.20, 0.20],   # Left ankle
    [ 0.20, 0.20],   # Right ankle
    [ 0.20, 0.00]    # Right toe (extra point)
])

# Set the number of frames and interval for the animation
n_frames = 120
interval = 50  # milliseconds between frames

# For rotation, choose the torso (point 7) as the center of rotation.
center = base_skeleton[7].copy()  # (0.0, 1.20)

# Create a figure with a black background and no axes.
fig, ax = plt.subplots(figsize=(5,8))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_xlim(-1,1)
ax.set_ylim(0,2.2)
ax.set_aspect('equal')
ax.axis("off")

# Create the scatter plot (white dots)
scatter = ax.scatter([], [], s=100, c='white')

def rotate_points(points, theta, center):
    """
    Rotate a set of points (N x 2) by angle theta (in radians) around a given center point.
    """
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    return (points - center) @ R.T + center

def get_frame_skeleton(frame):
    """
    For a given frame index, return the new skeleton positions after applying:
      1. A rotation by a smoothly changing angle.
      2. Small sinusoidal oscillations (for biomechanical plausibility) to arms and legs.
    """
    # Compute rotation angle. We'll complete a 360° turn over the animation.
    theta = 2 * np.pi * frame / n_frames

    # Copy the base skeleton to modify
    pos = base_skeleton.copy()
    
    # Add subtle oscillations.
    # Arms: left wrist (index 5) and right wrist (index 6) oscillate vertically in opposite phase.
    arm_amplitude = 0.05
    oscillation_arm = arm_amplitude * np.sin(2*np.pi*frame/n_frames*4)  # frequency factor 4

    pos[5, 1] += oscillation_arm      # left wrist goes up and down
    pos[6, 1] -= oscillation_arm      # right wrist oscillates in opposite phase

    # Elbows can have a bit of horizontal swing as well.
    elbow_amplitude = 0.03
    oscillation_elbow = elbow_amplitude * np.sin(2*np.pi*frame/n_frames*4 + np.pi/4)
    pos[3, 0] += -oscillation_elbow   # left elbow slightly left/right
    pos[4, 0] += oscillation_elbow    # right elbow slightly left/right

    # Legs: simulate a subtle bending motion at the knees and ankles.
    leg_amplitude = 0.03
    oscillation_leg = leg_amplitude * np.sin(2*np.pi*frame/n_frames*2)  # slower oscillation for legs

    # Left leg (knee and ankle)
    pos[10, 1] += oscillation_leg    # left knee vertical offset
    pos[12, 1] += oscillation_leg    # left ankle vertical offset

    # Right leg (knee and ankle) oscillate in opposite phase.
    pos[11, 1] -= oscillation_leg    # right knee vertical offset
    pos[13, 1] -= oscillation_leg    # right ankle vertical offset
    pos[14, 1] -= oscillation_leg    # right toe as well

    # Now apply the rotation to simulate turning.
    pos_rotated = rotate_points(pos, theta, center)
    return pos_rotated

def init():
    scatter.set_offsets([])
    return scatter,

def animate(frame):
    points = get_frame_skeleton(frame)
    scatter.set_offsets(points)
    return scatter,

ani = animation.FuncAnimation(fig, animate, frames=n_frames, init_func=init,
                              interval=interval, blit=True)

plt.show()