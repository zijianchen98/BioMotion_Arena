
"""
Point–light biological–motion stimulus
Sad, heavy woman running – 15 light–points
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sin, cos, pi

# ----------------------  KINEMATIC MODEL  ---------------------- #
# All angles are expressed in radians. 0 rad  ≙ pointing straight down.
# Positive angles rotate the segment forwards (to the right on screen).

# Segment lengths (arbitrary, but internally consistent)
THIGH_LEN     = 1.0
SHANK_LEN     = 1.0
TORSO_LEN     = 1.2
HEAD_OFFSET   = 0.35
UPPER_ARM_LEN = 0.75
FOREARM_LEN   = 0.75

# Body widths
PELVIS_WIDTH   = 0.45
SHOULDER_WIDTH = 0.55

# Gait parameters (slower, heavier looking running)
HIP_AMP    = np.deg2rad(35)          # max hip flex/extension
KNEE_AMP   = np.deg2rad(105)         # max knee flex
ARM_AMP    = np.deg2rad(45)          # arm swing
ELBOW_AMP  = np.deg2rad(80)          # elbow flex
CYCLE_DUR  = 0.9                     # duration of one full gait cycle [s]
FORWARD_V  = 2.0                     # forward speed (units / s)
BOUNCE_AMP = 0.12                    # vertical COM oscillation

# Convenience -----------------------------------------------------------------
def pol2cart(length, angle):
    """Return (dx, dy) from a length and an angle measured from -y (down)."""
    return ( length *  sin(angle),
            -length *  cos(angle))

# ----------------------------------------------------------------------------- 
def joint_positions(global_time):
    """
    Forward kinematics for one frame.
    Returns a list of (x,y) tuples for the 15 point–lights.
    """

    # Normalised phase within the gait cycle (0‥1)
    phase    = (global_time % CYCLE_DUR) / CYCLE_DUR
    phi      = 2.0 * pi * phase

    # Pelvis (body centre) – moves forward with constant velocity and bounces
    pelvis_x = FORWARD_V * global_time
    pelvis_y = 0.0 +  BOUNCE_AMP * np.sin(2*pi*phase*2)   # heavier bounce
    pelvis   = np.array([pelvis_x, pelvis_y])

    # Individual hip joints (left / right)
    l_hip = pelvis + np.array([-PEL VIS_WIDTH/2, 0])
    r_hip = pelvis + np.array([ PELVIS_WIDTH/2, 0])

    # Hip angles (legs move out of phase)
    hip_r =  HIP_AMP * sin(phi)
    hip_l =  HIP_AMP * sin(phi + pi)

    # Knee flexions
    knee_r = (KNEE_AMP * ( sin(phi + pi/2) + 1 ) / 2)
    knee_l = (KNEE_AMP * ( sin(phi + pi/2 + pi) + 1 ) / 2)

    # Right leg
    knee_r_pos = r_hip + np.array(pol2cart(THIGH_LEN, hip_r))
    shank_ang_r = hip_r + (pi - knee_r)        # absolute shank orientation
    ankle_r_pos = knee_r_pos + np.array(pol2cart(SHANK_LEN, shank_ang_r))

    # Left leg
    knee_l_pos = l_hip + np.array(pol2cart(THIGH_LEN, hip_l))
    shank_ang_l = hip_l + (pi - knee_l)
    ankle_l_pos = knee_l_pos + np.array(pol2cart(SHANK_LEN, shank_ang_l))

    # Torso / shoulders / head (slightly pitched forward & drooped head)
    spine_top  = pelvis + np.array([0, -TORSO_LEN*0.5])   # chest / spine marker
    shoulder_c = pelvis + np.array([0, -TORSO_LEN])

    l_shoulder = shoulder_c + np.array([-SHOULDER_WIDTH/2, 0])
    r_shoulder = shoulder_c + np.array([ SH OULDER_WIDTH/2, 0])

    head       = shoulder_c + np.array([0, -HEAD_OFFSET*1.4])  # drooped

    # Arm shoulder angles (opposite legs)
    arm_r =  ARM_AMP * sin(phi + pi)
    arm_l =  ARM_AMP * sin(phi)

    # Elbow flex
    elbow_r = (ELBOW_AMP * ( sin(phi + pi/2 + pi) + 1 ) / 2)
    elbow_l = (ELBOW_AMP * ( sin(phi + pi/2)       + 1 ) / 2)

    # Right arm
    r_elbow_pos = r_shoulder + np.array(pol2cart(UPPER_ARM_LEN, arm_r))
    forearm_ang_r = arm_r + (pi - elbow_r)
    r_wrist_pos = r_elbow_pos + np.array(pol2cart(FOREARM_LEN, forearm_ang_r))

    # Left arm
    l_elbow_pos = l_shoulder + np.array(pol2cart(UPPER_ARM_LEN, arm_l))
    forearm_ang_l = arm_l + (pi - elbow_l)
    l_wrist_pos = l_elbow_pos + np.array(pol2cart(FOREARM_LEN, forearm_ang_l))

    # Order: exactly 15 points
    points = [
        head,            #  1
        l_shoulder,      #  2
        r_shoulder,      #  3
        l_elbow_pos,     #  4
        r_elbow_pos,     #  5
        l_wrist_pos,     #  6
        r_wrist_pos,     #  7
        spine_top,       #  8
        pelvis,          #  9 (pelvis / hip centre)
        l_hip,           # 10
        r_hip,           # 11
        knee_l_pos,      # 12
        knee_r_pos,      # 13
        ankle_l_pos,     # 14
        ankle_r_pos      # 15
    ]

    return points

# ----------------------  VISUALISATION  ------------------------ #
fig, ax = plt.subplots(figsize=(4,7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal', 'box')
ax.axis('off')

# Create scatter plot with 15 points
initial_pts = joint_positions(0.0)
scat = ax.scatter([p[0] for p in initial_pts],
                  [p[1] for p in initial_pts],
                  s=35, c='white')

# Dynamic limits so the runner keeps centred on screen
WINDOW_WIDTH  = 8
WINDOW_HEIGHT = 8

def update(frame):
    t = frame / 60         # 60 fps
    pts = joint_positions(t)

    # Update scatter coordinates
    scat.set_offsets(np.array(pts))

    # Keep camera centred ahead of pelvis
    centre_x = FORWARD_V * t
    ax.set_xlim(centre_x - WINDOW_WIDTH/2,  centre_x + WINDOW_WIDTH/2)
    ax.set_ylim(-4, 4)

    return scat,

# Animation – 600 frames ≈ 10 s
ani = FuncAnimation(fig, update, frames=600, interval=1000/60, blit=True)

plt.show()
