
"""
This program shows an animation of a point‐light “happyman” made of exactly 15 white points
moving against a solid black background. The animation simulates a heavy‐set happy man turning
around in place with biomechanically plausible limb motions.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the base skeleton pose in body‐centered coordinates.
# The 15 joints (points) are:
# 0: Head
# 1: Neck
# 2: Left shoulder
# 3: Right shoulder
# 4: Left elbow
# 5: Right elbow
# 6: Left hand
# 7: Right hand
# 8: Torso (chest center)
# 9: Left hip
# 10: Right hip
# 11: Left knee
# 12: Right knee
# 13: Left foot
# 14: Right foot
base_skeleton = np.array([
    [ 0.0, 1.80 ],   # Head
    [ 0.0, 1.60 ],   # Neck
    [-0.20, 1.60 ],  # Left Shoulder
    [ 0.20, 1.60 ],  # Right Shoulder
    [-0.40, 1.40 ],  # Left Elbow
    [ 0.40, 1.40 ],  # Right Elbow
    [-0.50, 1.20 ],  # Left Hand
    [ 0.50, 1.20 ],  # Right Hand
    [ 0.0, 1.30 ],   # Torso (chest center)
    [-0.20, 1.00 ],  # Left Hip
    [ 0.20, 1.00 ],  # Right Hip
    [-0.20, 0.50 ],  # Left Knee
    [ 0.20, 0.50 ],  # Right Knee
    [-0.20, 0.00 ],  # Left Foot
    [ 0.20, 0.00 ]   # Right Foot
])

# Animation parameters
frames = 200           # number of frames in the animation
dt = 0.05              # time step in seconds
T = frames * dt        # total duration (seconds)
# We choose a turning speed so that the man makes a full 360° turn in T seconds.
angular_speed = 2 * np.pi / T

def biomechanical_modulation(base, t):
    """
    Returns a modulated copy of the base skeleton by adding
    small sine oscillations to simulate realistic limb movements during turning.
    The motions are subtle to represent a heavy-set individual's smooth turning.
    """
    pos = np.copy(base)
    
    # Arms: slight oscillation of the elbows and hands
    arm_amp_elbow = 0.02   # amplitude for elbows
    arm_amp_hand  = 0.03   # amplitude for hands
    phase = 2 * np.pi * t   # one oscillation period per second
    # Left side: indices 4 (elbow) and 6 (hand)
    pos[4,0] += arm_amp_elbow * np.sin(phase)   # left elbow horizontal shift
    pos[6,0] += arm_amp_hand  * np.sin(phase)     # left hand horizontal shift
    # Right side: indices 5 (elbow) and 7 (hand) - opposite phase
    pos[5,0] += -arm_amp_elbow * np.sin(phase)
    pos[7,0] += -arm_amp_hand  * np.sin(phase)
    
    # Legs: slight stepping shift of the feet
    leg_amp = 0.03  # amplitude for feet
    # Left foot (index 13) and right foot (index 14)
    pos[13,0] += leg_amp * np.sin(phase)
    pos[14,0] += -leg_amp * np.sin(phase)
    
    return pos

def rotate_points(points, angle, pivot):
    """
    Rotates an array of points (N,2) by angle (radians) about a pivot point.
    """
    # Translate points so that pivot is at origin
    translated = points - pivot
    # Define rotation matrix
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    rotated = translated.dot(R.T)
    # Translate back
    return rotated + pivot

def get_frame_positions(t):
    """
    Returns the positions of the 15 points for time t.
    Applies biomechanical limb modulations as well as rotation about the torso.
    """
    # First, modulate the base skeleton for limb movement
    modulated = biomechanical_modulation(base_skeleton, t)
    # The pivot for rotation is chosen as the torso center (joint index 8)
    pivot = modulated[8]
    # Compute overall rotation angle based on time and angular speed.
    angle = angular_speed * t
    # Rotate all points about the torso to simulate turning in place.
    rotated = rotate_points(modulated, angle, pivot)
    return rotated

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(6,8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
# Set the limits for a good view of the figure
ax.set_xlim(-1, 1)
ax.set_ylim(-0.2, 2.2)
# Remove axes visuals
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Create the scatter plot for the 15 point-lights, using white circles.
scatter = ax.scatter([], [], s=100, c='white')

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    # Current time
    t = frame * dt
    # Get transformed positions of all 15 points at time t.
    positions = get_frame_positions(t)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation using matplotlib's FuncAnimation.
anim = FuncAnimation(fig, update, frames=frames, init_func=init,
                     interval=dt*1000, blit=True)

# Uncomment one of the next lines to either save the animation as MP4 or show it.
# To save as mp4, you might need "ffmpeg" installed.
# anim.save("point_light_biological_motion.mp4", fps=30, dpi=200)

plt.show()