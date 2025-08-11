
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_frames = 60
num_points = 15
jump_height = 0.5
jump_distance = 1.0
frame_rate = 30

# Base positions of point lights for a "sad man"
def base_positions():
    return np.array([
        [0, 0],        # head
        [-0.1, -0.2],  # left shoulder
        [0.1, -0.2],   # right shoulder
        [-0.2, -0.4],  # left elbow
        [0.2, -0.4],   # right elbow
        [-0.15, -0.5], # left hand
        [0.15, -0.5],  # right hand
        [-0.1, -0.6],  # left hip
        [0.1, -0.6],   # right hip
        [-0.1, -0.8],  # left knee
        [0.1, -0.8],   # right knee
        [-0.1, -1.0],  # left foot
        [0.1, -1.0],   # right foot
        [0, -0.4],     # torso
        [-0.05, -0.5], # left knee
        [0.05, -0.5],  # right knee
    ])

# Update positions for jumping action
def update_positions(frame):
    # Jump trajectory
    t = frame / num_frames  # normalized time
    y_offset = jump_height * np.sin(np.pi * t)  # smooth jump motion
    x_offset = jump_distance * t  # forward motion

    points.set_data(base_positions()[:, 0] + x_offset, base_positions()[:, 1] + y_offset)
    return points,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 1)
ax.set_facecolor('black')
ax.axis('off')

# Initialize point lights
base_pos = base_positions()
points, = ax.plot(base_pos[:, 0], base_pos[:, 1], 'o', color='white')

# Create animation
ani = animation.FuncAnimation(fig, update_positions, frames=num_frames, interval=1000/frame_rate, blit=True)

# Show the animation
plt.show()
