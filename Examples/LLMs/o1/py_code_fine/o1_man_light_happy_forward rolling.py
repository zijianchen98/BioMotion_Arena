#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define 15 key points for a tucked "forward roll" posture
skeleton = np.array([
    [ 0.00,  0.30],  # Head
    [ 0.00,  0.20],  # Neck
    [ 0.08,  0.20],  # Right Shoulder
    [-0.08,  0.20],  # Left Shoulder
    [ 0.14,  0.10],  # Right Elbow
    [-0.14,  0.10],  # Left Elbow
    [ 0.18,  0.00],  # Right Wrist
    [-0.18,  0.00],  # Left Wrist
    [ 0.00,  0.10],  # Chest
    [ 0.05,  0.00],  # Right Hip
    [-0.05,  0.00],  # Left Hip
    [ 0.07, -0.15],  # Right Knee
    [-0.07, -0.15],  # Left Knee
    [ 0.07, -0.30],  # Right Ankle
    [-0.07, -0.30]   # Left Ankle
])

fig, ax = plt.subplots()
ax.set_facecolor("black")
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect("equal")
plt.axis("off")

scatter = ax.scatter([], [], c="white", s=40)

frames = 60
def update(frame):
    # Angle for rotation (one full turn over all frames)
    angle = 2.0 * np.pi * frame / frames
    # Horizontal shift from left to right
    shift_x = -2.0 + 4.0 * (frame / frames)
    
    # Rotation matrix around origin
    cos_a, sin_a = np.cos(angle), np.sin(angle)
    R = np.array([[cos_a, -sin_a],
                  [sin_a,  cos_a]])
    
    # Rotate each point, then shift in x
    rotated = (R @ skeleton.T).T
    rotated[:, 0] += shift_x
    
    scatter.set_offsets(rotated)
    return (scatter,)

ani = FuncAnimation(fig, update, frames=frames, interval=100, blit=True, repeat=True)
plt.show()