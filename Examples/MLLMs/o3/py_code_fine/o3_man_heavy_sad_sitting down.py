
"""
Biological-motion point-light stimulus
Action : Heavy (over-weight) sad man sitting down
15 white dots on a black background
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --------------------------------------------------
#  Helper : produce skeleton joint positions
# --------------------------------------------------
def skeleton(frame_idx, total_frames):
    """
    Return 15×2 array with (x,y) coordinates of the joints
    at the required point of the sit-down cycle.

    The animation is periodic. 0 … total_frames/2   : sitting down
                               total_frames/2 … end : standing up
    """

    # ----------------------------------------------
    #  Normalised progress 0-1-0 using a cosine ramp
    # ----------------------------------------------
    theta      = 2 * np.pi * frame_idx / total_frames      # 0 … 2π
    progress   = (1 - np.cos(theta)) * 0.5                 # 0 … 1 … 0

    # The progress value determines how far the person has bent his hips/knees.
    # 0   → fully standing
    # 1   → fully seated
    # To make the man look heavy we make the pelvis wider and the stance larger.
    #
    # Basic anthropometry (arbitrary units – roughly metres):
    head_r      = 0.08
    shoulder_w  = 0.45
    pelvis_w    = 0.55           # wide hip for the heavy build
    upper_arm   = 0.30
    lower_arm   = 0.30
    upper_leg   = 0.45
    lower_leg   = 0.45
    spine_l     = 0.55

    # Target y positions
    ankle_y     = 0.0
    knee_y_seat = lower_leg                     # when seated the knee is at a right angle
    hip_y_seat  = lower_leg + 0.05              # almost resting on a virtual chair
    hip_y_stand = upper_leg + lower_leg         # ≈ 0.9
    spine_bend  = spine_l * (1 - 0.15*progress) # heavy person leans forward slightly

    # Blend standing ↔ seated
    hip_y   = hip_y_stand * (1 - progress) + hip_y_seat * progress
    knee_y  = hip_y - upper_leg * (1 - 0.1*progress)      # knee rises slightly on sitting
    knee_x  =  0.20 * progress                            # knees move forward

    # Ankles are kept slightly apart, farther for a heavy person
    ankle_x_L = -0.22
    ankle_x_R =  0.22

    # Knees
    knee_x_L  = -knee_x
    knee_x_R  =  knee_x

    # Hips / pelvis (centre / L / R)
    hip_x     = 0.0
    hip_x_L   = -pelvis_w / 2
    hip_x_R   =  pelvis_w / 2

    # Spine top (base of neck)
    spine_top_y = hip_y + spine_bend
    spine_top_x = 0.0

    # Shoulders
    sh_y      = spine_top_y
    sh_x_L    = -shoulder_w / 2
    sh_x_R    =  shoulder_w / 2

    # Head (just one point in the centre)
    head_y    = sh_y + head_r * 2.2
    head_x    = 0.0

    # Arms – kept loosely beside the body
    # Because the man is sad, arms hang & sway slightly
    arm_swing = 0.10 * np.sin(theta)            # simple periodic sway
    elb_y     = sh_y - upper_arm
    wrs_y     = elb_y - lower_arm

    elb_x_L   = sh_x_L - 0.05 + arm_swing
    wrs_x_L   = sh_x_L - 0.10 + arm_swing

    elb_x_R   = sh_x_R + 0.05 + arm_swing
    wrs_x_R   = sh_x_R + 0.10 + arm_swing

    # Assemble in a fixed order (15 joints)
    #
    # 0 Head
    # 1 Neck / upper spine
    # 2 L-shoulder, 3 R-shoulder
    # 4 L-elbow,    5 R-elbow
    # 6 L-wrist,    7 R-wrist
    # 8 Pelvis / root
    # 9 L-hip,     10 R-hip
    # 11 L-knee,   12 R-knee
    # 13 L-ankle,  14 R-ankle
    joints = np.array([
        [head_x,  head_y],
        [spine_top_x, spine_top_y],
        [sh_x_L, sh_y],
        [sh_x_R, sh_y],
        [elb_x_L, elb_y],
        [elb_x_R, elb_y],
        [wrs_x_L, wrs_y],
        [wrs_x_R, wrs_y],
        [hip_x,   hip_y],
        [hip_x_L, hip_y],
        [hip_x_R, hip_y],
        [knee_x_L, knee_y],
        [knee_x_R, knee_y],
        [ankle_x_L, ankle_y],
        [ankle_x_R, ankle_y]
    ])

    return joints


# --------------------------------------------------
#  Matplotlib initialisation
# --------------------------------------------------
plt.style.use('dark_background')      # black BG, white foreground text by default

fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# 15 dots
dots, = ax.plot([], [], 'o', color='white', markersize=6)

# Nice tight framing
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-0.2, 1.8)
ax.set_aspect('equal')
ax.axis('off')

TOTAL_FRAMES = 120     # 2 seconds @60 fps

# --------------------------------------------------
#  Animation callback
# --------------------------------------------------
def init():
    dots.set_data([], [])
    return dots,

def update(frame):
    pts = skeleton(frame, TOTAL_FRAMES)
    dots.set_data(pts[:,0], pts[:,1])
    return dots,

ani = FuncAnimation(fig,
                    update,
                    frames=TOTAL_FRAMES,
                    init_func=init,
                    interval=1000/60,   # ~60 fps
                    blit=True)

plt.show()
