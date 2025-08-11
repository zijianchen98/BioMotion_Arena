import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define 15 keypoint coordinates for standing (sad posture) and sitting.
# Each row corresponds to (x, y) for a single point.
# The points are: 
# 1: Head
# 2: Neck
# 3: Right shoulder
# 4: Right elbow
# 5: Right wrist
# 6: Left shoulder
# 7: Left elbow
# 8: Left wrist
# 9: Right hip
# 10: Right knee
# 11: Right ankle
# 12: Left hip
# 13: Left knee
# 14: Left ankle
# 15: Torso center
stand_pos = np.array([
    [ 0.05, 1.80],  # Head
    [ 0.00, 1.60],  # Neck
    [ 0.15, 1.60],  # R Shoulder
    [ 0.25, 1.45],  # R Elbow
    [ 0.25, 1.25],  # R Wrist
    [-0.15, 1.60],  # L Shoulder
    [-0.25, 1.45],  # L Elbow
    [-0.25, 1.25],  # L Wrist
    [ 0.10, 1.20],  # R Hip
    [ 0.10, 0.70],  # R Knee
    [ 0.10, 0.00],  # R Ankle
    [-0.10, 1.20],  # L Hip
    [-0.10, 0.70],  # L Knee
    [-0.10, 0.00],  # L Ankle
    [ 0.00, 1.40],  # Torso center
])

sit_pos = np.array([
    [ 0.05, 1.50],  # Head
    [ 0.00, 1.35],  # Neck
    [ 0.15, 1.35],  # R Shoulder
    [ 0.22, 1.20],  # R Elbow
    [ 0.22, 1.00],  # R Wrist
    [-0.15, 1.35],  # L Shoulder
    [-0.22, 1.20],  # L Elbow
    [-0.22, 1.00],  # L Wrist
    [ 0.10, 0.90],  # R Hip
    [ 0.10, 0.50],  # R Knee
    [ 0.10, 0.00],  # R Ankle
    [-0.10, 0.90],  # L Hip
    [-0.10, 0.50],  # L Knee
    [-0.10, 0.00],  # L Ankle
    [ 0.00, 1.20],  # Torso center
])

# Interpolate positions between standing and sitting to create frames.
def get_positions(t):
    # t ranges from 0 (fully standing) to 1 (fully sitting)
    return (1 - t) * stand_pos + t * sit_pos

# Set up the figure and axes.
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0.0, 2.0)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the scatter plot with 15 white points.
points = ax.scatter([], [], s=60, c='white')

def init():
    # Initialize scatter with no data
    points.set_offsets([])
    return (points,)

def update(frame):
    # Frame goes from 0 to total_frames-1.
    # Normalize to [0,1] for interpolation.
    t = frame / 60.0
    pos = get_positions(t)
    points.set_offsets(pos)
    return (points,)

ani = FuncAnimation(
    fig, update, frames=61, init_func=init, blit=True, interval=50, repeat=True
)

# Show the animated stimulus
plt.show()