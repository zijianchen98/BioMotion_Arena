
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 15 marker names and order:
# Head, Right Shoulder, Left Shoulder, Right Elbow, Left Elbow,
# Right Wrist, Left Wrist, Chest, Pelvis, Right Hip, Left Hip,
# Right Knee, Left Knee, Right Ankle, Left Ankle
#
# Indexed below for convenience

def get_pose_points(theta):
    """
    Returns the 15 3D joint positions of a standing man with arms hanging,
    at a rotation theta (about vertical, Y axis).
    Units are in arbitrary but proportionally human scale (meters).
    """
    # Here, standing upright, arms at side
    # Y axis: up, X axis: left-right, Z axis: front-back
    # Centered at midpoint of pelvis at (0,0,0)
    #
    # Anatomical coordinates
    pose = np.array([
        [0.0, 1.8, 0.0],   # 0 Head (center)
        [0.20, 1.6, 0.07], # 1 Right Shoulder
        [-0.20, 1.6, 0.07],# 2 Left Shoulder
        [0.33, 1.28, 0.02],# 3 Right Elbow
        [-0.33, 1.28, 0.02],# 4 Left Elbow
        [0.37, 1.04, 0.00], # 5 Right Wrist
        [-0.37, 1.04, 0.00],# 6 Left Wrist
        [0.0, 1.54, 0.09], # 7 Chest (sternum)
        [0.0, 1.1, 0.11],  # 8 Pelvis (navel)
        [0.15, 1.04, 0.12],# 9 Right Hip
        [-0.15, 1.04, 0.12],#10 Left Hip
        [0.15, 0.58, 0.04],# 11 Right Knee
        [-0.15, 0.58, 0.04],#12 Left Knee
        [0.15, 0.1, 0.03], # 13 Right Ankle
        [-0.15, 0.1, 0.03] # 14 Left Ankle
    ])
    # Simulate a slight body sway to suggest natural stance
    sway = 0.015 * np.sin(np.array([
        1,0.7,0.7,0.8,0.8,0.9,0.9,1,1, 1, 1, 0.8,0.8,0.5,0.5
    ])*theta)*np.array([1,0.9,0.9,0.6,0.6,0.4,0.4,1,1,1,1,0.7,0.7,0.2,0.2])
    pose[:,0] += sway

    # Body rotates about Y around fixed axis at (0,1.1,0) (pelvis height)
    # Get translation to origin, rotate, translate back
    pelvis_y = 1.1
    T = pose.copy()
    T[:,1] -= pelvis_y

    # Rotation matrix about Y by theta
    ct = np.cos(theta)
    st = np.sin(theta)
    R = np.array([
        [ct, 0, st],
        [0,  1, 0],
        [-st,0, ct]
    ])
    T = T @ R.T

    T[:,1] += pelvis_y
    return T

def project_points(points3D):
    """Simple orthographic projection to 2D: X and Y axes (camera in front)"""
    # To match example: Y vertical, X horizontal (centered), origin at bottom
    return points3D[:,[0,1]]

# Animation parameters
FPS = 60
DUR = 2.5   # seconds per full rotation (turn)
NFRAMES = int(FPS * DUR)
FIGSIZE = (4, 8)

# Setup plot
fig, ax = plt.subplots(figsize=FIGSIZE)
ax.set_facecolor('black')
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0, 2)
ax.set_xticks([])
ax.set_yticks([])
plt.tight_layout(pad=0)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Draw points as scatter
points_plot = ax.scatter([], [], s=80, color='white', edgecolor='none')

def init():
    points_plot.set_offsets(np.zeros((15,2)))
    return (points_plot,)

def animate(i):
    # theta increases smoothly from 0 to 2pi (full turn) and continues
    t = i / NFRAMES
    # For a smooth 'turning around', we go from 0 to pi (half turn), then pi to 2pi (back), the man
    # literally rotates in place
    theta = 2 * np.pi * t
    pose = get_pose_points(theta)
    pts2d = project_points(pose)
    # Center image (mean X=0)
    pts2d[:,0] -= np.mean(pts2d[:,0])
    points_plot.set_offsets(pts2d)
    return (points_plot,)

ani = animation.FuncAnimation(
    fig, animate, frames=NFRAMES, interval=1000/FPS, blit=True, init_func=init, repeat=True
)

plt.show()
