
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define stick figure joint layout with 15 markers
joint_names = [
    "Head",         # 0
    "Neck",         # 1
    "RShoulder",    # 2
    "LShoulder",    # 3
    "RElbow",       # 4
    "LElbow",       # 5
    "RWrist",       # 6
    "LWrist",       # 7
    "Chest",        # 8
    "MidHip",       # 9
    "RHip",         # 10
    "LHip",         # 11
    "RKnee",        # 12
    "LKnee",        # 13
    "RAnkle",       # 14
    "LAnkle",       # 15
]

# Generate a sad jumping up motion for a lightweight woman
# Define key pose parameters
n_frames = 60
t = np.linspace(0, 1, n_frames)

# Body proportions (in arbitrary units)
head_h = 0.18
neck_h = 0.09
shoulder_w = 0.20
torso_h = 0.25
hip_w = 0.16
pelvis_h = 0.1
leg_h = 0.43
arm_h = 0.26

# Sagittal plane (side view): y=vertical, x=front-to-back
# We'll use x ~ 0 for most joints (very little forward movement), simulating a sagittal view
# The woman looks sad: head and shoulders droop forward, wrists limp down

def get_pose(frame):
    # t is in [0, 1]
    jump_cycle = np.sin(np.pi * frame) # 0 at rest; 1 at top of jump; 0 down
    jump_height = 0.23 * jump_cycle  # Max jump height
    feet_sep = 0.08 + 0.01*np.cos(2*np.pi*frame)
    hip_drop = 0.04 * (1-jump_cycle)
    
    # Head and body lean and droop to suggest sadness
    droop = 0.13 + 0.10 * (1-jump_cycle)   # max droop when not jumping
    # Shoulder slump and wrist lump
    shoulder_droop = 0.12 + 0.05 * (1-jump_cycle)
    arm_sag = 0.15 + 0.15*(1-jump_cycle)
    wrist_sag = 0.07 + 0.05*(1-jump_cycle)
    
    # Central reference vertical position (lowest at bottom, highest at jump apex)
    y_root = 0.30 + jump_height - hip_drop
    x_root = 0.0

    # Pelvis, chest, and neck positions
    mid_hip = np.array([x_root, y_root])
    chest = mid_hip + np.array([0, pelvis_h + torso_h])
    neck = chest + np.array([0, neck_h])
    head = neck + np.array([0, head_h])
    
    # Head drooping forward ("sad" lean)
    head = head + np.array([ -droop, 0 ])
    # Shoulders
    RShoulder = chest + np.array([shoulder_w/2, 0]) + np.array([ -shoulder_droop, -shoulder_droop*0.22 ])
    LShoulder = chest + np.array([-shoulder_w/2, 0]) + np.array([ -shoulder_droop, -shoulder_droop*0.22 ])
    
    # Hips
    RHip = mid_hip + np.array([ hip_w/2, 0 ])
    LHip = mid_hip + np.array([-hip_w/2, 0 ])
    
    # Elbows
    RElbow = RShoulder + np.array([ 0.01, -arm_h*0.62 ])
    LElbow = LShoulder + np.array([ 0.01, -arm_h*0.62 ])
    # Wrists limp downward + forward
    RWrist = RElbow + np.array([ -arm_sag, -arm_h*0.45 - wrist_sag ])
    LWrist = LElbow + np.array([ -arm_sag, -arm_h*0.45 - wrist_sag ])
    
    # Knees
    RKnee = RHip + np.array([ -0.02, -leg_h*0.52 + 0.03*jump_cycle ])
    LKnee = LHip + np.array([ 0.02, -leg_h*0.52 + 0.03*jump_cycle ])
    # Ankles (feet)
    RAnkle = RKnee + np.array([ 0.0, -leg_h*0.48 ])
    LAnkle = LKnee + np.array([ 0.0, -leg_h*0.48 ])
    # Feet spread slightly outward on landing and take-off
    RAnkle = RAnkle + np.array([feet_sep, 0])
    LAnkle = LAnkle + np.array([-feet_sep, 0])
    
    # Assemble positions (order: head, neck, RSh, LSh, REl, LEl, RW, LW, chest, midhip, RHip, LHip, RKnee, LKnee, RAnkle, LAnkle) - 16 markers
    # But question wants 15. We'll drop the midhip, merge feet
    pose = [
        head,
        neck,
        RShoulder,
        LShoulder,
        RElbow,
        LElbow,
        RWrist,
        LWrist,
        chest,
        #mid_hip,
        RHip,
        LHip,
        RKnee,
        LKnee,
        RAnkle,
        LAnkle,
    ]
    pose = np.array(pose)
    return pose

# Create the animation
fig, ax = plt.subplots(figsize=(4, 8))
ax.set_facecolor("black")
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0, 1.1)
plt.axis('off')

points, = plt.plot([], [], 'o', color='white', markersize=9)

# For subtlety, keep points as white dots, no lines

def init():
    points.set_data([], [])
    return points,

def animate(i):
    frame_idx = i % n_frames
    phase = t[frame_idx]
    pose = get_pose(phase)
    x, y = pose[:,0], pose[:,1]
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(
    fig, animate, frames=n_frames, interval=40, blit=True, init_func=init)

plt.show()
