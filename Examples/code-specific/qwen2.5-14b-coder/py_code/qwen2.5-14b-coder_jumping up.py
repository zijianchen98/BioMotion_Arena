
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_LIGHTS = 15
FRAME_RATE = 60
DURATION = 2  # seconds
FPS = FRAME_RATE
NUM_FRAMES = int(DURATION * FPS)

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create point lights
lights = [plt.scatter([], [], s=100, c='white') for _ in range(NUM_LIGHTS)]

# Define the motion of the jumping man
def get_jumping_positions(frame):
    t = frame / FPS
    x = np.linspace(0.4, 0.6, NUM_LIGHTS)
    y = np.sin(np.pi * t) ** 2 * np.linspace(0.2, 0.8, NUM_LIGHTS)
    return x, y

# Update function for animation
def update(frame):
    x, y = get_jumping_positions(frame)
    for light, xi, yi in zip(lights, x, y):
        light.set_offsets([xi, yi])
    return lights

# Create animation
ani = animation.FuncAnimation(fig, update, frames=NUM_FRAMES, blit=True, repeat=False)

# Show animation
plt.show()
