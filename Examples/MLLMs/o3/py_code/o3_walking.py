
"""
Point-Light Biological Motion Stimulus
15 white dots on a black background depicting a man walking
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# --------------------------------------------------------------------- #
#  Helper functions                                                     #
# --------------------------------------------------------------------- #
def rot(vec, angle):
    """
    Rotate a 2-D vector `vec` (x, y) by `angle` (rad) counter-clock-wise.
    """
    c, s = np.cos(angle), np.sin(angle)
    x, y = vec
    return np.array([c * x - s * y, s * x + c * y])


def walker_pose(phase, x_shift=0.0):
    """
    Compute the 2-D position of the 15 body landmarks for a single gait phase.

    Parameters
    ----------
    phase : float
        Gait phase ∈ [0, 2π).
    x_shift : float
        Global horizontal translation (so the walker drifts to the right).

    Returns
    -------
    np.ndarray
        (15, 2) array with x/y positions for the 15 landmarks.
        Ordering:
        0  head
        1  L shoulder,  2 R shoulder
        3  L elbow,     4 R elbow
        5  L wrist,     6 R wrist
        7  L hip,       8 R hip
        9  L knee,     10 R knee
        11 L ankle,    12 R ankle
        13 L toe,      14 R toe
    """

    # ------------------------  basic anthropometrics ------------------ #
    # (all values in “body-length” units, ≈ metres for an average adult)
    thigh = 0.45     # hip → knee
    shank = 0.45     # knee → ankle
    foot_len = 0.10  # ankle → toe
    upper_arm = 0.34  # shoulder → elbow
    fore_arm = 0.34   # elbow → wrist

    # vertical reference positions
    hip_y_base = 1.1              # mean hip height from ground
    shoulder_y_off = 0.45         # shoulder above hip
    head_y_off = 0.25             # head above shoulder

    # gait parameters (empirically reasonable values)
    hip_amp = np.deg2rad(30)      # forward/back swing of thigh
    knee_amp = np.deg2rad(30)     # knee flexion
    knee_base = np.deg2rad(15)    # baseline knee bend when standing
    arm_amp = np.deg2rad(30)      # arm swing at shoulder
    elbow_base = np.deg2rad(40)   # permanent bend in elbow

    # pelvis bobbing (vertical oscillation ≈ 2 cycles per step)
    bob_amp = 0.05
    hip_y = hip_y_base + bob_amp * np.sin(2 * phase)

    # small pitch of torso forward/back (affects shoulder & head x)
    torso_pitch = 0.05 * np.sin(2 * phase)

    # store joint positions here
    pts = np.zeros((15, 2))

    # global hip (mid-point between L/R hip)
    hip_x = x_shift
    hip_mid = np.array([hip_x, hip_y])

    # individual hip centres (slightly separated in depth – not visible in 2-D,
    # so we just offset them by a minuscule 2-D delta to avoid overlap)
    hip_sep = 0.02
    hip_L = hip_mid + np.array([-hip_sep, 0])
    hip_R = hip_mid + np.array([+hip_sep, 0])
    pts[7] = hip_L
    pts[8] = hip_R

    # Shoulder centre (directly above hip centre)
    shoulder_mid = hip_mid + np.array([0, shoulder_y_off])
    shoulder_L = shoulder_mid + np.array([-hip_sep, 0])
    shoulder_R = shoulder_mid + np.array([+hip_sep, 0])
    pts[1] = shoulder_L
    pts[2] = shoulder_R

    # Head
    pts[0] = shoulder_mid + np.array([torso_pitch, head_y_off])

    # --------------------------  legs  -------------------------------- #
    # left/right phase offset (π out-of-phase)
    for side, hip_point, phase_off, knee_idx, ankle_idx, toe_idx in (
        ("L", hip_L, 0.0, 9, 11, 13),
        ("R", hip_R, np.pi, 10, 12, 14),
    ):
        phi = phase + phase_off

        # Thigh absolute angle (0 = straight down)
        theta_thigh = hip_amp * np.sin(phi)
        # Knee flexion (0 = fully straight), maxima roughly at swing mid-point
        theta_knee = knee_base + knee_amp * np.maximum(
            0, np.sin(phi + np.pi / 2)
        )

        # Knee position
        knee_vec = rot([0, -thigh], theta_thigh)
        knee = hip_point + knee_vec

        # Ankle position
        shank_vec = rot([0, -shank], theta_thigh + theta_knee)
        ankle = knee + shank_vec

        # Toe position (keep foot mostly horizontal w.r.t ground)
        toe = ankle + np.array([foot_len * np.cos(theta_thigh + theta_knee),
                                -foot_len * np.sin(theta_thigh + theta_knee)])

        pts[knee_idx] = knee
        pts[ankle_idx] = ankle
        pts[toe_idx] = toe

    # --------------------------  arms  -------------------------------- #
    # arms swing roughly anti-phase with opposite leg (i.e. same sign as
    # contralateral thigh)
    for side, shoulder_point, phase_off, elbow_idx, wrist_idx in (
        ("L", shoulder_L, np.pi, 3, 5),
        ("R", shoulder_R, 0.0, 4, 6),
    ):
        phi = phase + phase_off

        # Upper-arm angle (0 = straight down)
        theta_upper = arm_amp * np.sin(phi)
        # keep elbow bent a little: forearm rotated relative to upper arm
        theta_elbow = elbow_base

        elbow_vec = rot([0, -upper_arm], theta_upper)
        elbow = shoulder_point + elbow_vec

        fore_vec = rot([0, -fore_arm], theta_upper + theta_elbow)
        wrist = elbow + fore_vec

        pts[elbow_idx] = elbow
        pts[wrist_idx] = wrist

    return pts


# --------------------------------------------------------------------- #
#  Animation                                                            #
# --------------------------------------------------------------------- #
def main():
    # Rendering parameters
    FPS = 60
    N_CYCLES = 3            # number of gait cycles to display
    CYCLE_FRAMES = 60       # frames per gait cycle
    FRAMES = N_CYCLES * CYCLE_FRAMES

    # Figure / axis setup
    fig, ax = plt.subplots(figsize=(4, 6))
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    ax.set_aspect("equal")
    ax.axis("off")

    # Limits chosen so the walker stays centred vertically
    ax.set_xlim(-0.2, 4.0)
    ax.set_ylim(-0.1, 2.3)

    # create the 15 white points
    scatter = ax.scatter([], [], s=60, c="white")

    def init():
        scatter.set_offsets(np.zeros((15, 2)))
        return scatter,

    def update(frame):
        # phase advances from 0 → 2π
        phase = 2 * np.pi * (frame % CYCLE_FRAMES) / CYCLE_FRAMES
        # walker slowly drifts to the right across cycles
        x_shift = 0.03 * frame
        pts = walker_pose(phase, x_shift)
        scatter.set_offsets(pts)
        return scatter,

    ani = animation.FuncAnimation(
        fig, update, frames=FRAMES, init_func=init,
        interval=1000 / FPS, blit=True
    )

    plt.show()


if __name__ == "__main__":
    main()
