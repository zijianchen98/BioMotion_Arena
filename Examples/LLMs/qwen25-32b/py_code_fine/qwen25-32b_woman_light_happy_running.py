
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
fps = 30
duration_seconds = 10
frames = fps * duration_seconds

# Initial positions of the lights
positions = np.zeros((frames, num_lights, 2))

def update_positions(frame):
    t = frame / fps  # time in seconds
    phase = t * 2 * np.pi  # phase angle
    
    # Define the positions of the lights based on the running motion
    positions[frame] = [
        [np.sin(t * 2 + i * 0.1), np.cos(t * 2 + i * 0.1)]  # Head
        if i == 0 else
        [np.sin(t * 2 + (i-1) * 0.1 + phase), np.cos(t * 2 + (i-1) * 0.1 + phase) - 1.5]  # Body
        if i == 1 else
        [np.sin(t * 2 + (i-2) * 0.1 + phase), np.cos(t * 2 + (i-2) * 0.1 + phase) - 2.0]  # Arms
        if i <= 4 else
        [np.sin(t * 2 + (i-5) * 0.1 + phase), np.cos(t * 2 + (i-5) * 0.1 + phase) - 2.5]  # Legs
        for i in range(num_lights)
    ]

# Update positions for each frame
for frame in range(frames):
    update_positions(frame)

# Setup plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide axes

dots, = ax.plot([], [], 'wo', markersize=10)

def init():
    dots.set_data([], [])
    return dots,

def animate(i):
    x = positions[i][:, 0]
    y = positions[i][:, 1]
    dots.set_data(x, y)
    return dots,

# Create animation
anim = FuncAnimation(fig, animate, init_func=init,
                     frames=frames, interval=1000/fps, blit=True)

plt.show()
