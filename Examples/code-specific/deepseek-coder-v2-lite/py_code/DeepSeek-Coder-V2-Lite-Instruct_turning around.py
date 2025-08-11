
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
radius = 0.1
black_bg = (0, 0, 0)
white_light = (1, 1, 1)

# Initial positions
positions = np.zeros((num_lights, 2))
for i in range(num_lights):
    angle = 2 * np.pi * i / num_lights
    positions[i, 0] = np.cos(angle)
    positions[i, 1] = np.sin(angle)

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal', 'box')
ax.set_facecolor(black_bg)

# Initialize lights
lights, = ax.plot([], [], 'o', color=white_light, markersize=radius*50)

def init():
    lights.set_data([], [])
    return lights,

def update(frame):
    angle = 2 * np.pi * frame / 100
    for i in range(num_lights):
        positions[i, 0] = np.cos(angle + 2 * np.pi * i / num_lights)
        positions[i, 1] = np.sin(angle + 2 * np.pi * i / num_lights)
    lights.set_data(positions[:, 0], positions[:, 1])
    return lights,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 150, 1), init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
