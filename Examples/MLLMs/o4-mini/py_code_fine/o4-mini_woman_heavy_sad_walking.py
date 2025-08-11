
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Animation parameters
T = 1.0                # duration of one gait cycle (seconds)
fps = 60               # frames per second
frames = int(T * fps)  # total frames per cycle

# Segment lengths (in arbitrary units)
thigh_len = 0.4
shin_len = 0.4
torso_len = 0.6
neck_len = 0.1
head_len = 0.2
upper_arm_len = 0.3
forearm_len = 0.3

# Width offsets
shoulder_width = 0.4
hip_width = 0.3

# Motion amplitudes
A_thigh = 0.4    # thigh swing amplitude (rad)
A_knee = 0.7     # knee flex amplitude (rad)
A_arm = 0.5      # arm swing amplitude (rad)
A_vert = 0.05    # vertical pelvis oscillation amplitude

# Elbow bend (constant)
elbow_bend = 0.2

# Angular frequency
omega = 2 * np.pi / T

# Base height of pelvis above "ground"
base_pelvis_y = thigh_len + shin_len - 0.05

# Set up figure
fig, ax = plt.subplots(figsize=(5, 7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2.5)
ax.set_aspect('equal')

# Initialize scatter plot for 15 points
pts = np.zeros((15, 2))
scatter = ax.scatter(pts[:, 0], pts[:, 1], c='white', s=80)

def update(frame):
    t = frame / fps
    # Pelvis (root)
    pelvis_x = 0.0
    pelvis_y = base_pelvis_y + A_vert * np.sin(2 * omega * t)
    pelvis = np.array([pelvis_x, pelvis_y])

    # Neck and head
    neck = pelvis + np.array([0, torso_len])
    head = neck + np.array([0, head_len])

    # Shoulders
    l_shoulder = neck + np.array([-shoulder_width/2, 0])
    r_shoulder = neck + np.array([ shoulder_width/2, 0])

    # Hips
    l_hip = pelvis + np.array([-hip_width/2, 0])
    r_hip = pelvis + np.array([ hip_width/2, 0])

    # Thigh angles (relative to vertical)
    theta_th_l =  A_thigh * np.sin(omega * t)
    theta_th_r =  A_thigh * np.sin(omega * t + np.pi)

    # Knee angles (relative to thigh)
    theta_kn_l =  A_knee * np.sin(2 * omega * t)
    theta_kn_r =  A_knee * np.sin(2 * omega * t + np.pi)

    # Arm swing angles (relative to vertical)
    phi_arm_l =  A_arm * np.sin(omega * t + np.pi)
    phi_arm_r =  A_arm * np.sin(omega * t)

    # Build leg joints
    # Left leg
    l_knee = l_hip + thigh_len * np.array([np.sin(theta_th_l), -np.cos(theta_th_l)])
    shin_angle_l = theta_th_l - theta_kn_l
    l_ankle = l_knee + shin_len * np.array([np.sin(shin_angle_l), -np.cos(shin_angle_l)])

    # Right leg
    r_knee = r_hip + thigh_len * np.array([np.sin(theta_th_r), -np.cos(theta_th_r)])
    shin_angle_r = theta_th_r - theta_kn_r
    r_ankle = r_knee + shin_len * np.array([np.sin(shin_angle_r), -np.cos(shin_angle_r)])

    # Build arm joints
    # Left arm
    l_elbow = l_shoulder + upper_arm_len * np.array([np.sin(phi_arm_l), -np.cos(phi_arm_l)])
    l_wrist = l_elbow + forearm_len * np.array([np.sin(phi_arm_l - elbow_bend),
                                                 -np.cos(phi_arm_l - elbow_bend)])
    # Right arm
    r_elbow = r_shoulder + upper_arm_len * np.array([np.sin(phi_arm_r), -np.cos(phi_arm_r)])
    r_wrist = r_elbow + forearm_len * np.array([np.sin(phi_arm_r - elbow_bend),
                                                 -np.cos(phi_arm_r - elbow_bend)])

    # Pack all 15 points in order
    pts[0]  = pelvis
    pts[1]  = neck
    pts[2]  = head
    pts[3]  = l_shoulder
    pts[4]  = r_shoulder
    pts[5]  = l_elbow
    pts[6]  = r_elbow
    pts[7]  = l_wrist
    pts[8]  = r_wrist
    pts[9]  = l_hip
    pts[10] = r_hip
    pts[11] = l_knee
    pts[12] = r_knee
    pts[13] = l_ankle
    pts[14] = r_ankle

    scatter.set_offsets(pts)
    return scatter,

# Run animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True, repeat=True)
plt.show()
