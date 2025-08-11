
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot( (autoscale_on=False,
xlim=(-10,10), ylim=(-10,10))
ax.set_aspect('equal')
line, = ax.plot([], [], 'o', ms=20)

def init():
    line xdata, ydata
    line line.set_data(xdata, ydata)
    return line,

def animate(i):
    r = 2 * np.random.rand()
    theta = 2 * np.pi * np.random.rand()
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    xdata.append(x)
    ydata.append(y)
    if len(xdata) > 15:
        xdata = xdata[1:]
        ydata = ydata[1:]
    line set_data(xdata, ydata)
    return line,

anim = animation.FuncAnimation(fig, animate, frames=100, interval=20, blit=True, init_func=init)

plt.show()

