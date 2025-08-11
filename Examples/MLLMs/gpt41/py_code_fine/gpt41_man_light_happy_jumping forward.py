
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of frames per second and total duration
FPS = 40
DURATION = 2.0  # seconds
N_FRAMES = int(FPS * DURATION)

# 15 points: head, neck, r/l shoulder, r/l elbow, r/l wrist, torso, r/l hip, r/l knee, r/l ankle, pelvis
#          0    1     2           3     4           5     6           7      8    9         10    11       12     13     14
# Labels:  H,  N,  LSH,  RSH,  LEL,  REL,  LWR,  RWR,  T, LHI, RHI,  LKN, RKN, LAN, RAN
# This order matches proto-biological motion conventions

# 2D stick figure model base skeleton (standing, normalized, facing right)
SKELETON = np.array([
    [0,   1.40], # Head
    [0,   1.20], # Neck
    [-0.18,1.14], # Left Shoulder
    [0.18,1.14],  # Right Shoulder
    [-0.32,0.88], # Left Elbow
    [0.32,0.88],  # Right Elbow
    [-0.37,0.63], # Left Wrist
    [0.37,0.63],  # Right Wrist
    [0,   0.90],  # Torso (upper chest)
    [-0.12,0.68], # Left Hip
    [0.12,0.68],  # Right Hip
    [-0.15,0.25], # Left Knee
    [0.15,0.25],  # Right Knee
    [-0.13,0.00], # Left Ankle
    [0.13,0.00],  # Right Ankle
])

# Kinematic chain: Which points are the children of joints for stick animation (not strictly necessary for dots)
KINEMATICS = {
    'head': 0, 'neck': 1, 'l_shoulder': 2, 'r_shoulder': 3,
    'l_elbow': 4, 'r_elbow': 5, 'l_wrist': 6, 'r_wrist': 7,
    'torso': 8, 'l_hip': 9, 'r_hip': 10, 'l_knee': 11,
    'r_knee': 12, 'l_ankle': 13, 'r_ankle': 14
}

# For forward jumping, the body goes up and forward in a parabolic trajectory,
# with knees bending before takeoff, legs kicked back during flight, arms swing, etc.

def jump_motion(t, takeoff=0.3, flight=0.6, land=0.9):
    """
    For t in [0, 1]: returns transformation parameters for the skeleton at moment t.
    """
    # Parameters for movement
    forward_dist = 1.0
    jump_height = 0.7

    # Pre-jump: bend knees, squat down, lean slightly forward
    if t < takeoff:
        # t in [0, takeoff)
        prog = t / takeoff
        root_y = SKELETON[9,1] - 0.12 * prog      # hips lower
        root_x = SKELETON[9,0] + 0.05 * prog      # lean forward
        knee_bend = 0.6 * prog                    # how much knees bend (radians)
        arms_back = 1.1 * prog                    # arms swing backward
        pose_phase = 'squat'
    elif t < flight:
        # t in [takeoff, flight): initiate jump
        prog = (t-takeoff) / (flight-takeoff)
        # Parabolic motion - up and forward
        jump_prog = 0.5 - 0.5 * np.cos(np.pi * prog)  # ease-in/ease-out
        root_y = SKELETON[9,1] - 0.12 + jump_prog * jump_height
        root_x = SKELETON[9,0] + 0.05 + jump_prog * forward_dist
        knee_bend = (0.6 - 0.4 * jump_prog)               # knees straighten in air
        arms_back = 1.1 - 1.7 * jump_prog                  # arms swing forward/up
        pose_phase = 'takeoff/flight'
    elif t < land:
        # in air, prepare to land
        prog = (t-flight) / (land-flight)
        jump_prog = 1.0 - 0.5 * (1-np.cos(np.pi * prog))  # ease-out
        root_y = SKELETON[9,1] - 0.12 + jump_prog * jump_height
        root_x = SKELETON[9,0] + 0.05 + jump_prog * forward_dist
        knee_bend = 0.2 + 0.8 * prog                 # knees bend for landing
        arms_back = -0.6 + 0.4 * prog                 # arms forward, slight swing down
        pose_phase = 'land'
    else:
        # stand up, arms swing to rest, knees recover
        prog = min((t-land)/(1-land), 1)
        root_y = SKELETON[9,1] - 0.12 + (0.0)*(1-prog)
        root_x = SKELETON[9,0] + 0.05 + (forward_dist)*(1-prog)
        knee_bend = 1.0 - 0.7 * prog
        arms_back = -0.2 * (1-prog)
        pose_phase = 'recover'

    return dict(
        root_x=root_x,     # pelvis x
        root_y=root_y,     # pelvis y
        knee_bend=knee_bend,
        arms_back=arms_back,
        pose_phase=pose_phase
    )

