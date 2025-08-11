
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Stickman body part structure (15 joints in order):
# 0: head
# 1: right shoulder
# 2: left shoulder
# 3: right elbow
# 4: left elbow
# 5: right hand
# 6: left hand
# 7: pelvis
# 8: right hip
# 9: left hip
# 10: right knee
# 11: left knee
# 12: right ankle
# 13: left ankle
# 14: trunk (chest/center)

# Skeleton tree (for reference, not shown)
# [ (0,14), (1,14), (2,14), (1,3), (3,5), (2,4), (4,6), (14,7), (7,8), (7,9), (8,10), (9,11), (10,12), (11,13) ]

n_joints = 15

# Model a forward roll in approximately 2 seconds (60 frames/sec, 120 frames)
n_frames = 120
fps = 60

# Limb lengths (in arbitrary units, consistent with 320x480 display)
len_head = 25
len_upperarm = 35
len_forearm = 30
len_trunk = 45
len_pelvis = 30
len_upperleg = 45
len_lowerleg = 40
len_shoulder_width = 40
len_hip_width = 30

# Coordinates for T-pose to be used as reference
def tpose_points(center=(160,240)):
    cx, cy = center
    pts = np.zeros((n_joints,2), dtype=float)
    # Trunk center
    pts[14] = [cx, cy]
    # Head
    pts[0] = [cx, cy-len_trunk-len_head]
    # Shoulders
    pts[1] = [cx-len_shoulder_width/2, cy-len_trunk//2]
    pts[2] = [cx+len_shoulder_width/2, cy-len_trunk//2]
    # Elbows
    pts[3] = pts[1] + [-(len_upperarm), 0]
    pts[4] = pts[2] + [ (len_upperarm), 0]
    # Hands
    pts[5] = pts[3] + [-(len_forearm), 0]
    pts[6] = pts[4] + [ (len_forearm), 0]
    # Pelvis
    pts[7] = [cx, cy+len_trunk//2]
    # Hips
    pts[8] = [cx-len_hip_width/2, cy+len_trunk//2]
    pts[9] = [cx+len_hip_width/2, cy+len_trunk//2]
    # Knees
    pts[10] = pts[8] + [0, len_upperleg]
    pts[11] = pts[9] + [0, len_upperleg]
    # Ankles
    pts[12] = pts[10] + [0, len_lowerleg]
    pts[13] = pts[11] + [0, len_lowerleg]
    return pts

# Generate forward roll motion sequence: Joint positions shape (n_frames, 15, 2)
def forward_roll_sequence(n_frames, center=(160,240), radius=80, travel_y=160):
    # Parameters:
    #   radius: roll radius (circle for trunk, all others depend on trunk angle)
    #   travel_y: total vertical distance (downwards) traveled during roll

    base_pts = tpose_points(center)
    # For each frame, calculate trunk angle and root position
    joint_seq = np.zeros((n_frames, n_joints, 2), dtype=float)

    for f in range(n_frames):
        # Progress: 0..1
        prog = f / (n_frames-1)
        # Main rolling angle (start upright, roll forward 360 deg, i.e. +2pi radians)
        theta = np.pi/2 + 2*np.pi*prog  # start at pi/2 (vertical), rolls forward
        # Trunk/torso center (14) traces a vertical + rolling path
        trunk_cx = center[0] + radius * np.cos(theta-np.pi/2)
        trunk_cy = center[1] + radius * np.sin(theta-np.pi/2) + travel_y*prog
        # The pelvis follows trunk, offset down along rolling direction
        pelvis_dx = 0
        pelvis_dy = len_trunk/2
        pelvis_vec = np.array([
            pelvis_dx*np.cos(theta) - pelvis_dy*np.sin(theta),
            pelvis_dx*np.sin(theta) + pelvis_dy*np.cos(theta),
        ])
        pelvis_xy = np.array([trunk_cx, trunk_cy]) + pelvis_vec

        # Head position (above trunk, along spine direction)
        head_dx = 0
        head_dy = - (len_trunk/2 + len_head)
        head_vec = np.array([
            head_dx*np.cos(theta) - head_dy*np.sin(theta),
            head_dx*np.sin(theta) + head_dy*np.cos(theta),
        ])
        head_xy = np.array([trunk_cx, trunk_cy]) + head_vec

        # Shoulders (left/right, at top of trunk)
        shoulder_offset = len_shoulder_width/2
        shoulder_height = -len_trunk/2
        right_shoulder_vec = np.array([
            -shoulder_offset*np.cos(theta) - shoulder_height*np.sin(theta),
            -shoulder_offset*np.sin(theta) + shoulder_height*np.cos(theta),
        ])
        left_shoulder_vec = np.array([
            shoulder_offset*np.cos(theta) - shoulder_height*np.sin(theta),
            shoulder_offset*np.sin(theta) + shoulder_height*np.cos(theta),
        ])
        rs_xy = np.array([trunk_cx, trunk_cy]) + right_shoulder_vec
        ls_xy = np.array([trunk_cx, trunk_cy]) + left_shoulder_vec

        # Hips (left/right, at pelvis)
        hip_offset = len_hip_width/2
        hip_height = len_trunk/2
        right_hip_vec = np.array([
            -hip_offset*np.cos(theta) - hip_height*np.sin(theta),
            -hip_offset*np.sin(theta) + hip_height*np.cos(theta),
        ])
        left_hip_vec = np.array([
            hip_offset*np.cos(theta) - hip_height*np.sin(theta),
            hip_offset*np.sin(theta) + hip_height*np.cos(theta),
        ])
        rh_xy = pelvis_xy + right_hip_vec
        lh_xy = pelvis_xy + left_hip_vec

        # Elbows: keep elbows flexed and oriented in line with rolling
        elbow_angle = theta + np.pi/1.5      # Bending arms in front during roll
        elbow_spread = 20 + 15*np.sin(2*np.pi*prog)  # slight undulation
        re_xy = rs_xy + np.array([
            -len_upperarm*np.cos(elbow_angle) + elbow_spread*np.sin(theta),
            -len_upperarm*np.sin(elbow_angle) + elbow_spread*np.cos(theta)
        ])
        le_xy = ls_xy + np.array([
            -len_upperarm*np.cos(elbow_angle) - elbow_spread*np.sin(theta),
            -len_upperarm*np.sin(elbow_angle) - elbow_spread*np.cos(theta)
        ])
        # Hands: arms bent, hands near head (simulate tucking in)
        hand_angle = elbow_angle + np.pi/1.8
        fh_spread = 12
        rh_xy_hand = re_xy + np.array([
            -len_forearm*np.cos(hand_angle) + fh_spread*np.sin(theta)/2,
            -len_forearm*np.sin(hand_angle) + fh_spread*np.cos(theta)/2
        ])
        lh_xy_hand = le_xy + np.array([
            -len_forearm*np.cos(hand_angle) - fh_spread*np.sin(theta)/2,
            -len_forearm*np.sin(hand_angle) - fh_spread*np.cos(theta)/2
        ])

        # Knees: flex knees, bring toward body, phase in rolling cycle for natural biomech.
        knee_flex = 0.7 + 0.13*np.cos(2*np.pi*prog)
        knee_angle_r = theta + np.pi/1.1
        knee_angle_l = theta + np.pi/1.1 + 0.2
        rk_xy = rh_xy + np.array([
            len_upperleg*knee_flex*np.cos(knee_angle_r),
            len_upperleg*knee_flex*np.sin(knee_angle_r)
        ])
        lk_xy = lh_xy + np.array([
            len_upperleg*knee_flex*np.cos(knee_angle_l),
            len_upperleg*knee_flex*np.sin(knee_angle_l)
        ])

        # Ankles: tucked near pelvis/trunk during roll
        ankle_angle_r = knee_angle_r + np.pi/1.8
        ankle_angle_l = knee_angle_l + np.pi/1.8
        ra_xy = rk_xy + np.array([
            len_lowerleg*0.7*np.cos(ankle_angle_r),
            len_lowerleg*0.7*np.sin(ankle_angle_r)
        ])
        la_xy = lk_xy + np.array([
            len_lowerleg*0.7*np.cos(ankle_angle_l),
            len_lowerleg*0.7*np.sin(ankle_angle_l)
        ])

        # Assign joint coords to this frame
        joints = np.zeros((n_joints,2),dtype=float)
        joints[0] = head_xy                           # head
        joints[1] = rs_xy                             # right shoulder
        joints[2] = ls_xy                             # left shoulder
        joints[3] = re_xy                             # right elbow
        joints[4] = le_xy                             # left elbow
        joints[5] = rh_xy_hand                        # right hand
        joints[6] = lh_xy_hand                        # left hand
        joints[7] = pelvis_xy                         # pelvis
        joints[8] = rh_xy                             # right hip
        joints[9] = lh_xy                             # left hip
        joints[10] = rk_xy                            # right knee
        joints[11] = lk_xy                            # left knee
        joints[12] = ra_xy                            # right ankle
        joints[13] = la_xy                            # left ankle
        joints[14] = [trunk_cx, trunk_cy]             # trunk/chest

        joint_seq[f,:,:] = joints

    return joint_seq

points = forward_roll_sequence(n_frames, center=(160,120), radius=80, travel_y=160)

fig, ax = plt.subplots(figsize=(3.5,5.6), dpi=100)
ax.set_facecolor('black')
plt.subplots_adjust(left=0,right=1,top=1,bottom=0)

sct = ax.scatter([],[], c='w', s=28)
ax.set_xlim(0, 320)
ax.set_ylim(0, 480)
ax.set_xticks([])
ax.set_yticks([])
plt.gca().invert_yaxis()

def init():
    sct.set_offsets(np.zeros((n_joints,2)))
    return sct,

def animate(i):
    # For smooth looping, compute idx using mod
    idx = i % n_frames
    sct.set_offsets(points[idx])
    return sct,

ani = animation.FuncAnimation(
    fig, animate, frames=n_frames, interval=1000//fps, blit=True, init_func=init, repeat=True)

plt.show()
