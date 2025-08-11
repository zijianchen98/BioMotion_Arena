#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
This program displays a 15-point biological motion stimulus of a walking "happy woman 
with heavy weight." The points are shown in white against a black background. 
The motion is generated via simple parametric approximations to achieve a smooth, 
biomechanically plausible walk cycle.
"""

# Set global parameters for the walking motion
FPS = 30           # frames per second
DURATION = 5       # total duration (seconds)
FRAMES = FPS * DURATION
STRIDE_ANGLE = 0.8 # peak swing angle for legs
ARM_SWING = 0.5    # peak swing angle for arms
HIP_WIDTH = 0.30   # distance between left and right hip
SHOULDER_WIDTH = 0.35
TORSO_LENGTH = 0.35
ARM_LENGTH_UPPER = 0.30
ARM_LENGTH_LOWER = 0.25
LEG_LENGTH_UPPER = 0.35
LEG_LENGTH_LOWER = 0.35
PELVIS_BOB = 0.05  # vertical amplitude of pelvis bounce
BODY_OFFSET = 0.10 # vertical offset from pelvis to chest

# We will produce exactly 15 points:
# 0 Head
# 1 Chest
# 2 Pelvis
# 3 LShoulder
# 4 LElbow
# 5 LWrist
# 6 RShoulder
# 7 RElbow
# 8 RWrist
# 9 LHip
# 10 LKnee
# 11 LAnkle
# 12 RHip
# 13 RKnee
# 14 RAnkle

def get_biomotion_points(frame):
    """
    Returns a (15, 2) array of x,y positions for each of the 15 point-lights
    at a given frame. The motion is parametric and repeats every 1 second (FPS frames).
    """
    # Convert frame to time in seconds, cycle repeats every 1 second
    t = frame / FPS
    # Basic walking frequency of 1 cycle per second (2π per second)
    phase = 2.0 * np.pi * t
    
    # Pelvis bounce (simulating heavier body with noticeable vertical displacement)
    pelvis_y = PELVIS_BOB * np.sin(phase * 2.0)
    
    # Pelvis is centered in x = 0, with small vertical bounce
    pelvis_pos = np.array([0.0, pelvis_y])
    
    # Chest is above the pelvis
    chest_pos = pelvis_pos + np.array([0.0, BODY_OFFSET + TORSO_LENGTH/2])
    
    # Shoulders (left and right) around the chest
    l_shoulder_pos = chest_pos + np.array([-SHOULDER_WIDTH/2, 0.0])
    r_shoulder_pos = chest_pos + np.array([ SHOULDER_WIDTH/2, 0.0])
    
    # Hips (left and right) around the pelvis
    l_hip_pos = pelvis_pos + np.array([-HIP_WIDTH/2, -0.00])
    r_hip_pos = pelvis_pos + np.array([ HIP_WIDTH/2, -0.00])
    
    # Leg angles: out of phase for left and right
    # The sign of the sine terms are chosen so at t=0, left leg is forward, right leg is back
    left_leg_angle  =  STRIDE_ANGLE * np.sin(phase)
    right_leg_angle =  STRIDE_ANGLE * np.sin(phase + np.pi)
    
    # Arm angles: similar pattern but smaller amplitude and opposite phase to the corresponding leg
    left_arm_angle  =  ARM_SWING * np.sin(phase + np.pi)
    right_arm_angle =  ARM_SWING * np.sin(phase)
    
    # Compute knees from hips
    # We'll assume the knee is at some angle that tracks half of the hip angle in a simplified approach
    l_knee_angle = left_leg_angle / 2.0
    r_knee_angle = right_leg_angle / 2.0
    
    # Positions for the knees using basic forward kinematics
    l_knee_pos = l_hip_pos + rotate2d(np.array([0, -LEG_LENGTH_UPPER]), left_leg_angle)
    r_knee_pos = r_hip_pos + rotate2d(np.array([0, -LEG_LENGTH_UPPER]), right_leg_angle)
    
    # Compute ankles from knees
    # We'll similarly assume the ankle displaces by the remainder of the leg
    l_ankle_pos = l_knee_pos + rotate2d(np.array([0, -LEG_LENGTH_LOWER]), l_knee_angle)
    r_ankle_pos = r_knee_pos + rotate2d(np.array([0, -LEG_LENGTH_LOWER]), r_knee_angle)
    
    # Elbows from shoulders
    l_elbow_pos = l_shoulder_pos + rotate2d(np.array([0, -ARM_LENGTH_UPPER]), left_arm_angle)
    r_elbow_pos = r_shoulder_pos + rotate2d(np.array([0, -ARM_LENGTH_UPPER]), right_arm_angle)
    
    # Wrists from elbows
    # We'll assume a similar half-angle approach for bending at the elbow
    l_wrist_angle = left_arm_angle / 2.0
    r_wrist_angle = right_arm_angle / 2.0
    l_wrist_pos = l_elbow_pos + rotate2d(np.array([0, -ARM_LENGTH_LOWER]), l_wrist_angle)
    r_wrist_pos = r_elbow_pos + rotate2d(np.array([0, -ARM_LENGTH_LOWER]), r_wrist_angle)
    
    # Head (slightly above the chest)
    head_pos = chest_pos + np.array([0, 0.15])
    
    # Combine all 15 points in the specified order
    points = np.zeros((15, 2))
    points[0]  = head_pos
    points[1]  = chest_pos
    points[2]  = pelvis_pos
    points[3]  = l_shoulder_pos
    points[4]  = l_elbow_pos
    points[5]  = l_wrist_pos
    points[6]  = r_shoulder_pos
    points[7]  = r_elbow_pos
    points[8]  = r_wrist_pos
    points[9]  = l_hip_pos
    points[10] = l_knee_pos
    points[11] = l_ankle_pos
    points[12] = r_hip_pos
    points[13] = r_knee_pos
    points[14] = r_ankle_pos
    
    return points

def rotate2d(vec, angle):
    """
    Rotate a 2D vector `vec` around the origin by `angle` (in radians).
    Returns a new rotated vector.
    """
    c, s = np.cos(angle), np.sin(angle)
    x, y = vec
    return np.array([c*x - s*y, s*x + c*y])

# Set up the figure and axis with black background
fig, ax = plt.subplots(figsize=(5, 5))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.8, 0.8)
ax.set_ylim(-1.0, 1.0)
ax.set_aspect('equal', 'box')
ax.axis('off')  # Hide axis lines/ticks for a clean look

# Create a scatter plot for the 15 points (white on black).
scatter = ax.scatter([], [], c='white', s=50)

def init():
    # Initialize scatter object; no data
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    # Update point positions
    pts = get_biomotion_points(frame)
    scatter.set_offsets(pts)
    return (scatter,)

ani = FuncAnimation(
    fig, update, frames=FRAMES, init_func=init, interval=1000/FPS, blit=True
)

plt.show()