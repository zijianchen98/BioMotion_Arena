
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and points
num_frames = 100
num_points = 15

# Define the initial positions of the points for a lying down human
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.3, 1.5], # Left shoulder
    [0.3, 1.5],  # Right shoulder
    [-0.6, 1.0], # Left elbow
    [0.6, 1.0],  # Right elbow
    [-0.9, 0.5], # Left wrist
    [0.9, 0.5],  # Right wrist
    [-0.1, 1.0], # Hip center
    [-0.4, 0.3], # Left hip
    [0.4, 0.3],  # Right hip
    [-0.7, -0.4],# Left knee
    [0.7, -0.4], # Right knee
    [-1.0, -1.0],# Left ankle
    [1.0, -1.0], # Right ankle
    [0.0, -1.5]  # Foot center
])

# Define the range of motion for each point
motion_range = np.array([
    [0.05, 0.05], # Head
    [0.1, 0.1],   # Left shoulder
    [0.1, 0.1],   # Right shoulder
    [0.2, 0.2],   # Left elbow
    [0.2, 0.2],   # Right elbow
    [0.3, 0.3],   # Left wrist
    [0.3, 0.3],   # Right wrist
    [0.1, 0.1],   # Hip center
    [0.1, 0.1],   # Left hip
    [0.1, 0.1],   # Right hip
    [0.2, 0.2],   # Left knee
    [0.2, 0.2],   # Right knee
    [0.3, 0.3],   # Left ankle
    [0.3, 0.3],   # Right ankle
    [0.1, 0.1]    # Foot center
])

# Generate random motion for each point
motion = np.random.uniform(-motion_range, motion_range, size=(num_points, num_frames, 2))

# Accumulate the motion to the initial positions
positions = initial_positions[:, np.newaxis, :] + np.cumsum(motion, axis=1)

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 3)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot
scat = ax.scatter([], [], s=20, c='white')

# Define the animation function
def animate(i):
    x = positions[:, i, 0]
    y = positions[:, i, 1]
    scat.set_offsets(np.c_[x, y])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
