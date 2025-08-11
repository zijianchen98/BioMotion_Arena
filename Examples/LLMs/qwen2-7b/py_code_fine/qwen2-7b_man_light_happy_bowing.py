
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot( (autoscale_on=False, xlim=(-10, 10), ylim=(-10, 10), xticks=[], yticks=[])
line, = ax.plot([], [], lw=2)

def init():
    line([0], [0])
    return line,

def animate(i):
    x = np.linspace((-np.pi/2, np.pi/2)
    y = np.sin(x + i / 5)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)

plt.show()

