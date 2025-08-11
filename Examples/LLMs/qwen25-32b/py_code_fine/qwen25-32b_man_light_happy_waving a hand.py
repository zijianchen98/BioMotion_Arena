
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_points = 15
fps = 30
duration = 5  # seconds
frames = fps * duration

# Define initial positions of the point-lights
positions = np.zeros((num_points, 2))

# Define the wave motion parameters
amplitude = 0.2
frequency = 0.5
phase_shifts = np.linspace(0, np.pi * 2, num_points)

# Function to update the positions of the point-lights
def update_positions(frame):
    t = frame / fps
    for i in range(num_points):
        if i < 5:
            positions[i] = [np.sin(frequency * t + phase_shifts[i]) * amplitude, np.cos(frequency * t + phase_shifts[i]) * amplitude]
        elif i >= 5 and i < 10:
            positions[i] = [0.5 + np.sin(frequency * t + phase_shifts[i]) * amplitude, -0.5 + np.cos(frequency * t + phase_shifts[i]) * amplitude]
        else:
            positions[i] = [-0.5 + np.sin(frequency * t + phase_shifts[i]) * amplitude, -0.5 + np.cos(frequency * t + phase_shifts[i]) * amplitude]

# Setup plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white')

# Animation function
def animate(frame):
    update_positions(frame)
    scat.set_offsets(positions)

# Create animation
ani = FuncAnimation(fig, animate, frames=frames, interval=1000/fps, repeat=False)

plt.show()
