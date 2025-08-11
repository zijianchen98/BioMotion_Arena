
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# --------------------------------------------------------------------------------------
# Helper utilities
# --------------------------------------------------------------------------------------
def rotate(vec, angle_deg) -> np.ndarray:
    """Rotate a 2-D vector `vec` by `angle_deg` degrees (counter-clockwise)."""
    ang = np.deg2rad(angle_deg)
    rot_mtx = np.array([[np.cos(ang), -np.sin(ang)],
                        [np.sin(ang),  np.cos(ang)]])
    return rot_mtx @ vec


# --------------------------------------------------------------------------------------
# Model constants  (crudely approximated anthropometrics; units are arbitrary)
# --------------------------------------------------------------------------------------
SHOULDER_WIDTH = 0.40
HIP_WIDTH      = 0.30
TORSO_LEN      = 0.60
NECK_HEAD      = 0.25

UPPER_ARM      = 0.30
LOWER_ARM      = 0.25
UPPER_LEG      = 0.45
LOWER_LEG      = 0.45

MAX_TORSO_PITCH = -60.0   # forward bend (negative = leaning forward)
GROUND_Y        = -(UPPER_LEG + LOWER_LEG)    # y-coordinate of both ankles


# --------------------------------------------------------------------------------------
# Kinematic skeleton
# --------------------------------------------------------------------------------------
def skeleton_points(phase: float) -> np.ndarray:
    """
    Construct 15 joint positions (x, y) for a bowing animation.

    phase ∈ [0, 1]  – 0  : upright
                     0.5 : deepest bow
                     1  : upright again
    """
    # Smooth half-sine profile for the bowing motion
    torso_pitch = MAX_TORSO_PITCH * np.sin(np.pi * phase)     # 0→max→0
    torso_pitch = float(torso_pitch)

    # ----------------------------------------------------------------------------------
    # Torso / head
    # ----------------------------------------------------------------------------------
    pelvis = np.array([0.0, 0.0])                             # origin of model
    shoulder_ctr = pelvis + rotate(np.array([0.0, TORSO_LEN]), torso_pitch)
    head = shoulder_ctr + rotate(np.array([0.0, NECK_HEAD]), torso_pitch)

    # Shoulder extremities (width is kept horizontal – front view)
    left_shoulder  = shoulder_ctr + np.array([-SHOULDER_WIDTH / 2, 0.0])
    right_shoulder = shoulder_ctr + np.array([+SHOULDER_WIDTH / 2, 0.0])

    # ----------------------------------------------------------------------------------
    # Arms – hanging vertically under gravity
    # ----------------------------------------------------------------------------------
    left_elbow  = left_shoulder  + np.array([0.0, -UPPER_ARM])
    right_elbow = right_shoulder + np.array([0.0, -UPPER_ARM])

    left_wrist  = left_elbow  + np.array([0.0, -LOWER_ARM])
    right_wrist = right_elbow + np.array([0.0, -LOWER_ARM])

    # ----------------------------------------------------------------------------------
    # Hip / legs
    # ----------------------------------------------------------------------------------
    left_hip  = pelvis + np.array([-HIP_WIDTH / 2, 0.0])
    right_hip = pelvis + np.array([+HIP_WIDTH / 2, 0.0])

    # For simplicity legs remain (approximately) straight and vertical
    left_knee   = left_hip  + np.array([0.0, -UPPER_LEG])
    right_knee  = right_hip + np.array([0.0, -UPPER_LEG])

    left_ankle  = np.array([left_hip[0],  GROUND_Y])
    right_ankle = np.array([right_hip[0], GROUND_Y])

    # ----------------------------------------------------------------------------------
    # Assemble the 15 required point-lights
    # Index   Joint
    #   0     Head
    #   1     Shoulder-centre / neck
    #   2-3   Right / left shoulder
    #   4-5   Right / left elbow
    #   6-7   Right / left wrist
    #   8     Pelvis centre
    #   9-10  Right / left hip
    #   11-12 Right / left knee
    #   13-14 Right / left ankle
    # ----------------------------------------------------------------------------------
    pts = np.vstack([
        head,                 # 0
        shoulder_ctr,         # 1
        right_shoulder,       # 2
        left_shoulder,        # 3
        right_elbow,          # 4
        left_elbow,           # 5
        right_wrist,          # 6
        left_wrist,           # 7
        pelvis,               # 8
        right_hip,            # 9
        left_hip,             #10
        right_knee,           #11
        left_knee,            #12
        right_ankle,          #13
        left_ankle            #14
    ])
    return pts


# --------------------------------------------------------------------------------------
# Matplotlib animation
# --------------------------------------------------------------------------------------
def create_animation(save_as: str | None = None):
    num_frames = 64                       # ≈ 1.3 s at 50 ms per frame
    phases = np.linspace(0.0, 1.0, num_frames, endpoint=False)

    fig, ax = plt.subplots(figsize=(4, 6))
    ax.set_facecolor("black")
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-0.8, 0.8)
    ax.set_ylim(-1.4, 1.2)

    # Initialise white scatter for the 15 point-lights
    scat = ax.scatter([], [], s=40, c="white")

    def init():
        scat.set_offsets(np.zeros((15, 2)))
        return scat,

    def update(frame: int):
        pts = skeleton_points(phases[frame])
        scat.set_offsets(pts)
        return scat,

    anim = FuncAnimation(
        fig, update, frames=num_frames, init_func=init,
        interval=50, blit=True, repeat=True
    )

    if save_as:                          # Optional: export as GIF/MP4
        if save_as.lower().endswith(".gif"):
            from matplotlib.animation import PillowWriter
            anim.save(save_as, writer=PillowWriter(fps=20))
        else:                            # fall-back to ffmpeg (MP4, etc.)
            anim.save(save_as, writer="ffmpeg", dpi=150)
    else:
        plt.show()


# --------------------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------------------
if __name__ == "__main__":
    # To preview interactively, simply call without parameters.
    # If you want to save the animation, pass a filename, e.g.:
    # create_animation("bowing_stimulus.gif")
    create_animation()
