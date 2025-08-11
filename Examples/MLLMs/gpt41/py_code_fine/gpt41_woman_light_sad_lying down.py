
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 15 point-lights: head, shoulders(2), elbows(2), wrists(2), hips(2), knees(2), ankles(2), chest
JOINT_NAMES = [
    'head',        # 0
    'l_shoulder',  # 1 
    'r_shoulder',  # 2 
    'l_elbow',     # 3 
    'r_elbow',     # 4 
    'l_wrist',     # 5 
    'r_wrist',     # 6 
    'chest',       # 7 
    'l_hip',       # 8 
    'r_hip',       # 9 
    'l_knee',      # 10 
    'r_knee',      # 11 
    'l_ankle',     # 12 
    'r_ankle',     # 13 
    'pelvis'       # 14
]

# "lying down" -- horizontal orientation, knees slightly bent, arms at sides, slight head slump, overall 'sad' gesture indicated.
# We'll define a skeleton in a canonical position, then animate a gentle breathing,
# sad pose (head slumped, one arm/hands curled towards head), and subtle foot movement.

# Define canonical positions (in 2D, horizontal)
# Units: arbitrary, but assume about 1.7 "tall", origin at pelvis (~middle)
BASE_POSE = np.array([
    [ 0.8,  0.0],   #  0 head
    [ 0.5,  0.2],   #  1 l_shoulder
    [ 0.5, -0.2],   #  2 r_shoulder
    [ 0.1,  0.25],  #  3 l_elbow
    [ 0.1, -0.25],  #  4 r_elbow
    [-0.4,  0.3],   #  5 l_wrist
    [-0.4, -0.3],   #  6 r_wrist
    [ 0.6,  0.0],   #  7 chest
    [ 0.4,  0.13],  #  8 l_hip
    [ 0.4, -0.13],  #  9 r_hip
    [ 0.0,  0.18],  # 10 l_knee
    [ 0.0, -0.18],  # 11 r_knee
    [-0.5,  0.23],  # 12 l_ankle
    [-0.5, -0.23],  # 13 r_ankle
    [ 0.4,  0.0]    # 14 pelvis
])

# We will horizontally flip so the body is lying left to right in image.
# Final pose will be formed as: [y, z] => [x, y]

def animate_pose(t):
    pose = np.copy(BASE_POSE)
    # Parameters for subtle animation
    # Breathing: chest and shoulders move up/down sinusoidally
    breath_amp = 0.03
    chest_offset = breath_amp * np.sin(2*np.pi*t/90)
    pose[1,1] += chest_offset  # l_shoulder
    pose[2,1] += chest_offset  # r_shoulder
    pose[7,1] += chest_offset  # chest

    # Sad head slump: slowly drop head, subtle head shake
    head_drop = 0.10 + 0.02 * np.sin(2*np.pi*t/120)
    head_shift = -0.04 + 0.01 * np.cos(2*np.pi*t/60)
    pose[0] += [head_drop, head_shift]
    
    # Curl in left wrist towards head (sad, dejected gesture)
    lw_curl = 0.15 * np.sin(2*np.pi*t/120)
    pose[5] += [lw_curl*0.5, -lw_curl*0.2]  

    # Curl right wrist a little to body
    rw_curl = 0.07 * np.sin(2*np.pi*t/90 + 1)
    pose[6] += [rw_curl*0.3, -rw_curl*0.2]

    # Subtle knee/ankle fidget
    k_f = 0.01 * np.sin(2*np.pi*t/50)
    pose[10,1] += k_f  # l_knee
    pose[11,1] -= k_f # r_knee
    pose[12,1] += 4*k_f # l_ankle
    pose[13,1] -= 4*k_f # r_ankle

    # 'Sadness': slightly round back, pull knees up a bit, tilt pelvis
    pose[10,0] += 0.03 * np.sin(2*np.pi*t/160 + 1)
    pose[11,0] += 0.03 * np.sin(2*np.pi*t/160 - 1)
    pose[8,0]  += 0.01 * np.sin(2*np.pi*t/160 + 1)
    pose[9,0]  += 0.01 * np.sin(2*np.pi*t/160 - 1)

    # Format for plotting: lying "left-right" in the figure
    # (swap axes so major body is horizontal, legs to left, head to right)
    # [-Y, X]
    X = -pose[:,1]
    Y = pose[:,0]
    
    # Shift/scale for centering in window
    X = X - np.mean(X)
    Y = Y - np.mean(Y)
    return X, Y

# Figure setup
fig, ax = plt.subplots(figsize=(5, 3))
ax.set_facecolor('black')
plt.axis('off')
margin = 0.18
ax.set_xlim(-0.7-margin, +0.8+margin)
ax.set_ylim(-0.5-margin, +0.5+margin)

# Animation function
scatter = ax.scatter([], [], s=70, c='white')

def update(frame):
    X, Y = animate_pose(frame)
    scatter.set_offsets(np.c_[X, Y])
    return scatter,

# Optionally: fix aspect ratio
ax.set_aspect('equal')

ani = FuncAnimation(fig, update, frames=180, interval=33, blit=True)
plt.show()
