import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This program displays a 2D point-light animation of a "sad woman" lying down.
# There are 15 point-lights on a black background, moving in a biomechanically
# plausible manner. The motion transitions smoothly from standing to lying.

# Define the number of frames in the animation and the frames per second
NUM_FRAMES = 100
FPS = 30

# We define 15 key points (head, neck, shoulders, elbows, wrists,
# hip center, hips, knees, ankles). We'll store their coordinates for a
# standing pose and a lying pose. The animation will linearly interpolate
# between these two poses to simulate lying down.

# Each row represents (x, y) in a 2D plane. Units are arbitrary screen coordinates.

# Standing pose (roughly upright, "sad" posture: slight bend at shoulders/head)
standing_pose = np.array([
    [ 0.0,  1.0],  # Head
    [ 0.0,  0.8],  # Neck
    [-0.2,  0.7],  # Left Shoulder
    [ 0.2,  0.7],  # Right Shoulder
    [-0.3,  0.5],  # Left Elbow
    [ 0.3,  0.5],  # Right Elbow
    [-0.35, 0.3],  # Left Wrist
    [ 0.35, 0.3],  # Right Wrist
    [ 0.0,  0.4],  # Hip Center
    [-0.15, 0.4],  # Left Hip
    [ 0.15, 0.4],  # Right Hip
    [-0.15, 0.1],  # Left Knee
    [ 0.15, 0.1],  # Right Knee
    [-0.15, -0.2], # Left Ankle
    [ 0.15, -0.2], # Right Ankle
])

# Lying pose (on the ground, horizontal, with slight curl as if sad)
lying_pose = np.array([
    [-0.5, 0.0],  # Head
    [-0.3, 0.0],  # Neck
    [-0.1, 0.0],  # Left Shoulder
    [ 0.1, 0.0],  # Right Shoulder
    [-0.05, -0.15],# Left Elbow
    [ 0.15, -0.15],# Right Elbow
    [ 0.0, -0.3],  # Left Wrist
    [ 0.2, -0.3],  # Right Wrist
    [-0.2, -0.1],  # Hip Center
    [-0.25, -0.1],  # Left Hip
    [-0.15, -0.1],  # Right Hip
    [-0.25, -0.2],  # Left Knee
    [-0.15, -0.2],  # Right Knee
    [-0.25, -0.3],  # Left Ankle
    [-0.15, -0.3],  # Right Ankle
])

# Create the figure and axes with a black background
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor("black")
ax.set_xlim([-1.0, 1.0])
ax.set_ylim([-0.5, 1.2])
ax.invert_yaxis()  # Invert y-axis to mimic typical 2D "screen" coordinates
plt.axis('off')

# Create scatter plot for the 15 white points
scatter = ax.scatter([], [], color='white', s=50)

def interpolate_pose(frame):
    """
    Linearly interpolate between standing_pose and lying_pose based on the
    current frame index. Returns an array of shape (15, 2).
    """
    t = frame / (NUM_FRAMES - 1)
    return (1 - t) * standing_pose + t * lying_pose

def init():
    """Initialize animation with empty data."""
    scatter.set_offsets(np.zeros((15, 2)))
    return (scatter,)

def update(frame):
    """Update scatter plot for each frame."""
    coords = interpolate_pose(frame)
    scatter.set_offsets(coords)
    return (scatter,)

anim = FuncAnimation(
    fig, update, frames=NUM_FRAMES, init_func=init, interval=1000/FPS, blit=True
)

# Uncomment the following line to save the animation as a GIF file:
# anim.save('sadwoman_lying_down.gif', writer='imagemagick', fps=FPS)

plt.show()