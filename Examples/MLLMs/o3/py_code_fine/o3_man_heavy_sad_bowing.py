
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------------------------------------------------------
#  Configuration
# -----------------------------------------------------------------------------
FPS                 = 30       # frames-per-second of the animation
CYCLE_DURATION_SEC  = 2.0      # how long one complete bow takes (seconds)
N_FRAMES            = int(FPS * CYCLE_DURATION_SEC)

# Skeleton dimensions  (arbitrary but proportionate, “1.0” ≈ length of the torso)
TORSO_LEN           = 1.0
HEAD_LEN            = 0.25
SHOULDER_OFFSET_X   = 0.30
HIP_OFFSET_X        = 0.20
UPPER_ARM_LEN       = 0.45
FORE_ARM_LEN        = 0.45
UPPER_LEG_LEN       = 0.60
LOWER_LEG_LEN       = 0.60

# Maximum forward lean (radians).  0 → upright; positive → bend forward
LEAN_MAX            = np.deg2rad(55.0)        # ≈ 55° bow

# Slight knee bend while leaning forward
KNEE_BEND_MAX       = np.deg2rad(25)

# -----------------------------------------------------------------------------
#  Forward-kinematics helper
# -----------------------------------------------------------------------------
def rot(vec, theta):
    """
    Rotate a 2-D vector by angle `theta` (radians)  (counter-clockwise).
    """
    c, s = np.cos(theta), np.sin(theta)
    x, y = vec
    return np.array([c * x - s * y,
                     s * x + c * y])

# -----------------------------------------------------------------------------
#  Compute the 15 joint locations for a given phase (0 … 1)
# -----------------------------------------------------------------------------
def get_pose(phase):
    """
    phase ∈ [0,1]   0   → start upright
                    0.5 → maximally bent forward
                    1   → back upright                (sinusoidal cycle)
                    
    Returns an (15,2) array with 2-D joint coordinates.
    """
    # -----------------------------------------------------------------
    # 1) Global parameters that vary over the cycle
    # -----------------------------------------------------------------
    lean       = LEAN_MAX * np.sin(np.pi * 2 * phase) * 0.5 + LEAN_MAX * 0.5 * (1 - np.cos(np.pi * 2 * phase))
    # The above curve (half-wave raised sinusoid)  makes the movement
    # slower at the turn-arounds – looks more “biological”.
    knee_bend  = KNEE_BEND_MAX * np.abs(np.sin(np.pi * phase))
    
    # -----------------------------------------------------------------
    # 2) Static body anchors
    # -----------------------------------------------------------------
    pelvis     = np.array([0.0, 0.0])             # origin
    left_hip   = pelvis + np.array([-HIP_OFFSET_X, 0.0])
    right_hip  = pelvis + np.array([ HIP_OFFSET_X, 0.0])

    # -----------------------------------------------------------------
    # 3) Torso  (pelvis → neck → head)
    # -----------------------------------------------------------------
    neck       = pelvis + rot(np.array([0,  TORSO_LEN]), -lean)
    head       = neck   + rot(np.array([0,  HEAD_LEN ]), -lean)
    
    # -----------------------------------------------------------------
    # 4) Shoulders & arms  (arms hang straight down, so they do not lean)
    # -----------------------------------------------------------------
    left_shoulder  = neck + np.array([-SHOULDER_OFFSET_X, 0])
    right_shoulder = neck + np.array([ SHOULDER_OFFSET_X, 0])
    
    # Arms: vertical world direction (gravity) regardless of torso lean
    arm_down        = np.array([0, -UPPER_ARM_LEN])
    forearm_down    = np.array([0, -FORE_ARM_LEN])
    
    left_elbow  = left_shoulder  + arm_down
    right_elbow = right_shoulder + arm_down
    left_wrist  = left_elbow     + forearm_down
    right_wrist = right_elbow    + forearm_down
    
    # -----------------------------------------------------------------
    # 5) Legs
    # -----------------------------------------------------------------
    # Thighs: straight down (but can sway a little with knee bend)
    thigh_down  = rot(np.array([0, -UPPER_LEG_LEN]), 0.15 * np.sin(np.pi * 2 * phase))
    
    left_knee   = left_hip  + thigh_down
    right_knee  = right_hip + thigh_down
    
    # Lower legs: rotated back depending on knee_bend
    shin_vec    = rot(np.array([0, -LOWER_LEG_LEN]), knee_bend)
    
    left_ankle  = left_knee  + shin_vec
    right_ankle = right_knee + shin_vec
    
    # -----------------------------------------------------------------
    # 6) Assemble   (exactly 15 points)
    # -----------------------------------------------------------------
    joints = np.vstack([
        head,                   #  0
        neck,                   #  1
        left_shoulder,          #  2
        right_shoulder,         #  3
        left_elbow,             #  4
        right_elbow,            #  5
        left_wrist,             #  6
        right_wrist,            #  7
        pelvis,                 #  8
        left_hip,               #  9
        right_hip,              # 10
        left_knee,              # 11
        right_knee,             # 12
        left_ankle,             # 13
        right_ankle             # 14
    ])
    return joints


# -----------------------------------------------------------------------------
#  Matplotlib animation setup
# -----------------------------------------------------------------------------
plt.rcParams['figure.facecolor'] = 'black'

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('equal')
ax.axis('off')

# Some generous limits so everything stays visible
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.2, 2.2)

# The scatter that will hold our 15 white point-lights
scatter = ax.scatter([], [], s=50, c='white')

# -----------------------------------------------------------------------------
#  Frame-update callback
# -----------------------------------------------------------------------------
def update(frame):
    # Where in the cycle are we?  (0 … 1)
    phase = (frame % N_FRAMES) / N_FRAMES
    joints = get_pose(phase)
    scatter.set_offsets(joints)
    return scatter,

# -----------------------------------------------------------------------------
#  Create & start the animation
# -----------------------------------------------------------------------------
anim = FuncAnimation(fig,
                     update,
                     frames=np.arange(0, 10 * N_FRAMES),  # run for 10 cycles
                     interval=1000 / FPS,
                     blit=True)

plt.show()
