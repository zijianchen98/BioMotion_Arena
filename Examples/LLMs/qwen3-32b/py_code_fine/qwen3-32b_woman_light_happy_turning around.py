
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Define joint positions relative to the body (in arbitrary units)
# These are approximate joint positions for a human turning around
# The joints are labeled for clarity: head, neck, spine, pelvis, left/right shoulder, left/right elbow,
# left/right hand, left/right hip, left/right knee, left/right foot

joint_names = [
    "head", "neck", "spine", "pelvis",
    "left_shoulder", "right_shoulder",
    "left_elbow", "right_elbow",
    "left_hand", "right_hand",
    "left_hip", "right_hip",
    "left_knee", "right_knee",
    "left_foot", "right_foot"
]

# Initial positions of the joints (relative to the center of the body)
initial_positions = np.array([
    [0, 10],  # head
    [0, 8],   # neck
    [0, 5],   # spine
    [0, 2],   # pelvis
    [-2, 5],  # left_shoulder
    [2, 5],   # right_shoulder
    [-4, 3],  # left_elbow
    [4, 3],   # right_elbow
    [-6, 2],  # left_hand
    [6, 2],   # right_hand
    [-2, 1],  # left_hip
    [2, 1],   # right_hip
    [-2, -2], # left_knee
    [2, -2],  # right_knee
    [-2, -5], # left_foot
    [2, -5],  # right_foot
], dtype=np.float32)

# Number of frames for the animation
num_frames = 120

# Generate the motion: turning around (rotating the body)
# We simulate a smooth rotation of the entire body over time
def rotate_point(point, angle, center):
    """Rotate a point around a center by a given angle (in radians)."""
    translated = point - center
    rotated = np.array([
        translated[0] * math.cos(angle) - translated[1] * math.sin(angle),
        translated[0] * math.sin(angle) + translated[1] * math.cos(angle)
    ])
    return rotated + center

# Create a rotation from 0 to 2*pi radians (full circle) over the animation
rotation_angles = np.linspace(0, 2 * math.pi, num_frames)

# Store all joint positions for each frame
positions = []

for angle in rotation_angles:
    # Rotate each joint around the pelvis (which is at [0, 2])
    rotated = np.array([rotate_point(pos, angle, [0, 2]) for pos in initial_positions])
    positions.append(rotated)

# Convert to numpy array for easier indexing
positions = np.array(positions)

# Set up the figure and axis for the animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.axis('off')

# Create scatter plot for the joints (white points)
scat = ax.scatter([], [], color='white', s=100)

# Animation function
def update(frame):
    scat.set_offsets(positions[frame])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
