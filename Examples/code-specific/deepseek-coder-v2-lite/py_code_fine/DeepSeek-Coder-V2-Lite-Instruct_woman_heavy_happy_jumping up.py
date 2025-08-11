
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 30
light_radius = 0.2
jump_height = 1.0
jump_duration = 1.0

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize light positions
lights = np.zeros((num_lights, 2))
for i in range(num_lights):
    lights[i, 0] = np.cos(2 * np.pi * i / num_lights)
    lights[i, 1] = np.sin(2 * np.pi * i / num_lights)

# Initialize the scatter plot for the lights
scatter = ax.scatter([], [], s=light_radius*100, color='white')

def init():
    scatter.set_offsets(lights)
    return scatter,

def update(frame):
    t = frame / (num_frames - 1)
    for i in range(num_lights):
        lights[i, 1] = np.sin(t * np.pi) * jump_height + (1 - t) * (1 - jump_height)
    scatter.set_offsets(lights)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, num_frames), init_func=init,
                              interval=50, blit=True, repeat=True)

plt.show()
