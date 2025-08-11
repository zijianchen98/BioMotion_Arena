
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

# Animation function
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    point.set_data(x, y)
    return point,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

# Show the animation
plt.show()
