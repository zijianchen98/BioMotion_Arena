
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
#  Skeleton description (15 pts)
# -----------------------------
# 0  - head
# 1  - neck
# 2  - left shoulder
# 3  - right shoulder
# 4  - left elbow
# 5  - right elbow
# 6  - left wrist
# 7  - right wrist
# 8  - hip-centre   (root)
# 9  - left hip
# 10 - right hip
# 11 - left knee
# 12 - right knee
# 13 - left ankle
# 14 - right ankle

# Relative coordinates for an upright standing pose (origin at hip–centre)
RELATIVE_POSE = np.array([
    [0.0,  0.60],   # head
    [0.0,  0.40],   # neck
    [-0.20, 0.35],  # L-shoulder
    [0.20,  0.35],  # R-shoulder
    [-0.35, 0.10],  # L-elbow
    [0.35,  0.10],  # R-elbow
    [-0.40,-0.15],  # L-wrist
    [0.40, -0.15],  # R-wrist
    [0.0,   0.00],  # hip-centre (root)
    [-0.15, 0.00],  # L-hip
    [0.15,  0.00],  # R-hip
    [-0.15,-0.50],  # L-knee
    [0.15, -0.50],  # R-knee
    [-0.15,-1.00],  # L-ankle
    [0.15, -1.00],  # R-ankle
])

# ------------------------------------------------------
# Helper to create one animation‐frame of joint positions
# ------------------------------------------------------
def skeleton(frame, n_frames):
    """
    Return (15,2) array with absolute xy coordinates
    for the required frame.
    """

    # ---------- phase parameters ----------
    crouch_end   = 14                # 0 … 14 (15 frames)
    launch_end   = crouch_end + 10   # 15 … 24  (10 frames)
    flight_end   = launch_end + 50   # 25 … 74  (50 frames)
    landing_end  = flight_end + 20   # 75 … 94  (20 frames)
    settle_end   = n_frames - 1      # 95 … 119 (25 frames)

    # ---------------------------------------
    # Root (hip-centre) vertical displacement
    # ---------------------------------------
    base_y   = 1.00               # standing hip height above ground
    root_y   = base_y
    crouch_y = 0.40               # depth of crouch
    jump_h   = 1.00               # maximum COM elevation during flight

    # Determine vertical motion
    if frame <= crouch_end:                               # crouching
        c = frame / crouch_end
        root_y -= c * crouch_y
        crouch_factor = c
    elif frame <= launch_end:                             # launching / extension
        c = (launch_end - frame) / (launch_end - crouch_end)
        root_y -= c * crouch_y     # smoothly back to 0
        crouch_factor = c
    elif frame <= flight_end:                             # airborne (parabola)
        t = (frame - launch_end) / (flight_end - launch_end)
        # parabolic vertical path 0→1→0
        root_y += jump_h * (4 * t * (1 - t))
        crouch_factor = 0.0
    elif frame <= landing_end:                            # first ground contact, landing crouch
        d = (frame - flight_end) / (landing_end - flight_end)
        root_y -= 0.20 * (1 - np.cos(np.pi * d)) / 2      # a gentle cushioning
        crouch_factor = (1 - np.cos(np.pi * d)) / 2       # 0 → 1 → 0
    else:                                                 # settling back to stand
        root_y = base_y
        crouch_factor = 0.0

    # -------------------------------
    # Root horizontal displacement
    # -------------------------------
    total_dist = 3.0
    root_x = (frame / (n_frames - 1)) * total_dist

    # ---------------------------------------------------
    # Adjust relative pose for crouch (simple, compressed)
    # ---------------------------------------------------
    rel = RELATIVE_POSE.copy()

    # compress everything above the hips for crouch
    if crouch_factor > 0:
        compression = 1 - 0.35 * crouch_factor   # up to 35 % shorter
        # indices above hips (0-7)
        rel[:8, 1] *= compression
        # knees & ankles move slightly forward during crouch
        spread = 0.10 * crouch_factor            # small knee forward motion
        rel[11:, 0] += np.array([-1, 1, -1, 1]) * spread

    # ---------------------------------
    # Assemble absolute joint positions
    # ---------------------------------
    abs_pos = rel + np.array([root_x, root_y])

    return abs_pos

# -----------------
#  Build animation
# -----------------
def main():
    n_frames = 120
    fig, ax = plt.subplots(figsize=(5, 5))
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    ax.set_aspect("equal")
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-0.2, 3.0)
    ax.axis("off")

    scat = ax.scatter([], [], s=60, c="white")

    def init():
        scat.set_offsets(np.zeros((15, 2)))
        return scat,

    def update(frame):
        points = skeleton(frame, n_frames)
        scat.set_offsets(points)
        return scat,

    ani = FuncAnimation(fig, update, frames=n_frames,
                        init_func=init, interval=40, blit=True, repeat=True)
    plt.show()


if __name__ == "__main__":
    main()
