
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Placeholder for loading BVH data
# In a real scenario, replace this with actual BVH loading and processing
# For example:
# from bvh import Bvh
# with open('jump_forward.bvh') as f:
#     mocap = Bvh(f)
# positions = [mocap.frame_joint_positions(frame) for frame in range(mocap.nframes)]
# Select 15 joints and extract their 3D positions

# For demonstration, use synthetic data
num_frames = 100
positions = [np.random.rand(15, 3) for _ in range(num_frames)]  # Replace with actual data

# Select x and y coordinates for 2D projection (assuming z is depth)
x_data = [pos[:, 0] for pos in positions]
y_data = [pos[:, 1] for pos in positions]

# Compute limits for the plot
x_min = min([np.min(x) for x in x_data])
x_max = max([np.max(x) for x in x_data])
y_min = min([np.min(y) for y in y_data])
y_max = max([np.max(y) for y in y_data])

# Set up the figure with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_aspect('equal')

# Create scatter plot for the point-lights
scatter = ax.scatter(x_data[0], y_data[0], c='white', s=50)

# Animation update function
def update(frame):
    scatter.set_offsets(np.c_[x_data[frame], y_data[frame]])
    return scatter,

# Create the animation with a slower speed to convey sadness
ani = FuncAnimation(fig, update, frames=len(positions), interval=100, blit=True)  # interval=100 ms for slower motion

plt.show()
