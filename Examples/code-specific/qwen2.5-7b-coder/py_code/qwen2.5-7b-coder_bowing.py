
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and frames
num_points = 15
frames = 60

# Initialize the positions of the points
positions = np.zeros((frames, num_points, 2))
for i in range(num_points):
    start_angle = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    radius = 0.5 + 0.2 * np.random.rand()
    x = radius * np.cos(start_angle + i * (np.pi / num_points))
    y = radius * np.sin(start_angle + i * (np.pi / num_points))
    positions[:, i, 0] = x
    positions[:, i, 1] = y

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot
scatter = ax.scatter(positions[0, :, 0], positions[0, :, 1], color='white')

def update(frame):
    scatter.set_offsets(positions[frame])
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Show the animation
plt.show()
