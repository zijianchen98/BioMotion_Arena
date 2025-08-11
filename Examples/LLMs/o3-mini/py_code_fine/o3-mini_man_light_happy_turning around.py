
"""
This Python program uses matplotlib’s animation framework to display an animation of a point‐light biological motion
stimulus. The stimulus depicts a “happyman with light weight” turning around – the figure is rendered using exactly 
15 white point lights on a solid black background. The motion is produced by smoothly rotating the figure while 
adding subtle sinusoidal oscillations to the arms and legs that simulate natural limb-swinging.
 
The 15 points (joints) are:
  0: Head
  1: Neck
  2: Left Shoulder
  3: Right Shoulder
  4: Left Elbow
  5: Right Elbow
  6: Left Wrist
  7: Right Wrist
  8: Spine (center)
  9: Left Hip
 10: Right Hip
 11: Left Knee
 12: Right Knee
 13: Left Ankle
 14: Right Ankle

Run this script to see the animation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define base coordinates for the 15 joints in the figure's local coordinate frame.
# Vertical direction = y, horizontal = x. Units are arbitrary.
base_points = np.array([
    [0.0, 0.4],    # 0: Head
    [0.0, 0.2],    # 1: Neck
    [-0.1, 0.18],  # 2: Left Shoulder
    [0.1, 0.18],   # 3: Right Shoulder
    [-0.25, 0.1],  # 4: Left Elbow
    [0.25, 0.1],   # 5: Right Elbow
    [-0.35, 0.0],  # 6: Left Wrist
    [0.35, 0.0],   # 7: Right Wrist
    [0.0, 0.0],    # 8: Spine (center)
    [-0.08, -0.2], # 9: Left Hip
    [0.08, -0.2],  #10: Right Hip
    [-0.08, -0.5], #11: Left Knee
    [0.08, -0.5],  #12: Right Knee
    [-0.08, -0.8], #13: Left Ankle
    [0.08, -0.8]   #14: Right Ankle
])

# Limb indices to which we will add small oscillatory motions.
# For arms (elbows and wrists) and legs (knees and ankles).
left_arm_indices = [4, 6]    # left elbow (4) and left wrist (6)
right_arm_indices = [5, 7]   # right elbow (5) and right wrist (7)
left_leg_indices = [11, 13]  # left knee (11) and left ankle (13)
right_leg_indices = [12, 14] # right knee (12) and right ankle (14)

# Animation parameters
frames_per_second = 30
animation_duration = 10  # seconds
num_frames = frames_per_second * animation_duration

# Rotation parameters: full 360 degree turn in 5 seconds.
rotation_period = 5.0  # seconds per full turn
omega = 2 * np.pi / rotation_period  # angular speed (radians per second)

# Limb oscillation (swing) parameters
arm_swing_amplitude = 0.05
leg_swing_amplitude = 0.05
arm_swing_frequency = 2.0  # Hz: how many cycles per second
leg_swing_frequency = 2.0  # Hz

# Phases: opposing arms and legs swing in opposite phases.
# left arm phase 0, right arm phase pi. For the legs, we do the opposite.
left_arm_phase = 0
right_arm_phase = np.pi
left_leg_phase = np.pi
right_leg_phase = 0

def rotate_points(points, theta):
    """
    Rotate the given points (Nx2) by angle theta (radians) around the origin.
    """
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s],
                  [s,  c]])
    return points.dot(R.T)

def get_frame_points(t):
    """
    For a given time t (seconds), compute the current 2D coordinates of all 15 points,
    including limb oscillations and rotation.
    """
    # Start with a copy of the base pose
    points = base_points.copy()
    
    # Compute the oscillatory offsets in the body's (local) frame.
    arm_offset = arm_swing_amplitude * np.sin(2 * np.pi * arm_swing_frequency * t + left_arm_phase)
    # For right arm, use opposite phase:
    right_arm_offset = arm_swing_amplitude * np.sin(2 * np.pi * arm_swing_frequency * t + right_arm_phase)
    
    leg_offset = leg_swing_amplitude * np.sin(2 * np.pi * leg_swing_frequency * t + left_leg_phase)
    right_leg_offset = leg_swing_amplitude * np.sin(2 * np.pi * leg_swing_frequency * t + right_leg_phase)
    
    # Adjust left arm joints (vertical shift in local coordinates)
    for idx in left_arm_indices:
        # Raise the joint slightly during swing
        points[idx, 1] += arm_offset
    # Adjust right arm joints with opposite direction
    for idx in right_arm_indices:
        points[idx, 1] += right_arm_offset

    # Adjust left leg joints (vertical displacement)
    for idx in left_leg_indices:
        points[idx, 1] += leg_offset
    # Adjust right leg joints
    for idx in right_leg_indices:
        points[idx, 1] += right_leg_offset

    # Compute rotation angle based on time.
    theta = omega * t
    # We want to simulate turning in place. The rotation is about the center of the body (spine, index 8).
    spine = points[8].copy()  # center of rotation
    # Subtract spine to put the origin at the center, rotate, then add spine back.
    points_centered = points - spine
    rotated_points = rotate_points(points_centered, theta)
    points_final = rotated_points + spine

    return points_final

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-1, 1)
ax.set_ylim(-1.0, 0.6)
ax.axis('off')

# Initialize scatter (15 white points)
scatter = ax.scatter([], [], s=100, color='white')

def init():
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    t = frame / frames_per_second
    pts = get_frame_points(t)
    scatter.set_offsets(pts)
    return (scatter,)

anim = FuncAnimation(fig, update, frames=num_frames, init_func=init,
                     interval=1000/frames_per_second, blit=True)

plt.show()