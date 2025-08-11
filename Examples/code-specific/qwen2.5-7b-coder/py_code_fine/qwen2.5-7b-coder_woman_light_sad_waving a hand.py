
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FPS = 30
DURATION = 5  # seconds
TIME_STEP = 1 / FPS
TOTAL_FRAMES = int(DURATION * FPS)

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create point lights
lights = [plt.Circle((np.random.uniform(-1, 1), np.random.uniform(-1, 1)), 0.02, color='white') for _ in range(NUM_LIGHTS)]
for light in lights:
    ax.add_artist(light)

# Animation function
def update(frame):
    for i, light in enumerate(lights):
        angle = frame * TIME_STEP * i * 0.1  # Adjust speed and direction
        x = np.cos(angle) * 0.8
        y = np.sin(angle) * 0.6
        light.center = (x, y)
    return lights

# Create animation
ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, blit=True)

# Show animation
plt.show()
