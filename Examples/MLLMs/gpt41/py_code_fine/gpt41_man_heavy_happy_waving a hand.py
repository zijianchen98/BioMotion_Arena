
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Body joint keypoints (BML walker order, 15 points):
# 0: Head/top, 1: RShoulder, 2: LShoulder, 3: RElbow, 4: LElbow, 5: RWrist, 6: LWrist,
# 7: Hip, 8: RHip, 9: LHip, 10: RKnee, 11: LKnee, 12: RAnkle, 13: LAnkle, 14: Spine

# Skeleton structure for biomechanical plausibility
def get_skeleton():
    return [
        (0, 1), (0, 2),                   # Head - shoulders
        (1, 3), (3, 5),                   # RShoulder - RElbow - RWrist
        (2, 4), (4, 6),                   # LShoulder - LElbow - LWrist
        (1, 7), (2, 7),                   # Shoulders to hip
        (7, 8), (7, 9),                   # Hip to right/left hip
        (8, 10), (10, 12),                # RHip - RKnee - RAnkle
        (9, 11), (11, 13),                # LHip - LKnee - LAnkle
        (7, 14)                           # Hip to spine
    ]

# Segment lengths (roughly normalized)
L = {
    'head_neck': 0.13,  # top of head to neck
    'shoulder': 0.17,   # neck to shoulder joint
    'upper_arm': 0.18,
    'forearm': 0.17,
    'torso': 0.24,      # neck to hip
    'hip_offset': 0.11, # hip joint separation
    'upper_leg': 0.22,
    'lower_leg': 0.22,
    'spine': 0.07
}

def get_pose(t):
    """Compute the 2D joint locations at time t for the heavy waver.

    Returns: ndarray shape (15, 2)
    """
    # Y axis: down is positive. Centered at (0,0)

    # Waving params
    wave_period = 1.1  # seconds (full cycles)
    wave_freq = 2 * np.pi / wave_period
    amp = np.deg2rad(45) # amplitude for arm waving
    heavy_amp_mod = 0.7  # reduce leg movement, emphasize upper body
    head_bounce = 0.03 * np.sin(2*wave_freq*t)
    # Body center (pelvis)
    cx = 0
    cy = 0

    # Hips
    hip_sep = L['hip_offset']
    R_hip = np.array([cx+hip_sep/2, cy])
    L_hip = np.array([cx-hip_sep/2, cy])

    # Spine/shoulder center
    torso_angle = np.deg2rad(5) * np.sin(wave_freq*t)  # happy mild swaying
    shoulder_c = np.array([cx, cy - L['torso']])

    # Shoulders
    shoulder_sep = 0.24
    R_shoulder = shoulder_c + np.array([shoulder_sep/2, 0])
    L_shoulder = shoulder_c + np.array([-shoulder_sep/2, 0])

    # Head
    head_top = shoulder_c + np.array([0, -L['head_neck']])
    head_top[1] += head_bounce

    # Spine point
    spine = shoulder_c + np.array([0, L['spine']*0.5])

    # Legs
    # Simulate heavy stance: small up/down for ankles/knees
    # Sway legs a bit left/right in sync
    walkphase = wave_freq*t * heavy_amp_mod
    knee_swing = np.deg2rad(7)*np.sin(walkphase + np.pi)
    ankle_swing = np.deg2rad(11)*np.sin(walkphase)
    knee_offset = 0.05*np.sin(2*walkphase + np.pi/5)

    # Right leg
    RK = R_hip + np.array([
        0.02*np.sin(walkphase+1.3), L['upper_leg']
    ])
    RA = RK + np.array([
        0.02*np.sin(walkphase-1.3), L['lower_leg']
    ])

    # Left leg
    LK = L_hip + np.array([
        -0.02*np.sin(walkphase-0.7), L['upper_leg']
    ])
    LA = LK + np.array([
        -0.02*np.sin(walkphase+0.8), L['lower_leg']
    ])

    # Arms
    # Right arm is waving a weight!
    # We'll use a 2-segment waving motion from shoulder.
    # Simulate heavy weight: slow, exaggerated, forearm lags
    wave_phase =  np.sin(wave_freq * t)
    baseangle = np.deg2rad(60) # up
    right_shoulder_angle = baseangle - amp*wave_phase
    right_elbow_rel = np.deg2rad(60) + 0.8*amp*wave_phase # elbow lags shoulder, extended for heavy

    # Compute right elbow
    RE = R_shoulder + np.array([
        L['upper_arm']*np.cos(right_shoulder_angle),
        L['upper_arm']*np.sin(right_shoulder_angle)
    ])
    # Compute right wrist (limit: doesn't go higher than shoulder)
    right_total = right_shoulder_angle + right_elbow_rel - np.deg2rad(30)
    RW = RE + np.array([
        L['forearm']*np.cos(right_total),
        L['forearm']*np.sin(right_total)
    ])
    # Add a circle to represent the "heavy weight" at RW
    RW_visual = RW.copy()

    # Left arm: natural swinging (lightly)
    left_shoulder_angle = -(baseangle - amp*0.3*wave_phase)
    left_elbow_rel = np.deg2rad(45)
    LE = L_shoulder + np.array([
        L['upper_arm']*np.cos(left_shoulder_angle),
        L['upper_arm']*np.sin(left_shoulder_angle)
    ])
    LW = LE + np.array([
        L['forearm']*np.cos(left_shoulder_angle + left_elbow_rel),
        L['forearm']*np.sin(left_shoulder_angle + left_elbow_rel)
    ])

    # Collect all keypoints
    keypoints = np.zeros((15,2))
    keypoints[0] = head_top
    keypoints[1] = R_shoulder
    keypoints[2] = L_shoulder
    keypoints[3] = RE
    keypoints[4] = LE
    keypoints[5] = RW_visual
    keypoints[6] = LW
    keypoints[7] = shoulder_c
    keypoints[8] = R_hip
    keypoints[9] = L_hip
    keypoints[10] = RK
    keypoints[11] = LK
    keypoints[12] = RA
    keypoints[13] = LA
    keypoints[14] = spine

    return keypoints

