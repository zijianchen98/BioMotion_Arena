
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Key points: 0: head, 1: neck, 2: left shoulder, 3: right shoulder, 4: left elbow, 5: right elbow,
# 6: left wrist, 7: right wrist, 8: midhip, 9: left hip, 10: right hip, 11: left knee, 12: right knee,
# 13: left ankle, 14: right ankle

# Constants
step_length = 0.3
step_height = 0.05
hip_vertical_amplitude = 0.04
torso_height = 1.0
torso_forward = 0.1
head_height = 0.25
shoulder_width = 0.4
hip_width = 0.35
upper_arm_length = 0.3
forearm_length = 0.25
elbow_angle = 0.3
arm_swing_amplitude = 0.3
thigh_length = 0.4
shin_length = 0.4

def get_point_positions(t):
    y_hip = hip_vertical_amplitude * math.sin(2 * math.pi * t)

    points = np.zeros((15, 2))

    # Hip center (point 8)
    points[8] = [0, y_hip]
    # Left hip (point 9)
    points[9] = [-hip_width / 2, y_hip]
    # Right hip (point 10)
    points[10] = [hip_width / 2, y_hip]
    # Neck (point 1) - slightly forward to simulate bent posture
    points[1] = [torso_forward, y_hip + torso_height]
    # Head (point 0)
    points[0] = [torso_forward, y_hip + torso_height + head_height]
    # Left shoulder (point 2)
    points[2] = [torso_forward - shoulder_width / 2, y_hip + torso_height]
    # Right shoulder (point 3)
    points[3] = [torso_forward + shoulder_width / 2, y_hip + torso_height]

    # Right arm - simplified arm motion with elbow bend
    arm_angle_right = arm_swing_amplitude * math.sin(2 * math.pi * t + math.pi / 2)
    points[5][0] = points[3][0] + upper_arm_length * math.sin(arm_angle_right)
    points[5][1] = points[3][1] - upper_arm_length * math.cos(arm_angle_right)
    points[7][0] = points[5][0] + forearm_length * math.sin(arm_angle_right + elbow_angle)
    points[7][1] = points[5][1] - forearm_length * math.cos(arm_angle_right + elbow_angle)

    # Left arm
    arm_angle_left = arm_swing_amplitude * math.sin(2 * math.pi * t - math.pi / 2)
    points[4][0] = points[2][0] + upper_arm_length * math.sin(arm_angle_left)
    points[4][1] = points[2][1] - upper_arm_length * math.cos(arm_angle_left)
    points[6][0] = points[4][0] + forearm_length * math.sin(arm_angle_left + elbow_angle)
    points[6][1] = points[4][1] - forearm_length * math.cos(arm_angle_left + elbow_angle)

    # Foot positions for the walking cycle
    # Right ankle (point 14)
    points[14][0] = step_length / 2 * math.sin(2 * math.pi * t - math.pi / 2)
    if t < 0.5:
        points[14][1] = 0
    else:
        points[14][1] = step_height * math.sin(2 * math.pi * (t - 0.5))

    # Left ankle (point 13)
    points[13][0] = step_length / 2 * math.sin(2 * math.pi * t + math.pi / 2)
    if t < 0.5:
        points[13][1] = step_height * math.sin(2 * math.pi * t)
    else:
        points[13][1] = 0

    # Calculate knee positions based on hips and ankles
    # Right knee (point 12)
    H = points[10].copy()
    A = points[14].copy()
    dx = A[0] - H[0]
    dy = A[1] - H[1]
    D = math.sqrt(dx * dx + dy * dy)
    a = (thigh_length**2 - shin_length**2 + D**2) / (2 * D) if D > 0 else 0
    h = math.sqrt(max(0, thigh_length**2 - a**2))
    if D == 0:
        points[12] = H
    else:
        P = H + a * (A - H) / D
        normal_vector = np.array([-dy, dx])
        normal_vector = normal_vector / D if D > 0 else normal_vector
        points[12] = P + h * normal_vector

    # Left knee (point 11)
    H = points[9].copy()
    A = points[13].copy()
    dx = A[0] - H[0]
    dy = A[1] - H[1]
    D = math.sqrt(dx * dx + dy * dy)
    a = (thigh_length**2 - shin_length**2 + D**2) / (2 * D) if D > 0 else 0
    h = math.sqrt(max(0, thigh_length**2 - a**2))
    if D == 0:
        points[11] = H
    else:
        P = H + a * (A - H) / D
        normal_vector = np.array([-dy, dx])
        normal_vector = normal_vector / D if D > 0 else normal_vector
        points[11] = P + h * normal_vector

    return points

fig, ax = plt.subplots(figsize=(7, 8))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-0.3, 1.7)
points_plot, = ax.plot([], [], 'wo', markersize=8)

def init():
    points_plot.set_data([], [])
    return [points_plot]

def update(frame):
    t = frame / 30.0
    points = get_point_positions(t)
    points_plot.set_data(points[:, 0], points[:, 1])
    return [points_plot]

ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=30)
plt.tight_layout()
plt.show()
