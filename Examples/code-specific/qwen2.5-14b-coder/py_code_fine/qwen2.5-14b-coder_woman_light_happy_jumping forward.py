
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_LIGHTS = 15
FPS = 30
DURATION = 2  # seconds
FRAMES = FPS * DURATION

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Create point lights
lights = []
for _ in range(NUM_LIGHTS):
    light, = ax.plot([], [], 'o', color='white', markersize=10)
    lights.append(light)

# Animation function
def animate(frame):
    t = frame / FPS
    for i, light in enumerate(lights):
        x = 2 + 4 * np.sin(2 * np.pi * (t + i * 0.2))
        y = 5 + 2 * np.sin(2 * np.pi * (t + i * 0.3))
        light.set_data(x, y)
    return lights

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=FRAMES, interval=1000/FPS, blit=True)

# Show animation
plt.show()
