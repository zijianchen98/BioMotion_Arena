
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


# ------------------------------------------------------------------
# 1.  Static canonical (rest) pose – 15 points (x, y)
# ------------------------------------------------------------------
#   0  head
#   1  neck
#   2  L-shoulder     3  R-shoulder
#   4  L-elbow        5  R-elbow
#   6  L-wrist        7  R-wrist
#   8  pelvis (root)
#   9  L-hip         10  R-hip
#  11  L-knee        12  R-knee
#  13  L-ankle       14  R-ankle
rest = np.array([
    [0.0, 6.6],      # head
    [0.0, 5.8],      # neck
    [-1.0, 5.5],     # L-shoulder
    [ 1.0, 5.5],     # R-shoulder
    [-1.5, 4.3],     # L-elbow
    [ 1.5, 4.3],     # R-elbow
    [-1.3, 3.0],     # L-wrist
    [ 1.3, 3.0],     # R-wrist
    [0.0, 3.0],      # pelvis
    [-0.8, 3.0],     # L-hip
    [ 0.8, 3.0],     # R-hip
    [-0.8, 1.5],     # L-knee
    [ 0.8, 1.5],     # R-knee
    [-0.8, 0.0],     # L-ankle
    [ 0.8, 0.0],     # R-ankle
])


# ------------------------------------------------------------------
# 2.  Helper: produce a single pose for a given phase (0…1)
# ------------------------------------------------------------------
def pose(phase: float) -> np.ndarray:
    """Return 15×2 array of joint positions for a given jump phase (0-1)."""
    pos = rest.copy()

    pelvis_y0 = 3.0  # rest pelvis height

    # ---- Pelvis trajectory -------------------------------------------------
    if phase < 0.20:                            # preparatory crouch
        f = phase / 0.20                        # 0 → 1
        pelvis_y = pelvis_y0 - 1.5 * f
    elif phase < 0.30:                          # explosive push-off
        f = (phase - 0.20) / 0.10               # 0 → 1
        pelvis_y = (pelvis_y0 - 1.5) + 2.5 * f
    elif phase < 0.70:                          # flight (parabolic)
        p = (phase - 0.30) / 0.40               # 0 → 1
        pelvis_y = pelvis_y0 + 1.0 + 2.0 * np.sin(np.pi * p)
    elif phase < 0.80:                          # landing absorption
        f = (phase - 0.70) / 0.10               # 0 → 1
        pelvis_y = (pelvis_y0 + 1.0) - 2.0 * f
    else:                                       # return to stance
        f = (phase - 0.80) / 0.20               # 0 → 1
        pelvis_y = (pelvis_y0 - 1.0) + 1.0 * f

    # ---- Crouch extent (0 = straight, 1 = deep squat) ----------------------
    crouch = max(0.0, pelvis_y0 - pelvis_y) / 1.5          # 0…1
    leg_scale = 1.0 - 0.30 * crouch                        # shorter legs when crouching

    # ---- Set pelvis & hips --------------------------------------------------
    dy = pelvis_y - pelvis_y0
    pos[8, 1]  = pelvis_y             # pelvis
    pos[9, 1]  = pelvis_y             # L-hip
    pos[10, 1] = pelvis_y             # R-hip

    # ---- Knees & ankles (scaled leg length) ---------------------------------
    knee_y   = pelvis_y - 1.5 * leg_scale
    ankle_y  = pelvis_y - 3.0 * leg_scale

    # keep feet on ground while not in flight
    in_flight = phase >= 0.27
    if not in_flight and ankle_y < 0:
        diff = -ankle_y
        ankle_y = 0
        knee_y -= diff

    pos[11, 1] = knee_y      # L-knee
    pos[12, 1] = knee_y      # R-knee
    pos[13, 1] = ankle_y     # L-ankle
    pos[14, 1] = ankle_y     # R-ankle

    # ---- Upper body: translate with pelvis shift ---------------------------
    pos[0:8, 1] += dy

    # ---- Arms swing upward during flight ------------------------------------
    if phase < 0.25:
        arm_up = 0.0
    elif phase < 0.45:
        arm_up = (phase - 0.25) / 0.20
    elif phase < 0.70:
        arm_up = 1.0
    elif phase < 0.90:
        arm_up = 1.0 - (phase - 0.70) / 0.20
    else:
        arm_up = 0.0

    arm_lift = 2.0 * arm_up            # additional y-shift for elbows & wrists
    pos[4, 1] += arm_lift              # L-elbow
    pos[5, 1] += arm_lift              # R-elbow
    pos[6, 1] += arm_lift              # L-wrist
    pos[7, 1] += arm_lift              # R-wrist

    return pos


# ------------------------------------------------------------------
# 3.  Build animation --------------------------------------------------------
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(3, 6), dpi=120)
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_xlim(-3.0, 3.0)
ax.set_ylim(-0.5, 8.0)
ax.set_aspect("equal")
ax.axis("off")

scat = ax.scatter([], [], s=60, c="white")

def init():
    scat.set_offsets(np.zeros((15, 2)))
    return scat,

def update(frame):
    phase = frame / (N_FRAMES - 1)
    pts = pose(phase)
    scat.set_offsets(pts)
    return scat,

N_FRAMES = 100
anim = FuncAnimation(fig, update, frames=N_FRAMES, init_func=init, blit=True)

# ------------------------------------------------------------------
# 4.  Save out as GIF --------------------------------------------------------
# ------------------------------------------------------------------
anim.save("point_light_jump.gif", writer=PillowWriter(fps=30))
print("Animation saved to 'point_light_jump.gif'")
