
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
num_lights = 15
light_size = 0.1  # Size of the light
light_color = (1, 1, 1)  # White color
light_speed = 0.05  # Speed of the lights
time_step = 0.01  # Time step for animation

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the lights
lights = []
for i in range(num_lights):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    lights.append(
        {'x': x, 'y': y, 'size': light_size, 'color': light_color}
    )

# Define the animation function
def animate(i):
    global lights
    for light in lights:
        light['x'] += light_speed * np.cos(i * np.pi / num_lights)
        light['y'] += light_speed * np.sin(i * np.pi / num_lights)
    
    # Update the plot
    ax.clear()
    for light in lights:
        ax.plot(light['x'], light['y'], 'o', color=light['color'], markersize=light['size'])
    
    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=1000, interval=10, blit=True)

# Show the animation
plt.show()
