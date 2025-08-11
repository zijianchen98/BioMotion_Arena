
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define the number of point lights
NUM_LIGHTS = 15

# Define the skeleton joints and their positions for a happy man bowing
# Joints are represented as (x, y) positions
# This is a simplified 2D model of a human skeleton for bowing motion

# Define joint indices for the skeleton
JOINTS = {
    'hips': (0, 0),
    'left_knee': (0, -0.5),
    'left_ankle': (0, -1.0),
    'right_knee': (0, -0.5),
    'right_ankle': (0, -1.0),
    'torso': (0, 0.5),
    'left_shoulder': (-0.3, 0.5),
    'left_elbow': (-0.3, 0.2),
    'left_wrist': (-0.3, 0.0),
    'right_shoulder': (0.3, 0.5),
    'right_elbow': (0.3, 0.2),
    'right_wrist': (0.3, 0.0),
    'head': (0, 1.0)
}

# Define the point lights as a list of joint indices
LIGHT_JOINTS = [
    'hips', 'left_knee', 'left_ankle', 'right_knee', 'right_ankle',
    'torso', 'left_shoulder', 'left_elbow', 'left_wrist', 'right_shoulder',
    'right_elbow', 'right_wrist', 'head', 'head', 'head'
]

# Scale factor for visualization
SCALE = 100

# Function to generate a bowing motion
def bowing_motion(t, total_time=10):
    # Time normalized between 0 and 1
    t_norm = t / total_time
    # Bowing motion: head lowers and arms move forward
    head_y = 1.0 - 0.5 * (1 - np.cos(2 * np.pi * t_norm))
    left_shoulder_y = 0.5 - 0.2 * (1 - np.cos(2 * np.pi * t_norm))
    left_elbow_y = 0.2 - 0.1 * (1 - np.cos(2 * np.pi * t_norm))
    left_wrist_y = 0.0 - 0.05 * (1 - np.cos(2 * np.pi * t_norm))
    right_shoulder_y = 0.5 - 0.2 * (1 - np.cos(2 * np.pi * t_norm))
    right_elbow_y = 0.2 - 0.1 * (1 - np.cos(2 * np.pi * t_norm))
    right_wrist_y = 0.0 - 0.05 * (1 - np.cos(2 * np.pi * t_norm))
    torso_y = 0.5 - 0.2 * (1 - np.cos(2 * np.pi * t_norm))
    left_knee_y = -0.5 + 0.1 * (1 - np.cos(2 * np.pi * t_norm))
    right_knee_y = -0.5 + 0.1 * (1 - np.cos(2 * np.pi * t_norm))
    left_ankle_y = -1.0 + 0.1 * (1 - np.cos(2 * np.pi * t_norm))
    right_ankle_y = -1.0 + 0.1 * (1 - np.cos(2 * np.pi * t_norm))
    return {
        'hips': (0, left_ankle_y),
        'left_knee': (0, left_knee_y),
        'left_ankle': (0, left_ankle_y),
        'right_knee': (0, right_knee_y),
        'right_ankle': (0, right_ankle_y),
        'torso': (0, torso_y),
        'left_shoulder': (-0.3, left_shoulder_y),
        'left_elbow': (-0.3, left_elbow_y),
        'left_wrist': (-0.3, left_wrist_y),
        'right_shoulder': (0.3, right_shoulder_y),
        'right_elbow': (0.3, right_elbow_y),
        'right_wrist': (0.3, right_wrist_y),
        'head': (0, head_y)
    }

# Convert joint positions to screen coordinates
def get_positions(motion):
    positions = []
    for joint in LIGHT_JOINTS:
        x, y = motion[joint]
        positions.append((x * SCALE, y * SCALE))
    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-150, 150)
ax.set_ylim(-200, 200)
ax.set_aspect('equal')
ax.axis('off')

# Create the point lights
lights = [ax.plot([], [], 'o', color='white', markersize=8)[0] for _ in range(NUM_LIGHTS)]

# Animation update function
def update(frame):
    motion = bowing_motion(frame)
    positions = get_positions(motion)
    for i, light in enumerate(lights):
        light.set_data(positions[i][0], positions[i][1])
    return lights

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
