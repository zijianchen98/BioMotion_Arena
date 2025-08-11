
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
duration = 2  # seconds
fps = 30
frames = duration * fps

# Initial positions for the point-lights (happy woman with heavy weight)
positions = np.array([
    [0.5, 0.1], [0.4, 0.3], [0.6, 0.3],
    [0.3, 0.5], [0.5, 0.5], [0.7, 0.5],
    [0.4, 0.7], [0.6, 0.7],
    [0.5, 0.9], [0.45, 0.85], [0.55, 0.85],
    [0.4, 0.9], [0.6, 0.9],
    [0.35, 0.95], [0.65, 0.95]
])

# Generate animation frames
def update(frame):
    t = frame / fps
    # Update positions for simulating sitting down motion
    positions[:, 1] = positions[:, 1] + 0.01 * np.sin(2 * np.pi * t)
    scatter.set_offsets(positions)

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, repeat=False)

# Show the animation
plt.show()
