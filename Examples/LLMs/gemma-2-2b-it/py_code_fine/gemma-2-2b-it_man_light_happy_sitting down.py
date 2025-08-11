
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
num_lights = 15
light_radius = 0.1
light_color = (1, 1, 1)  # White color
background_color = (0, 0, 0)  # Black background
light_positions = np.random.rand(num_lights, 2)  # Random initial positions
light_speed = 0.05  # Speed of the lights

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor(background_color)

# Create the lights
lights = []
for i in range(num_lights):
    light = plt.Circle((light_positions[i, 0], light_positions[i, 1]), light_radius, color=light_color, fill=False)
    lights.append(light)

# Create the animation
def animate(i):
    for light in lights:
        light.center = light_positions[i]
    return lights,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
