
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------------------------- #
#  Basic kinematic description  #
# ----------------------------- #

N_POINTS = 15

# Index map for readability
HEAD, NECK, R_SHOULDER, L_SHOULDER, R_ELBOW, L_ELBOW, R_WRIST, L_WRIST, \
PELVIS, R_HIP, L_HIP, R_KNEE, L_KNEE, R_ANKLE, L_ANKLE = range(N_POINTS)

# Static (standing) pose in a convenient coordinate system (front view)
BASE_Y = np.array([
    1.8,  # head
    1.5,  # neck
    1.4, 1.4,        # shoulders
    1.0, 1.0,        # elbows
    0.6, 0.6,        # wrists
    0.0,             # pelvis (root)
    0.0, 0.0,        # hips
   -0.5, -0.5,       # knees
   -1.0, -1.0        # ankles  (ground)
])

BASE_X = np.array([
    0.0,          # head
    0.0,          # neck
    0.30, -0.30,       # shoulders (R,L)
    0.35, -0.35,       # elbows   (R,L)
    0.35, -0.35,       # wrists   (R,L)
    0.0,               # pelvis
    0.20, -0.20,       # hips     (R,L)
    0.20, -0.20,       # knees    (R,L)
    0.20, -0.20        # ankles   (R,L)
])

# Ground level (visual reference)
GROUND_Y = -1.0

# ----------------------------- #
#   Temporal parameterization   #
# ----------------------------- #

def root_offset(t):
    """
    Vertical displacement of pelvis during the cycle.
    t is in [0,1].  One cycle = crouch -> jump -> land -> stand.
    """
    if t < 0.2:                # crouching down
        return -0.2 * (t / 0.2)
    elif t < 0.3:              # explosive push up back to neutral
        return -0.2 + 0.2 * ((t - 0.2) / 0.1)
    elif t < 0.7:              # airborne (parabolic flight)
        u = (t - 0.3) / 0.4    # 0 … 1
        return 0.8 * np.sin(np.pi * u)  # peak at u = 0.5
    elif t < 0.8:              # landing – squatting
        return 0.8 * np.sin(np.pi) - 0.2 * ((t - 0.7) / 0.1)
    else:                      # rising from squat back to neutral
        return -0.2 + 0.2 * ((t - 0.8) / 0.2)


def crouch_factor(t):
    """
    0 = upright, 1 = full crouch.
    """
    if t < 0.2:
        return t / 0.2
    elif t < 0.3:
        return 1 - (t - 0.2) / 0.1
    elif t < 0.7:
        return 0.0
    elif t < 0.8:
        return (t - 0.7) / 0.1
    else:
        return 1 - (t - 0.8) / 0.2


def arm_raise(t):
    """
    0 = arms down, 1 = arms up (during flight).
    """
    if 0.3 <= t <= 0.7:
        p = (t - 0.3) / 0.4  # 0 … 1
        return np.sin(np.pi * p)  # raise then lower smoothly
    return 0.0

# ----------------------------- #
#        Pose generation        #
# ----------------------------- #

def make_pose(t):
    """
    Generate 2D positions (x,y) for all 15 markers at time fraction t in [0,1].
    """
    y = BASE_Y.copy()
    x = BASE_X.copy()

    # Pelvis vertical movement
    dy_root = root_offset(t)
    y += dy_root

    # Crouch (affects knees)
    c = crouch_factor(t)
    # Bring knees up (reduce knee extension) and hips slightly forward for realism
    y[[R_KNEE, L_KNEE]] += 0.3 * c
    x[[R_KNEE, L_KNEE]] *= (1 - 0.3 * c)  # knees move towards midline when crouched

    # Arms animation
    a = arm_raise(t)
    y[[R_WRIST, L_WRIST]] = BASE_Y[[R_WRIST, L_WRIST]] + 0.8 * a + dy_root
    y[[R_ELBOW, L_ELBOW]] = BASE_Y[[R_ELBOW, L_ELBOW]] + 0.5 * a + dy_root
    x[[R_WRIST, R_ELBOW]] = BASE_X[[R_WRIST, R_ELBOW]] + 0.1 * a
    x[[L_WRIST, L_ELBOW]] = BASE_X[[L_WRIST, L_ELBOW]] - 0.1 * a

    # Ensure ankles stay at ground contact when not airborne
    if t < 0.3 or t > 0.7:
        y[[R_ANKLE, L_ANKLE]] = GROUND_Y
    else:
        # airborne: ankles follow pelvis rigidly at constant relative offset
        y[[R_ANKLE, L_ANKLE]] = BASE_Y[[R_ANKLE, L_ANKLE]] + dy_root
    return x, y

# ----------------------------- #
#        Matplotlib setup       #
# ----------------------------- #

fig = plt.figure(figsize=(4, 6), facecolor='black')
ax = fig.add_subplot(111)
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 2.5)
ax.set_aspect('equal')
ax.axis('off')

scatter = ax.scatter([], [], s=36, c='white')

# ----------------------------- #
#          Animation            #
# ----------------------------- #

FPS = 60
DURATION = 2.0  # seconds for a full jump cycle
N_FRAMES = int(FPS * DURATION)

def init():
    scatter.set_offsets(np.zeros((N_POINTS, 2)))
    return scatter,

def update(frame):
    t = (frame % N_FRAMES) / N_FRAMES  # normalized 0-1
    x, y = make_pose(t)
    pts = np.vstack([x, y]).T
    scatter.set_offsets(pts)
    return scatter,

ani = FuncAnimation(fig, update, frames=N_FRAMES, init_func=init,
                    interval=1000/FPS, blit=True)

# ----------------------------- #
#            Display            #
# ----------------------------- #

if __name__ == '__main__':
    plt.show()
