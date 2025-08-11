
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

# Initialize lights
lights = []
for i in range(num_lights):
    circle = plt.Circle((-1 + 2 * i / (num_lights - 1), -light_radius), light_radius, color='white')
    lights.append(circle)
    ax.add_artist(circle)

# Function to update the positions of the lights
def update(frame):
    t = frame / (num_frames - 1)
    for i, light in enumerate(lights):
        x = -1 + 2 * i / (num_lights - 1)
        y = -light_radius + (jump_height / 2) * np.sin(2 * np.pi * t / jump_duration)
        light.set_center((x, y))
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Display the animation
plt.show()
