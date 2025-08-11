
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
fps = 30
duration = 3  # seconds
frames = int(fps * duration)

# Initial positions for a sitting person (simplified)
initial_positions = np.array([
    [0.0, 0.5],  # Head
    [-0.1, 0.4], # Left eye
    [0.1, 0.4],  # Right eye
    [0.0, 0.3],  # Nose
    [0.0, 0.2],  # Mouth
    [-0.2, 0.3], # Left shoulder
    [0.2, 0.3],  # Right shoulder
    [-0.3, 0.1], # Left elbow
    [0.3, 0.1],  # Right elbow
    [-0.3, -0.1],# Left wrist
    [0.3, -0.1], # Right wrist
    [0.0, 0.0],  # Hip
    [-0.2, -0.2],# Left knee
    [0.2, -0.2], # Right knee
    [0.0, -0.4]  # Feet
])

# Generate smooth movement paths for each light
paths = []
for i in range(num_lights):
    x = initial_positions[i, 0] + 0.1 * np.sin(np.linspace(0, 2 * np.pi, frames) + i * 0.5)
    y = initial_positions[i, 1] + 0.1 * np.cos(np.linspace(0, 2 * np.pi, frames) + i * 0.5)
    paths.append(np.column_stack((x, y)))

# Setup plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scat = ax.scatter([], [], s=100, c='white')

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    offsets = np.concatenate([path[frame].reshape(1, 2) for path in paths])
    scat.set_offsets(offsets)
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=1000/fps)

plt.show()
