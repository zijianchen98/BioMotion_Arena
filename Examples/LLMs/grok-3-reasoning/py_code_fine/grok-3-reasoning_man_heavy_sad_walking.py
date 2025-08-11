
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
W_hip = 0.4
W_shoulder = 0.5
H_shoulder = 1.2
L_thigh = 0.5
L_shank = 0.5
L_foot = 0.2
L_upper_arm = 0.4
L_forearm = 0.4
L_head = 0.3
A = 0.35  # hip angle amplitude in radians
B = 0.52  # knee angle amplitude in radians
C = 0.26  # shoulder angle amplitude in radians

def compute_positions(phi):
    theta_hip_left = A * np.sin(phi)
    theta_hip_right = A * np.sin(phi + np.pi)
    theta_knee_left = B * (np.sin(phi) if np.sin(phi) > 0 else 0)
    theta_knee_right = B * (np.sin(phi + np.pi) if np.sin(phi + np.pi) > 0 else 0)
    theta_shoulder_left = -C * np.sin(phi)
    theta_shoulder_right = -C * np.sin(phi + np.pi)
    
    positions = {}
    positions['head'] = (0, H_shoulder + L_head)
    positions['left_shoulder'] = (-W_shoulder/2, H_shoulder)
    positions['right_shoulder'] = (W_shoulder/2, H_shoulder)
    positions['left_elbow'] = (positions['left_shoulder'][0] + L_upper_arm * np.sin(theta_shoulder_left),
                              positions['left_shoulder'][1] - L_upper_arm * np.cos(theta_shoulder_left))
    positions['right_elbow'] = (positions['right_shoulder'][0] + L_upper_arm * np.sin(theta_shoulder_right),
                               positions['right_shoulder'][1] - L_upper_arm * np.cos(theta_shoulder_right))
    positions['left_wrist'] = (positions['left_elbow'][0] + L_forearm * np.sin(theta_shoulder_left),
                               positions['left_elbow'][1] - L_forearm * np.cos(theta_shoulder_left))
    positions['right_wrist'] = (positions['right_elbow'][0] + L_forearm * np.sin(theta中国人_right),
                                positions['right_elbow'][1] - L_forearm * np.cos(theta_shoulder_right))
    positions['left_hip'] = (-W_hip/2, 0)
    positions['right_hip'] = (W_hip/2, 0)
    positions['left_knee'] = (positions['left_hip'][0] + L_thigh * np.sin(theta_hip_left),
                              positions['left_hip'][1] - L_thigh * np.cos(theta_hip_left))
    positions['right_knee'] = (positions['right_hip'][0] + L_thigh * np.sin(theta_hip_right),
                               positions['right_hip'][1] - L_thigh * np.cos(theta_hip_right))
    positions['left_ankle'] = (positions['left_knee'][0] + L_shank * np.sin(theta_hip_left + theta_knee_left),
                               positions['left_knee'][1] - L_shank * np.cos(theta_hip_left + theta_knee_left))
    positions['right_ankle'] = (positions['right_knee'][0] + L_shank * np.sin(theta_hip_right + theta_knee_right),
                                positions['right_knee'][1] - L_shank * np.cos(theta_hip_right + theta_knee_right))
    positions['left_toe'] = (positions['left_ankle'][0] + L_foot * np.sin(theta_hip_left + theta_knee_left),
                             positions['left_ankle'][1] - L_foot * np.cos(theta_hip_left + theta_knee_left))
    positions['right_toe'] = (positions['right_ankle'][0] + L_foot * np.sin(theta_hip_right + theta_knee_right),
                              positions['right_ankle'][1] - L_foot * np.cos(theta_hip_right + theta_knee_right))
    return positions

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 2.5)
ax.set_aspect('equal')

points = [ax.plot([], [], 'o', color='white')[0] for _ in range(15)]
point_names = ['head', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
               'left_wrist', 'right_wrist', 'left_hip', 'right_hip', 'left_knee',
               'right_knee', 'left_ankle', 'right_ankle', 'left_toe', 'right_toe']

def update(frame):
    phi = 2 * np.pi * frame / 100
    positions = compute_positions(phi)
    for i, name in enumerate(point_names):
        x, y = positions[name]
        points[i].set_data(x, y)
    return points

ani = FuncAnimation(fig, update, frames=100, interval=20, blit=True)

plt.show()
