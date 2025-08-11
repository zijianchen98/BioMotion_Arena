
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
FPS = 60
DURATION = 2.0     # seconds per jump
FRAMES = int(FPS * DURATION)
LOOPS = 2
FIGSIZE = (5, 8)
BG_COLOR = 'black'
POINT_COLOR = 'white'
POINT_SIZE = 80

# Define point-light marker locations (relative to "body root") at static reference pose (upright)
# 0-head, 1-rshoulder, 2-neck, 3-lshoulder, 4-relbow, 5-lelbow, 6-rwrist, 7-lwrist, 8-pelvis, 
# 9-rhip, 10-lhip, 11-rknee, 12-lknee, 13-rankle, 14-lankle
#          x      y
MARKERS = np.array([
    [0.00,  1.00],  # head
    [0.17,  0.85],  # rshoulder
    [0.00,  0.80],  # neck
    [-0.17, 0.85],  # lshoulder
    [0.31,  0.60],  # relbow
    [-0.31, 0.60],  # lelbow
    [0.36,  0.37],  # rwrist
    [-0.36, 0.37],  # lwrist
    [0.00,  0.55],  # pelvis (root)
    [0.14,  0.52],  # rhip
    [-0.14, 0.52],  # lhip
    [0.18,  0.21],  # rknee
    [-0.18, 0.21],  # lknee
    [0.18, -0.12],  # rankle
    [-0.18, -0.12], # lankle
])

# Keypoint indices for clarity
HEAD    = 0
RS      = 1
NECK    = 2
LS      = 3
RE      = 4
LE      = 5
RW      = 6
LW      = 7
PELVIS  = 8
RHIP    = 9
LHIP    = 10
RKNEE   = 11
LKNEE   = 12
RANKLE  = 13
LANKLE  = 14

# Animation parameters for "jumping forward":
#
# The whole body performs a parabolic jump (up/forward, then down), coordinating extension and flexion.
# Timing:
# - takeoff: initial squat, then knee/hip/shoulder extension
# - airborne: body extended, arms up
# - landing: legs start to flex, arms come down
#
# Each point is locally articulated from the pelvis using joint angles.
# The root (pelvis) follows a ballistic trajectory.

# Segment lengths (relative units), estimated from marker template
len_neck = 0.25
len_head = 0.17
len_shld = 0.18
len_uparm = 0.27
len_loarm = 0.27
len_hip = 0.16
len_uprleg = 0.36
len_loleg = 0.30
len_ankle = 0.08

# Helper functions for constructing skeleton pose from joint angles
def angle2xy(origin, length, angle):
    """Compute (x,y) from origin, length, and angle in radians."""
    x, y = origin
    return np.array([x + length * np.cos(angle), y + length * np.sin(angle)])

def pose_markers(joint_angles, pelvis_xy):
    """
    Given joint angles (dict) and pelvis xy, returns the positions of all 15 point-lights.
    joint_angles: dict of NA (see below)
    pelvis_xy: global x/y (np array 2,)
    Returns: 15x2 array
    """
    q = joint_angles
    res = np.zeros((15,2))

    # Torso: draw pelvis->neck->head
    # Define pelvis, neck, head
    res[PELVIS] = pelvis_xy
    res[NECK] = angle2xy(res[PELVIS], len_neck, q['torso'])
    res[HEAD] = angle2xy(res[NECK], len_head, q['torso'])

    # Shoulders
    r_shld_xy = angle2xy(res[NECK], len_shld, q['torso'] + q['r_shoulder'])
    l_shld_xy = angle2xy(res[NECK], len_shld, q['torso'] + q['l_shoulder'])
    res[RS] = r_shld_xy
    res[LS] = l_shld_xy

    # Right arm
    r_elbow = angle2xy(r_shld_xy, len_uparm, q['torso'] + q['r_shoulder'] + q['r_elbow'])
    r_wrist = angle2xy(r_elbow, len_loarm, q['torso'] + q['r_shoulder'] + q['r_elbow'] + q['r_wrist'])
    res[RE] = r_elbow
    res[RW] = r_wrist

    # Left arm
    l_elbow = angle2xy(l_shld_xy, len_uparm, q['torso'] + q['l_shoulder'] + q['l_elbow'])
    l_wrist = angle2xy(l_elbow, len_loarm, q['torso'] + q['l_shoulder'] + q['l_elbow'] + q['l_wrist'])
    res[LE] = l_elbow
    res[LW] = l_wrist

    # Hips
    r_hip_xy = angle2xy(res[PELVIS], len_hip, q['torso'] + q['r_hip'])
    l_hip_xy = angle2xy(res[PELVIS], len_hip, q['torso'] + q['l_hip'])
    res[RHIP] = r_hip_xy
    res[LHIP] = l_hip_xy

    # Right leg
    r_knee = angle2xy(r_hip_xy, len_uprleg, q['torso'] + q['r_hip'] + q['r_knee'])
    r_ankle = angle2xy(r_knee, len_loleg, q['torso'] + q['r_hip'] + q['r_knee'] + q['r_ankle'])
    res[RKNEE] = r_knee
    res[RANKLE] = r_ankle

    # Left leg
    l_knee = angle2xy(l_hip_xy, len_uprleg, q['torso'] + q['l_hip'] + q['l_knee'])
    l_ankle = angle2xy(l_knee, len_loleg, q['torso'] + q['l_hip'] + q['l_knee'] + q['l_ankle'])
    res[LKNEE] = l_knee
    res[LANKLE] = l_ankle

    return res

