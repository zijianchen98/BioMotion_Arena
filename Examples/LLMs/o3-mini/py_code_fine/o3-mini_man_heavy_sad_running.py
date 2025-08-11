
"""
This program displays a point‐light animation of a “sadman with heavy weight” running.
It displays exactly 15 white points (representing joints) on a black background.
The 15 points correspond to:
  0: Head
  1: Left Shoulder    2: Right Shoulder
  3: Left Elbow       4: Right Elbow
  5: Left Hand        6: Right Hand
  7: Spine
  8: Pelvis/Center of Mass (COM)
  9: Left Hip         10: Right Hip
  11: Left Knee       12: Right Knee
  13: Left Ankle      14: Right Ankle

The running motion is produced by a smooth sinusoidal modulation of the arms and leg segments,
together with a slight global vertical bob to simulate a heavy–laden gait.
The biomechanical “swing” is computed by rotating the baseline segment vectors about the
proximal joint. (This is a simplified model that nevertheless produces natural‐looking motion.)

Press Ctrl+C or close the window to quit.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Helper function: 2D rotation of a vector by angle theta (in radians)
def rotate(vec, theta):
    rot_mat = np.array([[np.cos(theta), -np.sin(theta)],
                        [np.sin(theta),  np.cos(theta)]])
    return rot_mat @ vec

# Define baseline (standing) skeleton joint positions (in 2D) as a 15x2 numpy array.
# Coordinates are in a local coordinate system.
# We design the skeleton with a slightly stooped posture.
# (x, y) positions for each joint:
# 0: Head, 1: LShoulder, 2: RShoulder, 3: LElbow, 4: RElbow, 
# 5: LHand, 6: RHand, 7: Spine, 8: Pelvis/COM, 9: LHip,
# 10: RHip, 11: LKnee, 12: RKnee, 13: LAnkle, 14: RAnkle

base_joints = np.array([
    [0.0,  8.0],   # 0 Head (high)
    [-1.5, 7.0],   # 1 Left Shoulder
    [ 1.5, 7.0],   # 2 Right Shoulder
    [-2.5, 5.5],   # 3 Left Elbow
    [ 2.5, 5.5],   # 4 Right Elbow
    [-3.0, 4.0],   # 5 Left Hand
    [ 3.0, 4.0],   # 6 Right Hand
    [ 0.0, 6.0],   # 7 Spine (upper trunk)
    [ 0.0, 3.0],   # 8 Pelvis / Center of Mass (COM)
    [-1.0, 3.0],   # 9 Left Hip
    [ 1.0, 3.0],   # 10 Right Hip
    [-1.0, 0.0],   # 11 Left Knee
    [ 1.0, 0.0],   # 12 Right Knee
    [-1.0,-3.0],   # 13 Left Ankle
    [ 1.0,-3.0]    # 14 Right Ankle
])

# Store baseline segment vectors for the limbs.
# Arms: We update joints 3 and 5 relative to joint 1 (left shoulder) and joints 4 and 6 relative to joint 2.
left_upper_arm = base_joints[3] - base_joints[1]  # From left shoulder to left elbow
left_lower_arm = base_joints[5] - base_joints[3]   # From left elbow to left hand

right_upper_arm = base_joints[4] - base_joints[2]  # From right shoulder to right elbow
right_lower_arm = base_joints[6] - base_joints[4]    # From right elbow to right hand

# Legs: update joints 11 and 13 relative to joint 9 (left leg) and similarly for right leg.
left_upper_leg = base_joints[11] - base_joints[9]    # From left hip to left knee
left_lower_leg = base_joints[13] - base_joints[11]     # From left knee to left ankle

right_upper_leg = base_joints[12] - base_joints[10]    # From right hip to right knee
right_lower_leg = base_joints[14] - base_joints[12]    # From right knee to right ankle

# Animation parameters
fps = 30
cycle_period = 1.0   # seconds for one run-cycle
speed = 4.0        # horizontal speed (units per second)
arm_swing_amp = np.deg2rad(30)  # maximum swing angle for arms (radians)
leg_swing_amp = np.deg2rad(30)  # maximum swing angle for legs (radians)
bob_amp = 0.5      # vertical bobbing amplitude

# Set up the figure and axis.
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor('black')
scat = ax.scatter([], [], s=100, c='white')  # white point-lights

# Adjust plot limits; we allow a moving window in x.
ax.set_xlim(-5, 15)
ax.set_ylim(-8, 10)
ax.set_aspect('equal')
ax.axis('off')

def update(frame):
    t = frame / fps

    # Global translation in x.
    x_trans = speed * t
    # Global vertical bobbing (applied uniformly to all joints).
    bob = bob_amp * np.abs(np.sin(2 * np.pi * t))  # using an absolute sine to keep bobbing upward

    # Start with a copy of baseline positions.
    joints = base_joints.copy()

    # Apply arm swinging.
    # For the left arm (indices 1,3,5)
    theta_left_arm = arm_swing_amp * np.sin(2 * np.pi * t)
    # Update left elbow (index 3)
    left_shoulder = joints[1]
    new_left_elbow = left_shoulder + rotate(left_upper_arm, theta_left_arm)
    joints[3] = new_left_elbow
    # Update left hand (index 5)
    new_left_hand = new_left_elbow + rotate(left_lower_arm, theta_left_arm)
    joints[5] = new_left_hand

    # For the right arm (indices 2,4,6)
    theta_right_arm = -arm_swing_amp * np.sin(2 * np.pi * t)
    right_shoulder = joints[2]
    new_right_elbow = right_shoulder + rotate(right_upper_arm, theta_right_arm)
    joints[4] = new_right_elbow
    new_right_hand = new_right_elbow + rotate(right_lower_arm, theta_right_arm)
    joints[6] = new_right_hand

    # Apply leg swinging.
    # For left leg (indices 9,11,13)
    theta_left_leg = leg_swing_amp * np.sin(2 * np.pi * t)
    left_hip = joints[9]
    new_left_knee = left_hip + rotate(left_upper_leg, theta_left_leg)
    joints[11] = new_left_knee
    new_left_ankle = new_left_knee + rotate(left_lower_leg, theta_left_leg)
    joints[13] = new_left_ankle

    # For right leg (indices 10,12,14)
    theta_right_leg = -leg_swing_amp * np.sin(2 * np.pi * t)
    right_hip = joints[10]
    new_right_knee = right_hip + rotate(right_upper_leg, theta_right_leg)
    joints[12] = new_right_knee
    new_right_ankle = new_right_knee + rotate(right_lower_leg, theta_right_leg)
    joints[14] = new_right_ankle

    # Add a subtle forward-backward vertical oscillation for the upper body (head, shoulders, spine),
    # to simulate impact and lift from running.
    upper_body_bob = 0.3 * np.sin(4 * np.pi * t)
    for idx in [0, 1, 2, 3, 4, 5, 6, 7]:
        joints[idx][1] += upper_body_bob

    # Apply global translation and bobbing to all joints.
    joints[:,0] += x_trans
    joints[:,1] += bob

    # Update the scatter plot.
    scat.set_offsets(joints)
    return scat,

ani = FuncAnimation(fig, update, frames=np.arange(0, 300), interval=1000/fps, blit=True)

plt.show()