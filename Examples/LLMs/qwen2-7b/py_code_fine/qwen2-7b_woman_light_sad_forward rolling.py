
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_animation():
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 8), ylim=(-1, 1))
    lineight, = ax.plot([], [], lw=2)

    def init():
        theight.set_data([], [])
        return theight,

    def animate(i):
        x = np.linspace((0, 8, 1000)
        y = np.sin((i + x) ** 2)
        theight.set_data(x, y)
        return theight,

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
    plt.show()

create_animation()
