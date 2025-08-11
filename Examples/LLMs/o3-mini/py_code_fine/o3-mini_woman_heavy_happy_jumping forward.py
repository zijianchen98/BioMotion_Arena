
"""
This program animates a point‐light display of a “happy, heavy” woman performing a forward jump.
Fifteen white point‐lights represent key joints:
  •  0: Head
  •  1: Neck
  •  2: Left Shoulder
  •  3: Right Shoulder
  •  4: Left Elbow
  •  5: Right Elbow
  •  6: Left Wrist
  •  7: Right Wrist
  •  8: Torso (center)
  •  9: Left Hip
  • 10: Right Hip
  • 11: Left Knee
  • 12: Right Knee
  • 13: Left Ankle
  • 14: Right Ankle

The animation uses a black background and white markers.
The movement is generated with a smooth “jump‐arc” for the center‐of‐mass plus simple,
sine‐modulated motions for the arms (swinging) and legs (bending and extending) to create a plausible
biomechanical forward jump.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Total animation duration (seconds) and number of frames
duration = 1.0
n_frames = 100
ts = np.linspace(0, duration, n_frames)

# Parameters for jump trajectory (center-of-mass of the torso)
L = 0.5              # total horizontal displacement (meters)
H = 0.25             # maximum jump height (meters)
def center_of_mass(t):
    # Use a smooth parabolic arc: start and end at y=0, maximum at t=duration/2.
    x = L * (t/duration)
    # Parabolic function: scaled so that max y=H at t=duration/2.
    y = 4 * H * (t/duration) * (1 - t/duration)
    return np.array([x, y])

# The following functions compute the local (relative) positions of each joint
# given the phase parameter t (0<=t<=duration) for swing and bending.

def get_joint_positions(t):
    # t is the time in seconds, but we use the normalized phase phi = t/duration.
    phi = t/duration

    # 1. Define the center-of-mass: the torso center will follow the jump trajectory.
    torso = center_of_mass(t)  # This will be our base reference (joint 8)

    # 2. Body segment lengths (in meters)
    head_length = 0.12     # from neck to head top
    neck_length = 0.05     # neck segment
    shoulder_offset = 0.12 # horizontal offset from neck to shoulder
    upper_arm = 0.25
    lower_arm = 0.25
    torso_length = 0.15    # from neck to torso center (downwards)
    hip_offset = 0.10      # horizontal offset from torso to hip
    upper_leg = 0.30
    lower_leg = 0.30

    # 3. Arm swing: let the arms swing forward/backward (in sagittal plane)
    # Use a sine function so arms start by hanging naturally,
    # swing forward at take-off, and then return for landing.
    # The swing angle (in radians) is small.
    arm_swing = 0.3 * math.sin(math.pi * phi)  # positive = forward (x)

    # 4. Leg bending: Let the knees flex in the mid-phase.
    # When phi=0 or 1 (start and landing) legs are fully extended.
    # At phi=0.5, they are maximally bent.
    knee_bend = 0.785 * math.sin(math.pi * phi)  # maximum about 45° bend (0.785 rad)

    # 5. Compute positions of each of the 15 joints.
    joints = [None]*15

    # Joint 8: Torso center (the center-of-mass)
    joints[8] = torso

    # Joint 1: Neck: positioned above torso center by torso_length.
    neck = torso + np.array([0, torso_length])
    joints[1] = neck

    # Joint 0: Head: above neck.
    head = neck + np.array([0, head_length])
    joints[0] = head

    # Shoulders (joints 2 and 3) relative to neck.
    left_shoulder = neck + np.array([-shoulder_offset, 0])
    right_shoulder = neck + np.array([shoulder_offset, 0])
    joints[2] = left_shoulder
    joints[3] = right_shoulder

    # Arms: compute elbows and wrists.
    # For the left arm:
    # The upper arm rotates by arm_swing around the shoulder.
    left_elbow = left_shoulder + np.array([upper_arm * math.cos(arm_swing),
                                             -upper_arm * math.sin(arm_swing)])
    left_wrist = left_elbow + np.array([lower_arm * math.cos(arm_swing),
                                         -lower_arm * math.sin(arm_swing)])
    joints[4] = left_elbow
    joints[6] = left_wrist

    # For the right arm:
    right_elbow = right_shoulder + np.array([upper_arm * math.cos(arm_swing),
                                               -upper_arm * math.sin(arm_swing)])
    right_wrist = right_elbow + np.array([lower_arm * math.cos(arm_swing),
                                           -lower_arm * math.sin(arm_swing)])
    joints[5] = right_elbow
    joints[7] = right_wrist

    # Hips (joints 9 and 10) relative to torso.
    left_hip = torso + np.array([-hip_offset, -torso_length])
    right_hip = torso + np.array([hip_offset, -torso_length])
    joints[9] = left_hip
    joints[10] = right_hip

    # Legs: For each leg, the thigh (upper leg) and shank (lower leg) segments are affected by knee bending.
    # We assume that the knee flexes by bending forward (in positive x direction).
    # Left leg:
    left_knee = left_hip + np.array([upper_leg * math.sin(knee_bend),
                                      -upper_leg * math.cos(knee_bend)])
    left_ankle = left_knee + np.array([lower_leg * math.sin(knee_bend),
                                        -lower_leg * math.cos(knee_bend)])
    joints[11] = left_knee
    joints[13] = left_ankle

    # Right leg:
    right_knee = right_hip + np.array([upper_leg * math.sin(knee_bend),
                                        -upper_leg * math.cos(knee_bend)])
    right_ankle = right_knee + np.array([lower_leg * math.sin(knee_bend),
                                          -lower_leg * math.cos(knee_bend)])
    joints[12] = right_knee
    joints[14] = right_ankle

    # Return as an array of shape (15,2)
    return np.array(joints)

# Set up the matplotlib figure and axis.
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_facecolor('black')
plt.style.use('dark_background')
ax.set_xlim(-0.2, L+0.8)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
plt.axis('off')

# Create an empty scatter plot for the 15 points.
scat = ax.scatter([], [], s=80, c='white')

def init():
    scat.set_offsets([])
    return scat,

def animate(i):
    t = ts[i]
    joints = get_joint_positions(t)
    # Update scatter plot data
    scat.set_offsets(joints)
    return scat,

anim = FuncAnimation(fig, animate, frames=n_frames, init_func=init,
                     interval=20, blit=True)

plt.show()