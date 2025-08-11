
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define 15 point-light positions for a stick-figure "lying down" model (side view, horizontal)
# The figure is lying on the ground (X horizontal, Y vertical)
# Order: head, neck, shoulders (L,R), elbows (L,R), wrists (L,R), torso, hips (L,R), knees (L,R), ankles (L,R)
# All units in arbitrary "body length" units

#              (viewed from the side, facing right)
#
#         z ^
#           |
#   y-----> |__o--o__o----o--o----o
#                |    |    |    |
#            (Ankles Knees Hips Shoulders ... Head at rightmost)

# The skeleton is:     (z,y)
SKELETON = {
    'head':         (0.85, 0.0),
    'neck':         (0.7, 0.0),
    'rshoulder':    (0.65, 0.06),
    'lshoulder':    (0.65, -0.06),
    'relbow':       (0.5, 0.09),
    'lelbow':       (0.5, -0.09),
    'rwrist':       (0.35, 0.12),
    'lwrist':       (0.35, -0.12),
    'torso':        (0.52, 0.0),
    'rhip':         (0.38, 0.05),
    'lhip':         (0.38, -0.05),
    'rknee':        (0.19, 0.08),
    'lknee':        (0.19, -0.08),
    'rankle':       (0.02, 0.11),
    'lankle':       (0.02, -0.11)
}
# The correspondence to 15 dots: order as below:
DOT_ORDER = [
    'head', 'neck', 'rshoulder', 'lshoulder',
    'relbow', 'lelbow', 'rwrist', 'lwrist',
    'torso', 'rhip', 'lhip', 'rknee', 'lknee',
    'rankle', 'lankle'
]

# We'll animate a slow breathing motion and some subtle limb/finger movements (lying down, arms slightly bend up)
# We'll also shift the whole body slightly as if the chest is moving up/down in breaths.

def get_pose(t):
    """
    Given time t (float, in seconds), return the 15 marker positions (as Nx2 array of XY).
    """
    #
    # Main movement: simulate breathing by raising/lowering chest and head a bit (move up in Y)
    # Lying on "ground", so body is horizontal.
    #
    # The axis in plot: x is rightward (along body lying axis), y is upward, head toward the right
    base = np.array([SKELETON[k] for k in DOT_ORDER])

    # Breathing (gentle oscillation)
    breath = 0.015 * np.sin(2 * np.pi * t / 2.6)  # breathing cycle: ~2.6 seconds

    # Head nod (slightly up/down, small)
    head_nod = 0.004 * np.sin(2 * np.pi * t / 1.4 + 1.1)

    # Left arm micro twitch (elbow/wrist movement)
    l_tw = 0.012 * np.sin(2 * np.pi * t / 4.7 + 1.3)

    # Right arm micro twitch
    r_tw = 0.008 * np.cos(2 * np.pi * t / 4.3 - 1.2)

    # Leg relaxation (tiny)
    leg_rel = 0.009 * np.sin(2 * np.pi * t / 5.0)

    # Build the movement
    points = base.copy()

    # Head bobs slightly upwards with breath
    points[0,1] += breath + head_nod    # head
    # Neck moves with breath, lesser amplitude
    points[1,1] += 0.5*breath + 0.6*head_nod
    # Shoulders rise a bit with breath (less than neck)
    points[2,1] += 0.3*breath
    points[3,1] += 0.3*breath
    # Torso (sternum marker) moves with breath too
    points[8,1] += 0.7*breath
    # Hips: very slightly (body) (just for realism)
    points[9,1] += 0.18*breath
    points[10,1] += 0.18*breath

    # Left elbow/wrist: small twitch UP/DOWN (simulate finger/hand lift)
    points[5,1] += l_tw * 0.4          # L elbow
    points[7,1] += l_tw                # L wrist

    # Right elbow/wrist: alternate small twitch
    points[4,1] += r_tw * 0.45         # R elbow
    points[6,1] += r_tw                # R wrist

    # Knees/ankles: subtle quadriceps movement, as breathing/legs relax
    points[11,1] += leg_rel * 0.4
    points[12,1] -= leg_rel * 0.36
    points[13,1] += leg_rel
    points[14,1] -= leg_rel

    # Optionally, slight, slow, near-invisible horizontal drift to show nonrigidity (lying person can fidget)
    position_shift = 0.003 * np.sin(2 * np.pi * t / 14.)
    points[:,0] += position_shift

    return points

# Setup matplotlib
fig, ax = plt.subplots(figsize=(4, 7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')
ax.set_aspect('equal')
ax.set_xlim(-0.1, 1.05)
ax.set_ylim(-0.2, 0.25)

# Prepare scatter plot
dots, = ax.plot([], [], 'o', color='white', markersize=11)

def init():
    dots.set_data([], [])
    return dots,

def animate(frame):
    t = frame / 30.0
    pt = get_pose(t)
    dots.set_data(pt[:,0], pt[:,1])
    return dots,

# Make animation
ani = FuncAnimation(fig, animate, frames=900, interval=33, blit=True, init_func=init)

plt.show()
