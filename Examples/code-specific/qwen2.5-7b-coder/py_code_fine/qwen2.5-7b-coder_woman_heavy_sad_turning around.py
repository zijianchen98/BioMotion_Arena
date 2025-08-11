
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters
num_points = 15
frames = 60
weight_factor = 0.5

# Initialize the positions of the points
positions = np.zeros((frames, num_points, 2))
for t in range(frames):
    angle = 2 * np.pi * t / frames
    radius = 1 + weight_factor * np.sin(4 * angle)
    theta = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    x = radius * np.cos(theta + angle)
    y = radius * np.sin(theta + angle)
    positions[t] = np.column_stack((x, y))

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot
scat = ax.scatter(positions[0, :, 0], positions[0, :, 1], color='white')

# Update function for the animation
def update(frame):
    scat.set_offsets(positions[frame])
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Show the animation
plt.show()
