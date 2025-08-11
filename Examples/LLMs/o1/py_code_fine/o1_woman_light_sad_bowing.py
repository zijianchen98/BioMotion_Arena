import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------------------------------------
# Configuration
# -------------------------------------------------------
# Number of total frames in the animation
TOTAL_FRAMES = 120

# We'll define 15 body points (x, y) for a "sadwoman" standing (startPose)
# and bowing (endPose). Then we'll animate between these two poses.

startPose = np.array([
    [ 0.0, 5.0],  # Head
    [ 0.0, 4.0],  # Neck
    [ 1.0, 4.0],  # Right Shoulder
    [ 1.0, 3.0],  # Right Elbow
    [ 1.0, 2.5],  # Right Wrist
    [-1.0, 4.0],  # Left Shoulder
    [-1.0, 3.0],  # Left Elbow
    [-1.0, 2.5],  # Left Wrist
    [ 0.0, 3.5],  # Torso
    [ 0.5, 3.0],  # Right Hip
    [ 0.5, 2.0],  # Right Knee
    [ 0.5, 1.0],  # Right Ankle
    [-0.5, 3.0],  # Left Hip
    [-0.5, 2.0],  # Left Knee
    [-0.5, 1.0]   # Left Ankle
])

endPose = np.array([
    [ 0.0, 4.2],  # Head (bowed)
    [ 0.0, 4.0],  # Neck
    [ 1.0, 3.9],  # Right Shoulder
    [ 1.2, 3.0],  # Right Elbow
    [ 1.2, 2.2],  # Right Wrist
    [-1.0, 3.9],  # Left Shoulder
    [-1.2, 3.0],  # Left Elbow
    [-1.2, 2.2],  # Left Wrist
    [ 0.0, 3.2],  # Torso
    [ 0.5, 2.7],  # Right Hip
    [ 0.5, 2.0],  # Right Knee
    [ 0.5, 1.0],  # Right Ankle
    [-0.5, 2.7],  # Left Hip
    [-0.5, 2.0],  # Left Knee
    [-0.5, 1.0]   # Left Ankle
])

# -------------------------------------------------------
# Helper Functions
# -------------------------------------------------------
def interpolate_pose(start, end, p):
    """
    Linearly interpolate between start and end, given parameter p in [0,1].
    start, end: (15,2) arrays for the 15 points
    p: float in [0,1]
    returns an array (15,2)
    """
    return (1 - p) * start + p * end

def get_parameter(frame):
    """
    Returns a parameter in [0,1] for frames 0..60, then in [1,0] for frames 60..120.
    This creates a single bow cycle (down, then up).
    """
    half = TOTAL_FRAMES // 2
    if frame <= half:
        return frame / float(half)
    else:
        return 1.0 - ((frame - half) / float(half))

# -------------------------------------------------------
# Animation
# -------------------------------------------------------
fig, ax = plt.subplots()
# Black background for the figure
fig.patch.set_facecolor("black")

# Scatter plot for 15 white points
scatter = ax.scatter([], [], c="white", s=50)

# Set axis limits and remove axes
ax.set_xlim(-2.0, 2.0)
ax.set_ylim(0.0, 6.0)
ax.set_facecolor("black")
ax.set_xticks([])
ax.set_yticks([])

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    p = get_parameter(frame)
    pose = interpolate_pose(startPose, endPose, p)
    scatter.set_offsets(pose)
    return scatter,

ani = FuncAnimation(
    fig,
    update,
    frames=range(TOTAL_FRAMES),
    init_func=init,
    blit=True,
    interval=50,  # ms between frames (adjust as desired)
    repeat=True
)

plt.show()