def apply_pose(pose):
    """Calculate transformed joint locations from canonical skeleton and pose params"""
    pts = np.copy(SKELETON)
    # Translate hips (pelvis origin)
    dx, dy = pose['root_x'], pose['root_y']
    # All points will be translated by (dx-SKELETON[9,0], dy-SKELETON[9,1])
    d = np.array([dx-SKELETON[9,0], dy-SKELETON[9,1]])
    pts += d

    # Knees -- add knee angles & ankle positions
    # Left leg
    lh = 9; lk = 11; la = 13
    U_thigh = pts[lk] - pts[lh]
    U_thigh /= np.linalg.norm(U_thigh)
    left_knee_bend = -pose['knee_bend']
    # Thigh points down/back for squat, more vertical in air.
    rot = np.array([[np.cos(left_knee_bend), -np.sin(left_knee_bend)],
                    [np.sin(left_knee_bend),  np.cos(left_knee_bend)]])
    # Lengths
    thigh_len = np.linalg.norm(SKELETON[11]-SKELETON[9])
    shank_len = np.linalg.norm(SKELETON[13]-SKELETON[11])

    thigh_dir = np.matmul(rot, np.array([0, -1]))
    pts[lk] = pts[lh] + thigh_len * thigh_dir
    # Shank (ankle)
    shank_angle = 0.05 + 0.7*pose['knee_bend'] # so feet swing up a bit in air
    shank_rot = np.array([[np.cos(shank_angle), -np.sin(shank_angle)],
                          [np.sin(shank_angle),  np.cos(shank_angle)]])
    pts[la] = pts[lk] + shank_len * np.matmul(shank_rot, np.array([0, -1]))

    # Right leg
    rh = 10; rk = 12; ra = 14
    right_knee_bend = pose['knee_bend']
    rot = np.array([[np.cos(right_knee_bend), -np.sin(right_knee_bend)],
                    [np.sin(right_knee_bend),  np.cos(right_knee_bend)]])
    # Thigh
    thigh_dir = np.matmul(rot, np.array([0, -1]))
    pts[rk] = pts[rh] + thigh_len * thigh_dir
    # Shank
    shank_angle = 0.05 + 0.7*pose['knee_bend']
    shank_rot = np.array([[np.cos(shank_angle), -np.sin(shank_angle)],
                          [np.sin(shank_angle),  np.cos(shank_angle)]])
    pts[ra] = pts[rk] + shank_len * np.matmul(shank_rot, np.array([0, -1]))

    # Shoulders Y shift with pose
    lsh = 2; rsh = 3
    shoulder_shift = 0.03*np.sin(np.pi*0.5*(pose['root_x']))     # slight up/down with horizontal move
    pts[lsh,1] += shoulder_shift
    pts[rsh,1] += shoulder_shift

    # Elbow/hand: swing arms (mostly at shoulder)
    # Use a swing parameter "arms_back" - positive = back, negative = forward/up
    lel, lwr = 4, 6
    rel, rwr = 5, 7
    # Arm lengths as baseline
    upper_len = np.linalg.norm(SKELETON[4]-SKELETON[2])
    lower_len = np.linalg.norm(SKELETON[6]-SKELETON[4])
    # Shoulder to elbow: start downward, swing back/forward in jump
    # Angle from vertical: arms_back (- = forward, + = backward)
    # Left
    base_sh_angle = np.pi/3  # 60deg down for standing
    arm_angle = base_sh_angle + pose['arms_back']
    sh_rot = np.array([[np.cos(arm_angle), -np.sin(arm_angle)],
                       [np.sin(arm_angle),  np.cos(arm_angle)]])
    pts[lel] = pts[lsh] + upper_len * np.matmul(sh_rot, np.array([0, -1]))
    # Elbow to wrist: another gently bent angle, may vary a little in air
    elw_angle = np.pi/10 + 0.10*pose['arms_back']
    elw_rot = np.array([[np.cos(elw_angle), -np.sin(elw_angle)],
                        [np.sin(elw_angle),  np.cos(elw_angle)]])
    pts[lwr] = pts[lel] + lower_len * np.matmul(elw_rot, np.array([0, -1]))
    # Right
    arm_angle_r = -base_sh_angle + pose['arms_back']
    sh_rot_r = np.array([[np.cos(arm_angle_r), -np.sin(arm_angle_r)],
                         [np.sin(arm_angle_r),  np.cos(arm_angle_r)]])
    pts[rel] = pts[rsh] + upper_len * np.matmul(sh_rot_r, np.array([0, -1]))
    elw_rot_r = np.array([[np.cos(elw_angle), -np.sin(elw_angle)],
                          [np.sin(elw_angle),  np.cos(elw_angle)]])
    pts[rwr] = pts[rel] + lower_len * np.matmul(elw_rot_r, np.array([0, -1]))

    # ~Neck and head: head moves up a little in jump
    # Head follows neck, with slight upward tilt
    neck = 1; head = 0
    head_dir = np.array([0, 1])
    neck_head_len = np.linalg.norm(SKELETON[0]-SKELETON[1])
    pts[head] = pts[neck] + neck_head_len * head_dir

    # Final: optionally add tiny "happy" head-motion or feet swing, but keep biomechanically plausible!
    return pts

# Prepare animation
fig, ax = plt.subplots(figsize=(3.2, 6.4), dpi=100)
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax.set_facecolor('black')
ax.set_xlim(-0.8, 2.0)
ax.set_ylim(-0.25, 2.1)
ax.axis('off')

# Plot scattar baseline for initialization
pts0 = SKELETON
dots, = ax.plot(pts0[:,0], pts0[:,1], 'o', color='white', markersize=8)

def animate(i):
    t = i / N_FRAMES
    tmod = t % 1.0
    pose = jump_motion(tmod)
    pts = apply_pose(pose)
    dots.set_data(pts[:,0], pts[:,1])
    return (dots,)

ani = animation.FuncAnimation(
    fig, animate, frames=N_FRAMES, interval=1000/FPS, blit=True
)

plt.show()
