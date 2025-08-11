import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ============================================================
# Generate a set of 15 3D points representing a simplistic human figure
# in a neutral pose (e.g., slightly spread standing pose).
# Indices (for reference):
# 0: Head
# 1: Neck
# 2: Right Shoulder
# 3: Right Elbow
# 4: Right Hand
# 5: Left Shoulder
# 6: Left Elbow
# 7: Left Hand
# 8: Hips (Pelvis Center)
# 9: Right Hip
# 10: Right Knee
# 11: Right Foot
# 12: Left Hip
# 13: Left Knee
# 14: Left Foot
# ============================================================

base_skeleton = np.array([
    [0.0,  1.7, 0.0],   # Head
    [0.0,  1.5, 0.0],   # Neck
    [0.2,  1.4, 0.0],   # Right Shoulder
    [0.4,  1.2, 0.0],   # Right Elbow
    [0.5,  1.0, 0.0],   # Right Hand
    [-0.2, 1.4, 0.0],   # Left Shoulder
    [-0.4, 1.2, 0.0],   # Left Elbow
    [-0.5, 1.0, 0.0],   # Left Hand
    [0.0,  1.0, 0.0],   # Hips (Pelvis Center)
    [0.15, 0.9, 0.0],   # Right Hip
    [0.15, 0.5, 0.0],   # Right Knee
    [0.15, 0.1, 0.0],   # Right Foot
    [-0.15,0.9, 0.0],   # Left Hip
    [-0.15,0.5, 0.0],   # Left Knee
    [-0.15,0.1, 0.0]    # Left Foot
])

def rotate_y(points, angle):
    """
    Rotate a set of points (Nx3) around the Y-axis by 'angle' (in radians).
    """
    rotation_matrix = np.array([
        [ np.cos(angle), 0, np.sin(angle)],
        [            0, 1,            0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])
    return points @ rotation_matrix.T

def animate_frame(frame):
    """
    Animation function called by FuncAnimation.
    This will rotate the skeleton about the Y-axis and add a small,
    natural arm-swing-like motion for plausibility.
    """
    # Clear previous draws
    plt.cla()
    ax.set_facecolor("black")
    fig.patch.set_facecolor("black")
    plt.xlim(-1.5, 1.5)
    plt.ylim(-0.1, 2.0)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.axis("off")

    # Angle for the turnaround
    angle = 2.0 * np.pi * frame / num_frames

    # Create a small additional sway for arms and legs
    sway = 0.1 * np.sin(2.0 * angle)

    # Copy base skeleton so we can modify
    skel = base_skeleton.copy()

    # Add some small up/down motion of arms (elbows, hands) for realism
    # Right arm
    skel[3,1] += sway
    skel[4,1] += sway
    # Left arm
    skel[6,1] -= sway
    skel[7,1] -= sway

    # Now rotate entire skeleton around y-axis
    skel = rotate_y(skel, angle)

    # Extract X, Y for 2D plotting (orthographic projection: ignore Z)
    x_vals = skel[:,0]
    y_vals = skel[:,1]

    # Plot the 15 white points
    plt.scatter(x_vals, y_vals, c="white", s=40)

    # You can optionally draw minimal lines to see the structure better:
    # (Not strictly necessary for point-light displays, but helpful to check.)
    # For a pure point-light stimulus, comment out these lines:
    # connections = [(0,1), (1,2), (2,3), (3,4), (1,5), (5,6), (6,7),
    #                (1,8), (8,9), (9,10), (10,11), (8,12), (12,13), (13,14)]
    # for (i,j) in connections:
    #     plt.plot([x_vals[i], x_vals[j]], [y_vals[i], y_vals[j]],
    #              c="white", linewidth=2)

# Number of frames for the turning animation
num_frames = 120

fig = plt.figure()
ax = fig.add_subplot(111)

anim = FuncAnimation(fig, animate_frame, frames=num_frames, interval=60, repeat=True)
plt.show()