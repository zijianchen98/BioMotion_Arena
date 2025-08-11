
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the coordinates of the 15 point lights
# These coordinates are placeholders and should be replaced with actual motion capture data
# This example demonstrates a simple up-and-down motion for illustration
num_points = 15
x = np.random.rand(num_points) * 2 - 1  # Initial x-coordinates
y = np.random.rand(num_points) * 2 - 1  # Initial y-coordinates

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot(x, y, 'wo', markersize=8)


# Animation update function
def animate(i):
    global x, y
    # Simulate movement by changing the y-coordinates over time.
    y += 0.05 * np.sin(i * 0.1 + np.arange(num_points))
    # Wrap around the top and bottom
    y = (y + 1.5) % 3 - 1.5
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# To save the animation as a gif:
# ani.save('point_light_animation.gif', writer='imagemagick', fps=20)

plt.show()

