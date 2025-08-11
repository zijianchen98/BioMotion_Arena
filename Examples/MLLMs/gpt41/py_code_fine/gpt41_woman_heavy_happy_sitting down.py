
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
n_frames = 100
dt = 1.0 / n_frames
point_size = 60
bg_color = 'black'
dot_color = 'white'

# 15 points: [head, L_shoulder, R_shoulder, L_elbow, R_elbow, L_hand, R_hand,
#             chest, hips, L_hip, R_hip, L_knee, R_knee, L_ankle, R_ankle]
# Index:       0       1          2          3         4        5       6
#              7       8         9          10         11      12       13     14

def heaviness_wide():
    # Joint distances (reflect 'heavy' / body proportions)
    s = {}
    s['head_chest'] = 30.0
    s['chest_shoulder'] = 18.0
    s['shoulder_elbow'] = 25.0
    s['elbow_hand'] = 22.0
    s['chest_hips'] = 30.0
    s['hips_hip'] = 13.0  # Hips width
    s['hip_knee'] = 27.0
    s['knee_ankle'] = 26.0
    s['body_width'] = 38.0
    return s

def happy_head_bounce(t, amp=3.5, freq=2.8):
    # Head moves up/down gently to convey 'happy' expressivity
    return amp * np.sin(2*np.pi*t*freq)

def happy_arm_bounce(t, amp=9, freq=1.7):
    return amp * np.sin(2*np.pi*freq*t)

