
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
num_lights = 15
light_radius = 0.1
light_color = (1, 1, 1)  # White color
background_color = (0, 0, 0)  # Black background

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor(background_color)

# Create the point lights
lights = []
for i in range(num_lights):
    x = np.random.uniform(-0.5, 0.5)
    y = np.random.uniform(-0.5, 0.5)
    lights.append(
        {'x': x, 'y': y, 'radius': light_radius, 'color': light_color}
    )

# Define the animation function
def animate(i):
    # Update the positions of the lights
    for light in lights:
        light['x'] += np.random.uniform(-0.01, 0.01)
        light['y'] += np.random.uniform(-0.01, 0.01)

    # Update the plot
    ax.clear()
    for light in lights:
        ax.plot(light['x'], light['y'], 'o', color=light['color'], markersize=light_radius)
    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
