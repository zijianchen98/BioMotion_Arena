
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
background_color = 'black'
light_color = 'white'
frames = 100
fps = 30

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 6), facecolor=background_color)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the point lights (simplified for demonstration)
initial_positions = np.array([
    [0.0, 0.8], [-0.2, 0.7], [0.2, 0.7], [-0.4, 0.6], [0.4, 0.6],
    [-0.6, 0.5], [0.6, 0.5], [0.0, 0.4], [-0.2, 0.3], [0.2, 0.3],
    [-0.4, 0.2], [0.4, 0.2], [0.0, 0.1], [-0.2, 0.0], [0.2, 0.0]
])

# Scatter plot for point lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color=light_color)

def update(frame):
    # Simple circular motion for demonstration; replace with more complex motion
    angle = 2 * np.pi * frame / frames
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    new_positions = initial_positions @ rotation_matrix.T
    scatter.set_offsets(new_positions)
    return scatter,

# Create animation
animation = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

plt.show()
