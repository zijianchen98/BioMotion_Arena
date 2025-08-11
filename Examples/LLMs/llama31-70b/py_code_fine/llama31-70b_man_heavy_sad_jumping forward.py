
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# Each point represents a joint in the body (e.g. head, shoulders, elbows, etc.)
initial_positions = np.array([
    [0, 0],  # head
    [-0.2, 0.5],  # left shoulder
    [0.2, 0.5],  # right shoulder
    [-0.3, 0.8],  # left elbow
    [0.3, 0.8],  # right elbow
    [-0.2, 1.1],  # left hand
    [0.2, 1.1],  # right hand
    [0, 0.3],  # torso
    [-0.2, -0.2],  # left hip
    [0.2, -0.2],  # right hip
    [-0.3, -0.5],  # left knee
    [0.3, -0.5],  # right knee
    [-0.2, -0.8],  # left ankle
    [0.2, -0.8],  # right ankle
    [0, -1.0]  # feet
])

# Define the motion parameters
num_frames = 100
jump_height = 0.5
stride_length = 0.5
weight = 0.2  # represents the 'heaviness' of the weight

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Calculate the positions of the point-lights at the current frame
    positions = initial_positions.copy()
    t = frame / num_frames

    # Simulate the jumping motion
    jump_progress = np.sin(2 * np.pi * t)
    positions[:, 1] += jump_progress * jump_height

    # Simulate the forward motion
    stride_progress = np.sin(np.pi * t)
    positions[:, 0] += stride_progress * stride_length

    # Simulate the weight's effect on the motion
    weight_progress = np.cos(np.pi * t)
    positions[:, 1] -= weight_progress * weight

    # Plot the point-lights
    ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, repeat=True)

plt.show()
