
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
t_start = 0
t_end = 2
num_frames = 60
t = np.linspace(t_start, t_end, num_frames)
dt = (t_end - t_start) / num_frames
l_knee = 0.4
l_ankle = 0.4
l_elbow = 0.3
l_wrist = 0.3

# Functions for torso position
def x_torso(t):
    if t < 1.0:
        return 0
    elif t < 1.5:
        return 2 * (t - 1.0)
    else:
        return 1.0

def y_torso(t):
    if t < 0.5:
        return 1.0 - 0.6 * t
    elif t < 1.0:
        return 0.7 + 1.0 * (t - 0.5)
    elif t < 1.5:
        g = 6.4
        v0 = 1.6
        return 1.0 + v0 * (t - 1.0) - 0.5 * g * (t - 1.0)**2
    elif t < 1.75:
        return 1.0 - 0.4 * (t - 1.5)
    else:
        return 0.9 + 0.4 * (t - 1.75)

# Functions for angles (in degrees)
def theta_hip(t):
    if t < 0.5:
        return -30 * (t / 0.5)
    elif t < 1.0:
        return -30 + 60 * ((t - 0.5) / 0.5)
    elif t < 1.5:
        return 30 - 30 * ((t - 1.0) / 0.5)
    else:
        return 0

def theta_knee(t):
    if t < 0.5:
        return 60 * (t / 0.5)
    elif t < 1.0:
        return 60 - 60 * ((t - 0.5) / 0.5)
    elif t < 1.5:
        return 30 * ((t - 1.0) / 0.5)
    else:
        return 30 - 30 * ((t - 1.5) / 0.5)

def theta_shoulder(t):
    if t < 0.5:
        return -90 + 45 * (t / 0.5)
    elif t < 1.0:
        return -45 + 45 * ((t - 0.5) / 0.5)
    elif t < 1.5:
        return 0 - 45 * ((t - 1.0) / 0.5)
    else:
        return -45 - 45 * ((t - 1.5) / 0.5)

# Function to get positions at time t
def get_positions(t):
    x_t = x_torso(t)
    y_t = y_torso(t)
    θ_hip = theta_hip(t)
    θ_knee = theta_knee(t)
    θ_shoulder = theta_shoulder(t)
    θ_hip_rad = np.deg2rad(θ_hip)
    θ_knee_rad = np.deg2rad(θ_knee)
    θ_shoulder_rad = np.deg2rad(θ_shoulder)
    pos = []
    pos.append((x_t, y_t))  # 0: torso center
    pos.append((x_t, y_t + 0.4))  # 1: neck
    pos.append((x_t, y_t + 0.5))  # 2: head
    left_shoulder = (x_t - 0.2, y_t + 0.3)
    pos.append(left_shoulder)  # 3
    right_shoulder = (x_t + 0.2, y_t + 0.3)
    pos.append(right_shoulder)  # 4
    left_elbow = (left_shoulder[0] + l_elbow * np.sin(θ_shoulder_rad), left_shoulder[1] - l_elbow * np.cos(θ_shoulder_rad))
    pos.append(left_elbow)  # 5
    right_elbow = (right_shoulder[0] + l_elbow * np.sin(θ_shoulder_rad), right_shoulder[1] - l_elbow * np.cos(θ_shoulder_rad))
    pos.append(right_elbow)  # 6
    left_wrist = (left_elbow[0] + l_wrist * np.sin(θ_shoulder_rad), left_elbow[1] - l_wrist * np.cos(θ_shoulder_rad))
    pos.append(left_wrist)  # 7
    right_wrist = (right_elbow[0] + l_wrist * np.sin(θ_shoulder_rad), right_elbow[1] - l_wrist * np.cos(θ_shoulder_rad))
    pos.append(right_wrist)  # 8
    left_hip = (x_t - 0.1, y_t - 0.1)
    pos.append(left_hip)  # 9
    right_hip = (x_t + 0.1, y_t - 0.1)
    pos.append(right_hip)  # 10
    left_knee = (left_hip[0] + l_knee * np.sin(θ_hip_rad), left_hip[1] - l_knee * np.cos(θ_hip_rad))
    pos.append(left_knee)  # 11
    right_knee = (right_hip[0] + l_knee * np.sin(θ_hip_rad), right_hip[1] - l_knee * np.cos(θ_hip_rad))
    pos.append(right_knee)  # 12
    left_ankle = (left_knee[0] + l_ankle * np.sin(θ_hip_rad + θ_knee_rad), left_knee[1] - l_ankle * np.cos(θ_hip_rad + θ_knee_rad))
    pos.append(left_ankle)  # 13
    right_ankle = (right_knee[0] + l_ankle * np.sin(θ_hip_rad + θ_knee_rad), right_knee[1] - l_ankle * np.cos(θ_hip_rad + θ_knee_rad))
    pos.append(right_ankle)  # 14
    return pos

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.set_facecolor('black')
ax.set_xlim(-1, 2)
ax.set_ylim(0, 2)
scatter = ax.scatter([], [], color='white', s=50)

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    t = frame * dt
    pos = get_positions(t)
    data = np.array(pos)
    scatter.set_offsets(data)
    return scatter,

ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True)
plt.show()
