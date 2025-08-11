
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_sittingdown(num):
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
    linelight, = ax.plot([], [], 'ro', ms=20)

    def init():
        thelight.set_data([], [])
        return thelight,

    def animate(i):
        x = [i/10, i/10 + 0.2, i/10 + 0.4, i/10 + 0.6, i/10 + 0.8]
        y = [np.sin(i/10), np.sin(i/10 + 0.2), np.sin(i/10 + 0.4), np.sin(i/10 + 0.6), np.sin(i/10 + 0.8)]
        thelight.set_data(x, y)
        return thelight,

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)
    plt.show()

animate_ssitdown(()
