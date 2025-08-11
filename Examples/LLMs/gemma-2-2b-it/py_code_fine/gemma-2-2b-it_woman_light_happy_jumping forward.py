
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
num_lights = 15
light_size = 0.1
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
    x = np.random.rand() * 2 - 1
    y = np.random.rand() * 2 - 1
    lights.append(
        [x, y, light_size]
    )

# Define the animation function
def animate(i):
    global lights
    for light in lights:
        light[0] += 0.01 * np.cos(i * 0.01)  # Simple sinusoidal movement
        light[1] += 0.01 * np.sin(i * 0.01)  # Simple sinusoidal movement
    
    # Update the plot
    ax.clear()
    ax.scatter(*[light for light in lights], s=light_size, c=light_color)
    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
