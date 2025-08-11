
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sin, cos, radians

# Fixed parameters defining the skeleton's proportions
d_shoulder = 0.1   # Horizontal distance from torso to shoulder
h_shoulder = 0.1   # Vertical distance from torso to shoulder
l_upper_arm = 0.2  # Length of upper arm
l_forearm = 0.2    # Length of forearm
d_hip = 0.05       # Horizontal distance from torso to hip
h_hip = 0.2        # Vertical distance from torso to hip
l_thigh = 0.3      # Length of thigh
l_shank = 0.3      # Length of shank
l_foot = 0.1       # Length of foot
h_neck = 0.15      # Vertical distance from torso to neck
h_head = 0.05      # Vertical distance from neck to head

# Key frames for joint angles (in degrees) over time t from 0 to 1
# These define the motion: standing -> crouch -> jump -> airborne -> land -> standing
hip_key_frames = [(0, 0), (0.2, 30), (0.4, -30), (0.6, 0), (0.8, 30), (1.0, 0)]
knee_key_frames = [(0, 0), (0.2, 60), (0.4, -30), (0.6, 0), (0.8, 60), (1.0, 0)]
ankle_key_frames = [(0, 0), (0.2, -30), (0.4, 0), (0.6, 0), (0.8, -30), (1.0, 0)]
shoulder_key_frames = [(0, 0), (0.2, -15), (0.4, 30), (0.6, 0), (0.8, -15), (1.0, 0)]
elbow_key_frames = [(0, 0), (0.2, 15), (0.4, 0), (0.6, 0), (0.8, 15), (1.0, 0)]

def interpolate(t, key_frames):
    """Linearly interpolate joint angles between key frames."""
    if t <= key_frames[0][0]:
        return key_frames[0][1]
    if t >= key_frames[-1][0]:
        return key_frames[-1][1]
    for i in range(len(key_frames) - 1):
        t1, phi1 = key_frames[i]
        t2, phi2 = key_frames[i + 1]
        if t1 <= t <= t2:
            return phi1 + (phi2 - phi1) * (t - t1) / (t2 - t1)

def y_torso(t):
    """Define vertical position of torso with a lower jump for 'heavy weight'."""
    return 0.8 + 0.4 * t * (1 - t)  # Peaks at 0.9, reflecting a heavy, less vigorous jump

def compute_positions(t):
    """Compute positions of 15 points at time t using forward kinematics."""
    # Interpolate joint angles
    phi_hip = interpolate(t, hip_key_frames)
    phi_knee = interpolate(t, knee_key_frames)
    phi_ankle = interpolate(t, ankle_key_frames)
    phi_shoulder = interpolate(t, shoulder_key_frames)
    phi_elbow = interpolate(t, elbow_key_frames)

    # Base position of torso (centered horizontally)
    torso_pos = (0, y_torso(t))

    # Compute positions relative to torso
    left_hip_pos = (torso_pos[0] - d_hip, torso_pos[1] - h_hip)
    right_hip_pos = (torso_pos[0] + d_hip, torso_pos[1] - h_hip)
    left_shoulder_pos = (torso_pos[0] - d_shoulder, torso_pos[1] + h_shoulder)
    right_shoulder_pos = (torso_pos[0] + d_shoulder, torso_pos[1] + h_shoulder)
    neck_pos = (torso_pos[0], torso_pos[1] + h_neck)
    head_pos = (neck_pos[0], neck_pos[1] + h_head)

    # Left leg: hip -> knee -> ankle -> toe
    left_knee_pos = (
        left_hip_pos[0] + l_thigh * sin(radians(phi_hip)),
        left_hip_pos[1] - l_thigh * cos(radians(phi_hip))
    )
    left_ankle_pos = (
        left_knee_pos[0] + l_shank * sin(radians(phi_knee)),
        left_knee_pos[1] - l_shank * cos(radians(phi_knee))
    )
    left_toe_pos = (
        left_ankle_pos[0] + l_foot * cos(radians(phi_ankle)),
        left_ankle_pos[1] + l_foot * sin(radians(phi_ankle))
    )

    # Right leg: symmetric motion
    right_knee_pos = (
        right_hip_pos[0] + l_thigh * sin(radians(phi_hip)),
        right_hip_pos[1] - l_thigh * cos(radians(phi_hip))
    )
    right_ankle_pos = (
        right_knee_pos[0] + l_shank * sin(radians(phi_knee)),
        right_knee_pos[1] - l_shank * cos(radians(phi_knee))
    )
    right_toe_pos = (
        right_ankle_pos[0] + l_foot * cos(radians(phi_ankle)),
        right_ankle_pos[1] + l_foot * sin(radians(phi_ankle))
    )

    # Left arm: shoulder -> elbow -> wrist (reduced motion for 'sadness')
    left_elbow_pos = (
        left_shoulder_pos[0] + l_upper_arm * sin(radians(phi_shoulder)),
        left_shoulder_pos[1] - l_upper_arm * cos(radians(phi_shoulder))
    )
    left_wrist_pos = (
        left_elbow_pos[0] + l_forearm * sin(radians(phi_elbow)),
        left_elbow_pos[1] - l_forearm * cos(radians(phi_elbow))
    )

    # Right arm: symmetric motion
    right_elbow_pos = (
        right_shoulder_pos[0] + l_upper_arm * sin(radians(phi_shoulder)),
        right_shoulder_pos[1] - l_upper_arm * cos(radians(phi_shoulder))
    )
    right_wrist_pos = (
        right_elbow_pos[0] + l_forearm * sin(radians(phi_elbow)),
        right_elbow_pos[1] - l_forearm * cos(radians(phi_elbow))
    )

    # List of all 15 point positions in order
    positions = [
        head_pos,           # Head
        left_shoulder_pos,  # Left shoulder
        right_shoulder_pos, # Right shoulder
        left_elbow_pos,     # Left elbow
        right_elbow_pos,    # Right elbow
        left_wrist_pos,     # Left wrist
        right_wrist_pos,    # Right wrist
        torso_pos,          # Torso (chest)
        left_hip_pos,       # Left hip
        right_hip_pos,      # Right hip
        left_knee_pos,      # Left knee
        right_knee_pos,     # Right knee
        left_ankle_pos,     # Left ankle
        right_ankle_pos,    # Right ankle
        left_toe_pos,       # Left toe
        right_toe_pos       # Right toe
    ]
    return positions

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)    # Wide enough to see all points
ax.set_ylim(0, 1.5)   # Tall enough for jump height
ax.set_aspect('equal')  # Maintain proportions
ax.set_facecolor('black')  # Solid black background
ax.axis('off')        # Remove axes for pure point-light display

# Initialize scatter plot with 15 white points
scat = ax.scatter([], [], s=10, c='white')

def update(frame):
    """Update point positions for each animation frame."""
    t = frame / 29  # Map frame 0-29 to t=0-1
    positions = compute_positions(t)
    x = [pos[0] for pos in positions]
    y = [pos[1] for pos in positions]
    scat.set_offsets(list(zip(x, y)))
    return scat,

# Create animation: 30 frames at 30 fps (1 second duration)
ani = FuncAnimation(fig, update, frames=30, interval=1000/30, blit=True)

plt.show()
