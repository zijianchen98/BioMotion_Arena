
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 15-point biological motion marker labels
JOINTS = [
    "Head",                 # 0
    "Right Shoulder",       # 1
    "Left Shoulder",        # 2
    "Right Elbow",          # 3
    "Left Elbow",           # 4
    "Right Wrist",          # 5
    "Left Wrist",           # 6
    "Chest",                # 7
    "Pelvis",               # 8
    "Right Hip",            # 9
    "Left Hip",             # 10
    "Right Knee",           # 11
    "Left Knee",            # 12
    "Right Ankle",          # 13
    "Left Ankle"            # 14
]

# BODY SEGMENTS (for plausibility, not displayed)
BONES = [
    (0,1), (0,2),      # head to shoulders
    (1,3),(3,5),       # right arm
    (2,4),(4,6),       # left arm
    (1,7),(2,7),(7,8), # trunk
    (8,9),(8,10),      # pelvis to hips
    (9,11),(11,13),    # right leg
    (10,12),(12,14)    # left leg
]

# Base "lying down" pose (side-view, woman on right side, right arm closer)
# Coordinates: (X, Y) in arbitrary units (lying along the X axis; Y is up)
# Proportions for an adult woman, light build
POSE = np.array([
    [0.0,  0.7],  # 0: head (center)
    [0.2,  0.65], # 1: right shoulder (closer to camera)
    [-0.2, 0.64], # 2: left shoulder (further from camera)
    [0.35, 0.50], # 3: right elbow
    [-0.30,0.52], # 4: left elbow
    [0.45, 0.30], # 5: right wrist
    [-0.35,0.34], # 6: left wrist
    [0.0,  0.60], # 7: chest
    [0.0,  0.35], # 8: pelvis
    [0.15, 0.33], # 9: right hip
    [-0.15,0.33], #10: left hip
    [0.18, 0.15], #11: right knee
    [-0.15,0.17], #12: left knee
    [0.18,-0.10], #13: right ankle (on ground)
    [-0.15,-0.08] #14: left ankle (on ground)
])

# Parameters for plausible happy, "lying down" micro-motions (subtle breathing, idle)
def animate_pose(t):
    """Returns 15x2 array, X,Y at time t (seconds)"""
    # Base pose (copy so we don't alter the static base)
    P = np.copy(POSE)
    # Add breathing motion (rib cage and shoulder oscillate up and down)
    breath = 0.01 * np.sin(2*np.pi*t/2.5)
    P[7,1] += breath * 2    # chest
    P[1,1] += breath        # right shoulder
    P[2,1] += breath        # left shoulder
    P[0,1] += breath / 2    # head
    # Gentle arm movement (wiggle right wrist as if playing with fingers)
    right_arm_angle = 0.06 * np.sin(2 * np.pi * t / 2.0)
    R = np.array([[np.cos(right_arm_angle), -np.sin(right_arm_angle)],
                  [np.sin(right_arm_angle),  np.cos(right_arm_angle)]])
    # Shoulder->elbow->wrist: joint at shoulder [1], full chain
    rel_elbow = P[3] - P[1]
    rel_wrist = P[5] - P[3]
    rel_elbow = R @ rel_elbow
    rel_wrist = R @ rel_wrist
    P[3] = P[1] + rel_elbow
    P[5] = P[3] + rel_wrist
    # Happy emotion: subtle head tilt and smile "nod"
    head_angle = 0.04 * np.sin(2*np.pi*t/2.7)
    head_R = np.array([[np.cos(head_angle), -np.sin(head_angle)],
                       [np.sin(head_angle),  np.cos(head_angle)]])
    P[0] = P[7] + head_R @ (P[0] - P[7])
    # Happy micro-fidget in legs (kick ankle forward a few mm)
    left_ankle_push = 0.012 * np.sin(2*np.pi*t/3)
    P[14,0] -= left_ankle_push
    # Small up/down movement of pelvis for breathing
    P[8,1] += breath/3
    # Whole body (woman is light, so a bit "springy") rises and falls
    base_osc = 0.006 * np.sin(2*np.pi*t/3.4)
    P[:,1] += base_osc
    return P

# Animation setup
fig, ax = plt.subplots(figsize=(4, 6))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_facecolor('black')
ax.set_aspect('equal')
# Logical coordinates (X, Y). Give enough space so nothing goes out.
ax.set_xlim(-0.5, 0.6)
ax.set_ylim(-0.2, 0.85)
ax.axis('off')

# Draw dots only (not lines)
dots, = ax.plot([],[], 'wo', ms=10)

def init():
    dots.set_data([], [])
    return dots,

def update(frame):
    t = frame/30.0  # 30 FPS assumed
    pts = animate_pose(t)
    # Shift right so "lying down" is left-to-right on screen (woman facing us)
    offset = np.array([0.35, 0.1])
    pts_disp = pts + offset
    dots.set_data(pts_disp[:,0], pts_disp[:,1])
    return dots,

ani = animation.FuncAnimation(
    fig, update, init_func=init, frames=180, interval=33, blit=True
)

plt.show()
