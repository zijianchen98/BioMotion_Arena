
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_lights = 15
frame_duration = 50  # ms
total_frames = 100
background_color = 'black'
light_color = 'white'

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create point lights
lights = [plt.scatter([], [], s=50, color=light_color) for _ in range(num_lights)]

# Define forward rolling motion for a sad woman
def forward_rolling(t):
    x = np.linspace(0, 1, num_lights)
    y = np.sin(2 * np.pi * t + x * 10) / 10 + 0.5
    return x, y

# Update function for animation
def update(frame):
    t = frame / total_frames
    x, y = forward_rolling(t)
    for i in range(num_lights):
        lights[i].set_offsets(np.c_[x[i], y[i]])
    return lights

# Create animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=frame_duration, blit=True)

# Show animation
plt.show()
