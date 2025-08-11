#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
This Python program creates a point-light stimulus animation with 15 white dots 
representing a simple 'happyman' figure performing a waving motion. The background 
is solid black, and the motion is intended to appear coherent and biomechanically 
plausible for a simplified 'waving hand' scene.
"""

# Number of points (joints)
NUM_POINTS = 15

# Total frames in the animation
FRAMES = 100

# Frames per second (adjust to taste)
FPS = 30

# Prepare figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-1.5, 1.0)
ax.set_aspect('equal')
ax.axis('off')

# Create a scatter plot for the 15 points, colored white
scatter = ax.scatter([], [], s=50, c='white')

def get_body_points(frame):
    """
    Returns the (x, y) positions for each of the 15 body points at a given frame.
    The motion simulates:
      - Slight vertical bounce (heavy weight shift)
      - Right hand waving upward and downward
    """

    # Normalize time [0,1] for one full wave
    t = frame / FRAMES
    # Convert to radians for trig
    theta = 2.0 * np.pi * t
    
    # Base vertical bounce
    bounce = 0.05 * np.sin(2 * np.pi * 2 * t)  # 2 bounces per wave cycle

    # Body reference points (approximate neutral positions):
    #  0: Head
    #  1-2: Shoulders (L, R)
    #  3-4: Elbows (L, R)
    #  5-6: Wrists (L, R)
    #  7: Torso center
    #  8-9: Hips (L, R)
    # 10-11: Knees (L, R)
    # 12-13: Ankles (L, R)
    # 14: (Extra point for demonstration, e.g., foot or center of mass)
    # We'll define a simple static layout, then add wave to the right arm (points 4, 6).
    
    # Neutral "happyman" positions (x, y)
    neutral_positions = np.array([
        [0.0,  0.75],   # Head
        [-0.2, 0.5],    # L Shoulder
        [ 0.2, 0.5],    # R Shoulder
        [-0.3, 0.2],    # L Elbow
        [ 0.3, 0.2],    # R Elbow
        [-0.4, 0.0],    # L Wrist
        [ 0.4, 0.0],    # R Wrist
        [ 0.0,  0.3],   # Torso center
        [-0.2, 0.0],    # L Hip
        [ 0.2, 0.0],    # R Hip
        [-0.2,-0.4],    # L Knee
        [ 0.2,-0.4],    # R Knee
        [-0.2,-0.8],    # L Ankle
        [ 0.2,-0.8],    # R Ankle
        [ 0.0,-0.8],    # Extra point (e.g., foot or center of mass)
    ])

    # Add overall bounce in y-direction
    neutral_positions[:, 1] += bounce

    # Make the right arm wave by swinging elbow and wrist up and down
    # For biomechanical plausibility, we rotate them around the right shoulder
    right_shoulder = neutral_positions[2]
    # We'll define a small rotation amplitude
    wave_angle = 0.5 * np.sin(2 * np.pi * 3 * t)  # 3 hand waves per cycle

    # Indices for the right elbow and right wrist
    idx_elbow, idx_wrist = 4, 6
    elbow = neutral_positions[idx_elbow] - right_shoulder
    wrist = neutral_positions[idx_wrist] - right_shoulder

    # Rotation matrix for wave
    rot = np.array([
        [ np.cos(wave_angle), -np.sin(wave_angle)],
        [ np.sin(wave_angle),  np.cos(wave_angle)]
    ])

    # Rotate elbow and wrist relative to the right shoulder
    elbow_rotated = rot @ elbow
    wrist_rotated = rot @ wrist

    # Reposition back
    neutral_positions[idx_elbow] = right_shoulder + elbow_rotated
    neutral_positions[idx_wrist] = right_shoulder + wrist_rotated

    return neutral_positions

def init():
    scatter.set_offsets(np.zeros((NUM_POINTS, 2)))
    return (scatter,)

def update(frame):
    body_xy = get_body_points(frame)
    scatter.set_offsets(body_xy)
    return (scatter,)

anim = FuncAnimation(fig, update, frames=FRAMES, interval=1000/FPS, init_func=init, blit=True)
plt.show()