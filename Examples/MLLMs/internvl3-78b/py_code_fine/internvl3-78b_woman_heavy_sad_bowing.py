
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setup the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_facecolor('black')

# Number of points
n_points = 15

# Create a list of points
points, = ax.plot([], [], 'wo')  # white points 'wo'

# Coordinates matrix
x = np.linspace(2, 18, n_points)
y = np.linspace(2, 18, n_points)
x, y = np.meshgrid(x, y)

# Update function for animation
def update(frame):
    # Define bowing motion
    t = frame / 100  # Time factor
    x_new = x + np.sin(t) * 2  # Horizontal sine wave movement
    y_new = y + np.cos(t) * 2  # Vertical cosine wave movement
    points.set_data(x_new扁平(), y_new扁平())
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
