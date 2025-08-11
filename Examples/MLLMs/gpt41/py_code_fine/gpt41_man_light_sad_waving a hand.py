
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Body segment lengths (proportional, in arbitrary units)
HEAD = 18
NECK = 4
SHOULDER = 10
TORSO = 22
PELVIS = 8
UPPER_ARM = 16
FOREARM = 15
HAND = 5
THIGH = 19
SHIN = 17
FOOT = 7

# Horizontal spacing
SHOULDER_WIDTH = 28
HIP_WIDTH = 15

# Joint index order:
# 0: Head Top
# 1,2: (L,R) Shoulders
# 3,4: (L,R) Elbow
# 5,6: (L,R) Wrist
# 7,8: (L,R) Hand
# 9: Base of neck / upper torso
# 10,11: (L,R) Hip
# 12,13: (L,R) Knee
# 14,15: (L,R) Ankle
# 16,17: (L,R) Foot

def body_structure():
    """Return the relative (x, y) positions (in 'standing neutral pose') for all joints."""
    y0 = 0  # pelvis
    x0 = 0  # midline

    y_neck = y0 + PELVIS + TORSO + NECK
    y_head = y_neck + HEAD

    # Shoulders
    x_shoulder_left = x0 - SHOULDER_WIDTH / 2
    x_shoulder_right = x0 + SHOULDER_WIDTH / 2

    # Hips
    x_hip_left = x0 - HIP_WIDTH/2
    x_hip_right = x0 + HIP_WIDTH/2

    # Elbows positions (arms straight down by side)
    y_elbow = y_neck - UPPER_ARM
    x_elbow_left = x_shoulder_left
    x_elbow_right = x_shoulder_right
    # Wrists, hands
    y_wrist = y_elbow - FOREARM
    x_wrist_left = x_elbow_left
    x_wrist_right = x_elbow_right

    y_hand = y_wrist - HAND
    x_hand_left = x_wrist_left
    x_hand_right = x_wrist_right

    # Knees, ankles, feet
    y_knee = y0 + PELVIS/2 - THIGH
    y_ankle = y_knee - SHIN
    y_foot = y_ankle

    x_knee_left = x_hip_left
    x_knee_right = x_hip_right
    x_ankle_left = x_knee_left
    x_ankle_right = x_knee_right

    x_foot_left = x_ankle_left - FOOT/2
    x_foot_right = x_ankle_right + FOOT/2

    # Now assemble 15 key points for the point-light display
    # We use the convention as in many bio-motion displays:

    #  0  Head Top
    #  1  Left Shoulder
    #  2  Right Shoulder
    #  3  Left Elbow
    #  4  Right Elbow
    #  5  Left Wrist
    #  6  Right Wrist
    #  7  Torso (neck junction)
    #  8  Left Hip
    #  9  Right Hip
    # 10  Left Knee
    # 11  Right Knee
    # 12  Left Ankle
    # 13  Right Ankle
    # 14  Pelvis center

    joints = [
        (x0, y_head),                      # 0 Head Top
        (x_shoulder_left, y_neck),         # 1 Left Shoulder
        (x_shoulder_right, y_neck),        # 2 Right Shoulder
        (x_elbow_left, y_elbow),           # 3 Left Elbow
        (x_elbow_right, y_elbow),          # 4 Right Elbow
        (x_wrist_left, y_wrist),           # 5 Left Wrist
        (x_wrist_right, y_wrist),          # 6 Right Wrist
        (x0, y_neck),                      # 7 Torso (neck)
        (x_hip_left, y0 + PELVIS),         # 8 Left Hip
        (x_hip_right, y0 + PELVIS),        # 9 Right Hip
        (x_knee_left, y_knee),             # 10 Left Knee
        (x_knee_right, y_knee),            # 11 Right Knee
        (x_ankle_left, y_ankle),           # 12 Left Ankle
        (x_ankle_right, y_ankle),          # 13 Right Ankle
        (x0, y0),                          # 14 Pelvis center
    ]
    return np.array(joints, dtype=float)

