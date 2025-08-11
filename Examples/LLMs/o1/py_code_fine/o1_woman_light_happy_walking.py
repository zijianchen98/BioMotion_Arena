#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
This program visualizes a 2D point-light display of a walking human figure
(“happy woman with light weight” in a walking motion). The stimulus consists
of exactly 15 white point-lights moving against a solid black background,
representing a coherent biological motion. The motion should appear smooth,
realistic, and biomechanically plausible for a simple point-light walker.
"""

# ----------------------------------------------------------------------------
# CONFIGURATION
# ----------------------------------------------------------------------------
FPS = 30             # Frames per second (approx)
CYCLE_FRAMES = 60    # Number of frames per walking cycle
TOTAL_FRAMES = 600   # Total frames to animate before repeating
POINT_SIZE = 50      # Size of the point markers

# Body segment lengths (approximate proportions)
HEAD_OFFSET = 0.15       # Distance from "neck" (top of trunk) to head marker
TRUNK_LENGTH = 0.6       # Distance between "pelvis center" and "neck" (top of trunk)
ARM_UPPER_LEN = 0.25     # Upper arm length
ARM_LOWER_LEN = 0.25     # Lower arm length
LEG_UPPER_LEN = 0.4      # Thigh length
LEG_LOWER_LEN = 0.4      # Shin (lower leg) length
SHOULDER_OFFSET = 0.15   # Horizontal offset from trunk midline to shoulders
HIP_OFFSET = 0.15        # Horizontal offset from trunk midline to hips

# Amplitudes for joint oscillations
ARM_SWING_AMP = np.radians(35)   # Max angle for shoulder swing
ELBOW_SWING_AMP = np.radians(20) # Max angle for elbow relative motion
HIP_SWING_AMP = np.radians(30)   # Max angle for hip swing
KNEE_SWING_AMP = np.radians(40)  # Max angle for knee relative motion
TRUNK_BOB_AMP = 0.05             # Vertical bob of the trunk during walking

# ----------------------------------------------------------------------------
# HELPER FUNCTIONS
# ----------------------------------------------------------------------------
def rotate_point(origin, angle, length):
    """
    Given an origin (x, y), an angle in radians, and a length,
    returns the (x, y) coordinates of the end of a segment.
    """
    ox, oy = origin
    x = ox + length * np.cos(angle)
    y = oy + length * np.sin(angle)
    return x, y

def get_biological_motion_points(frame):
    """
    Compute the 2D positions of 15 markers representing
    a point-light walker at a given frame.
    
    Returns a 2D NumPy array of shape (15, 2):
    [
      [head_x, head_y],
      [neck_x, neck_y],
      [left_shoulder_x, left_shoulder_y],
      [left_elbow_x, left_elbow_y],
      [left_wrist_x, left_wrist_y],
      [right_shoulder_x, right_shoulder_y],
      [right_elbow_x, right_elbow_y],
      [right_wrist_x, right_wrist_y],
      [left_hip_x, left_hip_y],
      [left_knee_x, left_knee_y],
      [left_ankle_x, left_ankle_y],
      [right_hip_x, right_hip_y],
      [right_knee_x, right_knee_y],
      [right_ankle_x, right_ankle_y],
      [pelvis_center_x, pelvis_center_y]
    ]
    """
    # Normalize time t in [0, 1) for a single cycle
    t = (frame % CYCLE_FRAMES) / CYCLE_FRAMES
    # Walking uses two steps per cycle, so angle base is 2*pi:
    # We'll parametrize angles with 2*pi*t
    base_angle = 2 * np.pi * t
    
    # Slight vertical "bobbing" of the trunk
    trunk_y_offset = TRUNK_BOB_AMP * np.cos(2 * base_angle)

    # Pelvis center (the bottom of the trunk) in the middle
    pelvis_center = np.array([0.0, 0.0 + trunk_y_offset])
    
    # Neck (top of trunk)
    neck = pelvis_center + np.array([0.0, TRUNK_LENGTH])

    # Head
    head = neck + np.array([0.0, HEAD_OFFSET])
    
    # Shoulders
    left_shoulder  = neck + np.array([-SHOULDER_OFFSET,  0.0])
    right_shoulder = neck + np.array([+SHOULDER_OFFSET,  0.0])
    
    # Hips
    left_hip  = pelvis_center + np.array([-HIP_OFFSET, 0.0])
    right_hip = pelvis_center + np.array([+HIP_OFFSET, 0.0])
    
    # Define angles for arms and legs (a simple sinusoidal model)
    # Arms usually swing opposite to legs:
    #   left arm in phase with right leg, right arm in phase with left leg.
    
    # Shoulder angles
    #   left arm:  negative half-cycle of base_angle => sin(base_angle + pi)
    #   right arm: sin(base_angle)
    left_shoulder_angle  = -ARM_SWING_AMP * np.sin(base_angle)
    right_shoulder_angle = +ARM_SWING_AMP * np.sin(base_angle)
    
    # Elbows: smaller amplitude and offset
    # We'll just pivot them based on the shoulder's motion
    left_elbow_angle  = left_shoulder_angle + (-ELBOW_SWING_AMP * np.sin(base_angle + np.pi / 2))
    right_elbow_angle = right_shoulder_angle + (+ELBOW_SWING_AMP * np.sin(base_angle + np.pi / 2))
    
    # Hips
    left_hip_angle  = +HIP_SWING_AMP * np.sin(base_angle)
    right_hip_angle = -HIP_SWING_AMP * np.sin(base_angle)
    
    # Knees
    left_knee_angle  = left_hip_angle + (+KNEE_SWING_AMP * np.sin(base_angle + np.pi / 2))
    right_knee_angle = right_hip_angle + (-KNEE_SWING_AMP * np.sin(base_angle + np.pi / 2))
    
    # Compute left arm segment endpoints: elbow, wrist
    left_elbow = rotate_point(left_shoulder,  np.pi/2 + left_shoulder_angle, ARM_UPPER_LEN)
    left_wrist = rotate_point(left_elbow,     np.pi/2 + left_elbow_angle,    ARM_LOWER_LEN)
    
    # Compute right arm segment endpoints: elbow, wrist
    right_elbow = rotate_point(right_shoulder, np.pi/2 + right_shoulder_angle, ARM_UPPER_LEN)
    right_wrist = rotate_point(right_elbow,    np.pi/2 + right_elbow_angle,    ARM_LOWER_LEN)
    
    # Compute left leg segment endpoints: knee, ankle
    left_knee = rotate_point(left_hip,  -np.pi/2 + left_hip_angle,  LEG_UPPER_LEN)
    left_ankle = rotate_point(left_knee, -np.pi/2 + left_knee_angle, LEG_LOWER_LEN)
    
    # Compute right leg segment endpoints: knee, ankle
    right_knee = rotate_point(right_hip,  -np.pi/2 + right_hip_angle,  LEG_UPPER_LEN)
    right_ankle = rotate_point(right_knee, -np.pi/2 + right_knee_angle, LEG_LOWER_LEN)
    
    # Assemble the 15 points in order
    points = np.array([
        [head[0],           head[1]],            # 1  Head
        [neck[0],           neck[1]],            # 2  Neck (top of trunk)
        [left_shoulder[0],  left_shoulder[1]],   # 3  Left shoulder
        [left_elbow[0],     left_elbow[1]],      # 4  Left elbow
        [left_wrist[0],     left_wrist[1]],      # 5  Left wrist
        [right_shoulder[0], right_shoulder[1]],  # 6  Right shoulder
        [right_elbow[0],    right_elbow[1]],     # 7  Right elbow
        [right_wrist[0],    right_wrist[1]],     # 8  Right wrist
        [left_hip[0],       left_hip[1]],        # 9  Left hip
        [left_knee[0],      left_knee[1]],       # 10 Left knee
        [left_ankle[0],     left_ankle[1]],      # 11 Left ankle
        [right_hip[0],      right_hip[1]],       # 12 Right hip
        [right_knee[0],     right_knee[1]],      # 13 Right knee
        [right_ankle[0],    right_ankle[1]],     # 14 Right ankle
        [pelvis_center[0],  pelvis_center[1]]    # 15 Pelvis center (bottom of trunk)
    ])
    return points

# ----------------------------------------------------------------------------
# ANIMATION
# ----------------------------------------------------------------------------
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')  # Black background
ax.set_facecolor('black')         # Black background in plot area
ax.set_aspect('equal', 'box')

# Create initial scatter for 15 points (white)
scatter = ax.scatter(np.zeros(15), np.zeros(15), s=POINT_SIZE, c='white')

# Adjust the view range so the walker is nicely visible
ax.set_xlim(-1, 1)
ax.set_ylim(-0.2, 1.5)
plt.axis('off')  # Turn off axis lines and labels

def update(frame):
    # Compute point coordinates
    coords = get_biological_motion_points(frame)
    scatter.set_offsets(coords)
    return (scatter,)

anim = FuncAnimation(
    fig, 
    update, 
    frames=TOTAL_FRAMES, 
    interval=1000 / FPS, 
    blit=True, 
    repeat=True
)

# ----------------------------------------------------------------------------
# Run the animation
# ----------------------------------------------------------------------------
plt.show()