
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
FPS = 60
DURATION = 5  # seconds
FRAMES = FPS * DURATION
AMPLITUDE = 100  # Jump height in pixels
FREQUENCY = 1 / 2  # Frequency of jump cycle in Hz

# Time array
t = np.linspace(0, DURATION, FRAMES)

# Point lights positions
positions = {
    'head': (0, AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t)),
    'left_shoulder': (-40, AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t + np.pi / 2)),
    'right_shoulder': (40, AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t + np.pi / 2)),
    'left_elbow': (-80, AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t - np.pi / 2)),
    'right_elbow': (80, AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t - np.pi / 2)),
    'left_hand': (-120, AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t)),
    'right_hand': (120, AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t)),
    'left_hip': (-40, AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t - np.pi)),
    'right_hip': (40, AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t - np.pi)),
    'left_knee': (-80, AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t - 3 * np.pi / 2)),
    'right_knee': (80, AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t - 3 * np.pi / 2)),
    'left_foot': (-120, AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t - 2 * np.pi)),
    'right_foot': (120, AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t - 2 * np.pi)),
}

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-150, 150)
ax.set_ylim(-150, 150)
ax.axis('off')

# Scatter plot for point lights
scat = ax.scatter([], [], s=50, c='white')

def update(frame):
    x = [positions[key][0] for key in positions]
    y = [positions[key][1][frame] for key in positions]
    scat.set_offsets(np.c_[x, y])
    return scat,

# Animation
ani = FuncAnimation(fig, update, frames=FRAMES, interval=1000/FPS, blit=True)
plt.show()
