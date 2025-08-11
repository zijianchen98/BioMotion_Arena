
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bowing_animation():
    fig, ax = plt.subplots()
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.set_axis_off()
    
    points = [np.array((x, 2)) for x in np.linspace(0, 10, 15)]
    line, = ax.plot([], [], 'o', markersize=5, color='white')
    
    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        x = [point[0] + 0.02 * np.sin(2 * np.pi * frame * 1.5) for point in points]
        y = [point[1] for point in points]
        line.set_data(x, y)
        return line,

    ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), init_func=init, blit=True, interval=50, repeat=False)
    plt.show()

bowing_animation()
