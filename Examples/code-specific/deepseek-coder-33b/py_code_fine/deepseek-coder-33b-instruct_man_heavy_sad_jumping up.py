
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set up the figure
ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))
ax.set_aspect('equal')
ax.set_axis_off()

# Create 15 point-lights
points = ax.plot([], [], 'o', color='white')

# Initialize the point-lights
def init():
    for point in points:
        point.set_data([], [])
    return points

# Update the point-lights
def update(frame):
    x = np.linspace(0, 2, 15)
    y = np.sin(x + frame/10.0)
    for point, new_y in zip(points, y):
        point.set_data([1], [new_y])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

# Show the animation
plt.show()
