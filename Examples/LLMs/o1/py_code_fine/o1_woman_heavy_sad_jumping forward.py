import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This program renders a minimalistic 15-point biological motion display
# of a "sad woman (heavy weight) jumping forward" against a black background.
# The points are shown in white. The motion is a simplified approximation
# for demonstration purposes.

# Number of points
NUM_POINTS = 15

# Total frames in the animation
FRAMES = 100

# Time array for normalizing 0 to 1 across the animation
t_vals = np.linspace(0, 1, FRAMES)

# Define a base posture (x, y) for each of 15 joints.
# These coordinates roughly outline a low-energy, somewhat "sad" posture.
# The arrangement is: [head, neck, R_shoulder, R_elbow, R_wrist,
#                      L_shoulder, L_elbow, L_wrist, hip_center,
#                      R_hip, R_knee, R_ankle, L_hip, L_knee, L_ankle]
base_posture = np.array([
    [ 0.0,  1.80],  # Head
    [ 0.0,  1.65],  # Neck
    [ 0.15, 1.60],  # Right shoulder
    [ 0.20, 1.45],  # Right elbow
    [ 0.25, 1.30],  # Right wrist
    [-0.15, 1.60],  # Left shoulder
    [-0.20, 1.45],  # Left elbow
    [-0.25, 1.30],  # Left wrist
    [ 0.0,  1.30],  # Hip center
    [ 0.10, 1.20],  # Right hip
    [ 0.10, 1.05],  # Right knee
    [ 0.10, 0.90],  # Right ankle
    [-0.10, 1.20],  # Left hip
    [-0.10, 1.05],  # Left knee
    [-0.10, 0.90],  # Left ankle
])

# Function to generate an upward/downward parabolic jump factor.
# For t in [0,1], we "take off" around t=0.3 and land around t=0.7.
def jump_height(t):
    # No jump before t=0.3 or after t=0.7
    if t < 0.3 or t > 0.7:
        return 0.0
    # Normalize jump phase between [0,1]
    tj = (t - 0.3) / (0.4)
    # Simple parabola for rise and fall
    return 0.3 * (4 * tj * (1 - tj))

# Generate forward progression in x over time
# She moves from x=0 at t=0 to x=2 at t=1
def forward_offset(t):
    return 2.0 * t

# Build a function that, for each time t, returns positions of all 15 points
def get_positions(t):
    # Copy base posture
    points = base_posture.copy()
    # Let the entire body move forward
    offset_x = forward_offset(t)
    # Let the entire torso (and everything) shift upward by the jump amount
    lift = jump_height(t)

    # Slight forward lean for a "heavy" jump posture
    # We'll tilt the torso about the hip_center
    hip_center = points[8]
    angle = -0.2  # negative angle for leaning forward
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)

    # Rotate torso above the hip_center
    head_to_hip_idxs = [0, 1, 2, 3, 4, 5, 6, 7]
    for idx in head_to_hip_idxs:
        rel = points[idx] - hip_center
        rot = np.array([rel[0]*cos_a - rel[1]*sin_a,
                        rel[0]*sin_a + rel[1]*cos_a])
        points[idx] = hip_center + rot

    # Add forward offset to all x-coordinates
    points[:, 0] += offset_x
    # Add jump lift to all y-coordinates
    points[:, 1] += lift

    # Simulate "heavy" sadness by lowering shoulders slightly over time
    shoulder_drop = 0.05 * t
    for sh_idx in [2, 5]:  # right shoulder, left shoulder
        points[sh_idx, 1] -= shoulder_drop

    return points

# Create figure and axes with black background
fig, ax = plt.subplots(figsize=(5, 5))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1, 4)
ax.set_ylim(0, 2.5)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot for 15 points (in white)
scatter = ax.scatter([], [], c='white', s=30)

# Update function for FuncAnimation
def update(frame):
    t = t_vals[frame]
    pts = get_positions(t)
    scatter.set_offsets(pts)
    return scatter,

ani = FuncAnimation(fig, update, frames=FRAMES, interval=50, blit=True)
plt.show()