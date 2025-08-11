
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 15 joint labels for stickman (standard for biological motion)
JOINTS = [
    'Head',
    'RShoulder', 'LShoulder',
    'RElbow', 'LElbow',
    'RWrist', 'LWrist',
    'Sternum',
    'RHip', 'LHip',
    'RKnee', 'LKnee',
    'RAnkle', 'LAnkle',
    'MidPelvis'
]

# Helper to get joint indices for the stick figure
JOINT_IDX = {name: idx for idx, name in enumerate(JOINTS)}

# Define the stick figure in 'lying down' neutral pose along x (horizontal), with y pointing up.
def lyingdown_pose(t):
    """
    Generates joint positions (N=15, 2) for 'lying down' biological motion.
    Animate gentle 'happy' limb movement and light chest movement.
    t: time in seconds
    """
    # Stickman dimensions (all units in arbitrary screen coords)
    head_r = 12           # head radius
    torso = 42            # distance sternum -> pelvis
    shoulder_w = 30       # shoulder width
    pelvis_w = 24         # pelvis width
    upper_arm = 26
    lower_arm = 24
    thigh = 32
    shank = 28
    foot_off = 10

    # The whole figure is horizontally oriented; center at (cx, cy)
    cx, cy = 0, 0

    # Subtle 'happy' wiggling: arms and legs move up/down/rotate rhythmically
    arm_swing = np.sin(2*np.pi*0.6*t) * np.deg2rad(18)      # + up/forward
    leg_swing = np.sin(2*np.pi*0.6*t + np.pi/2) * np.deg2rad(14)
    chest_breath = np.sin(2*np.pi*0.3*t) * 2.5

    # Joints: (x, y)
    P = np.zeros((15, 2))

    # Spine starts at 'mid pelvis' joint (origin for simplicity)
    P[JOINT_IDX['MidPelvis']] = np.array([cx, cy])

    # Pelvis left/right
    P[JOINT_IDX['RHip']] = np.array([cx + pelvis_w/2, cy])
    P[JOINT_IDX['LHip']] = np.array([cx - pelvis_w/2, cy])

    # Sternum/chest forward & slightly up (for breathing)
    chest_y = cy + torso + chest_breath
    P[JOINT_IDX['Sternum']] = np.array([cx, chest_y])

    # Shoulders left/right from sternum
    P[JOINT_IDX['RShoulder']] = P[JOINT_IDX['Sternum']] + [shoulder_w/2, 0]
    P[JOINT_IDX['LShoulder']] = P[JOINT_IDX['Sternum']] + [-shoulder_w/2, 0]

    # Head, just past sternum ("up")
    P[JOINT_IDX['Head']] = P[JOINT_IDX['Sternum']] + [0, head_r+10]

    # Right arm (from shoulder): animate swinging up/down
    shoulder = P[JOINT_IDX['RShoulder']]
    upper_arm_angle = -np.pi/2 + arm_swing + np.deg2rad(8)
    elbow = shoulder + upper_arm * np.array([np.cos(upper_arm_angle), np.sin(upper_arm_angle)])
    P[JOINT_IDX['RElbow']] = elbow
    elbow_to_wrist_angle = upper_arm_angle + np.deg2rad(18) + np.sin(2*np.pi*0.6*t+0.7)*np.deg2rad(10)
    wrist = elbow + lower_arm * np.array([np.cos(elbow_to_wrist_angle), np.sin(elbow_to_wrist_angle)])
    P[JOINT_IDX['RWrist']] = wrist

    # Left arm
    shoulder = P[JOINT_IDX['LShoulder']]
    upper_arm_angle = -np.pi/2 - arm_swing - np.deg2rad(8)
    elbow = shoulder + upper_arm * np.array([np.cos(upper_arm_angle), np.sin(upper_arm_angle)])
    P[JOINT_IDX['LElbow']] = elbow
    elbow_to_wrist_angle = upper_arm_angle - np.deg2rad(18) + np.sin(2*np.pi*0.6*t+0.5)*np.deg2rad(9)
    wrist = elbow + lower_arm * np.array([np.cos(elbow_to_wrist_angle), np.sin(elbow_to_wrist_angle)])
    P[JOINT_IDX['LWrist']] = wrist

    # Right Leg (from RHip)
    hip = P[JOINT_IDX['RHip']]
    thigh_angle = np.pi/2 - leg_swing - np.deg2rad(7)
    knee = hip + thigh * np.array([np.cos(thigh_angle), np.sin(thigh_angle)])
    P[JOINT_IDX['RKnee']] = knee
    knee_angle = thigh_angle - np.deg2rad(19) + np.sin(2*np.pi*0.5*t+0.2)*np.deg2rad(9)
    ankle = knee + shank * np.array([np.cos(knee_angle), np.sin(knee_angle)])
    P[JOINT_IDX['RAnkle']] = ankle

    # Left Leg (from LHip)
    hip = P[JOINT_IDX['LHip']]
    thigh_angle = np.pi/2 + leg_swing + np.deg2rad(7)
    knee = hip + thigh * np.array([np.cos(thigh_angle), np.sin(thigh_angle)])
    P[JOINT_IDX['LKnee']] = knee
    knee_angle = thigh_angle + np.deg2rad(19) + np.sin(2*np.pi*0.5*t+2.2)*np.deg2rad(8)
    ankle = knee + shank * np.array([np.cos(knee_angle), np.sin(knee_angle)])
    P[JOINT_IDX['LAnkle']] = ankle

    return P

# --- Animation setup ---
fig, ax = plt.subplots(figsize=(4, 2.2))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Plot dots (will update positions)
dots, = ax.plot([], [],
                'o',
                ms=10,
                color='white',
                markeredgecolor='black',
                markeredgewidth=0.6,
                linewidth=0)

def init():
    ax.set_xlim(-75, 75)
    ax.set_ylim(-25, 110)
    dots.set_data([], [])
    return dots,

def animate(frame):
    t = frame / 60.0
    P = lyingdown_pose(t)
    dots.set_data(P[:,0], P[:,1])
    return dots,

ani = FuncAnimation(
    fig, animate, frames=180, interval=1000/60, blit=True, init_func=init
)

plt.show()