# Trajectory and pose generator for jumping forward
def trajectory_and_pose(t):
    """
    Returns pelvis_xy and joint angles at time t (0...DURATION)
    """
    # 1. Root forward motion (pelvis): x0 + v * t
    jump_length = 0.65  # how far forward (in body lengths) in one jump
    x0 = -0.4
    x1 = x0 + jump_length
    p = t / DURATION
    pelvis_x = x0 * (1-p) + x1 * p

    # 2. Root jump (vertical): y = y0 + V0*t - 0.5*g*t^2 (parabola)
    y0 = 0.0
    jump_height = 0.45
    # t in [0, DURATION], peak at DURATION/2
    # So, V0 = g * (DURATION/2)
    g = 2*jump_height/(DURATION/2)**2
    v0 = g * (DURATION/2)
    dy = v0*t - 0.5*g*t**2
    pelvis_y = y0 + dy + 0.55    # raised above ground

    pelvis_xy = np.array([pelvis_x, pelvis_y])

    # 3. Joint angle trajectories (phase-based; 𝜃(t))
    phase = t / DURATION

    # Torso:
    torso_base = np.pi/2   # upright (pi/2)
    # Torso tilts forward during takeoff, back extending in air
    torso = torso_base + np.deg2rad(10 * np.sin(np.pi * phase))

    # Shoulders/hips swing to indicate energy and happiness
    r_shoulder = -np.deg2rad(7 + 17 * np.sin(2 * np.pi * phase))
    l_shoulder = np.deg2rad(7 + 17 * np.sin(2 * np.pi * phase + 0.6))

    # Arms: push up/fly, then down in landing
    r_elbow = np.deg2rad(-10 + 60 * np.sin(np.pi*phase - 0.25))
    l_elbow = np.deg2rad(-10 + 60 * np.sin(np.pi*phase - 0.25))
    r_wrist = np.deg2rad(0 + 40 * np.sin(np.pi*phase - 0.6))
    l_wrist = np.deg2rad(0 + 40 * np.sin(np.pi*phase - 1.0))

    # Hips: flex during squat pre-jump, extend in air, flex on landing
    r_hip = np.deg2rad( -43 * np.sin(np.pi * phase) - 3*np.cos(2*np.pi*phase) )
    l_hip = np.deg2rad( -43 * np.sin(np.pi * phase + 0.22) - 3*np.cos(2*np.pi*phase+0.2) )

    # Knees: squat before takeoff, extend in air, flex to absorb landing
    r_knee = np.deg2rad( 68 * np.sin(np.pi * phase - 0.15) )
    l_knee = np.deg2rad( 68 * np.sin(np.pi * phase - 0.18) )

    # Ankles: flex-extend
    r_ankle = np.deg2rad( -16 * np.sin(np.pi * phase + 0.55) )
    l_ankle = np.deg2rad( -16 * np.sin(np.pi * phase + 0.52) )

    joint_angles = {
        'torso': torso,
        'r_shoulder': r_shoulder,
        'l_shoulder': l_shoulder,
        'r_elbow': r_elbow,
        'l_elbow': l_elbow,
        'r_wrist': r_wrist,
        'l_wrist': l_wrist,
        'r_hip': r_hip,
        'l_hip': l_hip,
        'r_knee': r_knee,
        'l_knee': l_knee,
        'r_ankle': r_ankle,
        'l_ankle': l_ankle,
    }
    return pelvis_xy, joint_angles

# Create animation
fig, ax = plt.subplots(figsize=FIGSIZE)
ax.set_facecolor(BG_COLOR)
plt.axis('off')

scat = ax.scatter(
    MARKERS[:,0], MARKERS[:,1],
    s=POINT_SIZE, c=POINT_COLOR, linewidth=0, edgecolor=None,
    zorder=10, marker='o'
)

# Axes limits (big enough for whole jump)
plt.xlim(-1.0, 1.0)
plt.ylim(-0.25, 1.45)

def animate(frame):
    # Compute time
    t = (frame % FRAMES) / FPS
    pelvis_xy, angles = trajectory_and_pose(t)
    xy = pose_markers(angles, pelvis_xy)
    scat.set_offsets(xy)
    return scat,

ani = animation.FuncAnimation(
    fig, animate,
    frames=FRAMES*LOOPS,
    interval=1000/FPS,
    blit=True,
    repeat=True
)

plt.show()
