
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot( (autoscale_on=False,
xlim=(-50, 100),
ylim=(-50, 100))

line, = ax.plot([], [], 'ro', ms=20)

def init():
    line xdata, ydata
    return line line,

def animate(i):
    xdata.append(i)
    ydata.append(i)
    line.set_data(xdata, ydata)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=np.linspace((-51, 99, 15),
                              interval=100, blit=True)

plt.show()

