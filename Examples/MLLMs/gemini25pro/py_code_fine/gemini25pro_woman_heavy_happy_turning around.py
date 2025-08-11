
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# --- Configuration ---
NUM_FRAMES = 180
FPS = 30
INTERVAL = 1000 / FPS

# --- Skeleton Definition ---
# Indices for 15 joints
HEAD, STERNUM, PELVIS, L_SHOULDER, R_SHOULDER, L_ELBOW, R_ELBOW, \
L_WRIST, R_WRIST, L_HIP, R_HIP, L_KNEE, R_KNEE, L_ANKLE, R_ANKLE = range(15)

# Initial 3D pose, wider proportions for a "heavy" build
initial_pose_3d = np.array([
    [0.0,   0.85,  0.0],   # HEAD
    [0.0,   0.50,  0.0],   # STERNUM
    [0.0,   0.0,   0.0],   # PELVIS
    [-0.25,  0.50,  0.0],   # L_SHOULDER
    [0.25,  0.50,  0.0],   # R_SHOULDER
    [-0.25,  0.10,  0.0],   # L_ELBOW
    [0.25,  0.10,  0.0],   # R_ELBOW
    [-0.25, -0.30,  0.0],   # L_WRIST
    [0.25, -0.30,  0.0],   # R_WRIST
    [-0.18,  0.0,   0.0],   # L_HIP
    [0.18,  0.0,   0.0],   # R_HIP
    [-0.18, -0.40,  0.0],   # L_KNEE
    [0.18, -0.40,  0.0],   # R_KNEE
    [-0.18, -0.80,  0.0],   # L_ANKLE
    [0.18, -0.80,  0.0]    # R_ANKLE
])

# --- Animation Setup ---
fig, ax = plt.subplots()
fig.set_size_inches(5, 8)
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

points, = ax.plot([], [], 'o', color='white', markersize=7)

# --- Animation Logic ---
def y_rotation_matrix(theta):
    """Returns a 3D rotation matrix for a given angle around the Y-axis."""
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    return np.array([
        [cos_t, 0, sin_t],
        [0,     1,   0],
        [-sin_t, 0, cos_t]
    ])

def animate(frame_num):
    """Calculates the point positions for a given frame."""
    t = frame_num / NUM_FRAMES
    
    # Base rotation
    body_angle = t * 2 * np.pi
    R_body = y_rotation_matrix(body_angle)
    current_pose = initial_pose_3d.copy()

    # Arm swing (applied pre-rotation)
    arm_swing_freq = 2
    arm_swing_amp = 0.3
    z_swing = arm_swing_amp * np.sin(t * 2 * np.pi * arm_swing_freq)
    current_pose[[L_ELBOW, L_WRIST], 2] += z_swing
    current_pose[[R_ELBOW, R_WRIST], 2] -= z_swing

    rotated_pose = current_pose @ R_body.T

    # Vertical bob for weight shift (applied post-rotation)
    bob_freq = 2
    bob_amp = 0.03
    y_bob = -bob_amp * (1 - np.cos(t * 2 * np.pi * bob_freq))
    rotated_pose[:, 1] += y_bob

    # Head turns slightly ahead of the body
    head_lead_phase = np.sin(t * np.pi * 2)
    head_lead_angle = 0.3
    R_head = y_rotation_matrix(body_angle + head_lead_angle * head_lead_phase)
    rotated_pose[HEAD] = initial_pose_3d[HEAD] @ R_head.T
    rotated_pose[HEAD, 1] += y_bob

    # Foot shuffle to simulate stepping
    shuffle_freq = 2
    shuffle_amp_x = 0.04
    shuffle_amp_y = 0.04
    
    phase_L = t * 2 * np.pi * shuffle_freq
    lift_L = shuffle_amp_y * abs(np.sin(phase_L))
    rotated_pose[L_ANKLE, 0] += shuffle_amp_x * np.sin(phase_L)
    rotated_pose[L_ANKLE, 1] += lift_L
    rotated_pose[L_KNEE, 1] += lift_L * 0.5

    phase_R = t * 2 * np.pi * shuffle_freq + np.pi
    lift_R = shuffle_amp_y * abs(np.sin(phase_R))
    rotated_pose[R_ANKLE, 0] += shuffle_amp_x * np.sin(phase_R)
    rotated_pose[R_ANKLE, 1] += lift_R
    rotated_pose[R_KNEE, 1] += lift_R * 0.5

    # Project to 2D and update plot
    projected_points = rotated_pose[:, :2]
    points.set_data(projected_points[:, 0], projected_points[:, 1])

    return points,

# --- Create and run the animation ---
ani = animation.FuncAnimation(fig, animate, frames=NUM_FRAMES,
                              interval=INTERVAL, blit=True)

plt.show()
