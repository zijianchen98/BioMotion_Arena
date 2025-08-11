
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
l_thigh = 0.45
l_shin = 0.45
l_upper_arm = 0.27
l_forearm = 0.27
l_torso = 0.54
l_neck = 0.1
v_x = 1.0
y0 = 1.0
g = 4.444
v_y = 1.333
t_takeoff = 0.2
t_land = 0.8
T = 1.0

def theta_thigh(t):
    if 0 <= t <= t_takeoff:
        return 45 - 45*(t / t_takeoff)
    elif t_takeoff < t < t_land:
        return 0
    elif t_land <= t <= T:
        return 0 + 45*((t - t_land)/(T - t_land))
    else:
        return 45

def theta_knee(t):
    if 0 <= t <= t_takeoff:
        return 60 - 60*(t / t_takeoff)
    elif t_takeoff < t < t_land:
        return 0
    elif t_land <= t <= T:
        return 0 + 60*((t - t_land)/(T - t_land))
    else:
        return 60

def theta_upper_arm(t):
    if 0 <= t <= t_takeoff:
        return -60 + 120*(t / t_takeoff)
    elif t_takeoff < t < t_land:
        return 60
    elif t_land <= t <= T:
        return 60 - 120*((t - t_land)/(T - t_land))
    else:
        return -60

def theta_elbow(t):
    if 0 <= t <= t_takeoff:
        return 90 - 90*(t / t_takeoff)
    elif t_takeoff < t < t_land:
        return 0
    elif t_land <= t <= T:
        return 0 + 90*((t - t_land)/(T - t_land))
    else:
        return 90

def get_positions(t):
    if 0 <= t <= t_takeoff:
        y_root = 0.8 + (y0 - 0.8)*(t / t_takeoff)
    elif t_takeoff < t < t_land:
        dt = t - t_takeoff
        y_root = y0 + v_y * dt - 0.5 * g * dt**2
    elif t_land <= t <= T:
        y_root = y0 - (y0 - 0.8)*((t - t_land)/(T - t_land))
    else:
        y_root = 0.8
    x_root = v_x * t

    theta_t = theta_thigh(t)
    theta_k = theta_knee(t)
    theta_ua = theta_upper_arm(t)
    theta_e = theta_elbow(t)

    root_position = (x_root, y_root)
    left_hip = (x_root - 0.05, y_root)
    right_hip = (x_root + 0.05, y_root)
    left_knee = (left_hip[0] + l_thigh * np.sin(np.radians(theta_t)), left_hip[1] - l_thigh * np.cos(np.radians(theta_t)))
    right_knee = (right_hip[0] + l_thigh * np.sin(np.radians(theta_t)), right_hip[1] - l_thigh * np.cos(np.radians(theta_t)))
    left_ankle = (left_knee[0] + l_shin * np.sin(np.radians(theta_t + theta_k)), left_knee[1] - l_shin * np.cos(np.radians(theta_t + theta_k)))
    right_ankle = (right_knee[0] + l_shin * np.sin(np.radians(theta_t + theta_k)), right_knee[1] - l_shin * np.cos(np.radians(theta_t + theta_k)))
    if 0 <= t <= t_takeoff or t_land <= t <= T:
        left_foot = (left_ankle[0], 0)
        right_foot = (right_ankle[0], 0)
    else:
        left_foot = (left_ankle[0], left_ankle[1] - 0.1)
        right_foot = (right_ankle[0], right_ankle[1] - 0.1)
    shoulders = (x_root, y_root + l_torso)
    head = (x_root, shoulders[1] + l_neck)
    left_shoulder = (x_root - 0.1, shoulders[1])
    right_shoulder = (x_root + 0.1, shoulders[1])
    left_elbow = (left_shoulder[0] - l_upper_arm * np.sin(np.radians(theta_ua)), left_shoulder[1] - l_upper_arm * np.cos(np.radians(theta_ua)))
    right_elbow = (right_shoulder[0] + l_upper_arm * np.sin(np.radians(theta_ua)), right_shoulder[1] - l_upper_arm * np.cos(np.radians(theta_ua)))
    left_wrist = (left_elbow[0] - l_forearm * np.sin(np.radians(theta_ua + theta_e)), left_elbow[1] - l_forearm * np.cos(np.radians(theta_ua + theta_e)))
    right_wrist = (right_elbow[0] + l_forearm * np.sin(np.radians(theta_ua + theta_e)), right_elbow[1] - l_forearm * np.cos(np.radians(theta_ua + theta_e)))
    points = [
        head,
        left_shoulder,
        right_shoulder,
        left_elbow,
        right_elbow,
        left_wrist,
        right_wrist,
        left_hip,
        right_hip,
        left_knee,
        right_knee,
        left_ankle,
        right_ankle,
        left_foot,
        right_foot
    ]
    return points

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 2)
ax.set_ylim(-0.1, 2.5)
points_plot = ax.scatter([], [], color='white', s=50)

def init():
    points_plot.set_offsets([])
    return points_plot,

def update(frame):
    t = frame / fps * T
    points = get_positions(t)
    points_array = np.array(points)
    points_plot.set_offsets(points_array)
    return points_plot,

fps = 30
frames = int(fps * T)
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)

plt.show()
