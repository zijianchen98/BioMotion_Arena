
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Define the point-lights
point_lights = [
    {'x': 0.2, 'y': 0.2, 'z': 0.2},
    {'x': 0.4, 'y': 0.4, 'z': 0.4},
    {'x': 0.6, 'y': 0.6, 'z': 0.6},
    {'x': 0.8, 'y': 0.8, 'z': 0.8},
    {'x': 0.2, 'y': 0.2, 'z': 0.1},
    {'x': 0.4, 'y': 0.4, 'z': 0.1},
    {'x': 0.6, 'y': 0.6, 'z': 0.1},
    {'x': 0.8, 'y': 0.8, 'z': 0.1},
    {'x': 0.2, 'y': 0.2, 'z': 0.3},
    {'x': 0.4, 'y': 0.4, 'z': 0.3},
    {'x': 0.6, 'y': 0.6, 'z': 0.3},
    {'x': 0.8, 'y': 0.8, 'z': 0.3},
    {'x': 0.2, 'y': 0.2, 'z': 0.5},
    {'x': 0.4, 'y': 0.4, 'z': 0.5},
    {'x': 0.6, 'y': 0.6, 'z': 0.5},
    {'x': 0.8, 'y': 0.8, 'z': 0.5},
]

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_aspect('equal')
    
    for light in point_lights:
        x = light['x'] + np.sin(i/10) * 0.1
        y = light['y'] + np.cos(i/10) * 0.1
        z = light['z'] + np.sin(i/5) * 0.1
        ax.scatter(x, y, z, s=10, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
