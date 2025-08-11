
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))

# Create a point
point, = ax.plot([], [], 'o')

# Initialize the point
def init():
    point.set_data([], [])
    return point,

# Update the point position
def update(i):
    x = 1 + 0.1 * np.sin(np.radians(i))
    y = 0 + 0.1 * np.cos(np.radians(i))
    point.set_data(x, y)
    return point,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=360, init_func=init, blit=True)

# Show the animation
plt.show()
