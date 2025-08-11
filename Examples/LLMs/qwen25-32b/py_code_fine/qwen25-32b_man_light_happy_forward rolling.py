
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
fps = 30
duration = 5  # seconds
frames = fps * duration

# Generate time array
t = np.linspace(0, duration, frames)

# Define the positions of the lights
def forward_roll_positions(t):
    positions = []
    for i in range(num_lights):
        theta = i / num_lights * 2 * np.pi
        x = np.cos(theta) * 5 * np.sin(t + i/num_lights)
        y = np.sin(theta) * 5 * np.sin(t + i/num_lights)
        z = 10 * np.sin(t + i/num_lights) - 5 * np.sin(2 * t + i/num_lights)
        positions.append((x, y, z))
    return np.array(positions)

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')  # Hide axes

# Scatter plot for the points
scat = ax.scatter([], [], color='white')

def update(frame):
    pos = forward_roll_positions(frame / fps)
    scat.set_offsets(pos[:, :2])
    return scat,

ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.show()
