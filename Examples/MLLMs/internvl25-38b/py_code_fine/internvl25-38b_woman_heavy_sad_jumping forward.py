
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames
num_frames = 100

# Initialize positions for 15 point-lights (x, y) around the body
def initialize_positions():
    positions = np.zeros((num_frames, 15, 2))
    base_positions = np.array([
        [0, 0],    # torso
        [0.1, 0.2],  # right shoulder
        [0.1, -0.2], # right hip
        [-0.1, 0.2], # left shoulder
        [-0.1, -0.2],# left hip
        [0.2, 0.1],  # right elbow
        [0.2, -0.1], # right knee
        [-0.2, 0.1], # left elbow
        [-0.2, -0.1],# left knee
        [0.15, 0.3], # right hand
        [0.15, -0.3],# right foot
        [-0.15, 0.3],# left hand
        [-0.15, -0.3],# left foot
        [0.3, 0.1],  # right ankle
        [-0.3, 0.1]  # left ankle
    ])
    positions[0] = base_positions
    return positions

# Calculate new positions for each frame
def calculate_positions(positions):
    amplitude = 0.3
    frequency = 0.05
    t = np.linspace(0, 2 * np.pi, num_frames)
    for i in range(1, num_frames):
        positions[i] = positions[0]
        positions[i, :, 1] += amplitude * np.sin(frequency * t[i])
    
    # Adjust lower body for jumping with heavy weight
    positions[:, 2:6, 1] = positions[:, 2:6, 1] - amplitude * np.sin(frequency * t) * 0.5
    positions[:, 6:, 1] = positions[:, 6:, 1] - amplitude * np.sin(frequency * t) * 0.7
    return positions

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_axis_off()
points, = ax.plot([], [], 'wo', markersize=5)

positions = initialize_positions()
positions = calculate_positions(positions)

# Update function for animation
def update(frame):
    points.set_data(positions[frame, :, 0], positions[frame, :, 1])
    return points,

ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

plt.show()
