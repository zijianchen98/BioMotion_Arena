
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Configuration ---
NUM_FRAMES = 150
FPS = 30

# --- Joint Definitions (for clarity) ---
# These indices map to the rows in the coordinate arrays
HEAD = 0
STERNUM = 1
PELVIS = 2
L_SHOULDER, R_SHOULDER = 3, 4
L_ELBOW, R_ELBOW = 5, 6
L_WRIST, R_WRIST = 7, 8
L_HIP, R_HIP = 9, 10
L_KNEE, R_KNEE = 11, 12
L_ANKLE, R_ANKLE = 13, 14

# --- Keyframe Data ---
# The animation is defined by a series of key poses (keyframes).
# Each keyframe is a (15, 2) numpy array of (x, y) coordinates for the 15 joints.
# The motion is interpolated between these keyframes.

# Keyframe 0: Start (slumped, preparing to roll)
kf0 = np.array([
    [10, 25],    # Head
    [5, 10],     # Sternum
    [0, -10],    # Pelvis
    [0, 10],     # L Shoulder
    [10, 10],    # R Shoulder
    [5, -5],     # L Elbow
    [15, -5],    # R Elbow
    [10, -20],   # L Wrist
    [20, -20],   # R Wrist
    [-10, -10],  # L Hip
    [10, -10],   # R Hip
    [-10, -30],  # L Knee
    [10, -30],   # R Knee
    [-5, -50],   # L Ankle
    [5, -50]     # R Ankle
])

# Keyframe 1: Tucked, hands down, pushing off
kf1 = np.array([
    [20, -35],   # Head
    [10, -25],   # Sternum
    [0, -15],    # Pelvis
    [5, -25],    # L Shoulder
    [15, -25],   # R Shoulder
    [10, -35],   # L Elbow
    [20, -35],   # R Elbow
    [15, -50],   # L Wrist
    [25, -50],   # R Wrist
    [-5, -15],   # L Hip
    [5, -15],    # R Hip
    [0, -30],    # L Knee
    [10, -30],   # R Knee
    [-15, -45],  # L Ankle
    [-5, -45]    # R Ankle
])

# Keyframe 2: Peak of the roll (labored, low arc to represent weight/sadness)
kf2 = np.array([
    [35, -50],   # Head
    [30, -42],   # Sternum
    [38, 5],     # Pelvis
    [25, -40],   # L Shoulder
    [35, -40],   # R Shoulder
    [18, -35],   # L Elbow
    [42, -35],   # R Elbow
    [10, -25],   # L Wrist
    [50, -25],   # R Wrist
    [33, 5],     # L Hip
    [43, 5],     # R Hip
    [30, -10],   # L Knee
    [40, -10],   # R Knee
    [25, -20],   # L Ankle
    [35, -20]    # R Ankle
])

# Keyframe 3: Landing in a seated position
kf3 = np.array([
    [75, -10],   # Head
    [70, -25],   # Sternum
    [70, -45],   # Pelvis
    [65, -25],   # L Shoulder
    [75, -25],   # R Shoulder
    [70, -35],   # L Elbow
    [80, -35],   # R Elbow
    [80, -40],   # L Wrist
    [90, -40],   # R Wrist
    [65, -45],   # L Hip
    [75, -45],   # R Hip
    [80, -48],   # L Knee
    [90, -48],   # R Knee
    [95, -50],   # L Ankle
    [105, -50]   # R Ankle
])

# Keyframe 4: Final slumped resting pose
kf4 = np.array([
    [73, -15],   # Head
    [69, -28],   # Sternum
    [70, -45],   # Pelvis
    [64, -28],   # L Shoulder
    [74, -28],   # R Shoulder
    [69, -38],   # L Elbow
    [79, -38],   # R Elbow
    [78, -42],   # L Wrist
    [88, -42],   # R Wrist
    [65, -45],   # L Hip
    [75, -45],   # R Hip
    [80, -48],   # L Knee
    [90, -48],   # R Knee
    [95, -50],   # L Ankle
    [105, -50]   # R Ankle
])

keyframes = [kf0, kf1, kf2, kf3, kf4]
keyframe_times = np.array([0, 0.25, 0.55, 0.8, 1.0])
keyframe_indices = (keyframe_times * (NUM_FRAMES - 1)).astype(int)

# --- Motion Generation ---
# Interpolate between keyframes to generate all animation frames.
all_frames_data = np.zeros((NUM_FRAMES, 15, 2))

for i in range(len(keyframe_indices) - 1):
    start_frame_idx = keyframe_indices[i]
    end_frame_idx = keyframe_indices[i+1]
    
    start_pose = keyframes[i]
    end_pose = keyframes[i+1]
    
    for frame_idx in range(start_frame_idx, end_frame_idx + 1):
        if end_frame_idx == start_frame_idx:
            t = 1.0
        else:
            t = (frame_idx - start_frame_idx) / (end_frame_idx - start_frame_idx)
        
        # Use cosine interpolation for smooth ease-in and ease-out
        t_smooth = (1 - np.cos(t * np.pi)) / 2
        
        current_pose = start_pose * (1 - t_smooth) + end_pose * t_smooth
        all_frames_data[frame_idx] = current_pose

# --- Animation Setup ---
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Set axis limits to view the entire animation, with some padding
ax.set_xlim(-20, 125)
ax.set_ylim(-70, 45)

ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal', adjustable='box')
plt.tight_layout()

# Create the scatter plot object that will be updated each frame
scatter = ax.scatter([], [], c='white', s=60)

# Initialization function for the animation
def init():
    scatter.set_offsets(np.empty((0, 2)))
    return scatter,

# Update function called for each frame of the animation
def update(frame):
    data = all_frames_data[frame]
    scatter.set_offsets(data)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig,
    update,
    frames=NUM_FRAMES,
    init_func=init,
    blit=True,
    interval=1000/FPS
)

plt.show()
