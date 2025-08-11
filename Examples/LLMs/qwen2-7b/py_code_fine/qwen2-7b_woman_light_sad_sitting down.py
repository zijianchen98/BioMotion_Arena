
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot( (autoscale_on=False, xlim=(-10, 10), ylim=(-10, 10), xticks=[], yticks=[])
line, = ax.plot([], [], lw=2)

def init():
    line [-10, 10], [10], lw=2)
    return line,

def animate(i):
    theta = np.linspace( (0, 2*np.pi, 15)
    r = np.sin(np.cos(theta))
    x = r * np.cos(theta) + i / 50.
    y = r * np.sin(theta) + i / 50.

    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

plt.show()
