
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
y_min = 0.35
y_max = 0.65
theta_knee_max = np.pi / 3  # 60 degrees
theta_knee_min = 0
theta_shoulder_min = 0
theta_shoulder_max = np.pi / 2  # 90 degrees
w_hip = 0.05
w_shoulder = 0.1
l_spine = 0.3
l_head = 0.1
l_thigh = 0.25
l_calf = 0.25
l_upper_arm = 0.15
l_lower_arm = 0.15

def get_positions(t):
    alpha = (1 - np.cos(2 * np.pi * t)) / 2
    y_waist = y_min + (y_max - y_min) * alpha
    theta_knee = theta_knee_max * (1 - alpha) + theta_knee_min * alpha
    theta_shoulder = theta_shoulder_min * (1 - alpha) + theta_shoulder_max * alpha
    
    waist = (0, y_waist)
    neck = (0, y_waist + l_spine)
    head = (0, y_waist + l_spine + l_head)
    left_shoulder = (-w_shoulder, y_waist + l_spine)
    left_elbow = (left_shoulder[0] + l_upper_arm * np.sin(theta_shoulder), left_shoulder[1] - l_upper_arm * np.cos(theta_shoulder))
    left_wrist = (left_elbow[0] + l_lower_arm * np.sin(theta_shoulder), left_elbow[1] - l_lower_arm * np.cos(theta_shoulder))
    right_shoulder = (w_shoulder, y_waist + l_spine)
    right_elbow = (right_shoulder[0] - l_upper_arm * np.sin(theta_shoulder), right_shoulder[1] - l_upper_arm * np.cos(theta_shoulder))
    right_wrist = (right_elbow[0] - l_lower_arm * np.sin(theta_shoulder), right_elbow[1] - l_lower_arm * np.cos(theta_shoulder))
    left_hip = (-w_hip, y_waist)
    left_knee = (left_hip[0], left_hip[1] - l_thigh)
    left_ankle = (left_knee[0] + l_calf * np.sin(theta_knee), left_knee[1] - l_calf * np.cos(theta_knee))
    right_hip = (w_hip, y_waist)
    right_knee = (right_hip[0], right_hip[1] - l_thigh)
    right_ankle = (right_knee[0] - l_calf * np.sin(theta_knee), right_knee[1] - l_calf * np.cos(theta_knee))
    
    points = [head, neck, waist, left_shoulder, left_elbow, left_wrist, right_shoulder, right_elbow, right_wrist, left_hip, left_knee, left_ankle, right_hip, right_knee, right_ankle]
    return points

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0, 1)
points = ax.scatter([], [], color='white', s=20)

def update(t):
    pos = get_positions(t)
    x = [p[0] for p in pos]
    y = [p[1] for p in pos]
    points.set_offsets(np.c_[x, y])
    return points,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, 30), interval=1000/30, blit=True)
plt.show()
