
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 120
fps = 24
background_color = 'black'
light_color = 'white'

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_facecolor(background_color)
ax.axis('off')

# Initial positions of the lights (approximate for lying down pose)
initial_positions = np.array([
    [0.5, 0.8],  # Head
    [0.45, 0.7], # Left eye
    [0.55, 0.7], # Right eye
    [0.5, 0.65], # Nose
    [0.5, 0.5],  # Chest
    [0.45, 0.4], # Left shoulder
    [0.4, 0.3],  # Left elbow
    [0.35, 0.2], # Left wrist
    [0.55, 0.4], # Right shoulder
    [0.6, 0.3],  # Right elbow
    [0.65, 0.2], # Right wrist
    [0.5, 0.3],  # Hip
    [0.45, 0.2], # Left knee
    [0.4, 0.1],  # Left ankle
    [0.55, 0.2], # Right knee
    [0.6, 0.1]   # Right ankle
])

# Normalize positions
initial_positions[:, 0] /= max(initial_positions[:, 0])
initial_positions[:, 1] /= max(initial_positions[:, 1])

# Create scatter plot for lights
scat = ax.scatter([], [], s=100, color=light_color)

def init():
    scat.set_offsets([])
    return scat,

def animate(frame):
    t = frame / frames * 2 * np.pi
    # Simple sinusoidal movement to simulate breathing and slight body movements
    positions = initial_positions.copy()
    positions[:, 1] += 0.01 * np.sin(t + positions[:, 0] * 2 * np.pi)
    positions[:, 0] += 0.01 * np.cos(t + positions[:, 1] * 2 * np.pi)
    scat.set_offsets(positions)
    return scat,

# Create animation
ani = FuncAnimation(fig, animate, init_func=init, frames=frames, interval=1000/fps, blit=True)

plt.show()
