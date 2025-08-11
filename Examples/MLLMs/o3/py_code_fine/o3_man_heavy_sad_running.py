
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------
def compute_joint_positions(t):
    """
    Produce a 2-D (x, y) location for 15 biological-motion point-lights
    that represent a running human figure.

    Parameters
    ----------
    t : float
        Time (in seconds).

    Returns
    -------
    np.ndarray, shape (15, 2)
        Coordinates for the 15 point-lights.
    """
    # Basic temporal parameters
    step_freq = 2.0               # two steps per second
    phase     = 2 * np.pi * step_freq * t

    # Global (body) motion and bounce
    forward_speed = 0.7           # world-space speed (units / s)
    bounce        = 0.06 * np.sin(phase * 0.5)  # gentle vertical bounce
    pelvis        = np.array([forward_speed * t, 0.0 + bounce])

    # Vertical landmarks (in body-centred coordinates)
    y_head     = 1.60
    y_neck     = 1.40
    y_chest    = 1.20
    y_shoulder = 1.30
    y_pelvis   = 0.00
    y_hip      = -0.05
    y_knee     = -0.45
    y_ankle    = -0.95
    y_elbow    = 1.05
    y_wrist    = 0.75

    # Stride / swing amplitudes
    leg_stride_x   = 0.35
    leg_stride_y   = 0.12
    arm_stride_x   = 0.25
    arm_stride_y   = 0.04
    shoulder_width = 0.22
    hip_width      = 0.16

    # Right–/left–limb phases (legs in anti-phase, arms opposite to legs).
    phase_r_leg = phase
    phase_l_leg = phase + np.pi
    phase_r_arm = phase + np.pi
    phase_l_arm = phase

    # -----------------------------
    # Legs
    # -----------------------------
    # Hip joints
    r_hip = pelvis + np.array([+hip_width / 2, y_hip])
    l_hip = pelvis + np.array([-hip_width / 2, y_hip])

    # Knees
    r_knee = r_hip + np.array([
        leg_stride_x * np.sin(phase_r_leg),
        (y_knee - y_hip) + leg_stride_y * np.cos(phase_r_leg)
    ])
    l_knee = l_hip + np.array([
        leg_stride_x * np.sin(phase_l_leg),
        (y_knee - y_hip) + leg_stride_y * np.cos(phase_l_leg)
    ])

    # Ankles
    r_ankle = r_knee + np.array([
        leg_stride_x * 0.6 * np.sin(phase_r_leg),
        (y_ankle - y_knee) + leg_stride_y * 0.5 * np.cos(phase_r_leg)
    ])
    l_ankle = l_knee + np.array([
        leg_stride_x * 0.6 * np.sin(phase_l_leg),
        (y_ankle - y_knee) + leg_stride_y * 0.5 * np.cos(phase_l_leg)
    ])

    # -----------------------------
    # Arms
    # -----------------------------
    # Shoulder joints
    r_shoulder = pelvis + np.array([+shoulder_width / 2, y_shoulder])
    l_shoulder = pelvis + np.array([-shoulder_width / 2, y_shoulder])

    # Elbows
    r_elbow = r_shoulder + np.array([
        +arm_stride_x * np.sin(phase_r_arm),
        (y_elbow - y_shoulder) + arm_stride_y * np.cos(phase_r_arm)
    ])
    l_elbow = l_shoulder + np.array([
        +arm_stride_x * np.sin(phase_l_arm),
        (y_elbow - y_shoulder) + arm_stride_y * np.cos(phase_l_arm)
    ])

    # Wrists
    r_wrist = r_elbow + np.array([
        +arm_stride_x * 0.7 * np.sin(phase_r_arm),
        (y_wrist - y_elbow) + arm_stride_y * 0.5 * np.cos(phase_r_arm)
    ])
    l_wrist = l_elbow + np.array([
        +arm_stride_x * 0.7 * np.sin(phase_l_arm),
        (y_wrist - y_elbow) + arm_stride_y * 0.5 * np.cos(phase_l_arm)
    ])

    # -----------------------------
    # Axial skeleton (head / neck / chest / pelvis-centre)
    # -----------------------------
    head  = pelvis + np.array([0.0, y_head])
    neck  = pelvis + np.array([0.0, y_neck])
    chest = pelvis + np.array([0.0, y_chest])

    # -----------------------------
    # Aggregate the 15 markers
    # -----------------------------
    # Index mapping (15 points):
    # 0 head, 1 neck, 2 chest,
    # 3 r_shoulder, 4 r_elbow, 5 r_wrist,
    # 6 l_shoulder, 7 l_elbow, 8 l_wrist,
    # 9 pelvis-centre,
    # 10 r_hip, 11 r_knee, 12 r_ankle,
    # 13 l_hip, 14 l_knee, 15 l_ankle (but we only need up to 14)
    pts = np.vstack([
        head, neck, chest,
        r_shoulder, r_elbow, r_wrist,
        l_shoulder, l_elbow, l_wrist,
        pelvis,
        r_hip, r_knee, r_ankle,
        l_hip, l_knee, l_ankle
    ])

    # We constructed 16 points, drop the last to keep exactly 15
    return pts[:15]


# -----------------------------------------------------------------------------
# Matplotlib animation
# -----------------------------------------------------------------------------
def animate_point_light_run():
    plt.style.use('dark_background')          # black background, white dots
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(-1, 3)
    ax.set_ylim(-1.2, 1.9)
    ax.set_aspect('equal')
    ax.axis('off')

    # Initial scatter
    scatter = ax.scatter([], [], s=36, c='white')

    # Animation update function
    def update(frame_idx):
        t = frame_idx / 60.0                 # 60 FPS time-base
        pts = compute_joint_positions(t)
        scatter.set_offsets(pts)
        return scatter,

    frames = 360                             # 6 seconds at 60 fps
    ani = FuncAnimation(
        fig, update, frames=frames, interval=1000/60, blit=True, repeat=True
    )

    plt.show()


# -----------------------------------------------------------------------------
# Main guard
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    animate_point_light_run()
