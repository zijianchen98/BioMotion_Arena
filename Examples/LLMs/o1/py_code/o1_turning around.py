import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define 15 key points in 3D for a simplified "man" in a neutral pose
skeleton_3d = np.array([
    [0.0, 1.8, 0.0],   # Head
    [0.0, 1.6, 0.0],   # Neck
    [0.15, 1.6, 0.0],  # Right Shoulder
    [0.35, 1.4, 0.0],  # Right Elbow
    [0.45, 1.2, 0.0],  # Right Wrist
    [-0.15, 1.6, 0.0], # Left Shoulder
    [-0.35, 1.4, 0.0], # Left Elbow
    [-0.45, 1.2, 0.0], # Left Wrist
    [0.0, 1.0, 0.0],   # Pelvis
    [0.15, 1.0, 0.0],  # Right Hip
    [0.15, 0.6, 0.0],  # Right Knee
    [0.15, 0.2, 0.0],  # Right Ankle
    [-0.15, 1.0, 0.0], # Left Hip
    [-0.15, 0.6, 0.0], # Left Knee
    [-0.15, 0.2, 0.0]  # Left Ankle
])

# Rotation around the Y-axis (vertical) for turning around
def rotate_y(points, angle):
    c, s = np.cos(angle), np.sin(angle)
    R = np.array([
        [ c, 0.0,  s],
        [0.0, 1.0, 0.0],
        [-s, 0.0,  c]
    ])
    return points @ R.T

fig, ax = plt.subplots()
fig.set_facecolor("black")
ax.set_facecolor("black")
ax.set_aspect("equal")
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(0.0, 2.0)
plt.axis("off")

scatter = ax.scatter([], [], color="white", s=30)

frames = 60  # Number of frames for the 180° turn

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    angle = np.pi * frame / (frames - 1)  # 0 to pi (180°)
    # Apply slight sway of arms/legs for simple biomechanical plausibility
    sway = 0.05 * np.sin(2 * np.pi * frame / frames)
    mod_skeleton = skeleton_3d.copy()
    # Simple arm sway
    mod_skeleton[3,0] += sway
    mod_skeleton[4,0] += sway
    mod_skeleton[6,0] -= sway
    mod_skeleton[7,0] -= sway
    # Rotate the entire body
    rotated = rotate_y(mod_skeleton, angle)
    # Project (x, y) ignoring z
    xy = rotated[:, [0, 1]]
    scatter.set_offsets(xy)
    return scatter,

ani = FuncAnimation(
    fig, update, frames=frames, init_func=init, blit=True, interval=80, repeat=True
)

plt.show()