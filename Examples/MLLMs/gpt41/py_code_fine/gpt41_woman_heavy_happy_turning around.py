
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
NUM_POINTS = 15
FRAME_COUNT = 120  # one full turn in 120 frames (~4 sec at 30fps)
FPS = 30

# Joint definitions (x, y, z offset, relative to body origin)
#            0: head
#         1, 2: shoulders L, R
#         3, 4: elbows   L, R
#         5, 6: wrists   L, R
#         7, 8: hips     L, R
#         9,10: knees    L, R
#        11,12: ankles   L, R
#        13,14: chest, lower back (to accentuate bulk)
skeleton_offsets = np.array([
    [0.0,  1.1, 0.0],    # head
    [-0.23, 0.85, 0.0],  # shoulder L
    [0.23, 0.85, 0.0],   # shoulder R
    [-0.42, 0.5, 0.0],   # elbow L
    [0.42, 0.5, 0.0],    # elbow R
    [-0.5, 0.15, 0.0],   # wrist L
    [0.5, 0.15, 0.0],    # wrist R
    [-0.21, 0.1, 0.0],   # hip L
    [0.21, 0.1, 0.0],    # hip R
    [-0.21, -0.55, 0.0], # knee L
    [0.21, -0.55, 0.0],  # knee R
    [-0.21, -1.1, 0.0],  # ankle L
    [0.21, -1.1, 0.0],   # ankle R
    [0.0, 0.6, 0.15],    # chest (bulky, forward)
    [0.0, 0.25, -0.18],  # lower back (bulky, backward)
])

# "happy" gait & "heavy" weight parameters to subtly change arm swing & bounce
def pose(t):
    """
    Returns the 15x3 matrix of joint positions at time t (in [0,1]), in 3D.
    t: normalized time [0,1] for animation cycle (turn).
    """
    # Parameters for a 'turning around' motion:
    # 0 <= t < 0.5: turning from facing forward to side/back
    # 0.5 <= t < 1.0: return to facing forward (completing 360deg turn)
    # Turning: Yaw rotation about the vertical axis through hips.
    # Arms swinging, spine & chest may sway, slight up/down movement
    theta = 2 * np.pi * t  # 0 to 2pi, a full turn, CCW

    # Turn axis is the Y axis (vertical)
    # For "heavy weight", emphasize the width (shoulders, chest)
    offsets = skeleton_offsets.copy()

    # Basic bipedal sway: up/down head bob, shoulder sway, shoulder roll
    # Hip bounce (up/down) -- emphasizing "heavy weight" 
    bob = 0.06 * np.sin(2*theta)  # bounce every half-turn
    chest_forward = 0.05 * np.sin(theta)
    arms_back_swing = 0.16 * np.sin(theta + np.pi)  # happy arm swinging
    arms_forward_swing = -0.12 * np.sin(theta + np.pi)
    # Happy step, hips sway gently left/right with turning phase
    hip_sway = 0.11 * np.sin(theta)
    heavy_wobble = 0.025 * np.sin(4*theta)
    # Slight smile: tilt head up at certain points
    head_tilt = 0.10 * np.sin(theta) # up/down --> 'happy'

    # Apply (body center at (0,0,0))
    joint_xyz = offsets.copy()
    # Head bob and tilt
    joint_xyz[0, 1] += bob + 0.01 * np.cos(4*theta)
    joint_xyz[0, 2] += 0.13 * np.sin(theta)
    joint_xyz[0, 1] += head_tilt
    # Chest point forward on happy bounce
    joint_xyz[13, 2] += chest_forward
    joint_xyz[13, 1] += bob
    # Lower back follows general body tilt
    joint_xyz[14, 2] -= 0.02 * np.sin(theta)
    # Shoulders sway & arms swing
    joint_xyz[1, 0] -= hip_sway + 0.02*heavy_wobble        # L shldr
    joint_xyz[2, 0] += hip_sway + 0.02*heavy_wobble        # R shldr
    joint_xyz[1, 2] += arms_back_swing                     # L shldr
    joint_xyz[2, 2] += arms_forward_swing                  # R shldr
    # Elbows, wrists swing slowly
    joint_xyz[3, 2] += arms_back_swing * 1.05
    joint_xyz[4, 2] += arms_forward_swing * 1.05
    joint_xyz[5, 2] += arms_back_swing * 1.14
    joint_xyz[6, 2] += arms_forward_swing * 1.14
    # Outward swing (because turning), accentuate left-right
    joint_xyz[3, 0] -= 0.06 * np.cos(theta)
    joint_xyz[4, 0] += 0.06 * np.cos(theta)
    joint_xyz[5, 0] -= 0.12 * np.cos(theta)
    joint_xyz[6, 0] += 0.12 * np.cos(theta)
    # All arms get shoulder bob
    joint_xyz[[3,4,5,6], 1] += bob
    # Hips bounce & sway
    joint_xyz[[7,8], 1] += bob
    joint_xyz[7, 0] -= hip_sway * 0.7
    joint_xyz[8, 0] += hip_sway * 0.7
    # Knees/ankles -- little movement (turn)
    # All points: add a little in-front/back swing (z) on turn
    forward_move = 0.06 * np.sin(theta)
    joint_xyz[:, 2] += forward_move
    # Heavy body: add extra width for chest/hips/shoulders (as if body mass)
    joint_xyz[[1,2,7,8], 0] *= 1.33

    # Apply turn: rotate all points around vertical (y) by theta
    # The 'woman' turns around, about the average of her two hips
    hip_center = (joint_xyz[7] + joint_xyz[8]) / 2
    # Translate so hip_center is at origin
    rotated = joint_xyz - hip_center
    # Build rot matrix for angle theta (CCW)
    rotmat = np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [ 0            , 1, 0           ],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    rotated = rotated @ rotmat.T
    # Translate back
    joint_xyz = rotated + hip_center
    return joint_xyz

# For 2D projection, simulate perspective: camera at some distance
def project(joints3d, camera_distance=3.5):
    # Simple orthographic with slight perspective
    # Camera is looking from (0, 0.7, camera_distance)
    scale = 220
    focal_length = 2.0
    z = joints3d[:, 2] + camera_distance
    x_proj = scale * (joints3d[:, 0] / z)
    y_proj = scale * (joints3d[:, 1] / z)
    return x_proj, y_proj

# Matplotlib animation setup
fig, ax = plt.subplots(figsize=(4,8))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')
# Set axis limits (fixed in pixels)
ax.set_xlim(-100, 100)
ax.set_ylim(-130, 210)
# Draw scatter
scat = ax.scatter(np.zeros(NUM_POINTS), np.zeros(NUM_POINTS),
                  s=60, c='white', edgecolor='none')

def animate(frame):
    t = (frame % FRAME_COUNT) / (FRAME_COUNT - 1)
    j3d = pose(t)
    x, y = project(j3d)
    scat.set_offsets(np.c_[x, y])
    return scat,

ani = animation.FuncAnimation(
    fig, animate, frames=FRAME_COUNT, interval=1000/FPS, blit=True
)

plt.show()
