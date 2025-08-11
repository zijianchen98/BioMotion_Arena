
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_points = 15
fps = 30
duration = 5  # in seconds
frames = fps * duration

# Point positions (x, y)
initial_positions = np.array([
    [0.5, 0.6], [0.4, 0.6], [0.6, 0.6],  # shoulders
    [0.4, 0.7], [0.6, 0.7],  # arms
    [0.5, 0.5], [0.45, 0.5], [0.55, 0.5],  # waist
    [0.4, 0.4], [0.6, 0.4],  # hips
    [0.35, 0.3], [0.45, 0.3], [0.55, 0.3], [0.65, 0.3],  # legs
    [0.4, 0.2], [0.6, 0.2]  # feet
])

# Amplitude and frequency for the jumping motion
amplitude = 0.1
frequency = 0.5

def update(frame):
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # Jumping motion
    y_offset = amplitude * np.sin(2 * np.pi * frequency * frame / fps)
    new_positions = initial_positions.copy()
    new_positions[:, 1] += y_offset
    
    # Forward motion
    x_offset = 0.005 * frame % 1  # move forward smoothly
    new_positions[:, 0] += x_offset
    
    ax.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=10)

fig, ax = plt.subplots(figsize=(5, 5))
ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=False)
plt.show()
