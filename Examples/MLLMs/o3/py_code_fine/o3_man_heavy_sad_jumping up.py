
"""
Biological–motion point-light stimulus
Sad heavy man jumping up             

Exactly 15 white dots on a black background are animated with
matplotlib.  The kinematics are very simple but biomechanically
plausible enough to be recognised as a person who slowly squats,
explodes upward, floats shortly and finally lands again while
holding a heavy weight close to the belly.                                  
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------------------------------------------------
# Helper – simple planar (x, y) leg-solver (hip-knee-ankle)
# ------------------------------------------------------------
def solve_knee(hip, ankle, l1, l2, forward=True):
    """
    Return the knee position that connects hip→knee→ankle
    with segment lengths l1 (hip-knee) and l2 (knee-ankle).

    If no exact solution exists (too far/too close) the
    distance is clamped so the leg is either fully stretched
    or maximally flexed.
    """
    hx, hy = hip
    ax, ay = ankle
    dx, dy = ax - hx, ay - hy
    d = np.hypot(dx, dy)

    # Clamp distance into feasible range
    d = np.clip(d, 1e-6, l1 + l2 - 1e-6)

    # Law of cosines
    cos_ang_knee = (l1**2 + d**2 - l2**2) / (2 * l1 * d)
    cos_ang_knee = np.clip(cos_ang_knee, -1.0, 1.0)

    # Projection of knee on hip-ankle line
    proj = l1 * cos_ang_knee
    # Height of the triangle
    h = np.sqrt(max(l1**2 - proj**2, 0.0))

    # Unit vector hip→ankle
    ux, uy = dx / d, dy / d
    # Perpendicular (chooses knee in front/back)
    if forward:
        px, py = -uy, ux
    else:
        px, py = uy, -ux

    kx = hx + ux * proj + px * h
    ky = hy + uy * proj + py * h
    return np.array([kx, ky])


# ------------------------------------------------------------
# Global geometry (all in metres – arbitrary units)
# ------------------------------------------------------------
upper_leg = 0.55
lower_leg = 0.55
upper_arm = 0.35
lower_arm = 0.35

shoulder_width = 0.30
hip_width = 0.30
head_height = 0.60          # hip→head
shoulder_drop = 0.20        # hip→shoulders

# Foot positions on ground while standing
ankle_x = 0.25

# Animation timing
n_frames = 200
fps = 50

base_hip_y = 1.0            # standing hip height
squat_depth = 0.30          # how deep he squats
jump_boost = 0.80           # extra hip rise in flight

# Ease functions ------------------------------------------------
def ease_in_out_sine(t):
    return 0.5 * (1 - np.cos(np.pi * t))

def ease_out_quadratic(t):
    return 1 - (1 - t) ** 2

# Hip trajectory over time --------------------------------------
def hip_y_at(t):
    """
    0 … 1 --> hip height
    0-0.3 : slow squat
    0.3-0.4 : explosive extension (take-off)
    0.4-0.6 : airborne
    0.6-0.7 : landing compression
    0.7-1.0 : return to resting
    """
    if t < 0.3:                                 # down
        f = t / 0.3
        return base_hip_y - squat_depth * ease_in_out_sine(f)

    elif t < 0.4:                               # push up
        f = (t - 0.3) / 0.1
        return (base_hip_y - squat_depth +
                (squat_depth + jump_boost) * ease_out_quadratic(f))

    elif t < 0.6:                               # in air (parabola)
        f = (t - 0.4) / 0.2                     # 0→1
        return (base_hip_y + jump_boost -
                4 * jump_boost * (f - 0.5) ** 2)   # simple parabola

    elif t < 0.7:                               # land compress
        f = (t - 0.6) / 0.1
        return base_hip_y + (0.2 * squat_depth) * (1 - f)

    else:                                       # settle
        f = (t - 0.7) / 0.3
        return base_hip_y + (0.2 * squat_depth) * (1 - ease_in_out_sine(f))

# ------------------------------------------------------------
# Build frame-wise 15 point coordinates ----------------------
# Index meaning:
# 0 Head
# 1 L shoulder, 2 R shoulder
# 3 L elbow,    4 R elbow
# 5 L wrist,    6 R wrist
# 7 L hip,      8 R hip
# 9 L knee,    10 R knee
#11 L ankle,   12 R ankle
#13 Pelvis centre
#14 Weight (dumbbell) centre
# ------------------------------------------------------------
def make_frame(t_norm):
    """
    Create a 15×2 array of (x, y) joint positions for time t ∈ [0, 1].
    """
    hip_y = hip_y_at(t_norm)

    # Pelvis and hips (left/right)
    pelvis = np.array([0.0, hip_y])
    left_hip = pelvis + np.array([-hip_width / 2, 0.0])
    right_hip = pelvis + np.array([hip_width / 2, 0.0])

    # Shoulders
    shoulders_y = hip_y + head_height - 0.1       # torso lean (heavy, sad)
    left_shoulder = np.array([-shoulder_width / 2, shoulders_y])
    right_shoulder = np.array([shoulder_width / 2, shoulders_y])

    # Elbows (arms hang and hold weight)
    elbow_offset = np.array([0.0, -upper_arm * 0.9])
    left_elbow = left_shoulder + elbow_offset
    right_elbow = right_shoulder + elbow_offset

    # Wrists (towards midline)
    wrist_offset = np.array([(shoulder_width / 2) * 0.3, -lower_arm])
    left_wrist = left_elbow + np.array([ wrist_offset[0], wrist_offset[1]])
    right_wrist = right_elbow + np.array([-wrist_offset[0], wrist_offset[1]])

    # Weight point between wrists
    weight = (left_wrist + right_wrist) / 2 + np.array([0.0, -0.05])

    # Ankles – on ground unless airborne
    airborne = hip_y > base_hip_y + 0.05
    if airborne:
        airborne_ankle_y = hip_y - (upper_leg + lower_leg) + 0.05
        left_ankle = np.array([-ankle_x, airborne_ankle_y])
        right_ankle = np.array([ankle_x, airborne_ankle_y])
    else:
        left_ankle = np.array([-ankle_x, 0.0])
        right_ankle = np.array([ankle_x, 0.0])

    # Knees via 2-segment kinematics
    left_knee = solve_knee(left_hip, left_ankle, upper_leg, lower_leg,
                           forward=True)
    right_knee = solve_knee(right_hip, right_ankle, upper_leg, lower_leg,
                            forward=True)

    # Head (slightly hanging – sad)
    head = pelvis + np.array([0.0, head_height + 0.07 * np.sin(6*np.pi*t_norm)])

    # Assemble
    pts = np.vstack([head,
                     left_shoulder, right_shoulder,
                     left_elbow, right_elbow,
                     left_wrist, right_wrist,
                     left_hip, right_hip,
                     left_knee, right_knee,
                     left_ankle, right_ankle,
                     pelvis,
                     weight])
    return pts


# ------------------------------------------------------------
# Matplotlib animation
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 6), facecolor='black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(0.0, 2.2)
ax.axis('off')

# Initial scatter
points = make_frame(0.0)
scat = ax.scatter(points[:, 0], points[:, 1],
                  s=30, c='white', edgecolors='none')

# Animation update function
def update(frame):
    t_norm = frame / (n_frames - 1)
    pts = make_frame(t_norm)
    scat.set_offsets(pts)
    return scat,

anim = FuncAnimation(fig, update, frames=n_frames,
                     interval=1000 / fps, blit=True)

plt.show()
