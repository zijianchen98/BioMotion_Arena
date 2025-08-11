
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

# Set up the plot
ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))
ax.set_aspect('equal')

# Create a point light source
point, = ax.plot([], [], 'o', color='white')

# Create a solid black background
ax.set_facecolor('black')

# Initialize the point light source
def init():
    point.set_data([], [])
    return point,

# Update the point light source
def update(i):
    x = 1 + np.sin(np.radians(i))
    y = 1 + np.cos(np.radians(i))
    point.set_data(x, y)
    return point,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=360, init_func=init, blit=True)

# Show the animation
plt.show()