# Trajectory generation for sitting down
def pose_points(fr):
    # t: normalized progress [0, 1]
    t = min(max(fr / (n_frames-1), 0), 1)
    # Phases: Start stand, bending, contact, settle
    ph1 = 0.42   # Start to bend
    ph2 = 0.79   # Bending to seat contact
    ph3 = 1.00   # Settling
    
    s = heaviness_wide()
    # Initial positions, centered
    # Standing (Y axis points upward)
    px = 0.0
    py = 0.0

    # Dynamic vertical offset as the body lowers
    y_body = 0
    if t < ph1:
        y_body = 0
    elif t < ph2:
        # Quadratic ease as center body moves down
        d = t - ph1
        dmax = ph2 - ph1
        y_body = -60 * (d/dmax)**1.5
    else:
        # Reach final low point and tiny bounce at end
        y_body = -60 + 4*np.exp(-10*(t-ph2))*np.cos(25*(t-ph2))
        
    y_base = py + y_body

    # Head
    head = [px, y_base + s['head_chest'] + s['chest_hips'] + 40 + happy_head_bounce(t)]
    # Chest
    chest = [px, y_base + s['chest_hips'] + 40]
    # Hips (pelvis center)
    hips = [px, y_base + 40]

    # Shoulders: Outward for heavy/wider build
    shoulder_offset = s['body_width']/2
    l_shoulder = [px - shoulder_offset, chest[1]]
    r_shoulder = [px + shoulder_offset, chest[1]]

    # Elbows/Hands: Arms start at ~10° from body, then move forward and up to counterbalance
    # and display 'happy' (mild, non-withdrawing open arms, some hand bounce)
    arm_angle_0 = np.deg2rad(94)   # Downward
    arm_angle_1 = np.deg2rad(60)   # Forward-up when sitting
    arm_angle = (1-t)*arm_angle_0 + t*arm_angle_1

    # Animation: happy arm 'bounce'
    arm_bounce = happy_arm_bounce(t) * (1-t)

    # Left arm (left from viewer)
    l_elbow = [
        l_shoulder[0] + s['shoulder_elbow']*np.cos(np.pi+arm_angle) + 0.14*arm_bounce,
        l_shoulder[1] + s['shoulder_elbow']*np.sin(-arm_angle)       + 0.08*arm_bounce
    ]
    l_hand = [
        l_elbow[0] + s['elbow_hand']*np.cos(-np.pi+arm_angle) + 0.22*arm_bounce,
        l_elbow[1] + s['elbow_hand']*np.sin(-arm_angle)       + 0.08*arm_bounce
    ]
    # Right arm
    r_elbow = [
        r_shoulder[0] + s['shoulder_elbow']*np.cos(-arm_angle) - 0.14*arm_bounce,
        r_shoulder[1] + s['shoulder_elbow']*np.sin(-arm_angle) + 0.08*arm_bounce
    ]
    r_hand = [
        r_elbow[0] + s['elbow_hand']*np.cos(arm_angle) - 0.22*arm_bounce,
        r_elbow[1] + s['elbow_hand']*np.sin(-arm_angle) + 0.08*arm_bounce
    ]

    # Hips: width for 'heavy'
    hip_offset = s['hips_hip']
    l_hip = [hips[0] - hip_offset, hips[1]]
    r_hip = [hips[0] + hip_offset, hips[1]]

    # Up-down curved trajectory of hips to feet: for realism
    hip_traj_knee_flex = np.deg2rad(15 if t < ph1 else 58*(t-ph1)/(ph2-ph1) if t < ph2 else 62)
    knee_disp = 0
    if t < ph1:
        knee_disp = 0
    elif t < ph2:
        knee_disp = 22 * (t-ph1)/(ph2-ph1)
    else:
        knee_disp = 22
    # For legs, interpolate standing→seated
    knee_angles = [np.deg2rad(8), np.deg2rad(8)]  # standing
    ankle_angles = [np.deg2rad(0), np.deg2rad(0)]
    if t < ph1:
        pass
    elif t < ph2:
        bend_adv = (t-ph1)/(ph2-ph1)
        knee_angles = [np.deg2rad(8 + bend_adv*67), np.deg2rad(8 + bend_adv*67)]
        ankle_angles = [np.deg2rad(bend_adv*95), np.deg2rad(bend_adv*96)]
    else:
        knee_angles = [np.deg2rad(75), np.deg2rad(75)]
        ankle_angles = [np.deg2rad(93), np.deg2rad(94)]

    # Thigh and shank lengths (slightly shortened for heavy appearance)
    thigh = s['hip_knee'] * 0.97
    shank = s['knee_ankle'] * 0.96

    # Knees
    l_knee = [
        l_hip[0] + thigh * np.sin(knee_angles[0]),
        l_hip[1] - thigh * np.cos(knee_angles[0])
    ]
    r_knee = [
        r_hip[0] + thigh * np.sin(knee_angles[1]),
        r_hip[1] - thigh * np.cos(knee_angles[1])
    ]
    # Ankles
    l_ankle = [
        l_knee[0] + shank * np.sin(ankle_angles[0]),
        l_knee[1] - shank * np.cos(ankle_angles[0])
    ]
    r_ankle = [
        r_knee[0] + shank * np.sin(ankle_angles[1]),
        r_knee[1] - shank * np.cos(ankle_angles[1])
    ]
    
    # The feet are not used as explicit points, so the 15 dots are:
    points = [
        head,          # 0
        l_shoulder,    # 1
        r_shoulder,    # 2
        l_elbow,       # 3
        r_elbow,       # 4
        l_hand,        # 5
        r_hand,        # 6
        chest,         # 7
        hips,          # 8
        l_hip,         # 9
        r_hip,         # 10
        l_knee,        # 11
        r_knee,        # 12
        l_ankle,       # 13
        r_ankle,       # 14
    ]
    return np.array(points)

# Setup
fig, ax = plt.subplots(figsize=(4,8))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_facecolor(bg_color)
ax.set_aspect('equal')
ax.axis('off')

# Limits chosen to fit 'sitting down' movement
ax.set_xlim(-60, 60)
ax.set_ylim(-10, 180)

scat = ax.scatter([], [], s=point_size, c=dot_color, edgecolors='none')

def init():
    scat.set_offsets(np.zeros((15,2)))
    scatter_artist = scat
    return scatter_artist,

def animate(i):
    points = pose_points(i)
    scat.set_offsets(points)
    return scat,

ani = animation.FuncAnimation(
    fig, animate, frames=n_frames, interval=22, blit=True, init_func=init)

# To show the animation
plt.show()
