
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set up the figure
ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))
ax.set_aspect('equal')
ax.set_axis_off()

# Create 15 lights
lights = ax.plot([], [], 'o', color='white')

# Initialize the lights
def init():
    for light in lights:
        light.set_data([], [])
    return lights

# Update the lights
def update(frame):
    x = np.linspace(0, 2, 15)
    y = np.sin(x + frame/10.0)
    for i in range(len(lights)):
        lights[i].set_data(x[i], y[i])
    return lights

ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

plt.show()
