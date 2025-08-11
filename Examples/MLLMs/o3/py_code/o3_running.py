
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------------------- configuration ---------------------------- #
FPS               = 60          # frames‐per‐second for the animation
DURATION          = 10          # seconds
TOTAL_FRAMES      = FPS * DURATION
STEP_RATE         = 2.7         # running steps per second (≈ 162 spm)
LATERAL_OFFSET    = 0.06        # small x–offset that separates left / right points
GROUND_Y          = -0.15       # y position that approximates the ground
DOT_SIZE          = 70          # scatter size for the dots
DOT_COLOR         = 'white'     # colour of the dots
BG_COLOR          = 'black'     # background colour
VELOCITY          = 0.025       # forward speed (units / frame)

# ---------------------------- segment lengths (in arbitrary units) ----- #
TORSO_LEN         = 0.75        # hip → shoulder
NECK_LEN          = 0.12        # shoulder → neck
HEAD_LEN          = 0.18        # neck → top of head
UPPER_ARM_LEN     = 0.35
FOREARM_LEN       = 0.30
THIGH_LEN         = 0.50
SHANK_LEN         = 0.48

# indices for the 15 dots
HEAD, NECK, SL, SR, EL, ER, WL, WR, PELV, HL, HR, KL, KR, AL, AR = range(15)

def running_pose(t):
    """
    Compute 2-D coordinates (x, y) for the 15 point-lights that represent a
    running human at time *t* (seconds).
    A simple kinematic model is used – sinusoidal hip & shoulder angles as well
    as speed-dependent knee / elbow flexion – to create a smooth, biologically
    plausible motion.
    """

    phi = 2 * np.pi * STEP_RATE * t        # phase angle of the gait cycle
    x_pelvis = VELOCITY * FPS * t          # forward translation of the runner
    y_pelvis = 0.05 * np.sin(2 * phi)      # small vertical COM oscillation

    # ---------------------------- hip (leg) angles ---------------------------- #
    hip_l = np.deg2rad(30) * np.sin(phi)           # left hip          (±30°)
    hip_r = np.deg2rad(30) * np.sin(phi + np.pi)   # right hip (π-shift)

    # knee flexion increases when the leg is swung forward (hip angle > 0)
    knee_l = np.deg2rad(20 + 35 * (np.clip(np.sin(phi), 0, 1)))
    knee_r = np.deg2rad(20 + 35 * (np.clip(np.sin(phi + np.pi), 0, 1)))

    # ---------------------------- shoulder (arm) angles ----------------------- #
    sh_l = np.deg2rad(35) * np.sin(phi + np.pi)  # left shoulder swings opposite leg
    sh_r = np.deg2rad(35) * np.sin(phi)

    # elbow flexion: arm forward ⇒ elbow bent (≈ 90°), back swing ⇒ straighter
    elbow_l = np.deg2rad(70 + 50 * (1 - np.clip(np.sin(phi + np.pi), -1, 0)))
    elbow_r = np.deg2rad(70 + 50 * (1 - np.clip(np.sin(phi), -1, 0)))

    # ---------------------------- build the kinematic chain ------------------- #
    # pelvis (centre)
    pelvis = np.array([x_pelvis, y_pelvis])

    # left & right hip joints (slightly separated laterally)
    hip_left  = pelvis + np.array([-LATERAL_OFFSET, 0])
    hip_right = pelvis + np.array([ LATERAL_OFFSET, 0])

    # shoulder centre is one torso length above pelvis
    shoulder_c = pelvis + np.array([0, TORSO_LEN])
    # neck & head
    neck = shoulder_c + np.array([0, NECK_LEN])
    head = neck        + np.array([0, HEAD_LEN])

    # individual shoulders (small lateral displacement so both are visible)
    shoulder_l = shoulder_c + np.array([-LATERAL_OFFSET, 0])
    shoulder_r = shoulder_c + np.array([ LATERAL_OFFSET, 0])

    # ---------------------------- legs ---------------------------------------- #
    # Left knee
    knee_l_vec = np.array([np.sin(hip_l), -np.cos(hip_l)]) * THIGH_LEN
    knee_left  = hip_left + knee_l_vec
    # Left ankle
    shank_angle_l = hip_l - (np.pi - knee_l)      # relative orientation
    ankle_l_vec   = np.array([np.sin(shank_angle_l), -np.cos(shank_angle_l)]) * SHANK_LEN
    ankle_left    = knee_left + ankle_l_vec

    # Right leg
    knee_r_vec  = np.array([np.sin(hip_r), -np.cos(hip_r)]) * THIGH_LEN
    knee_right  = hip_right + knee_r_vec
    shank_angle_r = hip_r - (np.pi - knee_r)
    ankle_r_vec = np.array([np.sin(shank_angle_r), -np.cos(shank_angle_r)]) * SHANK_LEN
    ankle_right = knee_right + ankle_r_vec

    # Prevent feet going below ground for visual tidiness
    ankle_left [1]  = max(ankle_left [1],  GROUND_Y)
    ankle_right[1]  = max(ankle_right[1], GROUND_Y)

    # ---------------------------- arms ---------------------------------------- #
    # Left elbow & wrist
    elbow_l_vec = np.array([np.sin(sh_l), -np.cos(sh_l)]) * UPPER_ARM_LEN
    elbow_left  = shoulder_l + elbow_l_vec
    fore_l_angle = sh_l - (np.pi - elbow_l)       # elbow bend orientation
    wrist_l_vec  = np.array([np.sin(fore_l_angle), -np.cos(fore_l_angle)]) * FOREARM_LEN
    wrist_left   = elbow_left + wrist_l_vec

    # Right
    elbow_r_vec = np.array([np.sin(sh_r), -np.cos(sh_r)]) * UPPER_ARM_LEN
    elbow_right = shoulder_r + elbow_r_vec
    fore_r_angle = sh_r - (np.pi - elbow_r)
    wrist_r_vec  = np.array([np.sin(fore_r_angle), -np.cos(fore_r_angle)]) * FOREARM_LEN
    wrist_right  = elbow_right + wrist_r_vec

    # ---------------------------- collect all joints -------------------------- #
    joints = np.vstack([
        head,          #  0
        neck,          #  1
        shoulder_l,    #  2
        shoulder_r,    #  3
        elbow_left,    #  4
        elbow_right,   #  5
        wrist_left,    #  6
        wrist_right,   #  7
        pelvis,        #  8
        hip_left,      #  9
        hip_right,     # 10
        knee_left,     # 11
        knee_right,    # 12
        ankle_left,    # 13
        ankle_right    # 14
    ])
    return joints

# ---------------------------- figure & animation setup ------------------ #
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(-1, 3)         # will be adjusted during animation
ax.set_ylim(-0.5, 2.2)
ax.set_aspect('equal')
ax.axis('off')

scatter = ax.scatter([], [], s=DOT_SIZE, c=DOT_COLOR)

def init():
    scatter.set_offsets(np.zeros((15, 2)))
    return scatter,

def update(frame):
    t = frame / FPS
    joints = running_pose(t)
    scatter.set_offsets(joints)
    # keep the runner roughly centred in view
    ax.set_xlim(joints[PELV, 0] - 1, joints[PELV, 0] + 1.8)
    return scatter,

anim = FuncAnimation(fig, update, frames=TOTAL_FRAMES,
                     init_func=init, interval=1000/FPS, blit=True)

if __name__ == '__main__':
    plt.show()
