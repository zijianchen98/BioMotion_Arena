
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

# Set up the plot
ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))
ax.set_aspect('equal')

# Create a point light source
point, = ax.plot([], [], 'o', color='white')

# Create a solid black background
ax.set_facecolor('black')

# Create a sadman with heavy weight waving a hand
sadman, = ax.plot([], [], 'o', color='white')

# Animation function
def animate(i):
    x = np.sin(i)
    y = np.cos(i)
    point.set_data(x, y)
    sadman.set_data(x, y)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()
