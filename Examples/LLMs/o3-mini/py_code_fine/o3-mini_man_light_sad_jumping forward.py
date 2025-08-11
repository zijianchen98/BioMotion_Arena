
"""
This program creates an animation of a point‐light “sadman” (with a light body)
performing a realistic jumping‐forward movement. Exactly 15 white points are used,
which correspond to the following joints (in order):
  
  0. Head
  1. Neck
  2. Left Shoulder
  3. Right Shoulder
  4. Left Elbow
  5. Right Elbow
  6. Left Hand
  7. Right Hand
  8. Torso
  9. Left Hip
 10. Right Hip
 11. Left Knee
 12. Right Knee
 13. Left Foot
 14. Right Foot

The animation is drawn on a black background and uses biomechanically plausible
motion cues: the figure crouches before takeoff (and on landing) and extends its
limbs during flight. The arms also perform a subtle swing.
  
Run this program with Python3.
  
Dependencies: numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Helper: rotation function for 2D vector
def rotate(vec, theta):
    # vec: (x, y) numpy array
    # theta: angle in radians
    rot = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta),  np.cos(theta)]])
    return np.dot(rot, vec)

# Animation parameters
T = 100                 # total number of frames
total_time = 2.0        # seconds
fps = T / total_time    # frames per second

# Movement parameters
total_forward = 1.0     # total x displacement during jump
jump_height = 0.5       # maximum vertical jump (added as offset to entire skeleton)

# Leg crouch factor parameters:
# We'll modify the effective limb length from hip to knee and foot.
# When crouched, factor will be 0.5 (shorter effective length) and when extended factor=1.
def leg_factor(frame):
    # piecewise linear: first quarter: from 0.5 to 1, middle: 1, last quarter: from 1 to 0.5
    if frame < T/4:
        return 0.5 + 0.5*(frame/(T/4))
    elif frame > 3*T/4:
        return 1.0 - 0.5*((frame - 3*T/4)/(T/4))
    else:
        return 1.0

# Arm swing: let the arms swing with a small sinusoidal motion.
def arm_swing_angle(frame):
    # amplitude ~15 degrees (in radians ~0.26), modulated over the jump cycle.
    return 0.26 * np.sin(2*np.pi * frame/T)

# Base skeleton configuration (all positions relative to the torso origin at (0,0))
# Coordinates for static joints (if not modulated) in a neutral pose.
base = {}

# Torso center is at (0,0)
base["torso"] = np.array([0.0, 0.0])
# Neck (slightly above torso)
base["neck"] = np.array([0.0, 0.2])
# Head above neck
base["head"] = np.array([0.0, 0.4])
# Shoulders: left and right (relative to neck)
base["left_shoulder"] = np.array([-0.1, 0.2])
base["right_shoulder"] = np.array([0.1, 0.2])
# Hips: relative to torso
base["left_hip"] = np.array([-0.1, -0.2])
base["right_hip"] = np.array([0.1, -0.2])

# For the arms we use dynamic computation.
# We'll define base vectors (from shoulder to elbow and from elbow to hand).
left_elbow_offset = np.array([-0.1, -0.1])
left_hand_offset  = np.array([-0.1, -0.1])
right_elbow_offset = np.array([0.1, -0.1])
right_hand_offset  = np.array([0.1, -0.1])

# For the legs, the base differences (when limbs are fully extended):
# For left leg, knee and foot relative to left hip.
left_knee_diff = np.array([0.0, -0.2])
left_foot_diff = np.array([0.0, -0.4])
# For right leg:
right_knee_diff = np.array([0.0, -0.2])
right_foot_diff = np.array([0.0, -0.4])

# We will update 15 joints per frame in the following order:
# 0: Head
# 1: Neck
# 2: Left Shoulder
# 3: Right Shoulder
# 4: Left Elbow
# 5: Right Elbow
# 6: Left Hand
# 7: Right Hand
# 8: Torso
# 9: Left Hip
# 10: Right Hip
# 11: Left Knee
# 12: Right Knee
# 13: Left Foot
# 14: Right Foot

def compute_joint_positions(frame):
    # Compute overall translation from jump
    t_norm = frame / (T - 1)
    x_offset = total_forward * t_norm
    # Jump trajectory: a smooth parabolic jump (using sine shape)
    y_offset = jump_height * np.sin(np.pi * t_norm)
    
    translation = np.array([x_offset, y_offset])
    
    # Compute leg flexion factor for the current frame.
    lf = leg_factor(frame)
    
    joints = [None]*15
    
    # Torso and constrained parts that use base positions (translated)
    torso = base["torso"] + translation
    neck  = base["neck"]  + translation
    head  = base["head"]  + translation
    
    # Shoulders
    left_shoulder  = base["left_shoulder"] + translation
    right_shoulder = base["right_shoulder"] + translation
    
    # Hips
    left_hip  = base["left_hip"] + translation
    right_hip = base["right_hip"] + translation
    
    # Arms: compute dynamic swing.
    theta = arm_swing_angle(frame)
    # Left arm:
    left_elbow = left_shoulder + rotate(left_elbow_offset, theta)
    left_hand  = left_elbow   + rotate(left_hand_offset, theta)
    # Right arm (swing in opposite direction):
    right_elbow = right_shoulder + rotate(right_elbow_offset, -theta)
    right_hand  = right_elbow    + rotate(right_hand_offset, -theta)
    
    # Legs: modify knee and foot positions by leg flexion factor.
    left_knee = left_hip + left_knee_diff * lf
    left_foot = left_hip + left_foot_diff * lf
    right_knee = right_hip + right_knee_diff * lf
    right_foot = right_hip + right_foot_diff * lf
    
    # Assemble the joint list in the specified order:
    joints[0]  = head
    joints[1]  = neck
    joints[2]  = left_shoulder
    joints[3]  = right_shoulder
    joints[4]  = left_elbow
    joints[5]  = right_elbow
    joints[6]  = left_hand
    joints[7]  = right_hand
    joints[8]  = torso
    joints[9]  = left_hip
    joints[10] = right_hip
    joints[11] = left_knee
    joints[12] = right_knee
    joints[13] = left_foot
    joints[14] = right_foot
    
    return joints

# Set up the plot
fig, ax = plt.subplots(figsize=(6,6))
ax.set_facecolor('black')
plt.axis('equal')
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-1.0, 1.5)
plt.xticks([]), plt.yticks([])
plt.title("Point-light Jumping Animation", color='white')

# Create scatter plot for the 15 points
scat = ax.scatter([], [], c='white', s=80)

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    joints = compute_joint_positions(frame)
    # joints is a list of numpy arrays; convert to 2D array for scatter
    data = np.array(joints)
    scat.set_offsets(data)
    return scat,

anim = FuncAnimation(fig, update, frames=range(T), init_func=init,
                     interval=1000/fps, blit=True)

plt.show()