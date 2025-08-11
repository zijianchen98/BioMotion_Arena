
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# ----------------------  BIOMECHANICAL MODEL  ------------------------------- #
# The model is deliberately simple, yet produces a biomechanically‐plausible
# movement that *looks* like a lightweight human running.
#
# All angles are expressed in radians. 0 rad corresponds to a perfectly
# vertical (downward-pointing) segment. Positive values swing the segment
# forwards (to the right), negative values backwards (to the left).

SEG = dict(
    head          = 0.20,   # shoulders → head
    torso         = 0.40,   # hips      → shoulders
    thigh         = 0.45,   # hip       → knee
    shank         = 0.45,   # knee      → ankle
    upper_arm     = 0.30,   # shoulder  → elbow
    forearm       = 0.25,   # elbow     → wrist
    hip_width     = 0.20,   # distance between left/right hips
    shoulder_width= 0.30,   # distance between left/right shoulders
)

def leg_positions(hip, phase):
    """
    Returns knee, ankle positions for one leg given
    the hip joint position (x, y) and the phase (rad).
    """
    # Thigh angle (relative to downward vertical)
    thigh_amp = 0.8                # ~45°
    thigh_a   = thigh_amp * np.sin(phase)

    # Knee flexion – more flex during swing phase (when thigh forward)
    knee_base = 0.3                # baseline knee angle (~17°)
    knee_add  = 0.4 * (np.sin(phase) + 1) / 2.0   # 0 → 0.4
    knee_a    = thigh_a + knee_base + knee_add    # absolute angle of shank

    # Thigh endpoint (knee)
    knee = hip + SEG['thigh'] * np.array([np.sin(thigh_a),
                                          -np.cos(thigh_a)])

    # Shank endpoint (ankle)
    ankle = knee + SEG['shank'] * np.array([np.sin(knee_a),
                                            -np.cos(knee_a)])
    return knee, ankle


def arm_positions(shoulder, phase):
    """
    Returns elbow, wrist positions for one arm given
    the shoulder joint position (x, y) and the phase (rad).
    Arm motion is anti-phase with the contralateral leg.
    """
    # Upper-arm angle (mirror of contralateral thigh motion)
    upper_amp = 0.9
    upper_a   = upper_amp * np.sin(phase)

    # Elbow flex
    elbow_base = 0.4
    elbow_add  = 0.3 * (np.sin(phase + np.pi/2) + 1) / 2.0
    elbow_a    = upper_a + elbow_base + elbow_add

    # Elbow position
    elbow = shoulder + SEG['upper_arm'] * np.array([np.sin(upper_a),
                                                    -np.cos(upper_a)])

    # Wrist position
    wrist = elbow + SEG['forearm'] * np.array([np.sin(elbow_a),
                                               -np.cos(elbow_a)])
    return elbow, wrist


def skeleton_at(t, speed=1.0):
    """
    Returns 15×2 array with point positions for the running ‘happyman’
    at time t (seconds). The centre of mass moves left→right at `speed`.
    """

    # Global progression (runner moves across the screen)
    x0 = speed * t
    y0 = 1.0

    # Phase of gait cycle (two full steps per second → frequency = 2 Hz)
    freq  = 2.5                    # step frequency (Hz) – somewhat ‘running’
    phase = 2 * np.pi * freq * t   # right leg phase; left is +π

    # Hip & shoulder centres
    hip_c       = np.array([x0, y0])
    shoulder_c  = hip_c + np.array([0.0, SEG['torso']])

    # Left / Right hips
    hip_L = hip_c + np.array([-SEG['hip_width'] / 2, 0])
    hip_R = hip_c + np.array([ SEG['hip_width'] / 2, 0])

    # Left / Right shoulders
    sh_L = shoulder_c + np.array([-SEG['shoulder_width'] / 2, 0])
    sh_R = shoulder_c + np.array([ SEG['shoulder_width'] / 2, 0])

    # Legs
    knee_R, ankle_R = leg_positions(hip_R,  phase         )
    knee_L, ankle_L = leg_positions(hip_L,  phase + np.pi )

    # Arms (anti-phase with *contralateral* leg)
    elbow_R, wrist_R = arm_positions(sh_R, phase + np.pi)   # right arm ↔ left leg
    elbow_L, wrist_L = arm_positions(sh_L, phase         )

    # Head
    head = shoulder_c + np.array([0.0, SEG['head']])

    # Chest & pelvis markers (centres)
    chest  = shoulder_c
    pelvis = hip_c

    # Collect in the requested order (15 points)
    points = np.vstack([
        head,               #  0
        sh_L, sh_R,         #  1, 2
        elbow_L, elbow_R,   #  3, 4
        wrist_L, wrist_R,   #  5, 6
        hip_L, hip_R,       #  7, 8
        knee_L, knee_R,     #  9,10
        ankle_L, ankle_R,   # 11,12
        chest, pelvis       # 13,14
    ])
    return points


# ----------------------  VISUALISATION  ------------------------------------- #
def make_animation():
    duration = 6            # seconds
    fps      = 60
    frames   = int(duration * fps)

    fig, ax = plt.subplots(figsize=(5, 7))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_xlim(0, 6)
    ax.set_ylim(-0.2, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Scatter for the 15 white points
    scatter = ax.scatter([], [], s=50, c='white')

    def init():
        scatter.set_offsets(np.zeros((15, 2)))
        return scatter,

    def update(frame):
        t = frame / fps
        P = skeleton_at(t)
        scatter.set_offsets(P)
        return scatter,

    ani = FuncAnimation(fig, update, frames=frames, init_func=init,
                        blit=True, interval=1000/fps, repeat=True)
    return ani


if __name__ == '__main__':
    ani = make_animation()
    plt.show()
