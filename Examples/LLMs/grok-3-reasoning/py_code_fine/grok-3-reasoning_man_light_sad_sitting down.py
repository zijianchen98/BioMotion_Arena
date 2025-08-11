
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Constants
L_thigh = 0.4
L_calf = 0.4
L_torso = 0.5
L_ne \_upper_arm = 0.3
L_lower_arm = 0.3
N = 100  # Number of frames

def get_points(t):
    y_w = L_calf + (1 - t) * L_thigh
    x_w = 0
    theta_torso = t * np.deg2rad(30)
    theta_left_thigh = np.pi + t * (np.pi / 2)
    theta_right_thigh = np.pi - t * (np.pi / 2)
    theta_left_calf = np.pi
    theta_right_calf = np.pi
    theta_left_upper_arm = np.pi
    theta_left_lower_arm = np.pi
    theta_right_upper_arm = np.pi
    theta_right_lower_arm = np.pi
    theta_head = theta_torso + np.deg2rad(20)

    # Positions
    waist = [x_w, y_w]
    neck = [waist[0] + L_torso * np.sin(theta_torso), waist[1] + L_torso * np.cos(theta_torso)]
    head = [neck[0] + L_neck * np.sin(theta_head), neck[1] + L_neck * np.cos(theta_head)]
    left_shoulder = neck  # Simplified
    right_shoulder = neck  # Simplified
    left_elbow = [left_shoulder[0] + L_upper_arm * np.sin(theta_left_upper_arm), left_shoulder[1] + L_upper_arm * np.cos(theta_left_upper_arm)]
    right_elbow = [right_shoulder[0] + L_upper_arm * np.sin(theta_right_upper_arm), right_shoulder[1] + L_upper_arm * np.cos(theta_right_upper_arm)]
    left_wrist = [left_elbow[0] + L_lower_arm * np.sin(theta_left_lower_arm), left_elbow[1] + L_lower_arm * np.cos(theta_left_lower_arm)]
    right_wrist = [right_elbow[0] + L_lower_arm * np.sin(theta_right_lower_arm), right_elbow[1] + L_lower_arm * np.cos(theta_right_lower_arm)]
    left_hip = waist
    right_hip = waist
    left_knee = [left_hip[0] + L_thigh * np.sin(theta_left_thigh), left_hip[1] + L_thigh * np.cos(theta_left_thigh)]
    right_knee = [right_hip[0] + L_thigh * np.sin(theta_right_thigh), right_hip[1] + L_thigh * np.cos(theta_right_thigh)]
    left_ankle = [left_knee[0] + L_calf * np.sin(theta_left_calf), left_knee[1] + L_calf * np.cos(theta_left_calf)]
    right_ankle = [right_knee[0] + L_calf * np.sin(theta_right_calf), right_knee[1] + L_calf * np.cos(theta_right_calf)]

    points = np.array([head, neck, left_shoulder, right_shoulder, left_elbow, right_elbow, left_wrist, right_wrist, waist, left_hip, right_hip, left_knee, right_knee, left_ankle, right_ankle])
    return points

fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

points_plot = ax.scatter([], [], color='white', s=20)

def update(frame):
    t = frame / (N - 1)
    data = get_points(t)
    points_plot.set_offsets(data)
    return points_plot,

ani = animation.FuncAnimation(fig, update, frames=N, interval=50, blit=True)
plt.show()
