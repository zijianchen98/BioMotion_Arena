
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sadman_jumping(n_frames=100):
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 8), ylim=(-3, 4))
    lineman = ax.scatter([], [], s=200, c='white')
    
    def init():
        ax.set_xlim(0, 8)
        ax.set_ylim(-3, 4)
        return theman,
    
    def animate(i):
        x = np.linspace(0, 8, 1000)
        y = -np.sin(x * np.pi / 4) + i / 10
        theman.set_offsets(np.c_[x, y])
        return theman,

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=n_frames, interval=20, blit=True)
    plt.show()

if __name__ == '__main__':
    sadman_jumping()
