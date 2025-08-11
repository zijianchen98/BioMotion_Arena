
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the skeleton structure
# Each joint has a parent and a length from the parent
skeleton = {
    'waist': {'parent': None, 'length': 0},
    'neck': {'parent': 'waist', 'length': 0.2},
    'head': {'parent': 'neck', 'length': 0.1},
    'left_shoulder': {'parent': 'neck', 'length': 0.15},
    'left_elbow': {'parent': 'left_shoulder', 'length': 0.2},
    'left_wrist': {'parent': 'left_elbow', 'length': 0.2},
    'right_shoulder': {'parent': 'neck', 'length': 0.15},
    'right_elbow': {'parent': 'right_shoulder', 'length': 0.2},
    'right_wrist': {'parent': 'right_elbow', 'length': 0.2},
    'left_hip': {'parent': 'waist', 'length': 0.1},
    'left_knee': {'parent': 'left_hip', 'length': 0.3},
    'left_ankle': {'parent': 'left_knee', 'length': 0.3},
    'right_hip': {'parent': 'waist', 'length': 0.1},
    'right_knee': {'parent': 'right_hip', 'length': 0.3},
    'right_ankle': {'parent': 'right_knee', 'length': 0.3},
}

# Define the order of joints for plotting
joints = [
    'head', 'neck', 'left_shoulder', 'left_elbow', 'left_wrist',
    'right_shoulder', 'right_elbow', 'right_wrist', 'waist',
    'left_hip', 'left_knee', 'left_ankle', 'right_hip', 'right_knee', 'right_ankle'
]

# Define the running motion parameters
stride_period = 1.0  # seconds per stride
vertical_bob_amplitude = 0.05  # amplitude of vertical bobbing
hip_swing_amplitude = np.pi / 6  # 30 degrees
knee_bend_amplitude = np.pi / 3  # 60 degrees
arm_swing_amplitude = np.pi / 4  # 45 degrees

# Function to compute joint positions
def compute_positions(t):
    positions = {}
    # Compute waist position with vertical bobbing
    waist_y = vertical_bob_amplitude * np.sin(4 * np.pi * t / stride_period)
    positions['waist'] = np.array([0, waist_y])

    # Define angles for each joint
    angles = {
        'neck': 0,
        'head': 0,
        'left_shoulder': arm_swing_amplitude * np.sin(2 * np.pi * t / stride_period),
        'left_elbow': -knee_bend_amplitude * (1 + np.sin(2 * np.pi * t / stride_period)) / 2,
        'left_wrist': 0,
        'right_shoulder': arm_swing_amplitude * np.sin(2 * np.pi * t / stride_period + np.pi),
        'right_elbow': -knee_bend_amplitude * (1 + np.sin(2 * np.pi * t / stride_period + np.pi)) / 2,
        'right_wrist': 0,
        'left_hip': hip_swing_amplitude * np.sin(2 * np.pi * t / stride_period),
        'left_knee': knee_bend_amplitude * (1 + (np.sin(2 * np.pi * t / stride_period - np.pi / 2))) / 2,
        'left_ankle': 0,
        'right_hip': hip_swing_amplitude * np.sin(2 * np.pi * t / stride_period + np.pi),
        'right_knee': knee_bend_amplitude * (1 + (np.sin(2 * np.pi * t / stride_period + np.pi - np.pi / 2))) / 2,
        'right_ankle': 0,
    }

    # Compute positions recursively
    def get_position(joint):
        Ascending if joint in positions else:
        if joint not in positions:
            parent_pos = get_position(skeleton[joint]['parent']) if skeleton[joint]['parent'] else np.array([0, 0])
            angle = angles[joint]
            offset = skeleton[joint]['length'] * np.array([np.cos(angle), np.sin(angle)])
            positions[joint] = parent_pos + offset
        for joint in skeleton:
            get_position(joint)
        return positions

    positions = compute_positions(0)

    # Set up the figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Create scatter plot for points
    points = ax.scatter([], [], c='white', s=50)

    # Animation update function
    def update(frame):
        t = frame / 30.0  # assuming 30 fps
        positions = compute_positions(t % stride_period)
        x = [positions[joint][0] for joint in joints]
        y = [positions[joint][1] for joint in joints]
        points.set_offsets(np.c_[x, y])
        return points,

    # Create animation
    ani = FuncAnimation(fig, update, frames=np.arange(0, 30), interval=1000/30)

    plt.show()
