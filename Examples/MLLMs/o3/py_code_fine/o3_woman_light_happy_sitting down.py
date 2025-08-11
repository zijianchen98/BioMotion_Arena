
"""
Point-light biological–motion stimulus
Action : Heavy happy woman – sitting down (cyclic stand ⇢ sit ⇢ stand)
15 white markers on a solid black background
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------------------------------------------------------------
# Helper – build one frame of joint coordinates (2-D) given a progress
# value p  (0 = fully standing, 1 = fully seated)
# ---------------------------------------------------------------------
def body_points(p: float):
    """
    Create the 15 marker positions for the current posture progress p.
    Front view – y axis is vertical, x axis horizontal (left negative).
    """

    # Some global anthropometric constants (arbitrary units)
    ankle_y       = 0.0
    body_height   = 6.5          # overall height while standing
    hip_drop_max  = 2.0          # how far the hips go down while sitting
    knee_forward  = 1.0          # knees translate forwards while sitting
    arm_forward   = 1.0          # wrists & elbows move forwards
    shoulder_span = 1.2          # width of shoulders
    hip_span      = 1.6          # width of hips (heavy build → wider)
    arm_span      = 1.6          # distance wrist from body midline (standing)
    
    # ------------ Vertical coordinates -------------
    hip_y   = (body_height*0.62) - hip_drop_max * p          # hips descend
    knee_y  = (ankle_y + hip_y) / 2.0                        # simple hinge
    head_y  = body_height
    neck_y  = body_height*0.9
    chest_y = body_height*0.8
    shoulder_y = neck_y
    elbow_y = neck_y - 1.5 + 0.5 * p                        # drop tiny bit
    wrist_y = neck_y - 2.5 + 0.5 * p                        # wrists drop
    
    # ------------ Horizontal coordinates ------------
    mid_x   = 0.0                                           # body midline
    # Hips
    lhip_x  = mid_x - hip_span/2
    rhip_x  = mid_x + hip_span/2
    # Knees
    lknee_x = lhip_x + knee_forward * p
    rknee_x = rhip_x + knee_forward * p
    # Ankles (feet stay put)
    lankle_x = lhip_x
    rankle_x = rhip_x
    # Shoulders
    lsho_x  = mid_x - shoulder_span/2
    rsho_x  = mid_x + shoulder_span/2
    # Arms
    lelbow_x = lsho_x - 0.4 - arm_forward * p
    relbow_x = rsho_x + 0.4 + arm_forward * p
    lwrist_x = lelbow_x - 0.3 - arm_forward * p
    rwrist_x = relbow_x + 0.3 + arm_forward * p
    
    # 15 markers (x, y) ------------------------------------------------
    pts = np.array([
        [mid_x,       head_y],        # 0 head
        [mid_x,       neck_y],        # 1 neck
        [lsho_x,      shoulder_y],    # 2 left shoulder
        [rsho_x,      shoulder_y],    # 3 right shoulder
        [lelbow_x,    elbow_y],       # 4 left elbow
        [relbow_x,    elbow_y],       # 5 right elbow
        [lwrist_x,    wrist_y],       # 6 left wrist
        [rwrist_x,    wrist_y],       # 7 right wrist
        [lhip_x,      hip_y],         # 8 left hip
        [rhip_x,      hip_y],         # 9 right hip
        [lknee_x,     knee_y],        # 10 left knee
        [rknee_x,     knee_y],        # 11 right knee
        [lankle_x,    ankle_y],       # 12 left ankle
        [rankle_x,    ankle_y],       # 13 right ankle
        [mid_x,       chest_y],       # 14 chest / spine marker
    ])
    return pts

# ---------------------------------------------------------------------
# Animation setup
# ---------------------------------------------------------------------
frames  = 120                             # total animation frames
fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor('black')          # black background
ax.set_facecolor('black')
scat = ax.scatter([], [], s=50, c='white')  # point-light markers

# Fix axis limits so figure doesn't rescale
ax.set_xlim(-4, 4)
ax.set_ylim(-0.5, 7)
ax.set_aspect('equal')
ax.axis('off')                            # remove axes / ticks

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    # cosine easing to create smooth cyclic stand ⇢ sit ⇢ stand
    p = 0.5 - 0.5 * np.cos(2*np.pi * frame/frames)   # 0→1→0 over cycle
    pts = body_points(p)
    scat.set_offsets(pts)
    return scat,

ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=40)

plt.show()
