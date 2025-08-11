
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import sin, cos, pi, sqrt

# Constants
T = 1.0  # period of one gait cycle
step_length = 0.3
h = 0.1  # height of foot lift during swing
L_thigh = 0.5
L_shin = 0.5
L_upper_arm = 0.35
L_forearm = 0.35
dx_shoulder = 0.1
dy_shoulder = 0.2
dx_hip = 0.1
dy_hip = -0.4
dy_neck = 0.1
dy_head = 0.15
y0 = 1.0  # average height of torso
A = 0.05  # amplitude of vertical oscillation
W = 0.2  # amplitude of arm swing

# Function to compute joint position using inverse kinematics
def get_joint_position(p1, p2, L1, L2, side='left'):
    xh, yh = p1
    xa, ya = p2
    v = (xa - xh, ya - yh)
    d = sqrt(v[0]**2 + v[1]**2)
    if d > L1 + L2 or d < abs(L1 - L2):
        return None  # no solution
    a = (L1**2 - L2**2 + d**2) / (2 * d)
    h = sqrt(L1**2 - a**2)
    p = (xh + a * v[0] / d, yh + a * v[1] / d)
    u_perp = (-v[1] / d, v[0] / d)
    joint1 = (p[0] + h * u_perp[0], p[1] + h * u_perp[1])
    joint2 = (p[0] - h * u_perp[0], p[1] - h * u_perp[1])
    # Choose based on side
    cross1 = (joint1[0] - xh) * v[1] - (joint1[1] - yh) * v[0]
    if (side == 'left' and cross1 < 0) or (side == 'right' and cross1 > 0):
        return joint1
    else:
        return joint2

# Function to get all positions at time t
def get_positions(t):
    phase = (t % T) / T
    # Torso position
    x_torso = 0
    y_torso = y0 + A * sin(4 * pi * phase)
    # Shoulders
    x_shoulder_left = x_torso - dx_shoulder
    y_shoulder_left = y_torso + dy_shoulder
    x_shoulder_right = x_torso + dx_shoulder
    y_shoulder_right = y_torso + dy_shoulder
    # Hips
    x_hip_left = x_torso - dx_hip
    y_hip_left = y_torso + dy_hip
    x_hip_right = x_torso + dx_hip
    y_hip_right = y_torso + dy_hip
    # Neck and head
    x_neck = x_torso
    y_neck = y_torso + dy_neck
    x_head = x_torso
    y_head = y_torso + dy_head
    # Ankles
    if phase < 0.5:
        # Left leg in stance
        x_ankle_left = - step_length * (2 * phase)
        y_ankle_left = 0
        # Right leg in swing
        x_ankle_right = -step_length + 4 * step_length * phase
        y_ankle_right = h * sin(pi * (2 * phase))
    else:
        # Left leg in swing
        x_ankle_left = -step_length + 4 * step_length * (phase - 0.5)
        y_ankle_left = h * sin(pi * (2 * (phase - 0.5)))
        # Right leg in stance
        x_ankle_right = step_length - step_length * (2 * (phase - 0.5))
        y_ankle_right = 0
    # Wrists
    x_wrist_left = x_shoulder_left - W * cos(2 * pi * phase)
    y_wrist_left = y_shoulder_left - L_upper_arm - L_forearm
    x_wrist_right = x_shoulder_right + W * cos(2 * pi * phase)
    y_wrist_right = y_shoulder_right - L_upper_arm - L_forearm
    # Calculate knees
    knee_left = get_joint_position((x_hip_left, y_hip_left), (x_ankle_left, y_ankle_left), L_thigh, L_shin, side='left')
    knee_right = get_joint_position((x_hip_right, y_hip_right), (x_ankle_right, y_ankle_right), L_thigh, L_shin, side='right')
    # Calculate elbows
    elbow_left = get_joint_position((x_shoulder_left, y_shoulder_left), (x_wrist_left, y_wrist_left), L_upper_arm, L_forearm, side='left')
    elbow_right = get_joint_position((x_shoulder_right, y_shoulder_right), (x_wrist_right, y_wrist_right), L_upper_arm, L_forearm, side='right')
    # Torso center
    x_torso_center = x_torso
    y_torso_center = y_torso
    # Collect all positions
    positions = [
        (x_head, y_head),  # head
        (x_neck, y_neck),  # neck
        (x_shoulder_left, y_shoulder_left),  # L shoulder
        (x_shoulder_right, y_shoulder_right),  # R shoulder
        elbow_left,  # L elbow
        elbow_right,  # R elbow
        (x_wrist_left, y_wrist_left),  # L wrist
        (x_wrist_right, y_wrist_right),  # R wrist
        (x_torso_center, y_torso_center),  # torso center
        (x_hip_left, y_hip_left),  # L hip
        (x_hip_right, y_hip_right),  # R hip
        knee_left,  # L knee
        knee_right,  # R knee
        (x_ankle_left, y_ankle_left),  # L ankle
        (x_ankle_right, y_ankle_right),  # R ankle
    ]
    return positions

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_xticks([])
ax.set_yticks([])

# Create scatter plot
scatter = ax.scatter([], [], c='white', s=20)

# Update function for animation
def update(frame):
    t = frame * 0.01  # dt = 0.01 s
    positions = get_positions(t)
    x = [p[0] for p in positions if p is not None]
    y = [p[1] for p in positions if p is not None]
    scatter.set_offsets(np.column_stack((x, y)))
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(1000), interval=10, blit=True)

plt.show()
