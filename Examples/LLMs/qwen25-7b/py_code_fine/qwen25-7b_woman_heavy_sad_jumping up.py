
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
FPS = 30  # Frames per second
DURATION = 5  # Duration in seconds
NUM_FRAMES = DURATION * FPS
JUMP_HEIGHT = 0  # Adjust this value to control the jump height

def update_point_light(frame):
    y = JUMP_HEIGHT * np.sin(2 * np.pi * frame / (DURATION * FPS))
    point_light.set_ydata(y)
    return point_light,

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 16)
ax.set_ylim(-1, 1)

# Add point lights
point_lights = [plt.scatter([i] * 15, [0] * 15, color='white', s=100, zorder=10)

# Animation function
ani = animation.FuncAnimation(fig, update_point_light, frames=range(NUM_FRAMES), interval=int(1000 / FPS), blit=True)

# Show or save the animation
plt.show()
