
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------------------------  CONFIGURATION  ---------------------------- #
n_points = 15
fps       = 30           # frames / second
n_seconds = 4            # total duration of the clip
n_frames  = fps * n_seconds

# Biomechanical lengths (in arbitrary units)
LEN_ANKLE_KNEE   = 0.45
LEN_KNEE_HIP     = 0.45
LEN_HIP_SHOULDER = 0.60
LEN_SHOULDER_NECK = 0.10
LEN_NECK_HEAD    = 0.20
LEN_SHOULDER_ELBOW = 0.30
LEN_ELBOW_WRIST    = 0.30

# Horizontal spacings
HIP_SPACING       = 0.20   # distance between left & right hip
SHOULDER_SPACING  = 0.30   # distance between left & right shoulder

# Animation parameters for the bow action (in degrees)
LEAN_PEAK_DEG   = -60      # maximum forward lean (negative = leaning forward)
LEAN_START      = int(0.0 * n_frames)
LEAN_DOWN_END   = int(0.3 * n_frames)
LEAN_HOLD_END   = int(0.7 * n_frames)
LEAN_END        = n_frames

# Root (hip-centre) coordinates
ROOT_X = 0.0
ROOT_Y = LEN_ANKLE_KNEE + LEN_KNEE_HIP        # such that ankles lie on y = 0

# ----------------------  Helper: rotation utility  ----------------------- #
def rot(vec, deg):
    """Rotate a 2-D vector by <deg> degrees."""
    rad = np.deg2rad(deg)
    c, s = np.cos(rad), np.sin(rad)
    x, y = vec
    return np.array([c * x - s * y, s * x + c * y])

# -----------------------  Produce skeleton frames  ----------------------- #
frames = []

for f in range(n_frames):
    # ---------- Determine torso lean angle for this frame ----------
    if f <= LEAN_DOWN_END:
        # ease-in bow
        alpha = (f - LEAN_START) / (LEAN_DOWN_END - LEAN_START)
        lean_deg = (1 - np.cos(alpha * np.pi)) / 2 * LEAN_PEAK_DEG  # cosine-ease
    elif f <= LEAN_HOLD_END:
        lean_deg = LEAN_PEAK_DEG
    else:
        # ease-out bow (come back upright)
        alpha = (f - LEAN_HOLD_END) / (LEAN_END - LEAN_HOLD_END)
        lean_deg = LEAN_PEAK_DEG * (1 - (1 - np.cos(alpha * np.pi)) / 2)

    # ---------- Central (midline) joints ----------
    hip_center = np.array([ROOT_X, ROOT_Y])
    shoulder_center = hip_center + rot([0, LEN_HIP_SHOULDER], lean_deg)
    neck   = shoulder_center + rot([0, LEN_SHOULDER_NECK], lean_deg)
    head   = neck + rot([0, LEN_NECK_HEAD], lean_deg)

    # compute torso-perpendicular unit for shoulder width
    torso_vec = shoulder_center - hip_center
    perp = np.array([ torso_vec[1], -torso_vec[0] ])   # rotate 90°
    perp = perp / np.linalg.norm(perp)

    # ---------- Left / right shoulders & hips ----------
    l_shoulder = shoulder_center - perp * (SHOULDER_SPACING / 2)
    r_shoulder = shoulder_center + perp * (SHOULDER_SPACING / 2)
    l_hip      = hip_center      - perp * (HIP_SPACING / 2)
    r_hip      = hip_center      + perp * (HIP_SPACING / 2)

    # ---------- Arms (hanging straight down, sadness posture) ----------
    down = np.array([0, -1])
    l_elbow = l_shoulder + down * LEN_SHOULDER_ELBOW
    r_elbow = r_shoulder + down * LEN_SHOULDER_ELBOW
    l_wrist = l_elbow     + down * LEN_ELBOW_WRIST
    r_wrist = r_elbow     + down * LEN_ELBOW_WRIST

    # ---------- Legs (static stance) ----------
    l_knee  = l_hip + down * LEN_KNEE_HIP
    r_knee  = r_hip + down * LEN_KNEE_HIP
    l_ankle = l_knee + down * LEN_ANKLE_KNEE
    r_ankle = r_knee + down * LEN_ANKLE_KNEE

    # ---------- Collect the 15 points ----------
    pts = np.vstack([
        head,
        neck,
        l_shoulder, r_shoulder,
        l_elbow, r_elbow,
        l_wrist, r_wrist,
        hip_center,
        l_hip, r_hip,
        l_knee, r_knee,
        l_ankle, r_ankle
    ])
    frames.append(pts)

frames = np.stack(frames)     # shape : (n_frames, 15, 2)

# -----------------------------  VISUALISATION  --------------------------- #
fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-0.2, 2.0)
ax.axis('off')

# scatter plot with 15 white markers
scatter = ax.scatter([], [], s=50, lw=0, c='white')

def init():
    scatter.set_offsets(np.zeros((n_points, 2)))
    return scatter,

def animate(i):
    scatter.set_offsets(frames[i])
    return scatter,

ani = FuncAnimation(fig, animate, frames=n_frames, init_func=init,
                    interval=1000 / fps, blit=True, repeat=True)

plt.show()
