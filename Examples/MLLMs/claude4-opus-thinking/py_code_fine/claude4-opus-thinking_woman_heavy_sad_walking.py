
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to create motion data for a walking animation
def walking_motion(frame_index):
    # Basic parameters for the points
    height = 1.6  # Approximate height of the figure
    weight_shift = 0.1 * np.sin(frame_index / 10.0)  # Simulated weight shift
    offset = 0.1 * np.cos(frame_index / 10.0)  # Side to side sway

    # Joint coordinates (15 points)
    joints = np.array([
        [0, height],  # head
        [-0.2, height-0.2],  # left shoulder
        [0.2, height-0.2],  # right shoulder
        [-0.2, height-0.6],  # left elbow
        [0.2, height-0.6],  # right elbow
        [-0.2, height-0.9],  # left wrist
        [0.2, height-0.9],  # right wrist
        [-0.2, height-1.2],  # left hip
        [0.2, height-1.2],  # right hip
        [-0.2, height-1.5],  # left knee
        [0.2, height-1.5],  # right knee
        [-0.2 + offset, height-1.8 + weight_shift],  # left ankle
        [0.2 + offset, height-1.8 + weight_shift],  # right ankle
        [-0.2 + offset, height-2.1 + weight_shift],  # left foot
        [0.2 + offset, height-2.1 + weight_shift],  # right foot
        [0, height-3.0]  # point representing weight
    ])

    return joints

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-3.5, 1)
ax.set_facecolor('black')  # Solid black background
points, = ax.plot([], [], 'o', color='white')  # 15 point-lights

# Initialize the animation
def init():
    points.set_data([], [])
    return points,

# Animation update function
def update(frame):
    joints = walking_motion(frame)
    points.set_data(joints[:, 0], joints[:, 1])
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200, 1), 
                    init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
