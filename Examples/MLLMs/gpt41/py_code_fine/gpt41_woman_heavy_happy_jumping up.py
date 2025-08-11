
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 15-point-lights: head, shoulders (2), elbows (2), wrists (2), pelvis, hips (2), knees (2), ankles (2), feet (2)
POINT_LABELS = [
    "head",        # 0
    "l_shoulder",  # 1
    "r_shoulder",  # 2
    "l_elbow",     # 3
    "r_elbow",     # 4
    "l_wrist",     # 5
    "r_wrist",     # 6
    "pelvis",      # 7
    "l_hip",       # 8
    "r_hip",       # 9
    "l_knee",      # 10
    "r_knee",      # 11
    "l_ankle",     # 12
    "r_ankle",     # 13
    "mid_foot"     # 14 (both feet, as in classic figures)
]

# Anthropomorphic proportions (relative units, origin at pelvis)
S = {
    'shoulder': 0.28,
    'hip': 0.18,
    'upper_arm': 0.22,
    'lower_arm': 0.21,
    'upper_leg': 0.23,
    'lower_leg': 0.24,
    'foot': 0.10,
    'head': 0.16
}

def body_posture(phi, jump_prog, arms_up_frac, jump_height, joy_swing):
    # phi: phase within jumping (goes from 0 to 1)
    # jump_prog: for takeoff/land asym (0=start, ~0.6=top, 1=landing)
    # arms_up_frac: [0, 1]: arms above head on takeoff, come down on landing
    y0 = 0  # pelvis vertical origin

    # Simulate heavy weight by more crouch, less jump height, slight lateral foot swing
    heel_spread = 0.19 + 0.02 * np.sin(2 * np.pi * phi)  # heavier: wider stance
    torso_lean = np.clip(0.12*(1 - np.cos(np.pi * phi)), 0, 0.14)  # lean torso a bit on landing

    # Pelvis movement: smooth jump trajectory (parabola + more squat for heavy)
    squat = 0.26 - 0.18 * np.cos(np.pi * phi)    # squat at onset and landing
    pelvis_y = y0 + squat + jump_height * np.sin(np.pi * phi)
    
    # Lateral swing for joy (happy woman): small body oscillation
    swing_x = joy_swing * np.sin(2 * np.pi * phi)

    # Head
    head_x = swing_x
    head_y = pelvis_y + S['head'] + 2*S['shoulder'] + S['upper_arm']*0.1

    # Shoulders (add lean)
    shoulders_y = pelvis_y + S['head'] + S['shoulder']
    l_shoulder_x = -S['shoulder'] + swing_x - torso_lean
    r_shoulder_x =  S['shoulder'] + swing_x - torso_lean

    # Elbows: interpolate between 'arms up' and 'arms down'
    arm_angle_up = np.pi/2 - 0.35  # arms above
    arm_angle_down = 7*np.pi/12    # arms almost down; a little forward swing

    l_arm_angle = arms_up_frac * arm_angle_up + (1 - arms_up_frac) * arm_angle_down
    r_arm_angle = np.pi - l_arm_angle

    l_elbow_x = l_shoulder_x + S['upper_arm']*np.cos(l_arm_angle)
    l_elbow_y = shoulders_y + S['upper_arm']*np.sin(l_arm_angle)
    r_elbow_x = r_shoulder_x + S['upper_arm']*np.cos(r_arm_angle)
    r_elbow_y = shoulders_y + S['upper_arm']*np.sin(r_arm_angle)

    # Wrists: same logic, forearm rotates a bit more
    l_forearm_angle = l_arm_angle + 0.32 * (1-arms_up_frac)
    r_forearm_angle = r_arm_angle - 0.32 * (1-arms_up_frac)
    l_wrist_x = l_elbow_x + S['lower_arm']*np.cos(l_forearm_angle)
    l_wrist_y = l_elbow_y + S['lower_arm']*np.sin(l_forearm_angle)
    r_wrist_x = r_elbow_x + S['lower_arm']*np.cos(r_forearm_angle)
    r_wrist_y = r_elbow_y + S['lower_arm']*np.sin(r_forearm_angle)

    # Pelvis point
    pelvis_x = swing_x - torso_lean
    pelvis = (pelvis_x, pelvis_y)

    # Hips (wider for heavy)
    l_hip_x = pelvis_x - S['hip']*1.15
    r_hip_x = pelvis_x + S['hip']*1.15
    l_hip_y = r_hip_y = pelvis_y

    # Knees:
    # During crouch, knees forward; during push they extend
    knee_forward = 0.13 * (1 - np.cos(np.pi * phi))
    # add some lateral movement on takeoff for heavy/jump joy
    knee_lat_swing = 0.05 * np.sin(2 * np.pi * phi)
    l_knee_x = l_hip_x - 0.07 + knee_lat_swing
    r_knee_x = r_hip_x + 0.07 - knee_lat_swing
    # Upper-leg length mostly vertical in air, more forward on squat
    l_knee_y = pelvis_y - S['upper_leg'] + knee_forward
    r_knee_y = pelvis_y - S['upper_leg'] + knee_forward

    # Ankles: lower leg
    # Go further forward in landing/launch, closer in air
    foot_crouch_fw = 0.11 * (1 - np.cos(np.pi * phi))
    l_ankle_x = l_knee_x - 0.06 + foot_crouch_fw
    r_ankle_x = r_knee_x + 0.06 - foot_crouch_fw
    l_ankle_y = l_knee_y - S['lower_leg']
    r_ankle_y = r_knee_y - S['lower_leg']

    # Feet swing outward for heavy/joy,
    l_foot_x = l_ankle_x - 0.01
    r_foot_x = r_ankle_x + 0.01
    l_foot_y = l_ankle_y - S['foot']*0.5
    r_foot_y = r_ankle_y - S['foot']*0.5
    mid_foot_x = (l_foot_x + r_foot_x)/2
    mid_foot_y = (l_foot_y + r_foot_y)/2

    # Stack into array order
    pts = np.array([
        [head_x, head_y],              # 0: head
        [l_shoulder_x, shoulders_y],   # 1: l_shoulder
        [r_shoulder_x, shoulders_y],   # 2: r_shoulder
        [l_elbow_x, l_elbow_y],        # 3: l_elbow
        [r_elbow_x, r_elbow_y],        # 4: r_elbow
        [l_wrist_x, l_wrist_y],        # 5: l_wrist
        [r_wrist_x, r_wrist_y],        # 6: r_wrist
        [pelvis_x, pelvis_y],          # 7: pelvis
        [l_hip_x, l_hip_y],            # 8: l_hip
        [r_hip_x, r_hip_y],            # 9: r_hip
        [l_knee_x, l_knee_y],          #10: l_knee
        [r_knee_x, r_knee_y],          #11: r_knee
        [l_ankle_x, l_ankle_y],        #12: l_ankle
        [r_ankle_x, r_ankle_y],        #13: r_ankle
        [mid_foot_x, mid_foot_y]       #14: middle of feet
    ])
    return pts

