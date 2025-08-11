
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots()

ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))
ax.set_aspect('equal')
ax.set_axis_off()

# Create 15 point lights
points, = ax.plot([], [], 'o', color='white')

# Initialization function: plot the background of each frame
def init():
    ax.patch.set_facecolor('black')
    points.set_data([], [])
    return points,

# Animation function. This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 15)
    y = np.sin(x + i/10.0)
    points.set_data(x, y)
    return points,

# Call the animator. blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

plt.show()
