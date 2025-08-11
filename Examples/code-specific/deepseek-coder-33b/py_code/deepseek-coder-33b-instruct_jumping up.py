
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set up the figure
ax.set_xlim([0, 10]), ax.set_ylim([0, 10])
ax.set_aspect('equal')
ax.set_axis_off()

# Create 15 point-lights
points, = ax.plot([], [], 'o', color='white')

# Initialize the point-lights
def init():
    points.set_data([], [])
    return points,

# Update the point-lights
def update(frame):
    x = np.linspace(0, 10, 15)
    y = np.sin(x - 0.1 * frame) + 5
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

# Show the animation
plt.show()
