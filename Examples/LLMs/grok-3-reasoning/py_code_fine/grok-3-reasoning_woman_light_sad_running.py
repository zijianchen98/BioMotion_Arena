
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define bone lengths
bone_length_torso_neck = 0.1
bone_length_neck_head = 0.1
bone_length_neck_shoulder = 0.15
bone_length_shoulder_elbow = 0.3
bone_length_elbow_wrist = 0.25
bone_length_torso_hip = 0.1
bone_length_torso_hip_y = 0.1
bone_length_hip_knee = 0.4
bone_length_knee_ankle = 0.4

# Define amplitudes and period
T = 1.0  # seconds
A_hip = np.radians(30)
A_knee = np.radians(45)
A_shoulder = np.radians(20)
alpha = np.radians(5)
beta = np.radians(5)
B = 0.05  # vertical oscillation amplitude
y0 = 1.0  # average y-position of torso

# Define angle functions
def theta_left_hip(t):
    return A_hip * np.sin(2 * np.pi * t / T)

def theta_right_hip(t):
    return -A_hip * np.sin(2 * np.pi * t / T)

def theta_left_knee(t):
    return A_knee * (1 + np.sin(2 * np.pi * t / T)) / 2

def theta_right_knee(t):
    return A_knee * (1 - np.sin(2 * np.pi * t / T)) / 2

def theta_left_shoulder(t):
    return -A_shoulder * np.sin(2 * np.pi * t / T)

def theta_right_shoulder(t):
    return A_shoulder * np.sin(2 * np.pi * t / T)

def theta_neck(t):
    return -alpha

def theta_head(t):
    return -beta

def y_torso(t):
    return y0 + B * np.sin(4 * np.pi * t / T)

# Define joints
joints = {
    'torso': {'parent': None, 'offset': (0, 0), 'angle': lambda t: 0},
    'neck': {'parent': 'torso', 'offset': (0, bone_length_torso_neck), 'angle': theta_neck},
    'head': {'parent': 'neck', 'offset': (0, bone_length_neck_head), 'angle': theta_head},
    'left_shoulder': {'parent': 'neck', 'offset': (-bone_length_neck_shoulder, 0), 'angle': theta_left_shoulder},
    'left_elbow': {'parent': 'left_shoulder', 'offset': (0, -bone_length_shoulder_elbow), 'angle': lambda t: 0},
    'left_wrist': {'parent': 'left_elbow', 'offset': (0, -bone_length_elbow_wrist), 'angle': lambda t: 0},
    'right_shoulder': {'parent': 'neck', 'offset': (bone_length_neck_shoulder, 0), 'angle': theta_right_shoulder},
    'right_elbow': {'parent': 'right_shoulder', 'offset': (0, -bone_length_shoulder_elbow), 'angle': lambda t: 0},
    'right_wrist': {'parent': 'right_elbow', 'offset': (0, -bone_length_elbow_wrist), 'angle': lambda t: 0},
    'left_hip': {'parent': 'torso', 'offset': (-bone_length_torso_hip, -bone_length_torso_hip_y), 'angle': theta_left_hip},
    'left_knee': {'parent': 'left_hip', 'offset': (0, -bone_length_hip_knee), 'angle': theta_left_knee},
    'left_ankle': {'parent': 'left_knee', 'offset': (0, -bone_length_knee_ankle), 'angle': lambda t: 0},
    'right_hip': {'parent': 'torso', 'offset': (bone_length_torso_hip, -bone_length_torso_hip_y), 'angle': theta_right_hip},
    'right_knee': {'parent': 'right_hip', 'offset': (0, -bone_length_hip_knee), 'angle': theta_right_knee},
    'right_ankle': {'parent': 'right_knee', 'offset': (0, -bone_length_knee_ankle), 'angle': lambda t: 0},
}

# Define function to get global transformation matrix
def get_transform(joint_name, t):
    joint = joints[joint_name]
    if joint['parent'] is None:
        return np.array([[1, 0, 0], [0, 1, y_torso(t)], [0, 0, 1]])
    else:
        parent_transform = get_transform(joint['parent'], t)
        theta = joint['angle'](t)
        c, s = np.cos(theta), np.sin(theta)
        rot = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
        offset = joint['offset']
        trans = np.array([[1, 0, offset[0]], [0, 1, offset[1]], [0, 0, 1]])
        local_transform = rot @ trans
        return parent_transform @ local_transform

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_axis_off()

# Create scatter plot for points
points = ax.scatter([], [], color='white', s=50)

# Define update function for animation
def update(t):
    positions = []
    for joint_name in joints:
        transform = get_transform(joint_name, t)
        pos = transform[:2, 2]
        positions.append(pos)
    positions = np.array(positions)
    points.set_offsets(positions)
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, T, 100), interval=10, blit=True)

# Show the animation
plt.show()
