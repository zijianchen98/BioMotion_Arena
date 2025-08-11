
"""
This program displays an animation of a “jump‐forward” performed by a stick‐figure
represented by 15 point‐lights on a black background. Each point represents a key‐joint
of the body. The animation uses biomechanically plausible motion – a parabolic forward
jump combined with a time‐varying body rotation and subtle arm/leg oscillations.
 
The 15 markers (white point-lights) are:
  head, left_shoulder, right_shoulder, left_elbow, right_elbow,
  left_wrist, right_wrist, spine, pelvis, left_knee, right_knee,
  left_ankle, right_ankle, left_foot, right_foot.
  
The overall motion:
  • The pelvis follows a parabolic trajectory (starting at (0,0), peaking at a height of ~1 
    at mid-jump and landing at (2,0)).
  • The body rotates slightly during the jump (tilting backward at take-off, upright at mid‐jump 
    and leaning forward at landing).
  • The arms and knees are given a small oscillatory motion that mimics natural limb flexing.
  
Press Ctrl+C or close the window to exit.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Base positions for each marker relative to the pelvis (origin).
# These positions are chosen to approximate a standing human configuration.
markers = {
    'head':           np.array([0.0, 0.5]),
    'left_shoulder':  np.array([-0.1, 0.2]),
    'right_shoulder': np.array([0.1, 0.2]),
    'left_elbow':     np.array([-0.2, 0.1]),
    'right_elbow':    np.array([0.2, 0.1]),
    'left_wrist':     np.array([-0.3, 0.0]),
    'right_wrist':    np.array([0.3, 0.0]),
    'spine':          np.array([0.0, 0.2]),
    'pelvis':         np.array([0.0, 0.0]),
    'left_knee':      np.array([-0.1, -0.4]),
    'right_knee':     np.array([0.1, -0.4]),
    'left_ankle':     np.array([-0.1, -0.8]),
    'right_ankle':    np.array([0.1, -0.8]),
    'left_foot':      np.array([-0.1, -0.9]),
    'right_foot':     np.array([0.1, -0.9])
}

# Order in which points will be plotted
marker_names = ['head', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
                'left_wrist', 'right_wrist', 'spine', 'pelvis', 'left_knee', 'right_knee',
                'left_ankle', 'right_ankle', 'left_foot', 'right_foot']

# Animation parameters
n_frames = 100       # total number of frames in the animation
dt = 1.0 / n_frames  # normalized time step; use t in [0,1]
fps = 30

# Jump parameters
forward_distance = 2.0     # horizontal distance covered during jump
max_height = 1.0           # maximum vertical height at mid-jump

# Body rotation: at take-off t=0, slight backward tilt; at mid-jump t=0.5, upright;
# at landing, slight forward tilt. We use a linear interpolation in angle.
max_tilt_rad = np.deg2rad(10)  # maximum tilt angle (10 degrees)

def get_body_rotation(t):
    # t in [0,1]; at t=0: -max_tilt, t=0.5: 0, t=1: max_tilt.
    return max_tilt_rad * (2 * t - 1)

def get_pelvis_translation(t):
    """
    Calculate the pelvis translation (x,y) at normalized time t.
    x moves linearly forward; y follows a parabolic arc.
    """
    x = forward_distance * t
    # Parabolic trajectory: y = 4 * max_height * t * (1-t)
    y = 4 * max_height * t * (1 - t)
    return np.array([x, y])

def rotate_points(points, theta):
    """
    Rotate a set of points (2D array shape (n,2)) by angle theta (in radians)
    using a 2x2 rotation matrix.
    """
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    return points @ R.T

def compute_marker_positions(t):
    """
    Compute the world positions of all markers at normalized time t.
    The computation includes:
      1. A rigid-body transformation (rotation and translation) of the base positions.
      2. Small additional oscillatory offsets for arms and knees to mimic joint flexion.
    """
    # Convert dictionary of base positions to array (15,2) ordered by marker_names.
    base_points = np.array([markers[name] for name in marker_names])
    
    # Determine body rotation and pelvis translation.
    theta = get_body_rotation(t)
    T = get_pelvis_translation(t)
    
    # Apply the rigid-body transformation: rotate and then translate.
    transformed = rotate_points(base_points, theta) + T
    
    # Now add small oscillatory adjustments:
    # Arms: left_elbow and left_wrist move slightly with an oscillation to mimic swing.
    arm_amp = 0.05
    arm_offset = arm_amp * np.array([np.sin(2 * np.pi * t), 0])
    # left side: add positive offset
    for marker in ['left_elbow', 'left_wrist']:
        idx = marker_names.index(marker)
        transformed[idx] += arm_offset
    # right side: opposite phase
    arm_offset_right = -arm_amp * np.array([np.sin(2 * np.pi * t), 0])
    for marker in ['right_elbow', 'right_wrist']:
        idx = marker_names.index(marker)
        transformed[idx] += arm_offset_right

    # Knees: add a small vertical adjustment to simulate bending.
    knee_amp = 0.05
    knee_offset = np.array([0, -knee_amp * np.abs(np.cos(2 * np.pi * t))])
    for marker in ['left_knee', 'right_knee']:
        idx = marker_names.index(marker)
        transformed[idx] += knee_offset

    return transformed

# Set up the plot.
fig, ax = plt.subplots(figsize=(6,6))
ax.set_facecolor('black')
# Ensure a black background.
fig.patch.set_facecolor('black')

# Plot limits
ax.set_xlim(-1, forward_distance + 1)
ax.set_ylim(-1.5, max_height + 1)

# Remove ticks and spines.
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Initialize the scatter plot for the point-lights.
scatter = ax.scatter([], [], s=50, c='white')

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    t = frame * dt  # normalized time in [0,1]
    positions = compute_marker_positions(t)
    scatter.set_offsets(positions)
    return scatter,

# Create animation.
anim = FuncAnimation(fig, update, frames=n_frames, init_func=init,
                     interval=1000/fps, blit=True, repeat=True)

plt.show()