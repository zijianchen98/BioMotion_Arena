
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams

# Body points indices
HEAD, NECK, LSHO, RSHO, LELB, RELB, LWRI, RWRI, TORS, LHIP, RHIP, LKNE, RKNE, LANK, RANK = range(15)

# Key poses for the jump sequence (15 points, each with [x, y])
key_poses = [
    # Standing (initial pose)
    np.array([
        [0.0, 6.0],    # HEAD
        [0.0, 5.0],    # NECK
        [-1.0, 5.0],   # LSHO
        [1.0, 5.0],    # RSHO
        [-1.5, 3.5],   # LELB
        [1.5, 3.5],    # RELB
        [-2.0, 2.0],   # LWRI
        [2.0, 2.0],    # RWRI
        [0.0, 4.0],    # TORS
        [-1.0, 3.0],   # LHIP
        [1.0, 3.0],    # RHIP
        [-1.0, 1.5],   # LKNE
        [1.0, 1.5],    # RKNE
        [-1.0, 0.0],   # LANK
        [1.0, 0.0]     # RANK
    ]),
    # Preparation (squat pose)
    np.array([
        [0.3, 5.3],    # HEAD
        [0.3, 4.3],    # NECK
        [-0.7, 4.3],   # LSHO
        [1.3, 4.3],    # RSHO
        [-1.5, 3.3],   # LELB
        [1.5, 3.3],    # RELB
        [-2.2, 2.2],   # LWRI
        [2.2, 1.8],    # RWRI
        [0.3, 3.3],    # TORS
        [-0.7, 2.0],   # LHIP
        [1.3, 2.0],    # RHIP
        [-0.8, 0.8],   # LKNE
        [0.8, 0.8],    # RKNE
        [-0.8, 0.0],   # LANK
        [0.8, 0.0]     # RANK
    ]),
    # Takeoff (mid-air pose)
    np.array([
        [0.6, 7.0],    # HEAD
        [0.6, 6.0],    # NECK
        [-0.4, 6.0],   # LSHO
        [1.6, 6.0],    # RSHO
        [-1.0, 5.0],   # LELB
        [1.0, 5.0],    # RELB
        [-1.5, 4.0],   # LWRI
        [1.5, 4.0],    # RWRI
        [0.6, 5.0],    # TORS
        [-0.4, 3.5],   # LHIP
        [1.6, 3.5],    # RHIP
        [-0.5, 2.5],   # LKNE
        [0.5, 2.5],    # RKNE
        [-0.5, 1.5],   # LANK
        [0.5, 1.5]     # RANK
    ]),
    # Landing (recovery pose)
    np.array([
        [1.2, 5.5],    # HEAD
        [1.2, 4.5],    # NECK
        [0.2, 4.5],    # LSHO
        [2.2, 4.5],    # RSHO
        [-0.3, 3.0],   # LELB
        [2.7, 3.0],    # RELB
        [-0.8, 2.0],   # LWRI
        [3.2, 2.0],    # RWRI
        [1.2, 3.5],    # TORS
        [0.2, 2.2],    # LHIP
        [2.2, 2.2],    # RHIP
        [0.0, 0.8],    # LKNE
        [1.0, 0.8],    # RKNE
        [0.0, 0.0],    # LANK
        [1.0, 0.0]     # RANK
    ])
]

# Keyframe timing (in seconds)
key_times = np.array([0.0, 0.3, 0.5, 1.2])
total_duration = 1.5  # seconds
fps = 30
total_frames = int(fps * total_duration)

# Precompute all frames using linear interpolation
all_frames = []
for frame in range(total_frames):
    t = frame / fps
    
    # Find current interval between key poses
    for i in range(len(key_times) - 1):
        if key_times[i] <= t <= key_times[i + 1]:
            # Calculate interpolation factor (0 to 1)
            frac = (t - key_times[i]) / (key_times[i + 1] - key_times[i])
            # Linear interpolation between key poses
            pose = key_poses[i] + frac * (key_poses[i + 1] - key_poses[i])
            all_frames.append(pose)
            break
    else:
        # After last keyframe, use the final pose
        all_frames.append(key_poses[-1])

# Configure plot
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['savefig.facecolor'] = 'black'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['grid.color'] = 'white'
plt.rcParams['text.color'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
fig, ax = plt.subplots(figsize=(7, 6), facecolor='black')
ax.set_facecolor('black')
ax.set_xlim(-1, 4)
ax.set_ylim(-0.5, 7.5)
ax.set_aspect('equal')
ax.set_title('Biological Motion: Jumping Forward', color='white', fontsize=14)

# Create plot elements
points, = ax.plot([], [], 'wo', markersize=8, alpha=0.9)

def init():
    points.set_data([], [])
    return points,

def update(frame_num):
    pose = all_frames[frame_num]
    points.set_data(pose[:, 0], pose[:, 1])
    return points,

# Create animation
anim = FuncAnimation(
    fig, update, frames=total_frames,
    init_func=init, blit=True, interval=1000/fps
)

plt.tight_layout()
plt.show()
