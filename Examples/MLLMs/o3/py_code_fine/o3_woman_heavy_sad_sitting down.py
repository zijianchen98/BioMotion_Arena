
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------------------------------
#  Basic configuration
# -------------------------------------------------
POINT_SIZE = 80          # size of the point‐lights
FPS         = 30         # animation frame-rate
FRAMES_PER_HALF_CYCLE = 60   # frames from standing → sitting (and back)

# -------------------------------------------------
#  Helper: smooth easing (cosine ease in / out)
# -------------------------------------------------
def ease(v: float) -> float:
    """Cosine easing:   v in [0 … 1]  →  ease(v) in [0 … 1]."""
    return 0.5 - 0.5 * np.cos(np.pi * v)


# -------------------------------------------------
#  Define joint layout  (15 joints)
# -------------------------------------------------
#
#  Index   Joint
#  -----   ------------------------
#    0     Head
#    1     Neck
#    2     Shoulder – left
#    3     Shoulder – right
#    4     Elbow    – left
#    5     Elbow    – right
#    6     Wrist    – left
#    7     Wrist    – right
#    8     Hip      – left
#    9     Hip      – right
#   10     Knee     – left
#   11     Knee     – right
#   12     Ankle    – left
#   13     Ankle    – right
#   14     Pelvis centre
#
#  All coordinates are given in an arbitrary, front-view 2-D space
#  and subsequently interpolated to create motion.

# Standing posture (t = 0)
stand_x = np.array([ 0.0,  0.0, -0.5,  0.5, -0.8,  0.8, -0.9,  0.9,
                    -0.4,  0.4, -0.4,  0.4, -0.4,  0.4,  0.0])
stand_y = np.array([ 5.0,  4.5,  4.0,  4.0,  3.0,  3.0,  2.0,  2.0,
                     2.0,  2.0,  1.0,  1.0,  0.0,  0.0,  2.0])

# Sitting posture (t = 1)
sit_x   = np.array([ 0.0,  0.0, -0.5,  0.5, -0.7,  0.7, -0.6,  0.6,
                    -0.5,  0.5, -0.5,  0.5, -0.4,  0.4,  0.0])
sit_y   = np.array([ 4.2,  3.8,  3.4,  3.4,  2.4,  2.4,  1.4,  1.4,
                     1.0,  1.0,  1.0,  1.0,  0.0,  0.0,  1.0])


# -------------------------------------------------
#  Matplotlib setup
# -------------------------------------------------
plt.rcParams['toolbar'] = 'None'          # hide toolbar (optional)

fig = plt.figure(figsize=(4, 6))
fig.patch.set_facecolor('black')          # black background

ax = fig.add_subplot(111)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 6.0)
ax.axis('off')                            # no axes, ticks, etc.

# create scatter plot for the 15 point-lights
scatter = ax.scatter([], [], s=POINT_SIZE, c='white')

# -------------------------------------------------
#  Animation updating
# -------------------------------------------------
def update(frame: int):
    """Compute joint positions for current frame and
       update the scatter plot."""
    # triangular wave 0→1→0 describing the phase of the action
    cycle  = frame % (2 * FRAMES_PER_HALF_CYCLE)
    if cycle < FRAMES_PER_HALF_CYCLE:
        phase = cycle / FRAMES_PER_HALF_CYCLE          # 0 … 1  (down)
    else:
        phase = 1 - (cycle - FRAMES_PER_HALF_CYCLE) / FRAMES_PER_HALF_CYCLE   # 1 … 0 (up)

    t = ease(phase)                                    # smooth easing
    
    # interpolate between standing and sitting
    x = stand_x + t * (sit_x - stand_x)
    y = stand_y + t * (sit_y - stand_y)

    # update scatter object
    scatter.set_offsets(np.c_[x, y])

    return scatter,


# -------------------------------------------------
#  Run the animation
# -------------------------------------------------
anim = FuncAnimation(fig,
                     update,
                     interval=1000 / FPS,
                     blit=True)

plt.show()
