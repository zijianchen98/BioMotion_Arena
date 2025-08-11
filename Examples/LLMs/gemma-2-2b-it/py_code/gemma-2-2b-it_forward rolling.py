
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
num_lights = 15
light_size = 0.1  # Size of the light
light_color = (1, 1, 1)  # White color
light_speed = 0.05  # Speed of the lights
light_direction = np.array([0, 1, 0])  # Direction of the lights

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
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
        {'x': x, 'y': y, 'size': light_size, 'color': light_color, 'speed': light_speed, 'direction': light_direction}
    )

# Define the animation function
def animate(i):
    for light in lights:
        light['x'] += light['speed'] * light['direction']
        light['y'] += light['speed'] * light['direction']
    
    # Update the plot
    ax.clear()
    for light in lights:
        ax.plot(light['x'], light['y'], 'o', color=light['color'], markersize=light['size'])
    
    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
