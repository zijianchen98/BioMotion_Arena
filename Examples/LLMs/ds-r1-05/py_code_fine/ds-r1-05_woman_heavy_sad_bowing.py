
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Initialize positions (start, bowed, end)
positions = [
    # Start (upright)
    np.array([
        [0.0, 1.70],    # head (0)
        [0.0, 1.60],    # neck (1)
        [-0.20, 1.50],  # left shoulder (2)
        [0.20, 1.50],   # right shoulder (3)
        [-0.40, 1.30],  # left elbow (4)
        [0.40, 1.30],   # right elbow (5)
        [-0.50, 1.10],  # left wrist (6)
        [0.50, 1.10],   # right wrist (7)
        [0.00, 1.30],   # torso (8)
        [0.00, 0.90],   # hip center (9)
        [-0.15, 0.90],  # left hip (10)
        [0.15, 0.90],   # right hip (11)
        [-0.15, 0.50],  # left knee (12)
        [0.15, 0.50],   # right knee (13)
        [-0.15, 0.00]   # left ankle (14)
    ]),
    # Bowed position
    np.array([
        [0.00, 1.30],
        [0.00, 1.20],
        [-0.20, 1.10],
        [0.20, 1.10],
        [-0.40, 0.90],
        [0.40, 0.90],
        [-0.50, 0.70],
        [0.50, 0.70],
        [0.00, 1.00],
        [0.00, 0.90],
        [-0.15, 0.90],
        [0.15, 0.90],
        [-0.15, 0.50],
        [0.15, 0.50],
        [-0.15, 0.00]
    ]),
    # End (upright, same as start)
    np.array([
        [0.0, 1.70],
        [0.0, 1.60],
        [-0.20, 1.50],
        [0.20, 1.50],
        [-0.40, 1.30],
        [0.40, 1.30],
        [-0.50, 1.10],
        [0.50, 1.10],
        [0.00, 1.30],
        [0.00, 0.90],
        [-0.15, 0.90],
        [0.15, 0.90],
        [-0.15, 0.50],
        [0.15, 0.50],
        [-0.15, 0.00]
    ])
]

# Keyframes timing (normalized 0 to 1)
keyframes = [0, 0.3, 1]

# Cubic interpolation function
def interpolate(p0, p1, p2, p3, t):
    return (
        p1 + 
        0.5 * t * (p2 - p0 + 
        t * (2 * p0 - 5 * p1 + 4 * p2 - p3 + 
        t * (3 * (p1 - p2) + p3 - p0)))
    )

# Set up figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_facecolor('black')
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(0.0, 2.0)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

# Initialize scatter plot
scatter = ax.scatter(
    positions[0][:,0], positions[0][:,1], 
    s=100, c='white', edgecolor='none'
)

def update(frame):
    t_full = frame / 180.0
    # Bow cycle (0-180 frames)
    t = (t_full % 1.0)
    
    # Keyframe selection and interpolation weights
    if t <= keyframes[1]:
        t_norm = t / keyframes[1]
        idx0, idx1, idx2, idx3 = 0, 0, 1, 2
    else:
        t_norm = (t - keyframes[1]) / (1.0 - keyframes[1])
        idx0, idx1, idx2, idx3 = 0, 1, 2, 2

    # Interpolate positions
    new_pos = np.zeros((15, 2))
    for i in range(15):
        p0 = positions[idx0][i]
        p1 = positions[idx1][i]
        p2 = positions[idx2][i]
        p3 = positions[idx3][i]
        new_pos[i] = interpolate(p0, p1, p2, p3, t_norm)
    
    scatter.set_offsets(new_pos)
    return scatter,

# Create animation
ani = FuncAnimation(
    fig, update, frames=180, 
    interval=16, blit=True
)

plt.tight_layout()
plt.show()
