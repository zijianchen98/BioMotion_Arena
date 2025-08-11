
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the 15 skeletal points in a standing posture (x, y)
# Order: head, neck, l_shoulder, r_shoulder, l_elbow, r_elbow,
#        l_wrist, r_wrist, torso, l_hip, r_hip, l_knee,
#        r_knee, l_ankle, r_ankle
stand_pos = np.array([
    [0.00, 1.75],  # head
    [0.00, 1.60],  # neck
    [-0.20, 1.50], # l_shoulder
    [ 0.20, 1.50], # r_shoulder
    [-0.50, 1.20], # l_elbow
    [ 0.50, 1.20], # r_elbow
    [-0.70, 0.90], # l_wrist
    [ 0.70, 0.90], # r_wrist
    [0.00, 1.00],  # torso (hip base)
    [-0.20, 1.00], # l_hip
    [ 0.20, 1.00], # r_hip
    [-0.20, 0.50], # l_knee
    [ 0.20, 0.50], # r_knee
    [-0.20, 0.00], # l_ankle
    [ 0.20, 0.00], # r_ankle
])

# Relative positions for the tucked posture (centered at the COM)
tuck_rel = np.array([
    [ 0.00,  0.80],  # head
    [ 0.00,  0.90],  # neck
    [-0.20,  1.00],  # l_shoulder
    [ 0.20,  1.00],  # r_shoulder
    [-0.10,  1.15],  # l_elbow
    [ 0.10,  1.15],  # r_elbow
    [-0.05,  1.20],  # l_wrist
    [ 0.05,  1.20],  # r_wrist
    [ 0.00,  1.00],  # torso (COM)
    [-0.10,  1.00],  # l_hip
    [ 0.10,  1.00],  # r_hip
    [-0.15,  1.20],  # l_knee
    [ 0.15,  1.20],  # r_knee
    [-0.10,  1.10],  # l_ankle
    [ 0.10,  1.10],  # r_ankle
])

# Indices
TORso_IDX = 8  # index of the torso point

# Animation parameters
fps = 30
t1 = 1.0  # seconds to go from stand to tuck
t2 = 2.0  # seconds for the roll
t3 = 1.0  # seconds to go from tuck back to stand
n1 = int(fps * t1)
n2 = int(fps * t2)
n3 = int(fps * t3)
total_frames = n1 + n2 + n3

# Precompute the COM in standing posture
com_stand = stand_pos[TORso_IDX]

# Precompute absolute tuck positions (at the same COM location as stand)
tuck_abs = tuck_rel + com_stand

# Pre-allocate the full animation array
# shape = (total_frames, 15 points, 2 coordinates)
frames = np.zeros((total_frames, 15, 2), dtype=float)

# Phase 1: Stand -> Tuck
for i in range(n1):
    alpha = (i + 1) / n1
    frames[i] = (1 - alpha) * stand_pos + alpha * tuck_abs

# Phase 2: Forward roll (rotate and translate)
roll_distance = 2.0  # total x-translation during roll
for i in range(n2):
    angle = 2 * np.pi * (i / n2)
    # Rotation matrix
    R = np.array([[ np.cos(angle), -np.sin(angle)],
                  [ np.sin(angle),  np.cos(angle)]])
    # Moving COM along x
    com_x = com_stand[0] + roll_distance * (i / n2)
    com_y = com_stand[1]
    com = np.array([com_x, com_y])
    # Rotate each relative tuck point and then translate
    rotated = (R @ (tuck_rel.T)).T
    frames[n1 + i] = rotated + com

# Phase 3: Tuck -> Stand
for i in range(n3):
    beta = (i + 1) / n3
    start = tuck_abs
    end = stand_pos
    frames[n1 + n2 + i] = (1 - beta) * start + beta * end

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.axis('off')
ax.set_aspect('equal', 'box')
ax.set_xlim(-1, com_stand[0] + roll_distance + 1)
ax.set_ylim(-0.5, 2.0)

# Initial scatter
scatter = ax.scatter([], [], s=50, c='white')

# Animation update function
def update(frame_idx):
    pts = frames[frame_idx]
    scatter.set_offsets(pts)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

plt.show()
