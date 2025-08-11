
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 60
light_radius = 0.2
jump_height = 1.0
jump_duration = 3.0

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize light positions
lights = np.zeros((num_lights, 2))
for i in range(num_lights):
    lights[i, 0] = np.cos(2 * np.pi * i / num_lights)
    lights[i, 1] = np.sin(2 * np.pi * i / num_lights)

# Initialize the scatter plot for the lights
scatter = ax.scatter(lights[:, 0], lights[:, 1], s=light_radius**2, c='white')

def update(frame):
    t = frame / (num_frames - 1) * jump_duration
    for i in range(num_lights):
        lights[i, 1] = np.sin(t * np.pi) * jump_height * np.cos(2 * np.pi * t * (i / num_lights + 0.1))
    scatter.set_offsets(lights)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Display the animation
plt.show()
