
"""
This program uses matplotlib’s animation to display a point‐light stimulus of a “sadman”
with heavy weight performing a jump‐up action. Exactly 15 white point‐lights (representing
key body joints) are animated over a solid black background. The movement is biomechanically
plausible – beginning from a crouched “loaded” posture, transitioning upward into a jump peak,
and then returning to the initial crouched posture.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Total number of frames for a full jump cycle
TOTAL_FRAMES = 100
# Maximum additional vertical offset at the jump peak (in meters)
JUMP_HEIGHT = 0.5

# Define the 15 joints for two postures:
# We use the following order:
# 0: Head, 1: Mid-shoulder, 2: Left shoulder, 3: Right shoulder,
# 4: Left elbow, 5: Right elbow, 6: Left hand, 7: Right hand,
# 8: Waist, 9: Left hip, 10: Right hip, 11: Left knee, 12: Right knee,
# 13: Left ankle, 14: Right ankle

# Crouched posture (at the beginning and end, “loaded” for jump)
crouch = np.array([
    [0.0, 1.7],    # Head (slightly drooped)
    [0.0, 1.5],    # Mid-shoulder
    [-0.2, 1.5],   # Left shoulder
    [0.2, 1.5],    # Right shoulder
    [-0.35, 1.3],  # Left elbow
    [0.35, 1.3],   # Right elbow
    [-0.45, 1.1],  # Left hand
    [0.45, 1.1],   # Right hand
    [0.0, 1.1],    # Waist
    [-0.2, 0.9],   # Left hip
    [0.2, 0.9],    # Right hip
    [-0.2, 0.5],   # Left knee
    [0.2, 0.5],    # Right knee
    [-0.2, 0.1],   # Left ankle
    [0.2, 0.1]     # Right ankle
])

# Standing (or “extended”) posture typical at the jump peak
stand = np.array([
    [0.0, 1.8],    # Head (upright)
    [0.0, 1.6],    # Mid-shoulder
    [-0.2, 1.6],   # Left shoulder
    [0.2, 1.6],    # Right shoulder
    [-0.35, 1.4],  # Left elbow
    [0.35, 1.4],   # Right elbow
    [-0.45, 1.2],  # Left hand
    [0.45, 1.2],   # Right hand
    [0.0, 1.2],    # Waist
    [-0.2, 1.0],   # Left hip
    [0.2, 1.0],    # Right hip
    [-0.2, 0.6],   # Left knee
    [0.2, 0.6],    # Right knee
    [-0.2, 0.2],   # Left ankle
    [0.2, 0.2]     # Right ankle
])


def interpolate_posture(frame):
    """
    For frames 0 to TOTAL_FRAMES:
      - From frame 0 to frame TOTAL_FRAMES/2: interpolate from crouched to standing
      - From frame TOTAL_FRAMES/2 to TOTAL_FRAMES: interpolate from standing back to crouched
    """
    half = TOTAL_FRAMES // 2
    if frame <= half:
        r = frame / half
        posture = (1 - r) * crouch + r * stand
    else:
        r = (frame - half) / half
        posture = (1 - r) * stand + r * crouch
    return posture


def jump_vertical_offset(frame):
    """
    Calculate the additional vertical offset due to the jump.
    A parabolic trajectory is used so that the maximum vertical offset is achieved at the midpoint.
    Using the form: offset = 4 * H * t*(1-t) where t in [0, 1]
    """
    t = frame / TOTAL_FRAMES
    offset = 4 * JUMP_HEIGHT * t * (1 - t)
    return offset


# Set up the Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(5, 8))
ax.set_facecolor('black')
plt.axis('off')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 3)

# Initialize the scatter plot for the 15 points
scatter = ax.scatter([], [], s=100, c='white')


def init():
    scatter.set_offsets([])
    return scatter,


def update(frame):
    posture = interpolate_posture(frame)
    # Calculate the jump vertical offset
    y_offset = jump_vertical_offset(frame)
    # Add the vertical offset to all joints (only to the y coordinate)
    posture[:, 1] += y_offset

    scatter.set_offsets(posture)
    return scatter,


# Create the animation looping continuously.
anim = FuncAnimation(fig, update, frames=TOTAL_FRAMES, init_func=init,
                     interval=30, blit=True, repeat=True)

# To display the animation, use plt.show().
if __name__ == '__main__':
    plt.show()