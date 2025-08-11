
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Define joint positions for a running motion
# We'll use 15 joints: head, shoulders, elbows, wrists, hips, knees, ankles
# The joint positions are relative to a central reference point (torso)
# These are simplified and normalized for animation

# Time parameters
num_frames = 100
duration = 5.0  # seconds
fps = num_frames / duration

# Joint names for reference
joint_names = [
    'head', 'left_shoulder', 'right_shoulder',
    'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
    'left_hip', 'right_hip', 'left_knee', 'right_knee',
    'left_ankle', 'right_ankle'
]

# Function to generate a running motion for each joint
def generate_running_motion(num_frames, amplitude, frequency, phase):
    return amplitude * np.sin(2 * np.pi * frequency * np.linspace(0, duration, num_frames) + phase)

# Initial joint positions and motion parameters
joint_params = {
    'head': (0.0, 0.0, 0.0, 0.0),           # (x_offset, y_offset, amplitude, frequency)
    'left_shoulder': (-0.5, 0.5, 0.3, 2.0, 0.0),
    'right_shoulder': (0.5, 0.5, 0.3, 2.0, np.pi),
    'left_elbow': (-1.0, 0.3, 0.2, 2.0, 0.0),
    'right_elbow': (1.0, 0.3, 0.2, 2.0, np.pi),
    'left_wrist': (-1.5, 0.1, 0.1, 2.0, 0.0),
    'right_wrist': (1.5, 0.1, 0.1, 2.0, np.pi),
    'left_hip': (-0.5, -0.5, 0.3, 1.0, 0.0),
    'right_hip': (0.5, -0.5, 0.3, 1.0, np.pi),
    'left_knee': (-1.0, -1.0, 0.4, 1.5, 0.0),
    'right_knee': (1.0, -1.0, 0.4, 1.5, np.pi),
    'left_ankle': (-1.5, -1.5, 0.3, 1.0, 0.0),
    'right_ankle': (1.5, -1.5, 0.3, 1.0, np.pi),
}

# Generate motion for each joint
positions = {}
for joint in joint_names:
    x_offset, y_offset, amplitude, frequency, phase = joint_params[joint]
    t = np.linspace(0, duration, num_frames)
    x = x_offset + amplitude * np.sin(2 * np.pi * frequency * t + phase)
    y = y_offset + amplitude * np.cos(2 * np.pi * frequency * t + phase)
    positions[joint] = np.column_stack((x, y))

# Setup the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.axis('off')

# Create scatter points for each joint
points = [ax.plot([], [], 'o', color='white', markersize=8)[0] for _ in range(len(joint_names))]

# Function to update the animation
def update(frame):
    for i, joint in enumerate(joint_names):
        x, y = positions[joint][frame]
        points[i].set_data(x, y)
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000 / fps, blit=True)

# To save the animation as a video file, uncomment the following line:
# ani.save('happy_woman_running.mp4', writer='ffmpeg', fps=fps)

plt.show()
