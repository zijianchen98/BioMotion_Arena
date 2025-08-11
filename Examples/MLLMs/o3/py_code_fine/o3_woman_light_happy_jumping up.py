
"""
Biological-motion point-light display
Action : light, happy woman jumping up
Author : ChatGPT
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------------------------------------------------
# Helper – linear interpolation between two skeletons
# ------------------------------------------------------------
def lerp(a, b, t):
    """Linear interpolation"""
    return a + (b - a) * t


# ------------------------------------------------------------
# Skeleton definition
# ≡ 15 anatomical landmarks
#  0  head
#  1  l-shoulder   2  r-shoulder
#  3  l-elbow      4  r-elbow
#  5  l-wrist      6  r-wrist
#  7  l-hip        8  r-hip
#  9  l-knee       10 r-knee
#  11 l-ankle      12 r-ankle
#  13 l-foot/toe   14 r-foot/toe
# Every entry is an (x, y) coordinate in an arbitrary unit system
# ------------------------------------------------------------

# Helper to mirror a left-side list to right-side values
def mirror(points):
    """Return a mirrored copy around the vertical axis (x *= -1)"""
    m = points.copy()
    m[:, 0] *= -1
    return m

# Keyframes for one complete jump cycle
# Phases: 0.00 = crouch, 0.25 = take-off, 0.50 = apex, 0.75 = landing, 1.00 = crouch
key_phases = np.array([0.00, 0.25, 0.50, 0.75, 1.00])

# LEFT side coordinates for the 7 unilateral joints (shoulder, elbow, wrist,
# hip, knee, ankle, toe) at each key phase
# Format: (phase, 7×2 matrix)
left_side = {
    0.00: np.array([
        [-0.15, 1.00],  # shoulder
        [-0.22, 0.70],  # elbow
        [-0.25, 0.40],  # wrist
        [-0.10, 0.50],  # hip
        [-0.10, 0.30],  # knee
        [-0.08, 0.05],  # ankle
        [-0.10, 0.00],  # toe
    ]),
    0.25: np.array([
        [-0.18, 1.15],
        [-0.25, 0.95],
        [-0.28, 0.85],
        [-0.10, 0.60],
        [-0.10, 0.45],
        [-0.08, 0.10],
        [-0.10, 0.00],
    ]),
    0.50: np.array([
        [-0.05, 1.45],
        [-0.02, 1.30],
        [-0.02, 1.20],
        [-0.10, 1.00],
        [-0.10, 0.90],
        [-0.09, 0.65],
        [-0.12, 0.60],
    ]),
    0.75: np.array([
        [-0.18, 1.15],
        [-0.25, 0.95],
        [-0.28, 0.85],
        [-0.10, 0.60],
        [-0.10, 0.45],
        [-0.08, 0.10],
        [-0.10, 0.00],
    ]),
    1.00: np.array([
        [-0.15, 1.00],
        [-0.22, 0.70],
        [-0.25, 0.40],
        [-0.10, 0.50],
        [-0.10, 0.30],
        [-0.08, 0.05],
        [-0.10, 0.00],
    ]),
}

# Central line joints (head and spine joints)
center_points = {
    0.00: np.array([
        [0.0, 1.20],  # head
        [0.0, 0.50],  # spine midpoint (hips averaged later)
    ]),
    0.25: np.array([
        [0.0, 1.35],
        [0.0, 0.60],
    ]),
    0.50: np.array([
        [0.0, 1.60],
        [0.0, 1.05],
    ]),
    0.75: np.array([
        [0.0, 1.35],
        [0.0, 0.60],
    ]),
    1.00: np.array([
        [0.0, 1.20],
        [0.0, 0.50],
    ]),
}

# Build the full 15-point skeleton for each stored keyframe
skeletons = {}
for phase in key_phases:
    # Head
    head = center_points[phase][0:1]
    # Shoulders/Elbows/Wrists + Hips/Knees/Ankles/Toes
    left = left_side[phase]
    right = mirror(left)
    # Hips (indices 3 within left/right arrays)
    hips = np.vstack([left[3], right[3]])
    # Build ordered list
    skel = np.zeros((15, 2))
    skel[0] = head                          # head
    skel[1:3] = left[0], right[0]           # shoulders
    skel[3:5] = left[1], right[1]           # elbows
    skel[5:7] = left[2], right[2]           # wrists
    skel[7:9] = left[3], right[3]           # hips
    skel[9:11] = left[4], right[4]          # knees
    skel[11:13] = left[5], right[5]         # ankles
    skel[13:15] = left[6], right[6]         # toes
    # Average hip for spine midpoint
    spine_mid = hips.mean(axis=0)
    # Replace dummy with actual spine point
    skel = np.insert(skel, 1, spine_mid, axis=0)  # insert spine after head
    # Now we have 16 points; drop the last toe to keep 15 (merge toes)
    skel = np.delete(skel, -1, axis=0)
    skeletons[phase] = skel


# ------------------------------------------------------------
# Animation setup
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_facecolor('black')
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(0, 1.8)
ax.set_aspect('equal')
ax.axis('off')

scatter = ax.scatter([], [], s=30, c='white')

cycle_frames = 120  # total frames per jump cycle


def interpolate_skeleton(t):
    """Return interpolated skeleton (15×2) for cycle phase t∈[0,1]"""
    # Find surrounding keyframes
    idx = np.searchsorted(key_phases, t)  # first keyframe ≥ t
    if idx == 0:
        return skeletons[key_phases[0]]
    if idx == len(key_phases):
        return skeletons[key_phases[-1]]

    t0 = key_phases[idx - 1]
    t1 = key_phases[idx]
    s0 = skeletons[t0]
    s1 = skeletons[t1]
    local = (t - t0) / (t1 - t0)
    return lerp(s0, s1, local)


def init():
    scatter.set_offsets(np.zeros((15, 2)))
    return scatter,


def update(frame):
    phase = (frame % cycle_frames) / cycle_frames  # 0-1
    skel = interpolate_skeleton(phase)
    # Add slight horizontal swaying (happy nuance)
    sway = 0.02 * np.sin(2 * np.pi * phase)
    skel[:, 0] += sway
    scatter.set_offsets(skel)
    return scatter,


ani = animation.FuncAnimation(fig, update, frames=cycle_frames,
                              init_func=init, interval=1000/60,
                              blit=True, repeat=True)

plt.show()
