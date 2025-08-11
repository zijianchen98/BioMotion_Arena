
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 100
fps = 30
background_color = 'black'
point_color = 'white'
figsize = (8, 6)

# Initial positions of the point lights for happyman in a jumping position
initial_positions = np.array([
    [0.0, 1.5],  # Head
    [-0.3, 1.2], # Left eye
    [0.3, 1.2],  # Right eye
    [0.0, 1.0],  # Nose
    [0.0, 0.8],  # Neck
    [-0.5, 0.6], # Left shoulder
    [0.5, 0.6],  # Right shoulder
    [-0.7, 0.4], # Left elbow
    [0.7, 0.4],  # Right elbow
    [-0.9, 0.2], # Left hand
    [0.9, 0.2],  # Right hand
    [0.0, 0.6],  # Chest
    [-0.5, 0.2], # Left hip
    [0.5, 0.2],  # Right hip
    [0.0, 0.0]   # Feet
])

# Function to animate the jumping motion
def jump(t):
    # Jump height
    h = 0.5
    # Jump frequency
    f = 0.5
    # Horizontal movement
    x_shift = 0.5 * np.sin(2 * np.pi * f * t / frames)
    # Vertical movement
    y_shift = h * np.sin(2 * np.pi * f * t / frames - np.pi / 2)
    return x_shift, y_shift

# Function to update the positions of the point lights
def update(frame):
    x_shift, y_shift = jump(frame)
    positions = initial_positions.copy()
    # Update positions based on the jump function
    positions[:, 0] += x_shift
    positions[:, 1] += y_shift
    sc.set_offsets(positions)
    return sc,

# Create figure and axis
fig, ax = plt.subplots(figsize=figsize)
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.axis('off')
ax.set_facecolor(background_color)

# Scatter plot for the point lights
sc = ax.scatter([], [], s=100, c=point_color)

# Animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

plt.show()
