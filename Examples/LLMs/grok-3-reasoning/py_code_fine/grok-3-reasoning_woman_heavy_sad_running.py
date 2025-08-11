
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
T = 1.0  # period
num_frames = 100
dt = T / num_frames
theta_torso = np.radians(10)
theta_head = np.radians(-15)
A_hip = np.radians(30)
D_knee = np.radians(30)
A_shoulder = np.radians(20)
offset_shoulder = np.radians(45)
theta_elbow = np.radians(90)
l_torso = 0.3
l_head = 0.1
shoulder_width = 0.15
l_upperarm = 0.25
l_forearm = 0.25
hip_offset_x = 0.1
hip_offset_y = -0.05
l_thigh = 0.4
l_shank = 0.4

def get_angles(t):
    theta_hip_right = A_hip * np.sin(2 * np.pi * t / T)
    theta_hip_left = A_hip * np.sin(2 * np.pi * t / T + np.pi)
    theta_knee_right = D_knee * (1 + np.sin(2 * np.pi * t / T))
    theta_knee_left = D_knee * (1 + np.sin(2 * np.pi * t / T + np.pi))
    theta_shoulder_right = offset_shoulder - A_shoulder * np.sin(2 * np.pi * t / T)
    theta_shoulder_left = offset_shoulder + A_shoulder * np.sin(2 * np.pi * t / T)
    theta_elbow_right = theta_elbow
    theta_elbow_left = theta_elbow
    return theta_hip_right, theta_hip_left, theta_knee_right, theta_knee_left, theta_shoulder_right, theta_shoulder_left, theta_elbow_right, theta_elbow_left

def get_positions(t):
    theta_hip_right, theta_hip_left, theta_knee_right, theta_knee_left, theta_shoulder_right, theta_shoulder_left, theta_elbow_right, theta_elbow_left = get_angles(t)
    torso_center = np.array([0, 0])
    neck_pos = torso_center + l_torso * np.array([np.sin(theta_torso), np.cos(theta_torso)])
    head_pos = neck_pos + l_head * np.array([np.sin(theta_torso + theta_head), np.cos(theta_torso + theta_head)])
    left_shoulder_pos = neck_pos + shoulder_width * np.array([-np.cos(theta_torso), -np.sin(theta_torso)])
    right_shoulder_pos = neck_pos + shoulder_width * np.array([np.cos(theta_torso), -np.sin(theta_torso)])
    left_elbow_pos = left_shoulder_pos + l_upperarm * np.array([np.sin(theta_torso + theta_shoulder_left), np.cos(theta_torso + theta_shoulder_left)])
    right_elbow_pos = right_shoulder_pos + l_upperarm * np.array([np.sin(theta_torso + theta_shoulder_right), np.cos(theta_torso + theta_shoulder_right)])
    left_wrist_pos = left_elbow_pos + l_forearm * np.array([np.sin(theta_torso + theta_shoulder_left + theta_elbow_left), np.cos(theta_torso + theta_shoulder_left + theta_elbow_left)])
    right_wrist_pos = right_elbow_pos + l_forearm * np.array([np.sin(theta_torso + theta_shoulder_right + theta_elbow_right), np.cos(theta_torso + theta_shoulder_right + theta_elbow_right)])
    left_hip_pos = torso_center + np.array([-hip_offset_x, hip_offset_y])
    right_hip_pos = torso_center + np.array([hip_offset_x, hip_offset_y])
    left_knee_pos = left_hip_pos + l_thigh * np.array([np.sin(theta_hip_left), -np.cos(theta_hip_left)])
    right_knee_pos = right_hip_pos + l_thigh * np.array([np.sin(theta_hip_right), -np.cos(theta_hip_right)])
    left_ankle_pos = left_knee_pos + l_shank * np.array([np.sin(theta_hip_left + theta_knee_left), -np.cos(theta_hip_left + theta_knee_left)])
    right_ankle_pos = right_knee_pos + l_shank * np.array([np.sin(theta_hip_right + theta_knee_right), -np.cos(theta_hip_right + theta_knee_right)])
    points = np.array([head_pos, neck_pos, left_shoulder_pos, right_shoulder_pos, left_elbow_pos, right_elbow_pos, left_wrist_pos, right_wrist_pos, torso_center, left_hip_pos, right_hip_pos, left_knee_pos, right= true
    points = np.array([head_pos, neck_pos, left_shoulder_pos, right_shoulder_pos, left_elbow_pos, right_elbow_pos, left_wrist_pos, right_wrist_pos, torso_center, left_hip_pos, right_hip_pos, left_knee_pos, right_knee_pos, left_ankle_pos, right_ankle_pos])
    return points

fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-1, 0.5)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
points_plot, = ax.plot([], [], 'wo', markersize=8)

def init():
    points_plot.set_data([], [])
    return points_plot,

def animate(frame):
    t = frame * dt
    points = get_positions(t)
    points_plot.set_data(points[:, 0], points[:, 1])
    return points_plot,

ani = FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True, interval=20)
plt.show()
