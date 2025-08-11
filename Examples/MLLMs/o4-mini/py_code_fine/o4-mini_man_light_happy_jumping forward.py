
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define base joint positions (in a frontal view) for a 15‐point skeleton
base_joints = np.array([
    (0.00, 2.00),   #  0 head
    (0.00, 1.80),   #  1 neck
    (-0.25, 1.70),  #  2 left shoulder
    ( 0.25, 1.70),  #  3 right shoulder
    (-0.40, 1.40),  #  4 left elbow
    ( 0.40, 1.40),  #  5 right elbow
    (-0.40, 1.00),  #  6 left wrist
    ( 0.40, 1.00),  #  7 right wrist
    ( 0.00, 1.00),  #  8 pelvis (root)
    (-0.20, 1.00),  #  9 left hip
    ( 0.20, 1.00),  # 10 right hip
    (-0.20, 0.60),  # 11 left knee
    ( 0.20, 0.60),  # 12 right knee
    (-0.20, 0.20),  # 13 left ankle
    ( 0.20, 0.20),  # 14 right ankle
])

# Animation parameters
fps = 20
crouch_frames = 20
jump_frames = 40
stand_frames = 20
total_frames = crouch_frames + jump_frames + stand_frames

squat_depth = 0.20     # how deep the crouch is
jump_height = 0.60     # how high the center of mass moves

# Precompute vertical offsets for each frame
y_offsets = np.zeros(total_frames)

# 1) Crouch phase (lower the body)
for t in range(crouch_frames):
    c = t / (crouch_frames - 1)
    # half‐cosine for smooth start/end
    squat = 0.5 * (1 - np.cos(np.pi * c))
    y_offsets[t] = -squat_depth * squat

# 2) Jump phase (push off, flight, landing)
for t in range(jump_frames):
    u = t / (jump_frames - 1)
    # half‐sine: start/end at 0, peak at mid‐flight
    y_offsets[crouch_frames + t] = jump_height * np.sin(np.pi * u)

# 3) Stand‐up phase (recover from landing crouch)
for t in range(stand_frames):
    v = t / (stand_frames - 1)
    # half‐cosine to lift from squat to upright
    stand = 0.5 * (1 - np.cos(np.pi * v))
    # start at -squat_depth, go back to 0
    y_offsets[crouch_frames + jump_frames + t] = -squat_depth * (1 - stand)

# Set up the figure
fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2.5)
ax.axis('off')

# Initialize scatter for the 15 points
scatter = ax.scatter(
    base_joints[:, 0],
    base_joints[:, 1],
    color='white',
    s=50
)

def update(frame):
    """
    Update function for each animation frame.
    Applies the precomputed vertical offset to all joints.
    """
    y_off = y_offsets[frame]
    coords = base_joints + np.array([0, y_off])
    scatter.set_offsets(coords)
    return scatter,

# Create the animation
anim = FuncAnimation(
    fig,
    update,
    frames=total_frames,
    interval=1000 / fps,
    blit=True,
    repeat=True
)

plt.show()
