#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of animation frames
FRAMES = 60
FPS = 30
DURATION = FRAMES / FPS  # seconds

# We have 15 points (head, shoulders, elbows, wrists, pelvis, hips, knees, ankles).
# Define a function that returns their (x, y) positions at a given time fraction t in [0, 1].
# This is a simple keyframe-based approach approximating a "sad" posture jump forward.

def get_joint_positions(t):
    """
    Return an array of shape (15, 2) specifying the x,y positions for each
    of 15 point-lights that approximate a 'sad-man' jumping forward.
    t in [0,1] is the normalized time for one jump cycle.
    """
    
    # Overall horizontal displacement for the jump
    # Using a simple ease-in-out from x=0 to x=2
    # Applies to the entire body (center of mass).
    jump_distance = 2.0
    x_shift = jump_distance * (3*t**2 - 2*t**3)  # Smooth cubic from 0 to 1
    
    # Vertical motion of the center of mass (y_shift)
    # A parabolic jump shape: 4t(1 - t) scaled for apex
    jump_height = 0.6
    y_shift = jump_height * (4 * t * (1 - t))

    # Basic posture parameters (approximate proportions for a 1.7-1.8m figure):
    head_y = 1.6
    shoulder_y = 1.2
    pelvis_y = 0.8
    hip_y = 0.8
    knee_y = 0.4
    ankle_y = 0.0

    # Lateral offsets (for left/right body points)
    shoulder_offset = 0.15
    hip_offset = 0.12
    elbow_offset = 0.22
    wrist_offset = 0.25
    
    # "Sad" factor: arms droop more forward at time 0 or 1, slightly lift at mid-jump
    # We let arms be forward at t=0 and t=1, and less forward at t=0.5
    # for a quick approximation:
    droop_amount = 0.15 + 0.1*np.cos(np.pi * 2 * t)

    # Slight bend in knees at start (t=0) and end (t=1). They straighten mid-jump:
    knee_bend = 0.15 * np.cos(np.pi * 2 * t)

    # We'll define each joint's reference position (x,y) ignoring jump shift,
    # then add x_shift, y_shift and additional posture adjustments.

    # HEAD (single point)
    head = [0.0, head_y]

    # SHOULDERS (left, right)
    left_shoulder  = [-shoulder_offset, shoulder_y]
    right_shoulder = [ shoulder_offset, shoulder_y]

    # ELBOWS (left, right)
    # Add droop_amount to x for both elbows to produce forward droop
    left_elbow  = [-(shoulder_offset + droop_amount), 0.9]
    right_elbow = [ (shoulder_offset + droop_amount), 0.9]

    # WRISTS (left, right)
    # Droop them further out
    left_wrist  = [-(wrist_offset + droop_amount), 0.7]
    right_wrist = [ (wrist_offset + droop_amount), 0.7]

    # PELVIS (single point)
    pelvis = [0.0, pelvis_y]

    # HIPS (left, right)
    left_hip  = [-hip_offset, hip_y]
    right_hip = [ hip_offset, hip_y]

    # KNEES (left, right)
    # Additional knee bend is subtracted from y
    left_knee  = [-hip_offset, knee_y + knee_bend]
    right_knee = [ hip_offset, knee_y + knee_bend]

    # ANKLES (left, right)
    left_ankle  = [-hip_offset, ankle_y]
    right_ankle = [ hip_offset, ankle_y]

    # Combine them in a list (15 points)
    points = np.array([
        head,
        left_shoulder,
        right_shoulder,
        left_elbow,
        right_elbow,
        left_wrist,
        right_wrist,
        pelvis,
        left_hip,
        right_hip,
        left_knee,
        right_knee,
        left_ankle,
        right_ankle,
        # Extra point: let's place "center of mass" or mid-torso
        [0.0, (shoulder_y + pelvis_y)/2.0],
    ])

    # Add global jump shift (x_shift, y_shift) to each point
    points[:, 0] += x_shift
    points[:, 1] += y_shift

    return points

# Create a figure with black background
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1, 3)   # Some leeway for horizontal motion
ax.set_ylim(-0.5, 2) # Vertical range to see the jump
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

# Create the scatter plot for the points
scatter_plot = ax.scatter([], [], color='white', s=20)

def init():
    scatter_plot.set_offsets([])
    return (scatter_plot,)

def update(frame):
    # frame goes from 0 to FRAMES-1
    t = frame / (FRAMES - 1)
    pts = get_joint_positions(t)
    scatter_plot.set_offsets(pts)
    return (scatter_plot,)

ani = animation.FuncAnimation(
    fig, update, frames=FRAMES, init_func=init,
    interval=1000/FPS, blit=True
)

plt.show()