# ==== Visualization ====
fig, ax = plt.subplots(figsize=(4,8))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.axis('off')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-0.55, 0.55)
ax.set_ylim(-0.2, 1.28)

# Plots for joints
joint_dots, = ax.plot([], [], 'wo', markersize=11)
# Draw the 'weight' as an extra dot attached to the right wrist
weight_dot, = ax.plot([], [], 'wo', markersize=17, markeredgewidth=0, alpha=0.95)
# Optional: draw skeleton lines for debugging (comment out for pure BML point-lights)
skeleton_lines = [ax.plot([],[], 'w-', lw=1.5, alpha=0.08)[0] for _ in get_skeleton()]

def init():
    joint_dots.set_data([], [])
    weight_dot.set_data([], [])
    for line in skeleton_lines:
        line.set_data([], [])
    return [joint_dots, weight_dot] + skeleton_lines

def animate(i):
    t = i/45.0   # Animate at 45 FPS
    keypoints = get_pose(t)
    x = keypoints[:,0]
    y = 1.1 - keypoints[:,1] # Invert Y for upright figure

    # Plot 15 key dots
    joint_dots.set_data(x, y)

    # 'Weight' attached to right wrist (joint id 5)
    weight_dot.set_data([x[5]], [y[5]])

    # Skeleton overlay (debugging/for plausible biomech)
    skeleton = get_skeleton()
    for idx, (a, b) in enumerate(skeleton):
        skeleton_lines[idx].set_data([x[a], x[b]], [y[a], y[b]])
    return [joint_dots, weight_dot] + skeleton_lines

ani = FuncAnimation(fig, animate, frames=215, interval=1000/45, blit=True, init_func=init)

plt.show()
