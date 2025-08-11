
import numpy as np
import matplotlib
matplotlib.use("Agg")  # non-interactive backend, safe for headless execution
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


# ----- KINEMATIC MODEL -------------------------------------------------
# Joint index map for reference (15 points total):
#  0: head
#  1: left shoulder     2: right shoulder
#  3: left elbow        4: right elbow
#  5: left wrist        6: right wrist
#  7: left hip          8: right hip
#  9: left knee        10: right knee
# 11: left ankle       12: right ankle
# 13: left toe         14: right toe


# Segment lengths (arbitrary units, consistent proportions)
THIGH_LEN   = 0.45
SHIN_LEN    = 0.45
FOOT_LEN    = 0.15
UPARM_LEN   = 0.30
FOREARM_LEN = 0.30
HEAD_OFFSET = 0.25      # shoulder → head

HIP_HEIGHT_BASE = 0.90  # average hip height (ground y == 0)


def sad_walker_pose(t, base_x):
    """
    Compute 15 (x, y) positions for the sad, heavy walker
    at phase/time t (radians) with pelvis centred on base_x.
    """
    # Slow bob of the centre of mass (hips) to mimic heaviness
    hip_y = HIP_HEIGHT_BASE + 0.05 * np.sin(2 * t)  # vertical bob (twice step frequency)

    # Horizontal hip spacing (very small – almost single point for side view)
    hip_left_x  = base_x - 0.04
    hip_right_x = base_x + 0.04

    # Shoulders & head (slumped forward / down a little)
    shoulder_y = hip_y + 0.60
    head_y     = shoulder_y + HEAD_OFFSET
    shoulder_left_x  = base_x - 0.07
    shoulder_right_x = base_x + 0.07
    head_x = base_x

    # Arm swing (opposite phase to legs, reduced amplitude & downward bias for sadness)
    arm_amp = np.radians(20)
    sh_ang_l = -0.40 + arm_amp * np.sin(t + np.pi)   # left arm
    sh_ang_r = -0.40 + arm_amp * np.sin(t)           # right arm

    # Elbows
    elbow_left_x  = shoulder_left_x  + UPARM_LEN * np.sin(sh_ang_l)
    elbow_left_y  = shoulder_y       - UPARM_LEN * np.cos(sh_ang_l)
    elbow_right_x = shoulder_right_x + UPARM_LEN * np.sin(sh_ang_r)
    elbow_right_y = shoulder_y       - UPARM_LEN * np.cos(sh_ang_r)

    # Wrists (forearms bend forward slightly)
    el_ang_off = np.radians(30)
    wr_ang_l = sh_ang_l + el_ang_off
    wr_ang_r = sh_ang_r + el_ang_off
    wrist_left_x  = elbow_left_x  + FOREARM_LEN * np.sin(wr_ang_l)
    wrist_left_y  = elbow_left_y  - FOREARM_LEN * np.cos(wr_ang_l)
    wrist_right_x = elbow_right_x + FOREARM_LEN * np.sin(wr_ang_r)
    wrist_right_y = elbow_right_y - FOREARM_LEN * np.cos(wr_ang_r)

    # Leg swing parameters
    leg_amp = np.radians(30)  # hip swing amplitude
    # Hip joint rotation (left/right opposite phase)
    hip_ang_l =  leg_amp * np.sin(t)          # radians
    hip_ang_r =  leg_amp * np.sin(t + np.pi)

    # Knee flexion – bends when leg is moving forward (heavier flex to suggest effort)
    knee_flex_l = np.radians(50) * max(0.0, np.sin(t))          # only positive half-cycle
    knee_flex_r = np.radians(50) * max(0.0, np.sin(t + np.pi))  # opposite leg

    # Knees
    knee_left_x  = hip_left_x  + THIGH_LEN * np.sin(hip_ang_l)
    knee_left_y  = hip_y       - THIGH_LEN * np.cos(hip_ang_l)
    knee_right_x = hip_right_x + THIGH_LEN * np.sin(hip_ang_r)
    knee_right_y = hip_y       - THIGH_LEN * np.cos(hip_ang_r)

    # Shank (shin) global angle = hip angle + knee flex (forward bend)
    shang_l = hip_ang_l + knee_flex_l
    shang_r = hip_ang_r + knee_flex_r

    # Ankles
    ankle_left_x  = knee_left_x  + SHIN_LEN * np.sin(shang_l)
    ankle_left_y  = knee_left_y  - SHIN_LEN * np.cos(shang_l)
    ankle_right_x = knee_right_x + SHIN_LEN * np.sin(shang_r)
    ankle_right_y = knee_right_y - SHIN_LEN * np.cos(shang_r)

    # Feet (slightly forward from ankle)
    foot_ang_l = shang_l - np.radians(10)     # small plantar flex
    foot_ang_r = shang_r - np.radians(10)
    toe_left_x  = ankle_left_x  + FOOT_LEN * np.sin(foot_ang_l)
    toe_left_y  = ankle_left_y  - FOOT_LEN * np.cos(foot_ang_l)
    toe_right_x = ankle_right_x + FOOT_LEN * np.sin(foot_ang_r)
    toe_right_y = ankle_right_y - FOOT_LEN * np.cos(foot_ang_r)

    # Pack coordinates
    points = [
        (head_x,           head_y),             # 0 head
        (shoulder_left_x,  shoulder_y),         # 1 left shldr
        (shoulder_right_x, shoulder_y),         # 2 right shldr
        (elbow_left_x,     elbow_left_y),       # 3 left elbow
        (elbow_right_x,    elbow_right_y),      # 4 right elbow
        (wrist_left_x,     wrist_left_y),       # 5 left wrist
        (wrist_right_x,    wrist_right_y),      # 6 right wrist
        (hip_left_x,       hip_y),              # 7 left hip
        (hip_right_x,      hip_y),              # 8 right hip
        (knee_left_x,      knee_left_y),        # 9 left knee
        (knee_right_x,     knee_right_y),       #10 right knee
        (ankle_left_x,     ankle_left_y),       #11 left ankle
        (ankle_right_x,    ankle_right_y),      #12 right ankle
        (toe_left_x,       toe_left_y),         #13 left toe
        (toe_right_x,      toe_right_y)         #14 right toe
    ]
    return np.array(points)


# ----- ANIMATION SETUP -------------------------------------------------
# Animation parameters
FPS       = 30
DURATION  = 6           # seconds
FRAMES    = FPS * DURATION
STEP_PER_FRAME = 0.02   # horizontal translation speed

# Matplotlib figure
fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(0, 3)       # generous horizontal space
ax.set_ylim(-0.1, 1.6)  # ground to just above head
ax.axis('off')          # No axes

# Initialise 15-point scatter
scatter = ax.scatter([], [], s=40, c='white')

def init():
    scatter.set_offsets(np.zeros((15, 2)))
    return scatter,

def update(frame):
    # Time parameter (phase) spanning multiple full gait cycles
    t = 2 * np.pi * frame / FPS * 0.75   # frequency factor ~= walk cadence
    base_x = 0.3 + STEP_PER_FRAME * frame
    pts = sad_walker_pose(t, base_x)
    scatter.set_offsets(pts)
    return scatter,

anim = FuncAnimation(fig,
                     update,
                     frames=FRAMES,
                     init_func=init,
                     interval=1000 / FPS,
                     blit=True)

# Save to GIF (pure-python Pillow writer avoids external codecs)
writer = PillowWriter(fps=FPS)
anim.save("sad_heavy_walker.gif", writer=writer)
