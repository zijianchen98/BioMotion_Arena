
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 60
light_radius = 0.2
jump_height = 1.0
jump_distance = 2.0
jump_duration = 1.0

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize light positions
lights = np.zeros((num_lights, 2))
for i in range(num_lights):
    lights[i, 0] = -1 + 2 * i / (num_lights - 1)
    lights[i, 1] = 0

# Initialize the scatter plot for the lights
scatter = ax.scatter(lights[:, 0], lights[:, 1], s=light_radius**2, c='white')

def update(frame):
    t = frame / (num_frames - 1)
    for i in range(num_lights):
        x = -1 + 2 * i / (num_lights - 1)
        y = jump_height * np.sin(t * np.pi)
        lights[i, 0] = x + (jump_distance * t)
        lights[i, 1] = y
    scatter.set_offsets(lights)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, num_frames, num_frames), interval=50, blit=True)

# Show the animation
plt.show()
