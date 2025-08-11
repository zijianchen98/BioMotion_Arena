#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of frames in the animation
NUM_FRAMES = 60

# Define 15 keypoints (x, y) for a standing posture
standing = np.array([
    [0.0,  1.0],  # Head
    [0.0,  0.8],  # Neck
    [-0.2, 0.8],  # Left Shoulder
    [ 0.2, 0.8],  # Right Shoulder
    [-0.3, 0.6],  # Left Elbow
    [ 0.3, 0.6],  # Right Elbow
    [-0.35,0.4],  # Left Hand
    [ 0.35,0.4],  # Right Hand
    [0.0,  0.6],  # Torso Center
    [0.0,  0.4],  # Waist
    [-0.2, 0.2],  # Left Hip
    [ 0.2, 0.2],  # Right Hip
    [-0.2, 0.0],  # Left Knee
    [ 0.2, 0.0],  # Right Knee
    [0.0,  0.2],  # Extra Point (e.g., mid-chest)
])

# Define 15 keypoints (x, y) for a lying-down posture
lying = np.array([
    [-0.8, 0.1],  # Head
    [-0.7, 0.1],  # Neck
    [-0.7, 0.1],  # Left Shoulder
    [-0.6, 0.1],  # Right Shoulder
    [-0.6, 0.0],  # Left Elbow
    [-0.5, 0.0],  # Right Elbow
    [-0.55,-0.1], # Left Hand
    [-0.45,-0.1], # Right Hand
    [-0.65,0.0],  # Torso Center
    [-0.55,0.0],  # Waist
    [-0.4, 0.0],  # Left Hip
    [-0.3, 0.0],  # Right Hip
    [-0.2, 0.0],  # Left Knee
    [-0.1, 0.0],  # Right Knee
    [-0.5, 0.1],  # Extra Point (e.g., mid-chest)
])

# Set up the figure with black background
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-0.2, 1.2)
ax.set_aspect('equal')
ax.axis('off')

# Create scatter plot for the 15 white points
scatter = ax.scatter([], [], c='white', s=50)

def interpolate_positions(frame):
    """Linearly interpolate between standing and lying positions."""
    t = frame / (NUM_FRAMES - 1)
    return standing + t * (lying - standing)

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    pts = interpolate_positions(frame)
    scatter.set_offsets(pts)
    return scatter,

ani = FuncAnimation(
    fig, update, frames=NUM_FRAMES, init_func=init,
    interval=80, blit=True, repeat=True
)

plt.show()