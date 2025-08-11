#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define total frames and frame rate
TOTAL_FRAMES = 120
FPS = 30

# Time array
t_vals = np.linspace(0, 1, TOTAL_FRAMES)

# Number of points
NUM_POINTS = 15

# Define two key poses (upright and bowed) for each of 15 points in 2D.
# Each pose is an (NUM_POINTS, 2) array.
# For a "sad, heavy-weight" posture, we hunch shoulders slightly and shift hips.
# Coordinates are arbitrary but attempt a rough skeletal layout.

# Upright posture: [x, y] for each joint
upright_pose = np.array([
    [0.0,  1.7],  # Head
    [-0.3, 1.5],  # Left Shoulder
    [0.3,  1.5],  # Right Shoulder
    [-0.4, 1.2],  # Left Elbow
    [0.4,  1.2],  # Right Elbow
    [-0.5, 0.9],  # Left Wrist
    [0.5,  0.9],  # Right Wrist
    [0.0,  1.4],  # Chest Center
    [0.0,  1.2],  # Spine/Hip Center
    [-0.2, 1.0],  # Left Hip
    [0.2,  1.0],  # Right Hip
    [-0.2, 0.6],  # Left Knee
    [0.2,  0.6],  # Right Knee
    [-0.2, 0.0],  # Left Ankle
    [0.2,  0.0],  # Right Ankle
])

# Bowed posture: torso bent forward, head and shoulders dropped
bowed_pose = np.array([
    [0.0,  1.55], # Head
    [-0.35,1.35], # Left Shoulder
    [0.35, 1.35], # Right Shoulder
    [-0.45,1.05], # Left Elbow
    [0.45, 1.05], # Right Elbow
    [-0.55,0.8],  # Left Wrist
    [0.55, 0.8],  # Right Wrist
    [0.0,  1.25], # Chest Center
    [0.0,  1.05], # Spine/Hip Center
    [-0.2, 0.85], # Left Hip
    [0.2,  0.85], # Right Hip
    [-0.2, 0.45], # Left Knee
    [0.2,  0.45], # Right Knee
    [-0.2, -0.05],# Left Ankle
    [0.2,  -0.05],# Right Ankle
])

# Create figure
fig, ax = plt.subplots(figsize=(5, 5))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-0.2, 2.0)
ax.axis('off')

# Scatter plot for the 15 points
scat = ax.scatter([], [], c='white', s=50)

# Interpolation function: 
# We'll bow down from frames 0->(TOTAL_FRAMES/2) and back up from (TOTAL_FRAMES/2)->TOTAL_FRAMES.
def interpolate_pose(upright, bowed, frame, total):
    half = total // 2
    if frame <= half:
        alpha = frame / half
    else:
        alpha = 1.0 - (frame - half) / half
    return (1 - alpha) * upright + alpha * bowed

def init():
    scat.set_offsets([])
    return scat,

def animate(frame):
    current_pose = interpolate_pose(upright_pose, bowed_pose, frame, TOTAL_FRAMES)
    scat.set_offsets(current_pose)
    return scat,

ani = animation.FuncAnimation(
    fig, animate, frames=range(TOTAL_FRAMES), init_func=init, 
    interval=1000/FPS, blit=True, repeat=True
)

plt.show()