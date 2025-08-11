import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define a 3D skeleton for a "sad" posture with 15 key points
# (x, y, z) coordinates in meters, approximately hunched forward
skeleton_3d = np.array([
    [0.0,   1.70,  0.0],  # 1 Head
    [0.0,   1.50,  0.0],  # 2 Neck
    [-0.15, 1.40,  0.05], # 3 Left Shoulder
    [ 0.15, 1.40,  0.05], # 4 Right Shoulder
    [-0.25, 1.10,  0.05], # 5 Left Elbow
    [ 0.25, 1.10,  0.05], # 6 Right Elbow
    [-0.35, 0.85,  0.05], # 7 Left Hand
    [ 0.35, 0.85,  0.05], # 8 Right Hand
    [0.0,   1.00,  0.05], # 9 Upper Torso
    [0.0,   0.80,  0.00], # 10 Lower Torso
    [-0.15, 0.60, -0.05], # 11 Left Hip
    [ 0.15, 0.60, -0.05], # 12 Right Hip
    [-0.15, 0.30, -0.05], # 13 Left Knee
    [ 0.15, 0.30, -0.05], # 14 Right Knee
    [-0.15, 0.00,  0.0 ], # 15 Left Foot
    # (Note: We'll ignore the right foot's separate point;
    # we only need 15 total, so combining left and right feet 
    # if desired can be done but we will stick with 15 points.)
])

# For a "sad" posture, shift torso and head slightly forward
skeleton_3d[:, 2] += 0.10  # forward shift
skeleton_3d[:, 0] *= 0.9   # narrow shoulders, for a "light weight" build
skeleton_3d[:, 1] -= 0.05  # slight slump

# Create a figure with black background
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('equal')
ax.axis('off')

# Scatter plot (initially empty); we'll update in animation
scatter = ax.scatter([], [], c='white', s=30)

# Define rotation around the Y-axis to simulate turning
def rotate_y(points, theta):
    """Rotate points around the Y-axis by angle theta."""
    rotation_matrix = np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [             0, 1,             0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return points.dot(rotation_matrix.T)

# Project 3D points onto 2D for plotting (orthographic projection)
def project_2d(points_3d):
    # x = X, y = Y (ignore Z in orthographic)
    return points_3d[:, 0], points_3d[:, 1]

# Animation update function
def update(frame):
    # Theta goes from 0 to pi for a 180-degree turn
    theta = np.pi * frame / frames
    # Rotate 3D skeleton
    rotated = rotate_y(skeleton_3d, theta)
    # Project to 2D
    x, y = project_2d(rotated)
    scatter.set_offsets(np.column_stack((x, y)))
    return scatter,

frames = 60  # number of animation frames
ani = FuncAnimation(fig, update, frames=frames, interval=100, blit=True)

plt.show()