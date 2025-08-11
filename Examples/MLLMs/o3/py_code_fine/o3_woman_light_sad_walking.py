
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# --------------------  PARAMS  -------------------- #
FPS            = 30           # frames-per-second
DURATION       = 4            # seconds
N_FRAMES       = FPS * DURATION
OMEGA          = 2 * np.pi    # one gait-cycle per second (rad / sec)
THIGH_L        = 0.50         # metres (model units)
SHANK_L        = 0.50
UPPER_ARM_L    = 0.40
FORE_ARM_L     = 0.40
HIP_HEIGHT     = 1.00         # pelvis (y)
SHOULDER_H     = 1.60         # shoulder (y)
HEAD_H         = 1.90         # head   (y)
STEP_SPEED     = 0.015        # metres/frame  (how fast the walker travels)
HIP_SWING_A    = 0.35         # hip swing amplitude (rad)
KNEE_FLEX_A    = 0.60         # maximum knee flex   (rad)
ARM_SWING_A    = 0.50         # shoulder swing amplitude (rad)
ELBOW_FLEX     = 0.35         # fixed elbow flex (rad)

# -------------------------------------------------- #

def rot_down(angle):
    """
    Rotate the downward unit vector (0,-1) around the origin
    by ‘angle’ radians CCW and return the resulting vector.
    """
    return np.array((np.sin(angle), -np.cos(angle)))

def build_skeleton(t):
    """
    For a given global time ‘t’ (seconds) return 15 (x,y) points that
    represent one frame of a point-light ‘sad woman’ walker.
    """
    w      = OMEGA * t
    centre_x = STEP_SPEED * FPS * t                       # forward translation
    
    # ----------------  LOWER BODY  ---------------- #
    # Hip angles (front/back) – legs are out of‐phase (π).
    hip_l  =  HIP_SWING_A * np.sin(w)
    hip_r  =  HIP_SWING_A * np.sin(w + np.pi)

    # Knee flex – more flex whenever that leg is swinging forward.
    knee_l = KNEE_FLEX_A * np.clip( np.sin(w),  0, 1)
    knee_r = KNEE_FLEX_A * np.clip( np.sin(w+np.pi), 0, 1)
    
    pelvis = np.array((centre_x, HIP_HEIGHT))
    
    # Left leg
    kneeL   = pelvis + rot_down(hip_l)             * THIGH_L
    ankleL  = kneeL  + rot_down(hip_l - knee_l)    * SHANK_L
    footL   = ankleL + np.array((0.05, 0))         # tiny foot marker
    
    # Right leg
    kneeR   = pelvis + rot_down(hip_r)             * THIGH_L
    ankleR  = kneeR  + rot_down(hip_r - knee_r)    * SHANK_L
    footR   = ankleR + np.array((0.05, 0))
    
    # ----------------  UPPER BODY  ---------------- #
    shoulders = np.array((centre_x, SHOULDER_H))
    head      = np.array((centre_x, HEAD_H))
    
    # Arm (opposite phase to legs)
    sh_ang_l  = -ARM_SWING_A * np.sin(w)           # left arm swings backward when left leg forward
    sh_ang_r  = -ARM_SWING_A * np.sin(w + np.pi)
    
    elbowL = shoulders + rot_down(sh_ang_l)              * UPPER_ARM_L
    wristL = elbowL   + rot_down(sh_ang_l + ELBOW_FLEX)   * FORE_ARM_L
    
    elbowR = shoulders + rot_down(sh_ang_r)              * UPPER_ARM_L
    wristR = elbowR   + rot_down(sh_ang_r + ELBOW_FLEX)   * FORE_ARM_L
    
    # ---------------- COLLECT 15 POINTS ----------- #
    points = np.array([
        head,                 # 0
        shoulders,            # 1
        elbowL,               # 2
        elbowR,               # 3
        wristL,               # 4
        wristR,               # 5
        pelvis,               # 6
        kneeL,                # 7
        kneeR,                # 8
        ankleL,               # 9
        ankleR,               #10
        footL,                #11
        footR,                #12
        # two extra torso points for richer biological plausibility
        (shoulders + pelvis) / 2,                   # mid-torso 13
        (pelvis + (pelvis+np.array((0,-0.35))))/2   # lower-torso 14
    ])
    
    return points

# ---------------  MATPLOTLIB SET-UP  -------------- #
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_facecolor('black')
scat = ax.scatter([], [], c="white", s=30)

ax.set_xlim(-1, 1.6)
ax.set_ylim(0, 2.2)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    t      = frame / FPS
    coords = build_skeleton(t)
    scat.set_offsets(coords)
    return scat,

anim = FuncAnimation(fig,
                     update,
                     frames=N_FRAMES,
                     init_func=init,
                     interval=1000/FPS,
                     blit=True)

# --------  Display when run interactively, also save GIF  -------- #
if __name__ == "__main__":
    try:
        # Save the animation: this works on most machines without extra codecs
        anim.save("walking_point_light.gif",
                  writer=PillowWriter(fps=FPS))
        print("Animation saved to 'walking_point_light.gif'.")
    except Exception as e:
        print("Saving failed:", e)

    # Show the animation window (comment out if running headless)
    plt.show()
