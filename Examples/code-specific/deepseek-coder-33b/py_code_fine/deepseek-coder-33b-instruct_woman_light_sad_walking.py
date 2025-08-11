
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
def animate(i):
    x = i * 0.05
    y = np.sin(x)
    point.set_data(x, y)
    return point,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, blit=True)

# Show the animation
plt.show()
