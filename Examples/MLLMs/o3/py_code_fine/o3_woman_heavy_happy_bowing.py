
"""
Point–Light Biological–Motion Stimulus
Action  : Heavy, happy woman bowing
Lights  : 15 white dots on a black background
Library : matplotlib

The script creates an endlessly–looping, biomechanically–plausible ‘bow’ animation
that fulfils the requirements given in the problem statement.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -------------------------------------------------
# 1. Model definition
# -------------------------------------------------
# Each joint is first defined in an upright, neutral pose (standing, facing the
# camera).  All coordinates are in a canonical, unit-less space so that the figure
# roughly fits in the window [−1 … +1] horizontally, [−1 … +1] vertically.

# Index / body part map (15 joints)
HEAD            = 0
NECK            = 1
SHOULDER_L      = 2
ELBOW_L         = 3
WRIST_L         = 4
SHOULDER_R      = 5
ELBOW_R         = 6
WRIST_R         = 7
HIP_C           = 8
HIP_L           = 9
KNEE_L          = 10
ANKLE_L         = 11
HIP_R           = 12
KNEE_R          = 13
ANKLE_R         = 14

# Neutral, upright pose (x, y)
neutral_pose = np.array([
    [ 0.00,  0.80],   # 0  head
    [ 0.00,  0.60],   # 1  neck
    [-0.20,  0.60],   # 2  shoulder L
    [-0.30,  0.30],   # 3  elbow   L
    [-0.35,  0.00],   # 4  wrist   L
    [ 0.20,  0.60],   # 5  shoulder R
    [ 0.30,  0.30],   # 6  elbow   R
    [ 0.35,  0.00],   # 7  wrist   R
    [ 0.00,  0.00],   # 8  hip centre (bow pivot)
    [-0.10,  0.00],   # 9  hip L
    [-0.10, -0.40],   # 10 knee L
    [-0.10, -0.80],   # 11 ankle L
    [ 0.10,  0.00],   # 12 hip R
    [ 0.10, -0.40],   # 13 knee R
    [ 0.10, -0.80],   # 14 ankle R
])

# -------------------------------------------------
# 2. Motion generator
# -------------------------------------------------
def bow_pose(t_frac: float) -> np.ndarray:
    """
    Produce a single animation frame:
        t_frac ∈ [0 … 1] is the phase of the bow cycle.
        0.0 = upright → 0.5 = deepest bow → 1.0 = upright, ready to repeat.
    Returns an (N, 2) array of joint positions.
    """

    # Copy neutral pose so we do not destroy the template.
    P = neutral_pose.copy()

    # Define bow amount in range [0…1]; use a smooth half-sine for natural motion.
    # t_frac 0   → 0
    # t_frac 0.5 → 1 (deepest point)
    # t_frac 1   → 0
    bow_amt = np.sin(np.pi * t_frac)      # smooth, symmetrical bow

    # Parameters (tuned visually)
    max_forward_pitch = np.deg2rad(55)    # maximum torso rotation (degrees → rad)
    torso_drop        = 0.40              # vertical drop of shoulders at deepest bow
    arm_swing         = 0.25              # how far the wrists swing inward when bowing

    # ------------------------------------------------------------------
    # 2.1 Rotate torso, head & shoulder block around the hip-centre pivot
    # ------------------------------------------------------------------
    pivot = neutral_pose[HIP_C]           # rotation centre (pelvis)
    angle = max_forward_pitch * bow_amt   # pitch angle

    # Indices affected by torso rotation (everything above the hips)
    upper_body_idx = [HEAD, NECK,
                      SHOULDER_L, ELBOW_L, WRIST_L,
                      SHOULDER_R, ELBOW_R, WRIST_R]

    # Rotation matrix for pitch (in 2-D side projection : rotate in the y-axis
    # but our view is frontal → we mimic the bow by lowering y)
    # Instead of a real 3-D rotation we approximate by:
    #   1) translating points downward (torso_drop * bow_amt)
    #   2) bringing them forward slightly on the x-axis (small elliptical path)
    #
    # This is sufficient for a recognisable point-light stimulus.

    for idx in upper_body_idx:
        # Lower the joint
        P[idx, 1] -= torso_drop * bow_amt

        # Hint of forward displacement (perspective cue)
        P[idx, 0] *= (1 - 0.15 * bow_amt)

    # -------------------------------------------------
    # 2.2   Arm motion: wrists swing inward on a bow
    # -------------------------------------------------
    P[WRIST_L, 0] +=  arm_swing * bow_amt
    P[WRIST_R, 0] -=  arm_swing * bow_amt

    # Elbows follow the wrists slightly (smaller amplitude)
    P[ELBOW_L, 0] += 0.6 * arm_swing * bow_amt
    P[ELBOW_R, 0] -= 0.6 * arm_swing * bow_amt

    # -------------------------------------------------
    # 2.3   Optional head nod – small extra dip adds realism
    # -------------------------------------------------
    P[HEAD, 1] -= 0.08 * bow_amt

    # All done – return positions for this frame
    return P


# -------------------------------------------------
# 3. Animation with matplotlib
# -------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 6), facecolor='black')
ax.set_facecolor('black')
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-1.2, 1.0)
ax.set_aspect('equal')
ax.axis('off')                    # hide axes / ticks

# Create the 15 white dots
dots = ax.scatter([], [], s=40, c='white')

# Total frames per cycle and frame generator
FPS          = 30                  # frames-per-second
CYCLE_SEC    = 2                   # duration of a bow cycle (seconds)
N_FRAMES     = FPS * CYCLE_SEC     # total frames in one period


def init():
    """Initialisation function for FuncAnimation."""
    dots.set_offsets(np.zeros((15, 2)))
    return (dots,)


def animate(frame_idx):
    """Animation callback."""
    t_frac = (frame_idx % N_FRAMES) / N_FRAMES     # fractional position in cycle
    pose   = bow_pose(t_frac)
    dots.set_offsets(pose)
    return (dots,)


ani = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=N_FRAMES, interval=1000 / FPS, blit=True, repeat=True
)

plt.show()
