import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define keyframe coordinates (x, y) for 15 points in three main poses: standing, squatting, midair.
# Indices (for readability): 
# 0: head, 1: neck, 2: chest, 3: L_shoulder, 4: L_elbow, 5: L_wrist, 
# 6: R_shoulder, 7: R_elbow, 8: R_wrist, 9: L_hip, 10: L_knee, 11: L_ankle,
# 12: R_hip, 13: R_knee, 14: R_ankle
standing = np.array([
    [0.0, 7.0],   # head
    [0.0, 6.0],   # neck
    [0.0, 5.0],   # chest
    [-1.0, 5.0],  # L_shoulder
    [-1.0, 4.0],  # L_elbow
    [-1.0, 3.0],  # L_wrist
    [1.0, 5.0],   # R_shoulder
    [1.0, 4.0],   # R_elbow
    [1.0, 3.0],   # R_wrist
    [-0.5, 3.0],  # L_hip
    [-0.5, 1.5],  # L_knee
    [-0.5, 0.0],  # L_ankle
    [0.5, 3.0],   # R_hip
    [0.5, 1.5],   # R_knee
    [0.5, 0.0],   # R_ankle
])

# Slightly crouched
squatting = np.array([
    [0.0, 6.5],
    [0.0, 5.8],
    [0.0, 4.8],
    [-1.1, 4.7],
    [-1.2, 3.8],
    [-1.2, 3.0],
    [1.1, 4.7],
    [1.2, 3.8],
    [1.2, 3.0],
    [-0.5, 2.5],
    [-0.5, 1.3],
    [-0.5, 0.0],
    [0.5, 2.5],
    [0.5, 1.3],
    [0.5, 0.0],
])

# Jump apex (midair, body extended)
midair = np.array([
    [0.0, 8.0],
    [0.0, 7.0],
    [0.0, 6.0],
    [-1.0, 6.0],
    [-1.0, 5.0],
    [-1.0, 4.0],
    [1.0, 6.0],
    [1.0, 5.0],
    [1.0, 4.0],
    [-0.5, 4.0],
    [-0.5, 2.5],
    [-0.5, 1.0],
    [0.5, 4.0],
    [0.5, 2.5],
    [0.5, 1.0],
])

# Helper function to interpolate between two keyframes
def lerp(a, b, fraction):
    return a + (b - a) * fraction

# Given a time t in [0,1], return the 15 (x,y) coordinates.
# We break the jump cycle into four segments: 
# 0-0.25 (standing->squatting), 0.25-0.5 (squatting->midair), 
# 0.5-0.75 (midair->squatting), 0.75-1.0 (squatting->standing).
def get_positions(t):
    if t < 0.25:
        # standing -> squatting
        local_t = t / 0.25
        return lerp(standing, squatting, local_t)
    elif t < 0.5:
        # squatting -> midair
        local_t = (t - 0.25) / 0.25
        return lerp(squatting, midair, local_t)
    elif t < 0.75:
        # midair -> squatting
        local_t = (t - 0.5) / 0.25
        return lerp(midair, squatting, local_t)
    else:
        # squatting -> standing
        local_t = (t - 0.75) / 0.25
        return lerp(squatting, standing, local_t)

fig, ax = plt.subplots(figsize=(5, 5))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 9)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter([], [], c='white', s=50)

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    # frame goes from 0..total_frames-1
    total_frames = 100
    t = (frame % total_frames) / total_frames  # normalized time
    coords = get_positions(t)
    scatter.set_offsets(coords)
    return scatter,

ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=50)

plt.show()