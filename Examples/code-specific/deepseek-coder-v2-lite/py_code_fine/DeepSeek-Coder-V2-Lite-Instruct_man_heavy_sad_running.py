
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0, 1, num_lights)
positions[:, 1] = 0.5

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights
lights = []
for pos in positions:
    light = plt.Circle(pos, light_radius, color='white')
    lights.append(ax.add_patch(light))

def update(frame):
    # Update positions of the lights
    for i in range(num_lights):
        positions[i, 1] += 0.02 * (1 + 0.1 * np.sin(frame / 10 + i * 0.2))
        if positions[i, 1] > 1:
            positions[i, 1] = 0
        lights[i].center = positions[i]

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, repeat=True)

# Show the animation
plt.show()
