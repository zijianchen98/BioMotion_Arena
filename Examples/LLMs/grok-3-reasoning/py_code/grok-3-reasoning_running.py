
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
T = 1.0
num_frames = 100
root_y0 = 0.5
a = 0.1
hip_width = 0.4
shoulder_width = 0.6
torso_height = 1.0
upper_arm_length = 0.4
lower_arm_length = 0.4
upper_leg_length = 0.5
lower_leg_length = 0.5
foot_length = 0.2
head_height = 0.3
theta_leg_amplitude = np.pi / 6
theta_arm_amplitude = np.pi / 6
theta_knee_amplitude = np.pi / 4
theta_elbow_amplitude = np.pi / 4
phi_knee = np.pi / 2
phi_elbow = np.pi / 2

# Functions 15 points: head, left_shoulder, right_shoulder, left_elbow, right_elbow, left_wrist, right_wrist, left_hip, right_hip, left_knee, right_knee, left_ankle, right_ankle, left_toe, right_toe

# Define angle functions
def theta_left_upper_leg(t):
    return theta_leg_amplitude * np.sin(2 * np.pi * t / T)

def theta_right_upper_leg(t):
    return theta_leg_amplitude * np.sin(2 * np.pi * t / T + np.pi)

def theta_left_lower_leg(t):
    return theta_knee_amplitude * (1 + np.sin(2 * np.pi * t / T + phi_knee))

def theta_right_lower_leg(t):
    return theta_knee_amplitude * (1 + np.sin(2 * np.pi * t / T + np.pi + phi_knee))

def theta_left_upper_arm(t):
    return theta_arm_amplitude * np.sin(2 * np.pi * t / T + np.pi)

def theta_right_upper_arm(t):
    return theta_arm_amplitude * np.sin(2 * np.pi * t / T)

def theta_left_lower_arm(t):
    return theta_elbow_amplitude * (1 + np.sin(2 * np.pi * t / T + phi_elbow))

def theta_right_lower_arm(t):
    return theta_elbow_amplitude * (1 + np.sin(2 * np.pi * t / T + np.pi + phi_elbow))

def root_y(t):
    return root_y0 + a * np.sin(4 * np.pi * t / T)

def get_positions(t):
    root = (0, root_y(t))
    left_hip = (root[0] - hip_width / 2, root[1])
    right_hip = (root[0] + hip_width / 2, root[1])
    
    theta_ul = theta_left_upper_leg(t)
    left_knee = (left_hip[0] + upper_leg_length * np.sin(theta_ul),
                 left_hip[1] - upper_leg_length * np.cos(theta_ul))
    theta_ll = theta_left_lower_leg(t)
    left_ankle = (left_knee[0] + lower_leg_length * np.sin(theta_ul + theta_ll),
                  left_knee[1] - lower_leg_length * np.cos(theta_ul + theta_ll))
    left_toe = (left_ankle[0] + foot_length, left_ankle[1])
    
    theta_ur = theta_right_upper_leg(t)
    right_knee = (right_hip[0] + upper_leg_length * np.sin(theta_ur),
                  right_hip[1] - upper_leg_length * np.cos(theta_ur))
    theta_lr = theta_right_lower_leg(t)
    right_ankle = (right_knee[0] + lower_leg_length * np.sin(theta_ur + theta_lr),
                   right_knee[1] - lower_leg_length * np.cos(theta_ur + theta_lr))
    right_toe = (right_ankle[0] + foot_length, right_ankle[1])
    
    neck = (root[0], root[1] + torso_height)
    left_shoulder = (neck[0] - shoulder_width / 2, neck[1])
    right_shoulder = (neck[0] + shoulder_width / 2, neck[1])
    
    theta_ua = theta_left_upper_arm(t)
    left_elbow = (left_shoulder[0] + upper_arm_length * np.sin(theta_ua),
                  left_shoulder[1] - upper_arm_length * np.cos(theta_ua))
    theta_la = theta_left_lower_arm(t)
    left_wrist = (left_elbow[0] + lower_arm_length * np.sin(theta_ua + theta_la),
                  left_elbow[1] - lower_arm_length * np.cos(theta_ua + theta_la))
    
    theta_ua_r = theta_right_upper_arm(t)
    right_elbow = (right_shoulder[0] + upper_arm_length * np.sin(theta_ua_r),
                   right_shoulder[1] - upper_arm_length * np.cos(theta_ua_r))
    theta_la_r = theta_right_lower_arm(t)
    right_wrist = (right_elbow[0] + lower_arm_length * np.sin(theta_ua_r + theta_la_r),
                   right_elbow[1] - lower_arm_length * np.cos(theta_ua_r + theta_la_r))
    
    head = (neck[0], neck[1] + head_height)
    
    points = [
        head, left_shoulder, right_shoulder, left_elbow, right_elbow,
        left_wrist, right_wrist, left_hip, right_hip, left_knee,
        right_knee, left_ankle, right_ankle, left_toe, right_toe
    ]
    return points

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 2.5)
scatter = ax.scatter([], [], color='white', s=50)

def update(frame):
    t = (frame % num_frames) * T / num_frames
    points = get_positions(t)
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    scatter.set_offsets(np.c_[x, y])
    return scatter,

ani = FuncAnimation(fig, update, frames=range(num_frames), interval=50, blit=True)
plt.show()
