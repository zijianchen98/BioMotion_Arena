
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.axis('off')

# Number of points
num_points = 15

# Initial positions of the points
positions = np.zeros((num_points, 2))
# Assign initial positions for a jumping forward motion
positions[0] = [-4, -2]  # left hip
positions[1] = [4, -2]   # right hip
positions[2] = [-6, 0]   # left knee
positions[3] = [6, 0]    # right knee
positions[4] = [-8, 2]   # left ankle
positions[5] = [8, 2]    # right ankle
positions[6] = [0, 4]    # pelvis
positions[7] = [-2, 6]   # left shoulder
positions[8] = [2, 6]    # right shoulder
positions[9] = [-4, 8]   # left elbow
positions[10] = [4, 8]   # right elbow
positions[11] = [-6, 10] # left hand
positions[12] = [6, 10]  # right hand
positions[13] = [0, 12]  # head
positions[14] = [0, 14]  # top of head

# Scatter plot for the points
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Define the jumping motion
def update(frame):
    t = frame / 30.0  # time in seconds
    freq = 1  # frequency of the jump
    amp = 2  # amplitude of the jump
    
    # Update y position for a jumping motion
    for i in range(num_points):
        positions[i, 1] = positions[i, 1] + amp * np.sin(2 * np.pi * freq * t)
    
    # Update x position for a forward motion
    for i in range(num_points):
        positions[i, 0] = positions[i, 0] + 0.1 * t
    
    scat.set_offsets(positions)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=30)

plt.show()
