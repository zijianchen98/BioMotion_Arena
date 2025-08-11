
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set up the plot
ax.set_xlim([0, 10]), ax.set_ylim([0, 10])
ax.set_aspect('equal')
ax.set_axis_off()

# Create 15 point-lights
points, = ax.plot([], [], 'o', color='white')

# Define the initial positions of the point-lights
x = np.linspace(1, 9, 15)
y = np.ones_like(x) * 5

# Define the motion of the point-lights
def update(num):
    global x, y
    x += np.random.normal(0, 0.1, x.shape)
    y += np.random.normal(0, 0.1, y.shape)
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
