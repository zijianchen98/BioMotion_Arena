
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define the skeleton structure for a sad woman bowing
# Each point represents a joint (e.g., head, shoulders, hips, knees, etc.)
# Coordinates are relative to the center of the screen

# Define joints (simplified for a sad woman bowing)
joints = {
    'head': np.array([0.0, 0.8]),
    'neck': np.array([0.0, 0.6]),
    'shoulder_left': np.array([-0.3, 0.4]),
    'elbow_left': np.array([-0.5, 0.2]),
    'wrist_left': np.array([-0.6, 0.0]),
    'hand_left': np.array([-0.7, -0.1]),
    'shoulder_right': np.array([0.3, 0.4]),
    'elbow_right': np.array([0.5, 0.2]),
    'wrist_right': np.array([0.6, 0.0]),
    'hand_right': np.array([0.7, -0.1]),
    'hip_left': np.array([-0.3, -0.4]),
    'knee_left': np.array([-0.5, -0.6]),
    'ankle_left': np.array([-0.6, -0.8]),
    'foot_left': np.array([-0.7, -1.0]),
    'hip_right': np.array([0.3, -0.4]),
    'knee_right': np.array([0.5, -0.6]),
    'ankle_right': np.array([0.6, -0.8]),
    'foot_right': np.array([0.7, -1.0]),
}

# Define a function to simulate the motion of the joints during a bow
def animate_bow(t, joints, amplitude=0.2, frequency=0.5, phase_shift=0):
    for joint in joints:
        if joint in ['head', 'neck']:
            # Head and neck move up and down during bow
            joints[joint][1] = 0.6 + amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
        elif joint in ['hip_left', 'hip_right']:
            # Hips move forward and backward during bow
            joints[joint][0] = 0.0 + amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
        elif joint in ['knee_left', 'knee_right']:
            # Knees bend during bow
            joints[joint][1] = -0.6 + amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
        elif joint in ['ankle_left', 'ankle_right']:
            # Ankles move forward and backward during bow
            joints[joint][0] = 0.0 + amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
        elif joint in ['foot_left', 'foot_right']:
            # Feet stay in place
            pass
        elif joint in ['shoulder_left', 'shoulder_right']:
            # Shoulders move slightly forward during bow
            joints[joint][0] = 0.0 + amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
        elif joint in ['elbow_left', 'elbow_right']:
            # Elbows bend during bow
            joints[joint][1] = 0.2 + amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
        elif joint in ['wrist_left', 'wrist_right']:
            # Wrists move slightly forward during bow
            joints[joint][0] = 0.0 + amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
        elif joint in ['hand_left', 'hand_right']:
            # Hands move slightly forward during bow
            joints[joint][0] = 0.0 + amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
    return joints

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Solid black background
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Create point lights
point_lights = [ax.plot([], [], 'o', color='white', markersize=10)[0] for _ in range(15)]

# Define the order of joints to animate
joint_order = [
    'head', 'neck', 'shoulder_left', 'elbow_left', 'wrist_left', 'hand_left',
    'shoulder_right', 'elbow_right', 'wrist_right', 'hand_right',
    'hip_left', 'knee_left', 'ankle_left', 'foot_left', 'hip_right'
]

# Initialize the point lights
def init():
    for light in point_lights:
        light.set_data([], [])
    return point_lights

# Animation update function
def update(frame):
    animate_bow(frame, joints, amplitude=0.2, frequency=0.5, phase_shift=0)
    for i, joint in enumerate(joint_order):
        x, y = joints[joint]
        point_lights[i].set_data(x, y)
    return point_lights

# Create animation
ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

plt.show()
