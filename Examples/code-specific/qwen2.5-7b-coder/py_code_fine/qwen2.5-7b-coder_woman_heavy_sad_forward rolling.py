
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames and points
num_frames = 60
num_points = 15

# Initialize the positions of the points
positions = np.zeros((num_frames, num_points, 2))
for i in range(num_points):
    start_x = np.random.uniform(-1, 1)
    start_y = np.random.uniform(-1, 1)
    end_x = np.linspace(start_x, -1 if start_x > 0 else 1, num_frames)
    end_y = np.linspace(start_y, -1 if start_y > 0 else 1, num_frames)
    positions[:, i] = np.vstack((end_x, end_y)).T

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot
scatter = ax.scatter([], [], color='white', s=50)

def update(frame):
    scatter.set_offsets(positions[frame])
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=100, blit=True)

plt.show()
