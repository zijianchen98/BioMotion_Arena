
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
    light, = ax.plot([], [], 'o', color='white', markersize=5)
    lights.append(light)

# Sadman jumping forward function
def sadman_jump(t):
    # Simple harmonic motion for jumping
    height = 2 * np.sin(np.pi * t / DURATION)
    
    # Linear motion for forward jump
    x = np.linspace(0, 8, NUM_LIGHTS)
    y = np.full_like(x, height)
    
    return x, y

# Animation update function
def update(frame):
    t = frame / FPS
    x, y = sadman_jump(t)
    
    for i, light in enumerate(lights):
        light.set_data([x[i]], [y[i]])
    
    return lights

# Create animation
ani = FuncAnimation(fig, update, frames=FRAMES, interval=1000/FPS, blit=True)

# Show animation
plt.show()
