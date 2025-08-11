
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

# Set up the plot
ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))
ax.set_aspect('equal')

# Create a point light source
light_source, = ax.plot([], [], 'o', color='white')

# Create a line representing the path of the light source
path, = ax.plot([], [], '-', color='white')

# Initialize the light source and path
def init():
    light_source.set_data([], [])
    path.set_data([], [])
    return light_source, path,

# Update the light source and path
def update(num):
    x = np.linspace(0, 2, 1000)
    y = np.sin(x * num)
    light_source.set_data(x, y)
    path.set_data(x, y)
    return light_source, path,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 100),
                              init_func=init, blit=True)

# Show the animation
plt.show()
