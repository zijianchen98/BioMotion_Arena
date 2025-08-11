
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

# Set the axes limits
ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))

# Create 15 point-lights
points, = ax.plot([], [], 'o', color='white')

# Initialize the point-lights
def init():
    points.set_data([], [])
    return points,

# Update the point-lights
def update(frame):
    x = np.linspace(0, 2, 15)
    y = np.sin(x + frame)
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                              init_func=init, blit=True)

# Show the animation
plt.show()
