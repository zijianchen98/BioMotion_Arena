
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
num_lights = 15
light_radius = 0.1
light_color = 'white'
background_color = 'black'

# Create a figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor(background_color)

# Create the point lights
lights = []
for i in range(num_lights):
    x = np.random.uniform(-0.5, 0.5)
    y = np.random.uniform(-0.5, 0.5)
    lights.append(plt.Circle((x, y), light_radius, color=light_color, fill=False))

# Create the animation
def animate(i):
    for light in lights:
        light.center = (np.sin(i * 0.1) * 0.5 + 0.5, np.cos(i * 0.1) * 0.5 + 0.5)
    return lights,

# Create the animation object
ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
