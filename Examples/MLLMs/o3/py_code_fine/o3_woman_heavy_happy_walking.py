
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------------------#
#  Parameters that define body
# ------------------------------#
FPS                 = 30          # frames per second
SECS_PER_CYCLE      = 2.0         # time for a full left-right walking cycle
N_FRAMES            = int(FPS * SECS_PER_CYCLE)

# Segment lengths (roughly scaled for a heavy female walker)
HEAD_TO_SHOULDER    = 0.40
SHOULDER_TO_ELBOW   = 0.55
ELBOW_TO_WRIST      = 0.45
SHOULDER_TO_HIP_Y   = 0.75
HIP_TO_KNEE         = 0.65
KNEE_TO_ANKLE       = 0.65

# Lateral sizes
SHOULDER_WIDTH      = 0.70
HIP_WIDTH           = 0.80   # wider hips for heavy figure

# ------------------------------#
#  Function that builds a frame
# ------------------------------#
def body_points(t):
    """
    Return the 15 point-light coordinates (x, y) for time t (in seconds).
    Points are returned in the following order:
    0 head
    1 left shoulder   2 right shoulder
    3 left elbow      4 right elbow
    5 left wrist      6 right wrist
    7 left hip        8 right hip
    9 left knee      10 right knee
    11 left ankle    12 right ankle
    13 spine (mid-chest)
    14 pelvis (mid-hip)
    """
    # phase (0-2π) of gait cycle
    phase = 2*np.pi * (t % SECS_PER_CYCLE) / SECS_PER_CYCLE

    # small vertical body bobbing
    bob = 0.05 * np.sin(2*phase)

    # torso key levels
    pelvis_y   = 1.60 + bob
    spine_y    = pelvis_y + SHOULDER_TO_HIP_Y * 0.6
    shoulder_y = pelvis_y + SHOULDER_TO_HIP_Y
    head_y     = shoulder_y + HEAD_TO_SHOULDER

    # centres (x=0); walker stays roughly centred
    centre_x = 0.0

    # hip and shoulder centres (left/right)
    l_hip_x = centre_x - HIP_WIDTH/2
    r_hip_x = centre_x + HIP_WIDTH/2
    l_sh_x  = centre_x - SHOULDER_WIDTH/2
    r_sh_x  = centre_x + SHOULDER_WIDTH/2

    # ---------------- Legs ---------------- #
    # thigh swings (± ~26°)
    thigh_amp = 0.45
    l_thigh_ang =  thigh_amp * np.sin(phase)          # left leg
    r_thigh_ang =  thigh_amp * np.sin(phase + np.pi)  # right leg

    # knee flexion (offset so knee is never completely straight)
    knee_amp  = 0.60
    l_knee_ang = 0.40 + knee_amp * np.sin(phase + np.pi/2)
    r_knee_ang = 0.40 + knee_amp * np.sin(phase + np.pi/2 + np.pi)

    # Build left leg
    l_knee_x = l_hip_x + HIP_TO_KNEE * np.sin(l_thigh_ang)
    l_knee_y = pelvis_y - HIP_TO_KNEE * np.cos(l_thigh_ang)

    l_ankle_x = l_knee_x + KNEE_TO_ANKLE * np.sin(l_thigh_ang + l_knee_ang)
    l_ankle_y = l_knee_y - KNEE_TO_ANKLE * np.cos(l_thigh_ang + l_knee_ang)

    # Build right leg
    r_knee_x = r_hip_x + HIP_TO_KNEE * np.sin(r_thigh_ang)
    r_knee_y = pelvis_y - HIP_TO_KNEE * np.cos(r_thigh_ang)

    r_ankle_x = r_knee_x + KNEE_TO_ANKLE * np.sin(r_thigh_ang + r_knee_ang)
    r_ankle_y = r_knee_y - KNEE_TO_ANKLE * np.cos(r_thigh_ang + r_knee_ang)

    # ---------------- Arms ---------------- #
    # shoulders fixed (they already defined)
    # upper-arm swings (opposite phase to legs, smaller amplitude)
    upper_arm_amp = 0.50
    l_arm_ang =  upper_arm_amp * np.sin(phase + np.pi)     # left arm
    r_arm_ang =  upper_arm_amp * np.sin(phase)             # right arm

    # elbow flexion
    elbow_amp = 0.40
    l_elbow_ang = 0.30 + elbow_amp * np.sin(phase)
    r_elbow_ang = 0.30 + elbow_amp * np.sin(phase + np.pi)

    # Build left arm
    l_elbow_x = l_sh_x + SHOULDER_TO_ELBOW * np.sin(l_arm_ang)
    l_elbow_y = shoulder_y - SHOULDER_TO_ELBOW * np.cos(l_arm_ang)

    l_wrist_x = l_elbow_x + ELBOW_TO_WRIST * np.sin(l_arm_ang + l_elbow_ang)
    l_wrist_y = l_elbow_y - ELBOW_TO_WRIST * np.cos(l_arm_ang + l_elbow_ang)

    # Build right arm
    r_elbow_x = r_sh_x + SHOULDER_TO_ELBOW * np.sin(r_arm_ang)
    r_elbow_y = shoulder_y - SHOULDER_TO_ELBOW * np.cos(r_arm_ang)

    r_wrist_x = r_elbow_x + ELBOW_TO_WRIST * np.sin(r_arm_ang + r_elbow_ang)
    r_wrist_y = r_elbow_y - ELBOW_TO_WRIST * np.cos(r_arm_ang + r_elbow_ang)

    # Pack all 15 points
    pts = np.array([
        [centre_x,  head_y],        # 0 head
        [l_sh_x,    shoulder_y],    # 1 L shoulder
        [r_sh_x,    shoulder_y],    # 2 R shoulder
        [l_elbow_x, l_elbow_y],     # 3 L elbow
        [r_elbow_x, r_elbow_y],     # 4 R elbow
        [l_wrist_x, l_wrist_y],     # 5 L wrist
        [r_wrist_x, r_wrist_y],     # 6 R wrist
        [l_hip_x,   pelvis_y],      # 7 L hip
        [r_hip_x,   pelvis_y],      # 8 R hip
        [l_knee_x,  l_knee_y],      # 9 L knee
        [r_knee_x,  r_knee_y],      # 10 R knee
        [l_ankle_x, l_ankle_y],     # 11 L ankle
        [r_ankle_x, r_ankle_y],     # 12 R ankle
        [centre_x,  spine_y],       # 13 spine
        [centre_x,  pelvis_y]       # 14 pelvis
    ])
    return pts

# ------------------------------#
#      Prepare the figure
# ------------------------------#
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(3.5, 7), facecolor='black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Set bounds so the walker stays visible
ax.set_xlim(-2, 2)
ax.set_ylim(-0.5, 3.5)

# initial scatter (15 points)
points = body_points(0)
scatter = ax.scatter(points[:, 0], points[:, 1], s=60, color='white')

# ------------------------------#
#   Animation update function
# ------------------------------#
def update(frame):
    t = frame / FPS
    pts = body_points(t)
    scatter.set_offsets(pts)
    return scatter,

# ------------------------------#
#          Run animation
# ------------------------------#
ani = FuncAnimation(fig, update, frames=N_FRAMES, interval=1000/FPS, blit=True, repeat=True)

# Uncomment the next line to save as GIF (requires Pillow)
# ani.save("point_light_walker.gif", dpi=120, writer='pillow')

plt.show()
