
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 15 points: Head, Shoulders, Elbows, Wrists, Chest, Hips, Knees, Ankles, Hands [with weights]
#    0     1    2    3    4     5     6     7    8    9    10    11   12   13   14
# [head, R shoulder, L shoulder, R elbow, L elbow, R wrist, L wrist, chest, pelvis,
#  R hip, L hip, R knee, L knee, R ankle, L ankle]

# To represent the sadman 'bowing with heavy weight', arms hang down, body bent forward.
# We'll simulate a bowing movement over a cycle.

# Define skeleton in neutral pose (standing upright, 2D coordinates)
def get_skeleton_pose(theta, frame):
    ''' Given bow angle theta (in radians), returns shape (15,2) array of joint positions '''
    # Center x,y for pelvis (point 8)-- for animation, move pelvis up a bit
    pelvis_x = 0.0
    pelvis_y = 0.0

    # Segment lengths (in arbitrary units)
    head_len   = 0.22
    neck_len   = 0.12
    torso_len  = 0.34
    shoulder_offset = 0.13
    upperarm_len = 0.24
    forearm_len = 0.22
    hand_len = 0.08
    hip_offset = 0.11
    thigh_len = 0.26
    shank_len = 0.25
    foot_offset = 0.09

    # Add some natural variation, for swaying/heavy arms
    def heaviness_offset(t, l=0.08):
        return np.sin(2 * np.pi * t) * l

    t = (frame % 60) / 59

    # Pelvis (center)
    pelvis = np.array([pelvis_x, pelvis_y + 0.6])

    # Spine
    chest = pelvis + np.array([0, torso_len])
    neck = chest + np.array([0, neck_len])
    head = neck + np.array([0, head_len])

    # Hips
    r_hip = pelvis + np.array([ hip_offset, 0])
    l_hip = pelvis + np.array([-hip_offset, 0])

    # Shoulders
    r_shoulder = chest + np.array([ shoulder_offset, 0])
    l_shoulder = chest + np.array([-shoulder_offset, 0])

    # Repeat for arms:
    # Arms (hangs down, with elbows and wrists forwards due to bow, hands lower for the 'weight')
    r_elbow = r_shoulder + np.array([
        np.sin(theta+0.15) * upperarm_len * 0.98,
        -np.cos(theta+0.15) * upperarm_len
    ])
    l_elbow = l_shoulder + np.array([
        np.sin(theta-0.15) * upperarm_len * 0.98,
        -np.cos(theta-0.15) * upperarm_len
    ])
    # Wrists curve farther forward & down for "heavy"
    r_wrist = r_elbow + np.array([
        np.sin(theta+0.4) * forearm_len * 1.1 + heaviness_offset(t),
        -np.cos(theta+0.4) * forearm_len * 1.15
    ])
    l_wrist = l_elbow + np.array([
        np.sin(theta-0.4) * forearm_len * 1.1 + heaviness_offset(t+0.5),
        -np.cos(theta-0.4) * forearm_len * 1.15
    ])

    # Hands drag even farther (representing "weight")
    r_hand = r_wrist + np.array([
        np.sin(theta+0.80) * hand_len * 1.2 + heaviness_offset(t+0.35,0.10),
        -np.cos(theta+0.80) * hand_len * 1.25
    ])
    l_hand = l_wrist + np.array([
        np.sin(theta-0.80) * hand_len * 1.2 + heaviness_offset(t-0.35,0.10),
        -np.cos(theta-0.80) * hand_len * 1.25
    ])

    # Knees
    r_knee = r_hip + np.array([
        np.sin(np.deg2rad(100-theta*80)) * thigh_len,
        -np.cos(np.deg2rad(100-theta*80)) * thigh_len
    ])
    l_knee = l_hip + np.array([
        np.sin(np.deg2rad(100-theta*80)) * thigh_len,
        -np.cos(np.deg2rad(100-theta*80)) * thigh_len
    ])
    # Ankles
    r_ankle = r_knee + np.array([
        np.sin(np.deg2rad(99-theta*80)) * shank_len,
        -np.cos(np.deg2rad(99-theta*80)) * shank_len
    ])
    l_ankle = l_knee + np.array([
        np.sin(np.deg2rad(99-theta*80)) * shank_len,
        -np.cos(np.deg2rad(99-theta*80)) * shank_len
    ])

    # 15 points: head, R shoulder, L shoulder, R elbow, L elbow, R wrist, L wrist, chest,
    # pelvis, R hip, L hip, R knee, L knee, R ankle, L ankle
    pose = np.stack([
        head,
        r_shoulder, l_shoulder,
        r_elbow, l_elbow,
        r_wrist, l_wrist,
        chest, pelvis,
        r_hip, l_hip,
        r_knee, l_knee,
        r_ankle, l_ankle
    ])
    # Replace wrists with hands (for weight effect): point 5 (right wrist) and 6 (left wrist) should be the hands
    pose[5] = r_hand
    pose[6] = l_hand

    return pose

# Animation update
def animate(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.axis('off')
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-0.2, 1.8)

    # Bowing: theta ranges from 0 (upright) to about 1.0 radians (about 55 deg)
    cycle = (frame % 60) / 59
    if cycle < 0.3:
        theta = (cycle / 0.3) * 1.05     # Bow down smoothly
    elif cycle < 0.7:
        theta = 1.05                     # Hold bow at max angle
    else:
        # Rise up (symmetrically)
        theta = (1.0 - (cycle-0.7)/0.3) * 1.05
        theta = np.clip(theta, 0, 1.05)
    points = get_skeleton_pose(theta, frame)
    # Draw 15 white dots, as in example
    ax.scatter(points[:,0], points[:,1], s=65, c='white', edgecolors='none')

# Set up figure
fig, ax = plt.subplots(figsize=(4,7))
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_facecolor('black')
ax.axis('off')

ani = animation.FuncAnimation(
    fig, animate, frames=90, interval=40, blit=False, repeat=True
)
plt.show()
