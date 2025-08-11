
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---- PARAMETERS ----
N_FRAMES = 120       # Animation cycle
FPS = 30
POINT_SIZE = 56      # White dot size, matches example
BG_COLOR = 'black'
PT_COLOR = 'white'
WINDOW_SIZE = (6, 10)

# ---- BODY MODEL: 15-DOF Running Woman Biological Motion ----
# Joints (in order): [Head, RShoulder, LShoulder, Relbow, Lelbow, RWrist, LWrist,
#                     Torso, RHip, LHip, RKnee, LKnee, RAnkle, LAnkle, Pelvis]
#                 0     1          2         3       4       5       6
#                 7     8          9        10      11      12      13      14

# Limb structure for running, slightly feminine, light effusive stride

# Segment lengths (arbitrary units, stylized for human proportions)
HEAD_HEIGHT = 0.35
SHOULDER_WIDTH = 0.5
UPPER_ARM = 0.35
FOREARM = 0.30
TORSO_LEN = 0.7
HIP_WIDTH = 0.35
THIGH = 0.6
SHANK = 0.58
PELVIS_HEIGHT = 0.15

# Helper for 2D segment
def pol2cart(l, theta):
    return l * np.cos(theta), l * np.sin(theta)

def get_marker_positions(phase):
    """
    Returns: Nx2 matrix where N=15, containing:
    [head, r-shoulder, l-shoulder, r-elbow, l-elbow, r-wrist, l-wrist,
    torso, r-hip, l-hip, r-knee, l-knee, r-ankle, l-ankle, pelvis]
    """
    # Gait cycle phase (from 0...1), use for left/right alternation
    ph = phase * 2 * np.pi

    # Torso Y bounces with step, forward motion linearly increases
    base_y = 4 + 0.15 * np.sin(ph)
    base_x = phase * 3.5  # Subject runs from left to right

    # Hip/pelvis: slight oscillation, rotate left/right around forward axis
    pelvis_x = base_x
    pelvis_y = base_y - 1.4*(PAL := PELVIS_HEIGHT)
    pelvis = np.array([pelvis_x, pelvis_y])

    # Hip points
    rhip_x = pelvis_x - HIP_WIDTH/2 * np.cos(np.pi/12)
    lhip_x = pelvis_x + HIP_WIDTH/2 * np.cos(np.pi/12)
    rhip_y = pelvis_y
    lhip_y = pelvis_y
    rhip = np.array([rhip_x, rhip_y])
    lhip = np.array([lhip_x, lhip_y])

    # Torso
    # Torso angle swings slightly, accentuated for running
    torso_ang = (np.pi/2) + 0.08 * np.sin(ph - 0.2)
    torso_top_x, torso_top_y = pol2cart(TORSO_LEN, torso_ang)
    torso = np.array([pelvis_x, pelvis_y]) + np.array([torso_top_x, torso_top_y])

    # Shoulders
    shoulder_y = torso[1] + 0.07 * np.sin(ph+0.7)
    rshoulder = np.array([torso[0] - SHOULDER_WIDTH / 2, shoulder_y])
    lshoulder = np.array([torso[0] + SHOULDER_WIDTH / 2, shoulder_y])

    # Head (above shoulder center)
    head = np.array([torso[0], shoulder_y + HEAD_HEIGHT])

    # Arms swing - right and left out of phase
    # Add pronounced, smooth happy swing to arms
    arm_amp = 1.00
    foreamp = 1.05
    # Right arm
    ra_theta = -0.8 + arm_amp * 0.75 * np.sin(ph - .10)
    la_theta = -0.8 + arm_amp * 0.75 * np.sin(ph + np.pi - .15)
    # Elbows:
    relbow_vec = pol2cart(UPPER_ARM, ra_theta)
    lelbow_vec = pol2cart(UPPER_ARM, la_theta)
    relbow = rshoulder + relbow_vec
    lelbow = lshoulder + lelbow_vec
    # Forearm (with higher amplitude for "happy" gesture on wrist)
    rwrist_angle = ra_theta - 0.25 * np.cos(ph - .25)
    lwrist_angle = la_theta - 0.25 * np.cos(ph + np.pi - .23)
    rwrist_vec = pol2cart(FOREARM, rwrist_angle)
    lwrist_vec = pol2cart(FOREARM, lwrist_angle)
    rwrist = relbow + np.array(rwrist_vec)
    lwrist = lelbow + np.array(lwrist_vec)

    # Legs swing in phase with running action
    step_ang = 0.92 * np.sin(ph)  # Hip flex/ext.

    # Right leg: phase 0 = swing, pi = stance
    rhip_off = 0.09 * np.sin(ph)
    rknee_theta = -0.63 + 1.10 * np.sin(ph)  # thigh
    lknee_theta = -0.63 + 1.10 * np.sin(ph + np.pi)  # thigh
    # Knees: move from hip with thigh
    rknee_vec = pol2cart(THIGH, rknee_theta)
    lknee_vec = pol2cart(THIGH, lknee_theta)
    rknee = rhip + np.array(rknee_vec)
    lknee = lhip + np.array(lknee_vec)

    # Shank: flex much during swing, less during stance
    rshank_theta = (-0.12 + 1.3 * np.sin(ph + np.pi/3))
    lshank_theta = (-0.12 + 1.3 * np.sin(ph + np.pi + np.pi/3))
    rankle_vec = pol2cart(SHANK, rknee_theta + rshank_theta)
    lankle_vec = pol2cart(SHANK, lknee_theta + lshank_theta)
    rankle = rknee + np.array(rankle_vec)
    lankle = lknee + np.array(lankle_vec)

    # Stack all marker positions in required order
    points = np.stack([
        head,              # 0
        rshoulder, lshoulder,
        relbow, lelbow,
        rwrist, lwrist,
        torso,             # 7
        rhip, lhip,        # 8, 9
        rknee, lknee,      # 10, 11
        rankle, lankle,    # 12, 13
        pelvis             # 14
    ])

    return points

# ---- PLOTTING ----
fig, ax = plt.subplots(figsize=WINDOW_SIZE)
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(0, 6)
ax.set_ylim(0, 10)
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Initialize scatter points
scat = ax.scatter([], [], s=POINT_SIZE, color=PT_COLOR, edgecolors='none', zorder=10)

def init():
    scat.set_offsets(np.zeros((15,2)))
    return (scat,)

def animate(i):
    t = (i % N_FRAMES) / N_FRAMES
    pts = get_marker_positions(t)
    # Loop: when subject leaves frame, loop back
    wrap_pts = pts.copy()
    wrap_pts[:,0] = (wrap_pts[:,0] - (t)*3.5) % 6
    scat.set_offsets(wrap_pts)
    scat.set_edgecolor('none')
    return (scat,)

ani = animation.FuncAnimation(
    fig, animate, frames=N_FRAMES, interval=1000/FPS, blit=True, init_func=init
)

plt.show()
