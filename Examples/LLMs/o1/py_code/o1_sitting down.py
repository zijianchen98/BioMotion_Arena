#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def interpolate_points(start_points, end_points, t):
    """
    Linearly interpolate between two sets of points (start_points, end_points)
    for a fraction t, where 0 <= t <= 1.

    start_points and end_points are arrays of shape (N, 2), where N is the
    number of points. Returns an array of the same shape representing
    the interpolated set of points at time t.
    """
    return (1 - t) * start_points + t * end_points

# Define 15 key points for a standing posture in (x, y). Approximate positions:
standing = np.array([
    [ 0.0, 1.5],  # Head
    [-0.2, 1.3],  # Left Shoulder
    [ 0.2, 1.3],  # Right Shoulder
    [-0.3, 1.1],  # Left Elbow
    [ 0.3, 1.1],  # Right Elbow
    [-0.35,0.9],  # Left Wrist
    [ 0.35,0.9],  # Right Wrist
    [ 0.0, 1.0],  # Torso Center
    [-0.15,0.9],  # Left Hip
    [ 0.15,0.9],  # Right Hip
    [-0.2, 0.5],  # Left Knee
    [ 0.2, 0.5],  # Right Knee
    [-0.2, 0.0],  # Left Ankle
    [ 0.2, 0.0],  # Right Ankle
    [ 0.0, 0.75]  # (Optional extra torso/neck junction)
])

# Define corresponding points for a sitting posture in (x, y). Approximate positions:
sitting = np.array([
    [ 0.0, 1.0],   # Head
    [-0.2, 0.9],   # Left Shoulder
    [ 0.2, 0.9],   # Right Shoulder
    [-0.3, 0.8],   # Left Elbow
    [ 0.3, 0.8],   # Right Elbow
    [-0.35,0.7],   # Left Wrist
    [ 0.35,0.7],   # Right Wrist
    [ 0.0, 0.7],   # Torso Center
    [-0.15,0.5],   # Left Hip
    [ 0.15,0.5],   # Right Hip
    [-0.2, 0.35],  # Left Knee
    [ 0.2, 0.35],  # Right Knee
    [-0.2, 0.0],   # Left Ankle
    [ 0.2, 0.0],   # Right Ankle
    [ 0.0, 0.6]    # (Optional extra torso/neck junction)
])

# Number of frames in the animation and desired frame rate:
num_frames = 50
fps = 25
interval_ms = 1000 // fps

# Prepare figure and axis for animation (solid black background):
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-0.1, 1.6)
ax.axis('off')

# Create a scatter object for the point-lights (white points):
scatter = ax.scatter([], [], c='white', s=50)

def init():
    """
    Initialize the scatter plot with no data.
    """
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    """
    Update function for each frame of the animation.
    frame goes from 0 to num_frames - 1.
    We interpolate between standing and sitting based on frame index.
    """
    t = frame / (num_frames - 1)  # from 0 to 1
    points = interpolate_points(standing, sitting, t)
    scatter.set_offsets(points)
    return (scatter,)

ani = FuncAnimation(
    fig, update, frames=num_frames, init_func=init,
    blit=True, interval=interval_ms, repeat=True
)

plt.show()