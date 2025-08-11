
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FRAMES = 60
FPS = 30

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')
ax.set_aspect('equal')

# Create point lights
lights = [plt.scatter([], [], s=100, color='white') for _ in range(NUM_LIGHTS)]

# Sad woman jumping up motion model
def get_light_positions(frame):
    t = frame / FPS
    positions = []
    for i in range(NUM_LIGHTS):
        # Simple harmonic motion for vertical position
        y = np.sin(2 * np.pi * (t + i / NUM_LIGHTS)) * 0.5
        # Distribute lights horizontally
        x = np.cos(2 * np.pi * (t + i / NUM_LIGHTS)) * 0.5
        positions.append((x, y))
    return positions

# Update function for animation
def update(frame):
    positions = get_light_positions(frame)
    for light, (x, y) in zip(lights, positions):
        light.set_offsets([x, y])
    return lights

# Create animation
ani = FuncAnimation(fig, update, frames=FRAMES, blit=True, interval=1000/FPS)

# Show animation
plt.show()
