
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
L_thigh = 0.4
L_shin = 0.4
L_upper_arm = 0.3
L_forearm = 0.3
T = 2.0  # total time for one cycle
dt = 0.05  # time step for animation
times = np.arange(0, T, dt)

# Define y_hips(t)
def y_hips(t):
    if t < 0.2:
        return 0.9 - (0.2 / 0.2) * t  # linear decrease from 0.9 to 0.7
    elif t < 0.4:
        return 0.7 + (0.2 / 0.2) * (t - 0.2)  # linear increase from 0.7 to 0.9
    elif t < 1.4:
        t_air = t - 0.4
        return 0.9 + 1.2 * t_air - 0.5 * 2.4 * t_air**2
    else:
        return 0.9  # after landing

# Define angles
def theta_thigh(t):
    if t < 0.2:
        return 30 * (t / 0.2)  # from 0 to 30 degrees
    elif t < 0.4:
        return 30 - 30 * ((t - 0.2) / 0.2)  # from 30 to 0 degrees
    else:
        return 0  # straight during airborne and after

def theta_knee(t):
    if t < 0.2:
        return -60 * (t / 0.2)  # from 0 to -60 degrees
    elif t < 0.4:
        return -60 + 60 * ((t - 0.2) / 0.2)  # from -60 to 0 degrees
    else:
        return 0

def theta_upper_arm(t):
    if t < 0.2:
        return 45 * (t / 0.2)  # from 0 to 45 degrees (back)
    elif t < 0.4:
        return 45 - 90 * ((t - 0.2) / 0.2)  # from 45 to -45 degrees (forward)
    else:
        return -45  # stay forward during airborne

# Set up figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')

# Create points
points = [ax.plot([], [], 'o', color='white')[0] for _ in range(15)]

# Point indices
HEAD = 0
LEFT_SHOULDER = 1
RIGHT_SHOULDER = 2
LEFT_ELBOW = 3
RIGHT_ELBOW = 4
LEFT_WRIST = 5
RIGHT_WRIST = 6
LEFT_HIP = 7
RIGHT_HIP = 8
LEFT_KNEE = 9
RIGHT_KNEE = 10
LEFT_ANKLE = 11
RIGHT_ANKLE = 12
LEFT_FOOT = 13
RIGHT_FOOT = 14

# Update function
def update(t):
    y_hips_t = y_hips(t)
    theta_thigh_t = theta_thigh(t)
    theta_knee_t = theta_knee(t)
    theta_upper_arm_t = theta_upper_arm(t)
    theta_elbow_t = 0  # straight arms for simplicity

    # Upper body
    pos_head = (0, y_hips_t + 0.9)
    pos_left_shoulder = (-0.2, y_hips_t + 0.6)
    pos_right_shoulder = (0.2, y_hips_t + 0.6)

    # Arms
    pos_left_elbow = (pos_left_shoulder[0] + L_upper_arm * np.sin(np.radians(theta_upper_arm_t)),
                      pos_left_shoulder[1] - L_upper_arm * np.cos(np.radians(theta_upper_arm_t)))
    pos_left_wrist = (pos_left_elbow[0] + L_forearm * np.sin(np.radians(theta_upper_arm_t + theta_elbow_t)),
                      pos_left_elbow[1] - L_forearm * np.cos(np.radians(theta_upper_arm_t + theta_elbow_t)))
    pos_right_elbow = (pos_right_shoulder[0] + L_upper_arm * np.sin(np.radians(theta_upper_arm_t)),
                       pos_right_shoulder[1] - L_upper_arm * np.cos(np.radians(theta_upper_arm_t)))
    pos_right_wrist = (pos_right_elbow[0] + L_forearm * np.sin(np.radians(theta_upper_arm_t + theta_elbow_t)),
                       pos_right_elbow[1] - L_forearm * np.cos(np.radians(theta_upper_arm_t + theta_elbow_t)))

    # Legs
    pos_left_hip = (-0.1, y_hips_t)
    pos_right_hip = (0.1, y_hips_t)
    pos_left_knee = (pos_left_hip[0] + L_thigh * np.sin(np.radians(theta_thigh_t)),
                     pos_left_hip[1] - L_thigh * np.cos(np.radians(theta_thigh_t)))
    pos_right_knee = (pos_right_hip[0] + L_thigh * np.sin(np.radians(theta_thigh_t)),
                      pos_right_hip[1] - L_thigh * np.cos(np.radians(theta_thigh_t)))
    pos_left_ankle = (pos_left_knee[0] + L_shin * np.sin(np.radians(theta_thigh_t + theta_knee_t)),
                      pos_left_knee[1] - L_shin * np.cos(np.radians(theta_thigh_t + theta_knee_t)))
    pos_right_ankle = (pos_right_knee[0] + L_shin * np.sin(np.radians(theta_thigh_t + theta_knee_t)),
                       pos_right_knee[1] - L_shin * np.cos(np.radians(theta_thigh_t + theta_knee_t)))

    # Feet
    if t < 0.4 or t > 1.4:
        pos_left_foot = (-0.05, 0)
        pos_right_foot = (0.05, 0)
    else:
        pos_left_foot = (pos_left_ankle[0], pos_left_ankle[1] - 0.05)
        pos_right_foot = (pos_right_ankle[0], pos_right_ankle[1] - 0.05)

    # Set data
    points[HEAD].set_data([pos_head[0]], [pos_head[1]])
    points[LEFT_SHOULDER].set_data([pos_left_shoulder[0]], [pos_left_shoulder[1]])
    points[RIGHT_SHOULDER].set_data([pos_right_shoulder[0]], [pos_right_shoulder[1]])
    points[LEFT_ELBOW].set_data([pos_left_elbow[0]], [pos_left_elbow[1]])
    points[RIGHT_ELBOW].set_data([pos_right_elbow[0]], [pos_right_elbow[1]])
    points[LEFT_WRIST].set_data([pos_left_wrist[0]], [pos_left_wrist[1]])
    points[RIGHT_WRIST].set_data([pos_right_wrist[0]], [pos_right_wrist[1]])
    points[LEFT_HIP].set_data([pos_left_hip[0]], [pos_left_hip[1]])
    points[RIGHT_HIP].set_data([pos_right_hip[0]], [pos_right_hip[1]])
    points[LEFT_KNEE].set_data([pos_left_knee[0]], [pos_left_knee[1]])
    points[RIGHT_KNEE].set_data([pos_right_knee[0]], [pos_right_knee[1]])
    points[LEFT_ANKLE].set_data([pos_left_ankle[0]], [pos_left_ankle[1]])
    points[RIGHT_ANKLE].set_data([pos_right_ankle[0]], [pos_right_ankle[1]])
    points[LEFT_FOOT].set_data([pos_left_foot[0]], [pos_left_foot[1]])
    points[RIGHT_FOOT].set_data([pos_right_foot[0]], [pos_right_foot[1]])

    return points

# Create animation
ani = FuncAnimation(fig, update, frames=times, interval=dt*1000, blit=True)

plt.show()
