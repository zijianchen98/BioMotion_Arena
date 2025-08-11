
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 points (happyman walker model)
#   0: Head
#   1,2: L, R Shoulder
#   3,4: L, R Elbow
#   5,6: L, R Wrist
#   7,8: L, R Hip
#   9,10: L, R Knee
#   11,12: L, R Ankle
#   13,14: L, R Foot

# Skeleton connections (for structure, but we show only points)
POINTS = [
    "Head",               # 0
    "LShoulder", "RShoulder",  # 1,2
    "LElbow", "RElbow",        # 3,4
    "LWrist", "RWrist",        # 5,6
    "LHip", "RHip",            # 7,8
    "LKnee", "RKnee",          # 9,10
    "LAnkle", "RAnkle",        # 11,12
    "LFoot", "RFoot"           # 13,14
]

# Body parameters (2D, standing upright at center)
# Units arbitrary, positions chosen for plausible proportions
def base_pose():
    #           X,   Y
    return np.array([
        [ 0.0,  8.0],   # 0: Head
        [-1.0,  7.0],   # 1: LShoulder
        [ 1.0,  7.0],   # 2: RShoulder
        [-1.5,  6.0],   # 3: LElbow
        [ 1.5,  6.0],   # 4: RElbow
        [-1.5,  5.0],   # 5: LWrist
        [ 1.5,  5.0],   # 6: RWrist
        [-0.7,  4.0],   # 7: LHip
        [ 0.7,  4.0],   # 8: RHip
        [-0.9,  2.0],   # 9: LKnee
        [ 0.9,  2.0],   # 10: RKnee
        [-1.0,  0.6],   # 11: LAnkle
        [ 1.0,  0.6],   # 12: RAnkle
        [-1.0,  0.0],   # 13: LFoot
        [ 1.0,  0.0],   # 14: RFoot
    ])

# Animation parameters
FPS = 60
WALK_CYCLE_FRAMES = 60  # 1 second per stride

def get_pose_in_walk(phase):
    """
    phase: float, phase of walk cycle (0 ... 2*pi)
    Returns: (15,2) ndarray pose of all points
    """
    pose = base_pose().copy()
    # Arms swing: opposite to legs
    # Legs swing centered at hip, knees and feet move sinusoidally

    # Amplitudes
    shoulder_swing = 0.8
    elbow_swing = 1.2
    wrist_swing = 1.7
    hip_swing = 0.6
    knee_amp = 1.2
    ankle_amp_y = 0.7
    foot_rise = 0.5
    ank_amp_x = 0.5

    # Leg phases
    # Left leg phase = 0, right leg = pi (opposite)
    ph_L = phase
    ph_R = phase + np.pi

    # Arms: left forward when right foot moves back (ph_L ~ pi, ph_R ~ 0)
    arm_ph_L = phase + np.pi
    arm_ph_R = phase

    # --- Arms/Shoulders ---
    # Shoulders (pivot in y, swing in x)
    pose[1,0] = -1.0 + shoulder_swing * np.sin(arm_ph_L)   # LShoulder x
    pose[2,0] =  1.0 + shoulder_swing * np.sin(arm_ph_R)   # RShoulder x
    # Elbows
    pose[3,0] = -1.5 + elbow_swing * np.sin(arm_ph_L)
    pose[4,0] =  1.5 + elbow_swing * np.sin(arm_ph_R)
    # Wrists
    pose[5,0] = -1.5 + wrist_swing * np.sin(arm_ph_L)
    pose[6,0] =  1.5 + wrist_swing * np.sin(arm_ph_R)

    # Keep y positions connected naturally (upper arm, forearm segments)
    pose[3,1] = 6.0 -   0.4*np.cos(arm_ph_L)
    pose[4,1] = 6.0 -   0.4*np.cos(arm_ph_R)
    pose[5,1] = 5.0 -   0.6*np.cos(arm_ph_L)
    pose[6,1] = 5.0 -   0.6*np.cos(arm_ph_R)

    # --- Hips (slight sway) ---
    hip_sway = hip_swing * np.sin(phase)
    pose[7,0] = -0.7 + hip_sway
    pose[8,0] =  0.7 + hip_sway

    # --- Legs ---
    def leg_anim(j, side):
        # j = [hip_idx, knee_idx, ankle_idx, foot_idx]
        # side = +1 (R), -1 (L)
        if side == -1:
            ph = ph_L
        else:
            ph = ph_R
        # Thigh swing: swing in x
        pose[j[1],0] = pose[j[0],0] + knee_amp * np.sin(ph)
        pose[j[1],1] = 2.0 + 1.1 * np.abs(np.sin(ph))    # knee y
        # Ankle: swings, lifts off when swinging forward
        pose[j[2],0] = pose[j[1],0] + ank_amp_x * np.sin(ph)
        foot_lift = foot_rise * np.maximum(0, np.sin(ph))
        pose[j[2],1] = 0.6 + foot_lift
        # Foot: follows ankle with offset (length of foot: ~0.3)
        pose[j[3],0] = pose[j[2],0]
        pose[j[3],1] = pose[j[2],1] - 0.3

    # Left leg: [hip_idx, knee_idx, ankle_idx, foot_idx]
    leg_anim([7, 9, 11, 13], side=-1)
    # Right leg
    leg_anim([8,10,12,14], side=+1)

    # Center the walker horizontally
    COM_x = (pose[7,0] + pose[8,0] + pose[0,0])/3
    pose[:,0] -= COM_x

    # Vertical bob (head, shoulders up/down): z-bounce at double stride frequency, classic walk
    bob_y = 0.12 * np.cos(2*phase)
    pose[:,1] += bob_y

    return pose

# --- Matplotlib animation setup ---
fig, ax = plt.subplots(figsize=(3.5, 6))
ax.set_facecolor('black')
ax.axis('equal')
ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-1.0, 9.0)
ax.axis('off')
sc = ax.scatter([], [], s=60, c='white', edgecolors='none')

# Animation function
def init():
    sc.set_offsets(np.zeros((15,2)))
    return (sc,)

def animate(i):
    phase = 2 * np.pi * (i % WALK_CYCLE_FRAMES) / WALK_CYCLE_FRAMES
    pose = get_pose_in_walk(phase)
    # Slowly move forward in x for demo
    shift_x = 3.5 * ((i/WALK_CYCLE_FRAMES) % 1.0) - 1.3
    pose[:,0] += shift_x
    sc.set_offsets(pose)
    return (sc,)

ani = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=5*WALK_CYCLE_FRAMES, interval=1000/FPS, blit=True
)

plt.show()
