
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Joint order (15 points matching classic biological motion notation):
# 0: Head
# 1: Left Shoulder
# 2: Right Shoulder
# 3: Left Elbow
# 4: Right Elbow
# 5: Left Wrist
# 6: Right Wrist
# 7: Torso (Hip center)
# 8: Left Hip
# 9: Right Hip
# 10: Left Knee
# 11: Right Knee
# 12: Left Ankle
# 13: Right Ankle
# 14: Root Pelvis (slightly below hip center, for balance)

# Human body segment lengths (approx. ratios)
L_head_neck = 0.12
L_torso = 0.32
L_shoulder = 0.14
L_upper_arm = 0.15
L_lower_arm = 0.12
L_hip = 0.16
L_upper_leg = 0.21
L_lower_leg = 0.21
L_root_offset = 0.04 # pelvis marker

# Center position of body (origin)
base_x = 0.0
base_y = 0.0

def get_bowed_pose(theta_bow, theta_arm, theta_knee, theta_ankle, offset_x=0, offset_y=0):
    # base = Hip center
    points = np.zeros((15, 2))
    # Torso
    # Hip center / pelvis (joint 7)
    pelvis = np.array([base_x + offset_x, base_y + offset_y])
    points[7] = pelvis
    # Shoulder center (rotate up from pelvis by torso and bow angle)
    shoulder = pelvis + L_torso * np.array([
        np.sin(theta_bow), np.cos(theta_bow)
    ])
    neck = shoulder
    # Head (above neck)
    head = neck + L_head_neck * np.array([
        np.sin(theta_bow), np.cos(theta_bow)
    ])
    points[0] = head

    # Shoulders: left/right from neck
    points[1] = neck + L_shoulder / 2 * np.array([np.cos(theta_bow), -np.sin(theta_bow)])
    points[2] = neck - L_shoulder / 2 * np.array([np.cos(theta_bow), -np.sin(theta_bow)])

    # Elbows: from shoulders, slightly drooping down and rotated forward by theta_arm
    points[3] = (
        points[1] +
        L_upper_arm * np.array([
            np.sin(theta_bow + theta_arm), np.cos(theta_bow + theta_arm)
        ])
    )
    points[4] = (
        points[2] +
        L_upper_arm * np.array([
            np.sin(theta_bow + theta_arm), np.cos(theta_bow + theta_arm)
        ])
    )
    # Wrists: from elbows, continue angle + a gentle further bend
    points[5] = (
        points[3] +
        L_lower_arm * np.array([
            np.sin(theta_bow + theta_arm + 0.15), np.cos(theta_bow + theta_arm + 0.15)
        ])
    )
    points[6] = (
        points[4] +
        L_lower_arm * np.array([
            np.sin(theta_bow + theta_arm + 0.15), np.cos(theta_bow + theta_arm + 0.15)
        ])
    )

    # Hips: left/right from pelvis
    points[8] = pelvis + L_hip / 2 * np.array([np.cos(theta_bow), -np.sin(theta_bow)])
    points[9] = pelvis - L_hip / 2 * np.array([np.cos(theta_bow), -np.sin(theta_bow)])

    # Knees: down from hips, bending by theta_knee (relative to bow direction)
    points[10] = (
        points[8] +
        L_upper_leg * np.array([
            np.sin(theta_bow - theta_knee), np.cos(theta_bow - theta_knee)
        ])
    )
    points[11] = (
        points[9] +
        L_upper_leg * np.array([
            np.sin(theta_bow - theta_knee), np.cos(theta_bow - theta_knee)
        ])
    )

    # Ankles: down from knees, bend a bit more by theta_ankle
    points[12] = (
        points[10] +
        L_lower_leg * np.array([
            np.sin(theta_bow - theta_knee - theta_ankle), np.cos(theta_bow - theta_knee - theta_ankle)
        ])
    )
    points[13] = (
        points[11] +
        L_lower_leg * np.array([
            np.sin(theta_bow - theta_knee - theta_ankle), np.cos(theta_bow - theta_knee - theta_ankle)
        ])
    )
    # Pelvis root (slightly below pelvis, for mass center)
    points[14] = pelvis - L_root_offset * np.array([np.sin(theta_bow), np.cos(theta_bow)])

    return points

# Animation parameters
n_frames = 64
fps = 30

def bow_motion_progress(t):
    # t: 0 (upright) to 1 (deep bow)
    # Bow smoothly in and out (slow in/out, smooth inbetween)
    return 0.5*(1-np.cos(np.pi*t))

def bow_parameters(t):
    # t from 0 to 1 for bow in, 1 to 2 for bow out
    # Bow angles (radians)
    # Typical bow: 50-65 degrees (0.9-1.2 radian)
    bow_angle = np.deg2rad(0) + bow_motion_progress(t%1.0)*np.deg2rad(60)
    arm_angle = np.deg2rad(15) + bow_motion_progress(t%1.0)*np.deg2rad(35)
    knee_angle = np.deg2rad(0) + bow_motion_progress(t%1.0)*np.deg2rad(25)
    ankle_angle = np.deg2rad(0) + bow_motion_progress(t%1.0)*np.deg2rad(12)
    # Sway gently during bow
    sway = 0.03 * np.sin(np.pi * t)
    return bow_angle, arm_angle, knee_angle, ankle_angle, sway

# Precompute frames
frames = []
cycle_frames = n_frames
for fi in range(cycle_frames):
    # The bow cycle is 2 seconds (bow-in then bow-out)
    t = (2*fi)/cycle_frames
    ba, aa, ka, anka, sx = bow_parameters(t)
    pts = get_bowed_pose(ba, aa, ka, anka, offset_x=0, offset_y=sx)
    frames.append(pts)

# Setup plot/animation
fig, ax = plt.subplots(figsize=(3, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
plt.axis('off')
ax.set_xlim(-0.3, 0.3)
ax.set_ylim(-0.1, 1.10)

dots, = ax.plot([], [], 'o', color='white', markersize=9, markeredgewidth=0)
# Optionally draw faint skeleton lines
pairs = [
    (0,1), (0,2), (1,2), # head to shoulders
    (1,3), (3,5), # left arm
    (2,4), (4,6), # right arm
    (1,7), (2,7), # shoulders to torso
    (7,8), (7,9), # torso to hips
    (8,10), (10,12), # left leg
    (9,11), (11,13), # right leg
    (7,14) # root pelvis
]
lines = []
for _ in pairs:
    l, = ax.plot([], [], '-', color='white', alpha=0.13, lw=2)
    lines.append(l)

def init():
    dots.set_data([], [])
    for l in lines:
        l.set_data([], [])
    return [dots] + lines

def animate(i):
    pts = frames[i % cycle_frames]
    dots.set_data(pts[:,0], pts[:,1])
    for li, (a,b) in enumerate(pairs):
        lines[li].set_data([pts[a,0], pts[b,0]], [pts[a,1], pts[b,1]])
    return [dots] + lines

ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=cycle_frames, interval=1000/fps, blit=True
)

plt.show()