# Animation params
N_FRAMES = 64
FPS = 30
jump_height = 0.26
joy_swing = 0.09

# For smooth takeoff/landing, we use phases so that arms and knees lead body slightly
def frame_pose(t):
    # t: in [0, 1]
    phi = t  # jump phase from 0 to 1
    # Arms up during early phase, lower on landing
    if phi < 0.3:
        arms_up = np.clip(1 - phi/0.3, 0, 1)
    else:
        arms_up = np.clip(1 - (phi-0.3)/0.7, 0, 1) * 0.6
    # Jump: more slow into air, faster landing (asymmetry)
    jump_prog = (np.sin(np.pi*phi - np.pi/2)+1)/2
    return body_posture(phi, jump_prog, arms_up, jump_height, joy_swing)

# Generate all frames at once (for efficient animation)
frames = np.stack([frame_pose(i/(N_FRAMES-1)) for i in range(N_FRAMES)], axis=0)

# Two cycles for smooth loop
loop_frames = np.concatenate([frames, frames[::-1]], axis=0)

# Plot
fig, ax = plt.subplots(figsize=(4, 7), facecolor='black')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_facecolor('black')
ax.axis('off')

scat = ax.scatter([], [], s=38, color='white', edgecolors='none')

# Fix axes so figure matches classic style
ax.set_xlim(-0.6, +0.6)
ax.set_ylim(-0.25, 1.86)
ax.set_aspect('equal')

def init():
    scat.set_offsets(np.zeros((15,2)))
    return scat,

def animate(i):
    pts = loop_frames[i % loop_frames.shape[0]]
    scat.set_offsets(pts)
    return scat,

ani = animation.FuncAnimation(fig, animate, frames=loop_frames.shape[0], interval=1000/FPS, blit=True, init_func=init, repeat=True)

plt.show()
