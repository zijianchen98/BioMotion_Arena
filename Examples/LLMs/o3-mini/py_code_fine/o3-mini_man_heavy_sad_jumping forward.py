
"""
This program creates an animation of a “sadman” with heavy weight (a slumped, heavy‐looking figure)
performing a “jumping forward” action. The stimulus is rendered as 15 white point‐lights against a black
background. The motion is designed to be smooth, coherent and biomechanically plausible though it is a
simplified point‐light approximation.

The 15 points represent:
  0: Head
  1: Left shoulder
  2: Right shoulder
  3: Torso (chest)
  4: Left elbow
  5: Right elbow
  6: Left hand
  7: Right hand
  8: Left hip
  9: Right hip
 10: Left knee
 11: Right knee
 12: Left foot
 13: Right foot
 14: Belly (a “heavy weight” center)

The program uses matplotlib’s animation framework. Run this script to see the animation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Animation parameters
duration = 3.0           # seconds of animation
fps = 30                 # frames per second
num_frames = int(duration * fps)
jump_distance = 1.0      # horizontal displacement (meters)
jump_height = 0.3        # maximum jump height (meters)

# Base configuration of joints (in a resting pose) 
# Coordinates (x,y) in meters. These are defined relative to an initial coordinate system.
base_joints = np.array([
    [ 0.0, 1.8],  # 0: Head
    [-0.2, 1.6],  # 1: Left shoulder
    [ 0.2, 1.6],  # 2: Right shoulder
    [ 0.0, 1.4],  # 3: Torso / Chest
    [-0.5, 1.4],  # 4: Left elbow
    [ 0.5, 1.4],  # 5: Right elbow
    [-0.6, 1.2],  # 6: Left hand
    [ 0.6, 1.2],  # 7: Right hand
    [-0.2, 1.0],  # 8: Left hip
    [ 0.2, 1.0],  # 9: Right hip
    [-0.2, 0.5],  # 10: Left knee
    [ 0.2, 0.5],  # 11: Right knee
    [-0.2, 0.0],  # 12: Left foot
    [ 0.2, 0.0],  # 13: Right foot
    [ 0.0, 1.2]   # 14: Belly (heavy weight center)
])

def get_pose(t):
    """
    Given a normalized time t in [0,1] (progress through the jump),
    return a (15,2) array of joint coordinates for that frame.
    The jump motion: the figure moves forward, following a parabolic arc.
    Additionally, subtle limb adjustments simulate biomechanically plausible
    preparatory crouch and arm/leg swings.
    """
    # Global translation: a jump forward along x and a parabolic jump in y.
    T_x = jump_distance * t
    # Parabolic jump: 4*t*(1-t) is 0 at t=0,1 and 1 at t=0.5.
    T_y = jump_height * 4 * t * (1 - t)
    translation = np.array([T_x, T_y])
    
    # Prepare a copy of base joints to modify for this frame.
    joints = base_joints.copy()
    
    # Use a sine function for smooth cyclic modulations.
    # s goes from 0 at start, 1 at mid-jump, 0 at end.
    s = np.sin(np.pi * t)
    
    # 1. Adjust leg joints (simulate crouch before takeoff and landing)
    # Knees (points 10 and 11) become more bent (lifted upward relative to hips) at the beginning and end.
    knee_bend = 0.1 * (1 - s)  # maximum extra upward displacement when t=0 or t=1, minimal at midjump.
    for idx in [10, 11]:
        joints[idx, 1] += knee_bend  # add vertical offset to knee y
    
    # 2. Adjust hips (points 8 and 9) to tilt slightly forward as the jump is initiated 
    hip_shift = 0.05 * np.sin(np.pi * t)  # small horizontal shift 
    for idx in [8, 9]:
        joints[idx, 0] += hip_shift

    # 3. Arm swing: simulate swinging arms for momentum.
    # Arms swing: left arm goes slightly backward while right arm goes forward, then reverse.
    arm_swing_amp = 0.1 
    # Left hand (6) and left elbow (4)
    delta_left = -arm_swing_amp * np.sin(2 * np.pi * t)
    joints[4, 0] += 0.5 * delta_left  # elbow small swing
    joints[6, 0] += delta_left
    joints[4, 1] += 0.05 * np.sin(2 * np.pi * t)  # subtle vertical component
    joints[6, 1] += 0.05 * np.sin(2 * np.pi * t)
    
    # Right hand (7) and right elbow (5)
    delta_right = arm_swing_amp * np.sin(2 * np.pi * t)
    joints[5, 0] += 0.5 * delta_right
    joints[7, 0] += delta_right
    joints[5, 1] += 0.05 * np.sin(2 * np.pi * t)
    joints[7, 1] += 0.05 * np.sin(2 * np.pi * t)

    # 4. Minor trunk posture change to reflect the "sad" slumped look:
    # The head (point 0) and shoulders (points 1,2) drop slightly as if weighed down.
    slump = 0.05 * (1 - s)  # most slump at takeoff and landing
    joints[0, 1] -= slump
    joints[1, 1] -= slump
    joints[2, 1] -= slump

    # 5. The belly (point 14) representing heavy weight remains near its base position
    # but we can add a slight jitter effect to emphasize the mass.
    belly_jitter = 0.02 * np.cos(2*np.pi * t)
    joints[14, 0] += belly_jitter

    # Now apply the global translation to all joints.
    joints += translation

    return joints

# Set up the figure and axis.
fig, ax = plt.subplots(figsize=(5,5))
ax.set_facecolor('black')
fig.patch.set_facecolor('black')

# Set up scatter plot for the 15 points.
points_scatter = ax.scatter([], [], s=80, c='white')

# Set axis limits (adjust for jump trajectory).
ax.set_xlim(-0.8, jump_distance + 1.0)
ax.set_ylim(-0.2, 2.2)
ax.set_aspect('equal')
ax.axis('off')

def init():
    points_scatter.set_offsets([])
    return points_scatter,

def update(frame):
    t = frame / num_frames  # normalized time in [0,1]
    joints = get_pose(t)
    points_scatter.set_offsets(joints)
    return points_scatter,

# Create the animation.
anim = FuncAnimation(fig, update, frames=num_frames, init_func=init,
                     interval=1000/fps, blit=True)

# To display the animation, use plt.show(). To save it as a video uncomment the saving line below.
if __name__ == '__main__':
    plt.show()
    # Uncomment the following lines to save the animation as an mp4 file:
    # Writer = plt.animation.FFMpegWriter
    # writer = Writer(fps=fps, metadata=dict(artist='Python Animation'), bitrate=1800)
    # anim.save("jumping_sadman.mp4", writer=writer)
