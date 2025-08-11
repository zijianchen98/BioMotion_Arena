
"""
A Python program that displays a point‐light stimulus animation using 15 white points on a black background.
The animation depicts a happy, heavy man jumping upward. The point‐lights represent 15 key body markers,
whose positions smoothly change during the jump to simulate a biomechanically plausible human jump.

The 15 markers are (in order):
  0  Head
  1  Left Shoulder
  2  Right Shoulder
  3  Left Elbow
  4  Right Elbow
  5  Left Hand
  6  Right Hand
  7  Torso (upper center)
  8  Left Hip
  9  Right Hip
 10  Belly (extra marker between torso and hips)
 11  Left Knee
 12  Right Knee
 13  Left Ankle
 14  Right Ankle

The animation is built over a jump cycle with five phases:
  Phase 1 (t from 0.0 to 0.2): Pre-jump crouch (transition from “extended” to “crouched” posture).
  Phase 2 (t from 0.2 to 0.4): Extension phase as the body pushes upward.
  Phase 3 (t from 0.4 to 0.6): Flight phase at jump apex (extended posture).
  Phase 4 (t from 0.6 to 0.8): Landing tone-down as the body recoils into a brief crouch.
  Phase 5 (t from 0.8 to 1.0): Recovery back to the extended posture.

Additionally, a smooth vertical translation is applied to all markers using a parabolic jump offset – 
starting and ending at 0, with a maximum lift at midcycle.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the two key postures as dictionaries.
# Extended (or jump apex) posture – the “normal” upright position.
extended_pose = {
    'head'         : (0.0, 1.7),
    'l_shoulder'   : (-0.25, 1.5),
    'r_shoulder'   : (0.25, 1.5),
    'l_elbow'      : (-0.50, 1.4),
    'r_elbow'      : (0.50, 1.4),
    'l_hand'       : (-0.60, 1.2),
    'r_hand'       : (0.60, 1.2),
    'torso'        : (0.0, 1.3),
    'l_hip'        : (-0.20, 1.0),
    'r_hip'        : (0.20, 1.0),
    'belly'        : (0.0, 1.15),
    'l_knee'      : (-0.20, 0.6),
    'r_knee'      : (0.20, 0.6),
    'l_ankle'     : (-0.20, 0.2),
    'r_ankle'     : (0.20, 0.2)
}

# Crouched posture – a lowered configuration preceding the jump and during landing.
crouched_pose = {
    'head'         : (0.0, 1.6),
    'l_shoulder'   : (-0.25, 1.4),
    'r_shoulder'   : (0.25, 1.4),
    'l_elbow'      : (-0.50, 1.3),
    'r_elbow'      : (0.50, 1.3),
    'l_hand'       : (-0.60, 1.2),
    'r_hand'       : (0.60, 1.2),
    'torso'        : (0.0, 1.1),
    'l_hip'        : (-0.20, 0.9),
    'r_hip'        : (0.20, 0.9),
    'belly'        : (0.0, 1.0),
    'l_knee'      : (-0.20, 0.5),
    'r_knee'      : (0.20, 0.5),
    'l_ankle'     : (-0.20, 0.1),
    'r_ankle'     : (0.20, 0.1)
}

# List of keys in a consistent order.
body_keys = [
    'head', 'l_shoulder', 'r_shoulder', 'l_elbow', 'r_elbow',
    'l_hand', 'r_hand', 'torso', 'l_hip', 'r_hip', 'belly',
    'l_knee', 'r_knee', 'l_ankle', 'r_ankle'
]

def lerp(a, b, t):
    "Linearly interpolate value a to b with factor t (0 <= t <= 1)"
    return a + (b - a) * t

def interpolate_pose(pose_a, pose_b, factor):
    "Interpolate between two poses (dictionaries mapping keys to (x,y) tuples)."
    new_pose = {}
    for key in pose_a:
        x_a, y_a = pose_a[key]
        x_b, y_b = pose_b[key]
        new_pose[key] = (lerp(x_a, x_b, factor), lerp(y_a, y_b, factor))
    return new_pose

def get_limb_pose(phase_time):
    """
    Given a normalized phase_time (0 to 1 for the overall jump cycle),
    return an interpolated pose for limb configuration according to the five phases:
      0.0 - 0.2: Transition from extended to crouched (pre-jump crouch)
      0.2 - 0.4: Transition from crouched back to extended (extension)
      0.4 - 0.6: Extended pose (flight phase)
      0.6 - 0.8: Transition from extended to crouched (landing impact)
      0.8 - 1.0: Transition from crouched to extended (recovery)
    """
    if phase_time < 0.2:
        factor = phase_time / 0.2
        pose = interpolate_pose(extended_pose, crouched_pose, factor)
    elif phase_time < 0.4:
        factor = (phase_time - 0.2) / 0.2
        pose = interpolate_pose(crouched_pose, extended_pose, factor)
    elif phase_time < 0.6:
        pose = extended_pose.copy()
    elif phase_time < 0.8:
        factor = (phase_time - 0.6) / 0.2
        pose = interpolate_pose(extended_pose, crouched_pose, factor)
    else:  # 0.8 to 1.0
        factor = (phase_time - 0.8) / 0.2
        pose = interpolate_pose(crouched_pose, extended_pose, factor)
    return pose

def jump_offset(phase_time, max_lift=0.3):
    """
    Compute vertical offset simulating a jump trajectory.
    A simple parabolic function is used so that offset=0 at t=0 and t=1, 
    with a maximum lift at t=0.5.
    """
    # Parabolic profile: scaled so that the maximum (at 0.5) is max_lift.
    return max_lift * 4 * phase_time * (1 - phase_time)

# Set up the figure and axis.
fig, ax = plt.subplots(figsize=(4,6))
ax.set_facecolor('black')
plt.axis('equal')
plt.axis('off')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2.2)

# Initialize scatter plot for the 15 point lights.
scatter = ax.scatter([], [], s=100, c='white')

# Total frames for the animation.
num_frames = 100

def init():
    scatter.set_offsets([])
    return scatter,

def animate(frame):
    # Normalize frame to phase time [0,1]
    t = frame / (num_frames - 1)
    
    # Get the correct limb pose (body configuration) for this cycle.
    pose = get_limb_pose(t)
    
    # Compute the vertical jump offset (applied to every marker).
    offset = jump_offset(t)
    
    # Compute final positions for each of the 15 markers.
    positions = []
    for key in body_keys:
        x, y = pose[key]
        positions.append((x, y + offset))
        
    scatter.set_offsets(np.array(positions))
    return scatter,

# Create the animation using FuncAnimation.
anim = FuncAnimation(fig, animate, frames=num_frames, init_func=init,
                     interval=30, blit=True, repeat=True)

plt.show()