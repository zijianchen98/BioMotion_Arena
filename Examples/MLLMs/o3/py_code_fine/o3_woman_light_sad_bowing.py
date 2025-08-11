
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------------------------------------------------------
#  Point-light biological motion stimulus: “sad, light-weight woman bowing”
#  ‑ 15 white point-lights on a solid black background
# -----------------------------------------------------------------------------

# Reference upright (standing) 2-D coordinates for 15 joints
# The scale is arbitrary – chosen simply to look good on screen
JOINT_NAMES = [
    "head", "neck",
    "l_shoulder", "r_shoulder",
    "l_elbow", "r_elbow",
    "l_wrist", "r_wrist",
    "spine",
    "l_hip", "r_hip",
    "l_knee", "r_knee",
    "l_ankle", "r_ankle"
]

upright = np.array([
    [ 0.00,  5.0],   # head
    [ 0.00,  4.5],   # neck
    [-0.50,  4.3],   # left shoulder
    [ 0.50,  4.3],   # right shoulder
    [-0.70,  3.3],   # left elbow
    [ 0.70,  3.3],   # right elbow
    [-0.70,  2.3],   # left wrist
    [ 0.70,  2.3],   # right wrist
    [ 0.00,  3.5],   # spine / mid-torso
    [-0.30,  2.5],   # left hip
    [ 0.30,  2.5],   # right hip
    [-0.30,  1.2],   # left knee
    [ 0.30,  1.2],   # right knee
    [-0.30,  0.0],   # left ankle
    [ 0.30,  0.0],   # right ankle
])

# Index helpers
HIP_L  = JOINT_NAMES.index("l_hip")
HIP_R  = JOINT_NAMES.index("r_hip")
HIP_C  = None  # hip centre will be computed frame-by-frame
TORSO_INDICES = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])  # joints above the hips

# Animation parameters
FPS        = 30
DURATION   = 6.0            # seconds
N_FRAMES   = int(FPS * DURATION)
AMPLITUDE  = np.deg2rad(40)  # maximal bend (in radians)
SAD_SLOW   = 0.7             # slowdown factor to make it feel “sad”

# Pre-create figure / axis
plt.rcParams["savefig.facecolor"] = "black"
fig, ax = plt.subplots(figsize=(4, 6), facecolor="black")
ax.set_facecolor("black")
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 6)
ax.set_aspect("equal")
ax.axis("off")

# Scatter for the 15 point-lights (white dots)
scatter = ax.scatter(upright[:, 0], upright[:, 1],
                     s=50, c="white", edgecolors="none")

def rotate(points, angle, origin):
    """
    Rotate a set of 2-D points around 'origin' by 'angle' radians.
    points : (N, 2) array
    """
    # Translate so that origin -> (0,0)
    translated = points - origin
    # Rotation matrix
    c, s = np.cos(angle), np.sin(angle)
    R = np.array([[c, -s],
                  [s,  c]])
    rotated = translated @ R.T
    # Translate back
    return rotated + origin

def frame_pose(t):
    """
    Compute joint positions at normalised time t∈[0,1].
    The bow is modelled as a smooth sinusoid (forward then back).
    """
    # Core bow angle (0 -> forward, then back)
    angle =  AMPLITUDE * np.sin(2 * np.pi * SAD_SLOW * t)
    pose = upright.copy()

    # Hip centre (mean of left & right hips)
    hip_c = pose[[HIP_L, HIP_R]].mean(axis=0)

    # Rotate torso (everything above hips) around hip centre
    pose[TORSO_INDICES] = rotate(pose[TORSO_INDICES], -angle, hip_c)

    # Optional subtle hand swing to enhance sadness (small lagged motion)
    hand_angle = -0.4 * angle        # hands lag torso a bit
    hand_indices = np.array([6, 7])  # left & right wrist indices
    pose[hand_indices] = rotate(pose[hand_indices], hand_angle, pose[[2, 3]].mean(axis=0))

    # Very slight knee flexion to keep balance
    knee_bend = 0.15 * (1 - np.cos(angle))     # 0 when upright, ~0.3 rad when fully bent
    knee_indices = np.array([11, 12])
    # rotate knees around hips (approx simplistic)
    for k, h in zip(knee_indices, [HIP_L, HIP_R]):
        pose[k] = rotate(pose[k:k+1], knee_bend, pose[h:h+1]).ravel()
    # Ankles follow knees a little
    ankle_shift = 0.25 * knee_bend
    ankle_indices = np.array([13, 14])
    for a, k in zip(ankle_indices, knee_indices):
        pose[a] = rotate(pose[a:a+1], ankle_shift, pose[k:k+1]).ravel()

    return pose

def update(frame_number):
    # Normalised time 0–1
    t = (frame_number % N_FRAMES) / N_FRAMES
    pose = frame_pose(t)
    scatter.set_offsets(pose)
    return scatter,

ani = FuncAnimation(fig,
                    update,
                    frames=N_FRAMES,
                    interval=1000/FPS,
                    blit=True,
                    repeat=True)

if __name__ == "__main__":
    plt.show()
