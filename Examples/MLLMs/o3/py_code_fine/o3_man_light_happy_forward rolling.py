
"""
Point-light stimulus: 15 white dots depicting a light-weight
“happy-man” performing a smooth, biomechanically plausible
forward roll (somersault) on a solid black background.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------------------------  basic skeleton  ----------------------------
# Fifteen standard biomechanical markers (x, y)
# (units are arbitrary – roughly metres)
SKELETON = np.array([
    [0.00,  2.0],   # 0  head
    [0.00,  1.5],   # 1  neck / upper-spine
    [-0.50, 1.5],   # 2  left  shoulder
    [0.50,  1.5],   # 3  right shoulder
    [-1.00, 1.0],   # 4  left  elbow
    [1.00,  1.0],   # 5  right elbow
    [-1.20, 0.5],   # 6  left  wrist
    [1.20,  0.5],   # 7  right wrist
    [-0.40, 0.0],   # 8  left  hip
    [0.40,  0.0],   # 9  right hip
    [-0.40,-1.0],   # 10 left  knee
    [0.40, -1.0],   # 11 right knee
    [-0.40,-2.0],   # 12 left  ankle
    [0.40, -2.0],   # 13 right ankle
    [0.00,  0.5]    # 14 centre of torso / COM
])

# indices into skeleton array for clarity (unused further, but helpful)
HEAD, NECK = 0, 1
L_SHO, R_SHO, L_ELB, R_ELB, L_WRI, R_WRI = 2, 3, 4, 5, 6, 7
L_HIP, R_HIP, L_KNE, R_KNE, L_ANK, R_ANK, TORSO = 8, 9, 10, 11, 12, 13, 14

# -----------------------------  parameters  ------------------------------
N_FRAMES = 180                  # frames per full roll
RADIUS    = 1.8                 # rolling radius for ground translation
DPI       = 100                 # figure resolution
POINTSIZE = 50                  # scatter marker size

# -----------------------------  figure setup  ----------------------------
fig = plt.figure(figsize=(4,8), facecolor="black", dpi=DPI)
ax  = plt.axes(xlim=(-2, 6), ylim=(-4, 4))
ax.set_facecolor('black')
ax.set_xticks([]); ax.set_yticks([])
ax.set_aspect("equal", adjustable="box")

scatter = ax.scatter(SKELETON[:,0], SKELETON[:,1],
                     s=POINTSIZE, c="white", edgecolors="none")

# -----------------------  helpers for animation  -------------------------
def tuck(skeleton, phase):
    """
    Returns a copy of the skeleton with limbs tucked according to phase.
    phase ranges 0..1 during one full roll.
    """
    sk = skeleton.copy()

    # Degree of tuck: 0 (standing) -> 1 (fully tucked)
    # We use a raised cosine so the tuck smoothly increases and decreases.
    tuck_amt = 0.5*(1-np.cos(2*np.pi*phase))  # 0→1→0 across full revolution

    # bring knees to chest
    sk[[L_KNE, R_KNE],1] +=  1.0*tuck_amt      # knees up
    sk[[L_ANK, R_ANK],1] +=  2.0*tuck_amt      # ankles up

    # elbows bend inwards
    sk[[L_ELB, R_ELB],0] *= (1-0.5*tuck_amt)
    sk[[L_WRI, R_WRI],0] *= (1-0.8*tuck_amt)
    sk[[L_WRI, R_WRI],1] +=  1.0*tuck_amt

    return sk

def transform(skeleton, theta):
    """
    Apply rotation (theta) about torso centre, then translate so the
    torso follows rolling-without-slipping along +x.
    """
    # Rotation matrix
    rot = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta),  np.cos(theta)]])

    # shift to origin at torso, rotate, shift back
    torso = skeleton[TORSO]
    shifted = skeleton - torso
    rotated = shifted @ rot.T + torso

    # ground translation (rolling without slipping)
    dx = RADIUS * theta
    rotated[:,0] += dx
    return rotated

# ------------------------------ animation --------------------------------
def update(frame):
    phase = frame / N_FRAMES        # 0 .. 1
    angle = 2*np.pi*phase           # full rotation

    sk = tuck(SKELETON, phase)      # tuck limbs
    sk = transform(sk, -angle)      # negative angle: forward roll

    # update plotted data
    scatter.set_offsets(sk)
    return scatter,

anim = FuncAnimation(fig, update, frames=N_FRAMES, interval=40, blit=True)

plt.show()
