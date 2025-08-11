#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
This program displays a point-light stimulus animation of a "sad man" carrying a heavy weight
while walking. There are exactly 15 white point-lights on a black background, and the motion is
biomechanically plausible, coherent, and smooth.
"""

# Number of points in the stimulus
NUM_POINTS = 15

# Total number of animation frames
NUM_FRAMES = 200

# Walking cycle duration in frames
CYCLE_FRAMES = 100

# Create figure and axis with black background
fig = plt.figure(figsize=(6, 6), facecolor="black")
ax = fig.add_subplot(111)
ax.set_facecolor("black")
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.2, 2.2)
ax.set_aspect("equal")
ax.axis("off")

# Scatter object for the 15 point-lights
scatter_plot = ax.scatter([], [], c="white", s=50)

def sad_man_biomotion(t):
    """
    Returns an array of shape (NUM_POINTS, 2) with (x,y) positions for the 15 point-lights.
    't' is a value from 0 to 1 representing the fraction of the walking cycle.
    
    We simulate a simple skeleton with:
      0  - Head
      1  - Neck
      2  - Right Shoulder
      3  - Left Shoulder
      4  - Right Elbow
      5  - Left Elbow
      6  - Right Hand
      7  - Left Hand
      8  - Torso/Pelvis
      9  - Right Hip
      10 - Left Hip
      11 - Right Knee
      12 - Left Knee
      13 - Right Foot
      14 - Left Foot
    
    The figure is slightly stooped forward, carrying a "heavy weight" in front.
    A walking cycle is approximated with sinusoidal joints and small forward motion.
    """
    
    # Angles for legs and arms (simple sinusoidal model of walking).
    # We'll define the right and left sides to be out of phase by pi.
    # t goes 0 -> 1 over one walking cycle.
    phase = 2 * np.pi * t
    
    # Vertical bob of the pelvis/torso
    # Slight up-down motion
    torso_y_bob = 0.05 * np.sin(2 * phase)
    
    # Forward motion along x-axis
    # He moves slowly forward, but remains near center visually (we only show partial translation).
    forward_x = 0.2 * (t - 0.5)
    
    # Leg angles
    # Right leg swings forward when phase in [0, pi], left leg forward in [pi, 2pi].
    # We'll make them smaller amplitude to look "heavy" or "sad".
    right_leg_angle =  0.4 * np.sin(phase)
    left_leg_angle  = -0.4 * np.sin(phase)
    
    # Knee bend (some fraction of leg angle)
    right_knee_bend = 0.5 * right_leg_angle
    left_knee_bend  = 0.5 * left_leg_angle
    
    # Arm angles (carrying weight in front, so limited swing)
    # We'll keep arms forward and relatively still, with a small sway
    right_arm_angle =  0.1 * np.sin(phase)
    left_arm_angle  = -0.1 * np.sin(phase)
    
    # Stooped torso angle (leaning forward)
    torso_angle = 0.2  # 0 is upright, positive is forward tilt
    
    # Base positions (pelvis as origin in this local model)
    pelvis_x = 0.0 + forward_x
    pelvis_y = 1.0 + torso_y_bob
    
    # Torso length segments
    head_height = 0.25
    torso_height = 0.3
    shoulder_offset = 0.2
    
    # Limb segment lengths (approximate):
    upper_arm_len = 0.25
    forearm_len = 0.25
    thigh_len = 0.4
    shin_len = 0.4
    
    # -------------------------------------------
    # Compute main reference points
    # -------------------------------------------
    # Pelvis (8)
    pelvis = np.array([pelvis_x, pelvis_y])
    
    # Torso top (near shoulders) - rotate by torso_angle from pelvis
    torso_top_offset = np.array([0, torso_height])
    # Apply a forward tilt:
    rot_torso = np.array([
        [np.cos(torso_angle), -np.sin(torso_angle)],
        [np.sin(torso_angle),  np.cos(torso_angle)]
    ])
    torso_top = pelvis + rot_torso @ torso_top_offset
    
    # Neck (1) and Head (0) positions
    neck_offset = np.array([0, 0.1])
    head_offset = np.array([0, head_height])
    neck = torso_top + rot_torso @ neck_offset
    head = neck + rot_torso @ head_offset
    
    # Shoulders (2 - right, 3 - left)
    # Shoulders spaced horizontally around torso_top
    right_shoulder_offset = np.array([ shoulder_offset, 0])
    left_shoulder_offset  = np.array([-shoulder_offset, 0])
    right_shoulder = torso_top + rot_torso @ right_shoulder_offset
    left_shoulder  = torso_top + rot_torso @ left_shoulder_offset
    
    # -------------------------------------------
    # Arms
    # -------------------------------------------
    # We'll place both arms somewhat forward, as if holding a heavy weight in front.
    # Right arm
    # Shoulder -> elbow
    # We'll pivot the entire arm forward by (some base angle + arm swing)
    base_arm_angle = 0.8  # arms forward
    r_arm_total_angle = base_arm_angle + right_arm_angle
    rot_r_arm = np.array([
        [np.cos(r_arm_total_angle), -np.sin(r_arm_total_angle)],
        [np.sin(r_arm_total_angle),  np.cos(r_arm_total_angle)]
    ])
    right_elbow = right_shoulder + rot_r_arm @ np.array([0, -upper_arm_len])
    
    # Elbow -> hand
    # Keep forearm roughly in line (no big bend)
    right_hand = right_elbow + rot_r_arm @ np.array([0, -forearm_len])
    
    # Left arm
    l_arm_total_angle = base_arm_angle + left_arm_angle
    rot_l_arm = np.array([
        [np.cos(l_arm_total_angle), -np.sin(l_arm_total_angle)],
        [np.sin(l_arm_total_angle),  np.cos(l_arm_total_angle)]
    ])
    left_elbow = left_shoulder + rot_l_arm @ np.array([0, -upper_arm_len])
    left_hand = left_elbow + rot_l_arm @ np.array([0, -forearm_len])
    
    # -------------------------------------------
    # Hips & Legs
    # -------------------------------------------
    # Right Hip (9) & Left Hip (10) 
    # We'll space them around pelvis
    hip_offset = 0.15
    right_hip = pelvis + np.array([ hip_offset, 0])
    left_hip  = pelvis + np.array([-hip_offset, 0])
    
    # Right Leg
    # Hip -> knee
    rot_r_leg = np.array([
        [np.cos(right_leg_angle), -np.sin(right_leg_angle)],
        [np.sin(right_leg_angle),  np.cos(right_leg_angle)]
    ])
    right_knee = right_hip + rot_r_leg @ np.array([0, -thigh_len])
    # Knee -> foot
    rot_r_shin = np.array([
        [np.cos(right_knee_bend), -np.sin(right_knee_bend)],
        [np.sin(right_knee_bend),  np.cos(right_knee_bend)]
    ])
    right_foot = right_knee + rot_r_leg @ (rot_r_shin @ np.array([0, -shin_len]))
    
    # Left Leg
    rot_l_leg = np.array([
        [np.cos(left_leg_angle), -np.sin(left_leg_angle)],
        [np.sin(left_leg_angle),  np.cos(left_leg_angle)]
    ])
    left_knee = left_hip + rot_l_leg @ np.array([0, -thigh_len])
    rot_l_shin = np.array([
        [np.cos(left_knee_bend), -np.sin(left_knee_bend)],
        [np.sin(left_knee_bend),  np.cos(left_knee_bend)]
    ])
    left_foot = left_knee + rot_l_leg @ (rot_l_shin @ np.array([0, -shin_len]))
    
    # Gather all 15 points in order:
    # 0:Head, 1:Neck, 2:RShoulder, 3:LShoulder, 4:RElbow, 5:LElbow,
    # 6:RHand, 7:LHand, 8:Torso/Pelvis, 9:RHip, 10:LHip,
    # 11:RKnee, 12:LKnee, 13:RFoot, 14:LFoot
    points = np.array([
        head,
        neck,
        right_shoulder,
        left_shoulder,
        right_elbow,
        left_elbow,
        right_hand,
        left_hand,
        pelvis,
        right_hip,
        left_hip,
        right_knee,
        left_knee,
        right_foot,
        left_foot
    ])
    
    return points


def init():
    """Initialize the scatter plot for animation."""
    scatter_plot.set_offsets(np.zeros((NUM_POINTS, 2)))
    return (scatter_plot,)

def update(frame):
    """Update the scatter plot for each frame."""
    # Fraction of the cycle
    t = (frame % CYCLE_FRAMES) / float(CYCLE_FRAMES)
    
    # Get coordinates of all 15 points
    coords = sad_man_biomotion(t)
    scatter_plot.set_offsets(coords)
    
    return (scatter_plot,)

anim = FuncAnimation(
    fig, update, frames=NUM_FRAMES, init_func=init, blit=True, interval=50
)

plt.show()