
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 60
light_radius = 0.2
jump_height = 1.0
jump_distance = 1.0
jump_duration = 1.0

# Initialize positions
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(-jump_distance, jump_distance, num_lights)
positions[:, 1] = -jump_height

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-jump_distance - 1, jump_distance + 1)
ax.set_ylim(-jump_height - 1, jump_height + 1)
ax.set_aspect('equal', 'box')
ax.set_facecolor('black')

# Initialize lights
lights = []
for i in range(num_lights):
    light = plt.Circle((positions[i, 0], positions[i, 1]), light_radius, color='white')
    lights.append(ax.add_patch(light))

def update(frame):
    t = frame / (num_frames - 1)
    for i in range(num_lights):
        x = positions[i, 0] + t * jump_distance
        y = positions[i, 1] + np.sin(t * np.pi) * jump_height
        lights[i].center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False, repeat=True)

# Show the animation
plt.show()
