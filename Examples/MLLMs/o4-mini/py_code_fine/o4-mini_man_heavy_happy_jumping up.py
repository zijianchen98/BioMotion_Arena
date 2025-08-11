
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Animation parameters
fps = 30                 # frames per second
duration = 5             # seconds
n_frames = fps * duration

# Biological‐motion skeleton: 15 point‐lights
# Order of joints:
# 0 head, 1 neck, 2 left shoulder, 3 right shoulder,
# 4 left elbow, 5 right elbow, 6 left wrist, 7 right wrist,
# 8 torso center, 9 left hip, 10 right hip,
# 11 left knee, 12 right knee, 13 left ankle, 14 right ankle

def skeleton_points(t):
    """
    Compute the 15 joint positions at time t (in seconds).
    Returns an array of shape (15,2).
    """
    # Slow vertical "bounce" to simulate heavy weight / breathing
    bounce = 0.02 * np.sin(2 * np.pi * 0.5 * t)

    # Static torso and hips
    torso_center = np.array([0.0, 0.0 + bounce])
    neck        = np.array([0.0, 1.2 + bounce])
    head        = np.array([0.0, 1.5 + bounce])
    left_sh     = np.array([-0.3, 1.1 + bounce])
    right_sh    = np.array([ 0.3, 1.1 + bounce])
    left_hip    = np.array([-0.2, -1.0])
    right_hip   = np.array([ 0.2, -1.0])

    # Left arm hangs down
    l_upper_len = 0.5
    l_lower_len = 0.5
    left_elbow  = left_sh + np.array([0.0, -l_upper_len])
    left_wrist  = left_elbow + np.array([0.0, -l_lower_len])

    # Right arm waving
    # Upper arm extended horizontally
    r_upper_len = 0.5
    r_lower_len = 0.5
    right_elbow = right_sh + np.array([r_upper_len, 0.0])

    # Forearm swings up/down about the elbow
    # base angle -45° (down-left), amplitude 45°, freq ~1.5Hz
    base_angle = -np.pi / 4
    amp        = np.pi / 4
    freq       = 1.5
    phi = base_angle + amp * np.sin(2 * np.pi * freq * t)

    right_wrist = right_elbow + r_lower_len * np.array([np.cos(phi), np.sin(phi)])

    # Legs: static, straight down
    thigh_len = 0.7
    calf_len  = 0.7
    left_knee   = left_hip  + np.array([0.0, -thigh_len])
    left_ankle  = left_knee + np.array([0.0, -calf_len])
    right_knee  = right_hip + np.array([0.0, -thigh_len])
    right_ankle = right_knee + np.array([0.0, -calf_len])

    # Collect all points in correct order
    pts = np.vstack([
        head,         # 0
        neck,         # 1
        left_sh,      # 2
        right_sh,     # 3
        left_elbow,   # 4
        right_elbow,  # 5
        left_wrist,   # 6
        right_wrist,  # 7
        torso_center, # 8
        left_hip,     # 9
        right_hip,    # 10
        left_knee,    # 11
        right_knee,   # 12
        left_ankle,   # 13
        right_ankle   # 14
    ])
    return pts

# Set up the figure and scatter plot
fig, ax = plt.subplots(figsize=(5,8))
ax.set_facecolor('black')
scat = ax.scatter([], [], s=100, c='white')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.6, 1.6)
ax.axis('off')
ax.set_aspect('equal', 'box')

# Animation update function
def update(frame):
    t = frame / fps
    pts = skeleton_points(t)
    scat.set_offsets(pts)
    return scat,

# Create and run the animation
ani = animation.FuncAnimation(
    fig, update, frames=n_frames, interval=1000/fps, blit=True
)

plt.show()
