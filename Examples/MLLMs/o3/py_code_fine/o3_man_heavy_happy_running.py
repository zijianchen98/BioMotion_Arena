
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------
NUM_POINTS         = 15          # must stay 15
FPS                = 30          # frames-per-second
SECS               = 10          # total duration
TOTAL_FRAMES       = SECS * FPS
OMEGA              = 2 * np.pi   # one “stride” each second
BG_COLOR           = 'black'
FG_COLOR           = 'white'

# ------------------------------------------------------------
# Helper: forward kinematics for a very simple stick figure
# ------------------------------------------------------------
def skeleton_xyz(t):
    """
    Return 15×2 array of x,y joint coordinates at time t (seconds).
    The figure ‘runs in place’.  All maths here is deliberately
    lightweight – the goal is simply a smooth, coherent display
    of biological motion rather than biomechanical exactitude.
    """
    # Basic body landmarks (static in the figure’s coordinate frame)
    hip_y        = 0.0       # origin
    shoulder_y   = hip_y + 1.2
    head_y       = shoulder_y + 0.8
    hip_w        = 0.30
    shoulder_w   = 0.45

    # Segment lengths
    thigh_len, shin_len     = 0.90, 0.90
    upper_arm_len, fore_len = 0.55, 0.55

    # Centre anchors
    hip_ctr      = np.array([0.0, hip_y])
    sh_ctr       = np.array([0.0, shoulder_y])

    # Oscillatory parameters ------------------------------------------------
    stride_phase = OMEGA * t
    # Legs
    thigh_R = np.deg2rad(-20)  + np.deg2rad(40)  * np.sin(stride_phase)        # Right thigh swings forward as sin
    thigh_L = np.deg2rad(-20)  + np.deg2rad(40)  * np.sin(stride_phase + np.pi)
    knee_R  = np.deg2rad(60)   - np.deg2rad(25)  * np.sin(stride_phase)        # knee flexion – out of phase a bit
    knee_L  = np.deg2rad(60)   - np.deg2rad(25)  * np.sin(stride_phase + np.pi)
    # Arms (anti-phase with legs)
    upp_R   = np.deg2rad( 30)  * np.sin(stride_phase + np.pi) * 0.7
    upp_L   = np.deg2rad( 30)  * np.sin(stride_phase)         * 0.7
    elb_R   = np.deg2rad(90)   - np.deg2rad(20)  * np.sin(stride_phase + np.pi)
    elb_L   = np.deg2rad(90)   - np.deg2rad(20)  * np.sin(stride_phase)

    # Compute torso points --------------------------------------------------
    head    = np.array([0.0               , head_y     ])
    sh_R    = np.array([ shoulder_w / 2.0 , shoulder_y ])
    sh_L    = np.array([-shoulder_w / 2.0 , shoulder_y ])
    hip_R   = np.array([ hip_w / 2.0      , hip_y      ])
    hip_L   = np.array([-hip_w / 2.0      , hip_y      ])

    # Legs ------------------------------------------------------------------
    # Right leg
    knee_R_pt   = hip_R + np.array([ np.sin(thigh_R), -np.cos(thigh_R)]) * thigh_len
    ankle_R_pt  = knee_R_pt + np.array([ np.sin(thigh_R + knee_R),
                                        -np.cos(thigh_R + knee_R)]) * shin_len
    # Left leg
    knee_L_pt   = hip_L + np.array([ np.sin(thigh_L), -np.cos(thigh_L)]) * thigh_len
    ankle_L_pt  = knee_L_pt + np.array([ np.sin(thigh_L + knee_L),
                                        -np.cos(thigh_L + knee_L)]) * shin_len

    # Arms ------------------------------------------------------------------
    # Right arm
    elbow_R_pt  = sh_R + np.array([ np.sin(upp_R), -np.cos(upp_R)]) * upper_arm_len
    wrist_R_pt  = elbow_R_pt + np.array([ np.sin(upp_R + elb_R),
                                         -np.cos(upp_R + elb_R)]) * fore_len
    # Left arm
    elbow_L_pt  = sh_L + np.array([ np.sin(upp_L), -np.cos(upp_L)]) * upper_arm_len
    wrist_L_pt  = elbow_L_pt + np.array([ np.sin(upp_L + elb_L),
                                         -np.cos(upp_L + elb_L)]) * fore_len

    # Assemble the vector (15 points) ---------------------------------------
    pts = np.vstack([
        head,          # 0
        sh_R, sh_L,    # 1,2
        elbow_R_pt, elbow_L_pt,        # 3,4
        wrist_R_pt, wrist_L_pt,        # 5,6
        hip_ctr := hip_ctr,            # 7 (pelvis centre)
        hip_R, hip_L,                  # 8,9
        knee_R_pt, knee_L_pt,          # 10,11
        ankle_R_pt, ankle_L_pt,        # 12,13
        sh_ctr                           # 14 (neck/base-of-neck)
    ])
    return pts

# ------------------------------------------------------------
# Build the animation
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 6), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(-2, 2)
ax.set_ylim(-2.5, 4)
ax.set_aspect('equal')
ax.axis('off')

# Scatter plot with 15 points
scat = ax.scatter([], [], s=60, c=FG_COLOR)

def init():
    scat.set_offsets(np.zeros((NUM_POINTS, 2)))
    return scat,

def update(frame):
    t        = frame / FPS
    pts      = skeleton_xyz(t)
    scat.set_offsets(pts)
    return scat,

ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES,
                    init_func=init, blit=True, interval=1000/FPS)

# ------------------------------------------------------------
# Main entry-point
# ------------------------------------------------------------
if __name__ == '__main__':
    plt.show()
