
"""
Biological-motion style point-light display
15 white dots on a black background showing a light-weight, happy woman
waving her right hand.

The code uses matplotlib to create a smooth, biomechanically plausible
animation.  The main parts are:

    • A very simple 2-D kinematic “skeleton” with 15 joints.
    • A tiny procedural animation that keeps the body mostly static while
      moving the right arm in a waving gesture (shoulder + elbow motion).
    • A matplotlib FuncAnimation that renders the dots.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# ----------------------------------------------------------------------
# Skeleton layout (all coordinates are in a simple, arbitrary unit system)
#
#  index   joint
#  -----   -----------------
#    0     head
#    1     neck
#    2     right shoulder
#    3     right elbow
#    4     right wrist        <-- waving!
#    5     left shoulder
#    6     left elbow
#    7     left wrist
#    8     upper-spine (mid-torso)
#    9     pelvis (root)
#   10     right hip
#   11     right knee
#   12     right ankle
#   13     left hip
#   14     left knee          (left ankle omitted to keep 15 points total)
#
# NOTE:  The absolute numbers are not meant to be anatomically perfect;
#        they are only meant to give a recognisable “stick-figure”
#        proportion so that the waving motion looks believable.
# ----------------------------------------------------------------------


def base_pose() -> np.ndarray:
    """
    Returns the default (rest) positions of all 15 joints
    as an (15, 2) array of [x, y] rows.
    """
    # Torso and head (central vertical line).
    head       = np.array([0.0,  1.60])
    neck       = np.array([0.0,  1.45])
    spine      = np.array([0.0,  1.05])
    pelvis     = np.array([0.0,  0.80])

    # Shoulders (slightly wider than hips).
    shoulder_y = 1.40
    r_shoulder = np.array([+0.18, shoulder_y])
    l_shoulder = np.array([-0.18, shoulder_y])

    # Elbows (straight down, arms relaxed).
    r_elbow = r_shoulder + np.array([ 0.00, -0.30])
    l_elbow = l_shoulder + np.array([ 0.00, -0.30])

    # Wrists (hands hanging loosely).
    r_wrist = r_elbow + np.array([ 0.00, -0.25])
    l_wrist = l_elbow + np.array([ 0.00, -0.25])

    # Hips and legs.
    hip_y = 0.75
    r_hip = np.array([+0.10, hip_y])
    l_hip = np.array([-0.10, hip_y])

    r_knee = r_hip + np.array([ 0.00, -0.45])
    l_knee = l_hip + np.array([ 0.00, -0.45])

    r_ankle = r_knee + np.array([ 0.00, -0.40])
    # We do not include the left ankle – that keeps us at 15 markers.

    # Assemble into a single matrix in the correct order.
    joints = np.vstack(
        [
            head, neck,
            r_shoulder, r_elbow, r_wrist,
            l_shoulder, l_elbow, l_wrist,
            spine, pelvis,
            r_hip, r_knee, r_ankle,
            l_hip, l_knee,
        ]
    )
    return joints


# Pre-compute things that do not change:
REST_POSE = base_pose()

# Segment lengths for the waving arm.
UPPER_ARM_LEN = np.linalg.norm(REST_POSE[3] - REST_POSE[2])   # shoulder → elbow
FOREARM_LEN   = np.linalg.norm(REST_POSE[4] - REST_POSE[3])   # elbow → wrist


def right_arm_positions(t: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Compute (elbow, wrist) positions at time t [0-1] for the right arm.

    A very small kinematic chain:
        shoulder is fixed (from REST_POSE)
        elbow = shoulder + R(θ1) * upper_arm_length
        wrist = elbow    + R(θ1 + θ2) * forearm_length

    θ1 oscillates slowly to lift/lower the arm,
    θ2 oscillates faster to create the waving motion.
    """
    shoulder = REST_POSE[2]

    # Shoulder angle:  (π/4) raises the arm 45°,
    # modulated ±15° with a slow period (one cycle per second).
    theta1 = np.radians(45) + np.radians(15) * np.sin(2 * np.pi * t)

    # Elbow angle (relative): mostly straight (~160°) but flexes ±10°
    # out of phase to give a pleasant waving curve.
    theta2 = np.radians(160) + np.radians(10) * np.sin(6 * np.pi * t + np.pi / 3)

    # Compute rotation vectors.
    v1 = UPPER_ARM_LEN * np.array([np.cos(theta1), np.sin(theta1)])
    elbow = shoulder + v1

    v2 = FOREARM_LEN * np.array([np.cos(theta1 - theta2), np.sin(theta1 - theta2)])
    wrist = elbow + v2

    return elbow, wrist


def generate_frame(t: float) -> np.ndarray:
    """
    Return 15×2 array with the joint positions for moment t (in seconds).

    The body is almost static except for a tiny vertical ‘bounce’ and
    a slow left-right sway, so that the woman looks happy and lively.
    """
    joints = REST_POSE.copy()

    # Small, subtle whole-body animation: vertical bounce & lateral sway
    bounce = 0.02 * np.sin(2 * np.pi * t)            # ±2 cm vertical
    sway   = 0.03 * np.sin(2 * np.pi * t * 0.5)      # ±3 cm horizontal, slower
    joints[:, 0] += sway
    joints[:, 1] += bounce

    # Right arm (indices 3 = elbow, 4 = wrist).
    elbow, wrist = right_arm_positions(t)
    joints[3] = elbow
    joints[4] = wrist

    return joints


# ----------------------------------------------------------------------
# Matplotlib animation
# ----------------------------------------------------------------------

def create_animation():
    # Basic mpl setup: black background, white points.
    fig, ax = plt.subplots(figsize=(4, 6))
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    ax.set_xlim(-0.7, 0.7)
    ax.set_ylim(-0.4, 1.9)
    ax.set_aspect("equal")
    ax.axis("off")

    # Scatter plot with 15 points.
    scat = ax.scatter(
        REST_POSE[:, 0],
        REST_POSE[:, 1],
        c="white",
        s=30,
        edgecolors="none",
    )

    # Frames per second and total duration.
    FPS = 30
    DURATION = 4          # seconds
    frame_count = FPS * DURATION

    def update(frame_number: int):
        t = frame_number / FPS  # time in seconds
        pts = generate_frame(t % 1.0)   # loop the motion every 1 second
        scat.set_offsets(pts)
        return scat,

    ani = FuncAnimation(
        fig,
        update,
        frames=frame_count,
        interval=1000 / FPS,
        blit=True,
    )

    return ani


def main():
    """
    Run the animation.  Close the window to end the program.
    """
    ani = create_animation()

    # Uncomment the next line if you want an animated GIF written to disk.
    # ani.save("point_light_waving.gif", dpi=100, fps=30)

    plt.show()


if __name__ == "__main__":
    main()
