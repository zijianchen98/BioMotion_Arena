
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set the axes limits
ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))

# Set the axes aspect ratio
ax.set_aspect('equal')

# Create 15 point-lights
points, = ax.plot([], [], 'o', color='white')

# Initialize the point-lights
def init():
    points.set_data([], [])
    return points,

# Update the point-lights
def update(num):
    x = np.linspace(0, 2, 15)
    y = np.sin(x + num/10.0)
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

# Show the animation
plt.show()