def update_pose(t):
    # Get the body template
    joints = body_structure()

    # Waving pattern for the RIGHT hand (indices 2,4,6)
    # shoulder (2), elbow (4), wrist (6)

    # Arm raise angle at shoulder (degrees; 0=down, 90=front, 180=up)
    base_shoulder_angle = 30  # arms somewhat down
    amp_shoulder = 60         # how much to raise it up
    shoulder_angle = np.deg2rad(base_shoulder_angle + amp_shoulder * 0.5 * (1-np.cos(2*np.pi*t)))

    # Elbow flexion angle (degrees; 180=straight, lower values=bend)
    base_elbow_angle = 170       # nearly straight at rest
    amp_elbow = 20               # how much to flex during wave
    elbow_angle = np.deg2rad(base_elbow_angle - amp_elbow * np.abs(np.sin(2*np.pi*t)))

    # At the shoulder: rotate upper arm relative to torso
    x_shoulder, y_shoulder = joints[2]
    x_neck, y_neck = joints[7]

    # Right upper arm
    upper_arm_dx = UPPER_ARM * np.sin(shoulder_angle)
    upper_arm_dy = -UPPER_ARM * np.cos(shoulder_angle)
    # elbow position
    x_elbow = x_shoulder + upper_arm_dx
    y_elbow = y_shoulder + upper_arm_dy

    # Forearm (relative to elbow)
    # Elbow angle is flexion (angle between upper/forearm). For waving, keep near-straight.
    # It is in same plane as upper arm
    forearm_dx = FOREARM * np.sin(shoulder_angle + (np.pi - elbow_angle))
    forearm_dy = -FOREARM * np.cos(shoulder_angle + (np.pi - elbow_angle))
    x_wrist = x_elbow + forearm_dx
    y_wrist = y_elbow + forearm_dy

    # Add optional "hand" flick: oscillate wrist about ±15° at 2x waving freq
    hand_angle = np.deg2rad(15 * np.sin(4 * np.pi * t))
    hand_dx = HAND * np.sin(shoulder_angle + (np.pi - elbow_angle) + hand_angle)
    hand_dy = -HAND * np.cos(shoulder_angle + (np.pi - elbow_angle) + hand_angle)
    x_hand = x_wrist + hand_dx
    y_hand = y_wrist + hand_dy

    # Update right arm keypoints
    joints[4] = [x_elbow, y_elbow]   # right elbow
    joints[6] = [x_wrist, y_wrist]   # right wrist
    # We do not mark hand explicitly; wrists as endpoints

    # Subtle compensation:
    # Raise the right shoulder a little when arm is up, drop left
    joints[2][1] += 2.5 * np.sin(shoulder_angle)
    joints[1][1] -= 1.0 * np.sin(shoulder_angle)   # Lower left shoulder a bit

    # Torso sways slightly to maintain balance
    joints[:,0] += 2 * np.cos(4*np.pi*t) * 0.09

    # Small vertical center-of-mass oscillation for realism
    joints[:,1] += 2 * np.sin(2 * np.pi * t) * 0.04

    # Feet bounce a little (reaction to motion)
    foot_bounce = 0.7 * np.abs(np.sin(2*np.pi*t))
    joints[12][1] -= foot_bounce
    joints[13][1] -= foot_bounce

    return joints

def animate_func(frame, scat):
    t = (frame % frames) / frames  # Loop between 0-1
    joints = update_pose(t)

    # Center vertically at 0 for better display
    y_center = (np.max(joints[:,1]) + np.min(joints[:,1]))/2
    x_center = (np.max(joints[:,0]) + np.min(joints[:,0]))/2
    display_scale = 80

    scat.set_offsets(np.column_stack((
        (joints[:,0] - x_center) * 1.1,    # stretch horizontally
        (joints[:,1] - y_center)
    )))
    return scat,

# Set up plot
fig, ax = plt.subplots(figsize=(3.5, 5))
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')
margin = 33
display_scale = 80
ax.set_xlim(-display_scale, display_scale)
ax.set_ylim(-display_scale, display_scale)

# Initial point-lights
joints0 = body_structure()
scat = ax.scatter(
    joints0[:,0], joints0[:,1],
    s=38, c='w', edgecolors='none'
)

frames = 80   # anim frames per cycle (~1.2s per wave)
ani = animation.FuncAnimation(
    fig, animate_func, fargs=(scat,),
    frames=frames, interval=1000*1.2/frames, blit=True
)

plt.show()
