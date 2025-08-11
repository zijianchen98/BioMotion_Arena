
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of joints (point‐lights)
n_joints = 15
# Number of frames in the animation
n_frames = 80

# Define initial (standing) joint positions (x, y)
# Order of joints:
# 0: Head, 1: Neck, 2: Left Shoulder, 3: Right Shoulder,
# 4: Left Elbow, 5: Right Elbow, 6: Left Wrist, 7: Right Wrist,
# 8: Pelvis, 9: Left Hip, 10: Right Hip,
# 11: Left Knee, 12: Right Knee, 13: Left Ankle, 14: Right Ankle

standing = np.array([
    [ 0.0, 1.8],   # Head
    [ 0.0, 1.6],   # Neck
    [-0.2, 1.5],   # L shoulder
    [ 0.2, 1.5],   # R shoulder
    [-0.5, 1.2],   # L elbow
    [ 0.5, 1.2],   # R elbow
    [-0.7, 0.9],   # L wrist
    [ 0.7, 0.9],   # R wrist
    [ 0.0, 1.1],   # Pelvis
    [-0.2, 1.0],   # L hip
    [ 0.2, 1.0],   # R hip
    [-0.2, 0.6],   # L knee
    [ 0.2, 0.6],   # R knee
    [-0.2, 0.0],   # L ankle
    [ 0.2, 0.0],   # R ankle
])

# Define final (sitting) joint positions
# Assume person sits on a chair so pelvis and knees at ~0.6m high
sitting = np.array([
    [ 0.0, 1.0],   # Head
    [ 0.0, 0.85],  # Neck
    [-0.2, 0.80],  # L shoulder
    [ 0.2, 0.80],  # R shoulder
    [-0.5, 0.60],  # L elbow
    [ 0.5, 0.60],  # R elbow
    [-0.7, 0.40],  # L wrist
    [ 0.7, 0.40],  # R wrist
    [ 0.0, 0.60],  # Pelvis
    [-0.2, 0.60],  # L hip
    [ 0.2, 0.60],  # R hip
    [-0.2, 0.60],  # L knee
    [ 0.2, 0.60],  # R knee
    [-0.2, 0.0],   # L ankle (foot on ground)
    [ 0.2, 0.0],   # R ankle
])

# Precompute interpolated positions for each frame
frames = np.zeros((n_frames, n_joints, 2))
for i in range(n_frames):
    alpha = i / (n_frames - 1)
    frames[i] = (1 - alpha) * standing + alpha * sitting

# Set up the figure
fig, ax = plt.subplots(figsize=(5, 8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(0.0, 2.0)
ax.axis('off')

# Scatter plot for the point‐lights
scatter = ax.scatter([], [], s=100, c='white')

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame_idx):
    pts = frames[frame_idx]
    scatter.set_offsets(pts)
    return scatter,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=n_frames,
    init_func=init, blit=True, interval=50
)

plt.show()
