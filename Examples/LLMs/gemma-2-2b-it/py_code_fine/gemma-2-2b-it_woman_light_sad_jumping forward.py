
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
num_lights = 15
light_size = 0.1
light_color = (1, 1, 1)  # White color
light_speed = 0.05  # Speed of the lights
light_position = np.array([0, 0])  # Initial position of the lights

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the lights
lights = []
for i in range(num_lights):
    lights.append(plt.Circle((light_position[0], light_position[1]), light_size, color=light_color, fill=False))

# Create the animation
def animate(i):
    # Update the light positions
    for light in lights:
        light.center = light_position
        light.center = light_position + np.array([light_speed * np.cos(i * np.pi / num_lights),
                                                light_speed * np.sin(i * np.pi / num_lights)])
    return lights,

# Create the animation object
ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
