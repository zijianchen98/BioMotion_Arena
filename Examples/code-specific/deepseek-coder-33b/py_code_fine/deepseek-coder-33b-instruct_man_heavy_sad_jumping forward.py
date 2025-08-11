
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

xdata, ydata = [], []

def animate(i):
    t = 0.1*i

    # x, y values to be plotted 
    x = np.sin(t)
    y = np.cos(t)

    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,

plt.plot([5, 5, 10, 10, 5], [5, 10, 10, 5, 5], 'k')
ani = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)

plt.show()
