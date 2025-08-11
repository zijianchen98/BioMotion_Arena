
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define the number of joints (15 points)
num_joints = 15

# Define the time steps for the animation
num_frames = 100

# Define the joint positions over time (example data for a forward rolling motion)
# This is a simplified and illustrative example. In a real application, this data would
# be derived from motion capture or a biomechanical model of a happy woman with heavy weight rolling forward.

# Joint indices:
# 0 - head
# 1 - left shoulder
# 2 - right shoulder
# 3 - left elbow
# 4 - right elbow
# 5 - left hand
# 6 - right hand
# 7 - torso center
# 8 - left hip
# 9 - right hip
# 10 - left knee
# 11 - right knee
# 12 - left foot
# 13 - right foot
# 14 - center of gravity

# We'll create a rolling motion by rotating the body forward

def create_forward_rolling_motion(num_frames):
    motion = np.zeros((num_frames, num_joints, 2))  # [frame, joint, (x,y)]

    # Define base positions for each joint
    base_positions = np.array([
        [0, 1.7],  # head
        [-0.3, 1.5],  # left shoulder
        [0.3, 1.5],  # right shoulder
        [-0.6, 1.2],  # left elbow
        [0.6, 1.2],  # right elbow
        [-1.0, 1.0],  # left hand
        [1.0, 1.0],  # right hand
        [0, 1.2],  # torso center
        [-0.4, 0.8],  # left hip
        [0.4, 0.8],  # right hip
        [-0.8, 0.3],  # left knee
        [0.8, 0.3],  # right knee
        [-1.2, -0.2],  # left foot
        [1.2, -0.2],  # right foot
        [0, 0.9],  # center of gravity
    ])

    for frame in range(num_frames):
        t = frame / num_frames  # normalize time

        # Create a forward rolling motion by rotating the body around a center point
        # and shifting forward
        angle = np.pi / 2 * np.sin(np.pi * t)  # increase rotation angle over time
        shift = t  # shift forward over time

        # Rotate and shift each joint
        for i in range(num_joints):
            x, y = base_positions[i]
            # Rotate around the center of gravity
            dx = x - base_positions[14, 0]
            dy = y - base_positions[14, 1]
            new_x = dx * np.cos(angle) - dy * np.sin(angle)
            new_y = dx * np.sin(angle) + dy * np.cos(angle)
            motion[frame, i, 0] = new_x + base_positions[14, 0] + shift
            motion[frame, i, 1] = new_y

    return motion

# Generate the motion data
motion_data = create_forward_rolling_motion(num_frames)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 3)
ax.set_ylim(-1, 2)
ax.axis('off')

# Create the point lights
points = [ax.plot([], [], 'o', color='white', markersize=8)[0] for _ in range(num_joints)]

# Animation update function
def update(frame):
    for i in range(num_joints):
        points[i].set_data(motion_data[frame, i, 0], motion_data[frame, i, 1])
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
